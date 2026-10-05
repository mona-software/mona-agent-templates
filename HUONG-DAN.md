# Tự dựng trợ lý AI riêng bằng Claude Code từ template MONA Agent trong 30 phút

Đã khuya muộn, điện thoại vẫn sáng đèn báo tin nhắn, anh chị lại cặm cụi gõ từng dòng báo giá cho khách để không lỡ đơn. Template này được sinh ra để AI tự dựng một trợ lý thay anh chị làm việc ngày đêm, anh chị chỉ cần ngồi trả lời các câu hỏi của hệ thống.

## MONA Agent là gì, và không phải là gì

MONA Agent là một kho template trợ lý AI. Mỗi template đóng vai trò là một thư mục chứa các file văn bản hướng dẫn và công cụ, để AI đọc hiểu và tự dựng thành trợ lý hoàn chỉnh chạy ngay trên máy tính của anh chị hoặc máy chủ MONA Cloud. Công cụ này KHÔNG phải là một chatbot dạng dịch vụ mà anh chị thuê đóng tiền hàng tháng. Đây cũng KHÔNG phải là dịch vụ lưu giữ dữ liệu của anh chị.

## Hai lời hứa tụi em tách bạch

Tụi em cam kết dữ liệu luôn nằm trên máy chủ của anh chị, áp dụng cho mọi gói. Kế tiếp, việc không có bất kỳ byte dữ liệu nào rời khỏi máy chủ CHỈ đúng ở gói Kín chạy mô hình AI tại chỗ. Với các gói thường, câu hỏi vẫn đi ra ngoài để các mô hình thông minh xử lý qua API, nhưng dữ liệu hoàn toàn không bị lưu lại và không bị đem đi huấn luyện.

## Chọn template nào

| Template | Trợ lý làm gì | Hợp với ai |
| :--- | :--- | :--- |
| `cskh-zalo` | Trả lời khách 24/7 từ tài liệu của shop, ca khó chuyển cho người. | Cửa hàng có nhiều khách nhắn tin hỏi đáp. |
| `sales-chot-don` | Hỏi nhu cầu, báo giá, dùng API ngân hàng và dịch vụ xác nhận thanh toán tự động MONA Pay để tạo QR, tiền vào là báo chủ. | Shop bán lẻ, doanh nghiệp thương mại. |
| `ke-toan-hddt` | Tiền vào tài khoản là ghi sổ, nhắc công nợ, chuẩn bị dữ liệu xuất hoá đơn. | Công ty cần tự động hoá khâu chứng từ. |
| `content-seo` | Viết bài theo giọng thương hiệu, tự soát lỗi văn AI, chờ người duyệt rồi mới đăng. | Đội ngũ marketing, người làm website. |
| `noi-bo-kin` | Đọc tài liệu công ty để trả lời nhân viên, model chạy tại chỗ, không byte nào rời server. | Doanh nghiệp có tài liệu mật cần giữ kín. |
| `tro-giang-academy` | Giải đáp bài học, nhắc hạn nộp bài, tổng hợp câu hỏi học viên cho giảng viên. | Trung tâm đào tạo, người dạy online. |
| `tuyen-dung` | Đọc CV, chấm theo tiêu chí, hẹn lịch phỏng vấn, trả lời ứng viên 24/7. | Phòng nhân sự, công ty tuyển dụng nhiều. |
| `quan-tri-so` | Hỏi công ty mình một câu khó, nhận câu trả lời kèm số lấy từ database thật. | Chủ doanh nghiệp cần xem số liệu nhanh. |
| `webmaster` | Canh website 24/7 xem có sập, lỗi, hết SSL, backup rồi báo Telegram và tự xử ca đơn giản. | Người quản lý website, công ty có web lớn. |
| `remarketing-email` | Giỏ bỏ dở, lead im lặng, khách cũ lâu không mua thì tự gửi đúng thư qua MONA Mail. | Doanh nghiệp muốn chăm sóc lại khách cũ. |
| `nhac-lich-hen` | Xác nhận lịch, nhắc trước 24 giờ, đổi lịch qua chat. | Spa, phòng khám, salon làm đẹp. |
| `don-hang-van-chuyen` | Đơn đi tới đâu khách biết tới đó, hoàn hàng và trễ giao có người xử ngay. | Shop online gửi nhiều hàng qua bưu cục. |
| `phap-che-hop-dong` | Đọc hợp đồng, chỉ điều khoản bất lợi, soạn theo mẫu công ty, luôn để người quyết. | Công ty hay làm việc với hợp đồng. |
| `mua-domain-cho-khach` | AI tra tên, giữ chỗ, mua tên miền, trỏ DNS, canh hạn gia hạn cho từng khách. | Công ty thiết kế web, agency dịch vụ. |

## Chuẩn bị 10 phút

Anh chị cần mở phần mềm Claude Code hoặc công cụ Codex/Gemini CLI lên trước. Sau đó, anh chị chuẩn bị một tài khoản Telegram và tìm @BotFather để tạo bot. Kế tiếp, anh chị cần khoá kết nối của một mô hình loại OpenAI-compatible hoặc một máy tính đang chạy phần mềm Ollama. Anh chị gom các dữ liệu riêng cần dạy cho AI thành file văn bản. Cuối cùng, anh chị cử 1 người làm "người duyệt" để hỗ trợ trợ lý thời gian đầu.

