# CSKH Zalo / Telegram: Trợ lý AI trực tin nhắn ngày đêm và giải đáp thắc mắc cho khách mua hàng
Nửa đêm khách nhắn tin hỏi giá, sáng sớm khách hối giao hàng, đang bận làm dịch vụ thì khách lại hỏi giờ đóng cửa. Chắc chắn anh chị từng rơi vào cảnh cầm điện thoại lên là thấy mấy chục tin nhắn chưa đọc, trả lời trễ thì khách đi mất, mà thuê người trực đêm thì chi phí quá cao. Trợ lý AI này sinh ra để thay anh chị xử lý gọn gàng khâu đó. Tụi em nạp sẵn kịch bản để AI tự đọc tài liệu của riêng shop anh chị, tự động nhắn tin lại cho khách ngay lập tức, còn ca nào khó quá thì nó sẽ gọi người thật vào tiếp quản.

## Trợ lý AI làm những việc cụ thể này mỗi ngày
* Lấy thông tin từ tài liệu để trả lời khách: Kỹ năng này gọi là tra-loi-tu-tai-lieu. Trợ lý chỉ đọc đúng thông tin từ bảng giá, giờ mở cửa, chính sách của anh chị để báo cho khách, tuyệt đối không tự bịa thông tin. Ví dụ khách nhắn "Shop có đổi trả không", AI nhắn lại: "Tiệm em cho phép đổi hàng trong 7 ngày nếu còn nguyên tem mác. Chị cần đổi mẫu nào gửi hình em xem thử nha." Nếu tài liệu thiếu thông tin, nó sẽ hỏi lại khách hoặc báo cho anh chị.
* Bàn giao ca khó cho người thật: Kỹ năng này gọi là chuyen-ca-kho. Khi khách khiếu nại gay gắt, hỏi mua giá sỉ, hay đòi đổi hàng quá thời gian quy định, AI sẽ nhận ra ngay đây là tình huống khó. Nó tự động nhắn "Vấn đề này cần quản lý xem xét, em đã ghi nhận lại, xíu nữa quản lý sẽ nhắn tin trực tiếp cho chị nha". Sau đó nó gửi tóm tắt tình hình qua email cho anh chị bằng dịch vụ hộp thư MONA Mail để anh chị nhảy vào xử lý tiếp.
* Làm việc không biết mệt: Hệ thống túc trực 24/7, khách nhắn lúc 3 giờ sáng hay mùng 1 Tết đều được phản hồi sau vài giây, giữ chân người mua nhanh chóng và hiệu quả.

## Ai nên dùng và ai chưa nên dùng mẫu này
* Nhóm nên dùng: Chủ shop bán lẻ, cơ sở làm đẹp spa, phòng khám nha khoa, trung tâm ngoại ngữ thường xuyên có khách nhắn tin hỏi những câu lặp đi lặp lại. Nếu anh chị đang mệt mỏi vì ngày nào cũng sao chép dán cùng một câu trả lời bảng giá, đây là mẫu dành cho anh chị.
* Nhóm đừng dùng: Những ngành kinh doanh cần tư vấn cảm xúc phức tạp, đòi hỏi đồng cảm sâu sắc như tư vấn tâm lý, hoặc các sản phẩm có giá trị quá lớn cần người thật gặp mặt thương lượng trực tiếp.

## Cần chuẩn bị những thứ này trước khi bắt đầu
* Tài liệu của shop: Anh chị gom lại bảng giá, chính sách đổi trả, giờ mở cửa, và các câu hỏi khách hay hỏi, lưu vào một tệp chữ có tên là `sample-data/tai-lieu-shop.md`.
* Mã kết nối Telegram: Một đoạn mã (thường gọi là token bot) để nối AI với ứng dụng Telegram. Việc lấy mã này diễn ra trong 2 phút trên ứng dụng Telegram.
* Chìa khoá AI: Mã kết nối của các hãng trí tuệ nhân tạo hoặc dùng bản cài đặt tại chỗ Ollama nếu anh chị có sẵn máy tính đủ mạnh ở nhà.
* Thời gian: Khoảng 10 phút ngồi máy tính.

