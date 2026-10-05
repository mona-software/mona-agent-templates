# Trợ lý nội bộ kín: Đọc tài liệu công ty để trả lời nhân viên, không để lọt dữ liệu ra ngoài
Nhân viên mới vào làm liên tục nhắn tin hỏi phòng nhân sự về quy trình nghỉ phép, cách tính lương, hay quy định công tác phí. Đội ngũ nhân sự phải lặp đi lặp lại những câu trả lời giống nhau, làm mất nhiều thời gian làm việc quý giá trong ngày. Khi dùng trợ lý nội bộ kín, nhân viên chỉ cần nhắn lên nhóm Telegram kín, trợ lý sẽ tự động tìm đọc tài liệu anh chị đã nạp và trả lời ngay lập tức. Toàn bộ quá trình xử lý ngôn ngữ diễn ra ngay trên máy chủ của anh chị bằng phần mềm trí tuệ nhân tạo chạy tại chỗ tên là Ollama, đảm bảo không một byte dữ liệu sổ sách nào bị gửi ra bên ngoài.

## Agent này làm gì mỗi ngày
* Trả lời câu hỏi nội bộ dựa trên tài liệu: Trợ lý đọc các tệp quy định và sổ tay nhân viên mà anh chị cung cấp, sau đó tổng hợp câu trả lời ngắn gọn. Ví dụ: Nhân viên nhắn "Nghỉ ốm cần nộp giấy tờ gì?", trợ lý sẽ đáp lại "Theo Quy định nghỉ phép, anh/chị cần nộp giấy khám bệnh do bệnh viện cấp trong vòng 2 ngày làm việc. Nguồn: quy-trinh-nghi-phep.md".
* Trích dẫn nguồn gốc thông tin: Mỗi khi đưa ra câu trả lời, trợ lý luôn ghi rõ thông tin đó được lấy từ tập tin nào và nằm ở đoạn nào. Việc này giúp người đọc biết ngay câu trả lời có căn cứ rõ ràng, không phải thông tin do máy tính tự bịa ra.
* Chặn mọi rò rỉ dữ liệu: Trước khi gửi bất kỳ câu trả lời nào, trợ lý sẽ tự động kiểm tra xem có vô tình gọi ra hệ thống bên ngoài hoặc chứa đường dẫn ra trang web lạ hay không. Nếu phát hiện có kết nối ra ngoài, trợ lý sẽ từ chối trả lời và ghi lại nhật ký để anh chị theo dõi.
* Hỗ trợ trên các nhóm làm việc kín: Trợ lý túc trực trên kênh nhắn tin nội bộ bằng nền tảng OpenClaw hoặc nhóm Telegram kín của công ty, sẵn sàng phản hồi mọi thắc mắc bất cứ lúc nào mà không cần người trực tiếp canh giữ.

## Ai nên dùng, ai đừng dùng
* Nên dùng: Các công ty làm việc với dữ liệu nhạy cảm cực kỳ kỵ việc để lọt thông tin ra ngoài như sổ sách kế toán, hồ sơ pháp lý, bệnh án y tế, hay thông tin cá nhân của người lao động. Anh chị muốn có một trợ lý trí tuệ nhân tạo thông minh nhưng lo sợ bị lấy cắp dữ liệu khi sử dụng các dịch vụ bên ngoài.
* Đừng dùng: Anh chị cần một trợ lý để giao tiếp trực tiếp với khách hàng bên ngoài, hay cần trợ lý để tìm kiếm thông tin tự do trên internet. Trợ lý này được thiết kế để chỉ làm việc với tài liệu nội bộ đã nạp sẵn và cố tình bị cắt đứt kết nối ra bên ngoài để bảo vệ an toàn cho dữ liệu.

