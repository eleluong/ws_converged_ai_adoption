# Workshop — Tài Liệu Ghi Chú Chi Tiết
## Các Thách Thức Kéo Dài Trong Agentic AI (Persistent Challenges)

> Các ghi chú này cung cấp thông tin chi tiết nâng cao, các phân tích đánh đổi và các giải pháp thiết kế thực tế.

---

### Phần 3.1: Độ Tin Cậy (Reliability)
* **Tại sao lại khó:** Các lỗi của tác nhân lan truyền xuống các giai đoạn sau, các hành động (ví dụ: ghi vào cơ sở dữ liệu) thường không thể hoàn tác, và các mô hình có thể tự tin ảo tưởng về sự thành công của chúng.
* **Các Kỹ Thuật Then Chốt:**
  1. **Schema Validation (Xác thực Lược đồ):** Bắt buộc các cấu trúc dữ liệu ở các biên của từng giai đoạn.
  2. **Idempotency (Tính không đổi):** Đảm bảo an toàn khi gọi lại các công cụ bị lỗi.
  3. **Rollbacks (Hoàn tác):** Cho phép hoàn tác các hành động trung gian khi gặp sự cố.
  4. **Guardrails (Rào chắn):** Các giới hạn cứng (ví dụ: cấp quyền chỉ đọc đối với cơ sở dữ liệu).

---

### Phần 3.2: Đánh Giá (Evaluation)
Các bài thử nghiệm LLM truyền thống chỉ đánh giá câu trả lời cuối cùng. Các tác nhân yêu cầu **Đánh Giá Quỹ Đạo (Trajectory Evaluation)** (đánh giá từng bước thực thi trung gian).

| Tiêu Chí (Dimension) | Trọng Tâm (Focus) | Ví Dụ (Example) |
|---|---|---|
| **Hiệu quả (Efficiency)** | Độ dài quỹ đạo so với tối ưu | Tác nhân có thực hiện các cuộc gọi công cụ dư thừa không? |
| **Phục hồi (Recovery)** | Phản hồi lỗi mềm dẻo | Tác nhân có lập lại kế hoạch sau khi công cụ bị lỗi không? |
| **Tuân thủ (Compliance)** | Sự tuân thủ chính sách | Các ranh giới chỉ đọc (read-only) có được tôn trọng không? |
| **Chi phí (Cost)** | Token và chi phí vận hành | Chúng ta có cách nào làm tác vụ này rẻ hơn không? |

* **Cách tiếp cận:** Chấm điểm sử dụng LLM làm giám khảo (LLM-as-judge scoring), chạy mô phỏng trong môi trường cô lập, và chạy lại các kiểm thử lịch sử (replay tests).

---

### Phần 3.3: Chi Phí và Độ Trễ (Cost and Latency)
Các tác nhân rất tốn kém về tài nguyên tính toán, thường yêu cầu hàng chục lệnh gọi mô hình tuần tự.

| Chiến Lược (Strategy) | Cơ Chế (Mechanism) | Mức Tiết Kiệm Thông Thường |
|---|---|---|
| **Model Routing** | Chuyển tác vụ đơn giản tới mô hình nhỏ | Giảm 40–70% chi phí |
| **Prompt Caching** | Cache hệ thống prompts & tiêu chuẩn | Giảm 50–90% lượng input token |
| **Nén Ngữ Cảnh** | Tóm tắt lịch sử trò chuyện | Giảm 30–60% ngữ cảnh |
| **Song Song Hóa** | Chạy đồng thời các tác vụ phụ độc lập | Giảm 30–60% độ trễ |

---

### Phần 3.4: Khả Năng Quan Sát & AgentOps (Observability & AgentOps)
Trạng thái của tác nhân được biểu diễn bằng lập luận ngôn ngữ tự nhiên, khiến các chỉ số truyền thống (CPU, lỗi HTTP) trở nên không đủ đáp ứng.

| Khả Năng | DevOps Truyền Thống | AgentOps |
|---|---|---|
| **Tracing (Theo dấu)** | Ngăn xếp lệnh gọi hàm (call stacks) | Theo vết lập luận & dữ liệu vào/ra của công cụ |
| **Replay (Phát lại)** | Phát lại request | Mô phỏng lại toàn bộ quỹ đạo thực thi |
| **Costing (Chi phí)** | Chi phí hạ tầng cloud | Lượng token sử dụng cho mỗi tác vụ/bước |
| **Security (Bảo mật)** | Nhật ký truy cập (Access logs) | Kiểm toán prompt injection & rào chắn bảo vệ |

* **Các Nền Tảng Then Chốt:** LangSmith, Helicone, Langfuse, Arize Phoenix.

---

### Tổng Hợp: ConnectED Như Một Hệ Thống Tác Nhân (Agentic System)
ConnectED đi đến kiến trúc tác nhân thông qua phương pháp kỹ nghệ định hướng lĩnh vực (domain-driven engineering):

| Lớp (Layer) | Triển Khai Thực Tế Trong ConnectED |
|---|---|
| **Orchestration** | Bộ quản lý đường ống (pipeline manager) điều phối 6 giai đoạn. |
| **Reasoning Core** | Các lệnh gọi LLM tại mỗi bước chuyên biệt. |
| **Skills** | Nhúng các templates chương trình học và các quy tắc chấm điểm. |
| **Tools** | Trình phân tích sách giáo khoa, các kết nối cơ sở dữ liệu địa phương. |
| **Memory** | Ánh xạ trạng thái trung gian (khái niệm cốt lõi, bản thiết kế bài học). |
| **Loop** | Đường ống tuyến tính; vòng lặp tuần hoàn được kích hoạt bởi các chỉnh sửa của giáo viên. |
