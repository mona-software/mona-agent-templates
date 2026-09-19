---
name: tra-cuu-noi-bo
description: Trả lời từ tài liệu nội bộ, trích đúng đoạn, ghi tên file; không đoán.
---
# Tra cứu và trả lời từ tài liệu nội bộ

## Khi nào dùng
- Khi nhân viên hỏi về quy định, chính sách, hoặc quy trình làm việc của công ty. Ví dụ: "Năm nay anh được nghỉ mấy ngày phép?", "Quy trình xin cấp máy tính mới như thế nào?"
- Khi cần lấy thông tin chính xác từ các tài liệu đã lưu trữ để giải đáp thắc mắc. Ví dụ: "Quy định đi làm trễ phạt bao nhiêu tiền nằm ở tệp nào?"

## Làm theo thứ tự
1. Nhận câu hỏi từ nhân viên qua phần mềm nhắn tin nội bộ (OpenClaw) hoặc nhóm Telegram kín.
2. Tìm kiếm thông tin trong các tệp văn bản ở thư mục tài liệu nội bộ do công ty cung cấp, ví dụ như `sample-data/noi-quy.md` hoặc `sample-data/quy-trinh-nghi-phep.md`.
3. Đọc kỹ nội dung tìm thấy để đảm bảo thông tin trả lời đúng trọng tâm câu hỏi của nhân viên.
4. Trích xuất chính xác đoạn văn bản chứa câu trả lời.
5. Soạn tin nhắn trả lời, bắt buộc phải trích dẫn nguyên văn đoạn văn bản và ghi rõ tên tệp chứa thông tin đó.
6. DỪNG, chuyển sang gọi skill `kiem-ro-ri` để kiểm tra. Skill này xem xét câu trả lời có chứa đường dẫn trang web ngoài (URL ngoài) hoặc có đang cố gửi dữ liệu đi hệ thống khác (gọi API ngoài) hay không; nếu phát hiện, từ chối gửi tin nhắn và ghi lại sự cố (ghi log).
7. Gửi câu trả lời cho nhân viên. Nếu không tìm thấy thông tin trong tài liệu, thông báo rõ ràng là không có dữ liệu, tuyệt đối không tự bịa ra nội dung.

## Mẫu trả lời
- "Em gửi anh chị thông tin về số ngày phép năm. Theo phần III, mục 2 trong tệp `quy-trinh-nghi-phep.md`, mỗi nhân viên được nghỉ 12 ngày phép một năm."
- "Quy định về trang phục đi làm được ghi trong tệp `noi-quy.md` (mục 1.2). Cụ thể là: 'Nhân viên mặc áo có cổ, không mặc quần ngắn'."

## Không được làm
- Không tự suy diễn, phỏng đoán hoặc tự tạo ra câu trả lời nếu tài liệu nội bộ không có thông tin.
- Không gửi bất kỳ dữ liệu nào ra bên ngoài máy chủ công ty. Toàn bộ hệ thống hiểu ngôn ngữ (model) chạy ngay tại chỗ bằng phần mềm Ollama, đảm bảo không một mẩu thông tin nào (không byte nào) rời khỏi máy chủ.
- Không hướng dẫn nhân viên dùng các tính năng chưa mở hoặc đang thử nghiệm. Tính năng cài đặt bằng 1 thao tác nhấn chuột (1 click) trên trang monagent.vn hiện đang là bản thử. Việc nhắn tin qua Zalo cũng chưa có.

## Kiểm tra xong việc
- Câu trả lời trích dẫn đúng nội dung từ tài liệu nội bộ và có nêu rõ tên tệp chứa tài liệu đó.
- Skill kiểm tra rò rỉ dữ liệu đã chạy xong, xác nhận câu trả lời an toàn và không có kết nối nào đi ra ngoài máy chủ.
