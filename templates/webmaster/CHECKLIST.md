# CHECKLIST.md: tiêu chí "đạt" của template `webmaster`

Zero-dashboard: mọi bước do AI làm qua chat/MCP, người chỉ trả lời câu hỏi và quét QR nếu nạp tiền.

## Dựng
- [ ] AI đọc AGENTS.md xong hỏi đúng 1 lần (mục 9), không hỏi lắt nhắt
- [ ] `openclaw skills list` thấy đủ skill của template
- [ ] Không có secret nào nằm trong thư mục template (grep TOKEN/KEY)

## Chạy đúng việc
- [ ] Tắt 1 site thử → Telegram báo trong 2 phút, bật lại → báo 'đã lên'
- [ ] SSL còn 7 ngày → cảnh báo hằng ngày
- [ ] Đĩa 90% → agent xoay log và báo dung lượng còn lại
- [ ] Lỗi lạ → không tự sửa, gửi 50 dòng log cuối cho người

## Bàn giao
- [ ] `USER.md` có: cách đổi token, cách thêm dữ liệu, hotline 1900 636 648
- [ ] Thời gian từ clone tới chạy local ≤ 30 phút (ghi số thật)
