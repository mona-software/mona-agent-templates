# Nhắc lịch hẹn: Trợ lý AI tự động xác nhận, nhắc lịch và đổi giờ cho cơ sở dịch vụ

Mỗi ngày bộ phận lễ tân của anh chị phải tốn rất nhiều thời gian để gọi điện hoặc nhắn tin cho từng khách hàng nhằm nhắc lịch hẹn, việc này vừa mệt mỏi vừa dễ bỏ sót khách. Nhiều trường hợp khách hàng bận đột xuất nhưng sát giờ mới báo, khiến nhân viên luống cuống tìm giờ trống để dời lịch và làm xáo trộn lịch trình của cả cơ sở. Những khoảng thời gian trống đột ngột này làm lãng phí công sức của thợ và làm giảm trực tiếp doanh thu của cửa hàng. Trợ lý AI này sẽ tự động thay anh chị làm hết những công việc lặp đi lặp lại đó một cách chính xác. Agent sẽ tự động nhắn tin nhắc khách đúng giờ, đề xuất giờ trống nếu khách muốn đổi lịch và báo ngay cho lễ tân khi có bất kỳ thay đổi nào để mọi người cùng nắm thông tin.

## Agent này làm gì mỗi ngày

* Tiếp nhận và gửi tin xác nhận ngay lập tức: Khi có khách đặt lịch thành công, agent sẽ thông qua MONA Mail để gửi ngay một email hoặc tin nhắn Telegram xác nhận chi tiết ngày giờ và dịch vụ cho khách.
* Nhắc lịch tự động theo mốc thời gian: Agent dùng kỹ năng xac-nhan-va-nhac để tự động nhắn tin nhắc khách trước 24 giờ và trước 2 giờ so với thời điểm hẹn. Ở lần nhắc sát giờ, agent sẽ hỏi trực tiếp để chốt lịch giúp lễ tân chuẩn bị. Ví dụ: "Chào chị Mai, chiều nay 14:00 chị có lịch làm móng tay tại salon. Chị có ghé đúng giờ được không để bên em chuẩn bị ghế cho chị nhé?".
* Xử lý linh hoạt các yêu cầu đổi hoặc huỷ lịch: Khi khách hàng nhắn tin xin dời lịch, agent sẽ kích hoạt kỹ năng doi-huy-lich để kiểm tra quy tắc của cơ sở. Nếu quy tắc chỉ cho phép đổi lịch trước 4 tiếng, agent sẽ kiểm tra và từ chối khéo nếu vi phạm. Nếu hợp lệ, agent tự động tìm trong file dữ liệu lịch hẹn để đề xuất 3 khung giờ đang trống. Ví dụ: "Tiếc quá chị bận rồi, vậy em sắp xếp lại cho chị vào 15:00 chiều nay, hoặc 10:00 sáng mai nhé. Chị chọn giờ nào tiện hơn?".
* Cập nhật dữ liệu và báo cáo cho con người: Ngay khi khách chọn giờ mới, agent tự động ghi thông tin vào dữ liệu lịch hẹn của cơ sở, đồng thời nhắn tin báo cáo ngay cho nhân viên lễ tân biết để sắp xếp nhân sự đón khách.

## Ai nên dùng, ai đừng dùng

Nhóm nên dùng là các chủ spa, thẩm mỹ viện, salon tóc, phòng khám nha khoa, phòng tập yoga hoặc bất kỳ cơ sở dịch vụ nào cần khách đặt giờ trước. Đây là những nơi rất dễ bị thất thu nếu khách hàng quên lịch hoặc huỷ sát giờ mà không có khách khác đắp vào.

Nhóm không nên dùng là các cửa hàng bán lẻ, siêu thị mua đứt bán đoạn không cần hẹn giờ trước. Các doanh nghiệp có quy trình xếp lịch quá phức tạp, cần nhiều cấp quản lý hoặc chuyên gia trực tiếp duyệt từng hồ sơ khách hàng cũng không nên dùng mẫu này vì AI có thể không nắm bắt hết các luật ngầm của tổ chức.

## Cần chuẩn bị gì trước

Để trợ lý này hoạt động, anh chị cần chuẩn bị sẵn file dữ liệu lịch hẹn của cơ sở. Tụi em có để sẵn một file mẫu trong thư mục `sample-data/lich-hen.csv` trông giống như một bảng thông tin nhỏ, anh chị chỉ cần thay bằng dữ liệu thật của mình kèm theo danh sách các quy tắc đổi huỷ lịch của riêng cơ sở.

Kế tiếp, anh chị cần một tài khoản mã bot Telegram, đây giống như một số điện thoại ảo để agent dùng nhắn tin qua lại với khách. Anh chị cũng cần có một địa chỉ email để agent gửi thư, tụi em khuyên dùng dịch vụ MONA Mail vì hệ thống này cấp sẵn hộp thư riêng cho AI, giúp agent có thể tự đọc và trả lời thư của khách.

