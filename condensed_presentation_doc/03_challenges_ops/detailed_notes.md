# **Ghi Chú Chi Tiết: Thách Thức & Giải Pháp Thực Tế**

> *Tài liệu này đi sâu vào từng giải pháp kỹ thuật với ví dụ code cụ thể — dùng như tài liệu tham khảo kỹ thuật sau workshop.*

---

## **1. Độ Tin Cậy & Ảo Tưởng (Reliability & Hallucinations)**

Hệ thống tác nhân có đặc điểm lỗi khác hoàn toàn so với LLM đơn lượt: lỗi trung gian lan truyền qua nhiều bước, hành động gọi API không thể đảo ngược, và sai số tích lũy theo từng giai đoạn.

### **Giải pháp 1: Ép Buộc Cấu Trúc Đầu Ra (Structured Outputs)**
Dùng Pydantic để ràng buộc cấu trúc đầu ra ở mức độ giải mã của mô hình:

```python
from pydantic import BaseModel, Field
from openai import OpenAI

class Invoice(BaseModel):
    vendor: str = Field(min_length=1)
    amount: float = Field(gt=0)
    date: str = Field(pattern=r"\d{4}-\d{2}-\d{2}")

client = OpenAI()
completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[...],
    response_format=Invoice
)
invoice = completion.choices[0].message.parsed
```

### **Giải pháp 2: Cổng Xác Thực Hai Lớp**
- **Lớp 1 — Xác thực cú pháp:** Kiểm tra cấu trúc schema Pydantic.
- **Lớp 2 — Đối chiếu ngữ nghĩa (Grounding):** Kiểm tra chéo với index cơ sở dữ liệu nội bộ (Trie/Bloom filter) để loại bỏ thực thể ảo tưởng.

### **Giải pháp 3: Vòng Lặp Tự Sửa Lỗi Theo Ngữ Cảnh**
Khi validation thất bại, gửi phản hồi lỗi cụ thể để tác nhân tự chỉnh sửa — thay vì reset hoàn toàn:

```python
for attempt in range(3):
    try:
        result = structured_llm.invoke(prompt + correction_hint)
        validate_syntactic(result)
        validate_semantic(result)
        break
    except ValidationError as e:
        correction_hint = f"Previous error: {e}. Provide only valid JSON matching the schema."
else:
    save_to_human_review_queue(context)
```

### **Giải pháp 4: Human-in-the-Loop (HITL)**
Khi tự sửa lỗi thất bại sau 3 lần: dừng tiến trình, serialize trạng thái phiên làm việc, hiển thị lên UI kiểm duyệt. Người vận hành kiểm tra, sửa thủ công và nhấn Resume để tiếp tục từ điểm dừng.

---

## **2. Đánh Giá Hệ Thống Tác Nhân (Evaluation)**

Benchmark truyền thống chỉ đo kết quả cuối — không đủ cho hệ thống tác nhân, nơi **cách đạt được kết quả** cũng quan trọng không kém bản thân kết quả.

### **Sáu Chiều Kích Đánh Giá**

| Chiều kích | Câu hỏi đánh giá | Ví dụ thực tế |
|---|---|---|
| **Hiệu quả số bước** | Agent có dùng số bước tối thiểu cần thiết không? | Trích xuất hóa đơn trong dưới 5 lần lặp, không gọi công cụ dư thừa. |
| **Chất lượng kế hoạch** | Kế hoạch ban đầu có hợp lý và khả thi không? | Kế hoạch kiểm toán có nằm trong ngân sách mục tiêu không? |
| **Khả năng phục hồi** | Agent xử lý lỗi phát sinh tốt như thế nào? | Có phục hồi từ lỗi timeout database tạm thời không? |
| **Lựa chọn công cụ** | Có dùng đúng công cụ cho đúng tác vụ không? | Có truy vấn đúng cơ sở dữ liệu giao dịch khách hàng không? |
| **Tuân thủ an toàn** | Các rào chắn bảo mật có được tôn trọng không? | Có redact PII trước khi xuất kết quả không? |
| **Hiệu quả chi phí** | Định tuyến mô hình có tối ưu không? | Có định tuyến các bước cấp thấp sang mô hình rẻ hơn không? |

### **Phương Pháp Đánh Giá**

**Trajectory Eval & LLM-as-a-Judge:**
```python
def evaluate_with_judge(trajectory: dict, rubric: str) -> int:
    prompt = f"You are a Factuality Judge. Grade this trajectory on a 1-5 scale.\nRubric: {rubric}\nTrajectory: {trajectory}"
    response = llm.invoke(prompt)
    return extract_score(response)
```

**Bộ kịch bản chuẩn (Golden Trajectory Suite):** Xây dựng hơn 200 kịch bản mẫu để chạy kiểm thử hồi quy tự động trong CI/CD — phát hiện sớm khi thay đổi prompt hoặc model làm suy giảm chất lượng.

**Ràng buộc bất biến (Invariants):** Assert các quy tắc nghiệp vụ cứng:
```python
assert total_amount == sum(item.amount for item in line_items)
```

