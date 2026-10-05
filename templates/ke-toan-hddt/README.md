# Kế toán hoá đơn: Trợ lý tự động ghi nhận tiền vào và theo dõi công nợ cho chủ kinh doanh

Cuối tháng, anh chị thường phải ngồi căng mắt dò từng dòng sao kê ngân hàng rồi lật sổ công nợ ra gạch xoá. Đôi khi, anh chị lỡ sót một khoản tiền nhỏ khách chuyển từ tuần trước mà tìm mỏi mắt không ra nguyên nhân. Việc thu tiền, theo dõi công nợ và chuẩn bị dữ liệu xuất hoá đơn chiếm quá nhiều thời gian làm việc chính. Đó là chưa kể cảm giác ngại ngùng khi anh chị phải tự tay nhắn tin đòi nợ khách quen. Trợ lý AI này sinh ra để gánh vác phần việc tay chân lặp đi lặp lại đó. Nó túc trực suốt ngày đêm để đọc thông báo tiền vào, tự động gạch nợ và chuẩn bị sẵn dữ liệu để anh chị xuất hoá đơn, giúp anh chị rảnh tay tập trung lo việc kinh doanh cốt lõi.

## Agent này làm gì mỗi ngày

* Đọc thông báo tiền vào theo thời gian thực: Khi có khách chuyển khoản qua tài khoản ngân hàng của anh chị, trợ lý sẽ dùng API ngân hàng và dịch vụ xác nhận thanh toán tự động MONA Pay để nhận thông báo tức thì. Tiền của khách không đi qua MONA mà vào thẳng tài khoản ngân hàng đứng tên anh chị. Hệ thống không bỏ sót bất kỳ giao dịch nào dù là nhỏ nhất.
* Ghi sổ và đối soát tự động: Với kỹ năng ghi-so-tien-vao, trợ lý tự động đọc nội dung chuyển khoản để tìm mã khách hàng hoặc mã đơn hàng. Sau đó, nó đối chiếu với file công nợ của anh chị. Nếu số tiền khớp, nó tự gạch nợ. Nếu thừa hoặc thiếu, nó nhắn tin báo ngay. Ví dụ tin nhắn Telegram: "Khách hàng Nguyễn Văn A (mã KH01) vừa chuyển 500.000đ thanh toán đơn hàng #123. Em đã gạch nợ thành công."
* Điểm danh công nợ mỗi sáng: Thông qua kỹ năng nhac-cong-no, đúng 8 giờ sáng hàng ngày, trợ lý gửi một bản báo cáo ngắn gọn qua Telegram liệt kê danh sách những khách hàng đang nợ quá hạn. Nó giúp anh chị biết ai đang nợ, nợ bao lâu và tổng số tiền là bao nhiêu.
* Soạn email nhắc nợ lịch sự: Nó không tự ý đòi nợ mà sẽ hỏi ý kiến anh chị trước. Khi anh chị duyệt, trợ lý dùng MONA Mail để soạn một email gửi khách với nội dung mềm mỏng, lịch sự nhưng rõ ràng, đính kèm số tiền cần thanh toán. Anh chị chỉ việc xem qua và đồng ý cho gửi đi.
* Gom dữ liệu xuất hoá đơn: Khi quá trình thanh toán hoàn tất, trợ lý tập hợp đầy đủ tên công ty, mã số thuế, số tiền thành một danh sách gọn gàng. Phần dữ liệu này được dùng cho hệ thống MONA eInvoice, giúp anh chị chép qua phần mềm kế toán nhanh chóng. Hiện tại API dành cho nhà phát triển để tự phát hành hoá đơn chưa mở nên trợ lý chỉ dừng ở bước chuẩn bị dữ liệu.

## Ai nên dùng, ai đừng dùng

* Người nên dùng: Chủ doanh nghiệp nhỏ đang tự tay làm sổ sách thu chi mỗi ngày, hoặc kế toán của công ty ít người đang bị ngập trong giấy tờ, tin nhắn báo có và file Excel mỗi kỳ chốt sổ. Trợ lý này giúp anh chị quy củ lại luồng tiền vào và công nợ một cách chính xác.
* Người đừng dùng: Doanh nghiệp quy mô lớn có quy trình kế toán nhiều bước duyệt phức tạp, cần một hệ thống ERP khổng lồ với hàng chục phân hệ đan chéo nhau. Trợ lý này được thiết kế nhỏ gọn, tập trung giải quyết triệt để khâu ghi nhận tiền và nhắc nợ nên không phù hợp với luồng quản lý quá nhiều tầng nấc.

