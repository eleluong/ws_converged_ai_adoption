# Workshop — Tài Liệu Ghi Chú Chi Tiết
## Các Thách Thức Kéo Dài Trong Agentic AI (Persistent Challenges)

> Các ghi chú này cung cấp thông tin chi tiết nâng cao, các phân tích đánh đổi và các giải pháp thiết kế thực tế cho hệ thống tác nhân doanh nghiệp nói chung.

---

### Phần 3.1: Độ Tin Cậy & Ảo Tưởng (Reliability & Hallucinations)

**Tại sao độ tin cậy của các tác nhân (agents) lại khó đảm bảo hơn so với LLM đơn lẻ:**  
Một phản hồi của LLM đơn lẻ, ngay cả khi không hoàn hảo, thường thất bại một cách nhẹ nhàng (gracefully) — người dùng thấy câu trả lời tệ và thử lại. Nhưng lỗi của tác nhân (agent) sẽ dẫn đến hậu quả nghiêm trọng hơn:  
- Các lỗi trung gian có thể lan truyền qua một đường ống xử lý (pipeline) nhiều bước.  
- Các hành động thực hiện (gọi API, ghi tệp, gửi tin nhắn) có thể không đảo ngược được.  
- Tác nhân có thể không phát hiện ra mình đã thất bại (ảo tưởng về sự thành công - hallucinated success).  
- Lỗi tích lũy: một sai số nhỏ ở bước 3 có thể biểu hiện thành một thảm họa nghiêm trọng ở bước 12.  

**🎯 Workshop hook – Trực quan hóa nhật ký lỗi thực tế (2 phút):**  
Trình bày vết thực thi (trace) đã được ẩn danh này và đặt câu hỏi: *“Tác nhân đã đi sai ở đâu? Nguyên nhân gốc rễ là gì?”*
```
Bước 1: LLM output → {"vendor": "Amaz0n", "amount": "four thousand", "date": "2025-02-30"}
Bước 2: Parser → gặp lỗi crash do số thực float không hợp lệ
Bước 3: Agent retries without context → tạo ra {"vendor": "Amazon", "amount": 4000, "date": "2025-02-30"}
Bước 4: Writes to CSV → ghi vào CSV thất bại do ngày 30/02/2025 không tồn tại
Bước 5: Agent reports “Successfully wrote invoice” → ảo tưởng thành công
```

**Cách các hệ thống thực tế giải quyết bài toán độ tin cậy:**  
Các kiến trúc sản xuất (production) giảm thiểu thách thức về độ tin cậy bằng cách sử dụng chiến lược xác thực và phục hồi nhiều lớp:

1. **Ép buộc sinh định dạng JSON (Structured Outputs):**  
   Thay vì phân tích cú pháp văn bản thô sau khi suy luận, các nền tảng thực tế ép buộc định dạng đầu ra JSON nghiêm ngặt ngay tại cấp độ giải mã (decoding level). Sử dụng phương pháp giải mã bị ràng buộc bởi schema (thông qua JSON schema cấp hệ thống và các API được hỗ trợ bởi Claude 4.6 Sonnet), lõi lập luận (reasoning core) được ngăn chặn về mặt cấu trúc để không tạo ra các khóa JSON không hợp lệ hoặc lỗi cú pháp.

   **✋ Code snippet – Ép buộc đầu ra có cấu trúc bằng Pydantic:**
   ```python
   from pydantic import BaseModel, Field, ValidationError
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

2. **Cổng xác thực hai lớp (Two-Tier Validation Gate):**  
   - *Xác thực cú pháp (Syntactic Validation):* Các nền tảng đưa đầu ra qua một cổng schema Pydantic nghiêm ngặt để xác thực kiểu dữ liệu, phạm vi và mối quan hệ đối tượng ngay sau khi hoàn thành.  
   - *Cổng đối chiếu ngữ nghĩa (Semantic Grounding Gate):* Để ngăn tác nhân ảo tưởng ra các thực thể miền (domain entities), các phần tử được trích xuất sẽ được xác thực đối chiếu với chỉ mục siêu dữ liệu miền cục bộ (Domain Metadata Index - được hỗ trợ bởi cấu trúc dữ liệu Trie/Bloom filter).

   **🧠 Bài tập Workshop (10 phút):**  
   Triển khai cổng xác thực ngữ nghĩa: cho trước tập hợp các nhà cung cấp được phép `allowed_vendors = {"amazon", "walmart", "costco"}`, từ chối bất kỳ nhà cung cấp nào được trích xuất không nằm trong tập hợp này (không phân biệt chữ hoa chữ thường, cho phép khớp mờ - fuzzy match) và ném ra lỗi `ValidationError`.

3. **Vòng lặp tự sửa lỗi theo ngữ cảnh (Contextual Self-Correction / Diff-Based Reflection):**  
   Nếu xác thực thất bại, bộ điều phối (orchestrator) sẽ kích hoạt một vòng lặp tự sửa sai. Thay vì chỉ gửi một thông báo lỗi thô, nó xây dựng một prompt có cấu trúc chứa đoạn dữ liệu vi phạm, ràng buộc cụ thể bị phá vỡ, một bản so sánh khác biệt ngữ nghĩa (semantic diff) của kết quả mong đợi và các hướng dẫn khắc phục lỗi.

   **✋ Code pattern – Tự sửa sai với số lần thử tối đa:**
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
       # chuyển giao sang HITL
       save_to_human_review_queue(context)
   ```

