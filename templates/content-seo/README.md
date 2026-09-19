# Content SEO có gate: Viết bài theo đúng giọng thương hiệu và tự soát lỗi trước khi gửi anh chị duyệt

Nhiều anh chị làm nội dung thường phải tự ôm đồm quá nhiều việc, từ lúc lên ý tưởng, viết bài cho đến khi rà soát từng chữ một. Khi giao việc này cho nhân sự mới hoặc để máy móc viết tự do, bài viết thường rơi vào tình trạng văn phong nhạt nhòa, câu chữ khô khan, hoặc tệ hơn là vi phạm những từ cấm kỵ của ngành nghề kinh doanh. Trợ lý AI này sinh ra để đóng vai trò làm người viết nháp kiêm màng lọc kỹ tính cho anh chị. Thay vì tốn hàng giờ đồng hồ ngồi gõ từng dòng, anh chị chỉ cần đưa ra một dàn ý cơ bản, trợ lý sẽ viết bài đúng giọng điệu thương hiệu, tự động kiểm tra kỹ lưỡng để loại bỏ văn mẫu, sau đó trình lên một bản nháp sạch sẽ chờ anh chị duyệt và bấm đăng.

## Agent này làm gì mỗi ngày

*   **Viết bài bám sát giọng thương hiệu của doanh nghiệp:** Trợ lý sẽ đọc thật kỹ tài liệu hướng dẫn giọng văn (như file `sample-data/giong-thuong-hieu.md`) và phân tích năm bài mẫu do anh chị cung cấp trước khi bắt đầu đặt bút viết. Kỹ năng `viet-theo-giong` giúp bài viết giữ đúng thần thái của người trong nghề.
    *   *Ví dụ tin nhắn:* "Tụi em đã viết xong bản nháp bài Cách chọn mua vật liệu xây dựng, xưng hô là kỹ sư tư vấn đúng như bài mẫu anh chị đã gửi tuần trước."
*   **Kiểm tra bài viết qua màng lọc khắt khe:** Kỹ năng `soat-truoc-khi-dang` đóng vai trò như một người biên tập viên khó tính. Hệ thống tự động quét toàn bộ bản nháp để đối chiếu với file `sample-data/tu-cam.md`, tìm kiếm các từ ngữ bị cấm, những lời hứa lố, hoặc các con số không có nguồn gốc rõ ràng. Kỹ năng này cũng đo lường độ dài của các câu để đảm bảo văn bản không bị đều đều như máy viết.
*   **Tự động sửa lỗi khi rớt màng lọc:** Nếu phát hiện bất kỳ lỗi nào trong quá trình kiểm tra, trợ lý sẽ tự động xóa đoạn đó và viết lại cho đến khi đạt tiêu chuẩn, thay vì gửi ngay một bản nháp lỗi cho anh chị.
    *   *Ví dụ tin nhắn:* "Bản nháp đầu tiên bị vướng từ cam kết chữa dứt điểm 100%, tụi em đã tự động sửa thành hỗ trợ cải thiện tình trạng bệnh cho đúng luật và gửi lại bản mới."
*   **Gửi bản cuối qua Telegram và chờ duyệt:** Chỉ khi bản nháp vượt qua được tất cả các tiêu chí kiểm tra, trợ lý mới gửi bản thảo cho anh chị qua kênh Telegram để anh chị đọc thử.
*   **Đăng bài trực tiếp lên WordPress:** Khi anh chị gật đầu đồng ý với bản nháp, trợ lý sẽ tự động đăng tải bài viết lên trang web WordPress, giúp tiết kiệm thêm thời gian thao tác thủ công.

## Ai nên dùng, ai đừng dùng

*   **Người nên dùng:** Chủ doanh nghiệp đang tự làm nội dung nhưng thiếu thời gian gõ bài, hoặc đội ngũ marketing từ một đến hai người cần một trợ lý viết nháp và tự động rà soát lỗi văn phong.
*   **Người đừng dùng:** Những đội ngũ chuyên viết nội dung bay bổng, hoặc các hệ thống cần xuất bản hàng ngàn bài viết mỗi ngày mà không cần người kiểm duyệt.

