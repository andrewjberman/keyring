# /ws-charter cycle 0010 — §10.6 critical-paths ledger (Andrew-direct via CVO) + D8-AE rulings
**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE

## Classification
- **Class:** NOVEL-delta under Andrew direction (Andrew-direct testing-phase requirements relayed via CVO
  175050Z — same authorization shape as the v0.4.1 cycle-0007 fold), folded into NFRA_GRAPHS §10 as §10.6
  BEFORE AE's D8 TO is cut. Plus two CTO rulings answering COO's open D8-AE questions (175104Z) in the
  same amendment so the TO is cut from one coherent spec.

## Andrew's ask -> the fold
Real-time GLOBGRPH change-tracking on the high-risk surfaces (Model Portfolios — especially
benchmarks/performance — and Advisor Intelligence): loud on ANY feeding-path change; manual-approval
permission; centralized ledger (approved methodology changes, ingestion-source changes, code changes,
staleness) at org/critical_paths/{stale_warning,change_management}. CVO's mapping (D8 covers ~90%, 4
deltas) CONCURRED after my own §10 read — deltas folded as §10.6 L1-L4:
- L1 durable ledger, approval-as-ledger-entry STRUCTURAL (SURFACE_ACK writes its own entry);
- L2 critical-chain staleness routes into /stale_warning;
- L3 marker-keyed real-time leg with honest per-class latency statement (2b-extracted = minutes; outside
  2b coverage = nightly; P1-A option-c extends);
- L4 caught classes named (methodology = gold SHA delta; ingestion = bronze/source-config node delta).
AC8 extended (d) ledger-entry-per-class + (e) marker-keyed minutes-latency demo.
Skeleton seeded: org/critical_paths/README.md + change_management/ + stale_warning/.

## Rulings (D8-AE open items, COO 175104Z)
1. **advisory->blocking flip = composite of all three:** clean post-F6 re-sign w/ CVO confirm + one full
   nightly (synthetic-break fires, Day-0 knowns suppressed) + 0 advisory false-positive SEV1 hits.
   Either single trigger alone risks blocking on a bad baseline or alarm fatigue. ~1-2 day ramp.
2. **Integration tier = safe-commit.sh wrapper (parent, all-file scope per Rule 14a) + portal pre-push.**
   NOT ds-commit-gate (Python-only). Hook path is QUERY-only (cached comp-diff, ms; no rebuild — Rule 20).

## Compiler Tools
| Tool | Run? | Why / result |
|---|---|---|
| comp-* (any) | NO | Doc/registry amendment + ledger skeleton; carve verification ran THIS session under the v0.3 review (direct portal-source reads). Build mandates ride AE's D8 TO (comp-diff/comp-xref are its subject matter). |

## Follow-on
COO cuts/updates AE's D8 TO from §10.6 (L1-L4 + the two rulings); DE baselines proceed on v0.3 (already
unblocked); CVO validates the §10.6 scribe vs Andrew's ask + holds AC8(d)/(e) verification legs.
