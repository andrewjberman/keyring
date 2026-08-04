# CI-R6R Phase 2 — held-vs-measured implementation + render evidence — 0308-0340Z

**archetype:** IMPLEMENT

## What happened

CTO ratification 030839Z cleared the Phase-2 gate (v1.1 + participation-LITE; F-C sparse
confirmed; F-D by_model_channels approved optional). DS pre-commit name flag 031649Z pinned the
LITE binding (same names + new `scope` discriminator; `no_measured_value` reason vocabulary;
demo data described). Implemented on the portal DEV working tree:

- `src/lib/pairedProvenanceRead.ts` +149: ratified-vocabulary readers
  (`readChannelParticipation` / `readParticipationMarks` / `firstPastWindowDates` /
  `participationWindowStatement` / `readByModelChannels`), tolerant + loud-degrade
  (unknown status → absent, never silently contributed), binding ONLY
  `meta.channel_participation` — never the incumbent carried-leg strings.
- `src/pages/ModelPortfolios.tsx` +213/-11: participation state block; T1 slate dashed
  `carried_total` trace + hollow ring dots (amber on watch) + facts-only tooltip rows +
  legend chip; T2 vertical `window end — <channel> dark` ReferenceLine (frontier-safe after
  two measured label-clipping iterations) + past_window tooltip rows + footnote dark-notes
  (carries T2 for gap-dropped tail dates); T3 served-meta carry-window statement;
  `carried_total` added to the tooltip's double-count exclusion beside `interp_total`.

**Load-bearing discoveries en route:** (1) the page carried THREE Andrew-direct deletion
markers (~0450Z via COO 044951Z) striking a prior carried treatment whose reason-asserting
label misled — SURFACED to COO before proceeding (031621Z); COO interim 031733Z: T2/T3
proceed, T1 commits nothing until Andrew's word (he is at COO's terminal); my implementation
binds pixels to the ratified meta only, so nothing renders on any artifact served today.
(2) The deletion comment's condition — "decided with real data in front of Andrew" — is
served by the fixture PNG + DS's coming real artifacts. (3) Answered COO's stamp-attribution
ask from my map: 'Model detail as of 2026-07-23' = the F1 frozen json artifact's own
last_updated (MP.tsx:1306, :1310-1311), an unrepointed read, stamp mechanism itself honest.

**Evidence @ committed `deliverables/ci_r6r_evidence/`:** no-regression PNG (meta absent =
pixel-identical page, LOC /portfolios verified, silver-canvas law read on the PNG) +
lit-up fixture PNG (REAL platinum global artifact + demo meta: carried age-1 / age-2+watch /
past_window transition — T1/T2/T3 all visible) + the fixture json.

**COMMIT (portal) HELD ON TWO GATES:** Andrew's T1 word (via COO) + CTO's SEV1 surface ack.
T2/T3 + readers commit regardless of the T1 answer (delimited strip-clean blocks).

## Compiler Tools (TO mandate rows, observed vs expect)

| `<run>` | Observed | vs `<expect>` |
|---|---|---|
| implement on DEV | working tree +351/-11 across 2 files; portal stays on DEV; nothing committed | per interim gates — deliberate |
| `bun run typecheck` (tsc -b, canonical) | clean, zero errors | PASS |
| `test:provenance-guard` | `OK: no unlabeled reads` | PASS — new readers live in the allowlisted module |
| comp-transform schema-check ModelPortfolios --feature carried | WARN types-resolution only (types in portal-proxy.ts/aum.ts, source-read) | if_mismatch honored; no data-prop MISSING |
| comp-transform ternary-audit ModelPortfolios | no union-typed variables found (TabType only) | PASS — design adds NO union token; carried rides participation marks, `pointClass` untouched |
| comp-surface-check check | **SEV1 block-with-ack** (headline+benchmark file-membership) + SEV2 WARNs + contract advisories | STOP honored: routed to CTO 033653Z with the no-value-path justification; SURFACE_ACK not invoked |
| /frontend-dev screenshots (ui-smoke.mjs, LOC-verified) | no-regression PNG + lit fixture PNG v3 (2 label-clip iterations measured and fixed) | PASS — rendered distinction visible; silver-canvas law checked on the PNGs |

## Open / gates

- Andrew's T1 word (COO terminal) → then portal commit (with or without T1 blocks).
- CTO SEV1 surface ack → same commit gate.
- DS's S3-vintage ping when served artifacts carry the meta → the ACCEPTANCE exercise pass
  (/frontend-dev on real served data), then the closure package to COO+CTO+DS + DT promote handoff.
- Deferred: T4 card badges (needs by_model_channels live), monthly-grain treatment decision.
