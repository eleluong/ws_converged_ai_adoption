# Workshop — Tài Liệu Ghi Chú Chi Tiết
## Các Thách Thức Kéo Dài Trong Agentic AI (Persistent Challenges)

> Các ghi chú này cung cấp thông tin chi tiết nâng cao, các phân tích đánh đổi và các giải pháp thiết kế thực tế cho hệ thống tác nhân doanh nghiệp nói chung.

---

### Phần 3.1: Độ Tin Cậy & Ảo Tưởng (Reliability & Hallucinations)

* **Tại sao lại khó:** Các tác nhân thông minh dễ gặp các lỗi nghiêm trọng như vòng lặp suy nghĩ vô hạn (infinite reasoning loops), sinh payload JSON bị lỗi cấu trúc, gọi các công cụ hoặc API không tồn tại, trôi dạt chỉ thị (instruction drift) qua các chu kỳ phản hồi, hoặc ảo tưởng ra các thực thể/khái niệm nằm ngoài tài liệu gốc. Do đường ống agent là đa bước và có tính bất định (nondeterministic), một sai số nhỏ ở khâu trung gian có thể khuếch đại thành thảm họa ở đầu ra cuối cùng.
* **Giải pháp Độ Tin Cậy chất lượng cao:**
  * **Ràng buộc JSON ở cấp độ giải mã (Guaranteed JSON Generation):** Cấu hình mô hình ở mức suy luận (ví dụ: cấu hình JSON mode của nhà phát triển hoặc dùng thư viện Outlines) để ép buộc định dạng cú pháp JSON hợp lệ ngay trong quá trình sinh token, loại bỏ hoàn toàn lỗi cú pháp dấu ngoặc hoặc dấu phẩy.
  * **Cổng xác thực hai lớp (Two-Tier Validation Gate):** 
    - *Lớp 1 (Xác thực cấu trúc & kiểu):* Sử dụng thư viện Pydantic để kiểm tra định dạng dữ liệu đầu ra JSON của agent xem có khớp với schema yêu cầu hay không.
    - *Lớp 2 (Semantic Grounding Validation):* Đối chiếu các thực thể ngữ nghĩa vừa trích xuất với một chỉ mục siêu dữ liệu miền (Domain Metadata Index) được lưu trữ cục bộ dưới dạng cấu trúc dữ liệu Trie hoặc Bloom filter để đảm bảo không có khái niệm nào bị ảo tưởng ra ngoài tài liệu nguồn.
  * **Vòng lặp tự sửa sai theo ngữ cảnh (Contextual Self-Correction Loop):** Khi phát hiện lỗi xác thực ở cổng Validation Gate, orchestrator sẽ trích xuất chi tiết lỗi (dưới dạng diff/parser error) và đính kèm vào lịch sử hội thoại để gửi lại cho mô hình tự điều chỉnh.
  * **Dashboard con người can thiệp (Human-in-the-loop - HITL):** Nếu tự sửa sai thất bại quá 3 lần, orchestrator sẽ tạm dừng tiến trình, lưu lại trạng thái bộ nhớ episodic hiện tại và chuyển giao sang giao diện bảng điều khiển của kiểm trị viên/người vận hành để duyệt hoặc chỉnh sửa thủ công trước khi kích hoạt chạy tiếp, ngăn ngừa hoàn toàn việc truyền tải dữ liệu lỗi xuống các tác nhân hạ nguồn.

---

### Phần 3.2: Đánh Giá (Evaluation)

