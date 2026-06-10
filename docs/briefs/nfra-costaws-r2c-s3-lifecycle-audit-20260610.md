# NFRA_COSTAWS R2(c) — Fabric-Wide S3 Lifecycle Audit

**Owner:** 0.7.0_AE_CloudOps~B · **Date:** 2026-06-10 · **Mode:** READ-ONLY analysis (no lifecycle writes)
**PRD:** docs/architecture/NFRA_COSTRED_PRD.md §R2 · **Standard target:** noncurrent ≤14d (or NewerNoncurrentVersions:3) on versioned buckets *except where noncurrent is load-bearing*, `logs/` expiry, abort-incomplete-MPU 7d.

---

## Per-bucket lifecycle census + gap assessment

| Bucket | Versioning | Current lifecycle | Gap vs standard | Noncurrent load-bearing? |
|---|---|---|---|---|
| opal-data-bd | Enabled | noncurr 90d (*) + gold/ 36d + platinum/ 36d + abortMPU 7d | whole-bucket 90d→14d candidate (R2a, Andrew-gate); gold/+platinum/ 36d are DELIBERATE floor | **YES** — gold/ → Portal Time Machine (bd-time-machine pins VersionIds); 36d floor = Dynamo PITR 35d coherence. DO NOT tighten gold/ below 36d |
| opal-data-inf | Enabled | otp/ expire 1d ONLY | **BIG GAP** — versioned + daily gold rebuild + NO noncurrent rule + NO abortMPU. PRD-flagged (88 GB). Add noncurrent + abortMPU | Check: derive/yang consumers? grep clean for inf so far — likely safe to add noncurrent |
| opal-data-mdpf | Enabled | NONE | **GAP** — versioned, daily rebuild, no rules | **MAYBE** — build_mdpf_count_backfill_pre0518 read noncurrent (MDPF_COUNTS recovery). Verify before tighten |
| opal-data-cot | Enabled | NONE | GAP — versioned, no rules | **YES** — gldrst restore tooling (preflight_snapshot/restore_old_keys) + the $373M gold seed safety net. Treat carefully |
| opal-data-portal-v2 | Enabled | noncurr 90d (*) + abortMPU 7d | 90d→14d candidate | **YES** — yang-time-machine + capture-output-versions consume noncurrent. DO NOT blanket-tighten |
| opal-data-portfolio | Enabled | expire 90d (*) | current-expiry 90d may delete LIVE data (verify intent); no noncurrent rule; no abortMPU | **YES** — portfolio_versions_list / portfolio_export_download serve version history |
| opal-data-schwab | Enabled | 01_raw/ archive transition | no noncurrent, no abortMPU | Custodian source-of-truth — likely keep; add abortMPU |
| opal-data-imo | Enabled | rich (corp/serving/telemetry/qa/archives cold + telemetry/qa noncurr 30d + abortMPU) | noncurrent only on telemetry/+qa/ (30d>14d); missing on corp/serving/archives | Likely safe; best-covered bucket |
| opal-data-smartx-v2 | Enabled | NONE | GAP — add noncurrent + abortMPU | grep clean — likely safe |
| opal-data-aaii-v2 | Enabled | NONE | GAP — add noncurrent + abortMPU | likely safe |
| opal-data-news-v2 | Enabled | NONE | GAP — add noncurrent + abortMPU | likely safe |
| opal-data-demo | Enabled | NONE | LOW PRIORITY — one-time static build (memory: never rewritten → minimal noncurrent bloat); add abortMPU | n/a (static) |
| opal-data-trade-submissions | Enabled | submissions/ Glacier | no noncurrent/abortMPU | **COMPLIANCE** — likely regulatory-retain; do not expire |
| opal-data-etfs | Disabled | NONE | minor — add abortMPU | n/a (versioning off) |
| opal-data-news-av | Disabled | NONE | minor — add abortMPU | n/a |
| opal-data-pm | Disabled | NONE | minor — add abortMPU | n/a |
| opal-313476888478-globgrph | Disabled | abortMPU 7d | OK (versioning off by design; Nessie versions) | n/a |
| opal-runner-shared | Enabled | NONE | minor — low churn; add noncurrent + abortMPU | likely safe |
| opal-313476888478-lambda-artifacts | Enabled | NONE | GAP — deploy-history zips accumulate; keep-N noncurrent reasonable | TF uses latest version_id; old = history |

(*) = whole-bucket prefix.

---