## Cần chuẩn bị gì trước

Để trợ lý hoạt động đúng ý, anh chị cần chuẩn bị sẵn một số tài nguyên:
*   Dữ liệu riêng của doanh nghiệp: Một file mô tả chi tiết giọng thương hiệu, một danh sách các từ cấm không được phép dùng, và năm bài viết mẫu mà anh chị ưng ý nhất.
*   Token bot Telegram để tạo kênh giao tiếp riêng với trợ lý (anh chị có thể lấy đoạn mã này qua BotFather trên ứng dụng Telegram).
*   Khóa API (key model) của các dịch vụ cung cấp mô hình ngôn ngữ lớn, hoặc phần mềm Ollama nếu anh chị muốn chạy mô hình trực tiếp trên máy tính của mình.
*   Khoảng mười phút để thực hiện các thao tác thiết lập ban đầu.

## Dựng thử trong 5 phút

AI sẽ làm toàn bộ phần kỹ thuật, anh chị chỉ cần trả lời các câu hỏi AI đưa ra.
1.  Tải thư mục chứa mẫu trợ lý này về máy tính (clone mã nguồn).
2.  Mở thư mục vừa tải bằng phần mềm Claude Code (hoặc Codex, Gemini).
3.  Yêu cầu AI đọc file `AGENTS.md` để hiểu rõ cách thức làm việc của trợ lý.
4.  AI sẽ hỏi anh chị các thông tin cần thiết như token Telegram hay vị trí lưu file bài mẫu, anh chị chỉ việc gõ câu trả lời.
5.  Ra lệnh để AI tự động cài đặt môi trường OpenClaw và chạy thử ngay trên máy tính của anh chị.
6.  Mở ứng dụng Telegram, nhắn một câu thử nghiệm lấy từ danh sách kiểm tra (CHECKLIST) để xem trợ lý phản hồi như thế nào.

## Đưa lên chạy thật trên MONA Cloud

Khi đã thử nghiệm ưng ý, anh chị có thể đưa trợ lý lên chạy liên tục trên nền tảng MONA Cloud. Máy chủ ảo (VPS) có mức giá tính theo giờ chỉ từ 550đ/giờ (cấu hình 1 core CPU, 1 GB RAM, 10 GB ổ cứng), anh chị tắt máy là hệ thống ngừng tính tiền. Mọi thanh toán đều bằng tiền Việt Nam Đồng (VND), có xuất hóa đơn VAT đầy đủ, dữ liệu nằm an toàn trên máy chủ đặt tại Việt Nam. AI gọi thẳng tới các dịch vụ, và luôn có đội ngũ nhân viên MONA đứng sau hỗ trợ qua số điện thoại 1900 636 648. Nút bấm thao tác Dùng ngay với một cú nhấp chuột hiện đang là bản thử nghiệm, tụi em sẽ sớm mở tính năng này chính thức.

## Giới hạn tụi em nói trước

Hiện tại hệ thống OpenClaw chưa có cầu nối trực tiếp với Zalo, tụi em đang xây dựng tính năng này và sẽ ra mắt sau. Dịch vụ MONA AI hiện chưa mở, nên anh chị cần dùng khóa model của chính mình hoặc sử dụng phần mềm Ollama chạy tại chỗ. Trợ lý cũng được thiết lập nguyên tắc không bao giờ tự ý quyết định các công việc gây tốn tiền.

## Anh chị đang là khách MONA?

Nếu anh chị đang sử dụng trang web hoặc phần mềm do The MONA Group xây dựng (công ty hoạt động từ 2016, thực hiện hơn 14.000 dự án, 85% khách hàng quay lại), tụi em có gói Doanh nghiệp triển khai riêng. Gói này giúp gắn thẳng trợ lý vào hệ thống hiện tại của anh chị, hãy gọi ngay đến tổng đài 1900 636 648 để được tư vấn chi tiết.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/themonagroup/mona-agent-templates
