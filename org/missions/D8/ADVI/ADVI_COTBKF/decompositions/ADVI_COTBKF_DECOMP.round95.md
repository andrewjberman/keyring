# ADVI_COTBKF decomposition -- ROUND 95 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-16) -- provision the served-returns run data on dell1 and price the served move

**Status: DRAFT -> ISSUED in one issuance.**

**Numbering.** Round 95 was once the second CRM window; the CTO ruled that window not needed (msg 6389), so the number is free and this round takes it.

**Cut on:** the CTO's word on the served move (msg 6455, 2026-10-16 ~03:18Z): "Provision the builder's run data on dell1 from S3, read-only. Price the move per account: under 3adb (a) every value's DELTA should be 0, with only the label added, so any value that moves is a finding and a stop. Apply under never-widen halves from you and me. Bring your COO half when it is priced." Andrew's call `3adb` (a): served Yahoo-priced days for securities held in V2 stay, labelled interim-Yahoo.

**What the read of the record adds (not in the CTO's word).** Round 89's `CB-ck-2` stopped at `NO_DATA_DIR`: the run data (`.scratch/advi_cotbkf/`, gitignored) lives on dell2 and is absent here. The three served tables were last minted from the round-82 build (`fwd3_serve_r34`, run_commit `728d223ddca5472884c464b0482f814bfc706f41`). Round 83's `porting_verdict` column was built locally and never applied (`NEVER_WIDEN_R83_PORTING_VERDICT_COO_HALF.md` is a DRAFT, unsigned). So the builder as it stands now adds TWO columns to each served table, `use_class` and `porting_verdict`, and the pair that follows must cover both; `CB-cq-1` counts both.

**Rule 24.** Domain: the served move of the three FWD-3 tables under call `3adb` (a). Subtraction: provisioning the run data and the pre-act price of the move -> `CB-cq-1`; the signed pair and the served write -> round 96 (the COO half is this seat's act, the apply is CloudOps' under the pair, and neither is a task order of this round). Uncovered here: the apply, by design.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-cq-1` | on dell1, rebuild the default re-grade run's data and the three tables locally from S3 (read-only) at the pins the round-82 build recorded; read the three SERVED tables; prove every pre-existing column equals the served one row for row; count what the two added columns would say; stop and record if the control fails | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~185` |

**Fan-out (to state at the cut):** `1 of 1 chains, cap 8`.
