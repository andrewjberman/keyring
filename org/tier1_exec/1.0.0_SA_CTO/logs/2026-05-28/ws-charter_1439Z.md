# ws-charter cycle 1439Z — NOVEL: ADVI_INFMVP PRD v0.1

**Class:** NOVEL (Andrew direction this cycle — authorized per HARD-BLOCK #7 override)
**Date:** 2026-05-28T~1945Z

## Inbox / context
- Andrew working session in progress: authoring two sibling projects — ADVI_INFMVP (this) + MDPF_SCOPED (forthcoming). Andrew said "take both instructions first" then mid-session authorized authoring ADVI_INFMVP now to start COO decomposition while he writes MDPF_SCOPED.
- Halt-gate clear; watcher PROCESS-OK; registration LIVE; inbox empty.

## Action
- Authored `docs/architecture/ADVI_INFMVP.md` (PRD v0.1) + `org/projects/ADVI_INFMVP.json` + REGISTRY.md row.
- Grounded F2 + F5 in real portal code before writing: F2 = drop `/trade-submission` from inflection allowlist (`firmAccess.ts:39`), section auto-hides (`App.tsx:288-309`); F5 root-cause hypothesis = snapshot vs continuous read different artifact series in `DistributionTab.tsx` (snapshot donut/bell vs continuous `cumulative_chart`), Lifetime Activity a third path.
- Committed `5f6018778`, pushed CLOUD (`f5d75d2f5..5f6018778`).
- Dispatched to COO for TO-decomposition (msg `20260528T194503Z`), F5 flagged as the spine + CVO-RIGID empirical cross-view-equality gate as the acceptance bar.

## Workstreams (F1-F5)
- F1 Assets Overview all-zeroes (DT/DE, investigation-first)
- F2 strip Trade Submission/Tools from Inflection sidebar (RD, small FE-only)
- F3 keyword popup instant-analysis (roll up MKOV_DLYCLD async-precompute, pod 0.1)
- F4 fee-split NNA Lifetime Activity ties to Exec Summary Flows (depends on F5)
- F5 **canonical Advisor NNA — identical across all views; CVO-RIGID gate** (highest priority, the spine)

## Follow-on / next-cycle expected state
- COO decomposition + lane assignment incoming; CC expected.
- MDPF_SCOPED (Andrew sibling PRD) overlaps — esp. F3 general-portal keyword popup; reconcile when it lands to avoid double-dispatch. Watch for it.
- Andrew continuing page-by-page; more ADVI_INFMVP detail or MDPF_SCOPED instructions may arrive.
