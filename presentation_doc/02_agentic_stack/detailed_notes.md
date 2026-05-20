# Workshop — Tài Liệu Ghi Chú Chi Tiết
## Hệ Sinh Thái Tác Nhân AI Mới Nổi (The Emerging Agentic AI Stack)

> Các ghi chú này cung cấp thông tin chi tiết nâng cao, các bảng so sánh kiến trúc và các phân tích đánh đổi trong thiết kế.

---

### Phần 2.1: Từ Generative AI Đến Agentic AI

* **Vòng lặp nhận thức (Cognitive loops):** Thay vì các prompts đơn lượt (single-turn prompts), hệ thống tác nhân (agentic systems) chạy các vòng lặp LÊN KẾ HOẠCH (PLANNING), HÀNH ĐỘNG (ACTING), QUAN SÁT (OBSERVING) và PHẢN TƯ (REFLECTING).
* **Nhiệm vụ mang tính khám phá (Exploratory tasks):** Hệ thống tác nhân tối ưu nhất khi thông tin đầu vào chưa đầy đủ ngay từ đầu, hoặc khi hướng thực thi tiếp theo phụ thuộc vào kết quả của các công cụ trung gian (intermediate tool results).
* **Ví dụ thực tế:** Một tác nhân lập kế hoạch chi tiết, trích xuất kiến thức từ nguồn tài nguyên ngoài, đối chiếu mục tiêu và tự động phản tư sửa đổi các tham số không phù hợp trước khi hiển thị cho người dùng.

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
| **Tùy chỉnh (Custom)** | Kiểm soát trực tiếp trạng thái và ngân sách | Hệ thống chạy thực tế (Production systems) |

**Kiến trúc Điều phối tùy chỉnh (Custom Orchestration Architecture):**
Để đảm bảo tính nhất quán tuyệt đối và tránh các bước chuyển đổi trạng thái phi tuyến tính không mong muốn, các hệ thống chạy thực tế (production systems) thường sử dụng **máy trạng thái hữu hạn tùy chỉnh (custom state machine)** thay vì các framework nguồn mở như LangChain hay CrewAI. Điều này đảm bảo dữ liệu đầu ra JSON được xác thực cấu trúc nghiêm ngặt trước khi chuyển sang giai đoạn tiếp theo trong luồng công việc.

---

### Phần 2.3: Lớp 2 — Nhân Tố Lập Luận (Reasoning Core)

Hiệu năng, chi phí và độ trễ của tác nhân phụ thuộc rất nhiều vào các chiến lược định tuyến mô hình (model routing strategies).

| Nhóm Mô Hình | Điểm Mạnh Cốt Lõi | Trường Hợp Sử Dụng Tốt Nhất |
|---|---|---|
| **Frontier Large** (e.g., Claude 4.6 Sonnet) | Tổng hợp thông tin cấp cao, lập kế hoạch sâu | Lập kế hoạch phức tạp (Complex planning) |
| **Reasoning Core** (e.g., o1/o3, R1) | Logic đa bước nâng cao | Tạo mã nguồn, lập kế hoạch siêu sâu |
| **Small/Utility Models** (e.g., Gemini 2.5 Flash, Llama 3.3 70B) | Thực thi nhanh, chi phí rẻ | Phân loại dữ liệu, định dạng, định tuyến (Routing) |
| **Domain Fine-tuned** | Độ chính xác nghiệp vụ cao | Tìm kiếm / Trích xuất thông tin chuyên biệt |

**Định Tuyến Mô Hình Thực Tế & Định Tuyến Ngữ Nghĩa (Semantic Routing):**
Hệ thống thực tế sử dụng định tuyến ngữ nghĩa (Semantic Routing) để phân tích mục đích yêu cầu của người dùng trước. Nhiệm vụ phức tạp cần tư duy sâu được định tuyến tới các mô hình lớn (Frontier/Reasoning Core như **Claude 4.6 Sonnet** / **DeepSeek-R1**), trong khi giao việc định dạng cấu trúc, dịch thuật và phân loại siêu dữ liệu (metadata) cho các mô hình nhỏ/tiện ích (Utility Models như **Llama 3.3 70B** / **Gemini 2.5 Flash**) nhằm tối ưu hóa chi phí vận hành token lên tới 70% và giảm độ trễ 45%.

---

### Phần 2.4: Lớp 3 — Kỹ Năng (Skills)

Kỹ năng đại diện cho các gói tài nguyên và hướng dẫn nghiệp vụ có tính module và phiên bản, thay vì các prompts nguyên khối lớn (monolithic prompts).

