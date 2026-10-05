# Trợ lý tuyển dụng: Đọc hồ sơ và sắp xếp lịch phỏng vấn thay cho anh chị

Một ngày làm việc bận rộn trôi qua, đến tối muộn anh chị lại phải mở hòm thư tải từng file hồ sơ xuống đọc, nhặt ra thông tin kinh nghiệm, rồi tự tay viết thư hẹn lịch phỏng vấn. Việc này chiếm rất nhiều thời gian nghỉ ngơi và dễ làm anh chị bỏ sót người tài. Trợ lý tuyển dụng này sẽ thay anh chị nhận thư, đọc file đính kèm, đối chiếu với tiêu chí anh chị đề ra và tự động lên lịch với các ứng viên phù hợp.

## Trợ lý này thay anh chị làm các việc cụ thể mỗi ngày

* Đọc thư ứng tuyển gửi đến hộp thư: Trợ lý dùng MONA Mail để nhận email, sau đó tự động tải các file đính kèm.
* Chấm điểm hồ sơ theo tiêu chí: Trợ lý dùng kỹ năng đọc hồ sơ (cham-cv) để đối chiếu nội dung với bảng mô tả công việc. Kế tiếp, nó xếp hạng các ứng viên từ cao xuống thấp và ghi rõ lý do đạt hay chưa đạt từng điểm.
* Gửi thư hẹn lịch phỏng vấn: Với người qua vòng hồ sơ, trợ lý dùng kỹ năng hẹn lịch (hen-phong-van) để chủ động gửi email đề xuất khung giờ anh chị đã báo rảnh (ví dụ: "Chào Minh, công ty mời em phỏng vấn vào 14h hoặc 15h thứ Năm tuần này").
* Xác nhận và nhắc lịch: Khi nhận thư chốt giờ từ ứng viên, trợ lý nhắn tin báo lại cho anh chị qua Telegram, đồng thời tự động gửi email nhắc ứng viên trước giờ hẹn 2 tiếng đồng hồ.

## Nhóm công ty nên dùng và nhóm chưa phù hợp lúc này

* Doanh nghiệp nên dùng: Các công ty nhỏ tuyển khoảng 5 đến 50 người mỗi năm, không có bộ phận nhân sự chuyên trách. Người quản lý đang phải tự đọc hồ sơ và hẹn lịch thủ công.
* Doanh nghiệp đừng dùng: Các tổ chức lớn cần tuyển hàng nghìn công nhân mỗi đợt, yêu cầu quy trình xét duyệt qua nhiều phòng ban, hoặc cần phỏng vấn sơ loại trực tiếp qua điện thoại.

## Anh chị cần chuẩn bị vài thứ trước khi bắt đầu

Để trợ lý làm việc, anh chị cần gom sẵn dữ liệu trong khoảng 10 phút:
* Mô tả công việc và bảng tiêu chí: Chép ra file thông thường để trợ lý biết anh chị đang tìm người như thế nào. Tụi em có để sẵn mẫu ở file sample-data/jd-sale.md và sample-data/tieu-chi.csv.
* Đoạn mã kết nối bot Telegram: Anh chị lấy đoạn mã từ Telegram để tạo kênh chat, nơi trợ lý nhắn tin báo cáo công việc cho anh chị.
* Chìa khoá kết nối AI: Anh chị tự chuẩn bị chìa khoá của các nhà cung cấp mô hình ngôn ngữ hoặc dùng phần mềm Ollama chạy tại chỗ để cung cấp bộ não cho trợ lý.

## Trí tuệ nhân tạo giúp anh chị dựng thử trên máy tính trong 5 phút

Anh chị không cần tự làm phần kỹ thuật, chỉ cần để AI đọc và thiết lập qua 6 bước ngắn:
1. Tải thư mục bộ mã trợ lý này về máy tính (clone).
2. Mở công cụ Claude Code (hoặc Codex, Gemini) trong thư mục vừa tải.
3. Gõ lệnh yêu cầu công cụ AI đọc file AGENTS.md để nó hiểu cách cài đặt OpenClaw.
4. Công cụ AI sẽ tự động chạy lệnh cài đặt, nó hỏi thông tin gì thì anh chị trả lời thông tin đó.
5. Khi AI báo hoàn tất, anh chị có thể chạy hệ thống trực tiếp trên máy tính.
6. Anh chị đối chiếu với danh sách trong file CHECKLIST, thử nhắn vài câu trên Telegram hoặc gửi email mẫu để kiểm tra trợ lý hoạt động.

## Anh chị đưa trợ lý lên chạy thật trên nền tảng MONA Cloud

Khi chạy thử ưng ý, anh chị có thể đưa trợ lý lên máy chủ ảo trên MONA Cloud để túc trực làm việc. Gói máy chủ tính phí theo giờ chỉ từ 550đ/giờ, thanh toán bằng VND, xuất hoá đơn VAT 10% và mọi dữ liệu nằm an toàn trên máy chủ tại Việt Nam. Nút bấm dùng ngay với một cú click chuột đang là bản thử nghiệm, tụi em sẽ sớm hoàn thiện tính năng này. Khi hết đợt tuyển dụng, anh chị tắt máy chủ là hệ thống lập tức ngừng tính tiền.

## Tụi em báo trước một số giới hạn kỹ thuật

* Ứng dụng nền OpenClaw chưa kết nối được với Zalo. Tụi em đang xây dựng cầu nối Zalo OA MONA, trợ lý hiện chỉ có thể trao đổi với anh chị qua Telegram.
* Tính năng MONA AI hiện chưa mở, nên anh chị bắt buộc phải dùng chìa khoá AI của anh chị hoặc dùng phần mềm Ollama.
* Trợ lý bị giới hạn quyền, không thể tự quyết định các việc gây tốn tiền mà chưa hỏi ý kiến anh chị.

## Khách hàng đang dùng phần mềm MONA có thể gắn thẳng vào hệ thống

Nếu anh chị đã là khách hàng của tụi em, gói Doanh nghiệp cho phép gắn thẳng trợ lý này vào website hoặc phần mềm quản lý mà MONA đã dựng. Công ty The MONA Group thành lập từ năm 2016, đã làm hơn 14.000 dự án và có 85% khách hàng quay lại. Anh chị gọi số 1900 636 648 để có người MONA đứng sau tư vấn và hỗ trợ triển khai trực tiếp.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/mona-software/mona-agent-templates
