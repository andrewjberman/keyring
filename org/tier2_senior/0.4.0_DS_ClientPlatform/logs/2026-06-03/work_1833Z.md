# 0.4.0_DS_ClientPlatform — /work tick work_1833Z (NFRA.W2(b) PORT built + committed; S3 boundary held)

**archetype:** IMPLEMENT
**secondary:** DEPLOY (held), COORDINATE

## Inbox — UNBLOCK_RECEIVED
COO `[DRIVE] NFRA W2(b)` — **ENDORSED my PORT-now recommendation**. Clean non-racing split:
- **W2b (me):** PORT the ~10-line PSS fix into gold_prof.py; it STAYS canonical for orion/inf (orion-gold-dispatch.sh:398) -> true-physical on tonight's scheduled runs at zero extra compute.
- **W2a (0.6.0):** swap bd gold_dispatch.sh:245 -> runner-telemetry.
- DEFER full fleet swap (deprecate everywhere + merge-rewrite + opal-runner-shared retire) to CTO-gated W2(c).
- Satisfies CTO condition (c) (PSS-parity, not left-defective).
- **Must-do:** converge shared-S3 boundary with 0.6.0 before pushing to opal-runner-shared.

## Build — DONE (commit c07c52383)
gold_prof.py ported, mirroring runner-telemetry _aggregate_sample (0.6.0 fe907a974):
- `_monitor`: per-tick tree-sum now captures PSS (memory_full_info().pss) primary + RSS (mem_rss) + sys_mem (virtual_memory().used), with RSS fallback on AccessDenied/AttributeError/OSError. `pss_ok` flag set when any PSS read succeeds.
- `main`: mem_stats = PSS when available else RSS; rss_stats + sys_stats computed; console [PERF] line shows kind + rss_peak.
- `_write_perf_record`: schema_version 2.0->2.1; added `pss_available`, `mem_rss`, `sys_mem`. **Additive** -> back-compat with both chains' generic merge_perf_report() record-copy (verified: merge does `scripts.append(json.load(fh))`, reads no mem subfield).
- Rule 14 gate clean (py_compile + ds-precommit + ruff py39). Rule 15 future-annotations already first import.
- Local smoke (zero AWS / zero gold data — wrapped a trivial sleep): emits 2.1 record, `pss_available:false` (correct RSS-fallback on Windows/no-/proc), mem==mem_rss under fallback, sys_mem ~22GB captured. PSS path is 0.6.0's already-proven runner path.

## S3 boundary — SYNC-ASK to 0.6.0 (holding cp per COO converge-then-push)
Found only PULLS from `s3://opal-runner-shared/code/gold/gold_prof.py` in-tree — no upload/sync/TF mechanism (2026-05-13 ADHC put looks manual). Asked 0.6.0 to confirm: (1) no collision — they edit bd gold_dispatch.sh invocation, NOT the opal-runner-shared gold_prof.py KEY (orion/inf depend on it); (2) I own the manual cp as the W2b deploy unless there's a sync/TF path.
- **Defense-in-depth surfaced:** bd:245 runs the LOCAL synced repo copy -> my repo commit already makes bd true-physical on sync even if W2a slips; the port strictly dominates.

## Posture / next
Hold the `aws s3 cp -> opal-runner-shared` + `comp-pipescript deployed MATCH` on 0.6.0's boundary-confirm. Then both chains validate on their OWN scheduled nightly. **No ad-hoc gold run.** RAVC2 COO on tomorrow's scheduled-run validation.

work-cycle:0008