| Tiêu Chí | Monolithic Prompt | Cấu Trúc Dựa Trên Skills |
|---|---|---|
| **Cửa Sổ Ngữ Cảnh** | Luôn tải toàn bộ (phình to) | Tải động theo nhu cầu (hiệu quả) |
| **Quản Lý Phiên Bản** | Thủ công, dễ lỗi | Sử dụng Git để quản lý, dễ kiểm toán |
| **Khả Năng Tái Sử Dụng** | Sao chép-dán mã nguồn | Một nguồn sự thật duy nhất (Single source of truth) |
| **Kiểm Thử** | Khó cô lập lỗi | Có thể kiểm thử độc lập từng module |

**Kiến Trúc Dựa Trên Skills:**
Mỗi bước trong quy trình xử lý phức tạp được đóng gói thành một kỹ năng độc lập (Skill Module). Mỗi gói chứa prompts hệ thống chuyên biệt, các schemas dữ liệu đầu ra định sẵn để dễ dàng kiểm thử, bảo trì và cập nhật phiên bản một cách cô lập.

---

### Phần 2.5: Lớp 4 — Các Giao Thức Tương Thích (Interoperability Protocols)

Chuẩn hóa giao diện giao tiếp giữa các tác nhân (agents), môi trường bên ngoài và các mạng lưới giao dịch.
* **Model Context Protocol (MCP):** Sử dụng MCP để tạo cầu nối chuẩn hóa giữa tác nhân và cơ sở dữ liệu doanh nghiệp hoặc kho tài nguyên ngoài.
* **AP2 (Agent Payments Protocol):** Cho phép tác nhân tự động thực hiện giao dịch tài chính an toàn:
  * **Intent Mandate:** Người dùng ủy quyền trước giới hạn ngân sách (ví dụ: tối đa $2.00).
  * **Cart Mandate:** Tác nhân xác nhận giỏ hàng và thực hiện thanh toán tự động qua cổng thanh toán của đối tác.
* **Google UCP:** Hỗ trợ điều phối toàn bộ chu trình xử lý đơn hàng, cấp quyền sử dụng sản phẩm số và quản lý tài nguyên tự động.

---

### Section 2.6: Lớp 5 — Hệ Thống Bộ Nhớ (Memory Systems)

Hệ thống bộ nhớ giúp vượt qua các giới hạn về cửa sổ ngữ cảnh cố định của các mô hình ngôn ngữ.

| Loại Bộ Nhớ | Vị Trí Lưu Trữ | Phương Pháp Truy Hồi | Thời Gian Tồn Tại |
|---|---|---|---|
| **In-context** | Cửa sổ ngữ cảnh | Cơ chế tự chú ý (Attention) | Một lượt thực thi |
| **Episodic** | Bộ đệm bộ nhớ trong | Truy xuất tuần tự | Phiên làm việc (Active session) |
| **Semantic** | Cơ sở dữ liệu Vector | Tìm kiếm tương đồng vector | Lâu dài (Persistent) |
| **Procedural** | Kho lưu trữ Skill | Tra cứu siêu dữ liệu (Metadata) | Lâu dài (Persistent) |
| **Structured** | Cơ sở dữ liệu SQL/KV | Truy vấn theo khóa | Lâu dài (Persistent) |

**Kiến Trúc Bộ Nhớ Thực Tế:**
Hệ thống kết hợp **Episodic Memory** (để giữ trạng thái phiên làm việc hiện tại của người dùng, cho phép khôi phục nhanh nếu xảy ra lỗi) và **Semantic Memory** thông qua Vector DB (lưu giữ thông tin lịch sử, sở thích người dùng để cá nhân hóa kết quả đầu ra trong tương lai).

---

### Phần 2.7: Vòng Lặp Tác Nhân Cốt Lõi (Core Agentic Loop)

```
[PLAN] -> [ACT] -> [OBSERVE] -> [REFLECT] -> [ITERATE]
```

* **Các chế độ lỗi (Failure Modes):** Bị cố định kế hoạch (bỏ qua lỗi phát sinh), vòng lặp vô hạn (không thể hội tụ để hoàn thành) và kết thúc sớm (báo cáo hoàn thành sai thực tế).
* **Kiểm soát Vòng lặp Nhận Thức:** Tại mỗi bước trong quy trình, tác nhân chạy vòng lặp PLAN-ACT-OBSERVE-REFLECT. Cổng kiểm tra validation (OBSERVE) sẽ phát hiện lỗi hoặc sự không khớp. Nếu phát hiện vấn đề, nó tự phản tư (REFLECT) và sửa đổi (ITERATE). Hệ thống áp dụng giới hạn số lần lặp lại (ví dụ: tối đa 3 lần) trước khi chuyển giao cho con người (Human-in-the-loop) để tránh vòng lặp vô hạn.
