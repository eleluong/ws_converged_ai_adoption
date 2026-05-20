# Tài Liệu Hướng Dẫn: Danh Sách Kiểm Tra (Checklists)
## ConnectED & Hệ Sinh Thái Tác Nhân AI Mới Nổi (The Emerging Agentic AI Stack)
### Các Danh Sách Kiểm Tra Thực Tế Cho Hệ Thống Tác Nhân Hoạt Động Thực Tế (Production Agentic Systems)

---

> **Cách sử dụng tài liệu hướng dẫn này:**
> Hãy rà soát kỹ lưỡng từng danh sách kiểm tra khi xây dựng hoặc đánh giá một hệ thống tác nhân AI.
> Các mục được đánh dấu **[CRITICAL]** là bắt buộc phải có cho môi trường production.
> Các mục được đánh dấu **[RECOMMENDED]** đại diện cho các thực tiễn tốt nhất giúp tối ưu hóa hệ thống.
> Các mục được đánh dấu **[ADVANCED]** áp dụng cho các hệ thống phức tạp hoặc có tính rủi ro cao.

---

## THAM CHIẾU NHANH: Các Khái Niệm Cốt Lõi

### Vòng Lặp Tác Nhân (Agentic Loop)
```
PLAN (Lên kế hoạch) → ACT (Hành động) → OBSERVE (Quan sát) → REFLECT (Phản tư) → ITERATE (Lặp lại) → COMPLETE (Hoàn thành)
```

### Agentic Stack (Từ dưới lên trên)
```
1. Orchestration Layer    (Máy trạng thái tùy chỉnh, LangChain, CrewAI, AutoGen)
2. Reasoning Core         (Định tuyến mô hình: Frontier models, Reasoning models, Small models)
3. Skills                 (Tri thức nghiệp vụ đóng gói: Trích xuất khái niệm, Thiết kế hoạt động)
4. Tools & Protocols      (Truy vấn sách giáo khoa qua MCP, ủy quyền thanh toán AP2, APIs)
5. Memory Systems         (Bộ nhớ ngắn hạn episodic, Vector DB dài hạn)
```

### Quy Trình ConnectED
```
Concept Extraction → Objective Generation → Activity Design
→ Content Development → Visual Materials (qua AP2) → Evaluation Review
```

### Mô Hình Sư Phạm ADDIE
```
Analyze (Phân tích) → Design (Thiết kế) → Develop (Phát triển) → Implement (Triển khai) → Evaluate (Đánh giá)
```

---

## CHECKLIST 1: Agentic System Deployment

Sử dụng danh sách này trước khi đưa bất kỳ hệ thống dựa trên tác nhân (agent-based system) nào vào hoạt động thực tế (production).

### Kiến Trúc và Thiết Kế (Architecture and Design)

- [ ] **[CRITICAL]** Tác vụ đã được phân rã thành các tác vụ phụ (subtasks) có ranh giới rõ ràng kèm schemas dữ liệu.
- [ ] **[CRITICAL]** Các điểm kiểm duyệt của con người (Human-in-the-loop checkpoints) đã được kích hoạt cho các hành động có rủi ro cao (ví dụ: giáo viên phê duyệt trước khi gọi thanh toán AP2 mua học liệu STEM trong ConnectED).
- [ ] **[CRITICAL]** Mỗi subtask đều có mô tả lỗi dự phòng và phương án fallback xử lý lỗi.
- [ ] **[RECOMMENDED]** Kiến trúc hệ thống được phân cấp (hierarchical) (ví dụ: tách biệt trích xuất khái niệm khỏi thiết kế hoạt động thay vì dùng prompt nguyên khối).
- [ ] **[RECOMMENDED]** Mỗi giai đoạn đều tạo đầu ra có cấu trúc và được xác thực schema nghiêm ngặt (ví dụ: kiểm tra JSON Concept Graph trước khi bắt đầu tạo Objectives).
- [ ] **[RECOMMENDED]** Các kỹ năng (Skills) được đóng gói dưới dạng các tệp riêng độc lập, được kiểm soát phiên bản trong Git.
- [ ] **[RECOMMENDED]** Các quy định về bản địa hóa ngữ cảnh được nhúng trực tiếp vào các templates và prompts (ví dụ: chuẩn thuật ngữ MOET).
- [ ] **[ADVANCED]** Xác định tiêu chí dừng rõ ràng và giới hạn số lượt tự sửa sai (ví dụ: tự sửa tối đa 3 lần trước khi gửi cảnh báo HITL cho con người).
- [ ] **[ADVANCED]** Ngân sách chi phí tối đa của tác vụ được giới hạn và kiểm soát cứng ở lớp điều phối.

### An Toàn và Rào Chắn (Safety and Guardrails)

