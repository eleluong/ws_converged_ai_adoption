# Kịch Bản Thuyết Trình Workshop
## Phần II: Sự Trỗi Dậy Của Agentic AI Stack

> **Format:** Phần II | khoảng 40 phút tổng cộng  
> **Người nghe:** Nhà phát triển, Quản lý sản phẩm (PMs), Nhà nghiên cứu và Kỹ sư  

---

## CHUYỂN TIẾP (TRANSITION)

**Visual:** Thẻ Tiêu Đề: "Phần II: Tái Thiết Kế Kiến Trúc AI"

**Script:**
> "Mô hình quy trình công việc mà chúng ta xây dựng trong ConnectED không phải là trường hợp cá biệt. Trong phần này, chúng ta sẽ mở rộng góc nhìn để nghiên cứu về Agentic AI Stack đang hình thành."

---

## PHẦN II — Sự Trỗi Dậy Của Agentic AI Stack

### Slide 11: Generative AI vs. Agentic AI
**Visual:** Bảng So Sánh:

| Generative AI | Agentic AI |
|---|---|
| Prompt sang Phản hồi | Mục tiêu sang Vòng lặp (Lập kế hoạch -> Hành động -> Quan sát -> Phản tư) |
| Đơn lượt (Single-turn) | Đa lượt (Multi-turn), có tính lặp lại |
| Phản ứng (Reactive) | Tự chủ (Autonomous), mang tính khám phá |

**Ví dụ (Tác nhân du lịch - Travel Agent):**
1. **Lập kế hoạch (Plan):** Đặt chuyến bay & khách sạn.
2. **Hành động (Act):** Truy vấn APIs của hãng.
3. **Quan sát (Observe):** Nhận thấy giá vé máy bay vượt quá ngân sách.
4. **Phản tư (Reflect):** Đổi sân bay hoặc thay đổi ngày bay.
5. **Hoàn thành (Complete):** Đặt vé và gửi hành trình cho khách.

**Script:**
> "Chúng ta đang chuyển dịch từ thế giới tạo văn bản thụ động sang các hệ thống giải quyết vấn đề chủ động và tự chủ. LLM giờ đây đóng vai trò là một thành phần, chứ không phải toàn bộ hệ sinh thái (stack) nữa."

---

### Slide 12: Agentic Stack Hiện Đại (The Modern Agentic Stack)
**Visual:** Sơ đồ 5 lớp của kiến trúc tác nhân:
```
5. Memory Systems (Bộ nhớ Ngắn hạn & Dài hạn)
4. Tools and Protocols (MCP, AP2, ACP)
3. Skills (Tri thức nghiệp vụ được đóng gói dưới dạng Rules/Schemas)
2. Reasoning Core (Định tuyến mô hình - Model Routing)
1. Orchestration Layer (Trình quản lý vòng đời thực thi - Lifecycle Manager)
```

**Script:**
> "Dưới đây là năm lớp riêng biệt của kiến trúc tác nhân hiện đại. Chúng ta hãy cùng xem xét kỹ từng lớp một."

---

### Slide 13: Lớp 1 — Điều Phối (Orchestration)
**Visual:** Lưới Logo các Framework: LangChain | LangGraph | CrewAI | AutoGen

* Quản lý việc phân rã tác vụ, theo dõi trạng thái và logic xử lý lỗi.
* Phối hợp các tác nhân theo vai trò (ví dụ: kết nối tác nhân phân tích dữ liệu với tác nhân viết lách).
* *Lời khuyên sản xuất:* Các orchestration engines tự viết thường vượt trội hơn các generic frameworks về độ tin cậy và kiểm soát chi phí.

**Script:**
> "Lớp điều phối đóng vai trò như cơ quan điều hành. Nó xử lý việc lập kế hoạch, quản lý trạng thái hệ thống và kích hoạt các lệnh gọi lại khi APIs gặp lỗi."

---

### Slide 14: Lớp 2 — Nhân Tố Lập Luận (Reasoning Core)
**Visual:** Sơ đồ luồng định tuyến mô hình:
`Incoming Task -> [Router] -> Small Model (Phân loại) HOẶC Frontier Model (Lập luận phức tạp)`

