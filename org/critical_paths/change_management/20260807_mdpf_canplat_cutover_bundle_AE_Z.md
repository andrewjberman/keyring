# DEPLOY-COMPLETION LEDGER — MDPF_CANPLAT cutover bundle (AE~Z)

**Opened:** 2026-08-07 ~03:25Z by `0.7.0_AE_CloudOps~Z` · **Status: OPEN — IN FLIGHT**
**Authority:** Andrew-direct completion bar (record @my deliverables 20260807) → COO~Z [DRIVE] GO 032046Z
(all four legs, in order, now; never-widen embodied: COO + CTO~Z hold the same Andrew broadcast, the
authorizing word is Andrew's own).
**Rule:** a begun deploy FINISHES in-session (every leg) or rolls back + escalates loud. Nothing
half-landed. This entry closes ONLY when every leg below reads LANDED or ROLLED-BACK.

| # | Leg | Status | Evidence |
|---|---|---|---|
| 1 | A8-a redeploy — pin moved @d3be2998e→@25b0bb038 (COO-ratified 032336Z), 21-entry package incl. G2 pair | **LANDED** | artifact bda8e124…, VersionId NHeXz38E…, CodeSha256 ties, 0-diff |
| 2 | RE-POINT atomic: floor target swap → mdpf-gold-lambda, old target removed same apply | **LANDED** | live get-schedule: cron(0 9 * * ? *)/America/New_York/ENABLED/target=mdpf-gold-lambda; 1add/2chg/1destroy; 0-diff |
| 3 | P3-1 publisher build + deploy @c0902245b (D5/D7/D8, roster build-copy, 6/6 fixtures) | **LANDED** | artifact f613200a…, VersionId 9nqnBHz6…, CodeSha256 9hMgCsmU… ties; env pins verified live |
| 2b | Union redeploy @470788096 (Andrew carry-forward ruling; COO-ratified 033922Z) | **LANDED** | artifact debd41b9…, CodeSha256 3r1BuRfc… ties, 0-diff; is_floor payload check discharged (11/12 build on exact floor payload) |
| 4 | CUTOVER FIRST EMISSION | **OPEN — fire 1 FAILED CLOSED** @03:45:51Z on DS's L-1 key-set gate (cottonwood-only `_leg_source_key` from the carry impl). Served plane untouched (proven by listing); one pre-gate staging write (gold/mdpf_revamp/global/non_model_assets.json) superseded by next good run. AWAITING DS re-pin → rebuild/redeploy row → re-fire | DS notified 034716Z w/ verbatim log |
| 5 | Verification battery + reports | PENDING leg 4 | is_floor: discharged (CTO 034428Z, COO downgrade 034500Z) |

**Rollback shapes, pre-stated:** Leg 1 → redeploy prior artifact (VersionId IILTZ… @387da6e1a pin).
Leg 2 → terraform apply of the pre-change commit (old floor target restored, scheduler removed).
Leg 3 → publisher keeps old deployed generation (no schedule change involved).
Leg 4 → A8 conditional writes make a bad emission a recorded conflict, never a clobber; platinum
projection rolls back by re-projecting prior gold (S3 versioning on).
