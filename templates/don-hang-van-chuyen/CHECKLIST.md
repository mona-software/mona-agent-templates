# CHECKLIST.md: tiêu chí "đạt" của template `don-hang-van-chuyen`

Zero-dashboard: mọi bước do AI làm qua chat/MCP, người chỉ trả lời câu hỏi và quét QR nếu nạp tiền.

## Dựng
- [ ] AI đọc AGENTS.md xong hỏi đúng 1 lần (mục 9), không hỏi lắt nhắt
- [ ] `openclaw skills list` thấy đủ skill của template
- [ ] Không có secret nào nằm trong thư mục template (grep TOKEN/KEY)

## Chạy đúng việc
- [ ] Nạp 10 đơn mẫu, giả lập đổi trạng thái → khách nhận đúng 1 mail/1 thay đổi
- [ ] Đơn quá hạn 2 ngày → có trong danh sách sáng cho người
- [ ] Người duyệt mail xin lỗi → gửi đúng khách, có mã đơn
- [ ] Không gửi gì khi API vận chuyển lỗi, chỉ báo nhóm

## Bàn giao
- [ ] `USER.md` có: cách đổi token, cách thêm dữ liệu, hotline 1900 636 648
- [ ] Thời gian từ clone tới chạy local ≤ 30 phút (ghi số thật)
