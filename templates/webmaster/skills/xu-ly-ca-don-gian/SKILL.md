---
name: xu-ly-ca-don-gian
description: Ca cho phép: restart dịch vụ, xoay log đầy đĩa, gia hạn SSL; ca khác chỉ báo người, kèm log 50 dòng cuối.
---
# Tự động xử lý các sự cố website cơ bản

## Khi nào dùng
Tụi em dùng hướng dẫn này khi phát hiện website hoặc máy chủ đang chạy trên MONA Cloud hoặc VPS khác của anh chị gặp vấn đề thông qua hệ thống cảnh báo, hoặc khi anh chị trực tiếp yêu cầu kiểm tra.
- Khi nhận được cảnh báo dịch vụ nền (như phần mềm chạy web, phần mềm cơ sở dữ liệu) bị tắt. Ví dụ, anh chị nhắn vào nhóm Telegram: "Kiểm tra xem trang chủ báo lỗi kết nối dữ liệu xử lý sao em."
- Khi nhận cảnh báo dung lượng đĩa cứng sắp đầy do các tệp ghi chú hoạt động (file log) lớn dần theo thời gian.
- Khi chứng chỉ bảo mật kết nối (SSL) sắp hết hạn hoặc báo lỗi không hợp lệ.

## Làm theo thứ tự
1. Xác định sự cố hiện tại có nằm trong 3 loại được cho phép tự xử lý hay không: khởi động lại dịch vụ (restart), xoay vòng tệp nhật ký để trống đĩa (log rotation), và gia hạn SSL.
2. Nếu sự cố không thuộc 3 loại trên (ví dụ: máy chủ mất kết nối hoàn toàn, lỗi bên trong mã nguồn ứng dụng), tụi em dùng bộ công cụ `monacloud-mcp` để truy cập máy chủ MONA Cloud và rút trích 50 dòng gần nhất từ tệp ghi chú lỗi (error log).
3. DỪNG, hỏi người phụ trách qua Telegram, gửi kèm 50 dòng log vừa lấy để anh chị có thông tin đánh giá.
4. Nếu sự cố nằm trong nhóm được phép, tụi em tự động chạy lệnh tương ứng: khởi động lại dịch vụ đang tắt, nén và xoá bớt các tệp log quá cũ, hoặc gọi lệnh cập nhật SSL.
5. Chờ 30 giây sau khi chạy lệnh, tụi em kiểm tra lại trang web bằng cách gửi thử yêu cầu kết nối để xem lỗi đã hết chưa.
6. Nhắn tin báo cáo vào nhóm Telegram cho anh chị biết sự cố đã diễn ra, thao tác vừa thực hiện và kết quả cuối cùng.
7. Nếu tụi em đã thử xử lý nhưng vẫn báo lỗi, DỪNG, hỏi người phụ trách kèm theo nhật ký lỗi để anh chị vào kiểm tra sâu hơn.

## Mẫu trả lời
Mẫu khi gặp sự cố lạ không được phép tự làm:
"Tụi em thấy website domain.vn đang báo lỗi 502. Ca này cần anh chị xem xét, em gửi kèm 50 dòng log lỗi cuối cùng của dịch vụ web bên dưới nha."

Mẫu khi đã tự xử lý xong:
"Máy chủ vừa bị báo đầy đĩa do tệp log quá lớn, tụi em đã nén và dọn dẹp các tệp log cũ tháng trước. Hiện tại dung lượng trống đã trở lại mức an toàn, anh chị yên tâm nha."

## Không được làm
- Không tự ý khởi động lại toàn bộ máy chủ (reboot) mà chỉ thao tác trên từng dịch vụ cụ thể bị lỗi để tránh ảnh hưởng các ứng dụng khác đang chạy bình thường.
- Không xoá, sửa đổi mã nguồn trang web, cấu hình hệ thống hay cơ sở dữ liệu; chỉ được phép dọn dẹp các tệp log cũ không còn dùng.
- Không bịa thêm các nguyên nhân sự cố hoặc tự đoán lỗi nếu thông tin trong tệp log chưa rõ ràng.
- Không báo cáo liên tục nhiều lần cho cùng một sự cố chưa được khắc phục để tránh gây phiền hà trong nhóm Telegram của anh chị.
- Không hứa hẹn với anh chị là nhấn nút cài đặt sửa lỗi 1 chạm đang chạy ngay vì tính năng này hiện tại đang là bản thử nghiệm, chưa mở chính thức.

## Kiểm tra xong việc
- Sự cố đã được phân loại đúng vào nhóm tự xử lý hoặc nhóm cần báo cáo anh chị.
- Đã thực hiện thao tác khắc phục hoặc lấy đúng 50 dòng log cuối cùng tùy theo nhóm sự cố.
- Tin nhắn báo cáo tình trạng đã được gửi thành công vào kênh Telegram của nhóm kỹ thuật.
