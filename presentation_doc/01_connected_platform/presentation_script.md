# Kịch Bản Thuyết Trình Workshop
## ConnectED: Một Nền Tảng AI-Native Cho Giáo Dục Việt Nam

> **Format:** Phần I | khoảng 35 phút tổng cộng  
> **Người nghe:** Nhà phát triển, Quản lý sản phẩm (PMs), Nhà nghiên cứu và Nhà giáo dục  

---

## DANH SÁCH KIỂM TRA TRƯỚC BUỔI NÓI CHUYỆN (PRE-TALK CHECKLIST)
- [ ] Các slide đã được tải lên giao diện UI và trình chiếu trên màn hình
- [ ] Môi trường Demo hoạt động bình thường (Giao diện ConnectED UI/Trace viewer)
- [ ] Đồng hồ đếm giờ của người thuyết trình đã hiển thị

---

## MỞ ĐẦU (OPENING) (3 phút)

### Slide 1: Slide Tiêu Đề (Title Slide)
**Visual:** Slide tiêu đề sạch sẽ với logo nền tảng: "ConnectED: AI-Native Lesson Planning"

**Script:**
> "Một giáo viên mất bao nhiêu thời gian để chuẩn bị cho một tiết học? Thông thường là 3 đến 4 tiếng. Cho mỗi một tiết học duy nhất."
> "Hôm nay, chúng ta sẽ tìm hiểu cách thức hệ thống điều phối AI chuyên biệt theo lĩnh vực (domain-specific AI orchestration) có thể cắt giảm gánh nặng này xuống còn vài phút, và những bài học kiến trúc hệ thống áp dụng cho tất cả các hệ thống doanh nghiệp (enterprise systems)."

**Transition:** "Hãy cùng giới thiệu về nền tảng."

---

## PHẦN I — ConnectED (30 phút)

### Slide 2: ConnectED là gì?
**Visual:** Một hàng gồm ba biểu tượng: Giáo án (Lesson Plans) | Slide kèm thuyết minh (Narrated Slides) | Phòng thí nghiệm ảo STEM (STEM Virtual Labs)

* Nền tảng soạn giáo án AI-native cho giáo dục K-12 tại Việt Nam.
* Tạo ra các tài liệu học tập chuẩn chương trình học và các phòng thí nghiệm ảo.
* Mục tiêu: Giảm tải khối lượng công việc chuẩn bị trong khi vẫn giữ quyền kiểm soát sư phạm của con người (human pedagogical control).

**Script:**
> "ConnectED không phải là một trình tạo nội dung bằng một prompt duy nhất (single prompt generator). Nó là một hệ thống đa tác nhân có cấu trúc (structured agentic system) được thiết kế để tạo ra các bài giảng chuẩn chương trình học, kịch bản slide và hướng dẫn phòng thí nghiệm ảo."

---

### Slide 3: Vấn Đề — Khối Lượng Công Việc Của Giáo Viên (Teacher Workload)
**Visual:** Sơ đồ phân bổ thời gian chuẩn bị bài học:
* Xác định mục tiêu (Objective formulation): khoảng 30 phút
* Trích xuất khái niệm (Concept extraction): khoảng 45 phút
* Thiết kế hoạt động (Activity design): khoảng 40 phút
* Tạo hình ảnh trực quan (Visual creation): khoảng 45 phút
* Sơ đồ đánh giá kiểm tra (Assessment mapping): khoảng 30 phút
* **Tổng cộng: 3-4 Tiếng**

**Script:**
> "Khi phân tích quy trình soạn bài, chúng tôi nhận ra đây không phải là một tác vụ đơn lẻ mà là một chuỗi các kỹ năng nhận thức khác nhau. Các LLMs thông dụng (out-of-the-box LLMs) không thể đáp ứng được thực tế phức tạp này."

---

### Slide 4: Tại Sao Các LLM Chung Chung Thất Bại (Why Generic LLMs Fall Short)
**Visual:** Các so sánh có độ tương phản cao:
* **Thiên lệch phương Tây (Western Bias):** Mặc định theo chương trình nước ngoài (ví dụ: US Common Core).
* **Không tương thích thiết bị (Equipment Mismatch):** Gợi ý các thiết bị phòng thí nghiệm không có sẵn.
* **Thiếu bản địa hóa (Lack of Localization):** Bỏ qua các tên gọi, lịch sử địa phương và các tiêu chuẩn của Bộ Giáo dục (MOET).
* **Ảo tưởng (Hallucinations):** Tự tạo ra các trình tự sư phạm không thực tế.

**Script:**
> "Các mô hình chung chung sẽ mặc định hoạt động theo dữ liệu mà chúng được huấn luyện. Để thành công, chúng ta phải đối chiếu và neo chúng vào bối cảnh địa phương ngay từ cấp độ kiến trúc hệ thống."

---

