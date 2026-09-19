---
name: theo-doi-va-dung
description: Đọc bounce/unsubscribe từ MONA Mail, đưa vào danh sách dừng, báo cáo tuần: gửi, mở, mua lại.
---
# Theo dõi và dừng gửi thư khi có yêu cầu hoặc lỗi

## Khi nào dùng
- Khi anh chị muốn dọn dẹp danh sách nhận thư hàng tuần để tránh bị đánh dấu thư rác. Ví dụ tin nhắn từ người phụ trách: "Tuần này có ai huỷ đăng ký nhận thư không em, gom lại giúp anh nhé."
- Khi anh chị cần thống kê hiệu quả của đợt gửi thư vừa qua. Ví dụ tin nhắn từ người phụ trách: "Lấy báo cáo số lượng thư mở và số người mua lại trong tuần này cho chị xem."
- Khi có một nhóm khách hàng không tồn tại địa chỉ email (thư bị dội lại), anh chị cần loại bỏ ngay lập tức để bảo vệ uy tín hòm thư.

## Làm theo thứ tự
1. Lấy thông báo lỗi gửi thư (thư bị dội lại do email không tồn tại hoặc đầy hộp thư) thông qua API của MONA Mail bằng cách gọi `GET /v1/inboxes/{id}/messages`.
2. Lọc ra các địa chỉ email có chứa từ khóa từ chối nhận thư hoặc nhấn vào liên kết huỷ đăng ký từ khách hàng.
3. Cập nhật các email lỗi và email huỷ đăng ký vào danh sách dừng (danh sách đen) trong tập tin dữ liệu hiện tại của anh chị.
4. Lấy số liệu thống kê tổng số thư đã gửi thành công và số thư đã được khách hàng mở xem thông qua các sự kiện được ghi nhận.
5. Đối chiếu danh sách email đã mở thư với dữ liệu sự kiện mua hàng trong tập tin sự kiện `sample-data/su-kien.jsonl` để đếm số lượng khách hàng quay lại mua hàng.
6. DỪNG, hỏi người phụ trách: Gửi danh sách email dự kiến đưa vào danh sách dừng để anh chị xem qua trước khi chốt.
7. Sau khi anh chị đồng ý, tiến hành lưu danh sách dừng và gửi báo cáo tổng hợp tuần bao gồm số lượng gửi, số lượng mở, số khách mua lại.

## Mẫu trả lời
- "Em đã lọc được 15 email bị lỗi và 2 khách hàng yêu cầu huỷ nhận thư. Anh chị xem qua danh sách này xem em có nên chặn gửi thư tiếp cho họ không nhé."
- "Báo cáo tuần này đã xong rồi anh chị ơi. Tụi em gửi thành công 500 thư, có 120 người mở xem và 15 người đã mua hàng lại. Danh sách chặn cũng đã được cập nhật."

## Không được làm
- Không tự ý xóa hẳn thông tin khách hàng khỏi dữ liệu gốc, chỉ được đánh dấu vào danh sách dừng gửi thư.
- Không gửi tiếp bất kỳ thư nào cho những địa chỉ email đã nằm trong danh sách dừng.
- Không tự ý gửi báo cáo cho người khác ngoài người phụ trách đã được cấu hình trong tập tin `USER.md`.
- Không bịa ra số liệu thống kê số thư mở hoặc số người mua lại nếu chưa kiểm tra chéo với dữ liệu sự kiện thật.

## Kiểm tra xong việc
- Tất cả email lỗi gửi hoặc có yêu cầu huỷ đăng ký đều đã được chuyển vào danh sách dừng.
- Báo cáo tuần có đầy đủ ba thông tin gồm tổng số thư gửi đi, số thư được mở và số lượng khách hàng mua lại.
- Dữ liệu báo cáo phải khớp chính xác với thông tin trả về từ MONA Mail và tập tin sự kiện của anh chị.
