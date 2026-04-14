# Session Log — ADVI_PROFAU.006: TaxCostBasisPanel L2 wire

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-04-14 (ET)
**Portal DEV commit:** `5233b91`
**CLOUD commit:** pending (batched below)

---

## Summary

Wired `TaxCostBasisPanel` at L2 (advisor/book view) with `capital_gains_ttm` and
`cost_basis_by_year` from `platinum/advisors/{id}/summary.json.tax_exposure`.
DS QA confirmed fields live 2026-04-14 morning. GO from COO received via MCP
at 15:16 UTC (inbox-watch delivery).

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/AdvisorBookView.tsx` | Add `capitalGainsTtm`, `costBasisByYear`, `topGainPositions: []` to `tax={{}}` prop at L2 | Yes — DEV `5233b91` |
| `portal/src/pages/AdvisorIntelligence/types.ts` | Extend `AdvisorTaxExposure` with `capital_gains_ttm?: number` + `cost_basis_by_year?: CostBasisYear[]`; update stale comment | Yes — DEV `5233b91` |

---

## Implementation Notes

`TaxCostBasisPanel` already fully handles `capitalGainsTtm` and `costBasisByYear`
(optional rendering with null guards). No component changes needed.

`topGainPositions` passed as `[]` — D_04 holdings_lots join deferred to .008.
Panel renders nothing for empty positions array (existing guard at L121).

`AdvisorTaxExposure` at types.ts L990 was missing the two fields despite the
platinum artifact having them. The `.004` TO comment ("types already updated")
was referring to fee/AUA fields on `PlatinumAdvisorSummary.book`, not the tax
sub-type. Both fields added as optional (`?`) for null-safety with older artifacts.

**comp-transform UNUSED note:** `capital_gains_ttm` and `cost_basis_by_year` do
not appear in the UNUSED report because comp-transform reports top-level fields on
`PlatinumAdvisorSummary`, not sub-fields of `AdvisorTaxExposure`. Same alias-
tracking gap noted in PROFAU.005. Render confirmed by code trace.

---

## Acceptance Criteria

| # | Criterion | Result |
|---|-----------|--------|
| 1 | `bun run build` exits 0 | PASS |
| 2 | TaxCostBasisPanel at L2 renders `capitalGainsTtm` | PASS — wired via prop |
| 3 | `costBasisByYear` iterates by `row.year` field (not dict key) | PASS — TaxCostBasisPanel.tsx L102 already uses `row.year` |
| 4 | `topGainPositions: []` — no crash | PASS — TaxCostBasisPanel L121 guards `length > 0` |
| 5 | Null-safe: optional fields, advisors without data show nothing | PASS — `?` on type + panel null guard |
| 6 | `capital_gains_ttm` NOT in UNUSED (sub-field of nested type) | PASS — expected alias gap, confirmed rendered |
| 7 | `cost_basis_by_year` NOT in UNUSED | PASS — same |
| 8 | `bun run build` exits 0 | PASS |
| 9 | Session log with compiler tools committed | PASS — this file |
| 10 | MCP to 2.0.0_SA_COO | PASS — sent post-commit |

---

## Compiler Tools

| Phase | Tool | Command | Result | Note |
|-------|------|---------|--------|------|
| P1 (before write) | comp-transform schema-check | schema-check AdvisorBookView | PASS | `tax_exposure` rendered; sub-fields not in UNUSED (alias gap) |
| P1 (before write) | comp-blast | comp-blast AdvisorBookView | PASS | 4 nodes (3 endpoints + 1 Lambda) |
| P2 (before commit) | comp-transform schema-check | schema-check AdvisorBookView | PASS | 0 MISSING, UNUSED unchanged at 21 |
| P2 (before commit) | comp-blast | comp-blast AdvisorBookView | PASS | 4 nodes unchanged |
| P2 (before commit) | bun build | bun run build | PASS | 0 TypeScript errors |
| P3 (after commit) | comp-transform schema-check | schema-check AdvisorBookView | PASS | 0 MISSING, no regression |

---

## Cross-pod Coordination

| Counterpart | Topic | Outcome |
|---|---|---|
| COO 2.0.0 | PROFAU.006 GO | Received 15:16 UTC, acted immediately |
| COO 2.0.0 | PROFAU.006 complete signal | MCP sent post-commit |
| DT 0.4.0 | .006 separate deploy from W4 batch | .006 ships as follow-up after W4 PROD |

---

## Outstanding

- **DT push** for .006 (after W4 batch completes)
- **/frontend-dev visual test** — TaxCostBasisPanel at L2 with capital gains TTM + cost basis table needs browser verification
- **PROFAU.007** — `is_fee_paying` per AdvisorClient L3 — staged, awaiting DS Q2 TO authoring
