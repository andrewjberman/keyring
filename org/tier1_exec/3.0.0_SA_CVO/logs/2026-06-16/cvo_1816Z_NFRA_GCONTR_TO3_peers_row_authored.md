# CVO — NFRA_GCONTR TO-3: peers (SEV2) contract row authored + aum=smartx-produced census finding — 2026-06-16 ~18:16Z

**archetype:** SCRIBE
**secondary_archetypes:** TRACE, DIAGNOSE

## Context
Session start (3.0.0_SA_CVO). /watcher healthy (Monitor bdrzrqxzz armed, killed a prior-session orphan stream;
0 crons, LD-0175 compliant). Continuing NFRA_GCONTR TO-3 (author the SEV1+SEV2 graph_contracts rows + the
CVO-owned period_defs value-check). Ground-truth at session start: benchmark SEV1 row is LIVE+Andrew-ratified
(TO-2b closed, both axes verified); TO-2 table COMPLETE on Nessie main. Remaining: headline (SEV1), NNA (SEV1,
policy-limb held to 06-17), peers + aum (SEV2), + the value-check assertion.

## Work this pass
Authored the **peers (SEV2)** contract row — the cleanest remaining surface, fully grounded against the live
graph + served artifact. Surfaced a significant **de-risking census finding on aum** (it is SMARTX-produced,
not yang — a wrong row averted). Scoped the remaining rows with grounded findings in the YAML WAVE STATUS.

### peers-model-portfolios (SEV2) — authored, pending CTO+COO sign-off
- **canonical_writer:** `yang-pipeline-lambda-role` (producer `yang-generate-peer-performance` ASSUMES it;
  confirmed against the canonical graph). SAME canonical_writer as the benchmark seed (both yang-pipeline) ->
  Q2-resolvable now, no EC2 gap.
- **artifact:** `s3://opal-data-portal-v2/json/peers/peer_performance.json` (served, data_as_of 2026-05-31,
  intermittent — peer_excel-gated).
- **period_defs:** 1M (trailing-1-calendar-month, the BMKAUD-class invariant), QTD, 1Q, YTD, 1Y, Since Inception;
  per-period fields {percentiles:{p5..p95}, model, benchmark}; models UST/ST/INT/LTC/LTA (all share the period set).
