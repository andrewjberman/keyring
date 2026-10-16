# G4 filings task: registered and enabled on dell1 (`2.0.0_SA_COO~R1`, 2026-10-16 05:4xZ / 01:3x ET)

**Authority:** both halves of the never-widen pair signed on the same bytes: COO half `NEVER_WIDEN_ROUND108_G4_FILINGS_FIRST_FIRE_COO_HALF.md` @`baf60bebcb` (sha256 `4bb06b3aba54d00d83ddbfad9d00d3c18fc62a1e6013135173ed9002dbea0e1f`, re-computed before the act: equal), CTO half `NEVER_WIDEN_ROUND108_G4_FILINGS_FIRST_FIRE_CTO_HALF.md` @`b619a274a1` (msg 6526). Andrew's word "Yes we definitely want to activate the batching". The cap: `first_fire_limit.json` `{"filings": 20}` (merged `a5abb5aa9f`).

## What was done (two acts, in the pair's order)

1. `python -m lib.research.llm_batch.register --apply` (rc 0): `OK OpalResearch-FilingsAnalyzer created DISABLED (read-back Disabled)`, `OK OpalResearch-ExecManagement created DISABLED (read-back Disabled)`, `OK OpalResearch-Scores created DISABLED (read-back Disabled)`, `APPLY: 3 task(s) created DISABLED`. Before: `OpalResearch*` 0 of 205 scheduled tasks on dell1 (read 05:2xZ). Description of each task names owner `2.0.0_SA_COO~R1`.
2. `schtasks /Change /TN "OpalResearch-FilingsAnalyzer" /ENABLE` (rc 0). Read-back by `Get-ScheduledTask`: FilingsAnalyzer **Ready**, ExecManagement **Disabled**, Scores **Disabled**; all three NextRun `10/16/2026 7:30:00 AM` (dell1 local, Eastern Standard Time; now 01:35 -04:00), so the first fire of the filings task is 11:30Z today, a trading day.

## What the first fire runs (printed by `python -m lib.research.llm_batch.run filings --print-command`)

`python -m lib.research.filings.batch --universe newest --write-pool --limit 20`, gated by `run.py`'s event decision (`first run: no last-run record` reads due on a dry run, read 2026-10-16).

## Not done, by design

The management and scores tasks stay Disabled (each needs its own pair). The cap is not lifted. No other task, alert or monitor was created.

## What the next acts read (owed by this seat)

- After the first fire (`tmp/llm_batch/last_run.json` carries `filings`; the run's stderr line `LLM-BATCH task=filings ran rc=0 last_run recorded`): which names it wrote (the 20 named in the COO half), and every written analysis's `usage.usd` through `filings/v1/<key>/<accession>.analysis.json`.
- Their MEAN. At or below 0.80: lift the cap (set `filings` to null in `first_fire_limit.json`, its own commit, the CTO told). Above 0.80: back to `1.0.0_SA_CTO~DELL1` before the cap lifts (the CTO's added condition).
- Rollback if the CTO or this seat reverses: `schtasks /Change /TN "OpalResearch-FilingsAnalyzer" /DISABLE`; objects by version per the COO half.
