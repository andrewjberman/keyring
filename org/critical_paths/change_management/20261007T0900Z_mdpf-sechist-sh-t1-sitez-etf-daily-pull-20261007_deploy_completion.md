# Deploy Completion Record
**Date opened:** 2026-10-07T09:00:43.319915+00:00
**Status:** OPEN
**Deploy:** MDPF_SECHIST SH-t-1: site Z working tree takes etf_daily_pull.py at the bytes of 20a69d5a62 (history backfill on the one Bloomberg budget ledger)
**Authored by:** 2.0.0_SA_COO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | site-Z CLOUD pull-merge of origin CLOUD by 0.0.0_AB_MSTR~Z on Andrew's word, outside 10:30Z-12:00Z | merge commit hash |  | OPEN |
| L2 | verify | working-tree integrations/bloomberg/pipeline/etf_daily_pull.py at site Z | git hash-object reads blob 0e399c9523f60511107b8491b9894c892a6aeb60 and py_compile rc 0 |  | OPEN |
| L3 | verify | first scheduled OPAL_BBGTML_daily_pull run after L1: s3://opal-data-etfs/bbg/<asof>/run_manifest.json | manifest names the planned securities, history_backfill_error null, leg exit 0, and a backfill line in the day's bbg_budget ledger file |  | OPEN |

## Log

- 20261007T090043Z OPENED by 2.0.0_SA_COO~Z with 3 leg(s)

## PRE-MERGE MEASUREMENT -- the condition of the CTO half (2.0.0_SA_COO~Z, 2026-10-07 ~09:0xZ, site Z)

Authority: CTO ruling msg 30730 (1.0.0_SA_CTO~Z); CTO half SIGNED at 20a69d5a62 by 1.0.0_SA_CTO~DELL1
(`git show origin/CLOUD:org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_MDPF_SECHIST_SH_T1_SITEZ_DEPLOY_20261007.md`,
origin CLOUD 34a81624ca); COO half SIGNED by 2.0.0_SA_COO~H1 (request @c21432885a, AMENDMENT 1).

**RESULT: EQUAL -- branch (a), the deploy lands. `RIVALFUNDS_BBG_BUDGET_DIR` is not set and need not be.**

| arm | user | RIVALFUNDS_BBG_BUDGET_DIR | bbg_budget.ledger_dir() |
|---|---|---|---|
| ETF leg, launcher line 247 environment | Opal Bloomberg | unset | `C:\Users\Opal Bloomberg\AppData\Local\opal_bbg_budget` |
| rival-funds collector, launcher line 431 environment (PYTHONPATH set) | Opal Bloomberg | unset | `C:\Users\Opal Bloomberg\AppData\Local\opal_bbg_budget` |
| collector's own import (`from rivalfunds import bbg_budget`) | Opal Bloomberg | unset | `C:\Users\Opal Bloomberg\AppData\Local\opal_bbg_budget` |
| NEGATIVE CONTROL, variable set to `C:\negctl` | Opal Bloomberg | `C:\negctl` | `C:\negctl` |

How it was measured, and its limit:
- The two legs are not two tasks. `scheduled_daily_pull.cmd` launches BOTH from one cmd process: the ETF leg at line 247
  (`"%PY_AWS%" -u "%ETF_PULL%"`) and the collector at line 431 (`"%PY_AWS%" -u -m rivalfunds.collector_bloomberg --mode daily`),
  same interpreter (Python311). No line of the launcher sets `RIVALFUNDS_BBG_BUDGET_DIR` or `LOCALAPPDATA`
  (every `set` line read; repo-wide the variable is named in 16 files, none a .cmd, .ps1, .bat or .vbs).
- Scheduled task `OPAL_BBGTML_daily_pull`: user `Opal Bloomberg`, logon Interactive, run level Limited (9 Opal tasks of 209
  read; no separate rival-funds task exists). The variable is unset at Machine scope and at User scope.
- The four arms were run through `cmd.exe /c` with the launcher's own `set` lines copied, by this seat's session, which is
  the same Windows user. It was NOT run inside the Task Scheduler's own process.
- Evidence from the real scheduled run: the 2026-10-06 07:00 ET log (`bbg_tplus1_20261006_070001.log:87`) carries collector
  batch `batch-20261006T110635Z`, and that batch id is a `daily` line in
  `C:\Users\Opal Bloomberg\AppData\Local\opal_bbg_budget\bbg_budget_2026-10-06.jsonl` (17 lines: backfill probes, daily, names).
- The new bytes reach the same module: `etf_daily_pull.py` at 20a69d5a62 globs `data/*/scripts/rivalfunds/bbg_budget.py`
  under the repo and imports it (lines 550-556), so both legs call one `ledger_dir()`.

Bytes: origin CLOUD carries the file at exactly the bytes of 20a69d5a62 (blob 0e399c9523f60511107b8491b9894c892a6aeb60;
20a69d5a62 is an ancestor of origin CLOUD 34a81624ca). The site-Z working tree and HEAD read blob
c9de003ed686b6da68512be7afad62de5d529f31 before the merge.

Rollback per key: as the COO half states (restore the file to its 6c7d8b29d6 bytes in the working tree; rewrite each
`history_topup` since the deploy to its production window; drop the three `history_backfill*` manifest fields; delete the
`backfill` lines this leg added to the day's ledger file; re-run gold and the publisher).

Not in this entry: the Positioning gold and publisher release beyond the four keys the request names.
