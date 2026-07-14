# 0.5.0_AE_OpalETL — session close 2026-07-14 0940–0958Z (window since session_0845-0940Z)

**archetype:** MIXED (VALIDATE + IMPLEMENT + COORDINATE)

## Window summary

1. **V2-8 gate chain CLOSED for the allocation_account_map family.** CTO code review (094300Z)
   demanded two changes, both the silent-failure class: multi-record feed-9 payloads now RAISE
   (`MapShapeError`, count named — never silent truncation to `data[0]`); the dedup now
   DISCRIMINATES (identical dups collapse; CONFLICTING dups on the natural key RAISE with
   offenders named — the invariant is detected, never keep-last-adjudicated); plus a loud
   null-key census. +4 tests, all pass. Landed @ `41e44aaa0`; re-review PASSED;
   **first-conversion signoff GRANTED** (094726Z) — conversion runs after 22:00Z through the
   phase discipline as the rules stand at run time.
2. **HAR-4 probe order executed (CTO 095252Z, Andrew's challenge to the 55.2% ceiling).**
   Results (~09:54Z, bundle credential, read-only): **5/5 by-UUID `accounts/{uuid}` GETs SERVED
   with brokerageAccountNumber (8-digit) at view perm** — the number-enrichment ceiling for the
   1,315 sweep-identified closed rows collapses to a bounded **91-call** pull (supersedes the
   option-(b) ruling as the measured winner). Precision held against over-claim: the
   **1,066 no-UUID class does NOT collapse** (no held surface yields their account UUIDs).
   Finding-inside-the-finding: the 5 probed "unresolved" accounts read `status='active'` — the
   4.1 roster walk was probably default-status-filtered; the sweep universe may widen.
   `nonzerosleeve`: 511 rows/511 accounts/511 with brokerageAcctNum, 47 outside the living map —
   second identity carrier + the money-leg surface. `models/summary` SERVES 5.2MB under the
   bundle (platform id is yaliu's — content check needed before the models_summary open closes).
3. **Andrew value-date addendum banked** (via CTO 095519Z): identity leg primary; money leg
   (account_number, as_of, amount vs fact_rps) as the join's SEMANTIC proof (agreement rate with
   denominators into D2 findings); last-resort recovery only with per-row confidence stated.

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| commit-gate + surface-check + risk-reflex | via safe-commit ×2 | PASS/clean |
| `python test_silver.py` | 13 cases post-review-changes | ALL PASS |
| raw `aws` (operational) | 3 HAR-4 probes under the bundle (by-UUID ×5, nonzerosleeve, models/summary) | measurements on the record; read-only, no landings |

No comp-* search tools: the window was review-response code + credentialed API probes (Rule-20
operational verification); no estate search question arose.

## Current State — THE HANDOFF (zero-prior-context)

**Serial 0.5.0_AE_OpalETL · branch CLOUD (all pushed through `41e44aaa0`; log commits after) ·
registered LIVE · Monitor task `bsar6k5zm` (inbox) + background watcher `b4g5x5ufh` (22:00Z).**

### The one thing that outranks everything tonight
**22:00Z ONE RUN, THREE VERDICTS** (ETF lane): parity day-2 + FIRST monolith bronze (C4 AC1,
LISTING-based) + ligament rows, **plus CTO's content assertion — open the landed bronze and SEE
content, never infer from the producer's raise-on-empty.** Gate: `python
.tools/etfs-parity-check.py` on the scheduled artifact, **UNPIPED** (rc-through-a-pipe is the
banked self-inflicted class). A day-2 refusal is the gate WORKING. Report to 2.0.0_SA_COO —
**V2-1's GO rides that report** (TO `OPAL_ASSETS.V2-1.etf-channel-level-up.md`, STAGED; producer
untouched until the proof). Preconditions PRE-VERIFIED on the deployed producer
(`etfs-netassets-daily` env read live 09:37Z: `BRONZE_BUCKET=opal-data-assets`,
`BRONZE_GRAMMAR=monolith`, `SILVER_ROOT=_cloudprobe/`, `ETFS_BUCKET=opal-data-etfs` — the C4
two-locals flip is APPLIED; bronze moves, silver stays, parity quarantined). A deadline-aware
watcher polls the (currently EMPTY) `opal-data-assets/etfs/` prefix — fires on first landing or
prints DEADLINE-MISS at 22:50Z; a fresh session must RE-ARM it (background tasks die with the
session): poll ListObjectsV2 on that prefix, success=keys exist, deadline=22:50Z.
⛔ LAPTOP STAYS ON.

### SmartX / C5 / D2 — where everything is
- **Pipeline `smartx-pipeline-v1.5.0`, all deployed + 0-diff:** `smartx-assets-daily-pull`
  (09:30 ET scheduler, fail-loud DirtyRunError; feeds 1–7 under opal7 SPLIT creds + feed 9 under
  the yaliu BUNDLE — env `FEED9_BUNDLE_SECRET=smartx/credentials/yaliu-bundle`, explicit-per-call
  mint, NEVER the `SMARTX_CRED_BUNDLE_SECRET` env-precedence path). Role
  `smartx-assets-pull-role` is fenced (22a complete all three layers) + bundle-secret-granted
  (pre/post/negative simulates on the record).
- **Bronze landed (run 2026-07-14):** atom 9,525/9,525 · model tier 11/11×5 feeds (feed-5
  re-landed 9,525 rows; model_aum first landing 4,270 rows) · feed-9 resolver 7/7 visible models
  (7,141 identity rows) · closed-identity sweep 6,620/6,620 accounts (23,213 rows).
- **KNOWN-DIRTY, honest:** `models_summary` = persistent vendor 500 at opal7's platform id →
  the daily lambda WILL error daily naming it (true alarm). It SERVES 5.2MB under the bundle —
  content check pending before that open closes.
- **D2 findings @ `826a44082` (CTO-accepted):** living identity 99.96% (7,141/7,144); closed
  55.2% (1,315/2,381) — number-enrichment now a 91-call by-UUID pull (probe-proven, awaiting
  CTO's ruling since it supersedes option-b); the 1,066 no-UUID class stands, routed to Andrew.
- **V2-8 converter:** code-ready + review-PASSED + first-conversion SIGNED (`silver.py` /
  `test_silver.py` @ `41e44aaa0`). Conversion slots AFTER 22:00Z; conditions: _probe/-vs-real-key
  phase rules at run time, ListObjectsV2 acceptance, denominated row counts + (b)-join miss
  count. **CHECK THE NAMING LAW at conversion time:** memory now records silver=`fact_{type}` /
  gold=`dim_*` — the map table's silver name may need the `fact_` form; confirm against the V2-8
  TO before first write.
- **Pending CTO ruling (probe report 095719Z):** 91-call enrichment pull + nonzerosleeve bronze
  landing + models/summary content check. Andrew's value-date money-leg (agreement-rate
  corroboration vs fact_rps) rides the same D2 findings update.
- **Fresh-CRS join re-measure:** when 0.6.2's fact_acc lands (monolith bronze ACC exists through
  07-13; legacy silver/ACC is measured-lossy and 2 months stale — wrong substrate).

### Standing context a fresh session must not re-learn
- **Three Andrew-directs recorded today** @ `d8aa44b6e` (client-identity table from the HAR),
  `9d42d2d77`+`c7cad5762` (NO vendor rate limit — "we're not rate limited so stop saying we
  are"; pacing disabled, MAX_WORKERS is the lever), `b9b11f7fd` (yaliu bundle = option (a);
  opal7 unchanged for feeds 1–7).
- Bundle JWTs are IN-MEMORY ONLY (never park to `smartx/jwt/current` — the opal7/legacy slot);
  the separation test is permanent in `test_auth_bundle.py`.
- The parked-JWT secret is malformed for our reader (re-mint every invocation, works by design;
  flagged to the jwt-refresher lane — open, low).
- All session logs: `org/tier2_senior/0.5.0_AE_OpalETL/logs/2026-07-14/` (0653, 0740, 0845, this).

## Next Steps
1. **[self] 22:00Z verdicts + report to [2.0.0_SA_COO]** — then V2-1 GO decision is COO's.
2. **[self, on CTO ruling] 91-call by-UUID enrichment + nonzerosleeve landing + models/summary
   content check** — bounded, bundle-credentialed, registries already outside the opal7 path.
3. **[self, after 22:00Z] first V2-8 conversion** (naming-law check first) with the denominated
   conversion report.
4. **[1.0.0_SA_CTO] holds:** the enrichment ruling; the 1,066-class → Andrew; D1/D3/D4 for the
   convergence session.
