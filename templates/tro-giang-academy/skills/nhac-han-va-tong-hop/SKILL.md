---
name: nhac-han-va-tong-hop
description: Nhắc hạn nộp bài trước 24 giờ, mỗi tuần gửi giảng viên 5 câu hỏi học viên hỏi nhiều nhất.
---
# Nhắc hạn nộp bài và tổng hợp câu hỏi cho giảng viên

## Khi nào dùng
* Học viên quên lịch nộp bài tập hoặc đồ án cuối môn. Ví dụ: Học viên nhắn "Chừng nào hết hạn nộp bài tập lớn vậy tụi em?".
* Giảng viên cần biết học viên đang yếu phần nào để chuẩn bị cho buổi học tiếp theo. Ví dụ: Giảng viên nhắn "Tuần này lớp hay hỏi về vấn đề gì nhất?".

## Làm theo thứ tự
1. Đọc tệp lịch học tại `sample-data/lich-hoc.csv` để tìm các bài tập hoặc cột mốc có hạn chót trong vòng 24 giờ tới.
2. Gọi MCP của trung tâm tại địa chỉ `https://mcp-elearing.mona.academy/mcp` (nhớ chạy `tools/list` để lấy đúng tên công cụ trước khi dùng) nhằm kiểm tra danh sách học viên chưa nộp bài.
3. Gửi tin nhắn thông báo vào kênh Telegram của nhóm lớp để nhắc mọi người hoàn thành bài tập.
4. Lọc lại bộ nhớ (memory) của OpenClaw trong 7 ngày qua để chọn ra đúng 5 câu hỏi được nhiều học viên thắc mắc nhất.
5. Gọi công cụ `mail_send` thông qua API của MONA Mail (https://api.monamail.vn/v1) để chuẩn bị một bản nháp email chứa 5 câu hỏi này.
6. DỪNG, hỏi người phụ trách là giảng viên xem bản nháp email đã hợp lý chưa trước khi gửi chính thức.
7. Nhận phản hồi đồng ý từ giảng viên rồi mới tiến hành gửi email và ghi lại kết quả vào bộ nhớ.

## Mẫu trả lời
* Mẫu nhắc nhở học viên: "Chào anh chị, tụi em nhắc nhẹ là bài tập phần Thực hành giao diện sẽ hết hạn nộp vào 23:59 tối nay nha. Anh chị tranh thủ hoàn thiện sớm để tụi em chấm điểm nhé."
* Mẫu báo cáo giảng viên: "Chào anh chị giảng viên, tuần này tụi em ghi nhận lớp hỏi nhiều nhất về phần kết nối cơ sở dữ liệu. Tụi em đã soạn danh sách 5 câu hỏi chi tiết, anh chị xem qua bản nháp này rồi báo lại để tụi em gửi email chính thức nhé."

## Không được làm
* Không tự ý dời hạn nộp bài của học viên khi chưa có sự đồng ý rõ ràng từ giảng viên.
* Không hướng dẫn thiết lập hệ thống qua Zalo vì cầu nối Zalo hiện chưa có.
* Không nhắc đến model trí tuệ nhân tạo của MONA vì MONA AI chưa mở. Anh chị phải hướng dẫn người dùng nhập mã khoá của riêng họ hoặc dùng Ollama chạy tại chỗ.
* Không quảng cáo tính năng cài đặt bằng 1 click đang chạy trơn tru vì nút "Dùng ngay" trên trang web hiện chỉ là bản thử nghiệm.

## Kiểm tra xong việc
* Tin nhắn nhắc lịch đã hiển thị thành công trên nhóm Telegram của lớp trước thời hạn nộp bài 24 giờ.
* Giảng viên đã nhận được email tổng hợp 5 câu hỏi phổ biến thông qua hệ thống MONA Mail sau khi đã duyệt bản nháp.
