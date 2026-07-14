# Implementation Brief — (1) Tax SMA Automation + (2) Opal Ticket System

**Author:** 0.5.0_AE_OpalETL~A | **Date:** 2026-07-14 (~19:20Z) | **For:** Andrew (sovereign), CC 2.0.0_SA_COO + 1.0.0_SA_CTO
**Instruction (Andrew-direct, verbatim record):** `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/ANDREW_DIRECT_20260714_taxsma_ticket_system_scoping.md` (committed `061db84a7`)
**Vintages for every repo citation:** workspace CLOUD @ `cc4a30507`, portal DEV @ `24fd10d0`. Mailbox facts read live via the OPLMCP m365 gateway 2026-07-14 ~19:0xZ.

---

# PART 1 — TAX SMA (existing project: PFMG_TAXSMA)

## 1.1 Registry check result (Andrew asked for this first)

**The project IS already registered.** `org/projects/PFMG_TAXSMA.json` — status **active**, created 2026-06-26,
renamed from `ADVI_TAXSMA` to `PFMG_TAXSMA` the same day by Andrew-direct macro reclassification (macro `PFMG` =
PortfolioManagement; `TAXX` also exists in MACRO_CODES.md as "Tax Strategy" but the 06-26 Andrew ruling placed this
project under PFMG — recorded here, not reopened). CTO PRD: `docs/architecture/PFMG_TAXSMA_PRD.md`. Owner
0.4.0_DS; pods 0.4 / 0.8 / 3.0 / 0.3.1. **This brief therefore reconciles and advances the existing project — it
does not re-scope it from zero.**

The project is **discovery-gated**: three S0 unknowns gate the build legs. Current S0 state, reconciled today:

| Gate | Question | Status (2026-07-14) |
|---|---|---|
| S0.1 | Does `opal-data-schwab` already carry lot-level cost basis for the 3 Tax SMA accounts? (decides step-2: cheap S3 lookup vs hard fresh-Schwab pull) | **OPEN** — no deliverable on the record. Assigned to CVO 06-26; note CVO~B is currently DOWN, so ownership likely needs a re-route (COO call). |
| S0.2 | Yang's two converter scripts: located, contracts, hosting | **COMPLETE** (`docs/briefs/PFMG_TAXSMA_S0.2_converter_scripts_assessment.md`, updated 06-29). Both scripts canonical in-repo: `tools/tax_sma/canonical/convert_cost_basis.py` (drift-verified vs Yang's original, logic byte-identical) + `convert_optimization.py` (byte-identical, `bfa81d9da`). I/O contracts pinned from source. Shim = inject `{BASE}` + `{date}` only — trivial. **The hard guardrail is confirmed in Yang's own code:** step-5's terminal action writes the trade CSV and stops — no upload, no execution. |
| S0.3 | Deterministic first-vs-second ("PRELIM" vs final) email rule | **MATERIALLY ADVANCED TODAY** — see 1.3. Remaining: attachment-name characterization + rule ratification. |

## 1.2 Yang's specification (the scope boundary, in his words)

Source email: **"Tax SMA Automation"**, Yang Liu (Yang@opalinvest.com) → Andrew, received **2026-06-26T18:13:16Z**
(read in full via the gateway today). Framing, verbatim: *"I would say step 1, 2, 3 are doing the processing. I
would handle the step 4 manually and step 5 would be the post processing."* Working directory:
`C:\Users\YangLiu\Opal Capital\Shared - Documents\TAX`; master file `Tax SMA Accounts.xlsx`. The five steps, verbatim:

1. **"Automate the download of short sale files from Schwab"** — *"Every morning, there will be two emails with
   subject of 'Short Sale Avail File'. Download two attachments of these two files and save them under the folder
   of 'Short Sale'. The first one should renamed with suffix of ' YYYYMMDD PRELIM' and the second one with suffix
   of ' YYYYMMDD'."*
2. **"Download cost basis of Tax SMA"** — *"Use the list of 'Master File' and select the accounts with 'Traded'
   columns as 'Yes'. Currently, there are 3 accounts live. Go to Schwab and look up the account by account number,
   use the tab of 'Cost Basis' on the top to 'Export only lot level detail'. Each file should be saved in the
   folder of 'Tax Lot/YYYYMMDD'."*
