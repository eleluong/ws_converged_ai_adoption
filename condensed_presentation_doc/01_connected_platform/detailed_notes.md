# **Ghi Chú Chi Tiết: ConnectED Platform**

> *Tài liệu này bổ sung chi tiết kỹ thuật cho `reference.md` — dùng khi cần đi sâu vào từng phần trong buổi workshop.*

---

### **1.1 — Khác Biệt Cốt Lõi & Bối Cảnh**
ConnectED không chỉ là công cụ tạo nội dung — nó thiết kế việc soạn giáo án như một **quy trình sư phạm có hệ thống**. Điều này tạo ra sự khác biệt căn bản so với các LLM thương mại áp dụng tiêu chuẩn phương Tây, không đồng bộ với thuật ngữ MOET và thiếu bản địa hóa cho bối cảnh Việt Nam.

**Mẫu thiết kế có thể tái sử dụng:** Kiến trúc của ConnectED — bản địa hóa sâu kết hợp với quy trình sư phạm có hệ thống — là mẫu thiết kế có giá trị để áp dụng cho các ngành chịu ràng buộc pháp lý hoặc văn hóa cao như y tế, tài chính và luật.

---

### **1.2 — Ánh Xạ ADDIE Thành Các Subtasks Tính Toán**
Mỗi giai đoạn ADDIE được cụ thể hóa thành một subtask với input, output và tiêu chí xác thực rõ ràng:

| Giai đoạn | Input | Output | Xác thực |
|---|---|---|---|
| **Phân Tích** | Sách giáo khoa | JSON Core Concepts Graph, năng lực, kiến thức tiền đề | Độ bao phủ chuẩn MOET |
| **Thiết Kế** | Concepts Graph | Cấu trúc bài học, phân bổ thời gian (45 phút), sơ đồ đánh giá | Tổng thời gian ≤ 45 phút |
| **Phát Triển** | Bản phác thảo | Script-First Resources (lời thoại → slide/media) | Khớp nối kịch bản |
| **Triển Khai & Đánh Giá** | Giáo án đầy đủ | Giáo án đã phê duyệt (HITL) + nhật ký phản hồi sau dạy | Giáo viên ký duyệt |

---

### **1.3 — Mô Hình Tùy Chỉnh: Qwen 3 8B**
Đây là điểm kỹ thuật phân biệt ConnectED với các giải pháp thương mại khác.

**Chiến lược huấn luyện hai bước:**
1. **Học tăng cường (RL):** Điều chỉnh chuỗi suy luận (chain-of-thought) để tuân thủ quy trình ADDIE và kiến thức sư phạm Việt Nam.
2. **DPO (Direct Preference Optimization):** Huấn luyện mô hình ưu tiên câu trả lời trung thực với tập dữ liệu vàng, loại bỏ đầu ra sai sự thật.

**Tập dữ liệu nền tảng:**
- Wikipedia tiếng Việt, lọc theo chủ đề giáo dục.
- MetaMath (tập con tiếng Việt) — bộ toán học suy luận từng bước.
- Sách giáo khoa và đề thi theo chuẩn MOET.

**Kết quả:** Đạt điểm cao nhất trên benchmark **AIThucchien** (private test set) — bộ đánh giá giáo dục lập luận của Việt Nam.

**Tích hợp vào pipeline:**
- Hoạt động như engine lập luận chuyên dụng cho các bước yêu cầu độ chính xác cao nhất: trích xuất khái niệm, sinh mục tiêu học tập.
- Tự động fallback về Claude/DeepSeek khi cần tác vụ sáng tạo hoặc kiến thức ngoài phạm vi giáo dục.

---

### **1.4 — Vòng Lặp Tự Sửa Lỗi**
Tại mỗi giai đoạn, tác nhân không chỉ thực thi mà còn tự kiểm tra và sửa lỗi:

```
PLAN → ACT → OBSERVE (Xác thực JSON schema & thời lượng) → REFLECT & ITERATE
```

- Nếu validation thất bại: gửi phản hồi lỗi cụ thể kèm schema để tác nhân tự chỉnh sửa.
- Tối đa **3 lần thử** trước khi escalate lên giáo viên hoặc rollback về trạng thái trước.
- Mọi lần thử và kết quả đều được ghi nhật ký để phân tích sau.

---

### **1.5 — Giải Quyết Thách Thức Vận Hành**

**Độ tin cậy:** Xác thực JSON schema tại ranh giới giữa các giai đoạn phát hiện và sửa lỗi ngay lập tức, trước khi lỗi lan truyền sang bước tiếp theo.

**Đánh giá chất lượng:** Khung offline LLM-as-judge dùng Claude 4.6 Sonnet làm giám khảo, chấm điểm chất lượng sư phạm theo rubrics chuẩn hóa trước khi cập nhật mã nguồn vào production.

**Chi phí & Độ trễ:** Đặt prompts hệ thống MOET (cố định, lặp lại nhiều lần) ở đầu ngữ cảnh để tối ưu **prompt caching** — tiết kiệm đến 80% chi phí token đầu vào cho mỗi lần gọi.

**Giám sát vận hành:** Xuất vết thực thi (execution traces) sang AgentOps để kiểm toán toàn bộ chuỗi quyết định và phát hiện thắt nút cổ chai.