## Cần chuẩn bị gì trước
* Các tập tin chứa tài liệu nội bộ: Anh chị gom các văn bản như nội quy công ty, quy trình xin nghỉ phép, sổ tay nhân viên dưới dạng văn bản thuần tuý. Tụi em có để sẵn một số mẫu trong thư mục dữ liệu mẫu như sample-data/noi-quy.md và sample-data/quy-trinh-nghi-phep.md để anh chị tham khảo cách viết.
* Mã kết nối của bot Telegram: Nếu anh chị muốn trợ lý giao tiếp và hoạt động trên nhóm Telegram của công ty, anh chị cần tạo một con bot trên Telegram và lấy một đoạn mã bí mật (gọi là token) để cho trợ lý kết nối vào kênh này.
* Mô hình trí tuệ nhân tạo: Để đảm bảo bảo mật tuyệt đối, anh chị cần cài đặt hệ thống xử lý tên là Ollama để chạy tại chỗ ngay trên máy chủ của anh chị. Nếu không quá khắt khe về việc dữ liệu chạy ra ngoài, anh chị có thể chuẩn bị khóa bí mật của các mô hình khác.
* Thời gian thiết lập: Anh chị cần sắp xếp khoảng 10 phút để tải bộ mã nguồn và thực hiện các bước cài đặt ban đầu.

## Dựng thử trong 5 phút
Anh chị sẽ để cho phần mềm trí tuệ nhân tạo như Claude Code (hoặc Codex, Gemini) làm hết các phần kỹ thuật phức tạp, anh chị chỉ việc gõ câu trả lời theo hướng dẫn.
1. Tải bộ thư mục mẫu này về máy tính cá nhân của anh chị.
2. Mở thư mục vừa tải bằng công cụ Claude Code (hoặc công cụ lập trình tương tự).
3. Yêu cầu công cụ trí tuệ nhân tạo tự đọc tập tin AGENTS.md để hiểu cách làm việc và tự động thiết lập trợ lý.
4. Trả lời các câu hỏi do công cụ trí tuệ nhân tạo đưa ra để điền thông tin riêng của công ty anh chị vào hệ thống.
5. Chạy thử trợ lý ngay trên máy tính cá nhân (môi trường local) để xem trợ lý đọc hiểu tài liệu và hoạt động như thế nào.
6. Đặt câu hỏi thử từ danh sách các câu hỏi mẫu có sẵn để kiểm tra trợ lý có trả lời đúng và có tuân thủ luật bảo mật dữ liệu như mong muốn hay không.

## Đưa lên chạy thật trên MONA Cloud
Khi đã chạy thử thành công trên máy tính cá nhân, anh chị có thể đưa trợ lý lên hoạt động chính thức trên máy chủ ảo của hệ thống MONA Cloud. Máy chủ ảo có bộ nhớ RAM lớn đủ để chạy mô hình tại chỗ, tính phí linh hoạt theo giờ chỉ từ 550đ/giờ (cấu hình cơ bản gồm 1 nhân CPU, 1 GB RAM và 10 GB ổ cứng). Anh chị thanh toán bằng Việt Nam Đồng, có hoá đơn VAT 10% hợp lệ. Hệ thống tính tiền theo thời gian thực, anh chị tắt máy chủ thì hệ thống tự động ngừng tính chi phí. Toàn bộ dữ liệu của doanh nghiệp sẽ nằm trên máy chủ đặt tại Việt Nam do anh chị kiểm soát. Nút bấm thao tác "Dùng ngay" bằng một lần bấm trên trang web monagent.vn hiện tại đang là bản thử nghiệm, tụi em sẽ mở chức năng này trong thời gian tới.

## Giới hạn tụi em nói trước
* Nền tảng Zalo hiện chưa có cầu nối chính thức, tụi em đang làm việc này và chưa có sẵn để dùng.
* Hệ thống MONA AI nội bộ chưa mở, nên anh chị cần tự cài đặt mô hình Ollama hoặc dùng khóa bí mật của mô hình anh chị tự mua.
* Trợ lý này không được cấp quyền tự quyết định các việc liên quan đến chi tiêu hay gọi ra các dịch vụ có tính phí khác.

## Anh chị đang là khách MONA?
Nếu công ty anh chị đã từng làm việc với tụi em và đang sử dụng hệ thống trang web hay phần mềm quản lý do The MONA Group xây dựng, anh chị có thể dùng gói Doanh nghiệp. Ở gói này, tụi em sẽ hỗ trợ gắn thẳng trợ lý nội bộ vào trong hệ thống phần mềm mà anh chị đã có sẵn (trên hạ tầng anh chị đang thuê). Anh chị chỉ cần gọi đến số tổng đài 1900 636 648 để trao đổi chi tiết và nhận báo giá. Tính từ lúc thành lập vào năm 2016, tụi em đã hoàn thành hơn 14.000 dự án khác nhau và tự hào có 85% khách hàng tiếp tục quay lại hợp tác.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/mona-software/mona-agent-templates
