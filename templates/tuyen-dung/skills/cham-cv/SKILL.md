---
name: cham-cv
description: Đọc CV từ hộp thư, chấm theo tiêu chí có trọng số, xếp hạng, ghi lý do từng điểm.
---
# Đọc và chấm điểm hồ sơ ứng viên

## Khi nào dùng
- Tình huống 1: Ứng viên gửi hồ sơ qua email. Anh chị muốn biết người này có phù hợp với yêu cầu tuyển dụng không. Ví dụ: "Kiểm tra giúp hồ sơ Tuấn mới gửi có đủ điểm kinh nghiệm không nhé."
- Tình huống 2: Doanh nghiệp cần lọc nhanh hàng chục hồ sơ vừa nhận. Ví dụ: "Hôm nay có 10 hồ sơ nộp vị trí Sale, xếp hạng từ cao xuống thấp cho anh chị nha."
- Tình huống 3: Cần biết lý do cụ thể vì sao một hồ sơ bị đánh giá thấp. Ví dụ: "Vì sao hồ sơ của Vy chỉ được 4 điểm?"

## Làm theo thứ tự
1. Lấy thông tin hộp thư nhận hồ sơ của doanh nghiệp bằng cách gọi lệnh GET /v1/inboxes/{id}/messages của MONA Mail. MONA Mail là dịch vụ cung cấp hộp thư để tụi em có thể nhận thư, đọc nội dung và tải file đính kèm của người tìm việc gửi tới.
2. Mở file sample-data/jd-sale.md để lấy mô tả công việc và file sample-data/tieu-chi.csv để lấy bảng tiêu chí. Đây là dữ liệu anh chị nạp vào để tụi em biết doanh nghiệp đang tìm người như thế nào.
3. Đọc nội dung hồ sơ, đối chiếu từng mục với bảng tiêu chí để chấm điểm. Tụi em xử lý thông tin ngay trên máy của anh chị qua Ollama hoặc qua key model của chính anh chị đưa vào.
4. Viết rõ lý do vì sao cho mức điểm đó ở từng tiêu chí. Nếu thông tin trong hồ sơ ghi chung chung thì tụi em sẽ đánh dấu lại để anh chị lưu ý.
5. Cộng tổng điểm và xếp hạng từ cao xuống thấp nếu có nhiều hồ sơ nộp cùng lúc.
6. DỪNG, hỏi người phụ trách qua Telegram để đưa kết quả xếp hạng.

## Mẫu trả lời
- "Tụi em vừa nhận được 3 hồ sơ nộp vị trí Sale. Cao điểm nhất là hồ sơ của Tuấn đạt 8.5/10, điểm mạnh là có 2 năm kinh nghiệm đúng ngành. Anh chị xem chi tiết ở báo cáo, tụi em có nên chuyển sang bước hẹn phỏng vấn không?"
- "Hồ sơ của Vy chỉ đạt 4/10. Ứng viên thiếu phần tiếng Anh theo tiêu chí anh chị đưa ra ở đầu vào. Tụi em tạm để hồ sơ này sang nhóm chờ đánh giá lại."

## Không được làm
- Không tự ý gửi email từ chối người tìm việc khi chưa có lệnh từ anh chị.
- Không thiên vị hoặc tự chấm điểm theo cảm tính, chỉ dựa đúng vào danh sách tiêu chí mà anh chị đã cung cấp.
- Không tự bịa thêm kinh nghiệm hoặc kỹ năng nếu trong hồ sơ không ghi rõ.
- Không báo người dùng bấm chạy bằng 1 click trên trang chủ vì tính năng này đang là bản thử.
- Không tìm cách nhắn tin qua Zalo vì hiện tại chưa có cầu nối sang kênh này, tụi em chỉ báo tin qua Telegram.

## Kiểm tra xong việc
- Đã đọc đúng hồ sơ mới nhất từ hộp thư do MONA Mail cấp.
- Đã chấm điểm đủ cho mọi tiêu chí và ghi rõ lý do.
- Đã gửi báo cáo điểm số qua Telegram để chờ quyết định từ anh chị.
