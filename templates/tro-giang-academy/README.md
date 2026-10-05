# Trợ giảng lớp online: Trợ lý AI tự động đáp bài và nhắc hạn cho giảng viên

Anh chị là giảng viên hoặc đang vận hành trung tâm bán khoá học qua mạng và lúc nào cũng ngập trong tin nhắn hỏi bài lúc nửa đêm. Học viên hỏi đi hỏi lại những câu đã có sẵn trong tài liệu giáo trình, còn anh chị thì mỏi tay nhắc từng người nộp bài tập đúng hạn. Template trợ giảng lớp online của tụi em sẽ đóng vai một người trợ lý cần mẫn trực chat xuyên suốt ngày đêm trong nhóm lớp. Trợ lý này tự động dò tìm kiến thức trong tài liệu anh chị cung cấp để đáp lời học viên ngay lập tức, đồng thời thay anh chị hối thúc người học hoàn thành bài tập đúng lịch trình.

## Agent này làm các công việc cụ thể sau đây mỗi ngày

- Giải đáp thắc mắc sát theo giáo trình: Khi học viên nhắn vào nhóm Telegram để hỏi bài, agent sẽ tìm đúng kiến thức trong file giáo trình riêng của lớp để trả lời. Trợ lý dùng kỹ năng giai-dap-bai-hoc để chỉ dẫn chính xác. Ví dụ: "Dựa theo chương 2 của bài giảng, hàm tính tổng trong bảng tính là hàm SUM, anh chị xem lại video bài 4 để rõ hơn cách thao tác nhé."
- Từ chối giải hộ bài kiểm tra: Trợ lý được thiết lập quy tắc cứng là không bao giờ làm bài thay người học để đảm bảo chất lượng giảng dạy. Ví dụ: "Câu hỏi này nằm trong phần kiểm tra cuối khoá nên tụi em chỉ có thể gợi ý anh chị ôn lại phần biến số ở trang 12 thôi."
- Nhắc hạn nộp bài đúng lúc: Dựa vào file lịch học do anh chị nạp vào, agent dùng kỹ năng nhac-han-va-tong-hop để tự động nhắn tin nhắc nhở học viên trước hạn nộp bài đúng 24 giờ.
- Gửi báo cáo tóm tắt cho giảng viên: Mỗi tuần agent sẽ tự thu thập 5 câu hỏi mà lớp thắc mắc nhiều nhất. Trợ lý dùng hệ thống API gửi email giao dịch MONA Mail để gửi danh sách này thẳng vào hộp thư của giảng viên.
- Kết nối nền tảng học tập: Trợ lý lấy dữ liệu trực tiếp từ hệ thống mona.academy thông qua tập lệnh kết nối nội bộ (anh chị có thể chạy lệnh lấy danh sách công cụ trong MCP để lấy tên tool thật trước khi dùng).

## Công cụ này phù hợp cho một nhóm người nhất định và không dành cho tất cả

- Ai nên dùng: Anh chị là giảng viên dạy trực tuyến, hoặc trung tâm đào tạo bán khoá học qua mạng có tài liệu giáo trình và lịch học được viết rõ ràng. Anh chị đang sử dụng nhóm Telegram để tương tác với lớp và muốn giảm bớt việc trực tin nhắn lặp đi lặp lại.
- Ai đừng dùng: Những lớp học chú trọng tương tác cảm xúc, nơi người học cần một người thật để tâm sự và chia sẻ. Hoặc anh chị chỉ muốn dùng kênh Zalo vì hiện tại tụi em chưa kết nối được vào hệ thống này.

## Anh chị cần chuẩn bị vài thông tin và tài khoản trước khi bắt đầu

