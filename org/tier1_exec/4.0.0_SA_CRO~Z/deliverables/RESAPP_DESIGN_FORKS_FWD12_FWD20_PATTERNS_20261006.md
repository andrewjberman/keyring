# AMGT_RESAPP design forks FWD-12 and FWD-20: the estate's past patterns

**From:** 4.0.0_SA_CRO~Z. **For:** 1.0.0_SA_CTO~Z (msg 30048; `ledger/ROUND_ANALYSIS.round75.md` ruling 3).
**Resumed:** the pause (Andrew ~13:2xZ, "return to this issue later") lifted with the Bloomberg hold (Andrew ~17:44Z,
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261006_1744Z_BLOOMBERG_RESOLVED_YANG_CIX_USER_ERROR_SITEZ_RESUMES_REGULAR_WORK.md`).
**Method:** two read-only estate sweeps; the load-bearing citations below were re-printed at HEAD by this seat
(marked READ). Paths are repo-relative; `PRD` = `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md`.
Search scope that bounds any absence is stated at the end of each note.

---

## Note 1 -- FWD-12: re-run ONE input from the page

### What the estate has done before (five page- or tool-started runs)

| Pattern | Auth / who may press | Cost and rate | Write path and readback |
|---|---|---|---|
| **AMGT on-demand pull** (closest) | JWT authorizer on the route (`infra/aws/terraform/harvest/api-gateway.tf:106-109`); the Lambda checks no role or firm (`infra/aws/lambda/research/pull_enqueue/lambda_function.py:77-108`); `ROLE_HEADER` declared and unused (`lib/research/api/scoped_amgt.py:6155`) | no dedupe, no lock, no DLQ; ~7.6 s and 2 Bloomberg calls per pull (`SEAM_DESIGN.md:109,122-124`) | `packs/<key>/status.json` REQUESTED, then one SQS send; box-side consumer moves it to FETCHING/LANDED/FAILED (`pull_consumer.py:87-118`) |
| **/data-refresh -> Yang pipeline** | browser requires `role==='admin'` (`portal/src/App.tsx:143,521`); backend requires `userType` Dev but passes a missing userType and a missing authorizer context (`infra/aws/lambda/data_refresh/lambda_function.py:166,189-192`), so the browser and the backend check different things | no running-run guard on `/trigger` (`:413-658`); only rollback refuses 409 while RUNNING (`:1233-1260`) | presigned upload, copy to `uploads/` fires the Step Function; DynamoDB row RUNNING; the page polls every 3 s |
| **IRPT YCharts generate** | tenant and identity from the verified user only, browser-supplied ones refused (`ycharts/generate/entry.py:19-23,73-74`); firm binding proven server-side (`_authz/enforce.py:145-177`) | **vendor-cost gate**: the worker refuses a live YCharts call unless an env var carries Andrew's per-use consent (`job.py:617-633`) | one SQS send, answers QUEUED; max 5 receives |
| **IRPT export submit/receipt** | render grant checked first | retries 0, events older than 60 s dropped (`b1_submit.tf:122-126`) | `pending.json` BUILDING, one async self-invoke, receipt reads BUILDING/FAILED/TIMED_OUT (`export/submit_async.py:113-164,200-212`) |
| **/mdpf-refresh** (agent skill, not a page) | any agent; `--reland` needs Andrew's in-session word | n/a | its runs are never production evidence |

### Prior refusals and rulings that bind a page-started re-run

1. **The consumer stays box-side and is not a Lambda; its cadence is reserved to Andrew; no monitor rides along**
   (PRD `:1380-1388`, READ).
2. **A control that cannot act says why**: a re-run control is bound to a stage that exists or refuses with a named
   reason, never a button that does nothing (PRD `:1393-1395`, READ).
3. **The current Refresh button already breaks rule 2**: `POST /api/scoped/amgt/refresh` answers 200 "declared" and
   enqueues nothing (`lib/research/api/scoped_amgt.py:6859-6876`, READ), and nothing in `portal/src` calls the
   enqueue route.
4. The round-12 refresh-carrier sign-off forbids consumer wiring and any `sqs:*` grant
   (`NEVER_WIDEN_ROUND12_REFRESH_CARRIER..._CTO_HALF.md:25,51-52`), so wiring one is a new never-widen act.
5. Starring is a marker and Refresh is a separate explicit act (Andrew 2026-09-11,
   `1.0.0_SA_CTO~Z/AMGT_RESAPP_FRONTEND_SYNTHESIS_20260911.md:12`).
6. CLAUDE.md: an ad-hoc run is QA and never production evidence; moving served output needs never-widen sign-off.

### What already exists for the per-input half

`lib/research/ledger/ledger.py:151-174` (READ) has `rerun(key, class)`, which runs that class's stage and nothing
else, and records an honest FAILED on a raise. **Every class registers `stage: None`** (`:48-55`, READ), so today
every re-run raises "no stage registered". `record_run` reads, appends and rewrites with no lock (`:122-133`), so two
concurrent re-runs of one key can lose an entry.

### Recommendation

- **Shape:** the AMGT pull pattern, keyed per (security_key, input_class): JWT route -> enqueue writes a status
  object REQUESTED -> one SQS send -> the class's registered stage runs where its source lives (market_data on the
  box) -> the page polls the status object. The `ledger.rerun` registry is the single source of what can be
  pressed: a class with `stage: None` renders the refusal with its reason (rule 2), never a button.
- **Close three gaps the precedents show:** (a) the role check is server-side and identical to the browser's (the
  /data-refresh mismatch is the pattern to avoid); (b) one run in flight per (key, class) by a conditional write on
  the status object, which also removes the ledger's read-modify-write race; (c) a per-class cost gate, on the
  YCharts precedent, for any class whose stage calls a vendor.
- **Smallest first version:** market_data only (the one class with a source and an existing carrier); the other
  five refuse with reason. Retire the "declared" no-op on `/refresh` in the same cell.
- **Calls for Andrew (not this seat's):** who may press (internal analyst or admin only), and whether a page press
  counts as his per-use word for a Bloomberg pull or needs its own consent.

Scope: POST routes in `portal/src/api/**`, `portal/src/App.tsx`, async-invoke and SQS sends in
`infra/aws/lambda/**`, throttles in `infra/aws/terraform/**`, `scoped_amgt.py`, `rcg/rulings/RULINGS.jsonl` (0 hits),
`org/**/ANDREW_DIRECT_*`. Not read: the `opal-portal-authorizer` source; `docs/doctrine/`.

---

## Note 2 -- FWD-20: a house forward FCF forecast

### What exists

- **Consensus only, no house projection anywhere.** The Bloomberg model block pulls annual reported history 2016 on
  (about 80 fields, incl. revenue, EBITDA, capex, FCF, CFO, margins) plus `BEST_*` consensus FY1-FY3 incl.
  `BEST_ESTIMATE_FCF` (`integrations/bloomberg/research/model_block_pull.py:220-314,330-338`). Coverage 94 of 100
  blocks from the 2026-09-25 pull (`org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:599-601`).
- **Divergence is built and waits on the forecast.** `lib/research/scores/divergence.py` computes
  D = (house FCF - consensus FCF) / dispersion and returns ABSENT_SOURCE when `model_fcf` is None (`:128-138`, READ);
  `run_scores.py:189-192` calls it with no arguments, by design, until AMGT-rk-29 serves (READ).
- **Base case** (served): consensus adjusted EPS x the name's trailing-median P/E (`lib/research/api/case_rule.py:12-23`).
- **No structured financials from filings.** `fetch.py` pulls 10-K/20-F narrative sections only; `companyfacts` has
  zero repo hits and no code parses XBRL numbers.

### Ruled out or held

1. **Drivers seeded from consensus are forbidden**: revenue, margin, tax, capex and working capital come from dated
   filings and operating history, every assumption stored with its source and time (CTO ruling,
   `CTO_ADJUDICATION_AMGT_RESAPP_20260915T195xZ.md:59-61`, READ). Gate: sd(D) across the universe < 0.25 means the
   drivers were seeded from consensus, D is ABSENT for every name, checked before deployment and binding the
   producer (PRD `:1400-1408`, READ).
2. **Upside is never the ranked score** (it would double-count price); U and Delta are reported, never ranked
   (Andrew 2026-09-15).
3. **Upside/Downside spreads**: held ABSENT, methodology reserved to Andrew (PRD `:1548-1549`).
4. **No reverse-engineered FactSet-style adjusted figures** (PRD `:1556-1558`).
5. **DCF**: never built. A DCF with stated WACC appears in Andrew's reference report format, but the CTO intake
   called it a new producer, and a DCF skill was taken as reference only. D compares FCF, not value, so FWD-20 does
   not need one.

### Recommendation: the smallest defensible first version

- **Per name, annual, FY1-FY3:** FCF = revenue x FCF margin. Revenue grows at the name's own trailing growth (median
  of the last 3-5 annual changes); FCF margin = the trailing median of FCF / revenue. Both come from the model
  block's reported history. Each driver is stored with its source field, the fiscal period and its as-of date. No
  consensus field is read by the producer.
- **Then:** D against `BEST_ESTIMATE_FCF` FY1 through the existing `divergence.py`; run the sd(D) >= 0.25 gate before
  anything is shown; ABSENT with reason for any name short of history.
- **The one gap that needs a ruling:** the PRD wants each driver "kept with the filing it came from and that filing's
  date" (PRD `:703-733`). Bloomberg history carries the period and an announcement date but no filing id. Either
  (a) the CTO accepts period-end plus announcement date as the filing reference for v1, or (b) an EDGAR XBRL
  companyfacts pull is built, which is egress off Opal infrastructure and needs Andrew's word. This seat recommends (a)
  for v1, with (b) as the enrichment.
- **Caveat:** a trailing-trend forecast can correlate with consensus without being seeded from it. The 0.25 floor
  catches near-zero spread only, so a passing gate is not proof of independence.

Scope: DCF/WACC/terminal value across the whole repo (58 files; `research_transcripts/` hits not read);
`companyfacts` and XBRL across the whole repo; FWD-20 and the forecast terms in `org/missions/D5/AMGT`, `lib/research`,
`integrations/bloomberg/research`, `portal/src`, `docs/briefs`, `data/`, `rcg/rulings`, dated Tier-0/1 records.
"EGRAPH" has no project by that name. Not searched: SharePoint workbooks, live S3.
