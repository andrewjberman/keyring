# NFRA_CTLPLN decomposition -- round 20: the real case, step by step -- the fetch record's device key, the deploy gate's pinned-entry fix, the register-copy pointer, and one hygiene batch (issuer 2.0.0_SA_COO~C; cut 2026-10-15)

**Status: ISSUED in one issuance. FROZEN at the cut.**

**Input.** `ledger/ROUND_ANALYSIS.round19.md` (1.0.0_SA_CTO, @2009d89478) sections 1-3 and msg 109424; the issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND19.md` and `ROUND19_INPUTS_FOR_ROUND_ANALYSIS.md` (@d359d2bd70); the CVO's re-grade `3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_FWD_REGRADE_20261015.md`. **PRD:** v0.31. **Process facts in force:** the round-19 worker-face lines; each worker worktree is cut by `wk-provision.sh` (sparse) and removed at its merge by `worktree_gc.py --go --only` (a relative path); the CTO's rule: the analysis opens with the FWD coverage table and the enrichment list cuts outcome-serving cells first, hygiene at most one batch.

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-aj-1` | Step 1 of the package journey: every fetch record names its device (`W111-S1`); the downloads reader counts per device and counts old records as unattributed; the laptop-side refusal that names the route is recorded. | FWD-19, FWD-18 | LOCAL | `~112` |
| `CT-aj-2` | `D1-S8`: the pre-push deploy gate also deploys a file named by an OPEN pinned change whose bucket bytes differ, whatever the box diff; planted case, three negative arms, local-folder bucket, stubbed `aws`. `safe_deploy_core.py` is not edited (one writer, IRPT_BCKEND). | FWD-5 | LOCAL | `~113` |
| `CT-aj-3` | The two unreached box-listing tests take a register copy, so the fixture-box read becomes 8 of 8. | FWD-2 | LOCAL | `~114` |
| `CT-aj-4` | ONE hygiene batch: `test_named_commit_deploy.py` runs to its last line (`W108-S2`); the risk reflex's map classes portal `.tsx` (`W110-S1`). | hygiene | LOCAL | `~115` |

## Dependencies the cut respects (cells NOT cut this round, with the condition that cuts them)

- **The package journey, steps 2-7 (FWD-15, 16, 18, 19):** the chain is `1.0.0_SA_CTO~DELL1` names a real package a Dell lane needs -> the request is filed -> `1.0.0_SA_CTO` approves it and refuses a second out-of-policy request -> fetch (device key, `CT-aj-1`) -> check -> taildrop -> install -> the lane's own run -> the CVO reads it all back. Step 1 is `CT-aj-1`. Steps 2-7 each wait on the earlier one and on the Dell CTO's named package; the issuer asked `1.0.0_SA_CTO~DELL1` to name it by crossbox call this tick. FWD-18's site Z arm (`kit_pip_no_egress.py wrap -- download six`) is asked of `0.0.0_AB_MSTR~Z` by crossbox call. Cut as soon as the name is in.
- **FWD-5's positive arm (a signed change deploys exactly its script, in a real push):** a WORLD act through `0.7.0_AE_CloudOps~U7`, opening and closing its own NEVER-2 ledger entry; waits on `CT-aj-2` merged (the gate fix lands first). Cut in round 21 under the evidence law (research owed, WORLD).
- **FWD-21:** the exercise is site Z's own respawns of 23:32Z; the issuer asked `0.0.0_AB_MSTR~Z` by crossbox call to report any ask in site Z's broker before those respawns, with its spawn audit and one day record. Read, not built.
- **FWD-3:** the open pair is laptop -> sitez (`XB-20261015T121713Z-e670`, unacknowledged at 14:2xZ, over 2 h). The issuer reads `crossbox-matrix.py` at the drain; if it reads 12 of 12 that read is the cell. **FWD-24:** waits on the same call's answer from `1.0.0_SA_CTO~Z`; then the two answers are compared on the record (qualified wait on another box's lead).
- **FWD-2:** a real second exercise needs a real new box; none is in sight (qualified wait). `CT-aj-3` makes the fixture read 8 of 8.
- **FWD-11, FWD-9, FWD-14, FWD-17, FWD-27's person arms:** Andrew's (calls `7841`, `c9a4`, `318f`), PARKED, and as before.

## Carried with an OWNER and the CONDITION that un-parks each

- **`S9125`:** dell1, before 2026-12-31. **`S9119`:** read when a dell2 lane is live (owner `0.0.0_AB_MSTR~DELL2`). **`S9103`:** no cell. **`S9120`, `S9122`:** per the CVO. **`Z-S3`, `W12-S1`:** each function's next deploy. **`W89-S3`:** ADVI_FIRMBKTS's. **`D1-S8`:** `CT-aj-2`. **`W111-S1`:** `CT-aj-1`. **`W106-S5`:** ruled (one writer IRPT_BCKEND), the CVO re-reads the placement.
- **The four old `r18_batch_*` folders under Temp:** a recursive delete, Andrew's word; added to the laptop clean-up call `715c`.

## Rule 24

**Domain:** the CTO's round-19 section 3 enrichment list (6 items) against the open FWD chain; denominator printed in the CTO's section 1 table (28 FWDs: 2 REALIZED, 21 ADVANCED, 1 GATED, 1 PARKED, 3 MOVED). **Same grain; one intent; disjoint write surface:** each cell writes its own new test file and the listed existing files; no two cells write the same file except the append-only surprise channel and `.tools/tests/test_round19_intake_requests.py` (`CT-aj-1` only) and `.tools/tests/test_round19_register.py` (`CT-aj-3` only). **State coherence:** no cell deploys, pushes or calls AWS; `CT-aj-2` edits a gate in a temporary-repository test and the real push is a later cell.

## Dependency chains and fan-out

Four chains, no dependency between them. `fanout: 4 of 4 chains, cap 8, reason: four independent laptop worker cells; the journey and FWD-5 positive arm wait on earlier steps named above`