- Dữ liệu riêng của lớp: Anh chị cần một file văn bản chứa nội dung giáo trình (ví dụ file sample-data/giao-trinh.md) và một file bảng tính chứa lịch học (ví dụ file sample-data/lich-hoc.csv).
- Khoá kết nối Telegram: Đây là một đoạn mã dài giống như mật khẩu (bot token), anh chị lấy miễn phí từ Telegram để tạo cho trợ lý một tài khoản nhắn tin.
- Khoá kết nối trí tuệ nhân tạo: Một đoạn mã (model key) để gọi các mô hình suy nghĩ từ bên ngoài, hoặc anh chị có thể cài đặt hệ thống xử lý nội bộ kín tên là Ollama chạy ngay trên máy tính của mình.
- Thời gian rảnh: Khoảng 10 phút để làm theo các bước hướng dẫn kỹ thuật bên dưới.

## Anh chị chỉ cần làm 6 bước ngắn để dựng thử trong 5 phút

Toàn bộ phần kỹ thuật khó đã có AI lo, anh chị chỉ cần đọc hiểu tiếng Việt và trả lời câu hỏi của AI.

1. Lấy bản sao mã nguồn của template này về máy tính cá nhân của anh chị (bằng lệnh clone).
2. Mở thư mục chứa mã nguồn bằng phần mềm trợ lý lập trình như Claude Code, Gemini hoặc Codex.
3. Gõ lệnh yêu cầu AI đọc kỹ file quy tắc làm việc AGENTS.md để nó tự hiểu cách cài đặt hệ thống.
4. AI sẽ hỏi anh chị vài thông tin, anh chị chỉ cần gõ câu trả lời để cung cấp tên lớp và mã kết nối Telegram.
5. Yêu cầu AI tự động bật trợ lý lên (chạy local qua bộ máy nền OpenClaw).
6. Mở nhóm Telegram đã cài đặt và nhắn thử vài câu trong danh sách kiểm tra (CHECKLIST) để xem agent phản hồi.

## Anh chị có thể đưa lên chạy thật trên MONA Cloud để hoạt động liên tục

Sau khi dùng thử trên máy tính cá nhân, anh chị có thể đưa lên máy chủ MONA Cloud để agent trực nhóm 24/7. Tụi em cho thuê máy chủ theo giờ với giá chỉ từ 550đ/giờ. Anh chị nạp ví trả bằng tiền Việt (VND), tắt máy là hệ thống ngừng tính tiền ngay lập tức. Dữ liệu lớp học nằm trọn trên máy chủ tại Việt Nam do chính anh chị quản lý, xuất được hoá đơn VAT hợp lệ, và luôn có đội ngũ MONA đứng sau hỗ trợ. Nút bấm một phát tự chạy lên mạng (1 click) trên trang monagent.vn hiện đang là bản thử nghiệm, tụi em sẽ sớm mở công khai để mọi người dùng.

## Có vài giới hạn thực tế tụi em muốn nói rõ từ đầu

- Zalo chưa có cầu nối: Hiện tại trợ lý chỉ chạy trên Telegram và gửi tin qua MONA Mail. Đội ngũ đang làm cầu nối qua Zalo OA nhưng chưa ra mắt.
- Cần chuẩn bị nguồn tư duy: Hệ thống MONA AI chưa mở cửa, nên anh chị tự dùng khoá kết nối trí tuệ nhân tạo của chính anh chị hoặc dùng nền tảng Ollama cài đặt tại chỗ.
- Không tự ý quyết định tài chính: Agent bị giới hạn quyền, không được tự ý đưa ra các quyết định có thể làm anh chị tốn tiền.

## Gói Doanh nghiệp dành riêng cho anh chị đang là khách hàng của MONA

Nếu trung tâm của anh chị đang sử dụng hệ thống web hoặc phần mềm do MONA xây dựng, tụi em có gói triển khai riêng để nhúng thẳng trợ lý vào hạ tầng anh chị đang thuê. The MONA Group được thành lập từ năm 2016, đã thực thi hơn 14.000 dự án với 85% khách hàng quay lại. Anh chị vui lòng gọi trực tiếp vào tổng đài 1900 636 648 để kỹ thuật viên kết nối cấu hình riêng mà không cần tự mày mò.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/mona-software/mona-agent-templates
