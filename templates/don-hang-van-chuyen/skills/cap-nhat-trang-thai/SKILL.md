---
name: cap-nhat-trang-thai
description: Mỗi 30 phút tra trạng thái vận đơn, đổi trạng thái thì báo khách 1 dòng, không spam.
---
# Cập nhật tình trạng giao hàng

## Khi nào dùng
- Khi đến lịch rà soát mỗi 30 phút cho các đơn đang vận chuyển của cửa hàng anh chị.
- Khi anh chị nhắn: "Kiểm tra xem đơn DH123 giao tới đâu rồi".
- Khi anh chị yêu cầu: "Cập nhật tình trạng các đơn ngày hôm qua nhé".

## Làm theo thứ tự
1. Đọc danh sách mã vận đơn và thông tin khách mua từ file `sample-data/don-van-chuyen.csv`.
2. Gọi API tra cứu của đơn vị vận chuyển bằng mã khóa mà anh chị đã cài đặt để lấy tình trạng mới nhất.
3. Đối chiếu tình trạng vừa nhận về với tình trạng đã lưu ở lần trước. Nếu không có gì thay đổi, kết thúc kiểm tra cho đơn đó.
4. Nếu tình trạng có thay đổi (chẳng hạn từ "đã lấy hàng" sang "đang giao"), soạn một thông báo ngắn đúng 1 dòng.
5. Gọi `POST /v1/emails` qua API của MONA Mail để gửi email thông báo này thẳng cho khách.
6. Lưu lại tình trạng mới nhất vào bộ nhớ để tụi em đối chiếu cho đợt 30 phút tiếp theo.

## Mẫu trả lời
- "Đơn hàng DH123 của anh chị đã được lấy đi và đang trên đường giao tới nhé."
- "Đơn hàng DH456 đã đến bưu cục gần nhà, anh chị chú ý điện thoại để nhận hàng nha."

## Không được làm
- Không gửi nhiều email nếu tình trạng đơn chưa thay đổi.
- Không viết email dài, chỉ báo tin đúng 1 dòng.
- Không tự bịa tình trạng đơn nếu lúc đó gọi API bị lỗi.
- Không bịa thông tin liên lạc của tổng đài hay hãng vận chuyển.

## Kiểm tra xong việc
- Đã quét qua hết toàn bộ các mã vận đơn anh chị đưa trong file.
- Những đơn vừa chuyển trạng thái đều đã được gửi email thông báo.
- Đã lưu lại tình trạng mới vào bộ nhớ.
