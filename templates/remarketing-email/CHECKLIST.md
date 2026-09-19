# CHECKLIST.md: tiêu chí "đạt" của template `remarketing-email`

Zero-dashboard: mọi bước do AI làm qua chat/MCP, người chỉ trả lời câu hỏi và quét QR nếu nạp tiền.

## Dựng
- [ ] AI đọc AGENTS.md xong hỏi đúng 1 lần (mục 9), không hỏi lắt nhắt
- [ ] `openclaw skills list` thấy đủ skill của template
- [ ] Không có secret nào nằm trong thư mục template (grep TOKEN/KEY)

## Chạy đúng việc
- [ ] Bắn sự kiện gio_bo_do → thư 'giỏ còn chờ' gửi sau 60 phút, đúng tên khách
- [ ] Cùng khách bắn 2 lần trong 7 ngày → chỉ gửi 1
- [ ] Địa chỉ bounce → không gửi nữa, có trong danh sách dừng
- [ ] Báo cáo tuần tới Telegram/email chủ đúng thứ 2

## Bàn giao
- [ ] `USER.md` có: cách đổi token, cách thêm dữ liệu, hotline 1900 636 648
- [ ] Thời gian từ clone tới chạy local ≤ 30 phút (ghi số thật)