4. **Giao diện phân loại có sự can thiệp của con người (Human-in-the-Loop - HITL):**  
   Nếu quá trình tự sửa lỗi thất bại sau 3 lần, tiến trình sẽ tạm dừng, bộ điều phối tuần tự hóa (serialize) trạng thái hoạt động hiện tại và kích hoạt cảnh báo phân loại. Người vận hành có thể xem xét điểm không khớp bị gắn cờ thông qua giao diện trực quan UI, chỉnh sửa dữ liệu thủ công và nhấn "Resume" để tiếp tục máy trạng thái một cách liền mạch mà không cần khởi động lại toàn bộ pipeline.

   **💬 Câu hỏi thảo luận:** *Khi nào bạn KHÔNG muốn áp dụng HITL? (ví dụ: giao dịch thời gian thực - real-time trading, xử lý hàng loạt thông lượng cao - high-throughput batch nơi sự chậm trễ của con người là không thể chấp nhận được)*

---

### Phần 3.2: Đánh Giá (Evaluation)

**Bài toán đánh giá quỹ đạo (Trajectory Evaluation):**  
Các phương pháp đánh giá LLM truyền thống thường so sánh câu trả lời được sinh ra với câu trả lời chuẩn (reference answer). Đánh giá tác nhân yêu cầu đánh giá toàn bộ quỹ đạo thực thi (trajectory) — mọi bước đi mà tác nhân đã thực hiện, chứ không chỉ là câu trả lời cuối cùng.

**Các chiều kích đánh giá quỹ đạo:**

| Chiều kích | Nội dung đo lường | Ví dụ thực tế |
|---|---|---|
| **Hiệu quả số bước** (Efficiency) | Số bước thực hiện so với mức tối thiểu | Agent có trích xuất hóa đơn trong dưới 5 lần lặp và không gọi công cụ dư thừa không? |
| **Chất lượng kế hoạch** (Planning quality) | Kế hoạch ban đầu có hợp lý không? | Kế hoạch kiểm toán có nằm trong ngân sách mục tiêu và phân bổ tài nguyên hợp lý không? |
| **Khả năng phục hồi** (Recovery quality) | Agent xử lý các lỗi phát sinh tốt như thế nào? | Agent có phục hồi được từ các lỗi hết thời gian chờ database tạm thời không? |
| **Lựa chọn công cụ** (Tool selection) | Các công cụ chính xác có được sử dụng không? | Agent có truy vấn đúng cơ sở dữ liệu giao dịch khách hàng của năm chính xác không? |
| **Tuân thủ an toàn** (Safety compliance) | Các rào chắn bảo mật có được tôn trọng không? | Agent có ẩn/redact các thông tin PII và dữ liệu nhạy cảm một cách chính xác trước khi xuất kết quả không? |
| **Hiệu quả chi phí** (Cost efficiency) | Chi phí token và API cho tác vụ | Hệ thống định tuyến mô hình có định tuyến chính xác các bước cấp thấp đến các tầng mô hình rẻ hơn không? |

