# **Tài Liệu Phát Tay: Danh Sách Kiểm Tra**

## **Tham Chiếu Nhanh**

**Vòng Lặp Tác Nhân:**
```
PLAN → ACT → OBSERVE → REFLECT → ITERATE → COMPLETE
```

**Agentic Stack 5 Lớp:**
1. Orchestration Layer — Máy trạng thái hữu hạn tùy chỉnh
2. Reasoning Core — Định tuyến mô hình (Frontier / Utility)
3. Skills — Tri thức nghiệp vụ đóng gói theo module
4. Tools & Protocols — MCP, AP2
5. Memory Systems — Bộ nhớ episodic + Vector DB

**Quy Trình ConnectED:**
```
Concept Extraction → Objective Gen → Activity Design → Content Dev → Visual Materials (AP2) → Evaluation Review
```

**Khung Sư Phạm ADDIE:**
```
Analyze → Design → Develop → Implement → Evaluate
```

---

## **CHECKLIST 1: Triển Khai Hệ Tác Nhân (Deployment)**

### Kiến Trúc & Thiết Kế
- [ ] **[CRITICAL]** Phân rã tác vụ thành subtasks với ranh giới và schemas rõ ràng.
- [ ] **[CRITICAL]** Bố trí điểm kiểm duyệt con người (HITL) cho các hành động có rủi ro cao.
- [ ] **[CRITICAL]** Xác định phương án fallback và mô tả lỗi dự phòng cho từng subtask.
- [ ] **[RECOMMENDED]** Áp dụng kiến trúc phân cấp — tách biệt các bước lập luận và thực thi.
- [ ] **[RECOMMENDED]** Đảm bảo đầu ra từng giai đoạn có cấu trúc và được xác thực schema.
- [ ] **[RECOMMENDED]** Đóng gói Skills thành tệp riêng biệt, quản lý phiên bản qua Git.
- [ ] **[RECOMMENDED]** Nhúng ngữ cảnh bản địa hóa trực tiếp vào prompts và templates.
- [ ] **[ADVANCED]** Giới hạn số lần tự sửa lỗi (tối đa 3 lần → kích hoạt HITL).
- [ ] **[ADVANCED]** Đặt hard cap ngân sách token tối đa ở lớp điều phối.

### An Toàn & Rào Chắn (Guardrails)
- [ ] **[CRITICAL]** Ràng buộc an toàn ngăn thay đổi trạng thái trái phép — thực thi ở tầng code.
- [ ] **[CRITICAL]** Lưu API keys/secrets trong biến môi trường, tuyệt đối không lưu trong prompt.
- [ ] **[CRITICAL]** Lọc sạch dữ liệu đầu ra trước khi hiển thị cho người dùng cuối.
- [ ] **[RECOMMENDED]** Hard cap token tối đa cho mỗi lần thực thi tác vụ.
- [ ] **[RECOMMENDED]** Xác định ngưỡng tin cậy để kích hoạt chuyển giao cho con người.
- [ ] **[ADVANCED]** Kiểm thử tấn công (adversarial testing) trên prompts và công cụ.
- [ ] **[ADVANCED]** Ủy quyền mật mã qua AP2 Intent/Cart Mandates để kiểm soát giao dịch tự động.

### Hạ Tầng & Vận Hành
- [ ] **[CRITICAL]** Gọi API qua exponential backoff retry handler.
- [ ] **[CRITICAL]** Phương án hạ cấp (graceful degradation) khi API ngoài ngừng hoạt động.
- [ ] **[RECOMMENDED]** Ghi nhật ký đầy đủ: tham số mô hình, dữ liệu vào/ra, chi phí token.
- [ ] **[RECOMMENDED]** Thiết kế cuộc gọi công cụ có tính idempotency.
- [ ] **[RECOMMENDED]** Bộ nhớ episodic lưu trạng thái tác nhân để khôi phục khi lỗi.
- [ ] **[ADVANCED]** Circuit breakers cho các công cụ lỗi liên tục.

### Sẵn Sàng Ra Mắt
- [ ] **[CRITICAL]** Kiểm thử end-to-end đạt tỷ lệ thành công >90%.
- [ ] **[CRITICAL]** Có tài liệu ứng phó sự cố (rollback plan, người phụ trách).
- [ ] **[RECOMMENDED]** Triển khai canary trước khi phát hành toàn diện.
- [ ] **[RECOMMENDED]** Kênh phản hồi trực tiếp từ người dùng thực tế.

---

## **CHECKLIST 2: Tối Ưu Quy Trình & Prompt**

