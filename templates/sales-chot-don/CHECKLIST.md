# CHECKLIST.md: tiêu chí "đạt" của template `sales-chot-don`

Zero-dashboard: mọi bước do AI làm qua chat/MCP, người chỉ trả lời câu hỏi và quét QR nếu nạp tiền.

## Dựng
- [ ] AI đọc AGENTS.md xong hỏi đúng 1 lần (mục 9), không hỏi lắt nhắt
- [ ] `openclaw skills list` thấy đủ skill của template
- [ ] Không có secret nào nằm trong thư mục template (grep TOKEN/KEY)

## Chạy đúng việc
- [ ] Khách hỏi giá 1 món → báo giá đúng bảng giá, có tổng và phí ship
- [ ] Khách chốt → agent tạo QR đúng số tiền, nội dung có mã đơn
- [ ] Bắn giao dịch sandbox MONA Pay khớp mã đơn → agent báo 'đã nhận' trong 30 giây cho khách và chủ
- [ ] Giao dịch lệch số tiền → agent KHÔNG xác nhận, báo chủ kiểm

## Bàn giao
- [ ] `USER.md` có: cách đổi token, cách thêm dữ liệu, hotline 1900 636 648
- [ ] Thời gian từ clone tới chạy local ≤ 30 phút (ghi số thật)