* **Frontier Models:** Chi phí cao / Năng lực lớn.
* **Reasoning Models:** OpenAI o1/DeepSeek-R1 (cho lập luận logic sâu và lập kế hoạch).
* **Small Models:** Chi phí rẻ / Tốc độ nhanh.

**Script:**
> "Đừng gửi các tác vụ định tuyến đơn giản đến các mô hình lớn (frontier models). Sử dụng một lớp định tuyến (routing layer) để cắt giảm chi phí token lên tới 80%."

---

### Slide 15: Lớp 3 — Kỹ Năng (Skills - Tri Thức Đóng Gói)
**Visual:** Đồ họa mô tả gói tài nguyên bao gồm: `manifest.json`, `instructions.md`, `templates/`, `policies/`

| Kỹ năng (Skill) | Nội dung bên trong |
|---|---|
| **Soạn giáo án** | Các tiêu chuẩn chương trình học, templates giáo án |
| **Đánh giá mã nguồn** | Các quy tắc linter, kiểm tra bảo mật |
| **Báo cáo tài chính MD&A** | Logic API kế toán, định dạng báo cáo SEC |

**Script:**
> "Một Skill là gói tri thức nghiệp vụ có thể tái sử dụng và được quản lý phiên bản bằng git. Chúng ta chỉ tải skill phù hợp khi cần thiết, giúp cho prompts luôn gọn nhẹ."

---

### Slide 16: Lớp 4 — Công Cụ Và Giao Thức (Tools and Protocols)
**Visual:** Bảng so sánh các giao thức tiêu chuẩn:

| Giao thức | Đơn vị phát triển | Trọng tâm chính |
|---|---|---|
| **MCP** | Anthropic | USB-C cho AI: Chuẩn hóa việc khám phá công cụ & tài nguyên |
| **AP2** | Google | Ý định mã hóa (Intent) & Ủy quyền giỏ hàng (Cart Mandates) để giao dịch an toàn |
| **A2A / ACP** | Cộng đồng | Ủy quyền tác nhân và điều phối qua WebSocket |
| **OpenAI ACP** | OpenAI | Thương mại hội thoại không giao diện (headless, dialogue-driven) |

**Script:**
> "AP2 là một giao thức rất thú vị: nó giới thiệu các ủy quyền người dùng được ký mã hóa (cryptographic mandates) để giải quyết các vấn đề về niềm tin, xác thực và tuân thủ thanh toán cho các tác nhân tự chủ."

---

### Slide 17: Lớp 5 — Hệ Thống Bộ Nhớ (Memory Systems)
**Visual:** Hai cột so sánh Bộ nhớ Ngắn hạn và Dài hạn:
* **Ngắn hạn (Episodic):** Bộ đệm phiên làm việc tại địa phương (local session buffers) theo dõi các bước thực thi.
* **Dài hạn (Semantic):** Cơ sở dữ liệu vector (Chroma, Weaviate) lưu trữ lịch sử người dùng và các thiết lập ưu tiên.
* **Quy trình (Procedural/Skills):** Tra cứu từ các file skill được quản lý phiên bản.

**Script:**
> "Quản lý bộ nhớ vẫn là một nút thắt cổ chai lớn trong kỹ nghệ tác nhân. Cơ sở dữ liệu vector có thể giúp ích, nhưng việc quản lý cửa sổ ngữ cảnh để tránh bị lệch hướng (drift) là tối quan trọng."

---

### Slide 18: Vòng Lặp Tác Nhân Cốt Lõi (Core Agentic Loop)
**Visual:** Hoạt cảnh vòng lặp tuần hoàn:
`PLAN -> ACT -> OBSERVE -> REFLECT -> ITERATE`

**Ví dụ (Tác nhân nghiên cứu Vật lý Lượng tử):**
* **Lên kế hoạch & Hành động (Plan & Act):** Tìm kiếm trên arXiv với từ khóa "quantum correction".
* **Quan sát (Observe):** Nhận về hơn 50 bài báo (quá nhiều nhiễu).
* **Phản tư & Lặp lại (Reflect & Iterate):** Thay đổi kế hoạch để sắp xếp theo số lượt trích dẫn, tải về 3 bài báo hàng đầu.

**Script:**
> "Vòng lặp nhận thức là yếu tố giúp các tác nhân tự phục hồi sau lỗi, viết lại kế hoạch và hội tụ về các kết quả hoàn thành thành công."