### Thiết Kế Prompt
- [ ] Mỗi system prompt tập trung vào một trách nhiệm duy nhất.
- [ ] Dùng câu mệnh lệnh trực tiếp, tránh văn phong mơ hồ.
- [ ] Định nghĩa rõ cấu trúc schema đầu ra (JSON/YAML) kèm ví dụ few-shot.
- [ ] Nêu rõ ràng buộc và quy tắc phủ định (những gì KHÔNG được làm).
- [ ] Loại bỏ ngữ cảnh thừa — tiết kiệm token và tránh loãng sự chú ý của mô hình.
- [ ] Thống nhất thuật ngữ nghiệp vụ trên toàn bộ hệ thống prompt.

### Cấu Trúc Pipeline
- [ ] Tách biệt ranh giới giai đoạn bằng data contracts rõ ràng (input/output schemas).
- [ ] **[RECOMMENDED]** Phân rã tác vụ lập luận phức tạp thành subtasks tuyến tính để giảm ảo tưởng.
- [ ] **[RECOMMENDED]** Cô lập trạng thái giữa các giai đoạn — chỉ truyền dữ liệu tối thiểu cần thiết.
- [ ] Chạy song song các giai đoạn không phụ thuộc nhau.
- [ ] Xác thực tại mỗi ranh giới giai đoạn — không để lỗi lan truyền.
- [ ] Xác định chiến lược xử lý lỗi cho từng bước: thử lại, bỏ qua, fallback, hoặc báo HITL.

### Quản Lý Ngữ Cảnh
- [ ] Giám sát lượng token tiêu thụ tại mỗi giai đoạn.
- [ ] Tóm tắt lịch sử hội thoại dài trước khi đưa vào ngữ cảnh mới.
- [ ] Xếp hạng và cắt ngắn kết quả RAG — chỉ lấy N kết quả hàng đầu.
- [ ] Prompt caching cho dữ liệu tĩnh ở đầu ngữ cảnh.

### Định Tuyến Mô Hình
- [ ] Định tuyến tác vụ đơn giản (phân loại, định dạng) → mô hình nhỏ (Llama 3.3 70B, Gemini 2.5 Flash).
- [ ] Định tuyến tác vụ lập luận phức tạp → Frontier/Reasoning Models (Claude 4.6 Sonnet / DeepSeek-R1).
- [ ] **[RECOMMENDED]** Semantic routing bằng embedding similarity hoặc bộ phân loại siêu nhẹ.
- [ ] Cấu trúc prompt tĩnh nhất quán để tối ưu prompt caching.

---

## **CHECKLIST 3: Tối Ưu Hóa Chi Phí & Token**
- [ ] Giám sát token (đầu vào, đầu ra, cache hit) trên mỗi lượt chạy.
- [ ] Prompts hệ thống và templates cố định ở đầu ngữ cảnh — tối ưu prompt caching (giảm đến 80% chi phí).
- [ ] **[RECOMMENDED]** Semantic routing phân bổ mô hình theo độ phức tạp yêu cầu.
- [ ] Cảnh báo khi chi phí token tăng đột ngột bất thường.
- [ ] Loại bỏ từ đệm và hướng dẫn thừa trong prompt.
- [ ] Giới hạn độ dài đầu ra trực tiếp trong prompt (ví dụ: "trả lời trong 3 câu").

---

## **CHECKLIST 4: Độ Tin Cậy & Đánh Giá**
- [ ] Phát hiện và chặn vòng lặp kế hoạch vô hạn (planning loops).
- [ ] Xác thực dữ liệu đầu vào của công cụ trước khi thực thi.
- [ ] Xác định kịch bản HITL cụ thể khi độ tự tin của tác nhân thấp.
- [ ] Kiểm thử tự động hiệu quả quỹ đạo thực thi (trajectory efficiency).
- [ ] Hồi quy CI/CD với bộ kịch bản lỗi từ quá khứ.
- [ ] Đánh giá offline LLM-as-judge cho chất lượng sư phạm và độ phủ chương trình học.

---

## **CHECKLIST 5: Sẵn Sàng Giám Sát (AgentOps)**
- [ ] Tracing toàn bộ chuỗi PLAN → ACT → OBSERVE → REFLECT kèm input/output công cụ.
- [ ] Hỗ trợ replay trajectory lỗi trong sandbox cô lập.
- [ ] Masking dữ liệu nhạy cảm (PII) trong trace nhật ký.
- [ ] Liên kết phản hồi người dùng với Trace ID tương ứng.
- [ ] Định kỳ rà soát các trajectory thất bại để cải thiện prompt/skills.
