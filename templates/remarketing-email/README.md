# Email theo sự kiện: Trợ lý AI tự động chọn và gửi thư cá nhân hoá đúng thời điểm khách hàng cần

Anh chị kinh doanh thường gặp cảnh khách hàng bỏ đồ vào giỏ rồi im lặng rời đi, hoặc những người từng mua nhưng sáu tháng nay không thấy quay lại. Ví dụ, anh chị bán quần áo, khách chọn ba chiếc áo bỏ vào giỏ nhưng quên thanh toán. Nếu tự làm thủ công, anh chị phải mở phần mềm xem danh sách, lọc ra khách bỏ giỏ, rồi copy dán từng mẫu thư để gửi nhắc họ rất mất thời gian. Trợ lý AI này sẽ thay mặt anh chị ngồi trực hệ thống ngày đêm. Hễ thấy có khách bỏ giỏ hàng hay ngừng tương tác, trợ lý tự động chọn đúng mẫu email và viết thêm vài câu hỏi thăm riêng biệt để gửi ngay qua hệ thống MONA Mail, giúp việc chăm sóc lại khách cũ trở nên nhẹ nhàng mà không cần anh chị phải nhớ nhớ quên quên.

## Agent này thay anh chị làm việc tự động mỗi ngày

* Nhận sự kiện từ phần mềm bán hàng: Khi hệ thống của anh chị gửi tín hiệu (webhook) báo có khách bỏ quên giỏ hàng hoặc đã lâu không mua sắm, trợ lý sẽ ghi nhận sự việc ngay lập tức.
* Chọn và cá nhân hoá thư: Trợ lý tự động mở kho mẫu thư để chọn đúng mẫu cần gửi (như mẫu nhắc giỏ hàng, mẫu tặng mã giảm giá sinh nhật) và viết thêm 2 đến 3 câu hỏi thăm dựa vào thông tin thực tế của người đó. 
* Ví dụ nội dung thư trợ lý tự viết: "Chào chị Hương, em thấy chị vừa chọn bộ đồ tập gym màu xanh nhưng chưa thanh toán, bên em đang có mã miễn phí vận chuyển cho đồ tập, chị dùng ngay nhé".
* Kiểm soát tần suất gửi thư: Trợ lý nhớ rõ đã gửi thư cho ai vào lúc nào, tự động kiểm tra lịch sử để đảm bảo không gửi trùng lặp hoặc quấy rầy khách quá một lần trong vòng 7 ngày.
* Theo dõi trạng thái và dừng gửi đúng lúc: Trợ lý biết đọc báo cáo từ MONA Mail để xem thư nào bị từ chối nhận (bounce) hoặc khi khách hàng bấm nút huỷ đăng ký (unsubscribe). Ngay sau đó, trợ lý tự đưa những người này vào danh sách dừng gửi để bảo vệ uy tín hòm thư của anh chị.
* Báo cáo công việc hàng tuần: Mỗi cuối tuần, trợ lý sẽ tổng hợp số liệu và nhắn tin qua Telegram cho anh chị. Ví dụ tin nhắn: "Tuần này em đã gửi 150 email nhắc giỏ hàng, có 45 người mở đọc và 12 người quay lại chốt đơn thành công, có 2 người được đưa vào danh sách ngừng gửi".

## Ai nên dùng và ai đừng dùng trợ lý này

Những ai nên dùng: Các chủ cửa hàng bán trực tuyến, công ty dịch vụ hoặc trung tâm đào tạo có sẵn danh sách email khách hàng và phần mềm bán hàng có khả năng xuất dữ liệu sự kiện. Anh chị cần một người phụ việc chăm chỉ, biết tự viết thêm nội dung cá nhân hoá vào từng bức thư để gửi đi một cách tự nhiên.

Những ai đừng dùng: Những cửa hàng chưa bao giờ thu thập email khách hàng, hoặc tệp khách hàng chủ yếu chỉ nhắn tin mua đồ qua tài khoản Zalo cá nhân. Trợ lý này thiết kế chuyên để xử lý sự kiện và gửi thư điện tử, nên nếu anh chị chưa dùng email làm kênh giao tiếp thì hệ thống này không mang lại hiệu quả thực tế.

## Anh chị cần chuẩn bị vài thứ trước khi bắt đầu

