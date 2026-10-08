# CTO never-widen half -- ETFS_RIVALS round 27, RIV-tw-1: the MERGE that puts the top-up writer in the scheduled vehicle's file, switch OFF

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-08 ~05:5xZ. **Ask:** `2.0.0_SA_COO~RV` msg 31587.
**COO half:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round27/NEVER_WIDEN_HALF_COO_R27_TW1_MERGE.md` @09e99a3532
(SIGNED), read whole.

## VERDICT: SIGNED for the merge of branch `wk-ETFS_RIVALS-19` @de25db03ea, AFTER the 2026-10-08 11:00Z run on the unchanged file is read. Two conditions.

The act is a merge. On this box it is a deploy of `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` to the scheduled vehicle.
No Lambda, no S3 write, no vendor call. The file is outside `integrations/bloomberg/`, so Andrew's no-modify order is not touched.

## What this seat read at signing

| read | result |
|---|---|
| the switch in the environment (`RIVALFUNDS_HISTORY_OWED`), process, User and Machine | empty, empty, empty |
| the name in the working tree under `integrations/`, `data/`, `infra/`, `lib/`, `.tools/` and in any `.cmd` or `.ps1` | 0 files. (The branch that adds it is not merged, so the product file does not carry it yet.) |
| **the scheduled task's own definition**, which the COO half says it did not open: `Get-ScheduledTask OPAL_BBGTML_daily_pull` | one action, `cmd.exe /c "...\integrations\bloomberg\pipeline\scheduled_daily_pull.cmd"`. No environment is set by the task. |

So on this box nothing sets the switch, at any of the four places it could be set. Not read by this seat: the 113 lines, the two
check files, the fixture.

## The four points of msg 31584: accepted as the COO half states them

1. Switch OFF is identical to the run before: sink calls in order, client requests, printed lines and the result, for unset,
   empty and "0"; a sentinel module shows the owed code is not imported on that path.
2. The switch is one environment variable, a value only for exactly `print` or `ask`.
3. `print` writes one line and nothing else: 0 requests, 0 budget checks, 0 ledger lines, 0 puts.
4. The rollback is one revert; the pair's read is the first scheduled run after the merge.

## C1 -- neither `print` nor `ask` is set by the merge, and each is its own act

- `ask` waits on Andrew's recorded answer on a standing Bloomberg request, relayed by this seat (PRD v0.19 ADDENDUM G.2).
- `print` calls no vendor and writes nothing, so it needs no word of his. It is still a change to what a scheduled job does: this
  seat rules it on a one-line ask naming WHERE the variable would be set, since the task sets no environment and the only places
  left are the User or Machine environment of this box (which every session would then inherit) or the `.cmd` under
  `integrations/bloomberg/` (which the no-modify order bars).

## C2 -- three things the COO half names are closed before `ask`, not before this merge

- **The top-up writes a NULL currency.** A close with no currency draws no curve. And R13 of the round-25 analysis requires each
  close to carry the trading date it belongs to. Both are in the writer before `ask` is ever set.
- **The owed window ends a day early** (the report date is passed as the day). Stated; a unit is a day late, never lost.
- **`HISTORY_OWED_CAP` is 5,000 units a run**, the issuer's number: 184,600 owed is 37 runs. Not ruled here. It is ruled with
  `ask`, against the pacer's day (120,000 less the vehicle, the AMGT_CORPUS fire reckoned at 66,879, and the reserve).

-- 1.0.0_SA_CTO~Z
