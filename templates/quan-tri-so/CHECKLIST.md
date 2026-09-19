# CHECKLIST.md: tiêu chí "đạt" của template `quan-tri-so`

Zero-dashboard: mọi bước do AI làm qua chat/MCP, người chỉ trả lời câu hỏi và quét QR nếu nạp tiền.

## Dựng
- [ ] AI đọc AGENTS.md xong hỏi đúng 1 lần (mục 9), không hỏi lắt nhắt
- [ ] `openclaw skills list` thấy đủ skill của template
- [ ] Không có secret nào nằm trong thư mục template (grep TOKEN/KEY)

## Chạy đúng việc
- [ ] User DB chỉ SELECT → agent thử UPDATE bị từ chối, agent báo đúng
- [ ] Hỏi 'doanh thu tháng này so với tháng trước' → số khớp SQL chạy tay
- [ ] Hỏi câu mơ hồ → agent hỏi lại 1 câu rồi mới chạy
- [ ] 7h30 nhận báo cáo 5 số đúng lịch

## Bàn giao
- [ ] `USER.md` có: cách đổi token, cách thêm dữ liệu, hotline 1900 636 648
- [ ] Thời gian từ clone tới chạy local ≤ 30 phút (ghi số thật)
