# CHECKLIST.md: tiêu chí "đạt" của template `nhac-lich-hen`

Zero-dashboard: mọi bước do AI làm qua chat/MCP, người chỉ trả lời câu hỏi và quét QR nếu nạp tiền.

## Dựng
- [ ] AI đọc AGENTS.md xong hỏi đúng 1 lần (mục 9), không hỏi lắt nhắt
- [ ] `openclaw skills list` thấy đủ skill của template
- [ ] Không có secret nào nằm trong thư mục template (grep TOKEN/KEY)

## Chạy đúng việc
- [ ] Thêm 1 lịch ngày mai → xác nhận gửi ngay, nhắc đúng 24 giờ và 2 giờ trước
- [ ] Khách nhắn 'đổi qua chiều' → nhận 3 khung trống, chọn 1 → lịch đổi, lễ tân nhận báo
- [ ] Huỷ trong vòng 4 giờ → agent nêu quy tắc, chuyển lễ tân quyết
- [ ] Không gửi nhắc cho lịch đã huỷ

## Bàn giao
- [ ] `USER.md` có: cách đổi token, cách thêm dữ liệu, hotline 1900 636 648
- [ ] Thời gian từ clone tới chạy local ≤ 30 phút (ghi số thật)
