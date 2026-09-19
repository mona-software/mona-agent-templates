---
name: tra-va-giu-domain
description: Tra 5 biến thể tên, báo giá VND, giữ chỗ (reserve) cho khách duyệt, mua khi khách gật; .vn cần bản khai + eKYC do khách làm 1 lần.
---

# Tra cứu và giữ chỗ tên miền cho khách

## Khi nào dùng
- Khách hàng nhắn muốn tìm tên miền mới cho dự án. Ví dụ tin nhắn: "Tụi em tra giúp anh xem tên miền thietbivesinhsg còn đuôi nào trống, anh tính làm web mới".
- Khách hàng có ý tưởng nhưng chưa chốt tên chính xác, cần xem các lựa chọn khả thi. Ví dụ tin nhắn: "Tụi em tìm vài tên miền về bán trái cây nhập khẩu đuôi .vn giùm chị".

## Làm theo thứ tự
1. Xác định ý tưởng chính của khách hàng.
2. Dùng công cụ `cloud_domain_search` để tra cứu tên khách yêu cầu cùng 4 biến thể liên quan (thêm từ khoá, đổi đuôi .vn, .com.vn, .com).
3. Lọc ra các tên miền chưa có người mua và lấy giá tiền VND (tham khảo .vn 756.000đ, .com 432.000đ đã bao gồm VAT).
4. Tổng hợp danh sách tên miền khả thi kèm giá tiền rồi gửi cho khách xem. DỪNG, hỏi người phụ trách.
5. Khi khách chọn được tên ưng ý, dùng công cụ `cloud_domain_reserve` để giữ chỗ tên miền đó ngay, tránh bị người khác mua mất.
6. Nếu khách chọn tên miền đuôi .vn, tụi em sẽ báo khách cần làm thủ tục bản khai và xác thực danh tính điện tử eKYC một lần theo quy định. DỪNG, hỏi người phụ trách.
7. Sau khi thủ tục hoàn tất và khách gật đầu mua, dùng công cụ `cloud_domain_register` để tiến hành đăng ký chính thức tên miền.
8. Báo cho khách biết tên miền đã mua thành công và lưu thông tin vào danh sách `sample-data/khach-domain.csv`.

## Mẫu trả lời
- "Em đã tra thử thì tên thietbivesinhsg.com có người mua rồi, nhưng thietbivesinhsg.vn và thietbivesinhsg.com.vn vẫn còn trống. Giá đuôi .vn là 756.000đ, anh xem ưng ý đuôi nào thì nhắn để em giữ chỗ liền nha."
- "Tên miền traicaynhap.vn chị chọn em đã giữ chỗ xong rồi. Chị điền giúp em phần bản khai và xác thực danh tính eKYC theo đường dẫn này để em tiến hành đăng ký chính thức luôn nha."

## Không được làm
- Tụi em không tự ý đăng ký mua tên miền khi khách chưa đồng ý giá tiền và tên cụ thể.
- Tụi em không tiến hành mua tên miền .vn nếu khách chưa hoàn tất thủ tục bản khai và xác thực eKYC.
- Tụi em không tự nghĩ ra giá tiền, chỉ báo đúng mức giá lấy từ hệ thống của MONA Domain.

## Kiểm tra xong việc
- Khách hàng đã nhận được danh sách tên miền khả thi kèm giá bán VND rõ ràng.
- Tên miền khách chọn đã được giữ chỗ thành công trên hệ thống.
- Thông tin tên miền mới mua đã được ghi nhận đầy đủ vào danh sách quản lý của anh chị.