**Khoảng cách ngữ nghĩa:** Dùng embeddings so sánh độ tương đồng giữa đầu ra sinh ra và tài liệu chính sách/quy định chính thức.

---

## **3. Chi Phí & Độ Trễ (Cost & Latency)**

Nguyên nhân cốt lõi: tác nhân tiêu tốn lượng token lớn do vòng lặp suy luận lặp lại và cửa sổ ngữ cảnh mở rộng theo thời gian.

### **Giải Pháp 1: Định Tuyến Phân Tầng**
```python
class TieredRouter:
    def route(self, task: str) -> str:
        if any(kw in task for kw in ["plan", "strategy", "reason"]):
            return "claude-4.6-sonnet"   # Frontier: lập kế hoạch phức tạp
        elif any(kw in task for kw in ["extract", "parse"]):
            return "gpt-4o-mini"         # Synthesis: tổng hợp trung gian
        else:
            return "llama-3.3-70b"       # Utility: định dạng, phân loại (giảm 70% chi phí)
```

### **Giải Pháp 2: Tối Ưu Prompt Caching**
Đặt các prompts hệ thống cố định ở **đầu ngữ cảnh** — phần này sẽ được cache và tái sử dụng qua các lần gọi, tiết kiệm đến **80% chi phí token đầu vào**.

### **Giải Pháp 3: Thu Gọn Ngữ Cảnh (Context Pruning)**
Dùng RAG dense-sparse để giới hạn ngữ cảnh dưới 10k tokens — chỉ đưa vào những thông tin thực sự cần thiết cho bước hiện tại.

### **Giải Pháp 4: Song Song Hóa Bất Đồng Bộ**
Chạy song song các giai đoạn độc lập bằng `asyncio.gather()` — giảm độ trễ tổng thể đến **45%**.

---

## **4. Khả Năng Giám Sát & AgentOps (Observability)**

Nhật ký hệ thống truyền thống không ghi nhận được luồng suy luận bằng ngôn ngữ tự nhiên — khi lỗi xảy ra, không biết tác nhân đang "nghĩ" gì.

### **Giải Pháp 1: Semantic Tracing**
```python
import mlflow
mlflow.langchain.autolog()

with mlflow.start_run(run_name="agent_trace"):
    result = agent.invoke("Analyze this contract")
```
Ghi đầy đủ: span name, inputs, outputs, token count, latency cho mỗi lần gọi LLM/tool.

### **Giải Pháp 2: Bảng Điều Khiển Cây Thực Thi**
Trực quan hóa cấu trúc cuộc gọi lồng nhau (call tree) để khoanh vùng chính xác nơi xảy ra lỗi trong chuỗi thực thi dài.

### **Giải Pháp 3: Offline Replay Sandbox**
Trích xuất trajectory lỗi từ production và phát lại trong sandbox cô lập — thử nghiệm các cách sửa prompt/skills mà không ảnh hưởng đến môi trường thực.

### **Giải Pháp 4: Real-time Guardrails**
Dùng **Llama Guard** tại cổng input/output của mỗi công cụ để ngăn prompt injection và vi phạm an toàn thông tin theo thời gian thực.

---

## **Tổng Hợp: Kiến Trúc Hệ Thống Tác Nhân Production**

| Lớp | Triển Khai Thực Tế |
|---|---|
| **Orchestration** | Máy trạng thái hữu hạn tùy chỉnh, đảm bảo luồng dữ liệu ổn định 100% |
| **Reasoning Core** | Định tuyến ngữ nghĩa lai → Claude 4.6 Sonnet / DeepSeek-R1 (lập luận) & Llama 3.3 70B / Gemini 2.5 Flash (tiện ích) |
| **Skills** | Module độc lập cho Trích xuất dữ liệu, Kiểm toán tuân thủ, Sinh báo cáo |
| **Tools & Protocols** | Filesystem/database qua MCP; giao dịch tự động qua AP2 |
| **Memory** | Vector DB cho bộ nhớ ngữ nghĩa dài hạn; episodic memory cho trạng thái phiên ngắn hạn |
| **Cognitive Loop** | PLAN → ACT → OBSERVE → REFLECT tại mỗi ranh giới giai đoạn |

---

## **Danh Sách Kiểm Tra Kỹ Thuật (Take-home Checklist)**
- [ ] Structured output (Pydantic) + xác thực hai lớp (cú pháp & ngữ nghĩa)
- [ ] Vòng lặp tự sửa lỗi tối đa 3 lần → escalate HITL nếu vẫn thất bại
- [ ] Trajectory logging + LLM-as-judge trong CI/CD pipeline
- [ ] Định tuyến phân tầng (tiered routing) + prompt caching cho prompts tĩnh
- [ ] `asyncio.gather()` cho các tác vụ song song độc lập
- [ ] MLflow tracing cho mỗi lượt chạy agent
- [ ] Replay sandbox cho các trajectory lỗi
- [ ] Guardrails (Llama Guard) tại cổng input/output công cụ