* **Tại sao lại khó:** Các bài kiểm tra truyền thống (như trắc nghiệm hay so sánh văn bản đơn thuần) không đánh giá được tính đúng đắn của hành trình tư duy đa bước. Đánh giá hệ thống tác nhân yêu cầu **Đánh Giá Quỹ Đạo (Trajectory Evaluation)**: kiểm tra lập kế hoạch, lựa chọn công cụ, khả năng phục hồi sau lỗi và tuân thủ các quy tắc an toàn.
* **Giải pháp Đánh giá chất lượng cao:**
  * **Khung đánh giá quỹ đạo (Trajectory Eval) & LLM-as-a-Judge:** Hệ thống ghi lại toàn bộ quỹ đạo hành động (Plan -> Act -> Observe -> Reflect -> Spans). Sử dụng một hội đồng giám khảo tự động (evaluator panel) chạy trên mô hình **Claude 4.6 Sonnet** (bao gồm Trọng tài Nghiệp vụ, Trọng tài Cấu trúc, Trọng tài Tính xác thực) để đánh giá quỹ đạo dựa trên các rubrics định lượng (thang điểm từ 1 đến 5) về tính đúng đắn logic, phân bổ tài nguyên thực tế, và độ chuẩn xác nội dung.
  * **Bộ kịch bản chuẩn (Golden Trajectory Suite):** Duy trì một tập hợp hơn 200 kịch bản mẫu đại diện trong hệ thống CI/CD để chạy thử nghiệm hồi quy (regression testing) tự động mỗi khi có thay đổi về prompt, kỹ năng (skills), hay nâng cấp mô hình.
  * **Ràng buộc cứng bằng lập trình (Programmatic Assertions) & Đo lường khoảng cách ngữ nghĩa (Embedding Semantic Distance):** Bổ sung các câu lệnh kiểm tra logic toán học (ví dụ: tổng chi phí phân bổ phải bằng đúng ngân sách quy định) phối hợp đo khoảng cách cosine vector nhúng để kiểm tra sự sai lệch về mặt ngữ nghĩa của nội dung sinh ra.

---

### Phần 3.3: Chi Phí và Độ Trễ (Cost and Latency)

* **Tại sao lại khó:** Các tác nhân rất tốn kém về tài nguyên tính toán, thường yêu cầu hàng chục lệnh gọi mô hình tuần tự trong một tác vụ đơn lẻ, gây tăng chi phí token lũy tiến và độ trễ phản hồi quá dài (thường > 2 phút/tác vụ) làm suy giảm trải nghiệm người dùng.
* **Giải pháp Chi Phí và Độ Trễ chất lượng cao:**
  * **Định tuyến mô hình lai & Định tuyến ngữ nghĩa (Tiered & Semantic Routing):**
    - *Semantic Router (Định tuyến Ngữ nghĩa):* Sử dụng một mô hình phân loại hoặc embedding gọn nhẹ để kiểm tra ý định (intent) của người dùng đầu vào. Nếu là yêu cầu dịch thuật đơn giản, sửa chính tả, hoặc định dạng bảng, request được chuyển ngay tới mô hình nhỏ ở tầng dưới để xử lý, tránh sử dụng lãng phí mô hình cao cấp.
    - *Tầng lập luận chuyên sâu (Reasoning Tier):* Chuyển các tác vụ phức tạp cần tư duy logic sâu và căn chỉnh ngữ nghĩa chuẩn như Lập kế hoạch hành động, Kiểm toán tài chính tới **Claude 4.6 Sonnet** hoặc **DeepSeek-R1**.
    - *Tầng tổng hợp nội dung (Synthesis Tier):* Định tuyến việc soạn thảo văn bản, chi tiết báo cáo, kịch bản giao tiếp tới các mô hình có chi phí trung bình như **Claude 4.6 Haiku** hoặc **GPT-4o-mini**.
    - *Tầng tiện ích (Utility Tier):* Dịch thuật từ vựng, phân loại metadata, định dạng dữ liệu thô được giao cho các mô hình siêu rẻ như **Llama 3.3 70B** hoặc **Gemini 2.5 Flash**, giúp tiết kiệm 70% tổng chi phí vận hành.
  * **Tối ưu hóa bộ đệm prompt (Prompt Caching):** Đặt các khung prompt hệ thống và văn bản chuẩn/hướng dẫn nghiệp vụ cố định ở đầu cửa sổ ngữ cảnh để tận dụng cơ chế Prompt Caching của nhà cung cấp API, giảm tới 80% chi phí nạp token đầu vào.
  * **Thu gọn ngữ cảnh (Context Pruning) & Song song hóa (Parallelism):** Sử dụng các kỹ thuật lọc RAG để giữ cửa sổ ngữ cảnh dưới 10k tokens. Chạy bất đồng bộ (async) các luồng xử lý không có phụ thuộc lẫn nhau (ví dụ: tạo phần 1 và phần 2 của báo cáo một cách song song) giúp giảm tổng độ trễ phản hồi xuống 45%.

---

### Phần 3.4: Khả Năng Quan Sát & AgentOps (Observability & AgentOps)

