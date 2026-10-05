# Trực website: Trợ lý AI canh gác hệ thống liên tục cho chủ trang web

Đang ngủ ngon giữa đêm thì điện thoại reo liên tục vì khách hàng phàn nàn không vào được trang web để đặt mua hàng. Lúc bật máy tính lên và mất cả chục phút kiểm tra, anh chị mới phát hiện ra ổ cứng chứa dữ liệu đã đầy từ mấy tiếng trước làm sập toàn bộ hệ thống cơ sở dữ liệu. Trợ lý AI trực website ra đời để làm một người gác cổng mẫn cán, thay anh chị kiểm tra tình trạng hệ thống liên tục không biết mệt mỏi. Thay vì chờ khách hàng bực tức báo lỗi rồi mới lật đật đi sửa, trợ lý sẽ tự động khởi động lại dịch vụ hoặc nhắn thẳng vào nhóm Telegram của đội kỹ thuật kèm theo nguyên nhân cụ thể để anh chị yên tâm ngủ ngon giấc.

## Agent này làm gì mỗi ngày

* Đều đặn mỗi phút một lần, trợ lý sẽ gõ cửa từng trang web để xem hệ thống có trả lời nhanh không, mã trạng thái hoạt động có bình thường không và chứng chỉ bảo mật SSL ổ khóa xanh còn bao nhiêu ngày thì hết hạn.
* Khi trang web bỗng dưng báo lỗi hoặc chạy chậm quá mức cho phép, trợ lý lập tức gửi tin nhắn cảnh báo vào nhóm Telegram. Ví dụ như nhắn: "Cảnh báo trang web bán hàng đang trả về lỗi 502, thời gian phản hồi quá chậm so với mức bình thường".
* Tự động bắt tay vào xử lý những sự cố đơn giản mà đã được anh chị cấp quyền từ trước giống như một người thợ thạo việc. Việc này bao gồm tự động khởi động lại dịch vụ đang bị treo, xóa bớt các file nhật ký sự kiện lưu trữ đã cũ để dọn trống ổ đĩa, hoặc tự động bấm lệnh gia hạn chứng chỉ bảo mật.
* Với những sự cố phức tạp ngoài khả năng tự chữa, trợ lý sẽ không đoán mò mà sẽ lấy đúng 50 dòng thông báo lỗi mới nhất của máy chủ để gửi cho con người. Việc này giúp anh chị vừa nắm tình hình vừa có ngay manh mối để sửa lỗi mà không cần tự chui vào máy chủ tìm kiếm mòn mỏi.
* Khi mọi thứ đã hoạt động ổn định trở lại, trợ lý sẽ gửi thông báo tin vui để mọi người nắm tình hình. Ví dụ như báo cáo: "Trang web đã truy cập bình thường trở lại, tổng thời gian xảy ra sự cố kéo dài 15 phút".

## Ai nên dùng, ai đừng dùng

Mẫu trợ lý trực website này sinh ra dành cho những anh chị đang vận hành trang web hoặc ứng dụng thực tế trên MONA Cloud hoặc bất kỳ máy chủ ảo nào khác. Đây là người phụ tá đắc lực cho những nhóm kỹ thuật không có người dư dả thời gian ngồi nhìn màn hình liên tục nhưng vẫn cần đảm bảo hệ thống chạy xuyên suốt ngày đêm.

Anh chị đừng dùng mẫu này nếu hệ thống đang chạy chỉ là một trang web giới thiệu tĩnh không có kết nối cơ sở dữ liệu bên dưới. Anh chị cũng không nên dùng nếu đang thuê dịch vụ máy chủ dùng chung, nơi người quản trị hệ thống không cấp quyền tự khởi động lại dịch vụ hay dọn dẹp bộ nhớ.

## Cần chuẩn bị gì trước

