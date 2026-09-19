---
name: doi-huy-lich
description: Khách xin đổi/huỷ: kiểm quy tắc (trước 4 giờ), đề xuất 3 khung trống, cập nhật lịch, báo lễ tân.
---

# Xử lý yêu cầu khách đổi hoặc huỷ lịch hẹn

## Khi nào dùng
- Khách nhắn tin xin đổi sang ngày giờ khác. Ví dụ: "Chị muốn dời lịch chiều nay sang sáng mai được không?"
- Khách báo bận, muốn huỷ lịch hẹn. Ví dụ: "Hôm nay kẹt họp rồi, cho anh huỷ lịch cắt tóc lúc 5h nhé."

## Làm theo thứ tự
1. Lấy thông tin lịch hẹn hiện tại của khách từ file `sample-data/lich-hen.csv`.
2. Kiểm tra quy định của cơ sở: khách có báo trước 4 tiếng so với giờ hẹn không.
3. Nếu khách báo quá sát giờ, giải thích nhẹ nhàng quy định và DỪNG, hỏi người phụ trách xem có hỗ trợ ngoại lệ không.
4. Nếu hợp lệ và khách muốn đổi lịch, tìm 3 khung giờ trống gần nhất để đề xuất cho khách chọn.
5. Khi khách chọn giờ mới hoặc xác nhận huỷ, cập nhật lại dữ liệu vào file `sample-data/lich-hen.csv`.
6. Báo cáo ngay cho bộ phận lễ tân bằng cách gọi API MONA Mail qua `POST /v1/emails` đến `https://api.monamail.vn/v1`.

## Mẫu trả lời
- Đổi lịch thành công: "Tụi em đã dời lịch của anh chị sang 9h sáng mai. Cảm ơn anh chị đã báo trước nhé."
- Huỷ lịch: "Tiếc quá, tụi em đã ghi nhận huỷ lịch chiều nay. Khi nào thu xếp được thời gian, anh chị nhắn lại để tụi em tìm giờ trống khác nha."

## Không được làm
- Không tự ý cho phép đổi huỷ nếu khách báo dưới 4 tiếng mà chưa hỏi người phụ trách.
- Không đề xuất khung giờ mới khi chưa xem lại file để tránh xếp trùng lịch với người khác.
- Không quên gọi MONA Mail để gửi thông báo cho lễ tân, tránh việc các bạn vẫn ngồi chờ.
- Không dùng từ ngữ trách móc nếu khách huỷ sát giờ.

## Kiểm tra xong việc
- File `sample-data/lich-hen.csv` đã lưu chính xác giờ mới hoặc trạng thái huỷ.
- Lễ tân đã nhận được email báo thay đổi qua hệ thống MONA Mail.
- Khách đã nhận được tin nhắn xác nhận cuối cùng và không thắc mắc thêm.
