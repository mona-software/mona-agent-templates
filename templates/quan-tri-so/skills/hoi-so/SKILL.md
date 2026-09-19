---
name: hoi-so
description: Dịch câu hỏi tiếng Việt thành SQL đọc-only, chạy, trả lời kèm số và cách tính; không bao giờ UPDATE/DELETE.
---
# Truy vấn số liệu từ cơ sở dữ liệu bằng câu hỏi tiếng Việt

## Khi nào dùng
- Khi anh chị hỏi một câu cần tính toán dựa trên dữ liệu thật đang có trong cơ sở dữ liệu bán hàng. Ví dụ: "Tháng trước bán được bao nhiêu tiền?", "Khách nào mua nhiều nhất tuần rồi?".
- Khi anh chị muốn đối chiếu lại một con số trong báo cáo. Ví dụ: "Lấy cho em danh sách 5 đơn hàng lớn nhất bị huỷ hôm qua".
- Khi anh chị cần kiểm tra tồn kho nhanh. Ví dụ: "Còn bao nhiêu cái áo mã A01?".

## Làm theo thứ tự
1. Đọc kỹ câu hỏi của anh chị để xác định các yếu tố cần tính gồm thời gian, điều kiện lọc và trường dữ liệu cần nhóm.
2. Kiểm tra cấu trúc cơ sở dữ liệu hiện tại trong file `sample-data/schema.sql` để biết tên bảng, tên cột và kiểu dữ liệu.
3. Dịch câu hỏi sang mã SQL dạng SELECT. Dùng công cụ kết nối cơ sở dữ liệu Postgres của MONA Cloud qua MCP `monacloud-mcp` để gửi truy vấn.
4. Chạy nháp mã SQL vừa viết. Nếu báo lỗi cấu trúc, xem lại file sơ đồ và sửa lại câu lệnh.
5. Nếu câu truy vấn lấy ra quá nhiều dòng, giới hạn lại bằng lệnh LIMIT 10 hoặc DỪNG, hỏi người phụ trách xem anh chị có muốn xem hết toàn bộ không.
6. Gom kết quả lấy được, tính toán lại một lần nữa để đối chiếu với yêu cầu gốc.
7. Soạn câu trả lời cho anh chị. Nêu rõ kết quả thu được và giải thích ngắn gọn cách tụi em đã tính con số này để anh chị yên tâm.

## Mẫu trả lời
Mẫu 1: Trả lời câu hỏi tổng
"Tháng trước, tổng doanh thu đã trừ hàng hoàn là 155.000.000 đồng. Tụi em tính bằng cách lấy tổng tiền các đơn ở trạng thái thành công từ ngày 1 tới ngày 31 tháng trước."

Mẫu 2: Trả lời câu hỏi danh sách
"Hôm qua có 3 đơn hàng lớn bị huỷ. Đơn lớn nhất trị giá 5.000.000 đồng của khách tên Nam vì lý do giao trễ. Hai đơn còn lại em để ở danh sách bên dưới cho anh chị xem chi tiết."

## Không được làm
- Tuyệt đối không chạy các lệnh thay đổi dữ liệu như UPDATE, DELETE, INSERT, DROP, ALTER. Chỉ dùng lệnh đọc SELECT.
- Không tự ý làm tròn số nếu anh chị chưa cho phép. Số tiền phải hiện đủ chữ số.
- Không đoán mò dữ liệu. Nếu bảng thiếu cột thông tin anh chị hỏi, báo ngay là cơ sở dữ liệu hiện tại chưa có thông tin này.
- Không gửi toàn bộ bảng dữ liệu dài hàng ngàn dòng ra đoạn chat để tránh trôi tin nhắn.

## Kiểm tra xong việc
- Đã cung cấp đúng con số hoặc danh sách theo đúng câu hỏi của anh chị chưa.
- Lời giải thích cách tính có rõ ràng và đúng logic thông thường không.
- Chắc chắn không có bất kỳ lệnh thay đổi dữ liệu nào được gửi xuống cơ sở dữ liệu.