**🎯 Case study Workshop (15 phút):**  
Cung cấp một nhật ký quỹ đạo đã được ẩn danh (10 bước). Theo cặp, mỗi nhóm đánh giá **một chiều kích** (ví dụ: hiệu quả số bước, lựa chọn công cụ) và đưa ra điểm số từ 1-5 kèm theo lý giải. Chia sẻ kết quả – cả lớp sẽ thấy tác nhân gần như đã thành công nhưng lại không hiệu quả/không an toàn như thế nào.

**Cách các hệ thống thực tế triển khai đánh giá:**  
Các hệ thống doanh nghiệp tiến xa hơn việc đánh giá thủ công bằng cách thiết lập một khung đánh giá tự động bằng lập trình:

1. **Hội đồng giám khảo LLM đa tiêu chí (Khung G-Eval):**  
   Đường ống sản xuất triển khai một ban giám khảo gồm các prompt đánh giá độc lập, chuyên biệt chạy trên Claude 4.6 Sonnet (ví dụ: Trọng tài Chính sách, Trọng tài Cấu trúc, Trọng tài Tính xác thực). Mỗi giám khảo sẽ chấm điểm các tiêu chí cụ thể bằng lập luận từng bước dựa trên một bảng tiêu chí (rubric) từ 1-5.

   **✋ Thực hành – Triển khai một giám khảo đơn giản:**
   ```python
   def evaluate_with_judge(trajectory: dict, rubric: str) -> int:
       prompt = f"""You are a Factuality Judge. Grade this trajectory on a 1-5 scale.
       Rubric: {rubric}
       Trajectory: {trajectory}
       Return only the score and one sentence rationale."""
       response = llm.invoke(prompt)
       return extract_score(response)
   ```

2. **Bộ kịch bản chuẩn kiểm thử hồi quy (Golden Trajectory Regression Suite):**  
   Đội ngũ phát triển duy trì một tập dữ liệu hồi quy gồm hơn 200 kịch bản lập kế hoạch doanh nghiệp được chọn lọc, đại diện cho các yêu cầu, dữ liệu đầu vào và cơ sở dữ liệu khách hàng đa dạng. Bất kỳ thay đổi nào đối với prompt hoặc bộ điều phối (orchestration) đều kích hoạt chạy một đường ống CI/CD tự động để đánh giá quỹ đạo của tác nhân đối chiếu với tập dữ liệu chuẩn này, từ đó phát hiện sự suy giảm điểm số chất lượng.

3. **Ràng buộc bất biến trong quỹ đạo (Trajectory Assertion Invariants):**  
   Các quy tắc lập trình cứng được khẳng định (assert) ở lớp điều phối (ví dụ: xác nhận rằng mỗi đoạn đầu ra ánh xạ tới ít nhất một nút nguồn đã được xác minh, hoặc tổng số tính toán phải khớp chính xác với tổng số học của các đoạn).

   **🧠 Bài tập:** Viết một câu lệnh ràng buộc (invariant) để kiểm tra: "total_amount = sum(line_item.amount) đối với tất cả các dòng chi tiết". Mô phỏng một tác nhân bị lỗi và bắt lỗi đó bằng chương trình.

4. **Đo lường khoảng cách ngữ nghĩa (Semantic Distance Measurement):**  
   Các nền tảng so sánh vector nhúng (embeddings) của nội dung được tạo ra với các tài liệu quy định/chính sách chính thức để tính toán điểm số tương đồng ngữ nghĩa, cung cấp bằng chứng định lượng về tính tuân thủ.

   **💬 Thảo luận:** *Ngưỡng tương đồng an toàn là bao nhiêu? 0.85? 0.95? Làm thế nào để tránh các trường hợp dương tính giả (false positives)?*

---

### Phần 3.3: Chi Phí và Độ Trễ (Cost and Latency)

