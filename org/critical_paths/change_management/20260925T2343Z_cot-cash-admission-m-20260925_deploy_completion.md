# Deploy Completion Record
**Date opened:** 2026-09-25T23:43:45.260517+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / CTO ruling S188 (msg 102504): R1 FAILED on the 09-28 COT run (z09308463 / z09308511 cash served as fixed_income FCASH; row W41-S1), stays OPEN, no rollback; dispositioned by the S173 re-point of COT gold to etf-classifications (after the POSN fill) (held since 2026-09-25T23:45:54.600178+00:00)
**Deploy:** S138 cash: deploy COT gold C_06 with cash in MIX_ASSET_CLASSES (own act, CTO @d257eb67aa; render on PROD 36a37afc portal-v2.1.188)
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 96.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | s3-prefix | opal-data-cot gold C_06.client_mix_timeseries.py | safe-deploy MATCH line (comp-pipescript) for C_06 | HALT_ACK=1 safe-deploy: DEPLOYED [cot] C_06.client_mix_timeseries.py -> code/gold/; VERIFY OK comp-pipescript deployed; OK safe-deploy gate PASS (code 7fd8149448 on CLOUD 75cc52a285); s3 read-back line 173 carries cash; version LmvfjXlBXUIGtyu0ax2a0EcILSNUMuZ3, rollback to prior version HJa2V4VY3FSB9CicsbkTJyLTAL.l.bjv (act-1 bytes, 20:33:53Z) | CLOSED 20260925T234537Z |
| R1 | verify | the first scheduled COT gold run after this deploy | z09308463 (0.37 cash at 09-22) shows a cash slice at its measured amount with shares summing to 1; all-cash z09326138 or z09308511 shows 100% cash |  | OPEN |

## Log

- 20260925T234345Z OPENED by 2.0.0_SA_COO~M with 2 leg(s)
- 20260925T234537Z LEG D1 closed: HALT_ACK=1 safe-deploy: DEPLOYED [cot] C_06.client_mix_timeseries.py -> code/gold/; VERIFY OK comp-pipescript deployed; 
- 20260925T234554Z HELD-SOVEREIGN-GATED gate=external/leg R1 reads the next scheduled COT gold run's outputs; COT gold runs on trading
- 20260929T002350Z HELD-SOVEREIGN-GATED gate=external/CTO ruling S188 (msg 102504): R1 FAILED on the 09-28 COT run (z09308463 / z09308
