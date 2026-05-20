# Workshop — Tài Liệu Ghi Chú Chi Tiết
## ConnectED: Một Nền Tảng AI-Native Cho Giáo Dục Việt Nam

> Các ghi chú này cung cấp chiều sâu kỹ thuật, lý do thiết kế và bối cảnh thực tế cho các giảng viên và học viên nâng cao.

---

### Phần 1.1: Tổng Quan — ConnectED là gì?

* **Khác Biệt Cốt Lõi (Core Distinction):** Coi việc soạn giáo án bài học như một quy trình thiết kế sư phạm có hệ thống thay vì chỉ là truy xuất nội dung đơn thuần.
* **Ba Sản Phẩm Đầu Ra Chính:** 
  1. Bản thiết kế bài học (lesson blueprints) có cấu trúc và phù hợp với chương trình học.
  2. Kịch bản slide lời thuyết minh và hoạt cảnh.
  3. Chuỗi hướng dẫn thí nghiệm ảo STEM (Virtual Lab sequences) mang tính tương tác.
* **Bối Cảnh Việt Nam:** ConnectED tận dụng chương trình giáo dục phổ thông quốc gia thống nhất của Việt Nam do Bộ Giáo dục và Đào tạo (MOET) quản lý. Điều này cung cấp một ràng buộc chặt chẽ và một đồ thị tri thức (knowledge graph) được xác định rõ ràng để đối chiếu (grounding).
* **Ý Nghĩa Rộng Hơn:** ConnectED không chỉ là một sản phẩm edtech đơn thuần mà là một mẫu thiết kế (design pattern) có thể tái sử dụng để triển khai các hệ thống AI chuyên biệt trong bất kỳ môi trường pháp lý hoặc văn hóa cụ thể nào (như y tế, pháp lý, tài chính).

---

### Phần 1.2: Bối Cảnh Vấn Đề — Khối Lượng Công Việc Của Giáo Viên

* **Thực Tế Của Giáo Viên:** Chuẩn bị bài dạy tiêu tốn từ 3–4 tiếng cho mỗi tiết dạy. Công việc này bao trùm nhiều miền nhận thức: trích xuất khái niệm từ sách giáo khoa, thiết kế hoạt động và lập sơ đồ đánh giá.
* **Tại Sao Các LLM Chung Chung Thất Bại:** Các mô hình có sẵn (out-of-the-box models) mặc định áp dụng các tiêu chuẩn chương trình giáo dục phương Tây, đề xuất các thiết bị thí nghiệm không có sẵn, sử dụng thuật ngữ không nhất quán và thiếu bối cảnh văn hóa địa phương.
* **Quyết Định Thiết Kế (Design Decision):** ConnectED giải quyết vấn đề này thông qua việc đối chiếu ngữ cảnh (grounding prompts) và sử dụng templates thay vì các phương án tinh chỉnh mô hình (fine-tuning) đắt đỏ và dễ lỗi.

---

### Phần 1.3: ADDIE — Ánh Xạ Tính Toán (Computational Mapping)

Các giai đoạn của ADDIE ánh xạ trực tiếp đến các tiểu tác vụ tính toán riêng biệt, mỗi giai đoạn đều có dữ liệu đầu vào (inputs), đầu ra (outputs) và các quy tắc xác thực (validation rules) nghiêm ngặt:

* **Phân Tích (Analyze):** Xử lý tài liệu sách giáo khoa để tạo ra cấu trúc JSON của các khái niệm cốt lõi (core concepts), năng lực cần đạt và kiến thức tiền đề (prerequisites).
* **Thiết Kế (Design):** Phác thảo bản thiết kế bài học, phân bổ thời gian hoạt động (nhắm mục tiêu tiết học 45 phút tiêu chuẩn) và chiến lược đánh giá.
* **Phát Triển (Develop):** Xây dựng các tài nguyên học tập. Quyết định cốt lõi: *Script-First Approach* (phương pháp kịch bản trước) — tạo lời thoại thuyết minh và nội dung sư phạm trước khi thiết kế phương tiện hình ảnh để đảm bảo tính liên kết.
* **Triển Khai & Đánh Giá (Implement & Evaluate):** Hiển thị qua giao diện xem xét (review UI) để giáo viên có thể chỉnh sửa và thu thập phản hồi.

---

### Phần 1.4: Quy Trình Xử Lý Đa Tác Nhân Phân Cấp (Hierarchical Agent Pipeline)

Cách tiếp cận prompt nguyên khối đơn lẻ (monolithic single-prompt) dễ gặp phải tình trạng bão hòa ngữ cảnh (context saturation), thiếu các điểm kiểm tra xác thực trung gian, khó gỡ lỗi và làm phóng đại các lỗi ảo tưởng (hallucination).

| Giai đoạn (Stage) | Đầu Vào (Input) | Đầu Ra (Output) | Xác Thực Quan Trọng (Key Validation) |
|---|---|---|---|
| **1. Concept Extraction** | Sách giáo khoa & Chương trình học | Concept Graph | Độ bao phủ so với chuẩn MOET |
| **2. Objective Gen** | Concept Graph | Mục tiêu gắn nhãn Bloom's | Kiểm tra tính khả thi (Actionability check) |
| **3. Activity Design** | Các mục tiêu | Tiến trình hoạt động theo thời gian | Tổng thời gian <= 45 phút |
| **4. Content Dev** | Bản phác thảo hoạt động | Kịch bản & Nội dung Slide | Sự đồng bộ về thuật ngữ |
| **5. Media Gen** | Kịch bản & Văn bản Slide | Hướng dẫn lab & Prompts hoạt cảnh | Khớp nối kịch bản (Narrative match) |
| **6. Evaluation Review** | Trọn bộ gói bài giảng | Review trên UI của giáo viên | Chốt kiểm soát Human-in-the-loop |