- **forbidden_writers: [] (HONEST EMPTY)** — no known non-canonical peer writer (no smartx peer override, unlike
  benchmark's smartx-model-monthly-pull). Did NOT transfer the benchmark threat model — read peers' own. Catch
  rests on canonical_writer match + WATCH(advisory, bucket-grain) + the value-limb + bucket policy.
- **value_check:** model+benchmark legs vs canonical Yang returns (1M=trailing); CVO-owned (cross-surface
  consistency with the benchmark contract).
- **ratified_by: [CTO, COO]** (SEV2 tier §9), **ratified_at: PENDING-CTO-COO-SIGNOFF** (AE stamps the authoring
  Nessie commit on in-VPC write, after CTO+COO sign off). Not Andrew-gated.

### FINDING [census — aum] aum/account-distribution is SMARTX-produced, NOT yang — do NOT transfer the yang pattern
`account-distribution.json` `generated_at` = `2026-06-16T11:30:38Z` == the `smartx-account-distribution-daily`
cron (cron 30 11 = 11:30 UTC) -> produced by `opal-smartx-ingestion-pipeline` (ASSUMES `smartx-ingestion-lambda-role`),
`data/smartx/scripts/compute_account_distribution.py`. So the model_portfolios.aum surface's canonical_writer is a
**smartx** role, NOT yang-pipeline-lambda-role; semantics are point-in-time (period = as-of date, not trailing
windows). Open items for the aum pass: (1) confirm no smartx-exporter **EC2** dual-write of account-distribution
(the same EC2-Q2-invisibility class as NNA — benchmark already lists the EC2 `opal-generate-benchmark-returns` as a
dormant dual-writer); (2) locate the 2nd AUM-metrics/growth artifact (AUMGrowthMetrics.tsx / getAUMMetrics);
(3) curate forbidden_writers; (4) the point-in-time value contract. Authoring aum off the yang pattern would have
mis-declared canonical_writer -> a dead policy limb on a critical surface. (Lesson applied:
[[feedback_twin_class_doesnt_transfer_read_candidate_own_determinism_mechanism]].)

### Cross-lane seam flagged to AE/COO (TO-2 <-> TO-3)
The local authoring YAML still shows the **benchmark** row `ratified_at: PENDING-ANDREW-SIGNOFF`, but benchmark is
LIVE+ratified on Nessie. AE must `--load-contracts` **only the new peers row** — NOT re-process the whole file —
or the live benchmark `ratified_at` could be re-stamped/regressed. Surfaced, not silently assumed.

## Remaining TO-3 scope (each needs its own grounded pass)
- headline (SEV1) — Andrew sign-off; AUA-total surface (MDPF aggregate + account-distribution; $1.71B
  stale-headline incident history) -> careful value-contract analysis.
- advisor_intelligence/NNA (SEV1) — value-limb authorable; POLICY limb HELD to the 06-17 nightly derive
  (AE deployed the iam:GetInstanceProfile fix; re-verify pends the nightly — no ad-hoc gold run per cost discipline).
- aum (SEV2) — per the census finding above.
- period_defs value-check assertion (CVO-owned) — the runnable codified BMKAUD WS-2 check.

## Compiler Tools
| Tool | `<run>` | Observed | vs `<expect>` |
|---|---|---|---|
| comp-surface-check list | Phase-1 scope ceiling | 5 surfaces, 0 drift: SEV1{headline,benchmark,advisor_intelligence} SEV2{peers,aum} | **PASS** — exact match to TO-3 §9 ceiling |
| pipescript model-portfolios | producer-type census | model_portfolios.* = yang-pipeline (Lambda); peers=yang-generate-peer-performance | PASS — Lambda (Q2-resolvable), no EC2 gap for peers |
| comp-kuzu (canonical graph, HEAD current) | WRITES/ASSUMES census | yang generators ASSUMES yang-pipeline-lambda-role; opal-data-portal-v2 = bucket-grain (~58 Lambda co-tenants); smartx-account-distribution-daily TRIGGERS opal-smartx-ingestion-pipeline (ASSUMES smartx-ingestion-lambda-role) | PASS — confirmed peers canonical_writer + surfaced aum=smartx |
| schema-conformance (Phase-2, yaml validator) | each row vs §3 schema | 2 rows: both PASS — all 13 cols, period_defs MAP well-formed, ratified_by tier matches SEV, active=true | **PASS** — ALL ROWS CONFORM |
| aws s3 cp (served-artifact ground-truth) | peer_performance.json + account-distribution.json structure | peers periods/models confirmed; account-distribution generated_at=11:30Z (smartx cron match) | PASS — period_defs grounded in served data, not self-report |

Phase-3 (BMKAUD replay) for peers: deferred to the joint replay with AE's Q2 once the row is CTO+COO-ratified and
AE writes it in-VPC (peers is intermittent/peer_excel-gated; the policy-limb mirrors the already-proven benchmark
Q2 path — same canonical_writer, same bucket). Recorded as a TO-3 acceptance hook, not skipped.

## UPDATE (~18:30Z) — aum (SEV2) AUTHORED + the loader bug the peers row surfaced
### aum-model-portfolios (SEV2) — authored, pending CTO+COO (SEV2 ceiling now COMPLETE)
- **Live canonical writer DISAMBIGUATED via CloudWatch** (verify-the-mechanism, not the fitting timestamp): at
  2026-06-16T11:30:35Z `opal-smartx-ingestion-pipeline` (smartx-ingestion-lambda-role) logged "MDLP daily
  re-source job ... all MDPF-feed-sourced; dead-source pipeline skipped" + uploaded account-distribution.json +
  aum-metrics.json + aum-timeseries.json + per-firm mdpf/{49financial,inflection}/account-distribution.json.
- **smartx-exporter EC2 (i-06ebcb27395eb3f49) = DORMANT dual-writer** — ai-supervisor-v2.py writes the SAME keys
  but the EC2 is STOPPED since 2026-06-01 (the "dead-source" path) -> did NOT write today's files. canonical_writer
  = smartx-ingestion-lambda-role (Q2-VISIBLE -> aum authorable now, unlike NNA).
- **HONEST CAVEAT in the row:** the EC2 dual-writer is Q2-INVISIBLE (0 EC2 WRITES edges, NNA-class gap) -> its
  forbidden_writers tripwire is DECLARATIVE until the 06-17 EC2-WRITES-derive fix; today's containment =
  EC2-stopped + IAM + value-limb. source_of_truth = MDPF feed; period_defs point-in-time (as_of latest-complete-day,
  total_aum=FUNDED only, aum-timeseries append-only). Phase-2 re-run: 3/3 rows PASS.

### AE seam-CLOSE (fe645e103) — my peers row surfaced a real latent loader defect
- IDEMPOTENCY: benchmark row double-protected (already-present guard derive_runner.py:1030 fires before any
  ratified_at logic + never --overwrite benchmark) -> per-row scoped load structurally guaranteed; stale benchmark
  PENDING placeholder cannot regress live ratified_at=6f21c75ca.
- **DEFECT my peers row exposed (now fixed):** loader PENDING-detection was an EXACT-match tuple knowing only
  `PENDING-ANDREW-SIGNOFF`. peers is the FIRST `PENDING-CTO-COO-SIGNOFF` row -> it would have been (a) SAFETY-GATE-
  BLIND (could land BEFORE CTO+COO sign-off — the exact failure the gate prevents) and (b) ratified_at mis-stamped
  with the literal placeholder. AE fixed both via prefix-aware `_is_pending_ratified()`, proven 10/10, gate PASS.
  CVO value-add: authoring with the correct SEV2-tier placeholder exposed a gate that only knew the SEV1 one.
- GO-TIME (CTO+COO sign): upload signed 3-row YAML to s3://...globgrph/contracts/, AE dry-runs (benchmark SKIP,
  peers/aum gate), --stamp-ratified per-row (no --overwrite), WRITE_VERIFY, then I byte-verify value-limbs. ACKed.

## RAVC
- RAVC2 -> COO (CC CTO): peers + aum SEV2 rows authored (SEV2 v1 ceiling COMPLETE), request CTO+COO sign-off.
- RAVC close <- AE: seam flag answered + loader defect fixed (fe645e103). ACKed; will byte-verify value-limbs at load.

## Net session outcome
peers + aum SEV2 rows authored + 3/3 schema-conformant (SEV2 v1 ceiling COMPLETE); benchmark SEV1 live+ratified.
Two de-risking census findings (aum=smartx-Lambda-canonical NOT yang; EC2 dormant dual-writer) + one real infra
fix surfaced (loader PENDING-gate was SEV1-only). Remaining TO-3: headline (SEV1/Andrew), NNA (policy-limb 06-17),
the period_defs value-check assertion. Grounded vs live graph + served artifacts + CloudWatch throughout.

— 3.0.0_SA_CVO
