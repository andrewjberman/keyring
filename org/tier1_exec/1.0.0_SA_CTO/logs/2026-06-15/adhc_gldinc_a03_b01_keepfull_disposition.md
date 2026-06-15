# ADHC_GLDINC design disposition — A_03 / B_01 KEEP-FULL (formal record)
**archetype:** SCRIBE

## Authority
ws CTO ADHC_GLDINC design authority (per-script incrementalization classification). Records an Andrew-direct ruling relayed via COO SYNC 145622Z (06-15) + AE bd-runner cutover assessment. Closes the "CTO formal disposition pending" reference held open in COO 145622Z and AE 152315Z.

## Disposition
**A_03 `positions_cube` + B_01 `holdings_lots`: KEEP-FULL.** Classified FULL-RECOMPUTE-INHERENT, treated exactly like A_04 (the precedent keep-full, 9a89926fd, DELTA=0). The windowed-FIFO refactor that would be required to make them incremental is **explicitly NOT commissioned.**

## Rationale (Andrew-direct D3, 06-15)
Three independent reasons, any one sufficient; together decisive:
1. **The skip-claim gate structurally cannot pass.** The whole-run skip fingerprint hashes the daily-changing silver/prices inputs, so the hash never matches the prior night -> the run never skips -> the skip counter is stuck at 0. An incremental gate that can never fire is not incremental.
2. **~$0 incremental savings.** Even with a working gate, their incremental yields essentially no compute reduction (the FIFO cube/lots must reprice the full position set against daily-changing prices regardless).
3. **They are the two largest scripts.** Highest blast radius, highest correctness risk, for the least payoff.

Net: cutover buys nothing and can't gate. Keep-full is correct; commissioning a windowed-FIFO project would be cost with no return + never-widen risk on FIFO-derived served numbers.

## Boundary (what this does NOT do)
- Does not touch A_04 (already keep-full), A_02 (cutover deployed 853974894, DELTA=0), or the ripening A_01/B_03/B_02 cutovers (Andrew pre-auth, 5-night gate ~06-16/17).
- Windowed-FIFO remains an UN-commissioned future option, not a backlog commitment — re-opened only if Andrew directs and the gate-feasibility + savings premises change.

## Cross-refs
- A_04 keep-full precedent + the never-widen "DELTA=0 deploy needs no hold" doctrine: [[feedback_never_widen_gates_served_movement_not_deploys_delta_zero_no_hold]].
- Cache-vs-fresh divergence doctrine (fix cache to match oracle, don't redesign dedup): [[reference_cache_vs_fresh_divergence_fix_cache_to_match_oracle_not_redesign_dedup]].
- c6i.16xlarge bd-gold-qa-runner is PURPOSE-KEPT (not reclaimable) — separately recorded in NFRA_COSTAWS governance; excluded from the week's cost review (item 2) + DEBTSCAN (item 4).
