# Mua domain cho khách: Trợ lý AI lo trọn gói tên miền cho anh chị làm dịch vụ web

Anh chị đang ôm hàng chục khách hàng làm web, mỗi người lại có dăm ba cái tên miền khác nhau. Chắc hẳn không ít lần anh chị giật mình vào sáng sớm vì trang web của khách chết queo do lỡ quên ngày gia hạn, hay mất cả buổi chỉ để tra cứu một cái tên miền phù hợp rồi báo giá thủ công. Việc dò tìm tên miền khả dụng, tính toán giá cả, giữ chỗ rồi canh ngày hết hạn từng người một bằng tay tốn quá nhiều thời gian và rất dễ sai sót. Trợ lý AI này sinh ra để gánh hết phần việc lắt nhắt đó thay anh chị. Thay vì chìm trong những bảng tính Excel dày đặc ngày tháng, anh chị chỉ cần nhắn vài dòng trên điện thoại, AI sẽ tự tra cứu, giữ chỗ tên miền mới và chủ động nhắc nhở khi có tên miền sắp hết hạn.

## Agent này làm gì mỗi ngày

* Tra cứu và giữ chỗ tên miền tự động: Khi anh chị nhắn yêu cầu tìm tên cho khách, AI sẽ dùng kỹ năng tra cứu để tìm ngay 5 biến thể phù hợp nhất. Nó tự lấy giá tiền Việt (VND) trực tiếp từ hệ thống MONA Domain và giữ chỗ trước (reserve) để khách thoải mái cân nhắc. Ví dụ anh chị nhắn trên Telegram: "Tìm cho khách anh tên miền bán giày thể thao". AI sẽ trả lời: "Tụi em thấy giaythethao.vn còn trống giá 756.000đ, giaythethao.com giá 432.000đ, anh chị xem khách ưng cái nào. Khách gật đầu là em mua luôn, riêng bản khai .vn khách chỉ cần xác thực khuôn mặt eKYC một lần duy nhất".
* Mua và trỏ tên miền (DNS) thay anh chị: Ngay khi khách đồng ý mua, trợ lý sẽ gọi công cụ để mua thật và tự động cấu hình trỏ tên miền về máy chủ web. Mọi thao tác đều thực hiện ngay trên khung chat Telegram hoặc gọi trực tiếp qua Claude Code mà anh chị không cần phải tự đăng nhập vào hệ thống quản lý nào cả.
* Canh chừng ngày gia hạn để nhắc nhở: Mỗi sáng thức dậy, trợ lý sẽ rà soát kỹ lưỡng danh sách tên miền của tất cả khách hàng. Nếu phát hiện tên miền nào chỉ còn đúng 30 ngày, 7 ngày hoặc 1 ngày là hết hạn, nó sẽ nhắn tin báo ngay cho anh chị biết. Ví dụ: "Tên miền banhang.com của chị Lan sắp hết hạn trong 7 ngày tới, anh chị có muốn em gia hạn luôn để không bị rớt mạng không?".
* Kiểm soát chi tiêu chặt chẽ: Dù trợ lý rất lanh lợi, tụi em đã thiết lập quy tắc cứng để nó không bao giờ tự ý xài tiền của anh chị. Mọi thao tác liên quan đến trừ tiền, mua mới hay gia hạn đều phải chờ anh chị xác nhận một câu "Đồng ý" thì nó mới làm tiếp.

## Ai nên dùng, ai đừng dùng

* Những ai nên dùng: Các công ty cung cấp dịch vụ thiết kế web (agency), hoặc những người làm web tự do (freelancer) đang nhận chăm sóc từ mười khách hàng trở lên. Khi lượng khách đông, việc ghi nhớ ngày đóng tiền gia hạn hay phải dò tìm mua tên miền mới liên tục sẽ làm anh chị kiệt sức, lúc này trợ lý AI sẽ là cánh tay phải đắc lực hỗ trợ anh chị quản lý chính xác.
* Những ai đừng dùng: Những anh chị chỉ quản lý một hoặc hai trang web cá nhân. Với số lượng quá ít, việc tự ghi chú lịch nhắc nhở vào điện thoại sẽ nhanh gọn hơn nhiều so với việc bỏ thời gian cài đặt và cấu hình trợ lý AI.

## Cần chuẩn bị gì trước

