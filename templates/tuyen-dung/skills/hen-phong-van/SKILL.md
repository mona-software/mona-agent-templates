---
name: hen-phong-van
description: Gửi mail hẹn phỏng vấn theo khung giờ chủ cho, xác nhận lại, nhắc trước 2 giờ.
---
# Hẹn lịch phỏng vấn và nhắc nhở ứng viên tự động

## Khi nào dùng
- Anh chị phụ trách đã duyệt hồ sơ trên kênh Telegram và giao cho tụi em đi hẹn lịch. Ví dụ tin nhắn: "Hẹn ứng viên Nguyễn Văn A vào sáng thứ 3 hoặc chiều thứ 5 nhé".
- Ứng viên gửi email vào hộp thư hỏi thông tin lịch phỏng vấn. Ví dụ tin nhắn: "Cho hỏi lịch phỏng vấn của mình vào ngày nào?".
- Tới hạn nhắc lịch phỏng vấn trước 2 giờ so với thời gian chốt.

## Làm theo thứ tự
1. Nhận danh sách khung giờ từ anh chị phụ trách, tìm lại tên và email ứng viên trong hồ sơ.
2. Dùng công cụ của MONA Mail để gửi thư mời phỏng vấn cho ứng viên. Gọi API POST /v1/emails để gửi thư kèm các lựa chọn giờ phỏng vấn.
3. Đọc hộp thư bằng GET /v1/inboxes/{id}/messages để chờ ứng viên phản hồi email.
4. Khi ứng viên chọn giờ, dùng API gửi email thứ hai để chốt lịch chính thức. Nếu ứng viên đề xuất giờ khác nằm ngoài danh sách, DỪNG, hỏi người phụ trách qua Telegram.
5. Gửi thông báo về kênh Telegram báo cho anh chị phụ trách biết lịch đã chốt.
6. Thiết lập nhắc hẹn. Trước 2 giờ diễn ra phỏng vấn, dùng MONA Mail gửi một email ngắn nhắc ứng viên nhớ tham gia.

## Mẫu trả lời
- Gửi ứng viên qua email: "Chào anh chị, công ty xin chúc mừng anh chị đã vượt qua vòng hồ sơ. Tụi em có các khung giờ trống vào 9:00 sáng mai và 2:00 chiều thứ 5. Anh chị phản hồi email này để chọn khung giờ phù hợp nhé."
- Gửi anh chị phụ trách qua Telegram: "Ứng viên Nguyễn Văn A đã chốt lịch phỏng vấn vào 9:00 sáng mai. Tụi em đã gửi thư xác nhận và sẽ nhắc ứng viên trước 2 giờ."

## Không được làm
- Không hứa hẹn khung giờ khi anh chị phụ trách chưa đồng ý.
- Không gửi thư chốt lịch nếu ứng viên chưa xác nhận rõ ràng bằng văn bản.
- Không chia sẻ thông tin của ứng viên này cho bên thứ ba hoặc ứng viên khác.
- Không tự ý trả lời các câu hỏi hóc búa của ứng viên, phải hỏi lại anh chị phụ trách.

## Kiểm tra xong việc
- Email mời và chốt lịch đã gửi đi thành công tới đúng địa chỉ của ứng viên.
- Lịch hẹn chốt xong đã báo cáo cho anh chị phụ trách qua Telegram.
- Có bước theo dõi thời gian để gửi email nhắc nhở trước 2 giờ.
