# AGENTS.md: Mua domain cho khách (template MONA Agent `mua-domain-cho-khach`)

> File này viết cho AI (Claude Code, Codex, Gemini CLI) đọc để DỰNG và CHỈNH agent này cho một người cụ thể. Người đọc thì xem `README.md`. Khi chạy trên OpenClaw, chính file này là "operating instructions" của agent (nạp mỗi phiên).

## 1. Agent này làm gì
Agency: AI tra tên, giữ chỗ, mua .vn, trỏ DNS, canh hạn gia hạn cho từng khách. Người dùng: agency web, freelancer làm web cho nhiều khách. Kênh: Telegram · Claude Code (gọi MCP trực tiếp).

## 2. Stack bắt buộc (không tự đổi)
- Runtime: OpenClaw (MIT). Workspace = thư mục template này. Persona ở `SOUL.md`, tên ở `IDENTITY.md`, skill ở `skills/`.
- Model: người dùng cấp key OpenAI-compatible (OpenAI, Gemini, Anthropic, hoặc Ollama local) qua `models.providers` trong `~/.openclaw/openclaw.json`. MONA AI (API trả VND) chưa mở; khi mở chỉ đổi `baseUrl` + `apiKey`.
- Hạ tầng: chạy local để thử, chạy thật trên VPS MONA Cloud (xem `deploy.md`). Sản phẩm MONA dùng trong template: MONA Domain, MONA Cloud.
- Dữ liệu riêng của người dùng: danh sách khách + domain (sample-data/khach-domain.csv). Dữ liệu chỉ nằm trong workspace trên máy/VPS của họ.

## 3. Tool MCP được phép gọi khi dựng/vận hành (tên THẬT, 19/09/2026)
`cloud_whoami`, `cloud_balance`, `cloud_prices`, `cloud_packages`, `cloud_vps_create`, `cloud_services`, `cloud_job_status`, `cloud_topup`, `cloud_topup_status`, `cloud_domain_search`, `cloud_domain_reserve`, `cloud_domain_reserve_status`, `cloud_domain_buy`, `cloud_domain_claim`, `cloud_domain_registrant_set`, `cloud_domain_verify_start`, `cloud_domain_verify_status`, `cloud_domain_dns_add`, `cloud_domain_dns_list`, `cloud_domain_ns_set`, `cloud_domain_renew`, `cloud_domain_health`, `cloud_domain_list`, `cloud_domain_webhook_set`

Tool không có trong `tools.json` thì không tồn tại. `cloud_agent_deploy` hiện trả stub; đừng hứa 1 click với người dùng.

## 4. API agent gọi lúc chạy
- monacloud-mcp cloud_domain_* (28 tool thật)

## 5. Biến môi trường (đặt trong `~/.openclaw/openclaw.json` mục `env.vars` hoặc file `.env` của VPS, KHÔNG commit)
- `MONACLOUD_TOKEN`
- `TELEGRAM_BOT_TOKEN`

## 6. Skill
- `skills/tra-va-giu-domain/SKILL.md`: Tra 5 biến thể tên, báo giá VND, giữ chỗ (reserve) cho khách duyệt, mua khi khách gật; .vn cần bản khai + eKYC do khách làm 1 lần.
- `skills/canh-han-gia-han/SKILL.md`: Mỗi sáng kiểm domain sắp hết hạn 30/7/1 ngày, nhắc khách, gia hạn khi khách duyệt, không tự gia hạn.

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