* Dữ liệu mẫu ban đầu: Các sự kiện mẫu trích xuất từ phần mềm (anh chị lưu ở tệp `sample-data/su-kien.jsonl`) và các mẫu thư văn bản anh chị hay dùng (để ở thư mục `sample-data/mau-thu/`).
* Một tài khoản quản lý và mã token của Telegram bot để trợ lý dùng làm nơi gửi tin nhắn báo cáo hàng tuần cho anh chị.
* Mã kết nối (key) của một mô hình AI thông minh, hoặc anh chị có thể cài sẵn phần mềm Ollama nếu muốn chạy mô hình nội bộ ngay trên máy tính của mình.
* Khoảng 10 phút ngồi trả lời vài câu hỏi để hệ thống AI hiểu phong cách viết thư của cửa hàng anh chị.

## Dựng thử trợ lý trong 5 phút bằng vài bước đơn giản

1. Tải toàn bộ thư mục chứa mã nguồn của trợ lý này về máy tính cá nhân của anh chị.
2. Mở một phần mềm AI hỗ trợ lập trình như Claude Code (hoặc Codex, Gemini) và trỏ vào thư mục vừa tải.
3. Gõ lệnh yêu cầu AI đọc tệp `AGENTS.md` để hiểu cách làm việc. Phần mềm AI sẽ tự động xử lý toàn bộ các bước cài đặt kỹ thuật nặng nhọc, anh chị không phải thao tác tay.
4. Trả lời các câu hỏi mà AI hiện ra trên màn hình. Anh chị chỉ cần gõ chữ bình thường như đang nhắn tin, AI sẽ tự động điền cấu hình vào các tệp.
5. Chạy thử trợ lý trên máy tính bằng môi trường OpenClaw. Anh chị có thể cài môi trường này bằng lệnh `npm install -g openclaw@latest` rồi gõ lệnh cài đặt gốc `openclaw onboard --install-daemon`.
6. Gõ thử vài câu lệnh mẫu trong danh sách kiểm tra hệ thống (CHECKLIST) xem trợ lý chọn mẫu thư và gửi có đúng như mong muốn không.

## Đưa trợ lý lên chạy thật trên máy chủ đám mây MONA Cloud

Khi đã thử nghiệm ổn định, anh chị nên đưa trợ lý lên hoạt động trên máy chủ đám mây MONA Cloud để làm việc xuyên suốt ngày đêm. Máy chủ riêng (VPS) ở đây tính phí theo giờ rất rẻ chỉ từ 550 đồng cho mỗi giờ hoạt động, thanh toán hoàn toàn bằng tiền Việt Nam (VND) qua quét mã VietQR và có xuất hoá đơn VAT đầy đủ. Điểm tiện lợi là anh chị dùng bao nhiêu trả bấy nhiêu, khi tắt máy là ngừng tính tiền, và toàn bộ dữ liệu khách hàng luôn nằm trên máy chủ tại Việt Nam của riêng anh chị. Nút bấm "Dùng ngay" bằng một cú nhấp chuột trên trang web hiện đang là bản thử nghiệm, tụi em sẽ mở tính năng này trong thời gian tới.

## Giới hạn kỹ thuật tụi em phải nói trước cho anh chị rõ

Nút cài đặt nhanh một bước đang trong giai đoạn thử nghiệm nên báo trạng thái chưa dùng được, anh chị chịu khó tải mã nguồn về và để AI thiết lập theo các bước trên. Hệ thống OpenClaw hiện chưa có cầu nối sang ứng dụng Zalo, do đó anh chị chỉ có thể theo dõi báo cáo qua Telegram. Tụi em cũng chưa mở mạng lưới MONA AI, nên anh chị cần tự trang bị mã kết nối của các mô hình bên ngoài hoặc dùng Ollama cài tại chỗ để giữ kín dữ liệu. Trợ lý này cũng bị giới hạn quyền hạn, không được tự ý quyết định các thao tác liên quan tới chi tiêu tiền bạc của anh chị.

## Anh chị đang là khách hàng cũ của MONA cần biết thêm

Nếu anh chị đang sử dụng trang web hay phần mềm do tụi em thiết kế, gói Doanh nghiệp cho phép gắn thẳng trợ lý này vào hệ thống cũ để hoạt động luôn. Anh chị cứ gọi lên tổng đài 1900 636 648, ở đây luôn có đội ngũ nhân sự MONA thật trực máy để tụi em cấu hình giúp anh chị. Công ty thành lập từ năm 2016 và đã thực hiện hơn 14.000 dự án với 85% khách hàng quay lại, nên anh chị cứ an tâm giao phần hệ thống kỹ thuật cho tụi em xử lý.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/mona-software/mona-agent-templates