**Tại sao các hệ thống tác nhân lại đắt đỏ:**  
Một tác vụ tác nhân đơn lẻ có thể bao gồm:  
- 10-50 cuộc gọi suy luận LLM (lập kế hoạch, phản chiếu, giải nghĩa kết quả công cụ)  
- 5-20 cuộc gọi công cụ (yêu cầu API, truy vấn cơ sở dữ liệu)  
- 2-5 hoạt động truy xuất từ cơ sở dữ liệu vector  
- Cửa sổ ngữ cảnh từ 10.000-100.000 tokens cho mỗi cuộc gọi  

**🎯 Tính toán trực tiếp (5 phút):**  
Ước tính: 15 cuộc gọi LLM × (8k token đầu vào + 2k token đầu ra) × giá của Claude 4.6 Sonnet ($3 / 1M token đầu vào, $15 / 1M token đầu ra) = ~$0.70 cho mỗi tác vụ.  
Cho 10.000 tác vụ/ngày → $7.000/ngày. *Đặt câu hỏi: “Quản lý của bạn sẽ nói gì về con số này?”*

**Cách các hệ thống thực tế giảm thiểu chi phí và độ trễ:**  
Các hệ thống thực tế giải quyết sự đánh đổi giữa chi phí - độ trễ - chất lượng bằng bốn tối ưu hóa cốt lõi:

1. **Định tuyến mô hình lai & Định tuyến ngữ nghĩa (Tiered & Semantic Model Routing):**  
   Thay vì chạy tất cả các bước trên một mô hình đắt tiền duy nhất, các kiến trúc sản xuất sử dụng một bộ định tuyến ngữ nghĩa (semantic router) để phân loại ý định người dùng và định tuyến tác vụ qua các tầng mô hình:  
   - *Tầng Lập luận Chuyên sâu (Frontier / Reasoning Tier - Claude 4.6 Sonnet / DeepSeek-R1):* Dành riêng cho các tác vụ phức tạp, đòi hỏi khả năng tư duy cao như lập kế hoạch ý định ban đầu và trích xuất đồ thị cấu trúc.  
   - *Tầng Tổng hợp (Synthesis Tier - Claude 4.6 Haiku / GPT-4o-mini):* Sử dụng cho sinh văn bản trung gian, phác thảo mã nguồn và tổng hợp tự sự.  
   - *Tầng Tiện ích (Utility Tier - Llama 3.3 70B / Gemini 2.5 Flash):* Xử lý các tác vụ nhẹ như dịch từ vựng, trích xuất thẻ tag và định dạng cấu trúc dữ liệu.

   **✋ Code pattern – Bộ định tuyến ngữ nghĩa:**
   ```python
   class TieredRouter:
       def route(self, task: str) -> str:
           if any(kw in task for kw in ["plan", "strategy", "reason"]):
               return "claude-4.6-sonnet"
           elif any(kw in task for kw in ["extract", "parse"]):
               return "gpt-4o-mini"
           else:
               return "llama-3.3-70b"
   ```

2. **Tối ưu hóa bố cục Prompt để tận dụng bộ nhớ đệm (Prompt Caching):**  
   Các nền tảng tách biệt dữ liệu tĩnh đầu vào (ví dụ: các quy tắc tuân thủ cố định, hướng dẫn hệ thống) khỏi dữ liệu động đầu vào (ví dụ: yêu cầu cụ thể của người dùng). Bằng cách đặt các khối tĩnh ở ngay đầu ngữ cảnh prompt, chúng tối đa hóa bộ nhớ đệm prompt bản địa (native prompt caching) của nhà cung cấp, giúp giảm đến **80%** phí token đầu vào và giảm một nửa độ trễ.

   **🧠 Bài tập:** Lấy một prompt gồm 4k token quy tắc tĩnh + 500 token truy vấn. Cấu trúc lại nó, kích hoạt bộ nhớ đệm caching (Anthropic/DeepSeek) và đo lường lượng chi phí tiết kiệm được.

3. **Thu gọn ngữ cảnh theo ngữ nghĩa (Tối ưu hóa RAG):**  
   Để ngăn việc nhồi nhét toàn bộ bảng cơ sở dữ liệu vào cửa sổ ngữ cảnh, hệ thống sử dụng tìm kiếm lai dense-sparse (vector embeddings kết hợp với BM25) để chỉ truy xuất $K$ phân đoạn phù hợp nhất (dưới 10k token), giúp giữ vững sự mạch lạc trong lập luận và giảm tải chi phí token dư thừa.

