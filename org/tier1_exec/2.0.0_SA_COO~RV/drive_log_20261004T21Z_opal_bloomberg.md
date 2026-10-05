# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-04 21Z-23Z (ETFS_RIVALS, FULL)

Row: project | limb | round | TOs | cells | thread | act.

## 21Z
| ETFS_RIVALS | L6 round 8 A | 8 | 0/5 | 5/5 cut | y | DRIVE FORWARD: Andrew-direct "yes, build round 8 tonight" recorded @0a4321b843 (CTO~Z told); signed-in smoke recorded @1c31a5f6ce (8 items); CTO~Z PRD v0.14 @4cc8e40575, CVO~Z re-sign, ADMITTED 21:15:49Z; lg-1 checks written (base FAIL 3/2); decomposition @cbe384e40c; issuance A @5f6b2a22d7 (fanout 4 of 4); 4 workers spawned; read-only investigations: grounding fail = uncited T7/T9, YTD clipped to first report, history depth census (WORKSTREAM_B_INPUTS @7cc969288b) |
## 22Z
| ETFS_RIVALS | L7 round 8 A | 8 | 5/5 built | 5/5 | y | DRIVE FORWARD: dt-1, an-1, rp-1, lg-1, rw-1 built; issuer re-ran every check in the worker worktrees (PASS); slot ~2 re-seated (no transcript to resume); row Z-W2-S13 ruled (g82 test amended ce381fd792; suite 602/0) |
## 23Z
| ETFS_RIVALS | L6/L7 round 8 B | 8 | A 5/5 + B 4/4 built | 9/9 | y | PARALLELIZE then DRIVE FORWARD: B checks written (6, base FAIL, controls OK); issuance B @c222ecc8fa (fanout 4 of 4, workstream tag); gc-1, hc-1, bt-1, rn-1 built; row Z-W7-S1 ruled (the bt-1 check's QTD was wrong, fixed ea8dbeba5e / 4b33f05d4b); integration dry-run of all 7 branches: suite 638/0, 15/15 checks PASS; drain set for 07:41 ET 10-05 |

## Compiler Tools
- comp-schedule --drift: WITHIN BUDGET, 6 of 6 carriers, 1 gate armed (not this project).
- comp-surprise --project ETFS_RIVALS --json: 149 items, 4 open, 2 armed (before the round).
- comp-find piped to a receiver was refused by the rail twice; re-ran with native Grep or without the pipe.
- to-pipeline-gate: refused the B issuance once (ONE ISSUER PER ROUND keyed to the round); passed with `<workstream>B</workstream>`.
