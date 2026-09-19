# AGENTS.md: Sales chốt đơn (template MONA Agent `sales-chot-don`)

> File này viết cho AI (Claude Code, Codex, Gemini CLI) đọc để DỰNG và CHỈNH agent này cho một người cụ thể. Người đọc thì xem `README.md`. Khi chạy trên OpenClaw, chính file này là "operating instructions" của agent (nạp mỗi phiên).

## 1. Agent này làm gì
Hỏi nhu cầu, báo giá, tạo QR chuyển khoản MONA Pay, tiền vào là báo chủ. Người dùng: shop bán qua chat, dịch vụ đặt cọc, khoá học, phòng tập. Kênh: Telegram (chạy ngay) · web chat (OpenClaw WebChat).

## 2. Stack bắt buộc (không tự đổi)
- Runtime: OpenClaw (MIT). Workspace = thư mục template này. Persona ở `SOUL.md`, tên ở `IDENTITY.md`, skill ở `skills/`.
- Model: người dùng cấp key OpenAI-compatible (OpenAI, Gemini, Anthropic, hoặc Ollama local) qua `models.providers` trong `~/.openclaw/openclaw.json`. MONA AI (API trả VND) chưa mở; khi mở chỉ đổi `baseUrl` + `apiKey`.
- Hạ tầng: chạy local để thử, chạy thật trên VPS MONA Cloud (xem `deploy.md`). Sản phẩm MONA dùng trong template: MONA Pay, MONA Cloud, MONA Mail.
- Dữ liệu riêng của người dùng: bảng giá + mẫu báo giá (sample-data/bang-gia.csv, sample-data/mau-bao-gia.md). Dữ liệu chỉ nằm trong workspace trên máy/VPS của họ.

## 3. Tool MCP được phép gọi khi dựng/vận hành (tên THẬT, 19/09/2026)
`cloud_whoami`, `cloud_balance`, `cloud_prices`, `cloud_packages`, `cloud_vps_create`, `cloud_services`, `cloud_job_status`, `cloud_topup`, `cloud_topup_status`, `monapay_quickstart`, `monapay_me`, `monapay_create_qr`, `monapay_get_transaction`, `monapay_list_transactions`, `monapay_create_webhook`, `monapay_test_webhook`, `monapay_verify_signature`, `monapay_sandbox_transaction`, `monapay_create_checkout`, `monapay_get_checkout`

Tool không có trong `tools.json` thì không tồn tại. `cloud_agent_deploy` hiện trả stub; đừng hứa 1 click với người dùng.

## 4. API agent gọi lúc chạy
- https://api.monapay.vn/api/v1: POST /api/v1/oauth/token, POST /api/v1/acb/qr-payment/generate (VietQR động theo đơn), GET /api/v1/acb/virtual-account/transactions, POST /api/v1/client-webhooks (webhook HMAC báo tiền vào), POST /api/v1/sandbox/transactions (thử), POST /api/v1/checkouts
- https://api.monamail.vn/v1: POST /v1/emails (gửi), POST /v1/templates, GET /v1/emails/{id}, POST /v1/webhooks, GET /v1/inboxes/{id}/messages (hộp thư agent), POST /v1/inboxes/{id}/messages/{mid}/reply

## 5. Biến môi trường (đặt trong `~/.openclaw/openclaw.json` mục `env.vars` hoặc file `.env` của VPS, KHÔNG commit)
- `OPENAI_COMPAT_API_KEY`
- `TELEGRAM_BOT_TOKEN`
- `MONAPAY_CLIENT_ID`
- `MONAPAY_CLIENT_SECRET`
- `MONAPAY_WEBHOOK_SECRET`

## 6. Skill
- `skills/bao-gia/SKILL.md`: Hỏi đúng 3 câu để chốt cấu hình rồi lập báo giá theo bảng giá, không giảm giá ngoài quy định.
- `skills/tao-qr-va-xac-nhan/SKILL.md`: Tạo VietQR động đúng số tiền + mã đơn qua API MONA Pay, chờ webhook tiền vào rồi xác nhận với khách và báo chủ.

## 7. Các bước dựng (AI làm, người chỉ trả lời câu hỏi)
1. Đọc `README.md` + `SOUL.md` + `skills/*/SKILL.md` + `sample-data/` để hiểu việc.
2. Hỏi người dùng đúng các câu ở mục 9, ghi câu trả lời vào `USER.md` (tạo mới) và thay `sample-data/` bằng dữ liệu thật của họ.
3. Cài OpenClaw local (`deploy.md` bước A), trỏ workspace về thư mục này, cấu hình model + kênh.
4. Chạy `openclaw skills list` để chắc skill đã nạp; chạy `openclaw agent --message "<câu thử trong CHECKLIST.md>"`.
5. Qua hết `CHECKLIST.md` ở local rồi mới lên VPS (`deploy.md` bước B).
6. Bàn giao: ghi vào `USER.md` cách đổi token, cách thêm tài liệu, số hotline MONA khi kẹt.

## 8. Chỗ được tuỳ biến / chỗ không
- Được: giọng trong `SOUL.md`, dữ liệu, ngưỡng nhắc, mẫu thư, tên agent.
- Không: bỏ bước "người duyệt" ở các hành động tốn tiền/gửi ra ngoài; tự thêm tool không có trong `tools.json`; ghi secret vào file trong repo; đổi runtime.

## 9. Điểm dừng hỏi người dùng (hỏi 1 lần, gom thành 1 tin)
- Tên agent + giọng (thân mật hay trang trọng)?
- Kênh nào trước (Telegram/web)? Token bot Telegram?
- Key model nào (OpenAI-compatible) hay chạy Ollama?
- Dữ liệu riêng: file nào thay cho `sample-data/`?
- Ai là "người duyệt" khi agent cần bàn giao (Telegram ID)?
- Chạy local trước hay lên VPS MONA Cloud ngay (ước tính từ 550đ/giờ, cần duyệt chi phí)?

## 10. Mất/đổi token thì sao
Token Telegram: tạo lại ở @BotFather → `openclaw channels add --channel telegram --token <mới>`. Key model: đổi trong `openclaw.json` → `openclaw gateway restart`. Token MONA Cloud: `cloud_link` lại bằng MONA Pass. Không có gì phải dựng lại.
