---
name: xu-ly-tre-va-hoan
description: Đơn quá hạn giao hoặc hoàn: gom thành danh sách, đề xuất hành động, chờ người duyệt rồi gửi khách.
---
# Xử lý đơn hàng giao trễ và bị hoàn trả

## Khi nào dùng
Dùng khi cần theo dõi sát các đơn bị kẹt trên đường giao hoặc khách không nhận hàng. Ví dụ:
- Người dùng nhắn: "Tụi em kiểm tra xem hôm nay có đơn nào giao trễ không để báo khách."
- Người dùng nhắn: "Gom danh sách đơn bị hoàn hôm qua rồi gửi qua nhóm Telegram nha."

## Làm theo thứ tự
1. Đọc dữ liệu mã vận đơn và thông tin từ file danh sách đơn `sample-data/don-van-chuyen.csv`.
2. Gọi API tra cứu của đơn vị vận chuyển mà cửa hàng đang dùng để lấy trạng thái mới nhất của các đơn này.
3. Lọc ra các đơn quá hạn giao so với ngày dự kiến hoặc đơn bị chuyển sang trạng thái hoàn hàng.
4. Gom các đơn có vấn đề thành một danh sách gọn gàng kèm lý do và đề xuất cách giải quyết. Ví dụ đề xuất: gửi email xin lỗi khách vì trễ, báo kho nhận lại hàng hoàn.
5. Gửi danh sách này qua nhóm Telegram vận hành để xin ý kiến.
6. DỪNG, hỏi người phụ trách trong nhóm Telegram xem chốt phương án nào.
7. Sau khi người phụ trách duyệt, gọi MONA Mail qua API `POST /v1/emails` để gửi email thông báo cho khách.

## Mẫu trả lời
- Báo cáo nhóm vận hành: "Tụi em vừa gom được 2 đơn giao trễ và 1 đơn hoàn hàng. Anh chị xem danh sách bên trên và chốt giúp em cách xử lý nha."
- Email gửi khách hàng: "Chào anh chị, đơn hàng MD123 đang gặp sự cố giao chậm hơn dự kiến do mưa bão. Tụi em đang hối thúc bên giao hàng và sẽ theo dõi sát đơn này cho anh chị."

## Không được làm
- Không tự ý gọi MONA Mail để gửi thư cho khách khi chưa có người duyệt trên Telegram.
- Không đoán mò trạng thái đơn hàng, chỉ lấy đúng dữ liệu từ API tra cứu của đơn vị vận chuyển.
- Không đổ lỗi trực tiếp cho bên giao hàng với lời lẽ tiêu cực khi soạn nội dung xin lỗi khách.

## Kiểm tra xong việc
- Danh sách đơn trễ và hoàn đã được gửi đầy đủ vào nhóm Telegram.
- Đã nhận được quyết định từ người phụ trách và gọi API gửi email xong xuôi.
- Đã thông báo lại cho nhóm vận hành là khách hàng đã nhận được email báo tình trạng đơn.
