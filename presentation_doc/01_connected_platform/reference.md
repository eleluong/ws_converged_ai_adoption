# ConnectED: Một Nền Tảng AI-Native Cho Giáo Dục Việt Nam

## Tổng Quan (Overview)
ConnectED là một nền tảng soạn giáo án tích hợp AI được thiết kế đặc biệt cho hệ thống giáo dục K–12 Việt Nam.
* **Mục Tiêu Cốt Lõi (Core Goal):** Tăng tốc quy trình thiết kế bài giảng chất lượng cao từ vài giờ xuống còn vài phút.
* **Sản Phẩm Đầu Ra:** Các giáo án chuẩn chương trình giáo dục phổ thông mới, slide bài giảng, tài liệu giảng dạy và phòng thí nghiệm ảo (virtual labs).
* **Cách Tiếp Cận (Approach):** Định hình việc tạo nội dung bằng AI theo các quy trình nghiệp vụ sư phạm thực tế tại địa phương thay vì sử dụng các one-shot prompts chung chung.

---

## Bối Cảnh Vấn Đề (Problem Context)
Để chuẩn bị một bài giảng chất lượng cao hoàn chỉnh, giáo viên phải mất từ **3 đến 4 tiếng** làm việc thủ công. Các mô hình ngôn ngữ lớn chung chung (như ChatGPT) thường thất bại khi triển khai thực tế trong lớp học vì:
* **Sự Phù Hợp Chương Trình Kém (Weak Curriculum Alignment):** Đưa ra các chủ đề ngoài sách giáo khoa.
* **Trình Tự Không Chính Xác (Inaccurate Sequencing):** Luồng sư phạm nghèo nàn.
* **Thiếu Bản Địa Hóa (Lack of Localization):** Giả định và thuật ngữ mang tính phương Tây.
* **Thiết Kế Hoạt Động Mơ Hồ (Vague Activity Design):** Các nhiệm vụ trong lớp không khả thi.
* **Nội Dung Bị Ảo Tưởng (Hallucinated Content):** Tham chiếu thông tin thực tế sai lệch.

*Bài học:* AI trong giáo dục phải được bản địa hóa sâu sắc (localized) và được xây dựng trên nền tảng sư phạm vững chắc (pedagogically grounded).

---

## Nền Tảng Thiết Kế Sư Phạm: ADDIE (Instructional Design Foundation)
Thay vì tạo nội dung một lần duy nhất, ConnectED chia nhỏ quy trình soạn bài giảng bằng mô hình **ADDIE**:

1. **Phân Tích (Analyze):** Xử lý sách giáo khoa/chương trình học để trích xuất các khái niệm cốt lõi (core concepts), kết quả học tập mong đợi (learning outcomes) và kiến thức tiền đề (prerequisites).
2. **Thiết Kế (Design):** Tạo cấu trúc bài học, các hoạt động, phân bổ thời gian và chiến lược đánh giá.
3. **Phát Triển (Develop):** Tạo các tài nguyên đa phương tiện bằng quy trình **Script-First Workflow** (tạo kịch bản lời thoại trước khi thiết kế hình ảnh) để đảm bảo tính nhất quán.
4. **Triển Khai & Đánh Giá (Implement & Evaluate):** Duy trì các chốt kiểm duyệt **Human-in-the-Loop** để giáo viên xem xét, tinh chỉnh và điều chỉnh.

---

## Quy Trình Xử Lý Đa Tác Nhân Phân Cấp (Hierarchical Agent Pipeline)
ConnectED tránh sử dụng các prompts nguyên khối lớn (monolithic prompts), thay vào đó sử dụng một **hierarchical agent pipeline** chuyên biệt:

```
[Concept Extraction] -> [Objective Gen] -> [Activity Design] -> [Content Dev] -> [Visuals] -> [Teacher Review]
```

**Lợi Ích Của Việc Phân Rã (Benefits of Decomposition):**
* Giảm độ phức tạp của prompt và hạ thấp tỷ lệ ảo tưởng (hallucination).
* Dễ dàng xác thực các kết quả trung gian.
* Gỡ lỗi theo từng module và đảm bảo tính nhất quán sư phạm mạnh mẽ.

---

## Phòng Thí Nghiệm Ảo Và Học Tập Tương Tác (Virtual Labs and Interactive Learning)
ConnectED tích hợp các hướng dẫn thí nghiệm ảo và mô phỏng (Vật lý, Hóa học, Sinh học) cho việc học STEM:
* **Hỗ Trợ Cơ Sở Vật Chất (Infrastructure Support):** Thu hẹp khoảng cách cho các trường học thiếu thiết bị thí nghiệm vật lý thực tế.
* **Học Tập Khám Phá (Exploratory Learning):** Kết nối các hình ảnh tương tác trực quan với các mục tiêu cụ thể trong sách giáo khoa.
* **Hỗ Trợ Sư Phạm Từ AI (AI Scaffolding):** Các hướng dẫn có cấu trúc giúp học sinh thực hiện các quan sát và rút ra kết luận.

---

## Bản Địa Hóa Như Một Nguyên Tắc Cốt Lõi (Localization as a Core Principle)
Bản địa hóa được coi là kiến trúc nền tảng, chứ không chỉ là một lớp dịch thuật (translation wrapper) bên ngoài:
* **Tích Hợp Sâu Sắc (Deep Integration):** Cấu trúc chương trình học tại địa phương, kỳ vọng ngôn ngữ và hệ thống đánh giá điểm số được nhúng trực tiếp vào các prompts và templates.
* **Bối Cảnh Văn Hóa (Cultural Context):** Sử dụng tên tiếng Việt, lịch sử địa phương và các tình huống thực tế của vùng miền cho các hoạt động lớp học.
* **Tính Bản Địa (Authenticity):** Mang lại các kết quả đầu ra tạo cảm giác tự nhiên và thân thuộc đối với các nhà giáo dục Việt Nam.

---

## Tác Động (Impact)
ConnectED thay đổi hoàn toàn việc soạn giáo án bài học:
* **Giảm Thời Gian (Time Reduction):** Thời gian chuẩn bị giảm từ **3-4 giờ** xuống còn **15-20 phút**.
* **Các Bài Học Cốt Lõi (Core Insights):** AI giáo dục chỉ thực sự hiệu quả khi:
  1. Sư phạm được nhúng trực tiếp vào kiến trúc hệ thống (pedagogy embedded in architecture).
  2. Quy trình làm việc được phân rã theo dạng phân cấp (hierarchically decomposed).
  3. Giáo viên được giữ vai trò kiểm duyệt (teachers remain in the loop).
  4. Bản địa hóa đóng vai trò như một hạ tầng nền tảng (localization is foundational infrastructure).
