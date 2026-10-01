# NFRA_TRNSPT -- status (FAST: /closer-drive under lease `NFRA_TRNSPT`, the one remaining round)

Seat `2.0.0_SA_COO~D` (CLAUDE), holding this round in place of the project's own lane `2.0.0_SA_COO~T` (dark). Authority:
1.0.0_SA_CTO RULINGS batch 82 @dcdd1989d5 (msg 103707, 2026-10-01T11:18Z):
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`; the round's content is
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_2_20261001.md` section 2. Contract: PRD
`org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` v0.1 (ENDPOINT unchanged). Reviewer `3.0.0_SA_CVO` (grades each
landed pin after the fact). **As of 2026-10-01T12:5xZ.** An Investor Reporting item that becomes ready INTERRUPTS this round
(batch 82 item 3); DSGN_REBRND's round 3 stays behind both (item 6).

## Pins

| What | Value |
|---|---|
| Lease | FAST `NFRA_TRNSPT` until 2026-10-01T15:40:09Z, seat 2.0.0_SA_COO~D, surface `data/transcripts`, `org/missions/D9/NFRA/NFRA_TRNSPT`; armed by this seat 11:40Z (`org/mcp/drive-mode.log`) |
| FULL -> FAST boundary | 17 of 17 task orders read `complete` at 11:25Z (rounds 1 and 2); no worker was running, nothing superseded, nothing new cut |
| Code pin | workspace CLOUD `2b003f0b99` (the caller and the lander), on `bcadf2fd94` (row S14). LOCAL; the push is 0.0.0_AB_MSTR's |
| Suite | `python -m pytest data/transcripts/scripts/tests -q`: 155 passed at 2b003f0b99; no tracked record modified after it. Deployed layout: `r2_bundle_import_check.py` BUNDLE-IMPORT-OK files=32 |
| The real run | `deliverables/2.0.0_SA_COO~D/R3_REAL_RUN_20261001.md`: one admitted message, route to silver, 12:2xZ-12:4xZ |
| The route | `https://mcp.opalinvest.dev/hx/mail`, exercised from the laptop: 401 with no bearer, the bearer read by name under IAM user Andrew_Berman, three GETs answered 200 for a table sender's message |

## Live thread

State: LIVE BY HAND for the communications workstream, for ONE message. A real admitted message went route -> recorded
directory -> precision scan -> bronze (4 objects, byte for byte, the PDF's hash equal to the route's and to site Z's
read) -> silver (1 row, held out) -> read back by a named reader. It is NOT live as FWD-7 asks: a seat fetched it by id;
the ordinary daily run cannot enumerate mail without a listing route.

## Landed this round

| # | Pin | What | Check |
|---|---|---|---|
| 1 | `bcadf2fd94` | ROW S14: the planted-wipe tests write their gate records to a temp path and compare with the committed ones; one explicit command writes the committed records | suite 134 passed; `git status` clean of tracked records after the suite and after the command; a stale committed record is refused (control) |
| 2 | `2b003f0b99` | THE LAPTOP CALLER (`outlook/gateway_mail.py`) and bronze that takes its answers: the one attachment unwrapper reads three shapes; C-DEDUP's primary key (`internetMessageId`); each PDF's bytes landed beside its message, named by hash; silver reads bronze through the unwrapper (it would have raised on the first real row) | 21 new tests, suite 155 passed; bundle import OK (CTO rule 103374); commit-gate 7 of 7 |
| 3 | this commit | THE REAL RUN and its record. The control (batch 82 item 4): today's message (received 2026-07-06) is NOT the one the project's row names (2026-08-11); it is another admitted message, admitted by this project's own criterion | every figure in the record was read back from S3, not from a run's own line |

## Rows, as this seat reads them (the grading is 3.0.0_SA_CVO's)

- **S13** (no byte-exact path): MET for the route. An admitted message's bytes reached the laptop without passing
  through a model, verified by hash and length.
- **S9** (land the recorded real sample; FWD-7 has no real row until then): a real row exists in bronze and silver.
  The message is not the one the row's remedy had in mind (see the control).
- **W4-S8** (measure the held-out rate on the first real rows): 1 of 1 held out; 5 names replaced; 14 unknown
  capitalised words flagged. The stated limit is not yet written where a reader meets the data (next item 1).
- **S14**: fixed (item 1).
- **S2** (the fallback id on every row): the headless route returns `internetMessageId`; the row landed today carries
  the primary key. Rows landed through the interactive tools would still fall back.

## Write claims

- `2.0.0_SA_COO~D`: `data/transcripts/scripts/outlook/silver.py`, `wipe.py` (next item 1).

## Next (in order)

1. **Review Q2 / row W4-S8's remedy** -- the wipe's stated limits written where a reader meets the data: the silver
   parquet's own schema and column notes (carried in the file), from one text in `wipe.py` that the gate record's
   limit text is pinned to. Then the date's silver is rebuilt so the served file carries it.
2. **The sidecar's source label** -- a recorded directory says where its answers came from (`/hx/mail`), so a sidecar
   stops reading `replay` for a route-recorded message. New messages only; a landed sidecar is never overwritten.
3. The thread trace re-run and the silver census for the transcripts workstream (FWD-1, FWD-2) after the import
   changes of this round.
4. The unattended daily pull over the listing route, the day it exists (parked below).

## Parked (one line each, owner + the condition that un-parks it)

- **A headless LISTING route** (sender, received-date window, has-attachment, paged): owner 1.0.0_SA_CTO to order from
  site Z (DECISION ask sent 12:22Z; site Z's gateway owner accepts it in principle). Un-parks FWD-7's DONE WHEN: the
  ordinary daily run, no person starting it.
- **The 14 flagged words of the first real row**: allowlist vocabulary or names? Owner: a named reader (Andrew), or
  1.0.0_SA_CTO to say whether this seat, which runs as a named reader, may list them to itself. Until then the row
  stays held out, which is the safe side. This seat counted them by shape and did not print them.
- **The message the project's row names** (2026-08-11): its full Graph id. Owner: whoever next holds an interactive
  gateway sign-in (the laptop's has lapsed; renewing it is a person act), or the listing route.
- The fourth meeting type (row S11): a person act, one calendar invite of that type (batch 82 item 5).
- The second named reader has no AWS principal yet (FWD-8): one named reader read the silver, stated in the record.

## Limits

- No reader beyond the two named ones reads a real mail row before the wipe's limit is written where a reader meets the
  data and the held-out rate is known (the CVO's condition, adopted by the CTO). The rate is known; the limit is next.
- No vendor model call, no ticket write, no alert, no schedule and no Terraform in this round. Bronze received only
  bytes that came from the route, never a copy relayed through a model.
- No message body, sender address or client name is in any committed file or broker message of this round. The
  recorded directory is outside the repository, on the laptop, and is removed when the round closes.
