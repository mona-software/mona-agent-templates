# CHECKLIST.md: tiêu chí "đạt" của template `mua-domain-cho-khach`

Zero-dashboard: mọi bước do AI làm qua chat/MCP, người chỉ trả lời câu hỏi và quét QR nếu nạp tiền.

## Dựng
- [ ] AI đọc AGENTS.md xong hỏi đúng 1 lần (mục 9), không hỏi lắt nhắt
- [ ] `openclaw skills list` thấy đủ skill của template
- [ ] Không có secret nào nằm trong thư mục template (grep TOKEN/KEY)

## Chạy đúng việc
- [ ] Tra 'tenkhach.vn' → trả về trống/không trống + giá VND đúng bảng MONA Domain
- [ ] Giữ chỗ → cloud_domain_reserve_status trả trạng thái, chưa trừ tiền
- [ ] Domain hết hạn trong 7 ngày (dữ liệu mẫu) → nhắc đúng khách
- [ ] Không gọi cloud_domain_buy khi chưa có xác nhận của khách

## Bàn giao
- [ ] `USER.md` có: cách đổi token, cách thêm dữ liệu, hotline 1900 636 648
- [ ] Thời gian từ clone tới chạy local ≤ 30 phút (ghi số thật)
