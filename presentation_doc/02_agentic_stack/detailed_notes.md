# Workshop — Tài Liệu Ghi Chú Chi Tiết
## Hệ Sinh Thái Tác Nhân AI Mới Nổi (The Emerging Agentic AI Stack)

> Các ghi chú này cung cấp thông tin chi tiết nâng cao, các bảng so sánh kiến trúc và các phân tích đánh đổi trong thiết kế.

---

### Phần 2.1: Từ Generative AI Đến Agentic AI
* **Vòng lặp nhận thức (Cognitive loops):** Thay vì các prompts đơn lượt (single-turn prompts), hệ thống tác nhân (agentic systems) chạy các vòng lặp LÊN KẾ HOẠCH (PLANNING), HÀNH ĐỘNG (ACTING), QUAN SÁT (OBSERVING) và PHẢN TƯ (REFLECTING).
* **Nhiệm vụ mang tính khám phá (Exploratory tasks):** Hệ thống tác nhân tối ưu nhất khi thông tin đầu vào chưa đầy đủ ngay từ đầu, hoặc khi hướng thực thi tiếp theo phụ thuộc vào kết quả của các công cụ trung gian (intermediate tool results).

---

### Phần 2.2: Lớp 1 — Điều Phối (Orchestration Layer)
Lớp điều phối đóng vai trò là cơ quan điều hành của hệ thống, quản lý và duy trì trạng thái cũng như xử lý các lỗi phát sinh.

| Framework | Điểm mạnh (Strengths) | Phù hợp nhất cho (Best For) |
|---|---|---|
| **LangChain** | Tích hợp công cụ đa dạng | Các đường ống dẫn dữ liệu chung (General pipelines) |
| **LangGraph** | Kiểm soát trạng thái dạng đồ thị | Các luồng công việc tuần hoàn phức tạp (Cyclic workflows) |
| **CrewAI** | Sự cộng tác tác nhân theo vai trò | Nhóm làm việc đa tác nhân (Multi-agent teams) |
| **AutoGen** | Mô hình tác nhân hội thoại | Các nhiệm vụ mang tính khám phá |
| **Claude Code** | Tích hợp sâu terminal/công cụ phát triển | Kỹ nghệ phần mềm (Software engineering) |
| **Tự viết (Custom)** | Kiểm soát trực tiếp trạng thái và ngân sách | Hệ thống chạy thực tế (Production systems) |

---

### Phần 2.3: Lớp 2 — Nhân Tố Lập Luận (Reasoning Core)
Hiệu năng, chi phí và độ trễ của tác nhân phụ thuộc rất nhiều vào các chiến lược định tuyến mô hình (model routing strategies).

| Nhóm Mô Hình | Điểm Mạnh Cốt Lõi | Trường Hợp Sử Dụng Tốt Nhất |
|---|---|---|
| **Frontier Large** (e.g., Claude 3.5) | Tổng hợp thông tin cấp cao | Lập kế hoạch phức tạp (Complex planning) |
| **Reasoning Core** (e.g., o1/R1) | Logic đa bước nâng cao | Tạo mã nguồn, lập kế hoạch sâu |
| **Small Models** (e.g., Llama 8B) | Thực thi nhanh, chi phí rẻ | Phân loại dữ liệu, định tuyến (Routing) |
| **Domain Fine-tuned** | Độ chính xác nghiệp vụ cao | Tìm kiếm / Trích xuất thông tin chuyên biệt |

---

### Phần 2.4: Lớp 3 — Kỹ Năng (Skills)
Kỹ năng đại diện cho các gói tài nguyên và hướng dẫn nghiệp vụ có tính module và phiên bản, thay vì các prompts nguyên khối lớn (monolithic prompts).

| Tiêu Chí | Monolithic Prompt | Cấu Trúc Dựa Trên Skills |
|---|---|---|
| **Cửa Sổ Ngữ Cảnh** | Luôn tải toàn bộ (phình to) | Tải động theo nhu cầu (hiệu quả) |
| **Quản Lý Phiên Bản** | Thủ công, dễ lỗi | Sử dụng Git để quản lý, dễ kiểm toán |
| **Khả Năng Tái Sử Dụng** | Sao chép-dán mã nguồn | Một nguồn sự thật duy nhất (Single source of truth) |
| **Kiểm Thử** | Khó cô lập lỗi | Có thể kiểm thử độc lập từng module |

---

### Phần 2.5: Lớp 4 — Các Giao Thức Tương Thích (Interoperability Protocols)
Chuẩn hóa giao diện giao tiếp giữa các tác nhân (agents), môi trường bên ngoài và các mạng lưới giao dịch.
* **MCP (Model Context Protocol):** Khai báo các giao diện Client-Server chuẩn hóa cho Công cụ (Tools), Tài nguyên (Resources) và Prompts.
* **AP2 (Agent Payments Protocol):** Khởi tạo và ký mã hóa các ủy quyền thanh toán tự động.
  * **Intent Mandate (Ủy quyền Ý định):** Giới hạn kiểm soát do người dùng xác định (ví dụ: "chỉ mua vé tối đa $200").
  * **Cart Mandate (Ủy quyền Giỏ hàng):** Cơ chế khóa và kiểm tra giỏ hàng cuối cùng để ngăn chặn sự gian lận của người bán.
* **OpenAI ACP & Google UCP:** Được thiết kế tối ưu cho cấu trúc thanh toán hội thoại (ACP) và điều phối toàn bộ chu trình xử lý đơn hàng/hoàn trả (UCP).

---

### Phần 2.6: Lớp 5 — Hệ Thống Bộ Nhớ (Memory Systems)
Hệ thống bộ nhớ giúp vượt qua các giới hạn về cửa sổ ngữ cảnh cố định của các mô hình ngôn ngữ.

| Loại Bộ Nhớ | Vị Trí Lưu Trữ | Phương Pháp Truy Hồi | Thời Gian Tồn Tại |
|---|---|---|---|
| **In-context** | Cửa sổ ngữ cảnh | Cơ chế tự chú ý (Attention) | Một lượt thực thi |
| **Episodic** | Bộ đệm bộ nhớ trong | Truy xuất tuần tự | Phiên làm việc (Active session) |
| **Semantic** | Cơ sở dữ liệu Vector | Tìm kiếm tương đồng vector | Lâu dài (Persistent) |
| **Procedural** | Kho lưu trữ Skill | Tra cứu siêu dữ liệu (Metadata) | Lâu dài (Persistent) |
| **Structured** | Cơ sở dữ liệu SQL/KV | Truy vấn theo khóa | Lâu dài (Persistent) |

---

### Phần 2.7: Vòng Lặp Tác Nhân Cốt Lõi (Core Agentic Loop)
```
[PLAN] -> [ACT] -> [OBSERVE] -> [REFLECT] -> [ITERATE]
```
* **Các chế độ lỗi (Failure Modes):** Bị cố định kế hoạch (bỏ qua lỗi phát sinh), vòng lặp vô hạn (không thể hội tụ để hoàn thành) và kết thúc sớm (báo cáo hoàn thành sai thực tế).
* **Giảm thiểu lỗi (Mitigation):** Áp dụng giới hạn chi phí (cost caps), bộ đếm số lượt lặp tối đa (max iterations) và các điểm kích hoạt Human-in-the-loop để chuyển giao cho con người.
