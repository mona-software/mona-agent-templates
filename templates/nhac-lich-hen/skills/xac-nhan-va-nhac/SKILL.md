---
name: xac-nhan-va-nhac
description: Đặt lịch xong gửi xác nhận, nhắc trước 24 giờ và 2 giờ, hỏi 'có tới không' để lễ tân biết.
---
# Xác nhận và nhắc lịch hẹn cho khách hàng

## Khi nào dùng
- Khi anh chị vừa thêm một lịch hẹn mới vào danh sách. Ví dụ khách nhắn: "Em ơi chị đặt lịch làm móng chiều nay 3h nhé".
- Khi hệ thống kiểm tra thấy sắp tới giờ hẹn của khách. Ví dụ: cần nhắc lịch cho anh Tuấn vào 9h sáng mai.

## Làm theo thứ tự
1. Đọc dữ liệu danh sách lịch hẹn từ tệp `sample-data/lich-hen.csv` trong thư mục máy.
2. Ngay khi có lịch mới, dùng công cụ gửi thư `POST /v1/emails` của MONA Mail để gửi email xác nhận lịch cho khách.
3. Kiểm tra danh sách những khách có lịch vào ngày mai. Nếu đúng 24 giờ trước giờ khách đến, gửi một tin nhắn nhắc nhở qua Telegram hoặc email.
4. Kiểm tra danh sách khách hẹn trong ngày hôm nay. Nếu đúng 2 giờ trước giờ bắt đầu, gửi tin nhắc cuối cùng và hỏi khách xem anh chị có tới đúng giờ không.
5. Đọc thư trả lời của khách qua công cụ đọc hộp thư `GET /v1/inboxes/{id}/messages` của MONA Mail hoặc kênh Telegram đang kết nối.
6. DỪNG, hỏi người phụ trách ở bàn lễ tân nếu khách báo tới trễ hoặc muốn đổi ngày, để lễ tân chủ động xếp lại công việc.

## Mẫu trả lời
- Mẫu xác nhận ban đầu: "Chào anh chị. Tụi em đã lưu lại lịch hẹn của mình vào lúc 15h chiều nay. Anh chị nhớ ghé đúng giờ giúp tụi em nhé."
- Mẫu nhắc trước 2 giờ: "Chào anh chị. Tụi em nhắn để nhắc lịch hẹn của mình sẽ bắt đầu trong 2 tiếng nữa. Anh chị phản hồi lại giúp tụi em biết mình có ghé đúng giờ được không nhé."

## Không được làm
- Không tự ý xoá hay đổi lịch của khách nếu chưa hỏi người phụ trách ở lễ tân.
- Không gửi tin nhắn nhắc nhở vào ban đêm vì sẽ làm phiền thời gian nghỉ ngơi của anh chị.
- Không hứa hẹn giảm giá hay đổi giờ làm việc nếu không có thông tin trong quy định của cửa hàng.
- Không dùng dịch vụ gửi thư nào khác ngoài MONA Mail để đảm bảo hệ thống có thể đọc được thư trả lời của khách.

## Kiểm tra xong việc
- Khách hàng đã nhận được tin nhắn đúng ba mốc thời gian quy định gồm lúc mới đặt, trước 24 giờ và trước 2 giờ.
- Tụi em đã nhận được câu trả lời chắc chắn của khách và báo lại tình hình cho lễ tân.
