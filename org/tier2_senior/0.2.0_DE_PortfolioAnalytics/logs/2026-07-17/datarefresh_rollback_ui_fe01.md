# DataRefresh rollback UI — TO_PORTALREFRESH_FE_01 build + Time Machine removal

**archetype:** IMPLEMENT

## Current State

Portal **DEV `9374414d4`** — all three FE_01 deliverables built, exercised, screenshot-verified;
Time Machine panel removed (Andrew-direct, see companion record log this date). DE cannot push —
DT batches the promote (CTO ruling 20260717T140755Z: one batch with pending `3b516623`/`84b24af8`).

Files (portal): `pages/DataRefresh/types.ts` (RollbackState/phase + busy flag),
`hooks/useDataRefreshState.ts` (lifecycle + synchronous one-POST ref guard + rollback-mode polling
with unknown-status = clean terminal failure + 409 busy parsing), `tabs/HistoryTab.tsx` (dialog wiring,
lockout on all rows, Rollback Progress panel, Time Machine + pill removed),
`components/RollbackConfirmDialog.tsx` (NEW — catalyst Dialog, dark-on-light per color law),
`api/portal-proxy.ts` (+`manifestKey?` additive, contract v1.1).

Cross-domain: DT contract v1.1 consumed (409 REJECTED_ALREADY_RUNNING / REJECTED_STATE_UNVERIFIABLE
-> amber pipeline-busy terminal; manifestKey optional). ACK exchanged both directions
(20260717T135735Z). FE has no dependency on the BE guard being deployed.

SEV1 note: portal pre-commit surface gate blocked on `portal-proxy.ts` (model_portfolios.benchmark
surface, file-level). Verified staged diff = 2 additive lines on DataRefreshRollbackResponse only;
proceeded with audited `SURFACE_ACK` naming that verification.

## Evidence (exercise-grade, playwright fixture-fed, scratchpad `rollback-exercise.mjs`)

- cancel => **0** rollback POSTs (PASS)
- 6 confirm clicks + 3 locked-row clicks => **exactly 1 POST** (PASS)
- lockout: **0 enabled** rollback buttons while running (PASS); **released** at terminal (2 re-enabled)
- terminals rendered + PNG-read vs silver-canvas law: success (green, restored date), forced 500
  (red, error body), 409 busy (amber, "started 7 minutes ago" age copy) — 4 screenshots in session
  scratchpad, attached to closure message
- `bun run typecheck` exit 0; `bun run lint` exit 0

## Andrew-direct (same session)

Time Machine removal executed (above). "Emergency Rollback" tab: sketch-first — ASCII options
presented in-session, Andrew's pick gates implementation; CTO constraints a/b/c recorded in amended
TO @37d37c5dc (confirm NOT waived; target displayed pre-acknowledge; ALREADY_RUNNING = calm state).

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-transform schema-check HistoryTab` | All rendered fields match response types |
| `comp-transform schema-check RollbackConfirmDialog` | All rendered fields match response types |
| `comp-surface-check check` (by hand, post-block) | CRITICAL file-level on portal-proxy.ts; diff verified additive-only; audited SURFACE_ACK |

No comp-blast: nothing deleted; touched components' consumers are the DataRefresh page only
(verified by import grep). No pod_inventory.xml update: DataRefresh is not a pod-0.2 inventory page
(admin surface, MSTR-assigned); structural additions recorded here instead.

## Phase 2 (same session): Emergency Rollback tab + manifest scrub — portal DEV `064658cd2`

Andrew picked **Option A** (sketch-gate closed by the sovereign pick). Built under CTO constraints
a/b/c: `tabs/EmergencyRollbackTab.tsx` (new, 2nd tab per Andrew's ordering ruling) — hero panel,
single action, target (date/exec/files/duration) displayed pre-acknowledge, same confirm dialog +
lockout + PipelineProgress; calm busy state for concurrent runs (FE-side now, DT's 409 guard slots
in with zero FE change). **manifest.json scrub** (Andrew-direct): all user-visible references
removed — UploadTab step copy + file-type card, FileDropZone hint/preview/row-tag + dead parse
state, `ManifestPreview.tsx` deleted, Invalid-Manifest toast dropped, CurrentStatePanel copy,
`ReadManifest`/`GenerateManifest` display-aliased in PipelineProgress. Internal machinery untouched.

Exercised (emergency scenarios added to the same script): cancel=0 POSTs; 6 clicks=1 POST;
target-displayed assert PASS; success terminal "Restored to 2026-07-14"; 409 → calm busy, no error
wall. typecheck/lint/`comp-transform schema-check EmergencyRollbackTab` clean. Hero + dialog +
terminal + scrubbed-Upload screenshots read vs silver-canvas law (all content inside dark panels).

## Next Steps

- [0.2.0_DT] Push DEV + batch-promote: `3b516623` + `84b24af8` + `064658cd2` head (promote was
  HELD for my final head — ping sent 20260717T144455Z; DE cannot push per role).
- [me] RD POSN_CUSTOM handback review (07-10) still queued behind this dispatch.