## Dựng thử lên máy tính của anh chị trong 5 phút
Anh chị không cần rành kỹ thuật, chỉ cần làm theo 6 bước ngắn sau đây. Trí tuệ nhân tạo sẽ làm phần cài đặt khó, anh chị chỉ việc trả lời các câu hỏi của nó:
1. Tải mẫu về máy: Anh chị tải thư mục chứa mẫu trợ lý này về máy tính (thao tác này gọi là clone).
2. Mở công cụ lập trình trí tuệ nhân tạo: Bật công cụ Claude Code, Codex hoặc Gemini ngay trong thư mục vừa tải.
3. Để trí tuệ nhân tạo tự đọc việc cần làm: Gõ lệnh yêu cầu hệ thống đọc tệp `AGENTS.md`. Tệp này chứa toàn bộ cách làm việc và chỉ dẫn cài đặt mà tụi em đã viết sẵn.
4. Trả lời câu hỏi cài đặt: Công cụ sẽ hỏi anh chị vài thông tin cơ bản để thiết lập. Anh chị cứ gõ chữ trả lời bình thường.
5. Chạy thử trên máy tính cục bộ: Khi cài xong, công cụ gọi phần mềm lõi có tên OpenClaw khởi động ngay trên máy tính của anh chị. Lúc này hệ thống đã bắt đầu chạy cục bộ (local).
6. Kiểm tra bằng danh sách mẫu: Anh chị mở Telegram nhắn tin thử vài câu khó có ghi trong tệp kiểm tra (CHECKLIST) xem nó trả lời đúng ý không. Khi có người nhắn tin lần đầu tiên, anh chị gõ lệnh `openclaw pairing approve telegram <MÃ>` để duyệt cho phép trợ lý nói chuyện.

## Đưa lên chạy thật trên nền tảng đám mây MONA Cloud
Khi chạy thử trên máy tính ưng ý, anh chị đưa trợ lý lên máy chủ đám mây (VPS) của MONA Cloud để nó hoạt động liên tục kể cả khi anh chị tắt máy tính ở nhà. Phí thuê máy chủ theo giờ cực rẻ chỉ từ 550 đồng cho mỗi giờ, thanh toán hoàn toàn bằng tiền Việt Nam (VND) và có xuất hoá đơn VAT đàng hoàng. Anh chị tắt máy chủ lúc nào là hệ thống ngừng tính tiền lúc đó, toàn bộ dữ liệu nằm trên máy chủ tại Việt Nam, AI gọi thẳng, có người của MONA đứng sau hỗ trợ. Nút "Dùng ngay" để đưa hệ thống lên đám mây bằng một thao tác nhấp chuột đang là bản thử nghiệm và sẽ sớm mở chính thức.

## Những giới hạn tụi em muốn nói rõ từ đầu
* Cầu nối Zalo chưa hoàn tất: Nền tảng lõi OpenClaw hiện có sẵn kênh Telegram để chạy ngay, nhưng cầu nối trực tiếp với Zalo OA thì tụi em đang xây dựng. Tạm thời người trực Zalo của anh chị có thể dùng phiên bản trên Telegram hoặc trang web.
* Chưa có tính năng nhấp chuột một cái là chạy: Nút bấm triển khai nhanh lên đám mây đang trong giai đoạn thử nghiệm, anh chị cần dùng câu lệnh để đưa hệ thống lên.
* Cần tự chuẩn bị chìa khoá AI: Do hệ thống trí tuệ nhân tạo MONA AI chưa mở, anh chị cần dùng mã kết nối mô hình của chính anh chị hoặc chạy bằng nền tảng Ollama.
* Trợ lý không tự quyết chuyện tiền bạc: Trợ lý này không tự ý chốt các khoản đền bù tiền hay giảm giá ngoài quy định đã ghi sẵn.

## Anh chị đang là khách hàng của MONA?
Nếu anh chị đang sử dụng hệ thống phần mềm hoặc website do tụi em xây dựng, MONA có gói Doanh nghiệp gắn thẳng trợ lý này vào quy trình hiện tại. Tụi em triển khai trực tiếp trên hạ tầng mà khách hàng đang thuê. Công ty The MONA Group hoạt động từ năm 2016, đã thực hiện hơn 14.000 dự án với 85% khách hàng quay lại. Anh chị gọi tổng đài 1900 636 648 để tụi em tư vấn chi tiết.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/mona-software/mona-agent-templates
