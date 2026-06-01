# /ws-charter tick — 2026-06-01 ~2018Z

**CLASS:** FIX (scope-ruling + PRD amendment within active bell-curve project; no novel-scope expansion)

## Inbox
- **0.4.0_DE_ClientPlatform [RAVC2/CC]** (201604Z): bell-curve TO-B partial verify. `INF_09` now emits `total.excluded_unfunded_count=5` (vs buggy 6639), accounts-grain (405 active + 5 excl = 410). **AC2 MET for Inflection** — option-(b) producer-emit proven-out (log 09e4446c9). AC3 NOT yet: only `INF_09` emits the field; `09.generate_partner_analytics` (49/global) + Inflection `by_model` don't. DE asked: is the per-model footer (L1009) in scope?

## Action
- **Scope ruling (201804Z) → DE, CC COO+DS~B:** YES, per-model footer L1009 IS in scope. Same cross-grain subtraction bug class as L1043 (firm-total), compounded for Inflection where model-level distribution is client-grained (`DistributionTab.tsx:175`). `by_model` must carry `excluded_unfunded_count` in BOTH producers so L1009 reads it verbatim. Leaving `by_model` unfixed = known-identical latent defect one model-selection away. FIX-class boundary of the existing durable fix, not novel scope.
- **PRD amend (29b310e4f):** `docs/briefs/mdpf-bellcurve-unfunded-footer-lineage-prd-20260601.md` §5(b) — `by_model`/L1009 explicit + TO-B proven-out status; AC3 → subcriteria 3a (49/global total) / 3b (by_model both producers) / 3c (FE reads field for L1043+L1009, subtraction dropped). INF_09 total = DONE; 3a/3b/3c remaining (DS~B post-respawn).

## Watcher
- VERDICT AUTO-RESPAWN-INTERRUPT-LOST (PID 542234, deaf to interrupts) → killed + relaunched tracked (task bfg9cc67w); interrupt path restored.

## Follow-on / next-cycle expected state
- DS~B (post MSTR [STUCK] respawn): extend `09.generate_partner_analytics` total + add `by_model` field in both producers → DE re-verify AC3 all-firm + per-model → CVO independent.
- Stopgap TO-C holds the visible footers meanwhile (no user-facing wrong number).
- Commit-tag: `ws-charter-cycle:0023 class:FIX` on 29b310e4f.
