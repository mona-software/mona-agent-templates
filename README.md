# MONA Agent: kho template trợ lý AI chạy trên server của anh chị

> MONA Agent là dịch vụ dựng trợ lý AI riêng thuộc MONA Cloud (The MONA Group): anh chị lấy template về, mở bằng Claude Code (hoặc Codex, Gemini CLI), AI đọc `AGENTS.md` rồi dựng trợ lý chạy trên máy anh chị hoặc trên VPS MONA Cloud tại Việt Nam, đọc được tài liệu của riêng mình, nhắn qua Telegram (Zalo khi có cầu nối), dữ liệu nằm trên máy của anh chị, trả bằng VND. Nút "Dùng ngay" 1 click trên [monagent.vn](https://monagent.vn) đang là bản thử, sẽ mở sau.

MONA Agent thuộc **nhóm monacloud**: dùng chung MONA Pass (1 tài khoản), ví VND và MCP `monacloud-mcp` với [MONA Cloud](https://monacloud.vn) · [MONA Mail](https://monamail.vn) · [MONA Pay](https://monapay.vn) · [MONA Domain](https://monadomain.vn) · [MONA Base](https://monabase.vn) · [MONA eInvoice](https://monaeinvoice.vn).

## Bắt đầu trong 30 phút

```bash
git clone https://github.com/themonagroup/mona-agent-templates
cd mona-agent-templates/templates/cskh-zalo
claude   # rồi gõ: "Đọc AGENTS.md rồi dựng agent này cho tôi"
```

Hướng dẫn đầy đủ cho người không rành kỹ thuật: [HUONG-DAN.md](HUONG-DAN.md). Runtime: [OpenClaw](https://github.com/openclaw/openclaw) (MIT). Catalog máy đọc: [catalog.json](catalog.json) (MCP `agent_templates_list` / `agent_templates_get`).

## 14 template

| Template | Tên | Làm gì | Đồ MONA dùng |
|---|---|---|---|
| [`cskh-zalo`](templates/cskh-zalo/) | CSKH Zalo / Telegram | Trả lời khách 24/7 từ tài liệu của shop, ca khó chuyển cho người. | MONA Cloud, MONA Mail |
| [`sales-chot-don`](templates/sales-chot-don/) | Sales chốt đơn | Hỏi nhu cầu, báo giá, tạo QR chuyển khoản MONA Pay, tiền vào là báo chủ. | MONA Pay, MONA Cloud, MONA Mail |
| [`ke-toan-hddt`](templates/ke-toan-hddt/) | Kế toán hoá đơn | Tiền vào tài khoản là ghi sổ, nhắc công nợ, chuẩn bị dữ liệu xuất hoá đơn. | MONA Pay, MONA Mail, MONA eInvoice (API dev chưa mở: phần xuất hoá đơn hiện là chuẩn bị dữ liệu, chưa tự phát hành) |
| [`content-seo`](templates/content-seo/) | Content SEO có gate | Viết bài theo giọng thương hiệu, tự soát lỗi văn AI, chờ người duyệt rồi mới đăng. | MONA Cloud |
| [`noi-bo-kin`](templates/noi-bo-kin/) | Trợ lý nội bộ kín | Đọc tài liệu công ty để trả lời nhân viên, model chạy tại chỗ, không byte nào rời server. | MONA Cloud (VPS RAM lớn), Ollama |
| [`tro-giang-academy`](templates/tro-giang-academy/) | Trợ giảng lớp online | Giải đáp bài học, nhắc hạn nộp bài, tổng hợp câu hỏi học viên cho giảng viên. | MONA Cloud, MONA Mail, mona.academy (MCP https://mcp-elearing.mona.academy/mcp: chạy tools/list để lấy tên tool thật trước khi dùng) |
| [`tuyen-dung`](templates/tuyen-dung/) | Trợ lý tuyển dụng | Đọc CV, chấm theo tiêu chí, hẹn lịch phỏng vấn, trả lời ứng viên 24/7. | MONA Mail, MONA Cloud |
| [`quan-tri-so`](templates/quan-tri-so/) | Trợ lý quản trị bằng số | Hỏi công ty mình một câu khó, nhận câu trả lời kèm số lấy từ database thật. | MONA Cloud (Postgres theo giờ) |
| [`webmaster`](templates/webmaster/) | Trực website | Canh website 24/7: sập, lỗi, hết SSL, backup; báo Telegram và tự xử ca đơn giản. | MONA Cloud |
| [`remarketing-email`](templates/remarketing-email/) | Email theo sự kiện | Giỏ bỏ dở, lead im lặng, khách cũ lâu không mua: đúng lúc gửi đúng thư qua MONA Mail. | MONA Mail, MONA Cloud |
| [`nhac-lich-hen`](templates/nhac-lich-hen/) | Nhắc lịch hẹn | Spa, phòng khám, salon: xác nhận lịch, nhắc trước 24 giờ, đổi lịch qua chat. | MONA Mail, MONA Cloud |
| [`don-hang-van-chuyen`](templates/don-hang-van-chuyen/) | Theo dõi đơn vận chuyển | Đơn đi tới đâu khách biết tới đó, hoàn hàng và trễ giao có người xử ngay. | MONA Mail, MONA Cloud |
| [`phap-che-hop-dong`](templates/phap-che-hop-dong/) | Soát hợp đồng | Đọc hợp đồng, chỉ điều khoản bất lợi, soạn theo mẫu công ty, luôn để người quyết. | MONA Cloud |
| [`mua-domain-cho-khach`](templates/mua-domain-cho-khach/) | Mua domain cho khách | Agency: AI tra tên, giữ chỗ, mua .vn, trỏ DNS, canh hạn gia hạn cho từng khách. | MONA Domain, MONA Cloud |

## Một template gồm gì

```
templates/<ten>/
├── README.md        # cho NGƯỜI: làm gì, cho ai, cần gì, 5 phút dựng thử
├── AGENTS.md        # cho AI: mục tiêu, stack bắt buộc, bước dựng, chỗ hỏi người
├── SOUL.md          # tính cách, giọng, ranh giới (OpenClaw nạp mỗi phiên)
├── IDENTITY.md      # tên, emoji
├── skills/<x>/SKILL.md  # từng việc, frontmatter name + description
├── tools.json       # tool MCP thật được phép gọi + API lúc chạy + env
├── deploy.md        # chạy local rồi lên VPS MONA Cloud
├── sample-data/     # dữ liệu mẫu để thử, thay bằng dữ liệu thật
└── CHECKLIST.md     # tiêu chí "đạt", test bằng chat, không cần bảng điều khiển
```

## Hai lời hứa, nói tách bạch

1. **Dữ liệu nằm trên server của anh chị**: đúng với mọi gói. Tài liệu, lịch sử chat, trí nhớ agent ở máy hoặc VPS riêng; xoá là mất thật.
2. **Không một byte rời server**: chỉ đúng ở gói Kín (template `noi-bo-kin`, model mở chạy tại chỗ bằng Ollama). Gói thường: dữ liệu ở server riêng nhưng câu hỏi và ngữ cảnh cần thiết vẫn đi ra model xịn qua API của nhà cung cấp anh chị chọn.

## Anh chị đang là khách MONA?

Gói Doanh nghiệp: MONA gắn trợ lý thẳng vào web, phần mềm, database MONA đã dựng cho anh chị, lo triển khai và vận hành. Gọi **1900 636 648** hoặc email info@themona.global.

## Giấy phép

MIT. Tên tool trong `tools.json` lấy từ mã nguồn `monacloud-mcp` và `monapay-mcp` ngày 19/09/2026. The MONA Group, từ 2016, 14.000+ dự án, 85% khách quay lại.