* Một danh sách các trang web cần theo dõi và mức thời gian phản hồi chậm nhất được cho phép, anh chị lưu toàn bộ vào file có tên `sample-data/sites.yaml`.
* Một chuỗi mã kết nối token của con bot Telegram để trợ lý biết đường gửi tin nhắn vào đúng nhóm kỹ thuật của anh chị.
* Một mã chìa khóa kết nối của các mô hình ngôn ngữ AI do nền tảng MONA AI hiện chưa mở cửa công khai. Nếu muốn an toàn tuyệt đối cho dữ liệu, anh chị hoàn toàn có thể dùng mô hình chạy tại chỗ Ollama.
* Khoảng 10 phút đồng hồ rảnh rỗi để cấu hình và dặn dò trợ lý trong lần thiết lập đầu tiên.

## Dựng thử trong 5 phút

* Bước 1: Tải toàn bộ thư mục mã nguồn của mẫu trực website này về máy tính cá nhân của anh chị.
* Bước 2: Mở thư mục vừa tải bằng các phần mềm lập trình có tích hợp AI như Claude Code, Codex hoặc Gemini.
* Bước 3: Gõ lệnh yêu cầu AI đọc thật kỹ file có tên `AGENTS.md` để AI tự học cách thức hoạt động của hệ thống OpenClaw.
* Bước 4: Trả lời các câu hỏi mà AI đặt ra để điền thông tin. Toàn bộ phần mã hóa và cấu hình kỹ thuật máy móc thì AI sẽ tự làm, anh chị chỉ cần làm người quản lý cung cấp tên trang web và mã kết nối.
* Bước 5: Chạy thử trợ lý ngay trên máy tính của anh chị để xem cách nó kiểm tra trạng thái trang web.
* Bước 6: Gõ thử vài câu lệnh yêu cầu nằm trong danh sách file CHECKLIST để kiểm tra xem trợ lý đã hiểu đúng nhiệm vụ canh gác hệ thống hay chưa.

## Đưa lên chạy thật trên MONA Cloud

Khi đã thiết lập xong trên máy tính cá nhân và ưng ý với kết quả, anh chị có thể đưa ngay trợ lý lên máy chủ đám mây MONA Cloud để trực cả ngày lẫn đêm. Hệ thống cung cấp cấu hình máy chủ tính theo giờ chỉ từ 550 đồng cho mỗi giờ sử dụng, trang bị sẵn 1 nhân xử lý, 1 GB bộ nhớ tạm và 10 GB ổ cứng. Mọi chi phí đều thanh toán bằng tiền Việt Nam, xuất hóa đơn giá trị gia tăng đầy đủ, tắt máy chủ là ngừng tính tiền, và dữ liệu luôn nằm an toàn trên máy chủ của chính anh chị tại Việt Nam. Tính năng bấm triển khai bằng một thao tác chuột đang trong giai đoạn thử nghiệm nên anh chị hãy gõ lệnh thủ công để đưa lên thêm một thời gian ngắn nữa nhé.

## Giới hạn tụi em nói trước

* Nút bấm dùng ngay trực tiếp trên trang monagent.vn hiện vẫn đang hiển thị ở dạng thử nghiệm và tụi em sẽ sớm mở chức năng thật.
* Trợ lý hiện chưa có cầu nối sang ứng dụng Zalo, tụi em đang xây dựng bộ phận này và sẽ cập nhật sau.
* Anh chị bắt buộc phải dùng mã kết nối mô hình AI của riêng mình hoặc chạy cấu hình Ollama tại chỗ.
* Trợ lý hoàn toàn tuân thủ mệnh lệnh và không tự ý quyết định các việc gây tốn thêm chi phí của anh chị nếu không được dặn trước.

## Anh chị đang là khách MONA?

Trường hợp anh chị cần giám sát hệ thống phức tạp hơn, tụi em có cung cấp gói Doanh nghiệp giúp gắn thẳng trợ lý vào trang web hoặc phần mềm mà MONA đã dựng sẵn cho anh chị. Công ty The MONA Group đã thành lập từ năm 2016 và hoàn thành hơn 14.000 dự án với 85% khách hàng quay lại, anh chị cứ gọi thẳng số tổng đài 1900 636 648 để tụi em tư vấn và lo liệu toàn bộ.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/mona-software/mona-agent-templates