4. **Xử lý song song bất đồng bộ (Asynchronous Parallel Processing):**  
   Các bước không phụ thuộc lẫn nhau (chẳng hạn như tạo các phần báo cáo riêng biệt hoặc chạy kiểm thử các mô hình mã nguồn độc lập) được thực thi song song qua mã Python bất đồng bộ (asyncio), giúp giảm độ trễ phản hồi cảm nhận bởi người dùng từ vài phút xuống còn vài giây.

   **✋ Live refactor:** Thay thế các lệnh gọi tuần tự bằng `asyncio.gather()` – đo lường thời gian thực chạy (wall-time) giảm từ 45 giây xuống 12 giây.

---

### Phần 3.4: Khả Năng Quan Sát và AgentOps (Observability and AgentOps)

**Tại sao các công cụ DevOps truyền thống lại thất bại đối với tác nhân:**  
Các công cụ quan sát truyền thống (logs, metrics, traces) được thiết kế cho các hệ thống mà trạng thái nội bộ của chúng được thể hiện bằng mã nguồn và dữ liệu. Trạng thái nội bộ của tác nhân lại được thể hiện bằng ngôn ngữ tự nhiên — những lập luận không thể ánh xạ một cách rõ ràng thành dữ liệu đo lường (telemetry) có cấu trúc.

**🎯 Demo – Vấn đề về tính mập mờ/thiếu minh bạch (3 phút):**  
Trực quan hóa nhật ký thô của một tác nhân bị lỗi. *“Bạn có thể biết tại sao nó gọi hàm `delete_file` không? Lập luận đằng sau là gì?”* Người tham gia không thể trả lời. Sau đó, hiển thị cùng lỗi đó nhưng đi kèm với dấu vết ngữ nghĩa (semantic tracing).

**Cách các hệ thống thực tế triển khai khả năng quan sát:**  
Các hệ thống thực tế coi khả năng quan sát là một yêu cầu sản xuất ưu tiên hàng đầu thông qua một cơ sở hạ tầng AgentOps chuyên dụng:

1. **Theo dấu ngữ nghĩa với MLflow Tracking (Semantic Tracing):**  
   Sử dụng hệ thống theo dõi tự động của MLflow (tích hợp qua `mlflow.langchain.autolog()`), mọi hành động được ghi lại dưới dạng một "Span". Các Span ghi lại dữ liệu đầu vào, đầu ra, mức tiêu thụ token, độ trễ, phiên bản prompt template và các siêu tham số mô hình cho mỗi cuộc gọi LLM và công cụ.

   **✋ Thực hành cài đặt thiết bị giám sát:**
   ```python
   import mlflow
   mlflow.langchain.autolog()
   with mlflow.start_run(run_name="agent_trace"):
       result = agent.invoke("Analyze this contract")
   # Sau đó mở MLflow UI để xem từng cuộc gọi LLM, mức tiêu thụ token và các spans lồng nhau
   ```

2. **Bảng điều khiển cây thực thi trực quan (Visual Execution Tree Dashboard):**  
   Các nhà phát triển có thể xem các trace spans dưới dạng phân cấp lồng nhau, thể hiện chính xác cách bộ điều phối định tuyến ý định, truy hồi bộ nhớ, phân tích công cụ và chuyển đổi trạng thái. Điều này giúp dễ dàng xác định vị trí chính xác của nút chịu trách nhiệm cho các lỗi hoặc sự tăng vọt về độ trễ.

3. **Hộp cát phát lại quỹ đạo ngoại tuyến (Offline Trajectory Replay Sandbox):**  
   Nếu người dùng báo cáo một lần thực thi thất bại hoặc phản hồi tiêu cực, các nhà phát triển có thể trích xuất nhật ký thực thi đó, tải nó vào một hộp cát (sandbox) cục bộ, đóng băng trạng thái đầu vào chính xác, tinh chỉnh các prompt hệ thống hoặc kỹ năng (skills) của tác nhân, và phát lại bước đó để xác nhận các sửa lỗi hồi quy.

   **🧠 Bài tập:** Ghi lại một quỹ đạo bị lỗi, thay đổi một prompt hệ thống, chạy phát lại và xác minh xem lỗi đã được khắc phục hay chưa.

