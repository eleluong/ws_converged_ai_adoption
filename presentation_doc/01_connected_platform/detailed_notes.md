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
* **Quyết Định Thiết Kế (Design Decision) (đã cập nhật):**  
  Mặc dù phương pháp chính của ConnectED vẫn là kỹ thuật prompt kết hợp template và đối chiếu chương trình học (grounding) – vốn dễ bảo trì và cập nhật khi chương trình thay đổi – nhóm phát triển cũng nhận thấy các tác vụ lập luận trọng tâm (như trích xuất khái niệm và suy luận sư phạm đa bước) sẽ được cải thiện mạnh nếu có một mô hình riêng được huấn luyện bài bản. Thay vì huấn luyện từ đầu, nhóm đã phát triển một **mô hình LLM tùy chỉnh cho giáo dục Việt Nam** dựa trên **Qwen 3 8B**, sử dụng học tăng cường (RL) để điều chỉnh hành vi và tối ưu hóa sở thích trực tiếp (DPO) trên các tập dữ liệu nền tảng. Mô hình này đạt kết quả cao nhất trên bộ thi AIThucchien cho các tác vụ lập luận (xem chi tiết tại Phần 1.8).

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
* **Lớp 2: Nhân tố Lập luận (Reasoning Core):** Sử dụng cơ chế định tuyến mô hình lai (hybrid model routing) kết hợp định tuyến ngữ nghĩa (Semantic Routing). Việc trích xuất khái niệm và thiết kế sư phạm được giao cho **Claude 4.6 Sonnet / DeepSeek-R1** (mô hình lớn/lập luận sâu), trong khi các tác vụ định dạng, dịch thuật từ vựng và gắn thẻ metadata được xử lý bởi **Llama 3.3 70B / Gemini 2.5 Flash** (mô hình nhỏ/tiện ích) để cắt giảm 70% chi phí vận hành và giảm độ trễ đầu cuối 45%. Đối với các tác vụ lập luận giáo dục Việt Nam cốt lõi, hệ thống có thể chuyển sang sử dụng mô hình tùy chỉnh **Qwen 3 8B** (được mô tả chi tiết tại Phần 1.8).
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

---

### Phần 1.8: Mô Hình LLM Tùy Chỉnh Cho Giáo Dục Việt Nam — Qwen 3 8B

Dù pipeline đa tác nhân phân cấp kết hợp prompt engineering với các mô hình frontier đã rất hiệu quả, nhóm ConnectED còn tiến xa hơn khi phát triển **một mô hình LLM chuyên dụng cho giáo dục phổ thông Việt Nam** dựa trên **Qwen 3 8B**. Mô hình này không phải là chatbot đa năng, mà được tối ưu cho các tác vụ lập luận như trích xuất khái niệm, lập bản đồ tiên quyết và suy luận sư phạm đa bước.

#### 1.8.1 Mô Hình Nền và Chiến Lược Huấn Luyện: RL để Điều Chỉnh Hành Vi

Nhóm chọn **Qwen 3 8B** làm mô hình nền – một kiến trúc nhỏ gọn, hiệu quả, cân bằng giữa hiệu năng và chi phí suy luận. Thay vì huấn luyện từ đầu một mô hình hàng trăm tỷ tham số (quá tốn kém và đòi hỏi dữ liệu khổng lồ), nhóm áp dụng **Học Tăng Cường (Reinforcement Learning – RL) để điều chỉnh hành vi**. RL tinh chỉnh các mẫu ra quyết định và chuỗi suy luận (chain‑of‑thought) của mô hình trên các tác vụ giáo dục, giúp nó tuân theo quy trình ADDIE một cách đáng tin cậy hơn so với chỉ fine‑tuning có giám sát thông thường.

#### 1.8.2 Tập Dữ Liệu Nền Tảng (Grounded Datasets): Wikipedia Tiếng Việt, MetaMath và Hơn Thế Nữa

Để khắc phục tình trạng thiếu dữ liệu giáo dục Việt Nam chất lượng cao trong các LLM đại trà, nhóm đã xây dựng một **tập dữ liệu vàng (golden dataset)** bao gồm:
- **Wikipedia tiếng Việt** (đã được lọc và làm sạch theo các chủ đề giáo dục).
- **Metamath** (Vietnamese subset) – bộ sưu tập các bài toán, lời giải và suy luận từng bước bằng tiếng Việt.
- Các đoạn trích sách giáo khoa và đề thi quốc gia theo chuẩn MOET.

Các tập dữ liệu này phục vụ hai mục đích:
1. **Đối chiếu tri thức (Knowledge grounding):** Mô hình học thuật ngữ, bối cảnh văn hóa và các dữ kiện chương trình học chính xác của Việt Nam.
2. **Giảm ảo tưởng (Hallucination reduction):** Sử dụng kỹ thuật **Tối ưu hóa Sở thích Trực tiếp (Direct Preference Optimization – DPO)**, nhóm huấn luyện mô hình ưu tiên các câu trả lời trung thành với tập dữ liệu vàng, đồng thời loại bỏ các đầu ra có vẻ hợp lý nhưng sai sự thật. DPO là phương pháp alignment dựa trên sở thích, không cần mô hình thưởng/phạt riêng, giúp quá trình huấn luyện ổn định và hiệu quả hơn RLHF truyền thống.

#### 1.8.3 Kết Quả: Đạt Điểm Cao Nhất Trên Cuộc Thi AIThucchien

Mô hình Qwen 3 8B tùy chỉnh đã được đánh giá trên **cuộc thi AIThucchien** – bộ benchmark hàng đầu của Việt Nam cho AI lập luận giáo dục. Trên **tập kiểm tra riêng (private test set)** bao gồm các câu hỏi bám sát chương trình chưa từng thấy và các tác vụ lập luận đa bước, mô hình của ConnectED đã đạt **điểm số cao nhất** trong số tất cả các hệ thống tham gia.

Các thành tựu chính:
- **LLM chính xác nhất cho các tác vụ lập luận** khi bật chế độ “thinking mode” (chuỗi suy luận tường minh).
- Hiệu suất vượt trội trên các bài tập suy luận tiên quyết khái niệm, lập luận khoa học đa bước và ánh xạ mục tiêu theo MOET.
- Hầu như loại bỏ hoàn toàn các hiện tượng ảo tưởng (hallucination) trong các bản soạn bài so với các mô hình generic.

#### 1.8.4 Tích Hợp Vào Pipeline Của ConnectED

Mô hình Qwen 3 8B tùy chỉnh **không được dùng cho tất cả các giai đoạn**, mà hoạt động như một **engine lập luận chuyên dụng** cho các bước đòi hỏi độ chính xác cao nhất như trích xuất khái niệm và sinh mục tiêu bài học. Bộ điều phối (orchestrator) sẽ định tuyến động các bước này sang mô hình tùy chỉnh khi cần độ chính xác cao, và fallback về các mô hình frontier (Claude, DeepSeek) cho các tác vụ sáng tạo hoặc cần kiến thức rộng. Cách tiếp cận lai ghép này cân bằng giữa độ chính xác, chi phí và độ trễ.

**Bài học quan trọng:** Huấn luyện một LLM chuyên lĩnh vực bằng RL + DPO trên các tập dữ liệu nền tảng, bắt đầu từ một mô hình nền nhỏ gọn như Qwen 3 8B, là một giải pháp thay thế tiết kiệm chi phí so với huấn luyện từ đầu, đồng thời vẫn đạt kết quả state‑of‑the‑art trên các benchmark địa phương, dễ bảo trì và mở rộng khi chương trình giáo dục thay đổi.