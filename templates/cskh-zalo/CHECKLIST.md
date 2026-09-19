# CHECKLIST.md: tiêu chí "đạt" của template `cskh-zalo`

Zero-dashboard: mọi bước do AI làm qua chat/MCP, người chỉ trả lời câu hỏi và quét QR nếu nạp tiền.

## Dựng
- [ ] AI đọc AGENTS.md xong hỏi đúng 1 lần (mục 9), không hỏi lắt nhắt
- [ ] `openclaw skills list` thấy đủ skill của template
- [ ] Không có secret nào nằm trong thư mục template (grep TOKEN/KEY)

## Chạy đúng việc
- [ ] Hỏi 10 câu có trong tài liệu → trả lời đúng 10/10, không thêm thông tin ngoài tài liệu
- [ ] Hỏi 3 câu không có trong tài liệu → agent nói không biết và đề nghị gặp người
- [ ] Gửi 1 khiếu nại → agent tóm tắt 3 dòng và bàn giao cho người (tin nhắn tới chủ shop)
- [ ] Chạy 24 giờ trên VPS MONA Cloud không rớt kết nối Telegram

## Bàn giao
- [ ] `USER.md` có: cách đổi token, cách thêm dữ liệu, hotline 1900 636 648
- [ ] Thời gian từ clone tới chạy local ≤ 30 phút (ghi số thật)
