---
name: chon-thu-theo-su-kien
description: Nhận sự kiện, chọn mẫu thư đúng, cá nhân hoá 2-3 câu từ dữ liệu khách, không gửi trùng trong 7 ngày.
---
# Chọn và gửi thư theo sự kiện của khách

## Khi nào dùng
Dùng kỹ năng này khi có sự kiện mới chuyển tới từ hệ thống của anh chị (ví dụ như khách bỏ giỏ hàng giữa chừng hoặc khách đã lâu không mua), hoặc khi anh chị yêu cầu xử lý trực tiếp một tệp dữ liệu khách hàng.
Ví dụ tin nhắn từ người dùng:
* "Em xem file sự kiện hôm nay, ai bỏ giỏ hàng thì chọn mẫu email nhắc mua rồi gửi nhé."
* "Có 5 khách cũ đã hơn tháng không mua, em chọn thư chăm sóc gửi cho họ giúp anh."

## Làm theo thứ tự
1. Đọc danh sách sự kiện từ file `sample-data/su-kien.jsonl` hoặc nhận thông tin trực tiếp từ webhook mà phần mềm của anh chị báo về.
2. Kiểm tra lịch sử nhận thư của từng khách. Nếu tụi em thấy khách đã nhận thư cùng loại trong vòng 7 ngày qua, lập tức bỏ qua người này để tránh làm phiền.
3. Mở thư mục `sample-data/mau-thu/` và chọn đúng mẫu thư khớp với loại sự kiện (thư nhắc giỏ hàng, thư hỏi thăm, thư chào mừng).
4. Viết thêm 2 đến 3 câu vào đầu thư để cá nhân hoá nội dung. Tụi em sẽ dựa vào tên khách, tên món hàng họ đang xem hoặc ngày cuối cùng họ mua hàng để viết.
5. DỪNG, hỏi người phụ trách: Gửi bản nháp của các email vừa soạn để anh chị xem lại và cho phép gửi.
6. Khi anh chị đã đồng ý, gọi API của MONA Mail (`POST /v1/emails` qua https://api.monamail.vn/v1) để phát thư đi.
7. Ghi nhận thời gian gửi và loại thư vào lịch sử của khách hàng để làm cơ sở lọc trùng cho những lần sau.

## Mẫu trả lời
* "Em đã soạn xong 5 email nhắc giỏ hàng dựa trên sự kiện hôm nay. Anh chị xem bản nháp dưới đây và báo em gửi nhé."
* "Các thư hỏi thăm đã được em gửi đi qua hệ thống MONA Mail. Tụi em cũng đã lưu lịch sử để đảm bảo tuần này không gửi lại thư tương tự cho họ."

## Không được làm
* Không phát hành bất kỳ email nào nếu chưa kiểm tra lịch sử 7 ngày qua của khách đó.
* Không tự ý gọi API gửi email khi chưa có sự đồng ý của anh chị trên bản nháp.
* Không ráp nhầm mẫu thư với sự kiện, khách mua xong thì không gửi thư nhắc thanh toán.
* Không tự ý hứa hẹn mã giảm giá hoặc quà tặng nếu mẫu thư gốc của anh chị không đề cập.

## Kiểm tra xong việc
* Thông tin cá nhân hoá như tên và món hàng trong thư phải khớp hoàn toàn với dữ liệu từ file sự kiện.
* Lịch sử gọi API `POST /v1/emails` phải báo thành công cho những email đã được duyệt.
* Danh sách khách hàng nhận thư không có ai bị trùng lặp nội dung so với 7 ngày trước đó.
