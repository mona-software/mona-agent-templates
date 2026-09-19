---
name: canh-han-gia-han
description: Mỗi sáng kiểm domain sắp hết hạn 30/7/1 ngày, nhắc khách, gia hạn khi khách duyệt, không tự gia hạn.
---
# Canh ngày hết hạn và xin phép gia hạn tên miền

## Khi nào dùng

Anh chị cần nhắc khách hàng đóng phí duy trì tên miền khi ngày hết hạn đến gần.
Ví dụ tin nhắn từ anh chị: "Sáng nay em check xem khách nào sắp hết hạn tên miền thì báo để anh gửi nhắc nhé."
Ví dụ khác: "Tên miền thecoffee.com.vn của anh Minh báo sắp hết hạn, em lên MONA Domain làm thủ tục gia hạn giúp anh."

## Làm theo thứ tự

1. Mỗi sáng, tụi em đọc danh sách khách hàng và tên miền trong file `sample-data/khach-domain.csv`.
2. Dùng các tool thuộc nhóm `cloud_domain_*` của MONA Domain (monadomain.vn) để lấy ngày hết hạn của từng tên miền.
3. Lọc ra các tên miền chỉ còn đúng ba mươi ngày, bảy ngày hoặc một ngày là hết hạn.
4. Tổng hợp danh sách tên miền sắp hết hạn kèm tên khách hàng tương ứng.
5. DỪNG, hỏi người phụ trách: Gửi danh sách qua Telegram cho anh chị xem xét nên nhắc khách nào.
6. Khi anh chị đồng ý nhắc, tụi em soạn tin nhắn mẫu để anh chị chép gửi cho khách.
7. Đợi anh chị báo khách đã gật đầu đồng ý gia hạn và đã chuyển tiền.
8. Khi anh chị cho phép, dùng tool của MONA Domain để thực hiện thao tác gia hạn thêm một năm.

## Mẫu trả lời

Mẫu báo danh sách: "Sáng nay em thấy tên miền tiembot.com của chị Ngọc còn bảy ngày nữa là hết hạn. Anh chị có muốn em soạn tin nhắc chị Ngọc không?"

Mẫu báo sau khi gia hạn: "Em đã làm lệnh gia hạn thêm một năm cho tên miền tiembot.com xong rồi anh chị nhé. Anh chị kiểm tra lại xem cần em hỗ trợ gì thêm không."

## Không được làm

- Tuyệt đối không tự ý dùng tool gia hạn khi chưa có lệnh từ anh chị.
- Không tự động gửi tin nhắn trực tiếp cho khách hàng cuối, mọi liên lạc đều thông qua anh chị.
- Không nhắc lại những tên miền anh chị đã dặn là khách bỏ không dùng nữa.
- Không tự nghĩ ra số ngày còn lại hoặc giá tiền gia hạn.

## Kiểm tra xong việc

- Danh sách tên miền sắp hết hạn ba mươi, bảy, một ngày được báo cáo đủ vào mỗi sáng.
- Mọi lệnh gia hạn đều có tin nhắn xác nhận anh chị đã cho phép.
- Tên miền đã gia hạn hiển thị ngày hết hạn mới trong hệ thống MONA Domain.
