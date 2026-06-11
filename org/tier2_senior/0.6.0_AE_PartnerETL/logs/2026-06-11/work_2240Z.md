# 0.6.0_AE_PartnerETL — work cycle 2026-06-11 2240Z

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, DEPLOY

GLDINC segment 5 (closing the day): A_01 incremental rebased + parity-proven
3/3 + final handoff to DS. Dispatcher SHADOW_SET extended for B_02. 3 of 7
scripts fully engineered+proven in one day, all through the DS Rule-13 chain.

## Dispatcher (AE lane)
GLDINC_SHADOW_SET += B_02.canonical_lots.py (d0f9345b8, pushed, S3 md5 MATCH
f2cecce6...). B_02 BOOTSTRAP rides the 04:00Z run; containment scoring night-2+.
The running 22:04Z chain pulled the pre-update dispatcher (A_02-only) — its
A_02 night-1 scorecard lands ~23:00Z.

## A_01 incremental — rebased on 73ec87a84, PROVEN, handed off
- DS landed the oracle-fix (73ec87a84, CTO 221138Z + COO 221154Z never-widen
  sign-offs, drift acceptance embedded in commit) + B_02 (4a62d0fdf) earlier.
- Rebase upgrades vs the parked v2: cache keeps BOTH provenance cols
  (_file_date + _intra_pos); under the deterministic total-order dedup,
  union-survivor == full-survivor at every (account,date) BY CONSTRUCTION.
- Rebase gap caught by re-proof: load_transactions(keys=None) param was
  WIP-only, HEAD lacked it -> TypeError; re-applied. (Also: pipe-masked exit
  codes hid the traceback as rc=0 in the first run — re-ran with per-lag rc
  capture. Proof-hygiene lesson banked.)
- PARITY vs STABILIZED oracle: 3/3 lags (1/3/10d) BYTE-IDENTICAL — 14,866
  rows, sym_diff=0, cell_mismatches=0 each.
- Load-completeness guard fired LIVE mid-proof on a real transient S3 read
  failure (1/1808, 2021-09-30.parquet), refused the build; retry clean. The
  pre-fix code would have silently built from incomplete data.
- Handoff -> DS 2237Z (files gate-clean uncommitted). Hardening flag (DS lane,
  separate): bounded retry-with-backoff then raise.
- After DS deploy: A_01 joins GLDINC_SHADOW_SET (AE lane).

## Day total (ADHC_GLDINC incremental workstream, Andrew-direct)
| Script | State | Evidence |
|---|---|---|
| A_02 (1/7) | DEPLOYED (887ffd17d+c8ed91949); night-1 parity shadow riding 22:04Z | 0-diff x3 offline |
| A_01 (2/7) | proven, final handoff w/ DS | 3/3 byte-identical vs stabilized oracle |
| B_02 (3/7) | DEPLOYED (4a62d0fdf); BOOTSTRAP rides 04:00Z | fp determinism 2,352/0; 7-date no-change sizing |
| B_03 (5/7) | classified (shares B_02 machinery) | next |
| B_01/A_03/A_04 | hybrid designs queued last | brief §3 |
+ 2 pre-existing production defects found+fixed via the proof harnesses:
  A_01 random tie-survivor (oracle non-determinism, CTO+COO-signed fix) and
  the swallowed-read-failure load path (guard, validated live same evening).

## Compiler Tools
| Tool | Result |
|------|--------|
| ds-commit-gate (A_01+s3_layout x2, dispatcher bash -n) | CLEAN |
| (proof harness) 3-lag shadow x2 runs | 3/3 PASS + 1 guard-fire (transient, retried clean) |

## Next (event-driven)
1. DS A_01 deploy RAVC2 -> A_01 joins SHADOW_SET.
2. B_03 implementation (B_02 machinery) — next working session.
3. AM review: COTETL verify (checklist staged) + A_02 night-1 + B_02 BOOTSTRAP
   + load_flows post-fix + PRTORG AC-closeout.
4. Cutovers: per-script clean nights + Andrew nod (hard gate).