---

### Phần 1.5: Ánh Xạ Lên Hệ Sinh Thái Tác Nhân AI Hiện Đại (Agentic Stack)

ConnectED là một triển khai sản xuất thực tế hoàn chỉnh của **Modern Agentic Stack** được mô tả trong Phần II. Các lớp được ánh xạ như sau:

* **Lớp 1: Điều phối (Orchestration):** Được quản lý bởi một bộ điều phối máy trạng thái tùy chỉnh (custom state machine). Điều hướng deterministic này được ưu tiên hơn các generic multi-agent frameworks (như LangChain hay CrewAI) nhằm đảm bảo quy trình soạn bài luôn tuân thủ đúng trình tự của mô hình ADDIE mà không lo rò rỉ trạng thái giữa các bước.
* **Lớp 2: Nhân tố Lập luận (Reasoning Core):** Sử dụng cơ chế định tuyến mô hình lai (hybrid model routing) kết hợp định tuyến ngữ nghĩa (Semantic Routing). Việc trích xuất khái niệm và thiết kế sư phạm được giao cho **Claude 4.6 Sonnet / DeepSeek-R1** (mô hình lớn/lập luận sâu), trong khi các tác vụ định dạng, dịch thuật từ vựng và gắn thẻ metadata được xử lý bởi **Llama 3.3 70B / Gemini 2.5 Flash** (mô hình nhỏ/tiện ích) để cắt giảm 70% chi phí vận hành và giảm độ trễ đầu cuối 45%.
* **Lớp 3: Kỹ năng (Skills):** Mỗi bước trong luồng soạn giáo án là một gói kỹ năng riêng biệt, có tính cô lập và quản lý phiên bản trong Git (chứa prompts hệ thống, templates và lược đồ JSON validation).
* **Lớp 4: Công cụ & Giao thức (Tools & Protocols):** Sử dụng giao thức **Model Context Protocol (MCP)** để cung cấp quyền truy cập an toàn vào kho sách giáo khoa và phân phối chương trình học. Đối với việc mua bản quyền học liệu trực quan STEM, tác nhân sử dụng giao thức thanh toán **Agent Payments Protocol (AP2)** để thanh toán các vi giao dịch một cách an toàn dựa trên Ý định Ủy quyền (Intent Mandates) được ký mã hóa bởi giáo viên.
* **Lớp 5: Hệ thống Bộ nhớ (Memory Systems):** Sử dụng bộ nhớ dài hạn vector (Vector DB lưu trữ hồ sơ và phong cách giảng dạy yêu thích của giáo viên) và bộ nhớ ngắn hạn episodic (lưu giữ trạng thái phiên soạn giáo án hiện tại để khôi phục nhanh khi xảy ra lỗi).

---

### Phần 1.6: Ánh Xạ Vòng Lặp Tác Nhân Cốt Lõi (Core Agentic Loop)

Mỗi giai đoạn trong quy trình phân cấp của ConnectED tự vận hành một vòng lặp nhận thức nội bộ:
1. **PLAN:** Lên kế hoạch cấu trúc chi tiết cho phần bài giảng đang soạn thảo.
2. **ACT:** Gọi mô hình lập luận core với schemas và dữ liệu sách giáo khoa.
3. **OBSERVE:** Kiểm tra kết quả đầu ra qua các cổng validation (ví dụ: xác thực tổng thời gian hoạt động có vượt quá 45 phút hay không).
4. **REFLECT & ITERATE:** Nếu kiểm tra thất bại (ví dụ: thời gian quá dài), tác nhân sẽ tự suy ngẫm xem phần nào cần cắt ngắn, viết lại hoạt động đó và tiến hành kiểm tra lại. Nếu thất bại quá 3 lần, nó sẽ kích hoạt leo thang (escalate) đến giáo viên hoặc rollback trạng thái.

---

### Phần 1.7: Giải Quyết Các Thách Thức Vận Hành Thực Tế

ConnectED là một dự án tham chiếu thực tế giúp vượt qua các rào cản sản xuất của hệ tác nhân AI:
* **Độ tin cậy:** Nhờ áp dụng xác thực JSON schema ở ranh giới giữa mỗi giai đoạn, các dữ liệu lỗi được phát hiện và sửa đổi lập tức trước khi lan rộng ra toàn bộ hệ thống.
* **Đánh giá (Evaluation):** Khung đánh giá offline chạy các bài test tự động thông qua cơ chế LLM-as-judge (sử dụng Claude 4.6 Sonnet làm giám khảo sư phạm) để chấm điểm chất lượng trước khi cập nhật mã nguồn mới.
* **Chi phí & Độ trễ:** Đặt các prompts hệ thống chương trình học MOET nặng lên đầu ngữ cảnh để tối ưu hóa tính năng prompt caching, giúp giảm đến 80% chi phí token đầu vào.
* **Khả năng giám sát (Observability):** Xuất toàn bộ cây thực thi chi tiết sang các công cụ AgentOps để nhóm phát triển dễ dàng giám sát thời gian, chi phí và từng cặp prompt/response lỗi.