3. **"Convert the lot holdings to Factset input format"** — *"Refer to the python code of 'src\convert_cost_basis'
   ... It would convert those downloaded files to new files for each account under 'Initial Holdings\YYYYMMDD'."*
   (The actual source writes **"Initial Holding"** singular — the source contract, pinned in the PRD, overrides the
   email prose.)
4. **"Portfolio Optimization"** — *"Yang use Factset to optimize and fine tune rebalance and save optimization
   report for each account under 'Optimization\YYYYMMDD'"* — **manual, Yang's own step.**
5. **"Convert Optimization to trade file"** — *"Refer to the python code of 'src\convert_optimization' ... It would
   generate trade file under 'Trade\YYYYMMDD\schwab_upload_YYYYMMDD'."*

### SCOPE DISCREPANCY — surfaced, not adjudicated

Andrew's instruction today: *"I believe we can automate Steps 1-4 in that email."* Yang's email: steps 1/2/3 are
processing, **step 4 is Yang's manual Factset step**, step 5 is post-processing. The PRD carries a PRD-level
constraint that step 4 stays human. So "Steps 1-4" as literally numbered would include the step Yang reserved for
himself. **Most consistent reading:** automate the four automatable things — steps 1, 2, 3 + the step-4 *handoff
surface* (present step-3 output to Yang, "waiting on optimization" gate) — with step 5 either included (Yang's own
scope says it is automatable post-processing, and his script already embodies the generate-don't-execute guardrail)
or deferred. **Needs one word from Andrew:** is step-5 trade-file generation in the initial build, or held back?
Everything below is structured so either answer works.

## 1.3 The SSAVAIL feed — VERIFIED LIVE today (feed-shape-verified, not just asserted)

Live mailbox verification (gateway `search_email` + full read of today's first email):

- **Sender:** `SmartLoan9990@fisglobal.com` ("Short Sale Avail File", FIS/SmartLoan). Body: *"Please find attached
  Short Sale Avail File for SmartLoan."*
- **Delivery path into Andrew's mailbox:** each FIS email arrives as a **forward from Yang** (yang@opalinvest.com)
  to **Manav, Menachem, Andrew, Alyssa**. The forward lag is ~3-4 minutes after the FIS send time **every day,
  including the 5 AM file** — this is a mailbox auto-forward rule, not Yang manually forwarding, i.e. the feed is
  mechanical and dependable. (Dependency worth noting: the feed rides Yang's mailbox rule. Recommendation in 1.6.)
- **Cadence observed (sent times, ET):** 07-08: 5:0x + 6:47 | 07-09: 5:03 + 6:47 | 07-10: 5:01 + 6:47 **+ 8:10 +
  8:14 (a FOUR-email day)** | 07-13: 5:01 + 6:47 | 07-14 (today): 5:02:58 + 6:47:38. Andrew's word confirmed: the
  assets are present and arriving daily.
- **S0.3 consequence (material):** the stable pattern is ~5:01-5:03 ET (first/PRELIM) and ~6:47 ET (second/final),
  but 07-10 proves **naive arrival-order ("first two of the day") is NOT a deterministic rule** — extra sends
  happen. The rule should be grounded on the full sample set (the ~15 samples Yang forwarded + the live daily flow);
  a time-window rule (first before ~6:00 ET = PRELIM; the ~6:47 = final; later sends flagged for human eyes, never
  silently renamed) fits every observed sample but should be ratified as S0.3's close, per the PRD "no coding
  step-1's rename before this is deterministic."
- **Payload gap (named, honest):** the current m365 gateway toolset has **no email-attachment-fetch tool** (verified
  against the live tool schema list today — mail read/search/send exist; attachment download does not). So I
  verified the feed's existence, cadence, sender, and recipients, but could NOT pull an attachment to characterize
  the file itself. Two consequences: (a) the PRD's assumption that the gateway "can fetch attachments" needs one
  correction; (b) **an attachment-fetch capability (gateway endpoint or a Graph-API Lambda) is the first build
  dependency of step 1.** Small, well-understood Graph call (`/messages/{id}/attachments`) — but it must be built.

## 1.4 What exists to build on (do not re-derive)

- **Converters:** canonical, verbatim-locked, contract-pinned (S0.2). Deps pandas + openpyxl — both already exist
  as Lambda layers in the estate (`pipeline_inventory`: pandas py3.11 layers, openpyxl-layer).
- **The TAX directory is a SharePoint-synced library** ("Opal Capital / Shared - Documents / TAX"), not a
  machine-local path — so cloud automation can write to the exact folders Yang and Alyssa already use, via the
  gateway's site-file tools (`find_sharepoint_site` / `list_site_files` / `read_site_file` are already live). This
  is the S0.2 "HOST INSIGHT" and it carries Andrew's folded decision **UI = HYBRID**.
- **Schwab lot-level ingest exists** for 49F account 08242234 (`/49-schwab-conv`: CRS files → `opal-data-schwab` →
  6 silver tables incl. canonical lots + realized lots). Whether the 3 Tax SMA accounts are in that delivery is
  exactly S0.1 — if yes, step 2 collapses from browser-automation-against-Schwab to an S3 lookup + reformat.
- **M365 daily-AM scheduling pattern** exists across the estate (EventBridge cron → Lambda).

## 1.5 Proposed architecture (hybrid, per the standing decisions)

```
                       ANDREW'S MAILBOX (or service mailbox -- see 1.6)
  FIS SmartLoan ──► Yang auto-fwd ──► [Step-1 Lambda, EventBridge ~7:15 ET daily]
                                        │  Graph: find today's "Short Sale Avail File" emails
                                        │  fetch attachments (NEW gateway/Graph capability)
                                        │  apply S0.3 rule -> " YYYYMMDD PRELIM" / " YYYYMMDD"
                                        ▼
                          SharePoint TAX/Short Sale/          (+ S3 audit mirror, raw bytes)
                                        │
  Tax SMA Accounts.xlsx (Traded=Yes) ──► [Step-2: SHAPE GATED ON S0.1]
                                        │   (a) opal-data-schwab lot lookup -> format -> TAX/Tax Lot/YYYYMMDD/
                                        │   (b) else: extend CRS ingest, or (least-preferred) Schwab browser pull
                                        ▼
                          [Step-3 runner] convert_cost_basis.py VERBATIM ({BASE},{date} injected)
                                        │        -> TAX/Initial Holding/YYYYMMDD/  + summary.xlsx
                                        ▼
                          "READY FOR OPTIMIZATION" state -> notify Yang (Teams/email via gateway)
                          [Step 4 -- YANG, MANUAL, FACTSET]  -> TAX/Optimization/YYYYMMDD/
                                        ▼
                          [Step-5 runner] convert_optimization.py VERBATIM
                                        │        -> TAX/Trade/YYYYMMDD/schwab_upload_YYYYMMDD.csv
                                        ▼
                          "TRADE FILE READY -- HUMAN REVIEW + UPLOAD" surface.  NEVER auto-uploaded.
```

- **Operator UI (Alyssa, day-to-day):** per Andrew's folded decision, hybrid — the data legs are cloud;
  the operating surface is a simple runner: one labeled button per automated step, the day's `YYYYMMDD` state,
  a visible "waiting on Yang" gate at step 4, clear success/failure per step. Platform choice remains **Andrew's
  call** (PRD §4); the DataRefresh page precedent (AE-owned Lambda `opal-data-refresh-api` + DE/RD-owned portal
  page, README `org/tier2_senior/0.5.0_AE_OpalETL/README.md`) means a portal "Tax SMA Runner" page is cheap and
  consistent — and pairs naturally with the Ticket Center below if both land in the portal.
- **Scheduling:** step 1 daily-AM (EventBridge); steps 2/3/5 on-demand (Alyssa's buttons); step-5 optionally
  auto-armed by an Optimization-folder watch but still terminating at the human-review surface.
- **Guardrails carried (PRD-level, non-negotiable):** the system GENERATES `schwab_upload_YYYYMMDD` — a HUMAN
  reviews and uploads; no Schwab/Factset credentials in code (if S0.1 forces a fresh-pull path, that credential
  design is its own CTO-gated leg); converters run VERBATIM (Andrew-direct 06-26), never "improved"; any SES
  notification sends from `opalinvest.dev` (CLAUDE.md Rule 23).

## 1.6 Recommended sequencing + the asks

| Phase | Work | Gate / acceptance |
|---|---|---|
| **A (immediately buildable)** | Close S0.3 (rule ratified on the full sample set incl. the 07-10 four-email day) -> build attachment-fetch -> build step-1 (email -> Short Sale folder + rename + S3 audit mirror). **Testable NOW against the live daily feed** — that is what Andrew's "assets arriving daily" unlocks. | Step-1 output matches Yang's manual filing byte-for-byte across >=3 consecutive live mornings, PRELIM/final labels correct, extra-send day handled loud-not-silent. |
| **B** | S0.1 verdict (re-route owner — CVO down; an AE-side audit with CTO gate works) -> build step-2 in the verdict's shape. | The 3 Tax SMA accounts' lot-level cost basis lands in `TAX/Tax Lot/YYYYMMDD/` matching Schwab's "Export only lot level detail" schema (`CostBasis_Acct_*.csv`, the pinned step-3 input contract). |
| **C** | Step-3 + step-5 runners (verbatim + shim), step-4 handoff states, the Alyssa UI per Andrew's platform call. | End-to-end dry-run on a historical `YYYYMMDD`: step-3 outputs reproduce Yang's known-good `Initial Holding` files exactly; step-5 reproduces a known-good `schwab_upload` file exactly; the trade file is generated-not-executed. |

**Asks of Andrew (each one word/line):** (1) confirm step-5 in or out of the initial build (the "Steps 1-4"
question, 1.2); (2) the UI platform call (portal page vs local runner — PRD §4 reserves this for you); (3) whether
to keep riding Yang's auto-forward or have FIS/Yang add a dedicated address (e.g. a service mailbox) to the
distribution — the forward works today but is a single point of failure in Yang's mailbox rules; (4) S0.1 owner
re-route (with COO).

---

# PART 2 — OPAL TICKET SYSTEM (new; proposed registration below)

## 2.1 Source material + registry state

- **No registered project exists** (registry swept today). COO confirmed registration follows this brief.
- Source: call transcript Andrew <-> AJ Graff, read in full today (`Downloads/Call with AJ Graff (1).vtt`; the
  `.docx` is the same transcript — it ends at the same "stopped transcription" point, no extra content).
- **Proposed registration (for COO/CTO to confirm):** new macro **`TCKT`** (TicketCenter) under **Pod 3 —
  TradingOperations** (it lives next to TradeSubmission/PortfolioManagement operationally, exactly where Andrew
  placed it in the call: *"in the bottom left, like by the security scanner and portfolio management stuff ... a
  ticket center page"* @ 8:18-8:36). Project code **`TCKT_CENTER`**. Macro must be added to
  `org/projects/MACRO_CODES.md` at registration (its rule 6). UI lane: DE/RD per the DataRefresh/SecurityScanner
  precedent (a new `0.3.5_RD_TicketCenter` mirrors how SSCN got `0.3.4_RD`); backend Lambda/infra: AE lane; final
  allocation is COO's.

## 2.2 Requirements extracted from the transcript (timestamped)

**Ticket types + intake (two distinct flows — AJ was explicit):**
- **Trade requests:** a structured form already exists — *"for the trades, there is a ticket that they do fill
  out"* (6:06), *"largely the structure of what Menachem already has"* (0:35), lives with Menachem (SharePoint,
  6:21-6:33). Advisors (e.g. Peter Lee / Inflection) already use it.
- **Service requests** (portfolio questions, account reviews, meeting requests — 0:11-0:28, 3:47-3:57): Andrew's
  intent is **zero-friction AI intake**: *"we just intelligently identify what a ticket would be based on the
  e-mail or based on the message ... so it's like no friction for them"* (5:47-6:06); AJ agreed AI interpretation
  fits service requests (6:10-6:20). AJ's hard-won caution: WealthBox's ticket system died because creating a
  ticket was too much work (5:23-5:42) — **intake friction is the killer risk.**

**Routing (role/type matrix, 3:13-3:46):** Trading group — Menachem + Bobby primary, Manav + Alyssa secondary.
Portfolio-management questions — Manav + Alyssa first, Bobby + others visibility, investment team (Yang) as needed.
Types map to responsible groups so coverage survives someone being out (Andrew, 2:16-3:13).

**Statuses + claim flow (7:22-7:48):** Open -> In Progress (someone claimed it) -> Completed, color-coded. Claim
must be one-touch: *"have like an SMS or something, where it's just like you just have to respond to one if you've
got it"* (7:48-7:57, also 7:00-7:18) — claiming removes it from the group's pending set.

**Cutoff + expectation-setting (0:58-1:16, 4:23-4:53):** a cutoff (AJ: *"I think it's like 2:00 Eastern"* — **must
be verified against the agreement**; AJ: *"We need to look at the alongside agreement to see what the time is"*).
Post-cutoff trade requests get an auto-acknowledgement: received; if the team can and the market is open, today;
otherwise **next trading day**. (Implementation note: "next trading day" comes from `lib/trading_calendar.py` — the
estate's one frontier definition; never wall-clock.)

**Reminders/escalation (1:02-1:40, 7:34-7:48):** open-ticket prompts at the cutoff and end-of-day; if nobody claims
by X, prompt the group / fall back past the primary owner (Andrew, 6:48-7:00).

**Dashboard + metrics:** portal Ticket Center page showing active + historic tickets (8:18-8:36); per-person /
per-type average response time (AJ, 10:46-10:57); response-expectation messaging (Andrew, 11:00; AJ, 11:11).

**Visibility model (9:04-10:45):** internal-first (*"totally internal"* is an option Andrew offered); external
filers (Inflection et al.) later get "file a ticket + see your ticket status," curated per group — AJ: *"in time we
could turn on to where they could see their ticket status"*; Andrew flagged the caution about too much external
visibility (10:32-10:45).

**Notifications:** Andrew wants AWS-native (his "AWS has a messenger" = SNS/End User Messaging) tied into
phone/Slack/Teams/email (8:36-9:05), no third-party ticketing vendor.

## 2.3 Design — in tandem with the Portal (the seams, named)

All portal citations: portal DEV @ `24fd10d0`.

- **Page placement:** new `/ticket-center` entry in the existing `NAV_SECTIONS` **Tools** section
  (`portal/src/App.tsx:106-113`) — precisely "by the Security Scanner and Portfolio Management stuff." New page dir
  `portal/src/pages/TicketCenter/` following the SecurityScanner page pattern (DESIGN_SPEC-driven, mirrors
  PortfolioManagement's visual language).
- **Auth/visibility seam (already built, reuse as-is):** nav + route visibility is gated per-item by the firm-access
  matrix `isPathAllowedForFirm(claims.firmId, path)` + `requiresDev`/`requiresAdmin`/`requiresTier`
  (`portal/src/App.tsx:294-312`, `useAuth` claims). Phase 1: `/ticket-center` allowed for the opal-capital firm
  only (internal). The later external phase is a config change (add the path to a partner firm's
  `FIRM_ALLOWED_PATHS`) + per-ticket requester scoping in the API — the mechanism Andrew described ("they get a
  curated group," 9:13-9:27) already exists.
- **TradeSubmission seam (do NOT duplicate):** the portal already has a full TradeSubmission page
  (`portal/src/pages/TradeSubmission/`, tabs submit/approvals/execution/history, `TRSB` macro, RD
  0.3.2). Trade-request tickets should LINK to/ride this flow (a trade-type ticket references a submission id),
  while Menachem's existing SharePoint form gets a connector (below) so current advisor behavior keeps working.
  Reconciling TradeSubmission-the-page with Menachem's-form-the-intake is a design decision for the build leg —
  both existing, neither should be rebuilt.
- **Backend pattern (established precedent, mirror it):** `opal-data-refresh-api` — one AE-owned Lambda behind the
  portal's API path, DynamoDB state table (`opal-data-refresh-executions`), DE/RD-owned pages consuming it
  (`org/tier2_senior/0.5.0_AE_OpalETL/README.md` "Data Refresh Backend"). Ticket system mirrors:
  - **DynamoDB `opal-tickets`** — ticket_id, type, status (open/in_progress/completed), requester (+ firm),
    assignee, claim events, timestamps, cutoff-relative flags, SLA fields, full audit trail (status transitions
    power the response-time metrics AJ asked for).
  - **Lambda `opal-ticket-api`** (`/tickets/*` routes: create, list, get, claim, complete, metrics) — Terraform
    module, IAM per Rule 22a discipline (simulate battery on the exact new table/queue ARNs before first deploy).
  - **Notification engine:** EventBridge schedules (cutoff sweep at the verified cutoff time, EOD sweep,
    claim-timeout escalations — trading-calendar-aware) + senders: **SES from `opalinvest.dev`** (Rule 23 —
    hard rule), **Teams via the m365 gateway** (`send_chat_message` exists today — cheapest one-touch channel),
    SMS via AWS End User Messaging as a follow-on. Claim mechanics recommendation: a one-tap **claim link**
    (deep-link to `/ticket-center?claim={id}`) in Teams/email first — it is two orders cheaper than two-way SMS
    ("reply 1") and delivers the same "respond with one touch" UX; add two-way SMS only if field behavior demands it.
  - **AI intake worker (service requests):** poll/webhook on the monitored mailbox + Teams
    (`poll_addressed_teams_messages` exists) -> Claude API classification (type, client, urgency, suggested
    routing) -> ticket draft. **Confidence-gated:** high-confidence creates the ticket + auto-ack; low-confidence
    lands in a "needs triage" queue — never silently dropped, never silently filed wrong. (Claude API via
    Bedrock/Anthropic — an approved-model call, not a vendor-egress question; flagging per COO's note anyway.)
  - **Form connector (trade requests):** Graph poll/webhook on Menachem's existing SharePoint form list -> ticket
    of type trade_request. Zero change to what advisors do today — AJ's friction rule satisfied by definition.

## 2.4 Phasing + acceptance

| Phase | Scope | Acceptance |
|---|---|---|
| **P0 — core loop** | DynamoDB + `opal-ticket-api` + `/ticket-center` portal page (internal-only): manual ticket create, type/routing matrix (config-driven), claim, statuses, active+historic views. | A ticket can be created, claimed, completed end-to-end in the portal; status transitions audited; page visible only to opal-capital firm. |
| **P1 — the clock** | Cutoff + EOD sweeps, auto-ack with expectation text (trading-calendar-aware), claim-timeout escalation, Teams+SES claim links. | A post-cutoff trade ticket generates the correct next-trading-day ack (verified across a weekend/holiday); an unclaimed ticket escalates on schedule; claim-by-link works from Teams and email. |
| **P2 — zero-friction intake** | AI email/Teams classification worker (confidence-gated) + Menachem-form connector. | >=90% of a labeled sample routes correctly; every low-confidence item lands in triage (0 silent drops); form submissions appear as tickets with no advisor behavior change. |
| **P3 — outside + metrics** | External filer visibility (firm-matrix + requester scoping), response-time metrics per person/type, SMS if wanted. | Inflection user sees exactly their firm's tickets and nothing else; metrics reconcile against the audit trail. |

**Open items needing a human word:** (1) the actual cutoff time from the agreement (AJ to pull it); (2) claim-link
vs two-way-SMS as the claim mechanic (recommendation: link first); (3) external visibility timing (AJ leaned "in
time"); (4) COO: registration (`TCKT` macro + `TCKT_CENTER`) + UI-lane allocation; (5) which mailbox/channel set the
AI intake monitors first (recommend: the shared/service address the team already uses for client asks, scoped
read-only).

---

# Shared risks + estate-discipline notes (both projects)

- **Email-attachment fetch is a NEW capability** needed by TAXSMA step-1 (and useful to ticket intake). Build once,
  in the gateway or as a Graph Lambda, bounded to named folders/mailboxes (SCTY_MCPGUARD posture).
- **Everything sends via `opalinvest.dev`** (Rule 23). Nothing touches `opalcapital.com` (not ours).
- **Trading calendar everywhere a "day" appears** (TAXSMA YYYYMMDD folders on trading days; ticket next-trading-day
  acks) — `lib/trading_calendar.py`, never wall-clock (NEVER#1).
- **New AWS resources ride the standard gates:** Terraform-only, safe-apply, source map, Rule 22a live-primitive IAM
  verify on exact ARNs (comp-iam fails GREEN on new resources), deploy-completion ledger for any multi-leg deploy.
- **Neither build touches tonight's 22:00Z pipeline or the INF chain.** TAXSMA writes live in SharePoint TAX/ +
  `opal-data-schwab` (read) + its own new keys; tickets live in their own new table/routes.
