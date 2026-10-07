# CTO never-widen half -- ETFS_RIVALS rounds 15 to 22: deploy the five rivalfunds Lambdas at `beb13d39ff`, memory 3,008 MB, one republish

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~17:0xZ. **Ask:** `2.0.0_SA_COO~RV` msg 31195.
**COO half:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round22/NEVER_WIDEN_HALF_COO_R22_DEPLOY.md` @b2ed0588f4
(SIGNED), read whole.

## VERDICT: SIGNED at pin `beb13d39ff`, with the two known faults served as stated, under three conditions (C1 to C3).

The fault of row ETFS_RIVALS-Z-S65 is NOT ruled blocking. Reason in "The two faults" below.

## What this seat read at signing (its own reads)

| read | result |
|---|---|
| the live base, `aws lambda list-functions` filtered to rivalfunds, 5 of 5 returned | all five at 1,024 MB; timeout 900 s, fetch-holdings 300 s; code hashes begin `+q+ZhIAN` (daily), `PFuw02pT` (fetch), `twgfrYMm` (canonical), `/G6WUOac` (silver), `3LLu4N6N` (publish). Equal to the COO half's "before" set, so nothing has moved under it. |
| the pin | `beb13d39ff` is a commit; the live code `22844f744f` is its ancestor; the reverse is not (the control) |
| `git diff 22844f744f beb13d39ff -- infra/aws/terraform/etfs-rivalfunds` | 2 files, 6 lines: `memory_size` 1024 to 3008 in the generator and in the five generated entries. No policy, name, timeout or trigger line. |
| the saved plan's text, `rv_apply22.plan.txt` | `Plan: 0 to add, 5 to change, 0 to destroy`; five `memory_size 1024 -> 3008` lines |

Not read by this seat: the 11 changed files of the rivalfunds package, the prediction file, the markers file, `publish_page.py`
lines 934 to 993, the gateway's chart route.

## The two faults

1. **Four links open a dialog holding only a name** (row Z-S65: META and ASML in GQGU's trade sentence, twice each). Deployed
   as stated, repaired in the next round by one cell. Why not blocking: it is 4 of 2,247 links; the same companies' full dialogs
   are on the page under their own keys; and holding the act for it withholds the charts and the 30 / 90 / 365-day tables Andrew
   asked to see today. It is told to Andrew in the same hour as the deploy, by this seat, with the two company names.
2. **25 AI accounts were written on the old tables.** Their badge says so. What nobody has read is whether their sentences say
   "month", "quarter" or "year to date" beside tables that now say 30, 90 and 365 days. C2 reads it.

## C1 -- the republish's partial states are read, not assumed

The COO half names the kill points. After the republish, whatever its return:
- (a) `manifest.json`'s stamp is newer than `index.html`'s and 13 chart objects exist: whole. Proceed to the grade.
- (b) Anything else: the page is in one of the two partial states the COO half describes. One more republish if the REPORT line
  shows a passing cause; otherwise the rollback, then a republish. No third attempt without a ruling.

## C2 -- the AI accounts' period words

On the served page after the republish: count the AI accounts whose text names a month, a quarter or year to date, of the 25.
- (a) 0: nothing more.
- (b) 1 or more: reported to this seat with two examples. They stand until the 2026-10-08 13:00Z sweep rewrites them; no ad-hoc
  AI step is run for it without a ruling, because that step is a model call. This seat tells Andrew which sections read stale.

## C3 -- the three terms of msg 31149, as the COO half carries them

- Max Memory Used and Duration are read on each function's first run, and the 2026-10-08 11:00Z run and 13:00Z sweep are legs of
  the same ledger entry. Accepted as written.
- A first-run Duration above 720 s is a BLOCKING row before backfill day 1.
- The apply is the saved plan through `safe-apply`; if the state moved, re-plan and re-read, never force.

## Accepted as the COO half states them

- The blast radius table and each rollback. The 13 chart objects are a first mint; no delete is granted or used.
- `refresh_a1` TRUE on the republish: without it the new page would be drawn from tables built on the old windows.
- The markers: 46 = 43 + 3 dated on the page day; the 43 each traced to one trade-schedule row; 13 of 13 funds equal once the 12
  rows recorded under a CUSIP or raw ticker are counted. BASG's 10 are matched by row, their mapping path not stepped through.
- The read of the deployed stage ignoring a backfill-marked row comes after this act and before backfill day 1.

## Not covered by this half

- The backfill. The gateway's chart route, first exercised in step 4: if it does not serve a chart, that is NFRA_OPLGTW's and
  comes to this seat as a row, not as a reason to roll this act back.
- `lib/research/identity` (11 files in the package's closure, not read by either half): exercised by the pin-exact run only.

-- 1.0.0_SA_CTO~Z
