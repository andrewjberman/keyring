# ws-charter — 2026-06-03 1657Z — ADHC_KEEPWARM PRD authored (Andrew GO, parallel-to-workers)

**CLASS:** NOVEL (Andrew direction = keep-warm GO present in inbox this cycle).
**Trigger:** COO relay (`20260603T165504Z`) — Andrew GO'd keep-warm (decision-a); COO fast-tracked both workers; asked CTO to scribe PRD in PARALLEL.

## Authority

NOVEL authorized — Andrew GO this cycle (/ws-charter Step 4b ladder #3). Concur COO's parallel call: design fully settled in AE brief `91df57398`, two-lane split clear, workers can execute while I document → parallel = faster, zero risk (documentation not gating). No HARD-BLOCK.

## Action

Authored **`docs/architecture/ADHC_KEEPWARM_PRD.md`** (v0.1) — FE-driven Lambda keep-warm. Project code ADHC_KEEPWARM (unused, verified).
- Problem: opal-partners-data ~5.4s cold-start (awswrangler module-top) on ~every Advisor-Intel load.
- Solution: Option (a) FE presence-gated view-targeted warm-ping (~$0.15/mo vs ~$27+/mo PC; follows user; $0 idle).
- Lane A (0.7.0_AE): no-op `?warm=1` early-return before I/O, behind edge auth, Terraform. Lane B (0.4.2_RD): useLambdaKeepWarm hook on api-client (presence-gate + view-target + debounce + jitter).
- Footguns (6, all handled), acceptance/verification per lane + e2e, warm-route contract recorded.

FIX1 (21be552d, v2.1.113) documented as already-shipped COMPANION (same cold-start family), NOT in scope. Confirmed SEPARATE surface from ADVI_FEREFI.

## Follow-on

- Notify COO: PRD landed (path + code ADHC_KEEPWARM); COO owns registration + TO-tracking (workers already dispatched). RAVC2s -> COO+CTO+cross-worker.
- Lane A = AE Lambda deploy (separate); Lane B = portal item -> v2.1.114+ promote bundle.
- Optional hybrid floor (d) deferred unless Andrew wants first-hit-of-day smoothing.
- Andrew stack now: cost-basis a/b · v2.1.114 GO (keep-warm GO consumed this cycle).
