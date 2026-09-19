# Soát hợp đồng: Trợ lý AI đọc và báo rủi ro hợp đồng cho doanh nghiệp không có pháp chế riêng

Mỗi lần đối tác gửi bản hợp đồng vài chục trang, anh chị lại mỏi mắt dò từng dòng xem có bị ép điều khoản phạt hay không. Việc này ngốn nhiều giờ đồng hồ, mà đôi khi đọc mệt quá lại sót những chữ nhỏ xíu lắt léo về bồi thường. Trợ lý AI này sinh ra để làm đúng một việc là đọc thay anh chị, nhặt ra những chỗ bất lợi, và điền thông tin vào mẫu có sẵn của công ty. Anh chị chỉ cần đọc báo cáo tóm tắt của nó và quyết định có ký hay không.

## Agent này làm gì mỗi ngày

- Đọc hợp đồng đối tác gửi qua Telegram: Anh chị thả một file PDF hoặc Word vào nhóm chat, trợ lý sẽ đọc và so với danh sách "điều khoản đỏ" mà anh chị đã dạy từ trước.
- Cảnh báo rủi ro: Nó liệt kê từng chỗ lệch so với ý muốn của anh chị, trích nguyên văn câu chữ đó ra và xếp mức độ rủi ro (ví dụ: "Điều 5.2 quy định phạt 20% là cao hơn mức 8% công ty mình quy định, rủi ro cao").
- Điền hợp đồng theo mẫu công ty: Khi cần ký với khách mới, anh chị gửi thông tin cơ bản, nó sẽ tự nhặt chữ bỏ vào đúng chỗ trống trong mẫu hợp đồng chuẩn của nhà mình.
- Đánh dấu chỗ cần người duyệt: Nó không tự sinh điều khoản pháp lý mới, mà chỉ tô màu những chỗ cần anh chị hoặc luật sư thật xem lại.

## Ai nên dùng, ai đừng dùng

- Nên dùng: Các công ty nhỏ và vừa ký khoảng 5 đến 30 hợp đồng mỗi tháng, không có nhân viên pháp chế ngồi trực riêng, người chủ hoặc giám đốc đang phải tự mình cày ải đọc từng chữ.
- Đừng dùng: Các tập đoàn có quy trình duyệt hợp đồng qua nhiều phòng ban, hoặc các văn phòng luật sư cần suy luận pháp lý phức tạp. Trợ lý này chỉ đối chiếu theo quy tắc anh chị dạy, nó không thay thế được luật sư.

## Cần chuẩn bị gì trước

- Mẫu hợp đồng chuẩn của công ty anh chị (chép vào file sample-data/mau-hop-dong-dich-vu.md).
- Danh sách những điều khoản mà anh chị kiên quyết không chấp nhận hoặc cần chú ý (chép vào file sample-data/dieu-khoan-do.md).
- Một token bot Telegram để trợ lý nhắn tin.
- Key của các mô hình ngôn ngữ hoặc máy tính cài sẵn Ollama để chạy tại chỗ.
- Khoảng 10 phút để thiết lập.

## Dựng thử trong 5 phút

Anh chị không cần rành kỹ thuật, phần khó cứ để AI làm, anh chị chỉ cần làm theo các bước sau:
1. Tải thư mục chứa template này về máy tính của anh chị.
2. Mở Claude Code (hoặc Codex, Gemini) ngay trong thư mục vừa tải.
3. Yêu cầu AI đọc file AGENTS.md để nó hiểu cách hoạt động.
4. Trả lời câu hỏi: AI sẽ hỏi anh chị vài thông tin như token bot Telegram, anh chị cứ cung cấp cho nó.
5. Chạy local: AI sẽ tự cài môi trường OpenClaw và chạy thử trợ lý ngay trên máy tính của anh chị.
6. Thử câu trong CHECKLIST: Khi trợ lý lên tiếng, anh chị gửi thử một file hợp đồng vào Telegram xem nó phân tích có đúng ý không.

## Đưa lên chạy thật trên MONA Cloud

Khi chạy thử ưng ý, anh chị có thể đẩy trợ lý lên chạy ổn định trên VPS của MONA Cloud. Chi phí thuê máy ảo tính theo giờ chỉ từ 550đ/giờ (tắt máy là ngừng tính tiền), thanh toán bằng tiền Việt, xuất hoá đơn VAT 10%, và dữ liệu hoàn toàn nằm trên máy của anh chị ở Việt Nam. Hiện tại nút bấm "Dùng ngay" 1 click trên web đang là bản thử nghiệm, tụi em sẽ sớm mở chính thức.

## Giới hạn tụi em nói trước

- Cầu nối Zalo hiện chưa có, anh chị cần dùng Telegram hoặc WebChat.
- MONA AI chưa mở nên anh chị cần tự gắn key mô hình ngôn ngữ của mình vào, hoặc dùng gói Kín chạy bằng Ollama tại chỗ.
- Trợ lý không tự quyết việc tốn tiền hay tự ý chốt hợp đồng thay anh chị.

## Anh chị đang là khách MONA?

Với các anh chị đang dùng phần mềm hoặc website do tụi em thiết kế, gói Doanh nghiệp có thể gắn thẳng trợ lý này vào hệ thống nội bộ hiện tại. Hãy gọi cho tụi em qua tổng đài 1900 636 648 để được tư vấn thêm. The MONA Group thành lập từ 2016, đã làm hơn 14.000 dự án với 85% khách hàng quay lại, luôn mong được đồng hành cùng anh chị.

MONA Agent thuộc nhóm MONA Cloud (The MONA Group). Kho template: github.com/themonagroup/mona-agent-templates
