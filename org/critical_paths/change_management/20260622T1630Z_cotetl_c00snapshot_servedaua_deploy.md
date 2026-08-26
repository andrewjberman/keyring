# Deploy-completion ledger — ADVI_COTETL.AUAFIX-C00SNAPSHOT (cot served-AUA snapshot-perf fix)

> **SUPERSEDED (gate-tracking) by the deploy_ledger.py tool-ledger** `20260622T1650Z_cotetl-c00snapshot-servedaua_deploy_completion.md` (slug `cotetl-c00snapshot-servedaua`), registered per COO so the `--red` gate sees it (a hand-written markdown is gate-invisible). The tool-ledger is authoritative: 4 legs proven (deploy/firmsep/rerun/servedverify), `cvocert` open -> closes on CVO firm-AUA cert. This file remains the human-readable narrative.

**Opened:** 2026-06-22 ~1630Z (deploy-start)
**Owner:** 0.4.0_DS_ClientPlatform
**Authority:** CTO-ruled FIX (A) + branch-confirmed (162916Z); Andrew-direct same-day P0; COO GO (160525Z)
**Class:** gold-script code deploy (cot tree only, firm-separated); NEVER#1-adjacent (firm-separation verified)

## What
The 4th-layer COTETL served-AUA fix: cot's served firm-AUA was wired to the bd-inherited
lots-FIFO performance lineage (D_00 clients_tab <- account_performance C_03 <- C_00 <-
account_gains <- lots) which cot's snapshot-first model does NOT feed (lots tier empty) ->
served AUA frozen 06-09 while canonical_holdings/positions_cube advanced to 06-18. FIX (A):
add a cot snapshot-perf branch (the leaner BD methodology's first instantiation) so
account_performance (C_03) + nna (C_01) derive total_aua/date from canonical_holdings (the
06-18 BD snapshot), NOT the dead account_gains chain.

## Legs
- [x] DS commit: C_03.account_performance.py + C_01.canonical_nna.py (5c80bf6ca)
- [x] DS deploy: aws s3 cp -> s3://opal-data-cot/code/gold/ (Rule 13); md5/etag MATCH (both)
- [x] comp-pipescript deployed (firm-separated): ONLY cot tree changed; 49F (opal-data-bd) C_03/C_01/C_01b/C_01c MATCH = zero-touch
- [x] AE: synced-sha==5c80bf6ca proven + full-chain gold re-run (cot-exporter, gold 62baea04 Success)
- [x] DS SERVED-VERIFY (independent ground-truth): clients_tab/header_metrics data_as_of=06-18 + total_aua=$395,300,238 (off $373M/06-09); account_performance contiguous 04-22->06-18 (707 accts/56 dates); nna 06-18. THE FREEZE IS BROKEN.
- [ ] CLOSE-CONDITION: CVO firm-AUA cert (RAVC 164631Z). Anomalies grounded: #1 D_00 707->694 filter (pre-existing, CVO-confirm 13-excl); #2 nna-identical = EXPECTED (cot 04-22 onboarding); #3 fee_count/707-vs-694 = OUT-OF-SCOPE fee-side (AUAFIX-L6).

## Notes
- C_03 ds-commit-gate CLEAN (removed 1 pre-existing unused import). C_01 ds-commit-gate: py_compile
  + AST + FA(future-import) PASS; BLOCKED only on 8 pre-existing bd-fork ruff violations (1 unused
  import :46 + 7 extraneous-f-prefix 1014-1055, ALL outside the change) -> RULE15 justified gate-note
  bypass; separate per-class cleanup TO flagged to CTO/COO.
- C_02 (client_performance) = non-blocking follow-on (D_00 fallback only; C_03 now primary).

**Status:** CLOSED -- SUPERSEDED. Re-stamped 2026-08-26 by `2.0.0_SA_COO`.

> This line read `OPEN` for 65 days and was WRONG THE WHOLE TIME. The authority this file names in its own second line -- `20260622T1650Z_cotetl-c00snapshot-servedaua_deploy_completion.md` -- reads **`Status: CLOSED -- nothing stranded -- closed 20260622T165318Z`**, with all 5 legs proven (deploy md5==etag MATCH 5c80bf6ca; firmsep 49F zero-touch; rerun AE synced-sha, gold 62baea04 Success; servedverify clients_tab 06-18 / $395,300,238; cvocert CVO firm-AUA cert, COO 165229Z). **The deploy closed 23 minutes after this narrative was written. It was never stranded.**
>
> ⛔ **WHY IT SURVIVED, AND IT IS NOT A GATE BLIND SPOT.** A supersession pointer is a CROSS-FILE relation and every predicate in `deploy_ledger.py` is SINGLE-FILE -- so a content-classifier correctly reads this as deploy-shaped-and-non-terminal and cannot see that a different file is its authority. `0.4.0_DT_ClientPlatform~C`'s 5 fixes (`ec3639cad5`) are unaffected; this is a named RESIDUAL, not a defect in them.
>
> ⚠ **AND IT WAS FOUND BY ROUTING, NOT BY CLASSIFYING.** This entry was reported as "the find that justifies the whole sweep" -- an OPEN deploy invisible for 65 days. Opening it to identify an OWNER is what revealed WHAT it was. The supersession line sits ABOVE the status line, in a file whose status line is the thing under classification.
>
> The narrative below is preserved verbatim and remains the human-readable account. **The tool-ledger is the terminal record.**