* **Tại sao lại khó:** Trạng thái của tác nhân được biểu diễn bằng lập luận ngôn ngữ tự nhiên, khiến các chỉ số giám sát hệ thống truyền thống (như CPU, RAM, hoặc mã lỗi HTTP) trở nên vô dụng khi cần phát hiện lỗi logic hoặc hành vi bất thường bên trong chuỗi suy nghĩ của mô hình.
* **Giải pháp Khả Năng Quan Sát chất lượng cao:**
  * **Semantic Tracing (Theo dấu Ngữ nghĩa):** Áp dụng chuẩn OpenInference (sử dụng các công cụ như Langfuse hoặc Arize Phoenix) để ghi nhận từng bước gọi LLM dưới dạng các "Spans" có cấu trúc, lưu lại thông tin chi tiết về prompt, phản hồi tư duy (thought chain), công cụ được gọi, tokens tiêu thụ, và độ trễ.
  * **Bảng điều khiển cây thực thi (Execution Tree Dashboard):** Trực quan hóa toàn bộ chuỗi cuộc gọi phân cấp của agent trong pipeline xử lý. Cho phép lập trình viên nhấp vào từng nút trong cây để kiểm tra chính xác tham số đầu vào/đầu ra và tìm ra nguyên nhân gây lỗi hoặc thắt nút cổ chai (latency bottleneck).
  * **Môi trường phát lại ngoại tuyến (Offline Trajectory Replay Sandbox):** Cho phép tải xuống toàn bộ quỹ đạo chạy bị lỗi của người dùng thực tế và phát lại (replay) cục bộ trong môi trường sandbox biệt lập để thử nghiệm và tinh chỉnh prompt mà không gây ra các phản ứng phụ (side effects) trên hệ thống sản xuất.
  * **Rào chắn bảo mật thời gian thực (Real-time Guardrails):** Tích hợp các mô hình lọc an toàn (như Llama Guard) để giám sát các câu lệnh trước khi nạp vào công cụ (input) và nội dung trước khi trả về cho người dùng (output), ngăn ngừa các cuộc tấn công prompt injection hoặc rò rỉ dữ liệu nhạy cảm.

---

### Tổng Hợp: Ví Dụ Về Hệ Thống Tác Nhân Thực Tế (Example of Production Agentic System)

Để minh họa, dưới đây là cách một hệ thống tác nhân thực tế được xây dựng dựa trên phương pháp kỹ nghệ hệ thống nâng cao (production-grade system engineering):

| Lớp (Layer) | Chi tiết triển khai thực tế của Hệ Thống Tác Nhân |
|---|---|
| **Orchestration** | Sử dụng máy trạng thái hữu hạn (Finite State Machine) tùy chỉnh để điều phối tuần tự các giai đoạn của quy trình xử lý, đảm bảo dữ liệu được chuyển giao và các ràng buộc được thực hiện một cách nhất quán 100%. |
| **Reasoning Core** | Cơ chế định tuyến ngữ nghĩa lai: lập kế hoạch và phân tích sâu chạy trên **Claude 4.6 Sonnet / DeepSeek-R1**; sinh văn bản báo cáo trung gian chạy trên **Claude 4.6 Haiku**; dịch thuật và định dạng chạy trên **Gemini 2.5 Flash / Llama 3.3 70B**. |
| **Skills** | Đóng gói mã nguồn prompt, Pydantic schemas, và dữ liệu few-shot của từng giai đoạn thành các kỹ năng (skills) độc lập, quản lý phiên bản qua Git. |
| **Tools & Protocols** | Sử dụng **Model Context Protocol (MCP)** để truy vấn dữ liệu và cơ sở dữ liệu doanh nghiệp; sử dụng **Agent Payments Protocol (AP2)** để thanh toán mua các API dịch vụ ngoài thông qua Intent Mandates. |
| **Memory** | *Episodic memory:* Lưu trạng thái xử lý hiện tại để tiếp tục quy trình; *Semantic memory:* Lưu phong cách định dạng và cấu hình của người dùng trong Vector DB để cá nhân hóa tự động. |
| **Cognitive Loop** | Quy trình tại mỗi nút tuân thủ nghiêm ngặt vòng lặp: PLAN (Lập kế hoạch thiết kế khối lượng) → ACT (Gọi mô hình sinh báo cáo) → OBSERVE (Xác thực dữ liệu) → REFLECT (Tự điều chỉnh nếu phát hiện sai lệch). |
