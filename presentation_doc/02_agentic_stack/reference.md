# Sự Trỗi Dậy Của Agentic AI Stack (Hệ Sinh Thái Tác Nhân AI)

## Từ Generative AI Đến Agentic AI

GenAI truyền thống hoạt động theo dạng phản hồi: **Prompt của người dùng → Phản hồi từ mô hình** (Single-turn - Hội thoại đơn lượt).
* *Hạn chế:* Không có khả năng tự lên kế hoạch (planning), sử dụng công cụ (tool usage) hoặc tự sửa sai (self-correction).

**Agentic AI** giới thiệu một mô hình tương tác hoàn toàn mới. Thay vì chỉ tạo ra văn bản một lượt, hệ thống vận hành theo các vòng lặp nhận thức lập luận - thực thi (reasoning-execution loops):  
**Mục tiêu (Goal) → Lập kế hoạch (Plan) → Hành động (Act) → Quan sát (Observe) → Phản tư (Reflect) → Lặp lại → Hoàn thành**.

Trong khung kiến trúc này, mô hình ngôn ngữ lớn đóng vai trò là nhân tố lập luận (reasoning engine) bên trong một hệ sinh thái tính toán lớn hơn. Tác nhân có thể:
* Lập kế hoạch thực hiện nhiệm vụ phức tạp,
* Gọi các công cụ và APIs bên ngoài,
* Thu nhận và phản tư dựa trên dữ liệu quan sát,
* Tự động điều chỉnh chiến lược và
* Phối hợp với các tác nhân khác để hoàn thành mục tiêu.

---

## Agentic Stack Hiện Đại

Các tác nhân AI hiện đại không phải là các mô hình đơn lẻ mà là các hệ thống điều phối đa lớp. Dưới đây là cấu trúc 5 lớp của Agentic Stack.

```
+-------------------------------------------------------------+
|  5. Memory Systems (Bộ nhớ ngắn hạn/dài hạn)                 |
+-------------------------------------------------------------+
|  4. Tools & Protocols (Giao tiếp công cụ & giao dịch)        |
+-------------------------------------------------------------+
|  3. Skills (Kỹ năng đóng gói chuyên biệt)                   |
+-------------------------------------------------------------+
|  2. Reasoning Core (Định tuyến mô hình: Frontier & Small)   |
+-------------------------------------------------------------+
|  1. Orchestration Layer (Harness/State Machine tùy chỉnh)   |
+-------------------------------------------------------------+
```

### 1. Lớp Điều Phối (Orchestration Layer)
Quản lý toàn bộ chu kỳ thực thi, phân rã nhiệm vụ, quản lý trạng thái và xử lý lỗi.

* **Kiến trúc chung:** Sử dụng các frameworks như LangChain, AutoGen hoặc CrewAI để phối hợp các tác nhân, hoặc phát triển máy trạng thái hữu hạn tùy chỉnh (custom state machine) để kiểm soát luồng chuyển giao dữ liệu với độ tin cậy tuyệt đối.

### 2. Nhân Tố Lập Luận (Reasoning Core)
Động cơ trí tuệ nằm ở trung tâm của stack.

* **Kiến trúc chung:** Sử dụng các chiến lược định tuyến mô hình (Model Routing) kết hợp định tuyến ngữ nghĩa (Semantic Routing) để phân phối nhiệm vụ đến các mô hình lớn (Frontier Models như **Claude 4.6 Sonnet**, OpenAI o1/o3, DeepSeek-R1) cho các tác vụ phức tạp cần tư duy sâu, hoặc mô hình nhỏ/tiện ích (Utility Models như **Llama 3.3 70B**, **Gemini 2.5 Flash**) cho các tác vụ đơn giản (phân loại, định dạng, dịch thuật) nhằm tối ưu hóa chi phí lên tới 70% và giảm độ trễ 45%.

### 3. Kỹ Năng (Skills - Tri Thức Đóng Gói)
Một Skill là một gói tri thức nghiệp vụ chuyên biệt, có tính module và được quản lý phiên bản (versioned).

* **Kiến trúc chung:** Tác nhân tải động các kỹ năng chuyên biệt khi cần (ví dụ: rà soát code, kiểm toán tài chính). Mỗi kỹ năng được đóng gói độc lập với prompts hệ thống chuyên biệt, các schemas dữ liệu cấu trúc định sẵn để dễ dàng kiểm thử, bảo trì và cập nhật phiên bản độc lập.

### 4. Công Cụ & Giao Thức (Tools & Protocols)
Chuẩn hóa giao diện giao tiếp giữa tác nhân, dữ liệu và thế giới bên ngoài.

* **Model Context Protocol (MCP):** Sử dụng MCP để kết nối các tác nhân với cơ sở dữ liệu và nguồn tài nguyên ngoài qua các MCP servers chuẩn hóa, loại bỏ các kết nối cơ sở dữ liệu tùy biến viết trực tiếp trong prompts.
* **Agent Payments Protocol (AP2):** Giao thức cho phép các tác nhân tự động thanh toán tài nguyên hoặc dịch vụ có phí một cách an toàn thông qua cơ chế ủy quyền mật mã (Intent Mandate) và khóa giỏ hàng (Cart Mandate).
* **ACP (Agent Communication Protocol) & UCP (Universal Commerce Protocol):** Được sử dụng để điều phối trạng thái đơn hàng và chuyển giao giấy phép sử dụng tài nguyên số trong thời gian thực.

### 5. Hệ Thống Bộ Nhớ (Memory Systems)
Duy trì ngữ cảnh và trạng thái làm việc vượt ra ngoài giới hạn cửa sổ ngữ cảnh (context window) của mô hình.

* **Bộ nhớ ngắn hạn (Episodic Memory):** Lưu giữ trạng thái của phiên làm việc hiện tại, giúp khôi phục nhanh nếu xảy ra sự cố hoặc cần người dùng nhập liệu giữa chừng.
* **Bộ nhớ dài hạn (Semantic Memory):** Sử dụng cơ sở dữ liệu vector hoặc KV để lưu trữ lịch sử, hồ sơ người dùng để cá nhân hóa kết quả đầu ra trong các phiên làm việc tiếp theo.

---

## Vòng Lặp Tác Nhân Cốt Lõi (Core Agentic Loop)

Hầu hết các hệ thống tác nhân chạy một vòng lặp nhận thức có tính cải tiến:

```
[PLAN] -> [ACT] -> [OBSERVE] -> [REFLECT] -> [ITERATE]
```

* **Ví dụ:** Một tác nhân nghiên cứu tìm kiếm các bài báo (PLAN/ACT), nhận về quá nhiều kết quả (OBSERVE), quyết định lọc theo số lượt trích dẫn trước (REFLECT), và chạy một tìm kiếm tinh chỉnh mới (ITERATE/COMPLETE).
* **Kiểm soát (Control):** Hệ thống yêu cầu cấu hình giới hạn thời gian (hard timeouts), hạn mức chi phí (cost caps) và các điểm kích hoạt chuyển giao cho con người (human escalation triggers) để tránh vòng lặp vô hạn.
