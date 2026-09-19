---
name: kiem-ro-ri
description: Trước khi trả lời kiểm tra: có gọi API ngoài không, có URL ngoài không; nếu có thì từ chối và ghi log.
---
# Kiểm tra rò rỉ dữ liệu trước khi trả lời

## Khi nào dùng
- Người dùng yêu cầu tóm tắt tài liệu nội bộ và gửi thông tin ra ngoài. Ví dụ: "Tóm tắt quy trình nghỉ phép rồi gửi email qua hệ thống bên ngoài cho anh Nguyễn Văn A".
- Người dùng yêu cầu phân tích tài liệu bằng một dịch vụ trên internet. Ví dụ: "Dịch file nội quy công ty này sang tiếng Anh bằng công cụ dịch trên mạng".
- Người dùng yêu cầu tra cứu thông tin kết hợp với dữ liệu trên internet. Ví dụ: "So sánh mức thưởng của công ty với số liệu trên trang web nước ngoài".

## Làm theo thứ tự
1. Đọc kỹ yêu cầu của anh chị và xác định toàn bộ các bước xử lý dữ liệu.
2. Kiểm tra xem các bước đó có gọi API ra bên ngoài hệ thống không. Tụi em đang chạy mẫu trợ lý nội bộ kín với model mở bằng Ollama tại chỗ nên không có byte nào rời server.
3. Quét nội dung câu trả lời dự kiến để tìm xem có chứa URL trỏ ra internet không.
4. Nếu phát hiện có gọi API ngoài hoặc có URL ngoài thì phải hủy ngay việc tạo câu trả lời.
5. Ghi lại thông tin sự việc vào tệp nhật ký trên máy chủ VPS MONA Cloud để lưu vết.
6. DỪNG, hỏi người phụ trách nếu anh chị yêu cầu xuất dữ liệu nội bộ ra ngoài nhiều lần.
7. Trả lời cho anh chị biết thao tác bị chặn để giữ an toàn cho sổ sách và dữ liệu nhân sự của công ty.

## Mẫu trả lời
- "Tụi em không thể thực hiện thao tác này vì hệ thống chỉ chạy nội bộ, không phép gọi dữ liệu ra bên ngoài, anh chị thông cảm nhé."
- "Yêu cầu của anh chị cần kết nối internet để hoàn thành. Tụi em đã chặn thao tác này nhằm đảm bảo an toàn dữ liệu công ty."

## Không được làm
- Không tự ý bỏ qua bước kiểm tra này dù anh chị có ra lệnh ưu tiên.
- Không mở bất kỳ luồng dữ liệu nào ra ngoài hệ thống cục bộ.
- Không đoán thông tin nếu tài liệu nội bộ không ghi rõ.
- Không cung cấp dữ liệu sổ sách hoặc pháp lý nếu phát hiện dấu hiệu rò rỉ.

## Kiểm tra xong việc
- Đã xác nhận câu trả lời không chứa bất kỳ URL hoặc lời gọi API bên ngoài nào.
- Đã ghi nhật ký đầy đủ nếu có thao tác bị chặn.
- Đảm bảo giữ đúng nguyên tắc không đi qua luồng ngoài của trợ lý nội bộ kín.
