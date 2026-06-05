# 0.4.0_DS_ClientPlatform — work_1800Z (MDLP I1+I2 per-firm built+validated; I1+I2 authoring COMPLETE)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

## MDLP_DISTFIX I1+I2 re-source — per-firm twin done; reconcile-consistency PROVEN

Per-firm producer (compute_per_firm_account_distribution.py) re-pointed onto the MDPF feed
(Option-A: BOTH builders). Unified the two divergent builders (49F=dead smartx_allocations;
INF=eclipse-gold) into one `_build_firm_distribution(firm_id)` reading
`model_aua_positions/{firm}/{latest}`: cohort_class=='model', per-account groupby sum model_value,
dropped obsolete Period/AllocationStatus/eclipse-date logic, >=$1K floor via the shared helper,
by_model = firm-NATIVE S4 taxonomy (49F 5 base; INF 5 base + 2 blends "50/50 INT/LTC","50/50 ST/INT").

### Validation (gate-clean + dry-run vs live feed)
- 49F: 6,852 funded / $1,376,858,220 ; INF: 449 funded / $115,124,705. Self-check PASS both
  (by_model sums to total). Native taxonomy preserved.
- **RECONCILE PROOF (Option-A goal):** 49F+INF = 7,301 / $1,491,982,925 == the GLOBAL producer's
  7,301 / $1,491,982,925 to the CENT. Global = sum-of-per-firm by construction (same feed) — the
  I1 reconcile-gap is structurally killed.
- INF source-change: 449/$115.1M today corroborates base-DE's MDPF-INF-today (~450/$114M); the
  served-eclipse 400/$96.6M -> 449/$115M is the confirmed freshness drift (merge-in growth), not a
  method shift. base-DE's matched-as-of served-verify was byte-identical -> clean. base-DE co-owns
  the post-deploy served-verify with me.
- Handed to 0.7.0_AE 180018Z for in-lane commit + scheduled-job deploy (both producers together).

## I1+I2 AUTHORING COMPLETE
- GLOBAL producer (compute_account_distribution.py): committed AE a7fd58c4e; DEPLOYING (COO relayed
  the literal-GO to AE 175442Z). true-Global 7,301/$1.49B fresh, dust-floored.
- PER-FIRM (compute_per_firm_account_distribution.py): validated + handed to AE (this cycle).
- HELPER-TRIPLE: floored_percentiles.py 3rd copy (AE a7fd58c4e) + sync-guard PAIR->TRIPLE (mine ab3339e68).
- REMAINING: AE in-lane commit of per-firm + deploy both as scheduled jobs; post-deploy served-verify
  (base-DE + me) on scheduled cadence; smartx-exporter R5 decommission AFTER live+validated.

## Governance
- LD-0157 (Andrew 2026-06-05): worker /work loops RETIRED (event-driven via Monitor + COO /drive).
  CANCELLED my /work cron (d232a3e9). Broker status stays WORKING:/IDLE:/BLOCKED: for /fabric-check.

## Other workstreams
- R2: DONE (tail = storage-trend read next CloudWatch cycle).
- MDLP I3: deployed+accepted (close = scheduled-nightly served-verify + visual smoke).
- GLDINC §5: reconcile-correctness co-owner (PRD v0.2 §5a); P0 reconcile-gate (0.6.0-lead).

## Compiler Tools
| Tool | Run | Result | Notes |
|---|---|---|---|
| ds-commit-gate | compute_per_firm_account_distribution.py | exit 0 | py_compile + undefined-name + ruff (post the builder-unification + constant cleanup) |
| (functional smoke) | python compute_per_firm... --dry-run vs live feed | PASS + RECONCILES w/ Global to the cent | the right validation for a re-sourced producer (read-only, no upload, no gold-runner) |

work-cycle:0017
