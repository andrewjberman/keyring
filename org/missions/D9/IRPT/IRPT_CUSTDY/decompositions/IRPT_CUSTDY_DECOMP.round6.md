# IRPT_CUSTDY decomposition -- ROUND 6 (issuer 2.0.0_SA_COO~K2; drafted 2026-10-07 ~13:2xZ, dell2)

**Status: DRAFT -> ISSUED in one issuance** (the issuance commit carries the `fanout:` line).

**Cut on:** the round-5 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_CUSTDY_ROUND_5_20261007.md` @f6160117ce
(`1.0.0_SA_CTO~DELL2` msg 610), section 4: E1-E3; rulings S10, W13-S2, W12-S1. receiving-check: UNCHECKED (no checker for a round analysis).

**Rule 24.** Domain: E1-E3. Three cells; E1 and E3 both change `client_report_figures.py`, so they are ONE chain (one worker queue, E1 then
E3); E2 touches neither.

## Measured constraints (dell2, ~13:2xZ)

1. **The template is not on DEV:** `ClientReportDocument` exists only on portal branch `wk-IRPT_CUSTDY-12-portal` @99addd80 (CTO review PASS
   with the not-covered note, msg 581; DEV landing waits on Andrew). E1's portal edits are cut on THAT commit: the slot's portal worktree is
   provisioned with `--portal-ref 99addd80 --node-modules link`, and its new commit extends that branch line.
2. **Not-covered today** (round 5, row W13-S2): `hop3_real_run.py` writes a not-held account as its own household document carrying
   `not_covered: {reason}` and no figures, outside `client_report_figures.validate_document` (which would reject it). Ruling W13-S2:
   `validate_document` admits it with its reason and without the per-household blocks; the producer never folds it into another household.
3. **The probe's time** (W12-S1): `hop3_real_run.py` runs ~140-1500 s on dell2, inside the SI anchor probe's S3 listing
   (`client_report_figures.py` ~:308, called from ~:710/:754/:861). Ruling: read a manifest or a narrowed prefix instead of listing.
4. **Bun** (rules 106215/106221, msgs 500/508/516/555/563): `bun --no-install` only, inside a portal tree with node_modules linked; never
   `bun install`; an unresolved import is STOP.
5. **Rows are committed the turn they are written** (CTO section 3: the corpus gate reads the shared working tree).

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `CU-f-1` (E1) | not-covered accounts end to end: `validate_document` admits one with its reason and refuses one without; the template renders `not covered: <reason>`; no not-held account under another household | FWD-1 | NOT-EVALUATED | dell2 | LOCAL | A, `0.9.0_WK_IRPT_CUSTDY~14` |
| `CU-f-3` (E3) | the SI anchor probe bounded: hop 3 for the chosen advisor in at most 120 s, timed; SI labels unchanged | FWD-1 | NOT-EVALUATED | dell2 | LOCAL | A (after CU-f-1), `~14` |
| `CU-f-2` (E2) | the tracer retired (S10): the test removed with a commit naming why; the suite 0 failed | FWD-1 | NOT-EVALUATED | dell2 | LOCAL | B, `0.9.0_WK_IRPT_CUSTDY~15` |

## Write sets

- **CU-f-1:** `client_report_figures.py`, `hop3_real_run.py`, `tests/test_not_covered_validation.py` (new); portal (on 99addd80):
  `render/clientreport/ClientReportDocument.tsx`, `render/clientreport/types.ts`, `render/fixtures/clientreport.firm-a.json`,
  `__tests__/clientreport/not-covered.test.tsx` (new).
- **CU-f-3:** `client_report_figures.py`, `hop3_timed_check.py` (new), `tests/test_si_anchor_bounded.py` (new).
- **CU-f-2:** `tests/test_advisor_projection_refused.py`, `none_source.py`.
- (python paths under `data/assets/scripts/gold/irpt_custody/`; portal paths under `portal/src/pages/InvestorReporting/`.)

**Ordering and fan-out:** `fanout: 2 of 2 chains, cap 8` -- A (CU-f-1 then CU-f-3, shared file) and B (CU-f-2).

## The issuer's acts after the drain

1. The real run (`hop3_timed_check.py` for `matthew_gooch`), timed; grade E1 (3) and E3 from it.
2. The portal candidate (the extended `wk-IRPT_CUSTDY-12-portal` line) back to `1.0.0_SA_CTO~DELL2`; DEV waits on Andrew.
