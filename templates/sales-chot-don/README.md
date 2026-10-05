# Sales chốt đơn: Trợ lý AI báo giá và nhận tiền tự động cho người bán hàng qua chat

Nhiều đêm anh chị phải thức đến một hai giờ sáng chỉ để trả lời tin nhắn xin báo giá, canh điện thoại xem khách chuyển khoản chưa để lên đơn. Việc này lặp đi lặp lại khiến anh chị mệt mỏi, dễ tính sai tiền hoặc sót đơn của khách đang cần gấp. Trợ lý "Sales chốt đơn" sinh ra để thay anh chị gánh vác phần việc chân tay này. Chỉ cần đưa bảng giá, máy sẽ tự động hỏi thăm nhu cầu, tính tiền, gửi mã nhận đúng số tiền và báo ngay cho anh chị khi tiền đã vào tài khoản.

## Agent này làm gì mỗi ngày

*   Hỏi đúng trọng tâm để lọc khách: Khách hàng nhắn tin tới thường có nhu cầu mơ hồ, agent sẽ đóng vai trò người bán hàng, chủ động hỏi khách tối đa 3 câu để chốt cấu hình sản phẩm theo đúng quy trình anh chị đặt ra. Bằng kỹ năng hỏi đáp gọi là báo giá, hệ thống lọc được khách thực sự muốn mua.
    Ví dụ: "Anh chị cần mua gói tập mấy tháng, có cần huấn luyện viên cá nhân theo sát để lên thực đơn ăn kiêng không?"
*   Báo giá chuẩn xác theo dữ liệu của cửa hàng: Sau khi thu thập đủ thông tin, hệ thống sẽ đọc bảng giá do anh chị cung cấp và tự động tính toán số tiền cuối cùng. Máy tuân thủ nghiêm ngặt mức giá này, không tự ý đưa ra chương trình giảm giá hay hứa hẹn ngoài quy định của cửa hàng.
    Ví dụ: "Tổng chi phí cho 3 tháng tập kèm huấn luyện viên là 4.500.000đ, anh chị thanh toán chuyển khoản luôn hôm nay để giữ chỗ nhé?"
*   Tạo mã thanh toán cá nhân hoá: Khi khách đồng ý mua, trợ lý gọi API ngân hàng và dịch vụ xác nhận thanh toán tự động MONA Pay để tạo một mã VietQR động thông minh. Mã này chứa sẵn số tài khoản của anh chị, đúng số tiền lẻ đến từng đồng và kèm theo mã đơn hàng tự động.
    Ví dụ: Gửi một hình ảnh QR ra màn hình chat, khách chỉ cần mở ứng dụng ngân hàng quét là xong, không phải gõ tay bất kỳ thông tin nào, tránh việc chuyển nhầm tiền.
*   Xác nhận tiền về và gửi thư báo chủ: Hệ thống âm thầm chờ thông báo giao dịch thành công từ MONA Pay. Tiền vào tài khoản là lập tức báo lại cho khách, đồng thời gửi tin nhắn thông báo cho anh chị biết đơn đã chốt xong thông qua công cụ MONA Mail.
    Ví dụ nhắn cho khách: "Tụi em đã nhận được 4.500.000đ, mã đơn hàng của anh chị là #12345". Ví dụ gửi email cho anh chị: "Đơn #12345 đã thanh toán thành công, số tiền 4.500.000đ".

## Ai nên dùng, ai đừng dùng

Nên dùng: Các cửa hàng bán lẻ qua tin nhắn, dịch vụ yêu cầu đặt cọc giữ chỗ, người bán khoá học trực tuyến, hoặc các phòng tập thể hình. Đây là những mô hình kinh doanh có bảng giá cố định, có thể tính toán theo công thức rõ ràng bằng bảng tính hoặc văn bản.

Đừng dùng: Các công ty bán hàng công trình lớn cần kỹ năng thương lượng giá cả phức tạp, hoặc những nơi cần AI tự động duyệt chi tiền ra khỏi tài khoản, xuất kho hàng hoá vật lý ngay lập tức mà không qua con người kiểm tra. Hệ thống hiện tại chỉ làm tốt vai trò nhận tiền và tính toán giá trị niêm yết.

## Cần chuẩn bị gì trước

