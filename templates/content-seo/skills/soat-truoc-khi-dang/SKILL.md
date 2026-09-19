---
name: soat-truoc-khi-dang
description: Chạy gate: từ cấm, câu quá dài đều nhau, hứa lố, số không có nguồn; rớt thì tự sửa, đạt thì gửi người duyệt.
---
# Rà soát lỗi và xin phép trước khi đăng bài

## Khi nào dùng
* Tình huống bài viết nháp đã xong, cần kiểm tra xem có vi phạm quy định viết bài của công ty không. (Ví dụ: "Tụi em kiểm tra bài viết mới nhất xem có dính từ cấm không nhé.")
* Tình huống người phụ trách yêu cầu đánh giá chất lượng văn bản do máy tính viết ra trước khi đưa lên mạng. (Ví dụ: "Soát lại bài này, rớt lỗi nào tự sửa luôn rồi báo cho anh chị.")
* Tình huống cần gửi bản nháp cuối cùng qua tin nhắn Telegram cho anh chị duyệt trước khi đẩy bài lên trang web. (Ví dụ: "Kiểm tra bài xong thì gửi qua Telegram cho chị xem.")

## Làm theo thứ tự
1. Đọc nội dung bài nháp hiện tại và đối chiếu với danh sách từ cấm nằm trong tập tin `sample-data/tu-cam.md`.
2. Quét qua toàn bộ các câu trong bài, phát hiện những chỗ có nhiều câu dài bằng nhau liên tiếp giống như văn mẫu máy tính và cắt ngắn hoặc ghép lại cho tự nhiên.
3. Tìm các câu hứa hẹn quá mức hoặc các con số thống kê, nếu không có nguồn dẫn chứng rõ ràng thì xoá bỏ hoặc viết lại cho đúng sự thật.
4. Tự động sửa lại toàn bộ các lỗi vừa tìm thấy để tạo ra bản nháp mới sạch sẽ hơn.
5. Gửi bản nháp đã sửa qua kênh Telegram cho anh chị xem.
6. DỪNG, hỏi người phụ trách xem bản nháp này đã đạt yêu cầu để đăng lên WordPress hay chưa.
7. Nếu anh chị đồng ý, tụi em sẽ tiến hành đăng bài, còn nếu anh chị yêu cầu sửa thêm thì tụi em quay lại bước đầu tiên.

## Mẫu trả lời
* "Tụi em đã rà soát xong bài viết. Bài cũ vướng vài từ cấm và vài câu hơi dài, tụi em đã tự sửa lại và gửi bản nháp mới nhất ở dưới, anh chị xem qua nhé."
* "Bản nháp này đã sạch lỗi rồi. Anh chị đọc thử, nếu ưng ý thì nhắn lại để tụi em đăng bài luôn."

## Không được làm
* Không tự ý đăng bài lên WordPress khi chưa có lệnh đồng ý từ anh chị qua kênh Telegram.
* Không giữ lại các số liệu bịa đặt hoặc tự nghĩ ra nguồn dẫn chứng giả để qua mặt bước kiểm tra.
* Không xóa bỏ cấu trúc chuẩn của bài viết khi đang sửa các câu văn dài hoặc chứa từ vi phạm.
* Không bỏ qua bước kiểm tra danh sách từ cấm trong tập tin mẫu mà anh chị đã cung cấp.

## Kiểm tra xong việc
* Bài nháp cuối cùng không chứa bất kỳ từ nào nằm trong danh sách cấm.
* Các số liệu và cam kết trong bài đều có thật hoặc có nguồn rõ ràng.
* Người phụ trách đã nhận được bản nháp qua Telegram và đưa ra quyết định duyệt.
