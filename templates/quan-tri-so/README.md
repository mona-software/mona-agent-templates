# Trợ lý quản trị bằng số: Hỏi công ty mình một câu khó, nhận câu trả lời kèm số thật từ dữ liệu bán hàng
Anh chị đang đi ngoài đường, đối tác gọi hỏi "Tháng trước bên anh bán được bao nhiêu mặt hàng A?". Thay vì phải gọi kế toán, mở máy tính, tìm báo cáo, xuất file Excel rồi cộng trừ mỏi mắt, anh chị chỉ cần mở điện thoại. Nhắn một tin vào Telegram cá nhân, vài giây sau, anh chị có ngay con số chính xác kèm theo cách tính toán. Trợ lý này kết nối trực tiếp vào phần mềm bán hàng của anh chị, đọc dữ liệu và trả lời câu hỏi bằng tiếng Việt như một người nhân viên mẫn cán.

## Agent này làm gì mỗi ngày
* Trả lời câu hỏi bất chợt bằng số: Anh chị hỏi "Hôm qua thu được bao nhiêu tiền mặt?", trợ lý tự động chuyển câu hỏi thành mã máy tính, đọc dữ liệu bán hàng (chỉ đọc, không bao giờ tự ý sửa hoặc xóa) và trả lời "Hôm qua thu được 25.000.000đ từ 5 đơn hàng, anh chị xem chi tiết bên dưới nhé".
* Gửi báo cáo sáng tự động: Đúng 7h30 mỗi sáng, trợ lý sẽ nhắn tin báo cáo 5 con số quan trọng nhất mà anh chị muốn biết. Ví dụ: Doanh thu hôm qua, số đơn hàng mới, số lượng khách hàng mới, những mặt hàng sắp hết trong kho, và tổng tiền khách còn nợ.
* Giải thích cách tính toán: Không chỉ đưa ra con số, trợ lý luôn giải thích rõ ràng số đó được lấy từ đâu. Ví dụ: "Con số 25.000.000đ này em tính tổng các đơn hàng có trạng thái 'đã thanh toán' trong ngày 18/09".

## Ai nên dùng, ai đừng dùng
* Ai nên dùng: Chủ doanh nghiệp, người quản lý đã có phần mềm bán hàng, phần mềm quản lý khách hàng (CRM) lưu dữ liệu trên hệ thống có cấu trúc (như Postgres hoặc MySQL). Anh chị muốn có số liệu nhanh chóng mọi lúc mọi nơi để ra quyết định mà không cần phụ thuộc vào người khác.
* Ai đừng dùng: Anh chị đang quản lý bán hàng hoàn toàn bằng sổ tay hoặc các file Excel rời rạc trên máy tính cá nhân. Trợ lý cần một nguồn dữ liệu tập trung để đọc và hiểu.

## Cần chuẩn bị gì trước
Để dựng trợ lý này, anh chị cần chuẩn bị ba thứ. Quá trình này thường mất khoảng 10 phút.
* Dữ liệu bán hàng: Thông tin kết nối vào nơi lưu trữ dữ liệu bán hàng của anh chị (tên máy chủ, tên đăng nhập, mật khẩu). Để thử nghiệm, tụi em có sẵn file dữ liệu mẫu trong thư mục `sample-data`.
* Một tài khoản Telegram riêng của anh chị để nhắn tin với trợ lý (tụi em gọi là bot token).
* Chìa khóa trí tuệ nhân tạo (API key) của các hãng như OpenAI, hoặc tải mô hình trí tuệ nhân tạo miễn phí Ollama về máy tính để chạy tại chỗ.

## Dựng thử trong 5 phút
Anh chị không cần biết lập trình, chỉ cần có Claude Code (hoặc Codex, Gemini) trên máy tính. Trí tuệ nhân tạo sẽ làm phần việc kỹ thuật, anh chị chỉ cần trả lời các câu hỏi.
1. Tải thư mục chứa trợ lý này về máy tính (clone).
2. Mở cửa sổ dòng lệnh ở thư mục đó và gõ lệnh gọi Claude Code.
3. Nhắn cho Claude Code: "Đọc file AGENTS.md và làm theo hướng dẫn trong đó để cài đặt".
4. Claude Code sẽ tự động tải các phần mềm cần thiết như OpenClaw, tạo kết nối Telegram và hỏi anh chị các thông tin đã chuẩn bị ở trên.
5. Sau khi Claude Code báo xong, trợ lý đã chạy ngay trên máy tính của anh chị.
6. Mở Telegram, nhắn một câu thử như "Tổng doanh thu tháng trước là bao nhiêu?" để xem trợ lý trả lời.

## Đưa lên chạy thật trên MONA Cloud
Khi đã thử ưng ý, anh chị có thể đưa trợ lý lên chạy liên tục trên máy chủ ảo của MONA Cloud. Giá thuê máy chủ tính theo giờ, bắt đầu từ 550đ/giờ (trả bằng tiền Việt Nam, có xuất hóa đơn VAT 10%). Anh chị tạo máy chỉ mất khoảng 11 giây, nạp tiền vào ví bằng cách quét mã VietQR. Tắt máy chủ là ngừng tính tiền, và quan trọng nhất là dữ liệu hoàn toàn nằm trên máy của anh chị. Tính năng bấm một nút "Dùng ngay" đưa thẳng lên mạng đang là bản thử nghiệm, tụi em sẽ mở tính năng này trong thời gian tới.

## Giới hạn tụi em nói trước
Tụi em luôn nói rõ những điểm chưa làm được để anh chị cân nhắc. Hiện tại nút bấm 1 nút để chạy thẳng lên mạng vẫn đang là bản thử nghiệm nên có thể chưa hoạt động trơn tru. Tụi em cũng chưa làm xong cầu nối với Zalo, nên hiện tại anh chị cần dùng Telegram để nhắn tin. Hệ thống trí tuệ nhân tạo nội bộ MONA AI chưa mở, do đó anh chị cần dùng chìa khóa (API key) của chính anh chị hoặc mô hình Ollama. Cuối cùng, trợ lý này chỉ có quyền đọc dữ liệu, nó không tự quyết định việc gì liên quan đến thay đổi dữ liệu hay tiêu tiền của anh chị.

## Anh chị đang là khách MONA?
Nếu anh chị đang dùng phần mềm hoặc trang web do MONA làm (thành lập từ 2016, với hơn 14.000 dự án và 85% khách hàng quay lại), mọi việc còn dễ hơn nữa. Tụi em có gói Doanh nghiệp, bộ phận kỹ thuật sẽ gắn thẳng trợ lý này vào hệ thống anh chị đang dùng. Anh chị hãy gọi tổng đài 1900 636 648 để tụi em báo giá và triển khai.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/themonagroup/mona-agent-templates