Cuối cùng, anh chị cần có key kết nối của mô hình AI để làm bộ não suy nghĩ, hoặc cài đặt phần mềm Ollama trên máy tính nếu muốn chạy mô hình AI nội bộ. Anh chị sẽ mất khoảng 10 phút để thu thập đủ các thông tin này trước khi bắt đầu.

## Dựng thử trong 5 phút

Quá trình cài đặt rất đơn giản vì phần kỹ thuật đã có các phần mềm AI lo liệu, anh chị chỉ đóng vai trò người kiểm duyệt và trả lời câu hỏi:

* Tải toàn bộ thư mục chứa mẫu agent này về máy tính cá nhân của anh chị.
* Mở thư mục này bằng các phần mềm AI hỗ trợ lập trình như Claude Code, Gemini hoặc Codex.
* Yêu cầu phần mềm AI tự đọc file `AGENTS.md` trong thư mục. File này chứa toàn bộ cách thức làm việc và hướng dẫn cài đặt môi trường OpenClaw.
* Phần mềm AI sẽ hỏi anh chị các thông tin cần thiết. Anh chị chỉ cần cung cấp thông tin như tên cơ sở, cấu hình mô hình AI vào tệp `models.providers.<id>`, và dán mã bot Telegram để cài đặt kênh liên lạc bằng lệnh `openclaw channels add`.
* Cho phép phần mềm AI tự động chạy lệnh `openclaw onboard --install-daemon` để khởi động agent ngay trên máy tính của anh chị (chạy local). Để duyệt cho khách nhắn tin lần đầu, anh chị dùng lệnh `openclaw pairing approve telegram` kèm mã code hệ thống cấp.
* Mở ứng dụng Telegram, đóng vai khách hàng nhắn tin thử cho agent và kiểm tra theo danh sách các tình huống trong mục CHECKLIST tụi em đã ghi sẵn để xem agent trả lời đúng ý chưa.

## Đưa lên chạy thật trên MONA Cloud

Khi anh chị đã chạy thử trên máy tính và thấy agent trả lời trơn tru, bước tiếp theo là đưa agent lên máy chủ MONA Cloud (VPS) để trợ lý này có thể làm việc liên tục không nghỉ. Chi phí thuê máy chủ tính theo giờ rất rẻ, chỉ từ 550đ cho một giờ chạy, anh chị trả bằng tiền VND và có xuất hoá đơn VAT 10% đàng hoàng. Anh chị dùng bao nhiêu tiếng thì hệ thống tính tiền bấy nhiêu, khi nào tắt máy chủ là ngừng tính phí. Toàn bộ dữ liệu lịch hẹn của khách hàng đều nằm an toàn trên máy chủ của chính anh chị tại Việt Nam. Nút bấm "Dùng ngay" bằng 1 click trên trang web hiện tại đang là bản thử nghiệm và sẽ sớm mở chính thức, nên lúc này anh chị có thể nhờ AI đưa agent lên mây thông qua lệnh `npx -y monacloud deploy` một cách dễ dàng.

## Giới hạn tụi em nói trước

Hiện tại nền tảng mã nguồn mở OpenClaw chưa có cầu nối với Zalo OA, tụi em đang xây dựng hệ thống này nên tạm thời anh chị dùng kênh Telegram và email trước. Hệ thống MONA AI nội bộ cũng chưa mở, do đó anh chị bắt buộc phải dùng key kết nối của mô hình AI mà anh chị tự mua, hoặc dùng mô hình mã nguồn mở qua Ollama. Agent này được thiết kế thuần tuý để theo dõi và thay đổi lịch hẹn, tụi em không cấp quyền cho agent tự quyết định các việc liên quan đến tiền bạc hay hoàn tiền cho khách. Cuối cùng, nút bấm triển khai nhanh 1 click vẫn đang trong giai đoạn thử nghiệm.

## Anh chị đang là khách MONA?

Nếu anh chị đang sử dụng trang web hoặc phần mềm quản lý do The MONA Group thiết kế, anh chị có thể chuyển sang dùng gói Doanh nghiệp để gắn thẳng mẫu agent này vào hệ thống phần mềm sẵn có. Công ty tụi em thành lập từ năm 2016 với hơn 14.000 dự án đã hoàn thành và 85% khách hàng tiếp tục quay lại, nên đội ngũ kỹ thuật có thừa kinh nghiệm để triển khai agent lên chính hạ tầng mà anh chị đang thuê. Anh chị hãy gọi thẳng vào tổng đài 1900 636 648 để tụi em kiểm tra hệ thống và tư vấn cài đặt trực tiếp.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/mona-software/mona-agent-templates