* Danh sách khách hàng và các tên miền hiện tại đang quản lý. Anh chị gom hết vào một tệp dữ liệu chung, tụi em đã để sẵn tệp mẫu tên là sample-data/khach-domain.csv để anh chị điền theo.
* Một đoạn mã kết nối của ứng dụng Telegram (token bot) để anh chị có thể nhắn tin điều khiển trợ lý qua điện thoại.
* Chìa khoá kết nối mô hình trí tuệ nhân tạo (key model). Anh chị có thể dùng chìa khoá của bên thứ ba, hoặc dùng mô hình cài đặt ngay trên máy tính của anh chị (Ollama).
* Khoảng 10 phút ngồi bên máy tính để làm theo vài bước cài đặt cơ bản.

## Dựng thử trong 5 phút

* Bước 1: Lấy toàn bộ thư mục mẫu (clone) về máy tính cá nhân của anh chị.
* Bước 2: Mở thư mục này bằng phần mềm Claude Code (hoặc Codex, Gemini). Ở bước này AI sẽ lo liệu hết phần kỹ thuật, anh chị không cần tự gõ bất kỳ lệnh phức tạp nào.
* Bước 3: Nhắn tin bảo AI đọc tệp AGENTS.md. Nó sẽ tự hiểu cách cài đặt và chạy môi trường OpenClaw.
* Bước 4: Trả lời những câu hỏi mà AI hiện lên màn hình. Nó hỏi xin chìa khoá kết nối mô hình hoặc token Telegram thì anh chị cứ chép rồi dán vào cho nó.
* Bước 5: AI tự động chạy trợ lý ngay trên máy tính (local) của anh chị. Anh chị mở điện thoại lên, nhắn một tin nhắn cho bot Telegram rồi nhập mã xác thực (pairing approve) để duyệt kết nối lần đầu.
* Bước 6: Gõ thử một câu trong danh sách kiểm tra (CHECKLIST), ví dụ "Sáng nay có tên miền nào của khách sắp hết hạn không" để xem trợ lý phản hồi ngay trên điện thoại.

## Đưa lên chạy thật trên MONA Cloud

Sau khi chạy thử trên máy tính thấy ưng ý, anh chị có thể đưa trợ lý này lên máy chủ (VPS) MONA Cloud để nó túc trực ngày đêm. Tiền thuê máy chủ tính theo giờ rất rẻ, chỉ từ 550đ/giờ (bao gồm 1 core CPU, 1 GB RAM và 10 GB ổ cứng). Anh chị thanh toán hoàn toàn bằng tiền Việt (VND), công ty có xuất hoá đơn VAT đầy đủ, lúc nào không dùng nữa cứ tắt máy là hệ thống ngừng tính tiền. Quan trọng nhất là toàn bộ dữ liệu danh sách khách hàng nằm an toàn trên máy chủ đặt tại Việt Nam do chính anh chị làm chủ. Tính năng bấm nút dùng ngay (1 click) đưa trợ lý lên mây hiện đang là bản thử nghiệm và tụi em sẽ sớm mở chính thức cho anh chị dùng.

## Giới hạn tụi em nói trước

Hệ thống nền tảng OpenClaw hiện tại mới chỉ chạy qua kênh Telegram. Tụi em đang xây dựng cầu nối sang nền tảng Zalo OA nhưng hiện tại chưa xong nên anh chị chưa thể nhắn tin qua Zalo được. Hệ thống MONA AI chưa chính thức mở cửa nên bắt buộc anh chị phải có chìa khoá mô hình (key model) của riêng mình, hoặc dùng máy tính cá nhân chạy mô hình nội bộ Ollama. Một điều nữa, như tụi em nói ở trên, trợ lý này tuyệt đối không tự quyết định các việc tốn tiền để đảm bảo an toàn cho túi tiền của anh chị.

## Anh chị đang là khách MONA?

Trường hợp anh chị đang dùng các phần mềm hoặc làm web do chính MONA thiết kế, tụi em có gói Doanh nghiệp hỗ trợ gắn thẳng trợ lý AI này vào hệ thống hiện tại. Việc đồng bộ dữ liệu sẽ diễn ra trực tiếp mà anh chị không cần xuất tệp thủ công. The MONA Group thành lập từ năm 2016, đã làm hơn 14.000 dự án với 85% khách hàng quay lại, luôn có đội ngũ MONA thật đứng sau hỗ trợ. Anh chị cứ gọi số tổng đài 1900 636 648 để tụi em tư vấn cách gắn vào phần mềm nhé.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/themonagroup/mona-agent-templates
