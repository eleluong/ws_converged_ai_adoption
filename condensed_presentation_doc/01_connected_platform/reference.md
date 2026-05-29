# **ConnectED: Nền Tảng AI-Native Cho Giáo Dục Việt Nam**

## **Tổng Quan**
ConnectED là nền tảng soạn giáo án AI-native dành cho hệ thống giáo dục K–12 Việt Nam, hỗ trợ tạo giáo án chuẩn chương trình quốc gia, slide bài giảng kèm kịch bản thuyết minh, và phòng thí nghiệm ảo (virtual labs) tích hợp.

Điểm khác biệt cốt lõi: ConnectED thiết kế việc soạn giáo án như một **quy trình sư phạm có hệ thống** — không chỉ đơn thuần truy xuất nội dung — thông qua sự kết hợp giữa khung sư phạm chuẩn, điều phối tác nhân phân cấp và đồ thị tri thức chương trình học. Mẫu thiết kế này có thể tái sử dụng cho các ngành chịu ràng buộc pháp lý hoặc văn hóa cao như y tế, tài chính và luật.

---

## **Bối Cảnh Vấn Đề**
Giáo viên Việt Nam mất trung bình **3–4 tiếng** chuẩn bị cho mỗi tiết dạy, bao gồm xác định mục tiêu, trích xuất khái niệm, thiết kế hoạt động, soạn kịch bản và chuẩn bị đánh giá.

Các LLM thương mại hiện tại không giải quyết được bài toán này vì áp dụng tiêu chuẩn phương Tây, dùng thuật ngữ không đồng bộ với MOET, thiếu bản địa hóa và đề xuất các hoạt động không phù hợp thực tế địa phương. ConnectED được xây dựng để lấp đầy khoảng trống này, với **bản địa hóa sâu** và **neo giữ sư phạm chặt chẽ** như những nguyên tắc thiết kế nền tảng.

---

## **Nền Tảng Thiết Kế Sư Phạm: ADDIE**
Quy trình soạn bài được ánh xạ thành các giai đoạn tính toán có cấu trúc, với input, output và tiêu chí xác thực rõ ràng tại mỗi bước:

1. **Phân Tích (Analyze):** Xử lý sách giáo khoa để xác định khái niệm cốt lõi, kết quả học tập mong đợi, kiến thức tiền đề, năng lực cần đạt và ràng buộc giảng dạy.
2. **Thiết Kế (Design):** Phác thảo cấu trúc bài học, chuỗi hoạt động, phân bổ thời gian (trong khung 45 phút) và sơ đồ đánh giá.
3. **Phát Triển (Develop):** Tạo tài nguyên theo quy trình **Kịch Bản Trước (Script-First)** — soạn lời thoại thuyết minh trước, thiết kế slide và media sau — đảm bảo sự mạch lạc giữa nội dung và hình thức.
4. **Triển Khai & Đánh Giá (Implement & Evaluate):** Giáo viên phê duyệt và chỉnh sửa trên UI (Human-in-the-loop); thu thập phản hồi sau tiết dạy để liên tục tối ưu prompt và template.

---

## **Quy Trình Xử Lý Đa Tác Nhân Phân Cấp**
Thay vì dùng một prompt nguyên khối, ConnectED phân rã quá trình soạn giáo án thành pipeline đa tác nhân phân cấp:

```
[Concept Extraction] → [Objective Gen] → [Activity Design] → [Content Dev] → [Visuals] → [Teacher Review]
```

**Bảng chi tiết từng giai đoạn:**

| Giai đoạn | Đầu Vào | Đầu Ra | Xác Thực Quan Trọng |
|---|---|---|---|
| **1. Concept Extraction** | Sách giáo khoa & Chương trình học | Concept Graph | Độ bao phủ so với chuẩn MOET |
| **2. Objective Gen** | Concept Graph | Mục tiêu Bloom's | Tính khả thi (Actionability) |
| **3. Activity Design** | Các mục tiêu | Tiến trình hoạt động | Tổng thời gian ≤ 45 phút |
| **4. Content Dev** | Bản phác thảo hoạt động | Kịch bản & Nội dung Slide | Sự đồng bộ về thuật ngữ |
| **5. Media Gen** | Kịch bản & Văn bản Slide | Hướng dẫn lab & Prompts hoạt cảnh | Khớp nối kịch bản (Narrative match) |
| **6. Evaluation Review** | Trọn bộ gói bài giảng | Review trên UI của giáo viên | Chốt kiểm soát Human-in-the-loop |

