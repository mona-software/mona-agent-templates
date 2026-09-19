---
name: bao-gia
description: Hỏi đúng 3 câu để chốt cấu hình rồi lập báo giá theo bảng giá, không giảm giá ngoài quy định.
---
# Lập báo giá theo đúng nhu cầu

## Khi nào dùng
- Khách nhắn tin hỏi giá chung chung mà chưa rõ họ cần mua gói nào. Ví dụ: "Anh muốn mua gói tháng, giá sao em?"
- Khách muốn thêm bớt các tính năng so với gói có sẵn. Ví dụ: "Chị lấy gói cơ bản nhưng muốn thêm phần gửi email thì tính tiền sao?"
- Khách đã chốt xong các món cần mua và chờ anh chị gửi tổng tiền để chuyển khoản.

## Làm theo thứ tự
1. Chào khách, xin lỗi vì để khách đợi (nếu có) và hỏi đúng 1 câu đầu tiên về nhu cầu cốt lõi. Tụi em ví dụ như hỏi họ dùng cho bao nhiêu người hoặc bán mặt hàng gì.
2. Dựa vào câu trả lời, hỏi tiếp câu thứ 2 về ngân sách dự kiến hoặc thời gian muốn dùng, giống như hỏi khách muốn thuê nhà theo tháng hay mua đứt luôn.
3. Hỏi câu cuối cùng về các tính năng nâng cao nếu khách có vẻ cần.
4. Mở file `sample-data/bang-gia.csv` và `sample-data/mau-bao-gia.md` để đối chiếu thông tin khách vừa cung cấp.
5. Soạn báo giá chi tiết, ghi rõ từng khoản tiền theo bảng giá. DỪNG, hỏi người phụ trách duyệt nháp này trước khi gửi khách.
6. Sau khi người phụ trách đồng ý, gửi báo giá cho khách.
7. Nếu khách chốt mua, chuyển sang bước tạo mã VietQR thanh toán bằng lệnh gọi `POST /api/v1/acb/qr-payment/generate` của MONA Pay.
8. Chờ hệ thống báo có tiền, sau đó báo cáo cho người phụ trách qua Telegram.

## Mẫu trả lời
- "Chào anh chị. Để tụi em tính giá chính xác nhất, anh chị cho em hỏi mình định dùng cho đội nhóm bao nhiêu người và cần lưu trữ nhiều tài liệu không?"
- "Em gửi anh chị bảng tính chi tiết các mục mình đã chọn. Tổng cộng là 3.990.000đ. Anh chị xem qua, nếu đồng ý thì em tạo mã QR để mình thanh toán."

## Không được làm
- Tự ý giảm giá hoặc tặng thêm tháng sử dụng khi không có trong bảng giá.
- Hỏi dồn dập nhiều câu một lúc khiến người đọc khó chịu.
- Hứa hẹn các chức năng chưa hoàn thiện. Phải nói rõ tính năng bấm "Dùng ngay" 1 click hiện đang là bản thử, tính năng gửi tin qua Zalo chưa có, và hiện tại phải dùng khóa model của chính anh chị hoặc mô hình Ollama chạy tại máy.

## Kiểm tra xong việc
- Khách đã nhận được báo giá chi tiết, hiểu rõ từng khoản phí.
- Tổng tiền báo cho khách khớp hoàn toàn với quy định trong dữ liệu đầu vào.
- Chuyển tiếp thành công sang bước tạo mã VietQR đúng số tiền nếu khách đồng ý chốt đơn.
