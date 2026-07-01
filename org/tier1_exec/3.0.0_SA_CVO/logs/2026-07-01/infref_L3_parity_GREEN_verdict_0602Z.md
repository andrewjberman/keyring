# CVO L3 verdict — ADVI_INFREF rebuild parity = GREEN (authorizes the atomic swap)

**archetype:** VALIDATE

**Serial:** 3.0.0_SA_CVO | **Date:** 2026-07-01 | **Window:** ~05:37-06:02Z
**Gate:** ADVI_INFREF cutover L3 (rebuild output == served full-recompute to the cent). Staged: SSM 2961fd47 (Success rc=0, sentinel 05:36:49Z, env-pinned RUN_DATE=06-30). Tri-validation closure gate (AE + DS~A + CVO), Andrew-direct.

## VERDICT: L3 = GREEN. The staged rebuild faithfully reproduces served to the cent. Swap authorized.

Grounded on the STAGED vs SERVED artifacts (live S3), never a producer self-report. Six failed attempts preceded this; the staged output (2961fd47) is the first complete one — and a scope false-alarm (below) was resolved on independent ground-truth before this verdict.

### Precondition — substrate completeness + scope (was contested; resolved)
A DS~A pre-check + COO HOLD flagged "702/1302 households MISSING → INCOMPLETE", while 0.6.1 claimed "0 missing, staged=active set." I adjudicated the DIRECT conflict on full-population ground-truth (not either self-report):
- Aged every "missing" household via served detail.json vintage (one listing, 998 rows): the 701 served-only = **690 dated 2026-04-27 + 11 NO_DETAIL, ZERO dated 2026-05/06**. Head-object corroboration: 15/15 sampled missing = "27 Apr 2026 18:10Z"; staged control = "30 Jun 2026 17:15Z".
- **Result: the 701 "missing" are pre-existing stale-April orphans (a scope change ~2026-04-24/27; matches clients/_quarantine_scope_bug_20260424/ + 0.6.1's "~1686 cruft"). NOT a dropped-active defect.** The DS~A pre-check tripped on a cruft-inflated denominator (1301 served dirs incl orphans vs the correct ~307-active). DS~A independently converged (SCOPE TRUTH 05:57Z). COO ACK'd DECISIVE; contingency stood down.
- Staged covers the 307-active book EXACTLY: 0 active missing, 0 spurious. client_count 307==307.

### L3 parity — GREEN across every grain (bar: to-the-cent AUA + $0.005 per-dim full-history)
1. **Silver-provenance (staged read the rebuild's own 06-30 silver, pre-daily-chain):** positions_mv (AUA backbone) silver LastModified = 07-01 03:15:36Z = the rebuild's STEP2a write; env-pinned RUN_DATE=06-30 (0.6.1 log); staged header as_of=06-30. It is ~06:00Z, well before the 12:13Z daily bronze->silver chain, so no daily overwrite is possible. All-4-dim correctness is confirmed transitively by the to-cent parity below (detail + timeseries aggregate all dims).
2. **AUA to-the-cent:** served total_aua == staged total_aua == **$202,125,678.08**, delta 0.0000; client_count 307==307; both as_of 06-30. (staged generated_at 07-01T05:35Z = this run; served 06-30T17:16Z = prior nightly.)
3. **Client-grain (point-in-time):** 14 active households, **419 value-fields, 100% match to the cent** (0 diffs > $0.005).
4. **Full-history timeseries:** firm/cumulative_chart (5972 pts) + firm/timeseries_chart (11120 pts) + 3 household timeseries (61 pts each) = **~17,275 numeric points, 100% match to the cent**, structurally identical (0 staged-only/served-only points). The firm-level series aggregate ALL 307 households, so any per-household perturbation would surface here → exhaustive firm-aggregate coverage + sampled per-household.

### Disposition
- **L3 GREEN → the atomic swap is authorized** (0.6.1). Additive / never-widen-safe: overwrites the 307 current, PRESERVES the 691 legacy-stale orphans (they're already served-stale; harness check-5 is scoped to platinum/firm/ top-level, not clients/, so the orphans won't false-RED — DS~A confirmed).
- **NOT yet closed.** Remaining tri-validation legs I still own: L5 cosign (atomic swap correctness, CTO co-signs) → post-swap LIVE verify-channel (served CDN/portal actually renders the rebuilt numbers) → explicit CVO closure-attestation. Only then does ADVI_INFREF close.

### Residuals (non-gating)
- **P2 (upstream, post-cutover):** why the ~690 April households went stale in the normal pipeline (stopped emitting after 2026-04-27) is a SEPARATE pre-existing question, independent of this refactor. The rebuild is faithful to CURRENT silver, which is what L3 tests. COO tracking post-cutover.
- **_meta leak (INF_B_00 → platinum/firm/_meta/):** 0.6.1 flags harness-excluded/benign, cleans post-swap. I will INDEPENDENTLY confirm _meta/ is excluded from the served surface at verify-channel — not blocking L3.
- **L4 (incremental == rebuild reference-parity):** a SEPARATE downstream gate tied to the perf-incremental flip / perf-cron decommission — not part of this full-recompute swap.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp-glob` (value_parity, silver, rebuild scripts) | locate artifacts/paths | PASS |
| `comp-which` (staged-artifact presence) | route | backstop → rail-checked raw S3 (no comp-tool enumerates a `_rebuild/` staging prefix or does staged-vs-served to-the-cent parity) |

What worked: aging the "missing" households via served-artifact vintage resolved a direct producer conflict on ground-truth — the whole point of independent CVO validation; it stopped a false-alarm re-stage AND confirmed the rebuild is complete. No comp-tool fits Lambda-invoke / staged-vs-served to-the-cent parity / SSM-status, so those ran rail-checked.

— 3.0.0_SA_CVO
