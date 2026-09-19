# deploy.md: chạy local rồi lên MONA Cloud (template `sales-chot-don`)

## A. Chạy local (thử trước, 0đ)
1. Cài OpenClaw (Node 24 trở lên): `curl -fsSL https://openclaw.ai/install.sh | bash` (hoặc `npm install -g openclaw@latest --allow-scripts=openclaw`).
2. Trỏ workspace về thư mục template: tạo `~/.openclaw/openclaw.json` (json5):
```json5
{
  agents: { defaults: { workspace: "/duong/dan/toi/sales-chot-don", skipBootstrap: true, model: { primary: "mona-compat/gpt-4o-mini" } } },
  models: { mode: "merge", providers: { "mona-compat": { baseUrl: "https://api.openai.com/v1", apiKey: "${OPENAI_COMPAT_API_KEY}", api: "openai-completions", models: [{ id: "gpt-4o-mini", name: "Model mặc định" }] } } },
  env: { vars: {
      OPENAI_COMPAT_API_KEY: "<điền>",
      TELEGRAM_BOT_TOKEN: "<điền>",
      MONAPAY_CLIENT_ID: "<điền>",
      MONAPAY_CLIENT_SECRET: "<điền>",
      MONAPAY_WEBHOOK_SECRET: "<điền>",
  } },
  channels: { telegram: { enabled: true, botToken: "${TELEGRAM_BOT_TOKEN}", dmPolicy: "pairing" } },
}
```
   Đổi `baseUrl`/`id` theo nhà cung cấp anh chị dùng (Gemini, Anthropic qua cổng OpenAI-compatible, hoặc Ollama `http://127.0.0.1:11434/v1`). MONA AI khi mở chỉ đổi 2 dòng này.
3. `openclaw onboard --install-daemon` → `openclaw skills list` (phải thấy bao-gia, tao-qr-va-xac-nhan) → `openclaw channels status --probe`.
4. Nhắn bot trên Telegram → `openclaw pairing list telegram` → `openclaw pairing approve telegram <CODE>`.
5. Chạy `CHECKLIST.md`. Đạt hết mới sang B.

## B. Lên VPS MONA Cloud (chạy thật 24/7)
Cách đang dùng được hôm nay (1 click `cloud_agent_deploy` còn là bản thử):
1. Trong Claude Code có `monacloud-mcp`: `cloud_whoami` → `cloud_balance` (thiếu tiền: `cloud_topup` in QR, anh chị quét) → `cloud_prices` → `cloud_vps_create` với sandbox=true để xem giá (gợi ý 1 core / 2 GB RAM cho OpenClaw; từ 550đ/giờ cho cấu hình nhỏ nhất) → anh chị duyệt → `cloud_vps_create` sandbox=false → `cloud_job_status` tới khi xong → `cloud_services` lấy IP.
2. SSH vào VPS (key có trong kết quả tạo máy): tạo user thường, `ufw` chỉ mở SSH (Telegram dùng long polling ra ngoài, không cần mở port vào), cài Node 24 + OpenClaw như bước A, `git clone` template (hoặc `scp` thư mục), đặt secret vào `~/.openclaw/openclaw.json`, `openclaw onboard --install-daemon`.
3. Kiểm: `openclaw gateway status`, `openclaw channels status --probe`, chạy lại `CHECKLIST.md` từ Telegram.
4. Tiền: VPS tính theo giờ trừ ví MONA Cloud; tắt máy = ngừng tính; gói tháng từ 399.000đ nếu chạy dài. Hoá đơn VAT xuất theo tháng.
5. Backup: workspace là git riêng tư (`git init` trong thư mục, push lên repo private của anh chị); `~/.openclaw/` chứa secret, KHÔNG commit.

## C. Bảo mật tối thiểu
- Không ghi token vào file trong repo; chỉ `openclaw.json` hoặc `.env` quyền 600.
- `dmPolicy: "pairing"`: chỉ người được duyệt mới nhắn được bot.
- Đổi token khi nghi lộ (xem AGENTS.md mục 10).

## D. Kẹt thì sao
Gọi 1900 636 648 hoặc email info@themona.global. Anh chị là khách MONA muốn gắn agent thẳng vào hệ thống đang chạy: gói Doanh nghiệp, MONA triển khai và vận hành.
