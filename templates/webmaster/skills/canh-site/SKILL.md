---
name: canh-site
description: Ping 1 phút/lần, kiểm mã HTTP, thời gian phản hồi, hạn SSL; đổi trạng thái thì báo, hết sự cố báo lại.
---

# Theo dõi trang web liên tục
## Khi nào dùng
Tụi em làm việc này khi anh chị có trang web hoặc phần mềm đang chạy thực tế trên máy chủ MONA Cloud hoặc máy chủ khác và cần người canh chừng liên tục ngày đêm.
Ví dụ anh chị nhắn: "Tụi em canh chừng trang bán hàng giúp anh chị, cứ mỗi một phút thì kiểm tra xem trang có bị sập không."
Hoặc anh chị yêu cầu: "Nhớ theo dõi chứng chỉ bảo mật của trang chủ, nếu còn dưới bảy ngày thì báo ngay."

## Làm theo thứ tự
1. Đọc nội dung trong tệp cấu hình chứa danh sách điểm lấy mẫu để lấy danh sách tên miền cần canh chừng và các con số giới hạn cho phép.
2. Hẹn giờ để cứ đúng một phút lại gọi thử tới các trang web này nhằm kiểm tra xem máy chủ có phản hồi không.
3. Ghi nhận tình trạng hiện tại bao gồm mã trạng thái trả về, số giây cần thiết để tải xong trang và số ngày còn lại của chứng chỉ bảo mật.
4. Đối chiếu tình trạng vừa thu thập với tình trạng của đúng một phút trước đó.
5. Nếu trang web đang hoạt động bỗng nhiên báo lỗi hoặc thời gian tải chậm hơn mức cho phép, tụi em sẽ gửi thông báo kèm theo các dòng ghi chép hệ thống gần nhất vào nhóm Telegram.
6. Nếu chứng chỉ bảo mật chuẩn bị hết hạn theo con số đã cài đặt, tụi em cũng nhắn tin nhắc nhở.
7. DỪNG, hỏi người phụ trách trong nhóm kỹ thuật nếu lỗi không thuộc nhóm các ca đơn giản được phép tự xử lý như khởi động lại dịch vụ, dọn dẹp các tệp lưu trữ khi đầy đĩa hay gia hạn chứng chỉ bảo mật.
8. Khi sự cố qua đi và trang web tải bình thường trở lại, tụi em gửi một tin nhắn báo cáo đã hết lỗi để mọi người yên tâm.

## Mẫu trả lời
* Tụi em báo cáo, trang web đang không truy cập được do báo lỗi máy chủ, thời điểm bắt đầu ghi nhận sự cố là 09:20.
* Tin vui là trang web đã phản hồi bình thường, chỉ mất một chút thời gian ngắn để tải xong, tụi em sẽ tiếp tục canh chừng.

## Không được làm
* Không hứa hẹn tính năng cài đặt bằng một thao tác bấm phím vì trên trang web đăng ký tính năng này đang là bản thử, anh chị vẫn cần chạy mã nguồn mở OpenClaw rồi đưa lên máy chủ.
* Không đề xuất gửi cảnh báo qua hệ thống Zalo vì OpenClaw chưa có cầu nối Zalo OA, tụi em chỉ nhận việc và báo cáo thông qua Telegram.
* Không sử dụng tài khoản mô hình trí tuệ nhân tạo của công ty vì hệ thống chưa mở, tụi em lấy khóa kết nối của chính anh chị nạp vào hoặc dùng phần mềm Ollama chạy tại chỗ hoàn toàn kín.
* Không báo lỗi liên tục mỗi phút gây ồn ào, tụi em chỉ nhắn tin duy nhất một lần khi trang web chuyển từ trạng thái bình thường sang lỗi hoặc từ lỗi sang bình thường.

## Kiểm tra xong việc
* Tụi em đã đọc đúng danh sách trang web cần canh chừng từ dữ liệu anh chị nạp vào tệp cấu hình.
* Đã gửi thành công tin nhắn cảnh báo đầu tiên vào nhóm Telegram khi thử ngắt kết nối trang web.
* Lịch kiểm tra tự động chạy trơn tru đều đặn từng phút mà không bị ngắt quãng.
