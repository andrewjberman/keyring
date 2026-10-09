# CTO site-Z half -- MDPF_DEMQUE.TO-DQ-t14: the Bloomberg budget-ledger uploader's WORLD acts (one S3 write + one site-Z schedule)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~08:2xZ. **Ask:** `0.7.0_AE_CloudOps~ZQ` msg 32542 (sender unverified at the broker; the ask
was checked against the file carriers below). **Order:** `org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t14.sitez-demand-ledger-uploader.md`,
step 5 (`1.0.0_SA_CTO~Z` signs the site-Z half). **Plan read:** `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T14_REVIEW.md` at HEAD.

## VERDICT: SIGNED for the four acts in the plan's "Exact proposed WORLD acts", on the code at `492cb5a2f1` (already in `box/sitez`), under conditions C1-C5.

## What this seat read at signing

| read | result |
|---|---|
| `492cb5a2f1` | 3 files: `bbg_ledger_upload.py` +134, its test +99, the review. `git branch --contains` lists `box/sitez`, so the code is on the shared tree |
| `bbg_ledger_upload.py` whole | imports `bbg_budget` (ledger dir only) and `lib.opal_naming.address`; no producer import; field counts read by `ast.literal_eval`, never executed; `upload()` writes ONE object, `put_object` to the builder address `.../dt=<day>/ledger.jsonl`, overwriting the same day; an empty or malformed day refuses; a dry run creates no client |
| `OPAL_BBGTML_daily_pull` (Get-ScheduledTask) | `cmd.exe /c "<shared workspace>\integrations\bloomberg\pipeline\scheduled_daily_pull.cmd"`, user `Opal Bloomberg`, Interactive. LastRunTime 2026-10-08 07:00:01, **LastTaskResult 50**, next 2026-10-09 07:00 |
| the plan's write identity | STS caller `user/Andrew_Berman`; simulate `s3:PutObject` on the exact object ARN: allowed. Accepted as stated, not re-read here |

## Conditions (each checked at the act)

- **C1. The new task runs the SHARED workspace tree**, the same convention as `OPAL_BBGTML_daily_pull`, not a linked worktree. A worktree
  is removed by `/cleanup`, and the task would then fail every day. The script path is quoted, because the workspace path has a space.
- **C2. A UTC day with no `bbg_budget_<day>.jsonl` exits 0 and prints `SKIP: no ledger file for <day>`**: a wrapper `Test-Path` before
  the Python call is enough. A day with no draws is not a failure. Every other error still propagates its exit code.
- **C3. Before the initial apply, read `head-object` on the exact target and record it** (expected: absent). Rollback restores that
  state: delete only the new object if it was absent, otherwise restore the prior version.
- **C4. The NEVER-2 change-management entry opens before the first write and closes after the task read-back.** The entry names the
  task's action, trigger, principal and source commit.
- **C5. `OPAL_BBGTML_daily_pull` is not touched**, and the uploader makes no Bloomberg call (the order's BOUNDS).

## Accepted as the plan states it

- One initial `--apply` for the latest existing UTC day (2026-10-08), then AC2 read-back with the served bytes compared to the local
  conversion.
- `OPAL_DEMQUE_bbg_ledger_upload` daily at 08:30 Eastern for the PREVIOUS UTC day, a closed day, after the 07:00 pull. No monitor and no
  other timer.
- Cells carry claim `held` (requested or returned rows times a stated width, never the vendor's meter). Ambiguous modes (`market-range`,
  `amgt-model-block`, non-`batch-` holdings) write `cells: null`, `claim: absent`.

## Observation, not a condition

The 07:00 pull's LastTaskResult on 2026-10-08 is **50**, not 0. That is not this order's subject, and the uploader reads whatever
`record()` wrote. It goes to the Bloomberg seat's record.

-- 1.0.0_SA_CTO~Z
