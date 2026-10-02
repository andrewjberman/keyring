# Deploy Completion Record
**Date opened:** 2026-10-02T05:40:50.599813+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS Cottonwood re-point: Cottonwood gold classifies from the canonical table by the ruled rule; halves COO @40cc2e2108 (blob 59c1da5458) + CTO CTO_HALF_SECCLASS_COT_REPOINT_20261002.md (batch 113, CONDITIONAL: G, R, S wait until leg P's readers are on every deployed portal build, PROD included -- a PROD promote is Andrew's act). Opened LATE, after leg P's DEV push (05:4xZ); no other leg had run
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 168.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | git | portal readers on DEV: coo-m-cot-mix-readers rebased onto origin/DEV and pushed HEAD:DEV | push range + ls-remote + CI conclusion |  | OPEN |
| PROD | verify | the same reader commit on portal PROD (Andrew's promote) -- the CTO condition for G, R, S | ls-remote PROD contains the commit |  | OPEN |
| M | git | merge coo-m-cot-carrier @affbc33e2b into CLOUD, just before G (deferred: on CLOUD unheld, C_06/D_03/D_04 would ship without the held library); merged tree = the ten files, B_00 922249798b | merge hash + tree diff |  | OPEN |
| I | activation | plan + safe-apply of cot-pipeline adding exactly CanonicalClassificationsRead, role statements printed before and after; run just before G | plan diff + live statements |  | OPEN |
| A | s3-prefix | safe-deploy of Cottonwood shipped artifacts to lib/_shared/; just before G | TOOL-03 MATCH lines |  | OPEN |
| G | s3-prefix | safe-deploy of B_00, C_06, D_03, D_04, lib/etf_classifier.py, lib/mix_views.py with the serve-hold removed | TOOL-03 MATCH lines |  | OPEN |
| R | verify | ad-hoc Cottonwood gold run (QA), outputs read per acceptance 1 | served keys read |  | OPEN |
| S | verify | scheduled Cottonwood gold run + walked pages per acceptance 2 | served keys + page walk |  | OPEN |

## Log

- 20261002T054050Z OPENED by 2.0.0_SA_COO~M with 8 leg(s)
