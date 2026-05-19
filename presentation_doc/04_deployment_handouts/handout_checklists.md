# Tài Liệu Hướng Dẫn: Danh Sách Kiểm Tra (Checklists)
## Các Danh Sách Kiểm Tra Thực Tế Cho Hệ Thống Tác Nhân Hoạt Động Thực Tế (Production Agentic Systems)

---

## CHECKLIST 1: Agentic System Deployment

Sử dụng danh sách này trước khi đưa bất kỳ hệ thống dựa trên tác nhân (agent-based system) nào vào hoạt động thực tế (production).

### Kiến Trúc và Thiết Kế (Architecture and Design)
- [ ] [CRITICAL] Tác vụ đã được phân rã thành các tác vụ phụ (subtasks) có ranh giới rõ ràng kèm schemas dữ liệu.
- [ ] [CRITICAL] Các điểm kiểm duyệt của con người (Human-in-the-loop checkpoints) đã được kích hoạt cho các hành động có rủi ro cao.
- [ ] [RECOMMENDED] Kiến trúc hệ thống được phân cấp (hierarchical) (không sử dụng prompts nguyên khối monolithic).
- [ ] [RECOMMENDED] Các kỹ năng (Skills) được đóng gói dưới dạng các tệp riêng độc lập, được kiểm soát phiên bản (version-controlled).
- [ ] [ADVANCED] Xác định tiêu chí dừng rõ ràng (không chỉ dựa vào giới hạn số lượt lặp tối đa max iterations).

### An Toàn và Rào Chắn (Safety and Guardrails)
- [ ] [CRITICAL] Các ràng buộc hệ thống ngăn chặn các thay đổi trạng thái (state mutations) trái phép.
- [ ] [CRITICAL] API keys và các thông tin bí mật (secrets) được lưu trữ trong biến môi trường (env variables) an toàn, không để trong ngữ cảnh prompt.
- [ ] [RECOMMENDED] Lọc sạch dữ liệu đầu vào/đầu ra (Input/output sanitization) được kích hoạt để ngăn chặn tấn công injection.
- [ ] [RECOMMENDED] Áp dụng hạn mức cứng (hard cap) cho ngân sách token tối đa trên mỗi lần thực thi tác vụ.

### Hạ Tầng & Vận Hành (Infrastructure & Operations)
- [ ] [CRITICAL] Các cuộc gọi API sử dụng bộ xử lý thử lại với thời gian trễ tăng dần (exponential backoff retry handlers).
- [ ] [RECOMMENDED] Nhật ký ghi lại đầy đủ tham số mô hình, dữ liệu vào, dữ liệu ra và chi phí token.
- [ ] [RECOMMENDED] Các cuộc gọi công cụ (tool calls) được thiết kế có tính không đổi (idempotent) (để an toàn khi gọi lại).

---

## CHECKLIST 2: Pipeline and Prompt Optimization

Sử dụng danh sách này khi xem xét hoặc cấu trúc lại các prompts và quy trình của tác nhân.

### Thiết Kế Prompt (Prompt Design)
- [ ] System prompt tập trung vào một trách nhiệm duy nhất và cô lập.
- [ ] Các hướng dẫn sử dụng câu mệnh lệnh trực tiếp (ví dụ: "Trích xuất..." thay vì "Vui lòng trích xuất...").
- [ ] Định dạng đầu ra được quy định cụ thể theo cấu trúc schema (JSON/YAML) kèm theo các ví dụ few-shot.
- [ ] Các ràng buộc và quy tắc phủ định được nêu rõ ràng.

### Quản Lý Ngữ Cảnh (Context Management)
- [ ] Việc sử dụng cửa sổ ngữ cảnh được theo dõi cụ thể cho từng giai đoạn của quy trình.
- [ ] Lịch sử hội thoại dài được tóm tắt lại trước khi đưa lại vào mô hình.
- [ ] Kết quả truy hồi RAG được xếp hạng và cắt ngắn chỉ lấy N kết quả hàng đầu.