## 30 phút dựng

Bước 1: Anh chị mở giao diện dòng lệnh trên máy tính lên. Sau đó, anh chị gõ lệnh `git clone https://github.com/mona-software/mona-agent-templates` để tải bộ thư mục về máy. Lệnh này giúp chép nguyên bản toàn bộ kho mã nguồn.

Bước 2: Khi máy tính tải xong, anh chị tìm đến thư mục template vừa lưu về. Tiếp theo, anh chị khởi động phần mềm Claude Code ngay bên trong không gian thư mục này. Thao tác này giúp AI nhận diện đúng nơi bắt đầu làm việc.

Bước 3: Mọi thứ đã sẵn sàng để anh chị ra lệnh. Anh chị gõ câu lệnh "Đọc AGENTS.md rồi dựng agent này cho tôi" để yêu cầu AI thực thi. AI sẽ đọc file hướng dẫn định sẵn và tự lên kế hoạch làm việc cho đúng cấu trúc.

Bước 4: Lúc này hệ thống sẽ đưa ra một số câu hỏi duy nhất 1 lần để thu thập thêm thông tin. Anh chị chỉ cần đọc kỹ và cung cấp các thông tin mà AI yêu cầu. Quá trình trao đổi này diễn ra hoàn toàn giống như lúc hai người trò chuyện.

Bước 5: Nhận đủ thông tin, AI sẽ tự cài đặt hệ thống OpenClaw vào máy. AI tự trỏ không gian làm việc, cấu hình mô hình và kết nối Telegram. Anh chị chỉ việc ngồi theo dõi các thao tác đang chạy mà không phải gõ gì thêm.

Bước 6: Khi cài đặt xong, anh chị lấy điện thoại nhắn tin cho con bot Telegram đã tạo. Sau đó, anh chị quay lại màn hình máy tính để duyệt quyền ghép đôi. Từ lúc này, trợ lý AI và ứng dụng chat của anh chị đã chính thức nhận nhau.

Bước 7: Để chắc chắn không xảy ra sai sót, anh chị yêu cầu AI kiểm tra lại hệ thống. Anh chị cho chạy lệnh kiểm tra file CHECKLIST.md để rà soát toàn bộ. File này đóng vai trò như bảng danh sách các đầu mục bắt buộc.

Bước 8: Giọng điệu giao tiếp mặc định đôi khi chưa phù hợp với thương hiệu của anh chị. Nếu muốn trợ lý nói chuyện mềm mỏng hơn, anh chị mở file SOUL.md ra. Tại file này, anh chị thoải mái tinh chỉnh lại giọng văn theo sở thích.

## Đưa lên MONA Cloud để chạy 24/7

Khi trợ lý đã chạy ổn định, anh chị đưa lên mạng để nó túc trực 24/7. Trợ lý AI tự gọi công cụ monacloud-mcp tạo máy chủ ảo từ 550đ/giờ. Hệ thống báo giá chi tiết, anh chị duyệt thì AI mới làm bước tiếp theo. Kế đó, anh chị nạp tiền vào ví bằng mã VietQR do AI in ra. Khi anh chị tắt máy thì hệ thống ngừng tính phí, và tụi em xuất hoá đơn VAT đầy đủ. Nút bấm "Dùng ngay" bằng 1 click trên trang monagent.vn đang là bản thử nghiệm, tụi em sẽ mở sau.

## Sửa và lớn dần

Không gian làm việc này hoàn toàn thuộc về anh chị. Trong lúc dùng, anh chị tự do thêm kỹ năng mới hoặc thêm tài liệu vào để trợ lý giỏi việc hơn. Anh chị đưa thư mục này lên kho git riêng tư để sao lưu.

## Kẹt thì gọi ai

Anh chị gọi số 1900 636 648 hoặc gửi thư vào info@themona.global để tụi em hỗ trợ. Với anh chị đang là khách quen của MONA, tụi em có gói Doanh nghiệp gắn trực tiếp trợ lý vào phần mềm MONA đã dựng. Công ty The MONA Group mở cửa năm 2016, hoàn thành hơn 14.000 dự án và có 85% khách hàng quay lại.

## Câu hỏi hay gặp

Chi phí tốn bao nhiêu: Anh chị trả tiền thuê máy chủ từ 550đ/giờ và phí gọi API theo mức dùng thực tế.
Có cần rành code không: Anh chị không cần biết code, toàn bộ việc cài đặt đã có AI lo.
Dữ liệu có bị lộ không: Dữ liệu nằm ở máy anh chị, gói thường thì câu hỏi vẫn đi ra model qua API nhà cung cấp anh chị chọn (không lưu, không train), gói Kín chạy model tại chỗ thì không byte nào rời server.
Zalo đã dùng được chưa: OpenClaw hiện chưa có Zalo, cầu nối Zalo OA MONA vẫn đang làm.
Đổi model khác được không: Anh chị đổi thoải mái, chỉ cần chỉnh cấu hình trong file cài đặt.
Khác chatbot thuê tháng chỗ nào: Anh chị nắm giữ mã nguồn và trả tiền theo tài nguyên sử dụng thật.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group): monacloud.vn · monamail.vn · monapay.vn · monadomain.vn.
