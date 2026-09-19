# CHECKLIST.md: tiêu chí "đạt" của template `ke-toan-hddt`

Zero-dashboard: mọi bước do AI làm qua chat/MCP, người chỉ trả lời câu hỏi và quét QR nếu nạp tiền.

## Dựng
- [ ] AI đọc AGENTS.md xong hỏi đúng 1 lần (mục 9), không hỏi lắt nhắt
- [ ] `openclaw skills list` thấy đủ skill của template
- [ ] Không có secret nào nằm trong thư mục template (grep TOKEN/KEY)

## Chạy đúng việc
- [ ] Nạp 5 giao dịch sandbox → sổ ghi đúng 5 dòng, khớp 4, báo lệch 1
- [ ] Sáng 8h nhận báo cáo công nợ quá hạn đúng danh sách
- [ ] Chủ gõ 'nhắc khách A' → mail nhắc gửi qua MONA Mail, có bản sao cho chủ
- [ ] Không tự ý gửi mail nhắc khi chủ chưa duyệt

## Bàn giao
- [ ] `USER.md` có: cách đổi token, cách thêm dữ liệu, hotline 1900 636 648
- [ ] Thời gian từ clone tới chạy local ≤ 30 phút (ghi số thật)
