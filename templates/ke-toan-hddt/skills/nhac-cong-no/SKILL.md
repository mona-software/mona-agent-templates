---
name: nhac-cong-no
description: Mỗi sáng gửi danh sách công nợ quá hạn, soạn mail nhắc lịch sự qua MONA Mail khi chủ duyệt.
---
# Nhắc công nợ khách hàng mỗi sáng và gửi email

## Khi nào dùng

- Khi đến giờ báo cáo buổi sáng và anh chị cần biết danh sách khách hàng đang nợ quá hạn. Ví dụ tin nhắn từ anh chị: "Hôm nay có ai nợ quá hạn không em?"
- Khi anh chị muốn gửi thư nhắc nợ cho một danh sách khách hàng cụ thể. Ví dụ tin nhắn từ anh chị: "Soạn mail nhắc nợ cho công ty ABC gửi anh xem trước nhé."

## Làm theo thứ tự

1. Đọc dữ liệu từ file `sample-data/cong-no.csv` để tìm các khoản nợ đã quá ngày thanh toán theo thỏa thuận.
2. Tổng hợp danh sách khách hàng nợ quá hạn, số dư nợ và số ngày trễ hẹn thành một báo cáo ngắn gọn gửi qua Telegram cho anh chị nắm thông tin.
3. DỪNG, hỏi người phụ trách xem anh chị có muốn gửi thư nhắc nợ cho những khách hàng này trong hôm nay không.
4. Nếu anh chị đồng ý, tiến hành soạn nội dung thư lịch sự, nêu rõ số tiền và mã hóa đơn. Gọi API POST /api/v1/acb/qr-payment/generate của MONA Pay, đây là API ngân hàng và dịch vụ xác nhận thanh toán tự động, để tạo mã VietQR động chứa sẵn số tiền đính kèm vào thư giúp khách quét mã trả tiền ngay.
5. Gửi bản nháp thư cho anh chị xem trước qua Telegram. DỪNG, hỏi người phụ trách chốt nội dung thư.
6. Sau khi anh chị duyệt, dùng công cụ API POST /v1/emails của hệ thống MONA Mail để chính thức gửi thư đi.
7. Ghi nhận lại thời gian đã gửi thư nhắc nợ vào hệ thống để theo dõi cho những ngày sau.

## Mẫu trả lời

- Sáng nay em thấy có 3 khách hàng đang nợ quá hạn tổng cộng 45 triệu, anh chị có muốn em soạn mail nhắc nợ luôn không?
- Em đã gửi thư nhắc nợ cho công ty ABC qua MONA Mail rồi, tiền vào tài khoản em sẽ báo ngay cho anh chị.

## Không được làm

- Không tự động gửi thư nhắc nợ khi chưa có sự đồng ý của anh chị.
- Không dùng từ ngữ gay gắt hay đe dọa trong thư nhắc nợ.
- Không bịa thêm số liệu hoặc thông tin khách hàng không có trong file dữ liệu gốc.
- Không tự ý tra cứu các luồng thông tin ngoài hoặc gọi API chưa được cấp phép.

## Kiểm tra xong việc

- Đã gửi danh sách công nợ quá hạn chính xác cho anh chị vào buổi sáng.
- Thư nhắc nợ đã được anh chị duyệt và gửi đi thành công qua hệ thống MONA Mail.
- Đã ghi chú lại lịch sử nhắc nợ để tránh gửi trùng lặp vào ngày mai.
