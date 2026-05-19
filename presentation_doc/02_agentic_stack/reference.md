# Sự Trỗi Dậy Của Agentic AI Stack (Hệ Sinh Thái Tác Nhân AI)

## Từ Generative AI Đến Agentic AI
GenAI truyền thống hoạt động theo dạng phản hồi: **Prompt của người dùng → Phản hồi từ mô hình** (Single-turn - Hội thoại đơn lượt).
* **Hạn chế:** Không có khả năng tự lên kế hoạch (planning), sử dụng công cụ (tool usage) hoặc tự sửa sai (self-correction).

Agentic AI hoạt động trong các vòng lặp lập luận - thực thi (reasoning-execution loops): **Mục tiêu → Lên kế hoạch → Hành động → Quan sát → Phản tư (Reflect) → Lặp lại → Hoàn thành**.
* **Khả năng:** Ủy quyền tác vụ, sử dụng cơ sở dữ liệu/APIs, sửa lỗi và điều phối hoạt động với các tác nhân (agents) khác.

Lúc này, LLM trở thành nhân tố lập luận (reasoning engine) bên trong một hệ thống lớn hơn.

---

## Agentic Stack Hiện Đại (The Modern Agentic Stack)
Các tác nhân (agents) hiện đại là hệ thống điều phối đa lớp:

```
+-----------------------------------+
|  5. Memory Systems (Short/Long)   |
+-----------------------------------+
|  4. Tools & Protocols (MCP, AP2)  |
+-----------------------------------+
|  3. Skills (Packaged Expertise)   |
+-----------------------------------+
|  2. Reasoning Core (LLMs)         |
+-----------------------------------+
|  1. Orchestration Layer (Harness) |
+-----------------------------------+
```

---

## Lớp 1: Điều Phối (Orchestration Layer)
Lớp điều phối quản lý toàn bộ chu kỳ thực thi:
* **Các nhiệm vụ:** Lập kế hoạch, quản lý trạng thái (state management), thực thi chính sách, gọi lại khi lỗi (error retries).
* **Các frameworks phổ biến:** LangChain, Claude Code, AutoGen, CrewAI.
* **Ví dụ:** Trong CrewAI, một tác nhân quản lý (manager agent) điều phối một tác nhân nghiên cứu (research agent) và một tác nhân viết lách (writer agent), quản lý việc chuyển giao dữ liệu và xử lý lỗi.

*Lời khuyên sản xuất:* Các công cụ điều phối tự viết (custom orchestration engines) thường có hiệu năng và chi phí tốt hơn các generic frameworks chung chung.

---

## Lớp 2: Nhân Tố Lập Luận (Reasoning Core)
Động cơ nằm ở trung tâm của stack:
* **Các Frontier Models:** GPT-4o, Claude 3.5 Sonnet (cho lập luận rộng/tổng quát).
* **Các Reasoning Models:** o1, DeepSeek-R1 (cho lập luận logic sâu, lên kế hoạch phức tạp).
* **Các Small Models:** Llama 3 (8B) (cho phân loại nhanh, rẻ).

*Mô hình định tuyến (Routing Pattern):* Chuyển các tác vụ phân loại đơn giản đến các mô hình nhỏ (small models), và các lập luận phức tạp đến các frontier models để giảm chi phí từ **60-80%**.

---

## Lớp 3: Kỹ Năng (Skills - Tri Thức Đóng Gói)
Một **Skill** là một gói tri thức nghiệp vụ chuyên biệt được chia theo phiên bản (versioned) và có tính module:
* **Thành phần:** System prompts, output schemas (lược đồ đầu ra), templates, bảng tra cứu (lookup tables) và các quy tắc.
* **Ví dụ:** Thiết kế bài giảng giáo dục, báo cáo tài chính MD&A, kiểm tra bảo mật mã nguồn.
* **Lợi ích:** Tải ngữ cảnh tăng dần (chỉ tải các skills cần thiết khi dùng), kiểm thử độc lập dễ dàng và cập nhật một nơi cho toàn hệ thống.

---

## Lớp 4: Công Cụ & Giao Thức (Tools & Protocols)
Các giao diện truyền thông chuẩn hóa giữa các tác nhân (agents), công cụ (tools) và các nền tảng:
* **MCP (Model Context Protocol):** Được xem như "USB-C cho AI." Kết nối các tác nhân với công cụ (hàm), tài nguyên (dữ liệu) và templates.
* **A2A / ACP (Agent-to-Agent / Agent Coordination Protocol):** Các giao thức ủy quyền và điều phối thời gian thực giữa các tác nhân.
* **AP2 (Agent Payments Protocol):** Các ủy quyền thanh toán an toàn (cryptographic Intent và Cart Mandates) cho phép tác nhân giao dịch tự động. Được hỗ trợ bởi Google, Coinbase và hơn 60 tổ chức tài chính hàng đầu.
* **OpenAI ACP & Google UCP:** Tối ưu hóa cho các cấu trúc thanh toán hội thoại (ACP) và điều phối toàn bộ chu trình xử lý đơn hàng/hoàn trả (UCP).

---

## Lớp 5: Hệ Thống Bộ Nhớ (Memory Systems)
Cho phép tác nhân duy trì ngữ cảnh vượt ra ngoài cửa sổ ngữ cảnh (context window) cố định của mô hình ngôn ngữ:
* **Ngắn hạn (Short-Term/Episodic):** Bộ đệm trong bộ nhớ (in-memory buffer) theo dõi các bước trong phiên làm việc hiện tại.
* **Dài hạn (Long-Term/Semantic):** Truy hồi độ tương đồng qua cơ sở dữ liệu vector (như SQLite, Chroma, Weaviate) cho các sở thích của người dùng và lịch sử dự án.
* **Nghiệp vụ (Procedural/Skills):** Tải động các hướng dẫn chuyên biệt cho từng lĩnh vực.

---

## Vòng Lặp Tác Nhân Cốt Lõi (Core Agentic Loop)
Hầu hết các hệ thống tác nhân chạy một vòng lặp nhận thức có tính cải tiến:

```
[PLAN] -> [ACT] -> [OBSERVE] -> [REFLECT] -> [ITERATE]
```

* **Ví dụ:** Một tác nhân nghiên cứu tìm kiếm các bài báo (PLAN/ACT), nhận về quá nhiều kết quả (OBSERVE), quyết định lọc theo số lượt trích dẫn trước (REFLECT), và chạy một tìm kiếm tinh chỉnh mới (ITERATE/COMPLETE).
* **Kiểm soát (Control):** Hệ thống yêu cầu cấu hình giới hạn thời gian (hard timeouts), hạn mức chi phí (cost caps) và các điểm kích hoạt chuyển giao cho con người (human escalation triggers) để tránh vòng lặp vô hạn.