### Slide 5: ADDIE — Xương Sống Thiết Kế Hệ Thống
**Visual:** Vòng lặp thể hiện: Phân tích (Analyze) -> Thiết kế (Design) -> Phát triển (Develop) -> Triển khai (Implement) -> Đánh giá (Evaluate)

**Script:**
> "Chúng tôi giải quyết vấn đề này bằng cách nhúng trực tiếp mô hình thiết kế sư phạm ADDIE đã được chứng minh vào kiến trúc AI. Mỗi giai đoạn của ADDIE sẽ tương ứng với một giai đoạn AI riêng biệt."

---

### Slide 6: Đi Sâu Vào Các Giai Đoạn ADDIE
**Visual:** Bảng phân tích hai cột:
* **Analyze & Design:** Sách giáo khoa được xử lý thành đồ thị khái niệm (concept graphs); bản phác thảo bài giảng được lập bản đồ giới hạn trong 45 phút tiết học tiêu chuẩn.
* **Develop & Implement:** Các tài nguyên truyền thông được tạo ra. Sử dụng quy trình *Script-First Workflow* (tạo lời thoại thuyết minh trước khi thiết kế hình ảnh). Giáo viên xem xét và tinh chỉnh lại.

**Script:**
> "Bằng cách tạo kịch bản lời thoại trước khi thiết kế các hình ảnh trực quan, chúng tôi đã cải thiện đáng kể tính nhất quán và sự liên kết chặt chẽ giữa các slide được tạo ra và tài liệu thực hành thí nghiệm."

---

### Slide 7: Quy Trình Xử Lý Đa Tác Nhân Phân Cấp (Hierarchical Agent Pipeline)
**Visual:** Sơ đồ luồng quy trình:
`Concept Extraction -> Objective Gen -> Activity Design -> Content Dev -> Media Gen -> Human Review`

* **Tại Sao Cần Phân Rã?**
  * Giảm bão hòa ngữ cảnh (context saturation) cho mỗi cuộc gọi mô hình.
  * Có các điểm kiểm tra xác thực trung gian (intermediate validation checkpoints).
  * Thay thế các prompts mơ hồ bằng khả năng gỡ lỗi theo từng module.

**Script:**
> "Chúng tôi chia nhỏ một vấn đề lớn thành sáu bước đã được xác thực. Nếu bước 1 thất bại, chúng tôi sẽ phát hiện và sửa chữa ngay trước khi nó làm ảnh hưởng xấu đến bước 5."

---

### Slide 8: Phòng Thí Nghiệm Ảo STEM (STEM Virtual Labs)
**Visual:** Ảnh chụp màn hình các hướng dẫn phòng thí nghiệm ảo tương tác:

* Phác thảo các bước tiến hành, hiện tượng quan sát mong đợi và các bảng số liệu.
* Thiết kế đặc biệt dành cho khoảng 30% số trường học đang thiếu thốn thiết bị thí nghiệm vật lý thực tế.
* Được gắn kết chặt chẽ với các mục tiêu của bài học.

**Script:**
> "Phòng thí nghiệm ảo là một công cụ bình đẳng giáo dục rất quan trọng. Chúng tôi tạo ra các tài liệu hướng dẫn có cấu trúc để dẫn dắt học sinh thực hành các thí nghiệm ngay cả khi không có thiết bị vật lý."

---

### Slide 9: Bản Địa Hóa Là Cơ Sở Hạ Tầng (Localization is Infrastructure)
**Visual:** Các lớp cốt lõi của bản địa hóa:
* System Prompts (các tiêu chuẩn chương trình học)
* Templates (cấu trúc đánh giá điểm số)
* Terminologies (thuật ngữ tiêu chuẩn của MOET)
* Bối cảnh văn hóa (tên gọi vùng miền, lịch sử Việt Nam)

**Script:**
> "Bản địa hóa không phải là bước xử lý sau khi dịch (post-processing). Nó là cơ sở hạ tầng. Hãy đối xử với nó như một ràng buộc kiến trúc cốt lõi ngay từ ngày đầu tiên."

---

### Slide 10: Tác Động & Góc Nhìn Thực Tế (Impact & Insights)
**Visual:** Chữ lớn nổi bật: **15 Phút** (so với 3 Tiếng)

* Tiết kiệm thời gian: 85-90% cho mỗi bài học.
* Giải phóng 75-90 giờ làm việc cho mỗi giáo viên trong mỗi học kỳ.
* Quy tắc cốt lõi: Chuyển dịch từ các mô hình biệt lập sang các hệ thống được điều phối và bản địa hóa tốt (orchestrated, localized systems).

**Script:**
> "ConnectED chứng minh rằng việc chuyển đổi từ các prompts thô sơ sang các hệ thống được điều phối chặt chẽ chính là chìa khóa để tạo ra tác động AI thực tế trong thế giới thực."
