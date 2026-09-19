---
name: bao-cao-sang
description: Mỗi sáng 7h30 gửi 5 con số chủ chọn (doanh thu hôm qua, đơn, khách mới, tồn kho thấp, công nợ).
---
# Báo cáo năm con số quan trọng mỗi sáng cho chủ doanh nghiệp

## Khi nào dùng
- Khi anh chị dặn dò tụi em: "Sáng nào cũng gửi anh doanh thu với tồn kho nhé".
- Khi đồng hồ hệ thống điểm đúng 7h30 sáng mỗi ngày, tụi em sẽ tự động chạy quy trình này.
- Khi anh chị cần thay đổi số liệu cần xem, ví dụ: "Đổi cho chị số khách mới thành số đơn bị huỷ nha".

## Làm theo thứ tự
1. Chờ hệ thống báo đúng 7h30 sáng mỗi ngày.
2. Đọc lại danh sách 5 con số anh chị đã chốt theo dõi trong phần bộ nhớ.
3. Dịch các yêu cầu lấy số thành câu lệnh SQL chỉ đọc.
4. Chạy lệnh SQL này trên cơ sở dữ liệu Postgres của hệ thống bán hàng mà anh chị đang đặt tại MONA Cloud.
5. Gom cả 5 kết quả vào một tin nhắn tổng hợp thật dễ đọc.
6. Gửi tin nhắn đó qua kênh Telegram riêng của anh chị.
7. DỪNG, hỏi người phụ trách nếu chạy lệnh SQL gặp lỗi hoặc không thể nối vào cơ sở dữ liệu.

## Mẫu trả lời
Mẫu 1: 
Gửi anh chị báo cáo sáng nay. Doanh thu hôm qua là 45.000.000 đồng từ 12 đơn hàng. Mình có thêm 3 khách mới. Tồn kho đang thấp ở 2 mã hàng. Tổng công nợ cần thu hiện tại là 15.200.000 đồng.

Mẫu 2:
Anh chị xem tóm tắt số liệu hôm qua. Tụi em thống kê được 23 đơn hàng với tổng 112.500.000 đồng doanh thu. Có 5 khách hàng lần đầu mua. Kho đang có 8 món sắp hết. Công nợ khách đang giữ là 20.000.000 đồng. Anh chị cần hỏi sâu về số nào thì cứ nhắn tụi em.

## Không được làm
- Tuyệt đối không bao giờ dùng các lệnh làm thay đổi hay xoá dữ liệu như UPDATE hay DELETE.
- Không tự ý đoán mò hay tạo ra số ảo nếu cơ sở dữ liệu bị lỗi không trả về kết quả.
- Không gửi báo cáo vào nhóm chat chung, chỉ gửi riêng cho tài khoản Telegram của anh chị.
- Không đưa thêm các lời bình luận thừa thãi ngoài 5 con số anh chị yêu cầu.

## Kiểm tra xong việc
- Đã chạy thành công các lệnh SQL chỉ đọc trên hệ thống Postgres mà không làm ảnh hưởng dữ liệu gốc.
- Đã gửi đúng một tin nhắn chứa đủ 5 số liệu vào Telegram của anh chị đúng giờ.
