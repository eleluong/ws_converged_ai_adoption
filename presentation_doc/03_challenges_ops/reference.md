# Các Thách Thức Kéo Dài Trong Agentic AI (Persistent Challenges)

## Độ Tin Cậy (Reliability)
Các tác nhân (agents) chạy thực tế (production) thường thất bại theo những cách khó dự đoán và có tính dây chuyền.
* **Các dạng lỗi (Failure Modes):** Ảo tưởng tham số công cụ (hallucinated tool parameters), vòng lặp lập luận vô hạn, trôi dạt hướng dẫn (instruction drift) và sự điều phối mong manh giữa các tác nhân.
* **Giải pháp:**
  * **Các lớp xác thực (Verification Layers):** Kiểm tra cấu trúc (schema checks) dữ liệu đầu ra giữa các giai đoạn.
  * **Rào chắn cứng (Hard Guardrails):** Từ chối các hành động trái phép ngay ở cấp độ hệ thống.
  * **Chuyển giao cho con người (Human Escalation):** Xác định rõ ràng các điều kiện chuyển giao cho con người kiểm soát.

---

## Đánh Giá (Evaluation)
Đánh giá các hệ thống tác nhân (agentic systems) khó hơn nhiều so với việc so sánh văn bản đơn thuần:
* **Bài Toán Quỹ Đạo (The Trajectory Problem):** Bạn phải đánh giá toàn bộ lộ trình thực thi (các bước lập luận, cuộc gọi công cụ) thay vì chỉ đánh giá câu trả lời cuối cùng.
* **Các Chiều Đo Lường Cốt Lõi:** Hiệu quả quỹ đạo (trajectory efficiency), chất lượng phục hồi sau lỗi (error recovery quality), sự tuân thủ an toàn (safety compliance) và chi phí.
* **Các phương pháp:** Chấm điểm bằng mô hình (LLM-as-judge scoring), các bộ kiểm thử hồi quy (regression test suites), mô phỏng môi trường cô lập (sandboxed simulations) và các kiểm tra đối nghịch (adversarial checks).

---

## Chi Phí & Độ Trễ (Cost & Latency)
Các vòng lặp tác nhân tạo ra chi phí vận hành rất lớn:
* **Các nút thắt cổ chai (Bottlenecks):** Phải thực hiện từ 10–50 cuộc gọi suy luận tuần tự, tích lũy cửa sổ ngữ cảnh lớn và lặp lại việc thực thi công cụ nhiều lần.
* **Tối ưu hóa:**
  * Caching các prompts lặp lại (giảm chi phí từ 50-90%).
  * Định tuyến mô hình theo nhiệm vụ (sử dụng các mô hình 8B giá rẻ để định tuyến/lọc dữ liệu).
  * Tóm tắt và nén ngữ cảnh (context summarization and compression).

---

## Khả Năng Quan Sát Và AgentOps (Observability and AgentOps)
Các công cụ DevOps truyền thống thất bại vì trạng thái của tác nhân được thể hiện bằng lập luận ngôn ngữ tự nhiên.
* **Nhu Cầu Của AgentOps:** 
  * Gỡ lỗi phát lại (Replay debugging) đối với các quỹ đạo thất bại.
  * Theo dõi chi tiết lượng token và độ trễ từng bước một.
  * Nhật ký prompt và kiểm toán các lượt gọi công cụ.
* **Các Nền Tảng Phổ Biến:** LangSmith, Helicone, Langfuse, Phoenix.

---

## Kết Luận (Conclusion)
Sự thành công của AI trong thế giới thực phụ thuộc vào các hệ thống xung quanh nhiều hơn là năng lực thô của bản thân mô hình:
* Dịch chuyển sự tập trung từ kỹ nghệ prompt (prompt engineering) sang **Kiến Trúc Hệ Thống (System Architecture)**.
* Neo các ứng dụng vào các lĩnh vực chuyên biệt (như ConnectED).
* Đầu tư mạnh mẽ vào **Sự Nghiêm Ngặt Trong Đánh Giá (Evaluation Rigor)** và **Khả Năng Quan Sát (Observability)** ngay từ ngày đầu tiên.