Kiến trúc phân tầng này giảm độ phức tạp của từng prompt, hạn chế ảo tưởng và cho phép gỡ lỗi độc lập theo module.

---

## **Ánh Xạ Lên Agentic Stack Hiện Đại**
Mỗi lớp của ConnectED tương ứng trực tiếp với một tầng trong Agentic Stack 5 lớp:

- **L1 — Orchestration:** Máy trạng thái hữu hạn tùy chỉnh đảm bảo tính xác định (determinism) và ngăn rò rỉ trạng thái.
- **L2 — Reasoning Core:** Định tuyến ngữ nghĩa lai giữa mô hình lớn (Claude 4.6 Sonnet / Qwen 3 8B fine-tuned) cho lập luận sư phạm sâu và mô hình nhỏ (Llama 3.3 70B / Gemini 2.5 Flash) cho các tác vụ tiện ích — giảm 70% chi phí, 45% độ trễ.
- **L3 — Skills:** Mỗi bước soạn giáo án được đóng gói thành một Skill Module độc lập (prompts + JSON validation schemas), quản lý phiên bản qua Git.
- **L4 — Tools & Protocols:** MCP truy cập kho sách giáo khoa MOET; AP2 (Intent Mandates + Cart Mandates) mua bản quyền học liệu trực quan STEM có giáo viên kiểm duyệt.
- **L5 — Memory:** Bộ nhớ episodic khôi phục trạng thái phiên soạn bài đang dở; Vector DB lưu hồ sơ và phong cách giảng dạy của từng giáo viên để cá nhân hóa lâu dài.

---

## **Vòng Lặp Tác Nhân Cốt Lõi (Core Agentic Loop)**
Tại mỗi giai đoạn, tác nhân chạy vòng lặp khép kín:

```
PLAN → ACT → OBSERVE (Xác thực JSON schema & thời lượng) → REFLECT & ITERATE
```

Khi validation thất bại, tác nhân tự sửa đổi tối đa **3 lần** trước khi escalate lên giáo viên hoặc rollback về trạng thái trước đó.

---

## **Mô Hình LLM Tùy Chỉnh: Qwen 3 8B Cho Giáo Dục Việt Nam**
Để đạt độ chính xác sư phạm cao nhất, ConnectED phát triển mô hình chuyên biệt dựa trên **Qwen 3 8B**:

- **Chiến lược huấn luyện:** Học tăng cường (RL) điều chỉnh chuỗi suy luận tuân thủ quy trình ADDIE và kiến thức sư phạm Việt Nam; DPO (Direct Preference Optimization) giúp mô hình ưu tiên câu trả lời trung thực, loại bỏ đầu ra sai sự thật.
- **Tập dữ liệu nền tảng:** Wikipedia tiếng Việt (lọc theo chủ đề giáo dục), MetaMath (tập con tiếng Việt) và sách giáo khoa/đề thi chuẩn MOET.
- **Kết quả:** Đạt điểm cao nhất trên benchmark giáo dục lập luận **AIThucchien** (private test set).
- **Tích hợp pipeline:** Hoạt động như engine lập luận chuyên dụng cho các bước yêu cầu độ chính xác cao (trích xuất khái niệm, sinh mục tiêu); tự động fallback về Claude/DeepSeek khi cần tác vụ sáng tạo hoặc kiến thức rộng.

---

## **Giải Quyết Thách Thức Vận Hành**
- **Độ tin cậy:** Xác thực JSON schema tại ranh giới giữa các giai đoạn giúp phát hiện và sửa lỗi ngay lập tức.
- **Đánh giá:** Khung offline LLM-as-judge (Claude 4.6 Sonnet làm giám khảo) chấm điểm chất lượng sư phạm trước khi cập nhật mã nguồn.
- **Chi phí & Độ trễ:** Đặt prompts hệ thống MOET cố định lên đầu ngữ cảnh để tối ưu prompt caching — tiết kiệm đến **80% chi phí token đầu vào**.
- **Khả năng giám sát:** Xuất vết thực thi (traces) sang AgentOps để kiểm toán và phát hiện thắt nút cổ chai.

---

## **Tác Động**
Giảm thời gian chuẩn bị bài giảng từ **3–4 giờ** xuống còn **15–20 phút**, trong khi vẫn duy trì chất lượng sư phạm xuất sắc và đảm bảo chuẩn chương trình quốc gia.
