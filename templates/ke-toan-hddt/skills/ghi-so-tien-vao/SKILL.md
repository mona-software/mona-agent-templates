---
name: ghi-so-tien-vao
description: Đọc giao dịch mới từ MONA Pay, khớp với công nợ theo mã khách/mã đơn, ghi sổ và báo lệch.
---
# Ghi sổ tiền vào khi có giao dịch mới

## Khi nào dùng
- Người phụ trách yêu cầu kiểm tra tiền vào. Ví dụ: "Kiểm tra xem khách hàng mã KH001 đã chuyển khoản tiền mua hàng chưa."
- Có thông báo giao dịch mới, cần đối soát công nợ. Ví dụ: "Sáng nay có những khoản tiền nào vào, em cập nhật sổ giúp anh nhé."

## Làm theo thứ tự
1. Lấy danh sách giao dịch mới bằng cách gọi công cụ thuộc MCP `monapay-mcp` hoặc API `GET /api/v1/acb/virtual-account/transactions` của MONA Pay.
2. Đọc file `sample-data/cong-no.csv` để lấy danh sách khách và số tiền còn nợ.
3. So sánh số tiền nhận được và nội dung chuyển khoản với thông tin công nợ.
4. Nếu số tiền khớp hoàn toàn, cập nhật trạng thái đã thanh toán vào file.
5. Nếu số tiền nhận được ít hơn hoặc nhiều hơn số nợ, ghi nhận số lệch và chuẩn bị thông báo.
6. Chuẩn bị sẵn dữ liệu xuất hoá đơn điện tử. DỪNG, hỏi người phụ trách xem có muốn gửi email thông báo xác nhận thanh toán qua MONA Mail không.

## Mẫu trả lời
- "Tụi em thấy có 2 khoản tiền vào khớp với công nợ của mã KH012 và KH015, em đã cập nhật sổ. Chênh lệch là 0 đồng. Anh chị có muốn gửi email xác nhận cho 2 khách này không?"
- "Khách mã KH020 chuyển thiếu 50.000 đồng so với công nợ. Em đã ghi sổ phần tiền nhận được, phần thiếu anh chị có cần em nhắn tin hỏi lại khách không?"

## Không được làm
- Không tự ý gửi email xác nhận hoặc nhắc nợ khi chưa được người phụ trách đồng ý.
- Không tự ý xoá hay sửa mã khách trong file công nợ.
- Không phát hành hoá đơn điện tử trực tiếp vì hệ thống hiện chỉ hỗ trợ bước chuẩn bị dữ liệu.
- Không bịa thông tin giao dịch nếu API trả về không có dữ liệu.

## Kiểm tra xong việc
- Đã đọc đủ giao dịch từ MONA Pay và file công nợ.
- File công nợ đã được cập nhật đúng số tiền và trạng thái dựa trên giao dịch thật.
- Đã thông báo rõ ràng về các khoản chênh lệch cho người phụ trách.
