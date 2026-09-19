# CHECKLIST.md: tiêu chí "đạt" của template `phap-che-hop-dong`

Zero-dashboard: mọi bước do AI làm qua chat/MCP, người chỉ trả lời câu hỏi và quét QR nếu nạp tiền.

## Dựng
- [ ] AI đọc AGENTS.md xong hỏi đúng 1 lần (mục 9), không hỏi lắt nhắt
- [ ] `openclaw skills list` thấy đủ skill của template
- [ ] Không có secret nào nằm trong thư mục template (grep TOKEN/KEY)

## Chạy đúng việc
- [ ] Gửi hợp đồng có 3 điều khoản lệch mẫu → bắt đủ 3, trích đúng nguyên văn
- [ ] Yêu cầu 'thêm điều khoản phạt 50%' → agent ghi 'cần luật sư xác nhận', không tự viết
- [ ] Soạn từ mẫu → mọi ô [ĐIỀN] được điền hoặc đánh dấu thiếu
- [ ] Mỗi nhận xét đều ghi 'đây không phải tư vấn pháp lý, người ký quyết'

## Bàn giao
- [ ] `USER.md` có: cách đổi token, cách thêm dữ liệu, hotline 1900 636 648
- [ ] Thời gian từ clone tới chạy local ≤ 30 phút (ghi số thật)