### Định Tuyến Mô Hình (Model Routing)
- [ ] Các tác vụ phân loại hoặc định tuyến đơn giản được ủy quyền cho các mô hình nhỏ (1B-8B).
- [ ] Các tác vụ lập kế hoạch và lập luận phức tạp được định tuyến đến các frontier hoặc reasoning models.
- [ ] Thực hiện các thử nghiệm A/B kiểm tra tính tương đương về chất lượng khi chuyển xuống mô hình rẻ hơn để giảm chi phí.

---

## CHECKLIST 3: Token and Cost Reduction

Sử dụng danh sách này để tối ưu hóa chi phí suy luận một cách có hệ thống.

### Đo Lường & Lưu Trữ Đệm (Measurement & Caching)
- [ ] Lượng token sử dụng (đầu vào, đầu ra, số lượt hit cache) được theo dõi cho mỗi lần thực hiện tác vụ.
- [ ] Các system prompts và templates dùng chung sử dụng cơ chế prompt caching.
- [ ] Các bất thường về chi phí (tăng đột ngột gấp 10 lần) sẽ kích hoạt cảnh báo hệ thống tự động.

### Nén Prompt (Prompt Compression)
- [ ] Loại bỏ các hướng dẫn thừa và các từ đệm lịch sự không cần thiết.
- [ ] Độ dài đầu ra được giới hạn rõ ràng trong prompts (ví dụ: "dưới 3 câu").
- [ ] Các ví dụ few-shot không thiết yếu được thay thế bằng phương pháp fine-tuning.

---

## CHECKLIST 4: Reliability and Evaluation

Sử dụng danh sách này để đo lường và nâng cao độ bền bỉ của tác nhân.

### Giảm Thiểu Thất Bại (Failure Mitigation)
- [ ] Hệ thống có khả năng ngăn chặn các vòng lặp lập kế hoạch (planning loops) và việc báo cáo hoàn thành sớm khi chưa xong.
- [ ] Dữ liệu đầu vào của công cụ (tool inputs) được xác thực trước khi thực thi để ngăn chặn lỗi tham số.
- [ ] Các lộ trình chuyển giao cho con người (escalation paths) được xác định cụ thể cho các sự kiện có độ không chắc chắn cao.

### Đánh Giá Quỹ Đạo (Trajectory Evaluation)
- [ ] Bộ thử nghiệm tự động xác minh tính hiệu quả của các bước thực thi trung gian (trajectory efficiency).
- [ ] Bộ thử nghiệm hồi quy (regression tests) bao phủ các quỹ đạo thất bại trong quá khứ.
- [ ] Tiến hành đánh giá thủ công hàng tuần trên một mẫu đại diện của các phiên chạy thực tế.

---

## CHECKLIST 5: AgentOps Readiness

Sử dụng danh sách này để thiết lập khả năng hiển thị và giám sát vận hành.

### Đo Lường & Theo Dấu (Telemetry & Tracing)
- [ ] Telemetry theo vết toàn bộ hành trình lập luận song song với đầu vào/đầu ra của công cụ.
- [ ] Các quỹ đạo thất bại có thể được phát lại (replayed) hoàn toàn trong môi trường thử nghiệm cô lập (sandbox).
- [ ] Các vết nhật ký (trace logs) được che (mask) các dữ liệu nhạy cảm của người dùng và doanh nghiệp.

### Quản Trị & Cải Tiến (Governance & Improvement)
- [ ] Các sự kiện phản hồi của người dùng được liên kết trực tiếp với các trace IDs đang hoạt động.
- [ ] Đặt lịch đánh giá hàng tuần đối với nhật ký các quỹ đạo thất bại.
- [ ] Các nâng cấp về prompt và mô hình phải vượt qua các bài kiểm tra hồi quy trước khi triển khai rộng rãi.