## Load-bearing noncurrent consumers (the critical finding)
VersionId/CopySourceVersionId grep surfaced **5 buckets whose noncurrent versions back live features** — a blanket "14d fabric-wide" would break them:
1. **opal-data-bd gold/** — Portal Time Machine (bd-time-machine, bd-capture-output-versions). 36d floor deliberate.
2. **opal-data-portal-v2** — yang-time-machine + capture-output-versions.
3. **opal-data-portfolio** — portfolio_versions_list / portfolio_export_download (version history UI).
4. **opal-data-cot** — gldrst restore tooling + $373M seed safety net.
5. **opal-data-mdpf** — count-backfill recovery (MDPF_COUNTS incident used noncurrent).

Per memory `reference_s3_noncurrent_retention_can_back_live_feature`: verify the noncurrent consumer + cross-source coherence floor BEFORE tightening any of these. Prefer prefix-scoped tightening (non-load-bearing prefixes) + keep the load-bearing prefix's window.

---

## Gap classification (non-gated vs Andrew-gated)

**NON-GATED (COO can authorize — near-zero recovery value):**
- Add `abort-incomplete-multipart-upload 7d` to the 11 buckets lacking it (deletes only failed uploads).
- Commit this audit table (AC3).

**ANDREW-GATED (C2 — expires real data):**
- Any `NoncurrentVersionExpiration` add/tighten (deletes old versions) — esp. the 5 load-bearing buckets.
- opal-data-bd whole-bucket 90d→14d (R2a).
- opal-data-portfolio current-expiry intent review (90d may delete live objects).
- `logs/` expiry adds.

**SAFEST FIRST MOVES (recommend):** (1) abort-MPU everywhere (non-gated); (2) noncurrent rules on the GREP-CLEAN versioned buckets (inf [verify], smartx-v2, aaii-v2, news-v2, runner-shared) — Andrew-gate but lowest risk; (3) hold all 5 load-bearing buckets for per-bucket consumer+coherence analysis before any tighten.

---

---

## ADDENDUM 2026-06-10T15:1xZ — deployed+INVOKED re-verification (Andrew premise correction)

Andrew sovereign ground-truth (via MSTR 151810Z): the Portal Time Machine was **never operationalized** (frontend scaffolding only). This invalidates the grep-based "load-bearing" call — grep finds code refs, but the code may be dead. Re-verified the 5 by the stricter **deployed + INVOKED** standard (CloudWatch Invocations, 90d):

| Bucket | Noncurrent consumer | Deployed? | Invocations/90d | REVISED verdict |
|---|---|---|---|---|
| opal-data-bd | bd-time-machine (restore) | yes | **10** (test-level) | NOT live-load-bearing. portal-time-machine (user entry) = **0**; bd-capture-output-versions writes 447/90d but for a never-wired feature. **36d floor void → Andrew-gated TIGHTEN CANDIDATE** (confirms Andrew + the CTO "waste" framing). Restore works if ever needed (10 test restores). |
| opal-data-portal-v2 | yang-time-machine | yes | **0** | DEAD scaffolding (yang-capture writes 26/90d, restore never invoked). **TIGHTEN CANDIDATE.** |
| opal-data-portfolio | opal-portfolio-versions-list | yes | **136** | **GENUINELY LIVE — KEEP noncurrent floor.** (export-download + version-get = 0, dead; but versions-list is an active portal feature serving noncurrent versions.) The ONLY survivor of the stricter test. |
| opal-data-cot | gldrst restore scripts | scripts (one-time migration tooling) | n/a (not standing) | seed now in git (6b0be4337) = primary backup; versioning secondary. **TIGHTEN CANDIDATE w/ care.** |
| opal-data-mdpf | count-backfill | one-time MDPF_COUNTS recovery | n/a (not standing) | one-time historical recovery, not a standing consumer. **TIGHTEN CANDIDATE** (note: noncurrent enabled a past recovery). |

**Net:** of the 5 originally flagged, only **opal-data-portfolio** is genuinely live-load-bearing (versions-list 136/90d). The other 4 (bd, portal-v2, cot, mdpf) are Andrew-gated tighten candidates by the deployed+invoked standard.

**portfolio 90d current-expiry — downgraded** (per COO 2026-06-10): versioning=ENABLED, so the 90d Expiration writes a DELETE MARKER (soft-hide, recoverable via noncurrent), NOT permanent deletion. 1 object (PFDE trade export, 8d old). Reclass from "LIVE-data-deletion risk" to "intent-confirm: 90d soft-hide on versioned PFDE exports, recoverable, not urgent."

**Banked rules:** (1) verify deployed+INVOKED (CloudWatch), not just grep, before calling a noncurrent consumer load-bearing — the Time Machine trap. (2) versioned bucket + current-object Expiration = delete-marker (recoverable), not permanent loss — check versioning before flagging Expiration as data-loss.

---

## ACs
- AC3 (fabric-wide audit table committed): THIS DOC (+ addendum).
- AC1/AC2/AC4/AC5: lifecycle CHANGES are a separate (gated) TO — this TO is analysis-only per drive #28. abort-MPU (non-gated) applied to all 15 lacker buckets (11 zero-rule + 4 merge) 2026-06-10, verified, existing rules preserved.
