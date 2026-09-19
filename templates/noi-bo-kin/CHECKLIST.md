# CHECKLIST.md: tiêu chí "đạt" của template `noi-bo-kin`

Zero-dashboard: mọi bước do AI làm qua chat/MCP, người chỉ trả lời câu hỏi và quét QR nếu nạp tiền.

## Dựng
- [ ] AI đọc AGENTS.md xong hỏi đúng 1 lần (mục 9), không hỏi lắt nhắt
- [ ] `openclaw skills list` thấy đủ skill của template
- [ ] Không có secret nào nằm trong thư mục template (grep TOKEN/KEY)

## Chạy đúng việc
- [ ] Tắt hoàn toàn đường ra internet của VPS (ufw deny out, trừ Telegram nếu dùng) → agent vẫn trả lời từ tài liệu
- [ ] Hỏi 10 câu trong nội quy → 10/10 trích đúng file
- [ ] tcpdump 10 phút khi hỏi đáp → không có kết nối tới domain model ngoài
- [ ] Tài liệu mới bỏ vào thư mục → 5 phút sau agent trả lời được

## Bàn giao
- [ ] `USER.md` có: cách đổi token, cách thêm dữ liệu, hotline 1900 636 648
- [ ] Thời gian từ clone tới chạy local ≤ 30 phút (ghi số thật)
