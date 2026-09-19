# Theo dõi đơn vận chuyển: Trợ lý AI báo tình trạng đơn cho khách và nhắc anh chị xử lý khi có biến

Khách hàng liên tục nhắn tin hỏi thăm xem đơn hàng đã đi tới đâu, trong khi kho hàng của anh chị đang tồn đọng hàng chục bưu kiện bị hoàn trả mà không ai kịp xử lý. Việc phải lên trang web của từng đơn vị vận chuyển rồi gõ từng mã số để tra cứu chiếm quá nhiều thời gian làm việc mỗi ngày. Trợ lý AI này được tạo ra để thay thế anh chị làm toàn bộ các công việc lặp đi lặp lại đó. Cứ mỗi 30 phút, nó tự động kiểm tra trạng thái của hàng trăm đơn hàng cùng lúc, gửi thông báo cho khách mua qua email nếu có thay đổi và gom các ca khó giao để xin ý kiến quyết định từ anh chị.

## Agent này làm gì mỗi ngày

*   Liên tục tra cứu tình trạng đơn hàng: Trợ lý tự động kết nối thẳng vào hệ thống dữ liệu của đơn vị vận chuyển bằng tài khoản của cửa hàng. Nó sẽ rà soát toàn bộ danh sách gửi đi mỗi 30 phút để biết chính xác món hàng đang ở kho nào, đã lên xe tải hay đang trên đường giao cho khách.
*   Gửi thông báo cập nhật cho người mua: Mỗi khi một đơn hàng chuyển sang trạng thái mới, ví dụ từ trạng thái đang xử lý sang trạng thái đang giao tới địa chỉ nhận, trợ lý sẽ dùng hệ thống MONA Mail gửi một email ngắn gọn cho khách hàng. Tin nhắn chỉ gửi một lần cho mỗi sự thay đổi để khách không bị làm phiền. Ví dụ: "Đơn hàng mã ABC của anh chị đã đến bưu cục gần nhà và dự kiến được giao trong hôm nay, anh chị chú ý điện thoại nhé".
*   Theo dõi và phân loại các đơn hàng gặp sự cố: Các đơn hàng giao quá thời gian dự kiến hoặc bị khách hàng từ chối nhận sẽ được trợ lý lọc riêng ra. Nó gom tất cả các trường hợp này thành một danh sách tổng hợp và gửi thẳng vào nhóm chat Telegram của đội ngũ vận hành cửa hàng.
*   Đề xuất phương án xử lý và chờ phê duyệt: Trợ lý không tự ý hủy đơn hay báo hoàn hàng. Nó đưa ra gợi ý xử lý trên nhóm Telegram để anh chị xem xét. Ví dụ: "Có 5 đơn hàng bị hoàn về kho chiều nay. Đề xuất gửi email hỏi khách lý do hoặc gọi điện thoại để xác nhận lại. Anh chị duyệt cho em gửi email theo mẫu có sẵn nhé?". Khi anh chị gõ chữ "Đồng ý" vào nhóm, nó mới bắt đầu gửi email đi.

## Ai nên dùng, ai đừng dùng

Nên dùng: Các chủ cửa hàng bán lẻ hoặc doanh nghiệp nhỏ có lượng đơn hàng đều đặn từ 50 đến 500 đơn mỗi ngày. Anh chị đang sử dụng dịch vụ của các đơn vị giao hàng bên ngoài nhưng thiếu người phụ trách theo dõi sát sao tình trạng từng kiện hàng, dẫn đến việc xử lý chậm trễ khi có sự cố.

Đừng dùng: Các hệ thống bán lẻ lớn đã có sẵn phần mềm quản lý kho bãi và hệ thống tự động gửi tin nhắn cho khách hàng mua sắm. Cửa hàng nhỏ lẻ mỗi ngày chỉ có dưới 10 đơn hàng cũng không cần dùng vì anh chị hoàn toàn có thể tự kiểm tra bằng tay trên điện thoại một cách nhanh chóng hơn việc thiết lập hệ thống.

## Cần chuẩn bị gì trước

