# 0.8.0_AE_CloudComp -- decommission research: 3 threads delivered (design + live-validated prototype) (2129-2226Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** EXPLORE (design + live grounding), VALIDATE (prototypes vs live AWS)

Continuation of the reserved-session decommission-research lane (base session; builds went to 0.8.0~D per the
staffing split logged @0f054e332). Delivered all three Andrew-direct research threads, each a grounded design
PLUS a prototype validated against live AWS. They compose into one superseded-twin detector.

## Window: 2129Z -> 2226Z (since prior log @0f054e332)

## What was done

### Thread 1 -- comp-debris extension past Lambda (PROTOTYPE) @f921f9e97
- `comp_debris_ext.py` (my lane): per-type activity adapters (DDB / S3 / EC2 / EventBridge) that IMPORT
  `comp_debris` and reuse `classify/BANDS/_HELD_RX` VERBATIM -- proving "one classify(), N adapters."
  GetMetricData batched; per-row `signal_basis`; UNKNOWN-band; hold-aware.
- Validated LIVE: self-test 7/7; `ddb,s3` = 75 resources (HOT44/COLD10/STILLBORN16/UNKNOWN5); `ec2,events`
  = 179 (HOT135/COLD11/UNKNOWN27/6 held). S3 write-cold works FREE (storage-delta; opal-data-smartx-v2 28d).
- **Discovered refinement:** scheduled rules need CADENCE-AWARE windowing (fred-ingestion-monthly-late cold
  at 23d is a MONTHLY rule = healthy; bd-49f-fees-runner-daily 21d = real). Folded into the design (control
  #6) + `VALIDATION_FINDINGS.md`. Andrew ruling folded: accept S3 read-blindness (design open-Q2 resolved).

### Thread 2 -- comp-iam-usage (design + PROTOTYPE) @bf4c846d5
- `COMP_IAM_USAGE_DESIGN_20260717.md` + `comp_iam_usage.py`: the access-plane coldness comp-iam lacks
  (comp-iam = deploy-time DESIRED + one simulate). `role-cold` = RoleLastUsed reusing `cd.classify` on the
  IDENTITY plane; `who-can-reach <arn>` = APPLIED resource-policy read (Rule-22a limit-2 fix).
- Grounded live: iam_cli.py has NO usage mode; 209 roles; RoleLastUsed populated; Access Analyzer ABSENT
  (recommend enabling); bucket policies readable.
- Validated LIVE: self-test 6/6; role-cold(60,90d) surfaced real stale grants -- AWSServiceRoleForAmazonOpenSearch
  228d, bd-gold-* 150-165d (OPAL_CONSOLIDATION IAM residue); service-linked/break-glass roles correctly
  STILLBORN not reap. who-can-reach opal-data-inf returned the CloudFront-OAI grant set.

### Thread 3 -- resource_heat_snap (design) @503b5e2a3
- `COMP_RESOURCE_HEAT_SNAP_DESIGN_20260717.md`: COMPOSITION, not new machinery -- a new SURFACE in the
  EXISTING `snap_store.py` (my TO-7 module), produced by thread-1's `comp_debris_ext`, yielding the
  day-over-day delta ("went cold when its twin went hot") = the heat-divergence axis comp-similar `supersede`
  consumes (CTO ruling 5). Validated: the resource_heat_snap surface coerces a real comp_debris_ext row
  through `snap_store.coerce_rows` (clean OK; missing-arn fails-closed; UNKNOWN-band null-optionals clean).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `commit-gate.sh` | comp_debris_ext.py, comp_iam_usage.py (x2 -- ruff F401/E702 fixed) | PASS | py_compile + ds-precommit + ruff py39 |
| `safe-commit.sh` | f921f9e97, bf4c846d5, 503b5e2a3 | PASS | my-lane deliverables (no owned-paths block) |
| raw `aws` (rail-checked) | cloudtrail/s3/ec2/ddb/events/iam GetMetricData, list-roles, get-role, get-bucket-policy, list-analyzers | PASS | LIVE validation of all three prototypes; read-only inspection |

**What worked:** reusing `comp_debris.classify()` across the resource-plane AND the identity-plane -- the same
coldness engine, two planes, proven by import. `snap_store`'s SURFACES registry made thread 3 a one-entry add.
**What failed:** heartbeat WinError-5 (transient liveness.json rename contention under multi-agent load) --
cosmetic, registration recent; not retried in a loop. **Gap:** none new.

## Files Modified (see commit messages: f921f9e97, bf4c846d5, 503b5e2a3)
- `deliverables/comp_debris_ext_prototype/` (comp_debris_ext.py + VALIDATION_FINDINGS.md) + design update @f921f9e97
- `deliverables/comp_iam_usage_prototype/comp_iam_usage.py` + `COMP_IAM_USAGE_DESIGN_20260717.md` @bf4c846d5
- `deliverables/COMP_RESOURCE_HEAT_SNAP_DESIGN_20260717.md` @503b5e2a3

## Deployment / Verification (AE)
NO infra deploy. Research + committed deliverables only. All AWS calls read-only inspection, rail-checked.

## Blockers
NONE. Building the prototypes into the production tools lands at `org/modules/graph/` (ANY_EXEC) -> build
lane/CTO -- EXPECTED lane routing, not a blocker.

## Current State (zero-context handoff)
- **All 3 decommission-research threads DELIVERED** (design + live-validated prototype each), in
  `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/`. They + comp-similar compose into ONE superseded-twin
  detector (thread1 signal -> thread3 delta -> comp-similar join -> thread2 access corroboration).
- comp-debris + comp-iam packages are being HANDED to CTO for landing (this session, next action).
- comp-similar PH1 corpus remains ~D's (working-tree file + record @30591c1d5; CTO landing open).
- Base session reserved; heartbeat contention is transient (liveness.json), registration recent.

## Next Steps
1. **[me, now]** Hand comp-debris + comp-iam packages to CTO for landing at the ANY_EXEC engine home.
2. **[1.0.0_SA_CTO]** land the two packages (+ the comp-similar corpus, option-a); the prototypes are
   build-ready (self-tests green, live-validated) -- integrate into comp_debris.py + a comp-iam-usage sibling.
3. **[me, on Andrew word]** next research increment, or fold CTO's landing feedback.
