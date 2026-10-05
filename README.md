# mona-agent-templates

Templates for self-hosted AI assistants that a coding agent (Claude Code, Codex, Gemini CLI) can set up on your own machine or a MONA Cloud VPS.

Each template is a folder of instructions, skills, tool lists and sample data. The coding agent reads `AGENTS.md` and builds the assistant on the [OpenClaw](https://github.com/openclaw/openclaw) runtime. Template content is written in Vietnamese for Vietnamese businesses.

## Quick start

```bash
git clone https://github.com/mona-software/mona-agent-templates
cd mona-agent-templates/templates/cskh-zalo
claude   # then type: "Read AGENTS.md and set up this agent for me"
```

## Usage

### Templates

| Template | What it does | Uses |
|---|---|---|
| [`cskh-zalo`](templates/cskh-zalo/) | Answers customers on Zalo or Telegram from the shop's own documents; hands hard cases to a person | MONA Cloud, MONA Mail |
| [`sales-chot-don`](templates/sales-chot-don/) | Qualifies leads, quotes prices, creates MONA Pay transfer QR codes and notifies the owner when payment arrives | MONA Pay, MONA Cloud, MONA Mail |
| [`ke-toan-hddt`](templates/ke-toan-hddt/) | Records incoming payments, sends debt reminders and prepares invoice data (does not issue e-invoices yet) | MONA Pay, MONA Mail |
| [`content-seo`](templates/content-seo/) | Writes in the brand voice, checks drafts and waits for human approval before publishing | MONA Cloud |
| [`noi-bo-kin`](templates/noi-bo-kin/) | Answers staff questions from company documents with a local model | MONA Cloud VPS, Ollama |
| [`tro-giang-academy`](templates/tro-giang-academy/) | Answers lesson questions, reminds learners of deadlines and summarizes questions for the instructor | MONA Cloud, MONA Mail, mona.academy MCP |
| [`tuyen-dung`](templates/tuyen-dung/) | Reads CVs, scores them against criteria, schedules interviews and replies to candidates | MONA Mail, MONA Cloud |
| [`quan-tri-so`](templates/quan-tri-so/) | Answers management questions with figures queried from a real database | MONA Cloud (Postgres) |
| [`webmaster`](templates/webmaster/) | Monitors a website for downtime, errors, SSL expiry and backups; alerts on Telegram | MONA Cloud |
| [`remarketing-email`](templates/remarketing-email/) | Sends event-triggered email for abandoned carts, quiet leads and lapsed customers | MONA Mail, MONA Cloud |
| [`nhac-lich-hen`](templates/nhac-lich-hen/) | Confirms appointments, sends reminders 24 hours ahead and reschedules over chat | MONA Mail, MONA Cloud |
| [`don-hang-van-chuyen`](templates/don-hang-van-chuyen/) | Keeps customers updated on shipments and escalates returns and late deliveries | MONA Mail, MONA Cloud |
| [`phap-che-hop-dong`](templates/phap-che-hop-dong/) | Reviews contracts, flags unfavorable clauses and drafts from company templates; a person always decides | MONA Cloud |
| [`mua-domain-cho-khach`](templates/mua-domain-cho-khach/) | For agencies: searches, reserves and buys domains, sets DNS and tracks renewals per client | MONA Domain, MONA Cloud |

### Template layout

```
templates/<slug>/
├── README.md            # for people: what it does, who it is for, what it needs
├── AGENTS.md            # for the coding agent: goal, required stack, setup steps, when to ask a person
├── SOUL.md              # personality, tone and boundaries (loaded by OpenClaw each session)
├── IDENTITY.md          # name and emoji
├── skills/<x>/SKILL.md  # one task per skill, with name + description frontmatter
├── tools.json           # MCP tools the agent may call, runtime APIs and env vars
├── deploy.md            # run locally, then move to a MONA Cloud VPS
├── sample-data/         # sample data for testing; replace with real data
└── CHECKLIST.md         # acceptance criteria, tested through chat
```

### Data

Documents, chat history and agent memory stay on your machine or your own VPS. Only the `noi-bo-kin` template keeps all processing local by running an open model with Ollama; the other templates send prompts and the needed context to the model provider you choose.

### Catalog

[`catalog.json`](catalog.json) lists every template, and `templates/<slug>.json` bundles each template's files. [monacloud-mcp](https://github.com/mona-software/monacloud-mcp) reads them through `agent_templates_list` and `agent_templates_get`.

## Development

Rebuild the catalog after editing a template:

```bash
python3 scripts/build_catalog.py
```

Tool names in `tools.json` are taken from the `monacloud-mcp` and `monapay-mcp` source.

Website: [monacloud.vn](https://monacloud.vn).

## License

MIT

**MONA Agent is part of MONA Cloud by The MONA Group.**