*   File danh sách đơn hàng và mã vận đơn để trợ lý biết cần theo dõi dữ liệu gì. Tụi em có để sẵn một file mẫu với tên `sample-data/don-van-chuyen.csv` để anh chị xem cấu trúc cột dòng.
*   Mã khóa kết nối của hệ thống vận chuyển mà cửa hàng đang sử dụng. Mã này dùng để trợ lý có quyền truy cập và tra cứu thông tin giống như một nhân viên thật.
*   Một mã nhận diện của phần mềm Telegram để trợ lý có thể gửi tin nhắn báo cáo vào nhóm chat chung của nhân viên cửa hàng.
*   Mã chìa khóa của các mô hình trí tuệ nhân tạo để làm não bộ suy nghĩ cho trợ lý, hoặc phần mềm Ollama cài đặt sẵn trên máy tính.
*   Khoảng 10 phút rảnh rỗi để làm theo các bước cài đặt lần đầu tiên.

## Dựng thử trong 5 phút

*   Bước 1: Tải toàn bộ thư mục chứa mẫu trợ lý này về máy tính cá nhân của anh chị.
*   Bước 2: Mở thư mục vừa tải bằng các phần mềm hỗ trợ viết mã có tích hợp AI như Claude Code, Codex hoặc Gemini.
*   Bước 3: Gõ lệnh yêu cầu AI đọc nội dung file `AGENTS.md` để nó nắm rõ cách thức hoạt động chung. Sau đó yêu cầu AI đọc tiếp file `SKILL.md` nằm trong thư mục `skills` để học các nghiệp vụ cập nhật trạng thái và xử lý đơn hoàn trả.
*   Bước 4: Trả lời các câu hỏi mà AI đưa ra để điền thông tin cài đặt hệ thống. Ví dụ AI sẽ hỏi xin mã Telegram hay cấu hình nhà vận chuyển. Anh chị lưu ý AI sẽ tự động viết các đoạn mã kỹ thuật kết nối, anh chị chỉ cần gõ câu trả lời cung cấp thông tin.
*   Bước 5: Chạy thử trợ lý ngay trên máy tính của anh chị thông qua công cụ nền tảng OpenClaw.
*   Bước 6: Gõ thử một câu yêu cầu nằm trong danh sách kiểm tra để xem trợ lý tra cứu hệ thống và xuất ra tin nhắn mẫu có đúng ý anh chị hay không.

## Đưa lên chạy thật trên MONA Cloud

Sau khi thử nghiệm và thấy trợ lý vận hành đúng ý trên máy tính, anh chị cần một nơi để nó chạy liên tục cả ngày lẫn đêm. Anh chị có thể thuê máy chủ ảo trên hệ thống MONA Cloud với hình thức trả tiền theo giờ sử dụng, mức giá chỉ từ 550đ cho một giờ. Khi không có nhu cầu dùng nữa, anh chị chỉ việc tắt máy chủ là hệ thống sẽ lập tức ngừng tính tiền. Dịch vụ hỗ trợ thanh toán bằng tiền Việt, xuất hoá đơn VAT đầy đủ và toàn bộ dữ liệu đơn hàng sẽ nằm an toàn trên máy chủ của anh chị đặt tại Việt Nam. Nút bấm để đưa trợ lý lên máy chủ với một cú nhấp chuột hiện tại vẫn đang là bản thử nghiệm, tụi em sẽ sớm mở chính thức tính năng này.

## Giới hạn tụi em nói trước

*   Hiện tại phần mềm nền tảng OpenClaw vẫn chưa có cầu nối trực tiếp để nhắn tin qua Zalo OA. Đội ngũ kỹ thuật đang xây dựng tính năng này và sẽ cung cấp cho anh chị sau.
*   Tụi em chưa mở dịch vụ cung cấp sẵn não bộ AI tập trung, do đó anh chị bắt buộc phải dùng mã khóa của mô hình do chính anh chị tự đăng ký, hoặc dùng các mô hình chạy trực tiếp trên máy tính.
*   Trợ lý được thiết kế để tuân thủ mệnh lệnh của con người. Nó không tự ý quyết định các thao tác liên quan đến tiền bạc hay thay đổi trạng thái kiện hàng nếu chưa có sự xác nhận từ nhân viên cửa hàng.

## Anh chị đang là khách MONA?

Nếu anh chị đang sử dụng dịch vụ thiết kế trang web hay phần mềm quản lý do The MONA Group thực hiện, tụi em có cung cấp sẵn gói Doanh nghiệp. Đội ngũ kỹ thuật sẽ hỗ trợ gắn thẳng trợ lý AI này vào hệ thống mà anh chị đang vận hành hàng ngày. Để biết thêm thông tin về gói dịch vụ này, anh chị vui lòng gọi trực tiếp đến tổng đài 1900 636 648 để tụi em tư vấn chi tiết hơn.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/themonagroup/mona-agent-templates
