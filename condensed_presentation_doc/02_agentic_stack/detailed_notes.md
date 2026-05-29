# **Ghi Chú Chi Tiết: Emerging Agentic AI Stack**

> *Tài liệu này bổ sung ví dụ code và phân tích sâu cho `reference.md` — dùng khi cần minh họa kỹ thuật trong buổi workshop.*

---

### **2.1 — Khi Nào Nên Dùng Agentic AI?**
Agentic AI phát huy tối đa khi:
- Nhiệm vụ mang tính **khám phá** — bước tiếp theo phụ thuộc vào kết quả của bước trước.
- Thông tin đầu vào **không đầy đủ** khi bắt đầu — cần thu thập dần qua công cụ.
- Hành động **không thể dự đoán hoàn toàn** từ đầu — cần vòng phản hồi liên tục.

Ngược lại, với các tác vụ có đầu vào xác định và đầu ra cố định, pipeline truyền thống vẫn là lựa chọn tốt hơn về chi phí và độ ổn định.

---

### **2.2 — Lựa Chọn Framework Orchestration**
Bảng so sánh nhanh để chọn framework phù hợp với từng trường hợp:

| Framework | Điểm mạnh | Phù hợp nhất cho |
|---|---|---|
| **LangChain** | Tích hợp công cụ đa dạng | Pipeline dữ liệu chung |
| **LangGraph** | Kiểm soát trạng thái dạng đồ thị | Luồng công việc tuần hoàn phức tạp |
| **CrewAI** | Cộng tác tác nhân theo vai trò | Nhóm làm việc đa tác nhân |
| **AutoGen** | Mô hình tác nhân hội thoại | Nhiệm vụ khám phá |
| **Claude Code** | Tích hợp sâu terminal/công cụ dev | Kỹ nghệ phần mềm |
| **Tùy chỉnh (Custom)** | Kiểm soát trực tiếp trạng thái & ngân sách | Hệ thống production |

**Quyết định cho production:** Custom state machine đảm bảo tính xác định 100% — không có chi phí dư thừa hay hành vi không mong đợi từ abstraction layer của framework.

---

### **2.3 — Định Tuyến Mô Hình: Ví Dụ Code**
Đây là pattern định tuyến phân tầng (tiered routing) cơ bản:

```python
class TieredRouter:
    def route(self, task: str) -> str:
        if any(kw in task for kw in ["plan", "strategy", "reason", "analyze"]):
            return "claude-4.6-sonnet"       # Frontier: lập kế hoạch phức tạp
        elif any(kw in task for kw in ["extract", "parse", "summarize"]):
            return "gpt-4o-mini"             # Synthesis: tổng hợp trung gian
        else:
            return "llama-3.3-70b"           # Utility: định dạng, phân loại
```

Để nâng cao hơn, thay thế điều kiện từ khóa bằng **semantic routing** dùng embedding similarity — chính xác hơn và không cần duy trì danh sách từ khóa thủ công.

---

### **2.4 — Skills: Kiến Trúc Đóng Gói Tri Thức**
Mỗi Skill Module là một gói độc lập, bao gồm:
- **System prompt** — hướng dẫn hành vi của tác nhân cho tác vụ cụ thể.
- **JSON validation schema** — ràng buộc cấu trúc đầu ra.
- **Templates** — các mẫu nội dung chuẩn hóa.

Quản lý qua Git cho phép: version control, A/B testing giữa các phiên bản skill, rollback khi cần và phát triển song song giữa các nhóm.

---

### **2.5 — Giao Thức AP2: Thanh Toán Tự Động Có Kiểm Soát**
AP2 giải quyết bài toán: làm thế nào để tác nhân có thể thực hiện giao dịch tài chính mà vẫn đảm bảo an toàn và có sự kiểm soát của con người?

**Luồng hoạt động:**
1. Người dùng ký **Intent Mandate** — xác định ngân sách tối đa cho phép, phạm vi tài nguyên được mua.
2. Tác nhân duyệt và chọn tài nguyên phù hợp.
3. Tác nhân tạo **Cart Mandate** và gửi đến cổng checkout đối tác để hoàn tất vi thanh toán.
4. Mọi giao dịch đều ghi nhật ký đầy đủ để kiểm toán.

---

### **2.6 — Kiểm Soát Vòng Lặp Tác Nhân**
Ba rủi ro phổ biến và cách phòng tránh:

- **Cố định kế hoạch (Plan Lock-in):** Tác nhân bám vào kế hoạch ban đầu dù có tín hiệu thất bại từ môi trường. → Giải pháp: bắt buộc xem xét lại kế hoạch sau mỗi N bước hoặc sau khi công cụ trả về lỗi.

- **Lặp vô hạn (Infinite Loop):** Tác nhân không thể hội tụ, cứ thử lại mãi. → Giải pháp: giới hạn cứng số lần thử (max_retries) và tổng số bước (max_steps).

- **Kết thúc sớm (Premature Termination):** Tác nhân báo cáo hoàn thành khi thực tế chưa đủ tiêu chí. → Giải pháp: xác thực kết quả cuối theo checklist bất biến (invariant assertions) trước khi đánh dấu task hoàn thành.
