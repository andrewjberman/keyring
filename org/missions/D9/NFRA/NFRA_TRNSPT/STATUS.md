# NFRA_TRNSPT -- status (FAST: /closer-drive under lease `NFRA_TRNSPT`, the one remaining round)

Seat `2.0.0_SA_COO~D` (CLAUDE), holding this round in place of the project's own lane `2.0.0_SA_COO~T` (dark). Authority:
1.0.0_SA_CTO RULINGS batch 82 @dcdd1989d5 (msg 103707, 2026-10-01T11:18Z):
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`; the round's content is
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_2_20261001.md` section 2. Contract: PRD
`org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` v0.1 (ENDPOINT unchanged). Reviewer `3.0.0_SA_CVO` (grades each
landed pin after the fact). **As of 2026-10-02T02:2xZ.** An Investor Reporting item that becomes ready INTERRUPTS this round
(batch 82 item 3); DSGN_REBRND's round 3 stays behind both (item 6).

## Pins

| What | Value |
|---|---|
| Lease | FAST `NFRA_TRNSPT`, seat 2.0.0_SA_COO~D, surface `data/transcripts`, `org/missions/D9/NFRA/NFRA_TRNSPT`; armed by this seat 11:40Z and 15:02Z (`org/mcp/drive-mode.log`), presence-extended (read FAST to 2026-10-02T02:24:11Z at 01:59Z) |
| FULL -> FAST boundary | 17 of 17 task orders read `complete` at 11:25Z (rounds 1 and 2); no worker was running, nothing superseded, nothing new cut |
| Code pin | workspace CLOUD `33176972f0` (admitted-only landing; the listing checks) on `a6c1d22d46` (the unattended pull over the listing) on `e4b89bcfb4` (the wipe's limits inside the silver parquet) on `2b003f0b99` (the caller and the lander) on `bcadf2fd94` (row S14). LOCAL; the push is 0.0.0_AB_MSTR's |
| Suite | `python -m pytest data/transcripts/scripts/tests -q`: 164 passed at a6c1d22d46; no tracked record modified after it. Deployed layout: `r2_bundle_import_check.py` BUNDLE-IMPORT-OK files=32. Transcripts: `r2_silver_census_check.py` SILVER-CENSUS bronze=30 silver=30 missing=0 empty=0 at 13:18Z (and `r2_suite_check.py` SUITE-GREEN passed=156 at e4b89bcfb4) |
| The real run | `deliverables/2.0.0_SA_COO~D/R3_REAL_RUN_20261001.md`: one admitted message, route to silver, 12:2xZ-12:4xZ |
| The positive arm | `deliverables/2.0.0_SA_COO~D/R3_APPLY_RUN_20261002.md`: `pull.py --gateway --days 7 --apply` at 02:07Z, 13 listed, 1 admitted, 4 bronze objects (hashes equal the sidecar's), silver 1 row NOT held out (0 residual flags) |
| The route | `https://mcp.opalinvest.dev/hx/mail`, exercised from the laptop: 401 with no bearer, the bearer read by name under IAM user Andrew_Berman, three GETs answered 200 for a table sender's message |

## Live thread

State: LIVE BY A SEAT'S COMMAND over the listing. 2026-10-02T02:07Z: the ordinary pull, given no message id, listed a
table sender's last 7 days through the released listing route, admitted one message by the project's criterion, and
landed it route -> bronze (4 objects) -> silver (1 row, not held out) -> read back by a named reader. It is NOT live as
FWD-7 asks: a seat started the run; the daily run with no person starting it needs the schedule (Next item 2).

## Landed this round

| # | Pin | What | Check |
|---|---|---|---|
| 1 | `bcadf2fd94` | ROW S14: the planted-wipe tests write their gate records to a temp path and compare with the committed ones; one explicit command writes the committed records | suite 134 passed; `git status` clean of tracked records after the suite and after the command; a stale committed record is refused (control) |
| 2 | `2b003f0b99` | THE LAPTOP CALLER (`outlook/gateway_mail.py`) and bronze that takes its answers: the one attachment unwrapper reads three shapes; C-DEDUP's primary key (`internetMessageId`); each PDF's bytes landed beside its message, named by hash; silver reads bronze through the unwrapper (it would have raised on the first real row) | 21 new tests, suite 155 passed; bundle import OK (CTO rule 103374); commit-gate 7 of 7 |
| 3 | `4615ecade0` | THE REAL RUN and its record. The control (batch 82 item 4): today's message (received 2026-07-06) is NOT the one the project's row names (2026-08-11); it is another admitted message, admitted by this project's own criterion | every figure in the record was read back from S3, not from a run's own line |
| 4 | `af6b7dd60c` | THE ORDER for a headless listing route (CTO batch 85 items 7-8, msg 103743), relayed to site Z 12:52Z. ACCEPTED 13:00Z-13:05Z (0.0.0_AB_MSTR 103761, 103766): NFRA_OPLGTW PRD v1.4 @dabb8e1e9f (site-Z LOCAL), the asked parameters, rows and refusals, plus site Z's terms -- a window of at most 31 days, `page_size` default 25 and cap 50, each row's sender re-checked, the page token bound to its sender and window. Release slot 5 after MX-r-8 | site Z's word; nothing is released yet |
| 5 | `e4b89bcfb4` | REVIEW Q2 / ROW W4-S8's REMEDY: the wipe's claim, what it does not claim and its three stated limits are in the silver parquet's own schema and column notes, from one text the gate record is pinned to. The served file for 2026-07-06 was rebuilt | suite 156 passed; read back from S3 at 13:17Z: table notes and four column notes present, 19 columns, the row unchanged (held_out true), 2 versions of the key |
| 6 | `a6c1d22d46` | THE UNATTENDED PULL over the listing, built before the release: `pull.py --gateway [--days 7]` lists each table sender's window (spans of at most 31 days, paged), skips rows whose sidecar is in bronze, fetches and lands the rest; a refused sender is recorded by position, never by address; a gateway that refuses every listing is a refusal, not an empty day. A recorded directory's sidecar label reads `replay:hx-mail` | 40 tests in the two touched files, suite 164 passed; bundle import OK; commit-gate 4 of 4. NEGATIVE ARM on the real gateway at 13:28Z: `--gateway --days 7 --dry-run` -> `OUTLOOK-DRY-REFUSED ... (404 None)`, rc=3. (That commit's message says 13:5xZ; the clock read 13:28Z. The message is not rewritten; this line is the correction.) |
| 7 | `33176972f0` | THE LISTING ROUTE'S FOUR CHECKS from the laptop (site Z's release, deployed_commit 0a1d9079c6, 1.0.0_SA_CTO 103880) and ADMITTED-ONLY landing: a near miss's PDF is never asked for and nothing of it is written (`--land-near-misses` restores the old behaviour) | `R3_CHECKS/r3_listing_checks.py` LISTING-CHECKS-OK n=4 at 16:09Z; suite 165 passed; bundle import OK; dry run 16:20Z 13 listed / 1 admitted / 12 near misses |
| 8 | record `R3_APPLY_RUN_20261002.md` | THE POSITIVE ARM: one `pull.py --gateway --days 7 --apply` (02:07Z) and `silver.py --date 2026-10-01 --apply` (02:16Z) | read back from S3: 4 bronze objects, sidecar hashes equal the objects', `tool_versions` hx-mail; silver 1 row, 19 columns, 0 residual flags, `held_out` false. Held-out rate over real rows: 1 of 2 |

## Rows, as this seat reads them (the grading is 3.0.0_SA_CVO's)

- **S13** (no byte-exact path): MET for the route. An admitted message's bytes reached the laptop without passing
  through a model, verified by hash and length.
- **S9** (land the recorded real sample; FWD-7 has no real row until then): a real row exists in bronze and silver.
  The message is not the one the row's remedy had in mind (see the control).
- **W4-S8** (measure the held-out rate on the first real rows): 1 of 1 held out; 5 names replaced; 14 unknown
  capitalised words flagged. The stated limits are written inside the silver file (item 5).
- **S14**: fixed (item 1).
- **S2** (the fallback id on every row): the headless route returns `internetMessageId`; the row landed today carries
  the primary key. Rows landed through the interactive tools would still fall back.

## Write claims

- None open at 13:3xZ.

## Next (in order)

1. ~~The order's four checks, then `--apply` once by hand~~ DONE (items 7 and 8).
2. **The pull's schedule and its Lambda entry** -- the handler in `infra/aws/lambda/transcripts-pull` runs the
   Teams pull only; the mail pull's own clock is a Terraform act under its own ledger and a principal that may
   read the bearer. The silver build is a separate command today; the placement says whether one clock runs both.
   Outside this lease's surface: a 1.0.0_SA_CTO placement, asked 2026-10-02.
3. The transcripts thread trace re-run (FWD-1). The census (13:18Z) and the suite are in the pins.

## Parked (one line each, owner + the condition that un-parks it)

- ~~The listing route's RELEASE~~ released by site Z 15:34:29Z (deployed_commit 0a1d9079c6); checked 4 of 4 (item 7).
  FWD-7's DONE WHEN (the ordinary daily run, no person starting it) still needs the schedule (Next item 2).
- **The 14 flagged words of the first real row**: allowlist vocabulary or names? Owner: a named reader (Andrew), or
  1.0.0_SA_CTO to say whether this seat, which runs as a named reader, may list them to itself. Until then the row
  stays held out, which is the safe side. This seat counted them by shape and did not print them.
- **The message the project's row names** (2026-08-11): its full Graph id. Owner: whoever next holds an interactive
  gateway sign-in (the laptop's has lapsed; renewing it is a person act), or the listing route.
- The fourth meeting type (row S11): a person act, one calendar invite of that type (batch 82 item 5).
- The second named reader has no AWS principal yet (FWD-8): one named reader read the silver, stated in the record.

## Limits

- No reader beyond the two named ones reads a real mail row before the wipe's limit is written where a reader meets the
  data and the held-out rate is known (the CVO's condition, adopted by the CTO). Both are now true; admitting a
  further reader is still not this seat's act.
- No vendor model call, no ticket write, no alert, no schedule and no Terraform in this round. Bronze received only
  bytes that came from the route, never a copy relayed through a model.
- No message body, sender address or client name is in any committed file or broker message of this round. The
  recorded directory is outside the repository, on the laptop, and is removed when the round closes.