- [ ] **[CRITICAL]** Các ràng buộc hệ thống ngăn chặn các thay đổi trạng thái (state mutations) trái phép được thực thi ở tầng code, không chỉ mô tả trong prompt.
- [ ] **[CRITICAL]** API keys và các thông tin bí mật (secrets) được lưu trữ trong biến môi trường an toàn, không để trong ngữ cảnh prompt.
- [ ] **[CRITICAL]** Lọc sạch dữ liệu đầu ra (Output sanitization) trước khi hiển thị cho người dùng cuối.
- [ ] **[RECOMMENDED]** Áp dụng hạn mức cứng (hard cap) cho ngân sách token tối đa trên mỗi lần thực thi tác vụ.
- [ ] **[RECOMMENDED]** Xác định lộ trình chuyển giao cho con người khi điểm tin cậy suy giảm dưới ngưỡng an toàn.
- [ ] **[ADVANCED]** Tiến hành red-team và tấn công thử nghiệm (adversarial testing) trên các prompts và công cụ.
- [ ] **[ADVANCED]** Áp dụng ủy quyền mật mã và hợp đồng Intent Mandate của AP2 để kiểm soát quyền mua sắm tự động của tác nhân.

### Hạ Tầng & Vận Hành (Infrastructure & Operations)

- [ ] **[CRITICAL]** Các cuộc gọi API sử dụng bộ xử lý thử lại với thời gian trễ tăng dần (exponential backoff retry handlers).
- [ ] **[CRITICAL]** Tác nhân có khả năng hạ cấp dịch vụ mượt mà khi API bên ngoài ngừng hoạt động.
- [ ] **[RECOMMENDED]** Nhật ký ghi lại đầy đủ tham số mô hình, dữ liệu vào, dữ liệu ra và chi phí token.
- [ ] **[RECOMMENDED]** Các cuộc gọi công cụ (tool calls) được thiết kế có tính không đổi (idempotent) (để an toàn khi gọi lại).
- [ ] **[RECOMMENDED]** Trạng thái tác nhân được lưu trữ bền vững để có thể khôi phục phiên làm việc khi lỗi (ví dụ: lưu episodic memory giáo án đang soạn dở).
- [ ] **[ADVANCED]** Cài đặt cầu dao ngắt mạch (circuit breakers) cho các công cụ bị lỗi liên tục.

### Sẵn Sàng Ra Mắt (Launch Readiness)

- [ ] **[CRITICAL]** Bộ kiểm thử tích hợp cuối luồng (end-to-end test suite) đạt tỷ lệ thành công >90% trên các bộ dữ liệu đại diện.
- [ ] **[CRITICAL]** Kịch bản ứng phó sự cố được tài liệu hóa rõ ràng (ai xử lý, cách rollback).
- [ ] **[RECOMMENDED]** Triển khai thử nghiệm từng bước (canary deployment) trước khi mở rộng toàn hệ thống.
- [ ] **[RECOMMENDED]** Xây dựng kênh phản hồi trực tiếp từ người dùng thực tế ngay từ ngày đầu.

---

## CHECKLIST 2: Pipeline and Prompt Optimization

Sử dụng danh sách này khi xem xét hoặc cấu trúc lại các prompts và quy trình của tác nhân.

### Thiết Kế Prompt (Prompt Design)

- [ ] System prompt tập trung vào một trách nhiệm duy nhất và cô lập (ví dụ: chỉ trích xuất, không kiêm nhiệm viết giáo án).
- [ ] Các hướng dẫn sử dụng câu mệnh lệnh trực tiếp (ví dụ: "Trích xuất..." thay vì "Vui lòng trích xuất...").
- [ ] Định dạng đầu ra được quy định cụ thể theo cấu trúc schema (JSON/YAML) kèm theo các ví dụ few-shot.
- [ ] Các ràng buộc và quy tắc phủ định được nêu rõ ràng.
- [ ] Loại bỏ các ngữ cảnh không liên quan để tiết kiệm token và tránh làm loãng sự chú ý của mô hình.
- [ ] Thuật ngữ nghiệp vụ thống nhất trong toàn bộ hệ thống prompt.

### Cấu Trúc Quy Trình (Pipeline Structure)

- [ ] Mỗi giai đoạn (stage) có một trách nhiệm duy nhất và có thể xác thực (no "and also" stages).
- [ ] Ranh giới giữa các giai đoạn được xác định bằng hợp đồng dữ liệu rõ ràng (input/output schemas).
- [ ] **[RECOMMENDED]** Phân rã tác vụ (Task Decomposition) được áp dụng một cách hệ thống để chia nhỏ các tác vụ lập luận phức tạp thành các tác vụ phụ tuyến tính hoặc phân cấp, giúp thu hẹp phạm vi suy luận và giảm tỷ lệ ảo tưởng (hallucination).
- [ ] **[RECOMMENDED]** Cô lập trạng thái (State Isolation) được duy trì giữa các giai đoạn đã phân rã (mỗi giai đoạn chỉ nhận dữ liệu đầu vào tối thiểu cần thiết, tránh chuyển tiếp toàn bộ ngữ cảnh gây phình to token).
- [ ] Các giai đoạn có thể chạy song song được xác định và thực thi song song để giảm thiểu độ trễ cho người dùng.
- [ ] Việc xác thực diễn ra ở mọi ranh giới giai đoạn, không chỉ ở đầu ra cuối cùng.
- [ ] Chiến lược xử lý lỗi rõ ràng cho từng giai đoạn (thử lại, bỏ qua, fallback, báo cáo lên con người).
- [ ] Thứ tự giai đoạn được tối ưu hóa (các giai đoạn tốn kém chỉ chạy sau khi các giai đoạn xác thực rẻ hơn đã vượt qua).
- [ ] Các giai đoạn bế tắc (luôn thất bại khi xác thực) được phát hiện và cảnh báo sớm.