*   Dữ liệu cốt lõi của anh chị: Một tệp lưu bảng giá dạng cơ bản (`sample-data/bang-gia.csv`) và một tệp quy định mẫu báo giá (`sample-data/mau-bao-gia.md`). Dựa vào đây, trợ lý sẽ biết cách nói chuyện và tính tiền chính xác.
*   Mã kết nối của kênh tương tác: Cụ thể là mã của bot Telegram mà anh chị vừa tạo mới để hệ thống có chỗ nhận tin nhắn của khách.
*   Trí thông minh nhân tạo: Chìa khoá kết nối với các mô hình ngôn ngữ, hoặc nếu máy tính của anh chị đủ mạnh thì có thể tải công cụ Ollama về chạy trực tiếp tại chỗ.
*   Khoảng 10 phút đồng hồ rảnh rỗi để thiết lập ban đầu.

## Dựng thử trong 5 phút

1.  Tải thư mục chứa mã nguồn mẫu này về máy tính của anh chị.
2.  Mở thư mục này bằng các công cụ hỗ trợ lập trình như Claude Code, Codex hoặc Gemini.
3.  Ra lệnh cho phần mềm đọc kỹ tệp `AGENTS.md`. Tệp này chứa toàn bộ quy định để hệ thống tự hiểu cách cài đặt môi trường chạy OpenClaw.
4.  Trả lời các câu hỏi mà máy đưa ra trên màn hình. Anh chị chỉ cần gõ chữ trả lời thông thường, còn phần kỹ thuật, kết nối và gõ lệnh cài đặt thì máy sẽ tự làm hết.
5.  Để hệ thống chạy thử trợ lý ngay trên máy tính cá nhân của anh chị.
6.  Dùng điện thoại nhắn tin với bot Telegram vừa tạo, nhập các tình huống mua hàng để thử xem máy tính toán đúng như trong danh sách kiểm tra hay không.

## Đưa lên chạy thật trên MONA Cloud

Sau khi thử nghiệm ưng ý trên máy tính, anh chị cần một máy chủ ảo hoạt động xuyên suốt để trợ lý làm việc liên tục không nghỉ. Anh chị có thể sử dụng nền tảng MONA Cloud với giá thuê tính theo giờ chỉ từ 550đ/giờ (cấu hình 1 core, 1 GB RAM, 10 GB disk). Hệ thống này cho phép thanh toán bằng tiền Việt Nam, xuất hoá đơn VAT hợp lệ, mọi dữ liệu khách hàng đều nằm an toàn trên máy chủ đặt tại Việt Nam và có chuyên viên của MONA hỗ trợ kỹ thuật trực tiếp. Khi nào ngưng dùng, anh chị tắt máy là hệ thống tự động ngừng tính tiền. Tính năng bấm nút "Dùng ngay" bằng một cú nhấp chuột đang là bản thử nghiệm, tụi em sẽ mở rộng rãi trong thời gian tới.

## Giới hạn tụi em nói trước

Hiện tại nền tảng chưa xây dựng xong cầu nối trực tiếp sang Zalo OA, nên trợ lý này chỉ chạy mượt nhất trên kênh Telegram hoặc ứng dụng chat gắn trên website là OpenClaw WebChat. Dịch vụ mô hình trí tuệ nhân tạo nội bộ MONA AI chưa mở thương mại, nên anh chị bắt buộc phải dùng chìa khoá kết nối của các hãng khác hoặc tự chạy mô hình nội bộ bằng công cụ Ollama. Cuối cùng, chức năng của hệ thống này dừng lại ở việc đọc giá, lên đơn và báo nhận tiền, trợ lý không có khả năng tự quyết định các công việc làm tốn tiền trong tài khoản ngân hàng của anh chị.

## Anh chị đang là khách MONA?

Nếu anh chị đang sử dụng phần mềm hoặc website do The MONA Group thiết kế (thành lập từ năm 2016, với hơn 14.000 dự án đã thực hiện và 85% khách hàng tiếp tục quay lại), tụi em có sẵn gói Doanh nghiệp. Gói này giúp triển khai gắn thẳng tính năng báo giá và thanh toán vào hệ thống anh chị đang dùng thay vì chạy rời rạc bên ngoài. Anh chị chỉ cần gọi tổng đài 1900 636 648 để kỹ thuật viên tư vấn riêng.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/mona-software/mona-agent-templates
