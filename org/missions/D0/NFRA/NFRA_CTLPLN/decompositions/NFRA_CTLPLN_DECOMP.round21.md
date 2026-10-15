# NFRA_CTLPLN decomposition -- round 21: the real case -- the last manager pairs, site Z's audit quote, the package journey's second step, the signed-change push, and one hygiene batch (issuer 2.0.0_SA_COO~C; cut 2026-10-15)

**Status: ISSUED in one issuance. FROZEN at the cut.**

**Input.** `ledger/ROUND_ANALYSIS.round20.md` (1.0.0_SA_CTO, @5df0b0af31) sections 1-3 and msg 109441; the CTO's package ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261015_151xZ_FWD15_PACKAGE_JOURNEY_DRIVEN_DELIBERATELY.md` @9735e81b15 (msg 109439); the CRO's research `org/tier1_exec/4.0.0_SA_CRO/deliverables/NFRA_CTLPLN_R21_FWD5_ONE_SIGNED_CHANGE_ONE_SCRIPT_RESEARCH_20261015.md` (msg 109442); the issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND20.md` @58a0c48950. **PRD:** v0.31. **Process facts in force:** the round-19 worker-face lines; each worker worktree is cut by `wk-provision.sh` (sparse) and removed at its merge by `worktree_gc.py --go --only` (a relative path); the CTO's rule: the analysis opens with the FWD coverage table, outcome cells first, hygiene one batch.

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-ak-1` | The records `intake_check.py` writes carry their device (`W112-S4`), before the journey's check step runs on a real package. | FWD-19, FWD-15 | LOCAL | `0.9.0_WK_NFRA_CTLPLN~116` |
| `CT-ak-2` | ONE hygiene batch: rebuild the stale comp-pulse danger map and make its test SKIP on a stale map (`S9127`); classify the four census values (`W114-S1`). | hygiene | LOCAL | `0.9.0_WK_NFRA_CTLPLN~117` |
| `CT-ak-3` | One signed change that names one script (`diag_sleeve_fix.py`) deploys exactly that script, in a real push from `box/laptop`, through the CloudOps seat, with its own NEVER-2 entry; step one is the `W113-S1` read of the hook's key map against the core's. Research owed and delivered (CRO). | FWD-5 | WORLD | `0.7.0_AE_CloudOps~U7` (spawned by the issuer, order named in its first message) |

## Driven by the issuer in this issuance (not cells)

- **FWD-3, the five manager pairs** (dell1 -> laptop, dell2 -> dell1, dell2 -> sitez, sitez -> dell1, sitez -> dell2): each sending box's manager opens a call to the receiving manager and the receiving manager acknowledges it; `0.0.0_AB_MSTR` asks each sending box's MSTR (a laptop seat cannot send from another box). The issuer reads `crossbox-matrix.py` afterwards. One message to MSTR.
- **FWD-21:** `0.0.0_AB_MSTR~Z` quotes site Z's spawn-audit lines 19401-19404 into a COMMITTED record, through a crossbox call; the issuer files one surprise row (owner `0.0.0_AB_MSTR`) that origin `box/sitez` has not advanced since 2026-10-09.
- **The package journey (FWD-15, 16, 18, 19):** ruled by the CTO (@9735e81b15) as duckdb, pinned, for one real read by a dell1 seat on a question it has open, chosen by `1.0.0_SA_CTO~DELL1`, no pipeline dependency added; two requests filed through `intake_request.py` (duckdb for that lane, and one naming no lane); the CTO approves the first and refuses the second and writes the approval file the fetch needs; the CVO reads it back. The issuer asked `1.0.0_SA_CTO~DELL1` by crossbox call to choose the lane and the question, and files the "no lane" request. The fetch, check, taildrop, install and the lane's run follow `CT-ak-1` and the CTO's approval file: cut in round 22, each waiting on the one before.
- **`W113-S1` disposition (issuer's):** the hook's bucket and key map for `black_diamond`, `inf`, `cot` (`code/<layer>/<name>`) equals the core's `CODE_TREES`; `mdpf` is gated in the core and absent from the hook's map, so the hook HOLDS it (safe). Recorded in the issuer's ruling row; `CT-ak-3` repeats the comparison as step one.

## Carried with an OWNER and the CONDITION that un-parks each

- **FWD-11:** a qualified wait on Andrew's word (call `laptop-20261014T205216Z-7841`); **FWD-9:** PARKED; **FWD-14, FWD-17:** Andrew's person acts (calls `c9a4`, `318f`); **FWD-27's person arms:** Andrew's; **FWD-24:** waits on `1.0.0_SA_CTO~Z`'s answer to `e670` (qualified wait on another box's lead); **FWD-2:** a real second box is a qualified wait.
- **`S9125`:** dell1, before 2026-12-31. **`S9119`:** read when a dell2 lane is live (owner `0.0.0_AB_MSTR~DELL2`). **`S9103`:** no cell. **`S9120`, `S9122`:** per the CVO. **`Z-S3`, `W12-S1`:** each function's next deploy. **`W89-S3`:** ADVI_FIRMBKTS's. **`R1`, `R2` of the CRO's gap table** (the pinned step admits top-level scripts only; the hook's bucket map is a hand copy): carried, a later hook cell.
- **The `r18_batch_*` folders under Temp:** a separate laptop act by the CTO.

## Rule 24

**Domain:** the CTO's round-20 section 3 enrichment list (5 items) against the open FWD chain; denominator printed in the CTO's section 1 table (28 FWDs: 2 REALIZED, 21 ADVANCED, 1 GATED, 1 PARKED, 3 MOVED). **Same grain; one intent; disjoint write surface:** `CT-ak-1` writes `intake_check.py` and its test; `CT-ak-2` writes the map, two test files; `CT-ak-3` writes one S3 key through the hook, the script, its ledger entry and a read test; no two cells write the same file except the append-only surprise channel. **State coherence:** `CT-ak-3` is the only cell with a real write (one S3 key, rolled back by VersionId on failure); `CT-ak-1` and `CT-ak-2` touch no gate and call no AWS.

## Dependency chains and fan-out

Three chains, no dependency between them. `fanout: 3 of 3 chains, cap 8, reason: two laptop worker cells and one CloudOps-seat WORLD cell; the journey's later steps wait on CT-ak-1 and the CTO's approval file, the manager pairs and the audit quote are crossbox acts`
