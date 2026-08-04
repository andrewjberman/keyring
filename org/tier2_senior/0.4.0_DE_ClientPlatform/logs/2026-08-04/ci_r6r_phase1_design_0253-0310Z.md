# CI-R6R Phase 1 — held-vs-measured render design — 0253-0310Z

**archetype:** IMPLEMENT (design half; no portal edit)

## What happened

COO GO 025350Z for `MDPF_CHANNEL_INDEPENDENCE.CI-R6R.held-vs-measured-render` @7021d48bb4
(row-6 render-half, authored on my ready-for-next; my @b48634789a map receipted as grounding).
ACKed 025412Z, TO flipped `pending`, `comp-to` set. CVO's RAVC-4 validation of the assessment
landed mid-phase (025500Z) — accepted on independent probes; ACKed with the
discriminating-zero method note banked.

Phase 1 delivered @fb872eb805:
`deliverables/CI_R6R_PHASE1_HELD_VS_MEASURED_RENDER_DESIGN_20260804.md` — component census
(6 sites, 2 affected-set exclusions), treatments T1–T5 (carried ring + slate dash distinct from
3F-BF2 amber; in-band window-end transition marker making honest-dark ≠ broken user-visible;
served-meta window statement; card badges; per-firm gated on F-A), field-availability table
(8/10 present in v1.1), flags F-A/F-B/F-C/F-D. Dispatched: DS field-confirm 030449Z (citing
@b91c99dfc4, sparse-preference answering their open Q3), CTO shape-validation flags 030500Z,
COO Phase-1 report 030523Z. **Phase 2 held for the ratified shape via COO/CTO. Portal untouched.**

## Compiler Tools (TO mandate rows, observed vs expect)

| `<run>` | Observed | vs `<expect>` |
|---|---|---|
| my @b48634789a map (cite, not re-derive) | cited; component census built from it + targeted PROD source reads (MP.tsx :417-448, :485-520, :589-594, :632-748, :752-848, :815-860, :2300-2360) | PASS — component list + current data-prop shapes enumerated |
| comp-transform schema-check ModelPortfolios | WARN types-resolution (no co-located types.ts; types live in `api/portal-proxy.ts:437-482` + `endpoints/aum.ts:571-604`) | if_mismatch honored: source read done, gap noted in doc §1 |
| comp-transform schema-check AccountDistributionChart | `Component not found` (tool registry gap) | if_mismatch honored: source-read `src/components/AccountDistributionChart.tsx:15-21`; component is outside the affected set (bell artifact carries no participation meta) |
| field-availability confirm with 0.2.0_DS citing the draft commit | message 030449Z citing @b91c99dfc4; 8/10 fields PRESENT; F-A/F-B the gap; F-D grain confirm requested | PASS — every rendered field exists in draft OR is flagged to CTO's shape validation NOW (F-A/F-B routed 030500Z, BEFORE ratification per if_mismatch: schema flag, not render workaround) |

## Open / gates

- CTO shape validation of v1.1 + my F-A/F-B (the one load-bearing gap) — gates Phase 2.
- DS position on F-A/F-B + F-D confirm.
- Phase 2 (implement on DEV, /frontend-dev screenshots, schema-check --feature + ternary-audit
  for the 'carried' union token, enforced surface-check) — starts only on the ratified shape
  relayed by COO/CTO.
