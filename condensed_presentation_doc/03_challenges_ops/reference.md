# **Các Thách Thức Trong Agentic AI & Giải Pháp Thực Tế**

## **Tổng Quan**
Xây dựng hệ thống tác nhân AI đi vào production đối mặt với bốn nhóm thách thức lớn. Mỗi thách thức đều có biểu hiện lỗi đặc trưng và giải pháp kỹ thuật cụ thể — không phải lý thuyết, mà là các pattern đã được kiểm chứng trong thực tế.

---

| Thách Thức | Biểu Hiện Lỗi Thực Tế | Giải Pháp Kỹ Thuật |
|:---|:---|:---|
| **Độ Tin Cậy & Ảo Tưởng** | Vòng lặp vô hạn, định dạng dữ liệu lỗi, gọi sai công cụ, lỗi trung gian lan truyền qua nhiều bước. | **Xác thực Schema Nghiêm Ngặt:** Ép cấu trúc đầu ra JSON bằng Pydantic. Tự động phản hồi lỗi để tác nhân tự sửa (tối đa 3 lần) trước khi kích hoạt HITL. |
| **Đánh Giá (Evaluation)** | Benchmark truyền thống chỉ đánh giá đầu ra cuối, không đánh giá được chuỗi hành động đa bước. | **Trajectory Eval & LLM-as-Judge:** Ghi nhật ký toàn bộ hành trình thực thi. Dùng mô hình độc lập chấm điểm theo rubrics chuẩn hóa. |
| **Chi Phí & Độ Trễ** | Số lượng lớn cuộc gọi suy luận lặp lại đẩy chi phí token và độ trễ tăng theo cấp số nhân. | **Prompt Caching & Định Tuyến Phân Tầng:** Prompts hệ thống cố định ở đầu ngữ cảnh; định tuyến linh hoạt sang mô hình nhỏ cho tác vụ đơn giản. |
| **Khả Năng Giám Sát (AgentOps)** | Luồng lập luận ngôn ngữ tự nhiên là "hộp đen" — không thể debug bằng công cụ truyền thống. | **Structured Tracing:** Tích hợp MLflow/AgentOps ghi spans, inputs, outputs, token và độ trễ. Hỗ trợ replay lại trajectory lỗi trong sandbox. |

---

## **Kết Luận**
Thành công của hệ thống tác nhân AI trong thực tế phụ thuộc nhiều vào **tính nghiêm ngặt trong kiến trúc và khả năng giám sát vận hành**, chứ không chỉ là năng lực thô của mô hình ngôn ngữ. Một hệ thống production tốt cần:

- **Orchestration có tính xác định** — máy trạng thái kiểm soát từng chuyển đổi trạng thái.
- **Skills đóng gói độc lập** — tri thức nghiệp vụ module hóa, quản lý phiên bản.
- **Giao thức chuẩn hóa** — MCP, AP2 làm cầu nối với thế giới bên ngoài.
- **Định tuyến thông minh** — phân bổ đúng mô hình cho đúng tác vụ.
- **Human-in-the-loop** — con người giữ quyền kiểm soát cuối cùng ở những điểm rủi ro cao.
