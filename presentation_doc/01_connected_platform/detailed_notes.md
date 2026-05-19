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

### Phần 1.5: Tích Hợp Phòng Thí Nghiệm Ảo (Virtual Labs Integration)
* **Cấu Trúc Sư Phạm:** Các phòng thí nghiệm ảo là các chuỗi hoạt động có cấu trúc (thiết lập, quy trình, kết quả mong đợi, phiếu bài tập) chứ không phải các mô phỏng không có cấu trúc.
* **Tích Hợp Quy Trình (Pipeline Integration):** Được tạo trong giai đoạn *Develop*, liên kết chính xác với kiến thức tiền đề từ Stage 1.
* **Tác Động Bình Đẳng Giáo Dục (Equity Impact):** Giải quyết tình trạng thiếu thiết bị tại khoảng 30% trường học Việt Nam chưa có hạ tầng phòng thí nghiệm vật lý thực tế.

---

### Phần 1.6: Các Cấp Độ Bản Địa Hóa (Localization Spectrum)
Bản địa hóa được tích hợp như một hạ tầng nền tảng hơn là một lớp dịch thuật đơn giản:
* **Bề mặt (Surface):** Dịch thuật sang tiếng Việt.
* **Thuật ngữ (Terminology):** Áp dụng các thuật ngữ MOET tiêu chuẩn.
* **Sư phạm (Pedagogical):** Điều chỉnh các hoạt động cho phù hợp với các lớp học sĩ số lớn và công nghệ hỗ trợ còn hạn chế tại địa phương.
* **Văn hóa (Cultural):** Tham chiếu lịch sử Việt Nam, danh lam thắng cảnh và tên gọi vùng miền.
* **Pháp lý (Regulatory):** Ánh xạ các đánh giá sang khung năng lực của MOET.

---

### Phần 1.7: Các Bài Học Cốt Lõi (Core Takeaways)
ConnectED chứng minh 4 nguyên tắc thiết kế kỹ thuật AI cốt lõi:
1. **Domain Grounding:** Loại bỏ hiện tượng ảo tưởng (hallucinations).
2. **Hierarchical Decomposition:** Tăng cường khả năng gỡ lỗi hệ thống.
3. **Human-in-the-loop:** Duy trì niềm tin và xử lý tốt các tình huống biên (edge cases).
4. **Localization as Moat:** Tạo ra giá trị vượt trội cho nhóm người dùng mục tiêu.
