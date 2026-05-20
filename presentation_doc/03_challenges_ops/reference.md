# Các Thách Thức Kéo Dài Trong Agentic AI

Dù có những bước tiến nhanh chóng, các thách thức lớn vẫn tồn tại khi thiết kế và mở rộng các hệ thống tác nhân AI trong thực tế sản xuất. Dưới đây là phân tích các thách thức chính và cách giảm thiểu chúng trong thực tế.

---

## Độ Tin Cậy & Ảo Tưởng (Reliability & Hallucinations)

Các tác nhân (agents) chạy thực tế (production) thường thất bại theo những cách khó dự đoán và có tính dây chuyền.
* **Các dạng lỗi (Failure Modes):** Vòng lặp vô hạn, payload JSON bị lỗi cấu trúc, gọi các công cụ/API không tồn tại, trôi dạt chỉ thị (instruction drift) và ảo tưởng thực thể ngoài phạm vi tài liệu gốc. Do quy trình tác nhân là đa bước và có tính phi tuyến tính, một lỗi nhỏ ở bước trung gian có thể tích lũy thành lỗi thảm họa ở đầu ra.
* **Giải pháp thực tế:** Ép buộc **Guaranteed JSON Generation** ở cấp độ giải mã (decoding level). Sử dụng cổng xác thực hai lớp: xác thực cấu trúc qua Pydantic JSON schema và xác thực ngữ nghĩa (Semantic Grounding Validation) đối chiếu thực thể trích xuất với chỉ mục siêu dữ liệu miền (Domain Metadata Index - Trie/Bloom filter). Thiết lập vòng lặp tự sửa sai theo ngữ cảnh (Contextual Self-Correction Loop) gửi phản hồi lỗi cú pháp (diff-based parser feedback) cho mô hình tự sửa. Nếu tự sửa thất bại quá 3 lần, hệ thống tạm dừng và hiển thị lên dashboard con người duyệt (Human-in-the-loop - HITL) để người vận hành phê duyệt trạng thái trước khi tiếp tục.

---

## Đánh Giá (Evaluation)

Đánh giá các hệ thống tác nhân (agentic systems) khó hơn nhiều so với việc so sánh văn bản đơn thuần:
* **Bài Toán Quỹ Đạo (The Trajectory Problem):** Bạn phải đánh giá toàn bộ lộ trình thực thi (các bước lập luận, cuộc gọi công cụ, truy hồi bộ nhớ, khả năng tự sửa lỗi và tuân thủ chính sách) thay vì chỉ đánh giá câu trả lời cuối cùng.
* **Giải pháp thực tế:** Triển khai hệ thống tự động **Trajectory Eval & LLM-as-a-Judge**. Hệ thống ghi nhật ký đầy đủ hành trình hoạt động (Plan -> Act -> Observe -> Reflect). Một hội đồng giám khảo tự động (evaluator panel) sử dụng **Claude 4.6 Sonnet** (Trọng tài Nghiệp vụ, Cấu trúc, Xác thực) để chấm điểm quỹ đạo dựa trên các thang rubrics định lượng (1-5) về độ bao phủ mục tiêu nghiệp vụ, hiệu năng tài nguyên thực tế, và tính chuẩn xác logic. Chạy bộ kịch bản chuẩn (Golden Trajectory Suite) gồm hơn 200 tình huống trong quy trình CI/CD để phát hiện suy giảm chất lượng, kết hợp kiểm tra ràng buộc cứng logic nghiệp vụ và đo khoảng cách cosine vector nhúng.

---

## Chi Phí & Độ Trễ (Cost & Latency)

Các vòng lặp tác nhân tạo ra chi phí vận hành rất lớn:
* **Các nút thắt cổ chai (Bottlenecks):** Phải thực hiện nhiều cuộc gọi suy luận tuần tự, tích lũy cửa sổ ngữ cảnh lớn và lặp lại việc thực thi công cụ nhiều lần.
* **Giải pháp thực tế:** Áp dụng **Định Tuyến & Caching Prompts (Tiered & Semantic Routing & Prompt Caching)**:
  - *Semantic Router:* Sử dụng mô hình phân loại/embedding gọn nhẹ để phân tích intent của người dùng nhằm định tuyến thông minh.
  - *Tầng Reasoning (Claude 4.6 Sonnet / DeepSeek-R1):* Xử lý các tác vụ phức tạp như Lập kế hoạch hành động và Phân tích quy trình chuyên sâu.
  - *Tầng Synthesis (Claude 4.6 Haiku / GPT-4o-mini):* Soạn thảo chi tiết các phần báo cáo và tài liệu trung gian.
  - *Tầng Utility (Llama 3.3 70B / Gemini 2.5 Flash):* Dịch thuật từ khóa, gắn tag siêu dữ liệu, phân loại đơn giản, giúp giảm chi phí 70%.
  - *Prompt Caching:* Đặt các chỉ thị hệ thống cố định và tài liệu quy chuẩn ở đầu cửa sổ ngữ cảnh để tận dụng bộ nhớ đệm (Prompt Caching), tiết kiệm đến 80% chi phí token đầu vào.
  - *Context Pruning & Parallelism:* Giới hạn ngữ cảnh dưới 10k tokens qua RAG và chạy song song (async) các luồng xử lý độc lập giúp giảm độ trễ 45%.

---

## Khả Năng Quan Sát Và AgentOps (Observability & AgentOps)

Các công cụ DevOps truyền thống thất bại vì trạng thái của tác nhân được thể hiện bằng lập luận ngôn ngữ tự nhiên.
* **Giải pháp thực tế:** Áp dụng **Semantic Tracing** bằng chuẩn OpenInference (sử dụng các công cụ như Langfuse hoặc Arize Phoenix) để ghi nhận từng bước gọi LLM dưới dạng các "Spans" có cấu trúc (input, output, token, độ trễ, cấu hình mô hình). Các kỹ sư có thể hiển thị trực quan cây thực thi (Execution Tree Dashboard) để cô lập nút thắt gây lỗi, thực hiện phát lại ngoại tuyến (Offline Trajectory Replay Sandbox) trên production dữ liệu lỗi để gỡ lỗi và thử nghiệm prompt mới, và chạy rào chắn bảo mật thời gian thực (Real-time Guardrails như Llama Guard) trên cả input/output của công cụ.

---

## Kết Luận (Conclusion)

Tương lai của các ứng dụng AI thực tế nằm ở các hệ thống thông minh được thiết kế chặt chẽ kết hợp giữa:
* Bộ điều phối luồng công việc có tính deterministic,
* Kỹ năng nghiệp vụ và tri thức miền chuyên sâu (Skills),
* Các giao thức chuẩn hóa (MCP, AP2),
* Sự kết hợp linh hoạt của các loại Reasoning Cores khác nhau,
* Và mô hình cộng tác lấy con người làm trung tâm (Human-in-the-loop).

Thành công của hệ thống tác nhân AI trong thực tế phụ thuộc nhiều vào tính nghiêm ngặt trong kiến trúc hệ thống và khả năng kiểm thử, giám sát vận hành hơn là năng lực thô của riêng mô hình ngôn ngữ lớn.
