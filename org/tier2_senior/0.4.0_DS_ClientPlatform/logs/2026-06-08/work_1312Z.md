# 0.4.0_DS_ClientPlatform — work_1312Z (MDLP_DISTFIX I1+I2 first-unattended parity-verify — GREEN)

**archetype:** VALIDATE

## Cold-boot bring-up (LD-0165, COO-provisioned 59ef527f8)

Startup clean: registered (PID 20528), persistent inbox Monitor armed (task `bgsvrg0hj`),
inbox empty, 0 stale crons. **No `/work` cron armed** — LD-0157/LD-0166 retired worker self-tick;
event-driven via Monitor + COO `/drive` is the tick driver. (Launch msg's LD-0082 "CronCreate /work
20m" is superseded — confirmed against org/XXX.md §F + LD-0166 ledger commit 01ff30845.)

## Deliverable — first unattended MDPF-sourced distribution validation (MDLP_DISTFIX I1+I2)

Per my 06-05 obligation #3 + project JSON close-item (1): the I1+I2 re-source deploy (AE, 06-05
~14:18 EDT, a3ad9a933) put the account-distribution producers on a **daily 11:30Z EventBridge
schedule** reading the live MDPF feed. The weekend was the first window the path ran **unattended**.
**Validate-on-nightly discipline observed — ZERO ad-hoc runs; verified the SERVED artifact only.**

### Served artifacts (all `opal-data-portal-v2`, portal-consumed)

| Artifact | Key | LastModified |
|---|---|---|
| Global | `json/portfolios/account-distribution.json` | 2026-06-08 11:30:40Z |
| Global (mirror) | `s3://opal-data-smartx-v2/views/account_distribution.json` | 2026-06-08 11:30:40Z |
| 49F | `json/mdpf/49financial/account-distribution.json` | 2026-06-08 11:30:41Z |
| INF | `json/mdpf/inflection/account-distribution.json` | 2026-06-08 11:30:41Z |

### EXISTS / FRESH / SCALED / NOT-FROZEN + reconcile + dust

- **FRESH + NOT-FROZEN (unattended):** version history of the Global key shows the schedule fired at
  11:30:39-40Z on **06-06, 06-07, 06-08** — three consecutive unattended runs, identical 7709B
  (stable because the MDPF feed partition is pinned at `2026-06-05` — Friday, the latest weekday;
  weekend feed does not advance, expected). The EventBridge daily schedule is reliable.
- **RECONCILE (I1 gap structurally dead):** Global `7,301 / $1,491,982,925.05` **== 49F+INF exactly**
  — count MATCH (6,852 + 449 = 7,301), AUM delta **$0.00**. Global is sum-of-per-firm by construction.
- **DUST FLOOR (I3 on the served unattended path):** min Global $1,037.34 / 49F $1,037.34 /
  INF $1,150.67 — all **≥ $1K**. p10 Global $7,987.52 / 49F $7,574.29 / INF $18,381.26 — all ≫ $1K
  (the pre-fix $8.42 dust is gone).
- **PARITY to attended deploy as-of:** numbers reproduce the 06-05 attended deploy-time validation
  (7,301 / $1.492B) to the unit — the unattended scheduled path is byte-consistent with the
  hand-validated deploy. Sources confirm MDPF feed (not the dead `smartx_allocations.parquet`):
  `s3://opal-data-mdpf/mdpf/feeds/model_aua_positions/{firm}/2026-06-05.parquet`.

### Non-scope note (not a defect)
Global `by_model` retains blend keys (`Opal Blend 5050 Int Ltc/St Int`) as separate model entries —
this is the **distribution producer's native taxonomy** for the secondary by_model cut, NOT the
MDPF_COUNTS Global-Count blend-fold (separate producer `build_aggregate_aua_timeseries.py`, which I
reverted 06-05 per 4386bdc2d). The load-bearing `total` (histogram + percentiles + reconcile) is
correct and reconciles to the cent. Out of I1/I2/I3 scope.

## Verdict
First unattended MDPF-sourced distribution validation = **GREEN on all axes** (fresh+unattended,
reconcile-to-cent, dust-floored). RAVC2-close filed to COO. Project close-item (2) — smartx-exporter
R5 decommission — is now unblocked (Andrew-gated, AE 0.7.0-owned, post-parity).

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| (S3 metadata) | head-object x4 served keys (freshness) + list-object-versions (unattended-run proof) | all 11:30Z 06-06/07/08 |
| (S3 content read) | get-object Global + 49F + INF, reconcile + dust check in Python | Global==49F+INF to $0.00; min all ≥$1K |
| comp-pipescript deployed | N/A | smartx/orion producers not bd-keyed (comp-pipescript is `opal-data-bd`-scoped); served-artifact read is the correct verifier for a re-sourced producer on a non-bd bucket |

work-cycle:0001
