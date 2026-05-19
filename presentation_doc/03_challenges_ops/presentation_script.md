# Kịch Bản Thuyết Trình Workshop
## Phần III: Các Thách Thức & Kết Luận

> **Format:** Phần III & Kết luận | khoảng 15 phút tổng cộng  
> **Người nghe:** Nhà phát triển, Quản lý sản phẩm (PMs), Nhà nghiên cứu và Kỹ sư  

---

## PHẦN III — Các Thách Thức Kéo Dài (Persistent Challenges)

### Slide 19: Các Bài Toán Khó Của Tác Nhân Chạy Thực Tế (Production Agents)
**Visual:** Bố cục bốn góc phần tư:
* **Độ tin cậy (Reliability):** lỗi chuỗi, vòng lặp vô hạn, trôi dạt ngữ cảnh. (Giải pháp: Kiểm tra lược đồ schema, cơ chế dự phòng).
* **Đánh giá (Evaluation):** kiểm thử quỹ đạo thực thi (trajectory testing) so với kiểm thử đầu ra. (Giải pháp: LLM làm giám khảo, chạy mô phỏng).
* **Chi phí & Độ trễ (Cost & Latency):** các chuỗi suy luận tuần tự. (Giải pháp: định tuyến, prompt caching).
* **Khả năng quan sát (Observability):** nhật ký trạng thái bằng ngôn ngữ tự nhiên. (Giải pháp: nền tảng AgentOps).

**Script:**
> "Xây dựng một bản demo tác nhân thì dễ; làm cho nó đạt tiêu chuẩn chạy thực tế (production-grade) là vô cùng khó khăn. Các lỗi phát sinh thường âm thầm và cộng dồn lại theo thời gian."

---

## KẾT LUẬN (CLOSING)

### Slide 20: Các Bài Học Then Chốt (Key Takeaways)
**Visual:** Danh sách được đánh số:
1. **Phân rã các vấn đề theo phân cấp (Decompose problems hierarchically):** Các prompts nguyên khối lớn (monolithic prompts) không thể mở rộng quy mô.
2. **Bản địa hóa là cơ sở hạ tầng (Localization is infrastructure):** Đây là yêu cầu thiết kế hệ thống cốt lõi, không phải là một bản dịch vá víu bên ngoài.
3. **Giữ con người trong vòng lặp (Keep humans in the loop):** Tối quan trọng cho sự an toàn, kiểm soát chất lượng và niềm tin của người dùng.
4. **Thiết kế hệ thống, không phải viết prompts (Design systems, not prompts):** Mô hình ngôn ngữ chỉ là một lớp trong thời gian chạy (runtime).
5. **Tác nhân được quan sát là tác nhân đáng tin cậy:** Thiết lập hệ thống AgentOps ngay từ ngày đầu tiên.

**Script:**
> "Nếu ngày hôm nay các bạn chỉ mang về một bài học duy nhất, thì hãy là điều này: hãy ngừng viết những prompts dài hơn. Hãy bắt đầu xây dựng những kiến trúc hệ thống tốt hơn. Hãy phân rã các đường ống (pipelines) của bạn, cô lập các chuyên môn (skills) và giám sát chặt chẽ các đường dẫn thực thi."

---

### Slide 21: Câu Hỏi Thảo Luận (Discussion Prompts)
**Visual:** Danh sách các đầu dòng:
* Quy trình công việc nào của bạn có thể hưởng lợi từ mô hình quy trình xử lý đa tác nhân phân cấp (hierarchical agent pipeline)?
* Đâu là những "điểm tối" trong khả năng giám sát (observability) của đường ống dẫn AI hiện tại của bạn?
* Một gói "Skill" có thể tái sử dụng sẽ trông như thế nào trong lĩnh vực nghiệp vụ của tổ chức bạn?

**Script:**
> "Cảm ơn các bạn. Chúng ta hãy cùng mở đầu phần Hỏi & Đáp (Q&A) và thảo luận xem các mô hình kiến trúc này ánh xạ vào các dự án của riêng các bạn như thế nào."
