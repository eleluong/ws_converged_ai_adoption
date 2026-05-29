# **Sự Trỗi Dậy Của Agentic AI Stack**

## **Từ Generative AI Đến Agentic AI**
GenAI truyền thống hoạt động theo mô hình **đơn lượt (single-turn)**: nhận yêu cầu, tạo phản hồi, kết thúc. Nó thiếu khả năng tự lên kế hoạch, sử dụng công cụ hay tự sửa lỗi dựa trên phản hồi từ môi trường.

**Agentic AI** thay đổi mô hình này hoàn toàn. Thay vì phản hồi tĩnh, tác nhân vận hành qua **vòng lặp nhận thức liên tục**:

```
Mục tiêu → Lập kế hoạch → Hành động → Quan sát → Phản tư → Lặp lại → Hoàn thành
```

Trong kiến trúc này, LLM không còn là điểm cuối — nó là **nhân tố lập luận (reasoning engine)** bên trong một hệ sinh thái tính toán lớn hơn, phù hợp nhất cho các nhiệm vụ khám phá, khi thông tin đầu vào chưa đầy đủ hoặc bước tiếp theo phụ thuộc vào kết quả công cụ trung gian.

---

## **Agentic Stack Hiện Đại (5 Lớp)**
```
+------------------------------------------------------------------+
|  5. Memory Systems  (Bộ nhớ ngắn hạn & dài hạn)                 |
+------------------------------------------------------------------+
|  4. Tools & Protocols  (Giao tiếp công cụ & giao dịch)           |
+------------------------------------------------------------------+
|  3. Skills  (Kỹ năng đóng gói chuyên biệt)                      |
+------------------------------------------------------------------+
|  2. Reasoning Core  (Định tuyến mô hình: Frontier & Small)       |
+------------------------------------------------------------------+
|  1. Orchestration Layer  (Máy trạng thái hữu hạn tùy chỉnh)     |
+------------------------------------------------------------------+
```

---

### **1. Lớp Điều Phối (Orchestration Layer)**
Quản lý toàn bộ chu kỳ thực thi: phân rã nhiệm vụ, quản lý trạng thái, xử lý lỗi và điều phối luồng dữ liệu giữa các tác nhân.

**Các framework phổ biến và trường hợp sử dụng phù hợp:**

| Framework | Điểm mạnh | Phù hợp nhất cho |
|---|---|---|
| **LangChain** | Tích hợp công cụ đa dạng | Pipeline dữ liệu chung |
| **LangGraph** | Kiểm soát trạng thái dạng đồ thị | Luồng công việc tuần hoàn phức tạp |
| **CrewAI** | Cộng tác tác nhân theo vai trò | Nhóm làm việc đa tác nhân |
| **AutoGen** | Mô hình tác nhân hội thoại | Nhiệm vụ khám phá |
| **Claude Code** | Tích hợp sâu terminal/công cụ dev | Kỹ nghệ phần mềm |
| **Tùy chỉnh (Custom)** | Kiểm soát trực tiếp trạng thái & ngân sách | Hệ thống production |

**Khuyến nghị cho production:** Ưu tiên **máy trạng thái hữu hạn tùy chỉnh (custom state machine)** để kiểm soát chặt chẽ luồng chuyển đổi trạng thái, đảm bảo định dạng JSON 100% cho dữ liệu trung gian và tránh chi phí dư thừa từ các framework mở.

---

### **2. Nhân Tố Lập Luận (Reasoning Core)**
Động cơ trí tuệ ở trung tâm của stack. Không phải một mô hình duy nhất mà là một **hệ sinh thái mô hình được định tuyến thông minh**.

**Phân loại mô hình:**

| Nhóm | Điểm mạnh | Trường hợp sử dụng tốt nhất |
|---|---|---|
| **Frontier Large** (Claude 4.6 Sonnet) | Tổng hợp thông tin cấp cao, lập kế hoạch sâu | Lập kế hoạch phức tạp, tác vụ sáng tạo |
| **Reasoning Core** (o1/o3, DeepSeek-R1) | Logic đa bước nâng cao | Tạo mã, lập kế hoạch siêu sâu |
| **Small/Utility** (Gemini 2.5 Flash, Llama 3.3 70B) | Thực thi nhanh, chi phí rẻ | Phân loại, định dạng, định tuyến |
| **Domain Fine-tuned** (Qwen 3 8B) | Độ chính xác nghiệp vụ cao | Trích xuất thông tin chuyên biệt |