4. **Rào chắn bảo mật an toàn và chính sách (Safety & Policy Guardrails):**  
   Tại cả ranh giới đầu vào và đầu ra của tất cả các công cụ, các rào chắn an toàn thời gian thực (như Llama Guard hoặc NeMo Guardrails) giám sát và lọc các truy vấn cũng như nội dung tạo ra để kiểm toán chính sách, ngăn chặn tấn công chèn lệnh (prompt injection) hoặc vi phạm chính sách.

   **💬 Thảo luận:** *Bạn sẽ triển khai các rào chắn bảo mật nào cho một tác nhân hỗ trợ khách hàng có quyền truy cập thông tin định danh cá nhân PII?*

---

## Tổng Hợp: Kiến Trúc Hệ Thống Tác Nhân Thực Tế (Production Agentic System Architecture)

Nhìn lại hệ thống tác nhân thực tế qua lăng kính của ngăn xếp tác nhân hiện đại:

| Lớp Ngăn Xếp Agent | Triển Khai Thực Tế |
|---|---|
| **Orchestration** (Điều phối) | Máy trạng thái hữu hạn tùy chỉnh điều phối đường ống xử lý, đảm bảo dữ liệu ổn định 100% |
| **Reasoning Core** (Lõi lập luận) | Cơ chế định tuyến ngữ nghĩa lai tới Claude 4.6 Sonnet / DeepSeek-R1 và Llama 3.3 70B / Gemini 2.5 Flash |
| **Skills** (Kỹ năng) | Đóng gói mô-đun độc lập cho Trích xuất dữ liệu, Kiểm toán tuân thủ và Sinh báo cáo |
| **Tools & Protocols** (Công cụ & Giao thức) | Hệ thống file/database qua MCP và ủy nhiệm thanh toán qua AP2 |
| **Memory** (Bộ nhớ) | Cơ sở dữ liệu Vector cho bộ nhớ ngữ nghĩa người dùng; bộ nhớ episodic cho trạng thái phiên ngắn hạn |
| **Cognitive Loop** (Vòng lặp nhận thức) | Vòng lặp xác thực PLAN → ACT → OBSERVE → REFLECT tại mỗi biên giai đoạn |

Kiến trúc sản xuất đạt đến cách bố trí này thông qua phương pháp kỹ nghệ dựa trên định hướng miền (domain-driven engineering), chứ không phải bằng cách áp dụng một framework chung chung có sẵn. Các mẫu kiến trúc của AI tác nhân không hề ngẫu nhiên — chúng xuất hiện một cách tự nhiên từ các yêu cầu của các tác vụ phức tạp, đa bước và dựa trên miền cụ thể.

**🎯 Hoạt động kết thúc workshop (thử thách nhóm):**  
Chia thành các nhóm nhỏ, lựa chọn một trường hợp sử dụng thực tế trong doanh nghiệp (ví dụ: “xử lý hóa đơn tự động có con người phê duyệt”). Ánh xạ nó vào ngăn xếp ở trên, sau đó xác định 3 rủi ro hàng đầu cho mỗi lớp và đề xuất một biện pháp giảm thiểu từ Phần 3.1–3.4. Thuyết trình trước lớp (5 phút cho mỗi nhóm).

**📚 Danh sách kiểm tra mang về (Take‑home checklist):**  
- [ ] Đầu ra có cấu trúc (Structured output) + xác thực hai lớp (two‑tier validation)  
- [ ] Vòng lặp tự sửa lỗi (tối đa 3 lần thử → chuyển giao HITL)  
- [ ] Ghi nhật ký quỹ đạo (Trajectory logging) + đánh giá bằng LLM-as-a-judge trong quy trình CI  
- [ ] Định tuyến mô hình phân tầng (tiered model routing) + bộ nhớ đệm prompt caching  
- [ ] Xử lý song song bất đồng bộ (async parallelism) cho các tác vụ độc lập  
- [ ] Theo vết MLflow tracing cho mỗi lượt chạy  
- [ ] Hộp cát phát lại (replay sandbox) đối với các trường hợp lỗi  
- [ ] Rào chắn bảo mật (guardrails) trên các công cụ
