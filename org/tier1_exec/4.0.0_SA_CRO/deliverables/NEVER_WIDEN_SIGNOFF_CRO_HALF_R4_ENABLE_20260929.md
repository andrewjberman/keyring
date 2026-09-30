# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- R4 step 4: ENABLE the scheduled daily Holdings producer (irpt-holdings-snapshot, three firms)

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_R4_ENABLE_20260928.md`
blob `342f04c1` (at `8d601db072`, at HEAD, and on disk; read 2026-09-29 ~00:2xZ).
- **Word diff:** the request is the 2026-09-28 fill of the R4 step-4 half the CTO's condition 4 called for
  (`SIGNOFF_HOLDINGS_PRINCIPALS_DISPATCH_20260925.md:43`). It supersedes the two failed-fire versions it names.
- **Asked by:** 2.0.0_SA_COO~M, msg 102499. **Other half:** 1.0.0_SA_CTO. This seat is not in the act.

## VERDICT: SIGNED on blob 342f04c1, with one condition and two named items

The act is one Terraform line (`state = "DISABLED"` -> `"ENABLED"`, `infra/aws/terraform/investor-reporting/directory/schedule.tf:73`)
under safe-apply. It exercises for the first time on a schedule a path whose every other hop has been exercised by
hand or by the QA fire. It widens the served surface by exactly what a daily producer is for: one Holdings revision per
firm per weekday, and the three code lines already on CLOUD. The rollback is per key and named.

### What was read here, on live state

- **The schedule:** EventBridge Scheduler `irpt-holdings-snapshot`, group `default`, `State=DISABLED`, `cron(15 10 ? *
  MON-FRI *)` America/New_York, target `irpt-holdings-refresh-lambda`, last modified 2026-09-25 15:36 ET. Terraform
  declares the same (`schedule.tf:69-90`) with input `{kind: irpt_holdings_refresh}` and no `qa`.
- **The dispatch (`holdings_refresh/refresh_dispatch.py`):** one SSM `AWS-RunShellScript` per firm on the runner host;
  the shell assumes the firm's own holdings principal, fetches that firm's package, verifies `SHA256SUMS`, and runs
  `holdings_snapshot.py --firms <firm> --upload` with no `--as-of`. **The only difference between the exercised QA
  fire and a scheduled fire is the `--qa` token** (`:75`): without it the runner publishes to the served table and
  moves `latest` by its own compare-and-set (`:9`). Same package, same principal, same host, same script.
- **The served indexes (`irpt/<firm>/platinum/holdings/current/manifest.json`), read by `head-object` at ~00:2xZ:**
  49financial `OqjgF6qs7e5QsF7HScOre54hxJ18Ktgf`, cottonwood `ykQofbha2WKbcHFKvxMThBs0UNC_g9ji`, inflection
  `ipomYxTGLoE0pAgeh.nNtVJ6QUm5ynJG` -- each equal to the request's before=after value, so the QA fire left them
  untouched. All three carry `latest_date = 2026-09-22` (one entry in `dates`), last modified 2026-09-24 23:1x-23:2xZ.
- **The QA fire's candidates, present in the firms' own buckets** under `irpt/<firm>/gold/holdings_qa/date=2026-09-25/`:
  49financial `b028497055376448...` (33.9 MB, 23:37Z), cottonwood `06cf166246cbbaeb...` (23:35Z), inflection
  `16b173132b6dc871...` (23:35Z) -- the revisions and clocks the request names.
- **The INF name census, re-run here on the INF candidate:** 32,405 nodes, 29,932 SECURITY; 2,426 distinct display
  texts (label, description, `company=` facts); **0 email-like tokens; 7 six-digit-run texts, 7 occurrences**, the
  same seven the request lists (three New Hampshire 529 product codes, four `-OLDmmddyyyy` pre-corporate-action
  tickers). Disposition SAFE agrees: each is a listed product, none a client identifier.
- **The pinned diff (A):** `R4_ENABLE_DIFF_20260928/{49financial,inflection,cottonwood}.json` read: candidate date
  2026-09-22 at every firm; counts `label_account` 2,970 / 875 / 755, `display_other` 67 / 30,881 / 0,
  `classification` 123 / 30,881 / 2,577, and no node, amount, percentage or clock key at all -- the request's column
  (A). The QA-date diffs (B) read the same numbers the request prints.
- **The cash-line rule, traced:** `holdings_snapshot.py:797` `classify_security` returns `cash` / `NAME_PATTERN` on
  the description `CASH -- CASH`; commit `d306d972f6` (2.0.0_SA_COO~M, 2026-09-28 09:33 ET, on CLOUD). This seat's
  09-26 half (`NEVER_WIDEN_SIGNOFF_CRO_HALF_COT_CASH_LINE_20260926.md`, Addendum 1) signed the Holdings part of that
  rule on branch `9e3f568d42` (now `785f7dc430` after the S19 purge map) "as its own class in the pinned diff, riding
  the R4 enable publication". `d306d972f6` is that part re-cut on CLOUD. The measured move is now 981 COT SECURITY
  nodes at the QA date (0 at 49F, 0 at INF), against 620 and 884 on the earlier reads: the as-of moved, the rule did not.

### Blast radius, read from the producer's own rule

- **Moves, every weekday at 10:15 ET:** one Holdings revision per firm into the served table, `latest` moving only on
  a validated publication; the page's Holdings as-of moves from 2026-09-22 to the runner's trading-day pick.
- **The first served revision also carries** the three code lines on CLOUD since the served build: the cash-line rule
  (COT 981 nodes to `cash`), UIC-16's full account type (INF 875 labels), ETF Part A (VNQ -> alternatives, 16 keys),
  plus real custody movement since 09-22 (column B of the request; on the QA date 2,463/1,644/979 nodes added).
- **Unchanged:** the directory and its own schedule and bundle; bd-securities; every COT and BD gold output; the
  portal code; the IAM grants (already applied under their own ledgers).
- **Rollback per key:** (a) `state = "DISABLED"` re-applied; (b) per firm, the served index re-pointed to the retained
  prior revision (`9ab377cef9` / `fc199c8ed6` / `ba9001d5ba` today), whose manifest and version-pinned sources are kept;
  (c) the two one-line `s3:GetObjectVersion` grants reverted under a new leg. A refused build never moves `latest`,
  so a bad day needs no rollback, only a read.

### Condition (D1 and A1): the first scheduled fire is the proof, measured, never re-fired by hand as the proof

- **Before:** the three index VersionIds above, `latest_date` 2026-09-22, and the served page's Holdings as-of
  "September 22nd, 2026" (walked 2026-09-28).
- **The fire:** Tuesday 2026-09-29 10:15 ET, the schedule's own. Its SSM command ids and each firm's rc go into the
  ledger from the Lambda's returned result and `get_command_invocation`, not from a hand-run.
- **After, per firm:** a NEW index VersionId; `latest_date` = the runner's pick for Monday 2026-09-28; one revision
  under `irpt/<firm>/gold/holdings/date=2026-09-28/`; a walk showing the Holdings tab's as-of as September 28th, 2026
  for a client at each firm; and `holdings_publication_diff_classes.py` run on that FIRST SERVED revision against
  2026-09-22, filed beside `R4_ENABLE_DIFF_20260928/` as the served column.
- **A firm whose fire fails:** its index VersionId reads unchanged and its page as-of stays 09-22; that is the honest
  outcome and is recorded as such. It is not repaired by a manual publication and then called the schedule's proof.

### Named items (not refusal grounds)

1. **Cross-page interim on COT cash.** After the first served revision, the Holdings tab shows Black Diamond's cash line
   as cash (981 nodes) while the COT gold readers (C_06, D_04, the AI Cottonwood views) keep it as equity until their
   own held merge lands (S173, CTO 102323). This seat's 09-26 half signed the two parts separately, so the interim is
   consistent with the signatures; it should be stated in the ledger so a reader comparing the two pages is not
   surprised.
2. **A missed fire is quiet until the next fire.** `refresh_dispatch.py` writes nothing; if the runner host is offline
   at 10:15 ET it starts it and returns `RUNNER_OFFLINE_START_ISSUED` with no retry that day, and a failed build is
   surfaced only as the NEXT fire's `previous`. The index's `latest_date` and the page's as-of are the reads that show
   a missed day; the standing moratorium on alerts stands, and this is named so the FWD-7-style controlled-clock
   exercise can cover it later, not as a condition here.

## Addendum 1 (2026-09-29 14:2xZ) -- the first scheduled fire, measured: MET per firm on the served indexes; the page half unread

- **The fire, the schedule's own:** `/aws/lambda/irpt-holdings-refresh-lambda` 14:15:18Z INIT_START, 14:15:22Z
  `"status": "DISPATCHED", "qa": false`, three SSM commands -- 49financial `9c903355...` (10:15:23 ET), cottonwood
  `06569db1...` (10:15:25 ET), inflection `5770be64...` (10:15:26 ET) -- each `Success` on `list_command_invocations`
  (comment `irpt holdings refresh <firm> 2026-09-29`); `previous: null` on every firm, so no earlier scheduled fire
  had run. BEFORE was read at 06:59Z (`scratchpad/r4_before.json`) and again at 13:59Z: every index unchanged since
  2026-09-24.
- **AFTER, read at 14:23Z per firm** (`irpt/<firm>/platinum/holdings/current/manifest.json`):

| firm | index VersionId before -> after | `latest_date` | `gold/holdings/date=2026-09-28/` |
|---|---|---|---|
| 49financial | `OqjgF6qs...` -> `AV66zNHk...` (MOVED) | 2026-09-22 -> **2026-09-28** | 0 -> 1 revision |
| cottonwood | `ykQofbha...` -> `3JfvRUHR...` (MOVED) | 2026-09-22 -> **2026-09-28** | 0 -> 1 revision |
| inflection | `ipomYxTG...` -> `.zfZoZlA...` (MOVED) | 2026-09-22 -> **2026-09-28** | 0 -> 1 revision |

  That is the condition's "after, per firm": a NEW index VersionId, `latest_date` = the runner's pick for Monday
  2026-09-28, one revision under the date partition, on the first scheduled fire and not a hand re-fire. **D1 and A1
  are MET on the served indexes for 3 of 3 firms.**
- **Unread here:** the page read (the Holdings tab's as-of as September 28th, 2026 for a client at each firm) needs the
  local dev build, which the machine's memory reaper stopped at 12:4xZ; it restarts on Andrew's word and the walk
  follows the same hour. `holdings_publication_diff_classes.py` on the first served revision against 2026-09-22 is
  ~M's filing beside `R4_ENABLE_DIFF_20260928/`.
- **Beside it, the same morning:** the sibling schedule `irpt-holdings-performance-daily` (07:30 ET, a different
  Lambda, a different table) fired with a stale producer; that is row S205 and this seat's half
  `NEVER_WIDEN_SIGNOFF_CRO_HALF_HOLDINGS_PRODUCER_V021_20260929.md`, not this act.

## What this half signs against

- Request blob `342f04c1`; the CTO's R4 condition 4 (`SIGNOFF_HOLDINGS_PRINCIPALS_DISPATCH_20260925.md` @`6c5c27a666`).
- The re-minted packages, members-sha256 `94f2e3433d9ecc018027418ebb057c4ce6bfd2bb5baa45b8edb697f036421e5e`
  (ledger `irpt-holdings-packages-m-20260928c`, commit `71d1099644`).
- The QA fire of 2026-09-28 23:32:43Z (commands `f61bb631...`, `3f2dca9e...`, `58cbeda0...`, all Success rc 0) and its
  three candidates; the served indexes' three VersionIds as read here.
- The blast radius above: one revision per firm per weekday, the three code lines, real custody movement; the
  rollback per key.