**Định tuyến ngữ nghĩa (Semantic Routing):** Tự động phân loại intent của yêu cầu để định tuyến đúng mô hình — tác vụ lập luận phức tạp đến Frontier/Reasoning Models, tác vụ phụ trợ/định dạng đến Small/Utility Models. Kết quả: **tiết kiệm đến 70% chi phí và giảm 45% độ trễ**.

---

### **3. Kỹ Năng (Skills — Tri Thức Đóng Gói)**
Skills đại diện cho tri thức nghiệp vụ được module hóa và quản lý phiên bản — khác hoàn toàn với cách tiếp cận prompt nguyên khối (monolithic).

**So sánh hai kiến trúc:**

| Tiêu chí | Monolithic Prompt | Kiến trúc Skill-Based |
|---|---|---|
| **Cửa sổ ngữ cảnh** | Luôn tải toàn bộ (phình to) | Tải động theo nhu cầu (hiệu quả) |
| **Quản lý phiên bản** | Thủ công, dễ lỗi | Git-managed, dễ kiểm toán |
| **Tái sử dụng** | Sao chép-dán | Single source of truth |
| **Kiểm thử** | Khó cô lập lỗi | Kiểm thử độc lập từng module |

Mỗi Skill Module đóng gói: prompts hệ thống + validation schemas + templates — đảm bảo cô lập trạng thái và cho phép phát triển song song hiệu quả.

---

### **4. Công Cụ & Giao Thức (Tools & Protocols)**
Chuẩn hóa giao diện giao tiếp giữa tác nhân, môi trường bên ngoài và các mạng giao dịch.

- **Model Context Protocol (MCP):** Cầu nối chuẩn hóa kết nối tác nhân với databases và filesystems doanh nghiệp.
- **Agent Payments Protocol (AP2):** Ủy quyền giao dịch tài chính tự động an toàn:
  - **Intent Mandate:** Người dùng ký mã hóa giới hạn ngân sách tối đa cho tác nhân.
  - **Cart Mandate:** Tác nhân chọn tài nguyên và thực hiện vi thanh toán an toàn tại cổng checkout đối tác.
- **ACP & UCP:** Quản lý vòng đời đơn hàng và quyền sở hữu tài nguyên số theo thời gian thực.

---

### **5. Hệ Thống Bộ Nhớ (Memory Systems)**
Duy trì ngữ cảnh và trạng thái làm việc vượt ra ngoài giới hạn cửa sổ ngữ cảnh của mô hình.

| Loại | Vị trí lưu trữ | Phương pháp truy hồi | Thời gian tồn tại |
|---|---|---|---|
| **In-context** | Cửa sổ ngữ cảnh | Cơ chế tự chú ý (Attention) | Một lượt thực thi |
| **Episodic** | Bộ đệm bộ nhớ trong | Truy xuất tuần tự | Phiên làm việc |
| **Semantic** | Vector Database | Tìm kiếm tương đồng vector | Lâu dài (Persistent) |
| **Procedural** | Kho lưu trữ Skill | Tra cứu siêu dữ liệu | Lâu dài (Persistent) |
| **Structured** | SQL/KV Store | Truy vấn theo khóa | Lâu dài (Persistent) |

---

## **Vòng Lặp Tác Nhân Cốt Lõi (Core Agentic Loop)**
Mọi hệ thống tác nhân đều chạy một vòng lặp nhận thức có tính cải tiến:

```
[PLAN] → [ACT] → [OBSERVE] → [REFLECT] → [ITERATE]
```

**Các lỗi phổ biến cần phòng tránh:**
- **Cố định kế hoạch:** Bỏ qua phản hồi từ môi trường, không điều chỉnh kế hoạch khi có thông tin mới.
- **Lặp vô hạn:** Không thể hội tụ về kết quả hoàn thành.
- **Kết thúc sớm:** Báo cáo hoàn thành trong khi thực tế chưa xong.

**Cơ chế kiểm soát:** Giới hạn cứng thời gian (timeouts), hạn mức ngân sách (cost caps) và chốt chặn chuyển giao cho con người (HITL triggers) là bắt buộc trong mọi hệ thống production.