## Cần chuẩn bị gì trước

Anh chị chỉ cần dành ra khoảng 10 phút và chuẩn bị sẵn những thứ sau:
* Danh sách khách hàng và công nợ hiện tại lưu trong file CSV. Tụi em có để sẵn một file mẫu tên là sample-data/cong-no.csv, anh chị cứ mở lên và điền thông tin thực tế vào đó.
* Một mã token bot Telegram để trợ lý dùng làm tài khoản nhắn tin báo cáo công việc cho anh chị mỗi ngày.
* Key của các mô hình AI. Do hệ thống MONA AI chưa mở, anh chị cần tự mua key hoặc nếu có máy tính mạnh, anh chị có thể dùng nền tảng Ollama chạy ngay tại chỗ để không byte nào rời server (cách của gói Kín).

## Dựng thử trong 5 phút

Quá trình cài đặt cực kỳ đơn giản vì AI sẽ làm phần kỹ thuật nặng nhọc, anh chị chỉ việc trả lời câu hỏi:
1. Lấy mã nguồn template trợ lý kế toán hoá đơn này về máy tính của anh chị.
2. Mở thư mục chứa mã nguồn bằng Claude Code, Codex hoặc Gemini.
3. Gõ lệnh yêu cầu AI đọc file AGENTS.md. File này chứa toàn bộ cách làm việc và thiết lập trợ lý.
4. AI sẽ tự động hỏi anh chị các thông tin cần thiết như token Telegram, đường dẫn thư mục chứa file CSV công nợ. Anh chị chỉ việc cung cấp thông tin.
5. Chạy trợ lý ngay trên máy tính của anh chị thông qua môi trường OpenClaw. OpenClaw là mã nguồn mở giúp trợ lý hoạt động ổn định.
6. Thử gửi vài tin nhắn giả lập tiền vào hoặc hỏi danh sách nợ để kiểm tra xem trợ lý trả lời đúng chưa theo các câu hỏi trong file CHECKLIST.

## Đưa lên chạy thật trên MONA Cloud

Khi đã thử ưng ý trên máy tính, anh chị nên đưa trợ lý lên máy chủ MONA Cloud để nó chạy suốt ngày đêm thay vì phải bật máy tính liên tục. MONA Cloud cho thuê VPS theo giờ chỉ từ 550đ/giờ, tính chi tiết theo cấu hình như CPU 250đ/core/giờ, RAM 150đ/GB/giờ, ổ cứng 15đ/GB/giờ. Anh chị dùng bao nhiêu trả bấy nhiêu, thanh toán bằng tiền Việt Nam Đồng, có xuất hoá đơn VAT. Khi nào không muốn dùng, anh chị tắt máy là hệ thống ngừng tính tiền. Đặc biệt, toàn bộ dữ liệu công nợ nằm hoàn toàn trên máy chủ của anh chị đặt tại Việt Nam. Nút bấm "Dùng ngay" trên website hiện đang là bản thử nghiệm và sẽ sớm mở để anh chị triển khai nhanh chóng.

## Giới hạn tụi em nói trước

Tụi em muốn nói rõ những thứ trợ lý chưa làm được để anh chị nắm thông tin. Thứ nhất, hệ thống OpenClaw hiện chưa có cầu nối sang Zalo OA, tụi em đang làm nên tạm thời trợ lý chỉ nhắn tin qua Telegram. Thứ hai, anh chị cần tự cung cấp key model AI riêng vì MONA chưa cung cấp model tích hợp sẵn. Thứ ba, trợ lý được thiết lập nguyên tắc rất nghiêm là không bao giờ tự quyết định những việc tốn tiền hay nhạy cảm. Việc xoá nợ hay gửi email đòi tiền đều phải chờ anh chị nhắn tin đồng ý thì nó mới dám làm.

## Anh chị đang là khách MONA?

The MONA Group thành lập từ năm 2016, đã thực hiện hơn 14.000 dự án và tự hào có 85% khách hàng quay lại. Nếu anh chị đang sử dụng website hay phần mềm do tụi em xây dựng, anh chị có thể chọn gói Doanh nghiệp để triển khai. Đội ngũ kỹ thuật sẽ gắn thẳng trợ lý AI này vào hạ tầng phần mềm hiện tại của anh chị, dữ liệu liên thông trực tiếp với hệ thống sẵn có. Anh chị cứ gọi số tổng đài 1900 636 648 để tụi em tư vấn chi tiết.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/mona-software/mona-agent-templates