### Quản Lý Ngữ Cảnh (Context Management)

- [ ] Việc sử dụng cửa sổ ngữ cảnh được theo dõi cụ thể cho từng giai đoạn của quy trình.
- [ ] Lịch sử hội thoại dài được tóm tắt lại trước khi đưa lại vào mô hình.
- [ ] Kết quả truy hồi RAG được xếp hạng và cắt ngắn chỉ lấy N kết quả hàng đầu.
- [ ] Sử dụng các tính năng prompt caching cho các tài liệu tiêu chuẩn dùng chung ở đầu ngữ cảnh.

### Định Tuyến Mô Hình (Model Routing)

- [ ] Các tác vụ phân loại hoặc định tuyến đơn giản được ủy quyền cho các mô hình nhỏ/tiện ích (Llama 3.3 70B, Gemini 2.5 Flash).
- [ ] Các tác vụ lập kế hoạch và lập luận phức tạp được định tuyến đến các frontier hoặc reasoning models (Claude 4.6 Sonnet / DeepSeek-R1).
- [ ] **[RECOMMENDED]** Định tuyến ngữ nghĩa (Semantic Routing) được triển khai (bằng độ tương đồng embedding, bộ lọc từ khóa, hoặc bộ phân loại siêu nhẹ) để phân loại ý định người dùng và dẫn hướng đến luồng tác nhân, prompt chuyên biệt, hoặc kích thước mô hình tối ưu.
- [ ] **[RECOMMENDED]** Logic định tuyến tối ưu hóa bộ nhớ đệm prompt (Prompt Caching), đảm bảo các truy vấn được định tuyến khớp với các khối prompt hệ thống cố định đã được lưu cache trước đó.
- [ ] Thực hiện các thử nghiệm A/B kiểm tra tính tương đương về chất lượng khi chuyển xuống mô hình rẻ hơn để giảm chi phí.

---

## CHECKLIST 3: Token and Cost Reduction

Sử dụng danh sách này để tối ưu hóa chi phí suy luận một cách có hệ thống.

### Đo Lường & Lưu Trữ Đệm (Measurement & Caching)

- [ ] Lượng token sử dụng (đầu vào, đầu ra, số lượt hit cache) được theo dõi cho mỗi lần thực hiện tác vụ.
- [ ] Các system prompts và templates dùng chung (ví dụ: bộ tiêu chuẩn chương trình học MOET) được xếp ở đầu ngữ cảnh để tối ưu prompt caching (giúp giảm tới 80% chi phí).
- [ ] **[RECOMMENDED]** Định tuyến ngữ nghĩa (Semantic Routing) được sử dụng để chuyển đổi linh hoạt giữa mô hình lập luận lớn đắt đỏ (như Claude 4.6 Sonnet, DeepSeek-R1) và mô hình nhỏ rẻ tiền (như Llama 3.3 70B, Gemini 2.5 Flash) dựa trên độ phức tạp của yêu cầu.
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
- [ ] Tiến hành đánh giá offline bằng cơ chế LLM-as-judge (sử dụng mô hình độc lập chấm điểm chất lượng sư phạm và độ phủ chương trình học của quỹ đạo).

---

## CHECKLIST 5: AgentOps Readiness

Sử dụng danh sách này để thiết lập khả năng hiển thị và giám sát vận hành.

### Telemetry & Tracing

- [ ] Telemetry theo vết toàn bộ hành trình lập luận (Plan -> Act -> Observe -> Reflect) song song với đầu vào/đầu ra của công cụ.
- [ ] Các quỹ đạo thất bại có thể được phát lại (replayed) hoàn toàn trong môi trường thử nghiệm cô lập để phục vụ gỡ lỗi.
- [ ] Các vết nhật ký (trace logs) được che (mask) các dữ liệu nhạy cảm của người dùng và doanh nghiệp.

### Quản Trị & Cải Tiến (Governance & Improvement)

- [ ] Các sự kiện phản hồi của người dùng được liên kết trực tiếp với các trace IDs đang hoạt động.
- [ ] Đặt lịch đánh giá hàng tuần đối với nhật ký các quỹ đạo thất bại.
- [ ] Các nâng cấp về prompt và mô hình phải vượt qua các bài kiểm tra hồi quy trước khi triển khai rộng rãi.
