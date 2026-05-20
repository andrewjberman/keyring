# SSCN_DIVDEF.010 — Factor Bank Group Relabel + 4-Color Polish (PRD v0.6 §6.9)

**Agent:** 0.3.0_DE_TradingOperations (PM/owner)
**Implementation:** 0.3.4_RD_SecurityScanner (under DE coordination)
**Date:** 2026-05-20
**TO:** `org/tier2_senior/0.3.0_DE_TradingOperations/task_orders/SSCN_DIVDEF.010.de-rd-factor-bank-group-ordering.md`
**RD TO:** `org/tier3_junior/0.3.4_RD_SecurityScanner/task_orders/SSCN_DIVDEF.010_factor_bank_group_relabel.md` (DE-authored, commit `09180b45c`)
**PRD:** `docs/architecture/SSCN_DIVDEF.md` v0.6 §6.9 (commit `2e9fe7f3a`)
**Portal DEV commit:** `7ef0f4a6` (2 files, +7 / -7)
**Workspace CLOUD commit:** see commit landing this log

---

## Phase 1 finding — TO-premise mismatch (surfaced, re-scoped)

The TO + PRD v0.6 §C-item-3 stated portal `utils/categoryOrder.ts` "encodes the WRONG
collapsed 11-category taxonomy" and needs an 11->18 fix. **Empirically false.** The Phase 1
check found `categoryOrder.ts` already has `CANONICAL_CATEGORY_ORDER` = exactly the 18
master groups + `CATEGORY_COLORS` = 18 distinct entries; the file's own docstring records
the migration ("18 categories ... Extracted 2026-03-05 -- supersedes ... 11-group
aggregated view"). The wrong-11 taxonomy is the **registry's** (SSCN_DIVDEF.009's data
scope); the TO conflated registry taxonomy with the portal file.

Per TO-scope discipline this was surfaced to COO before executing rather than silently
no-op-ing categoryOrder.ts. **COO confirmed the re-scope** (2026-05-20): .010 =
FactorBankTab "Category"->"Group" relabel + a 4-color separability polish; NO 11->18
change. CTO notified to correct PRD v0.6 §C in closeout (portal display surface was
already fixed in March -- v0.6's "3-surface fix" is effectively 2-surface).

## Implementation model

DE PM/owner; 0.3.4_RD_SecurityScanner implemented the FE under DE coordination. DE
authored the re-scoped RD design spec, dispatched GO, reviewed the implementation, ran
the compiler mandate, committed, owns this RAVC2.

## Work Completed (2 files)

### 1. `tabs/FactorBankTab.tsx` — 3 user-facing "Category" -> "Group" relabels
- Sortable column header: `<SortableTh label="Category" .../>` -> `label="Group"`.
  `col="category"` KEPT (internal field name; PRD v0.6 §D — do not rename).
- Filter label: `Category:` -> `Group:`.
- Filter "all" option text: `All Categories` -> `All Groups`.
Filter LOGIC untouched — `categoryFilter` state, the `categories` useMemo auto-derivation,
and the `f.category` reads are all unchanged.

### 2. `utils/categoryOrder.ts` — 4-color separability polish
`CANONICAL_CATEGORY_ORDER` unchanged (already the correct 18 master groups). Four
`CATEGORY_COLORS` entries re-hued out of a clustered ~40deg green/teal band:

| Group | Old HSL | New HSL |
|-------|---------|---------|
| solvency | `160, 65%, 52%` | `112, 60%, 50%` |
| growth | `145, 70%, 55%` | `132, 70%, 58%` |
| efficiency | `175, 70%, 55%` | `152, 55%, 48%` |
| liquidity | `185, 70%, 55%` | `170, 72%, 60%` |

Spread across a 58deg band (112-170) vs the old 40deg, with alternating lightness
(50/58/48/60%) + saturation (60/70/55/72%) so the ~20deg-adjacent pairs also separate on
L/S. Bounded clear of neighbors management(85, 27deg) and volatility(195, 25deg); no
collision with the other 14 in-use hues.

---

## Acceptance Criteria Evidence

| AC | Status | Evidence |
|----|--------|----------|
| AC1 | PASS | `CANONICAL_CATEGORY_ORDER` (18) + `CATEGORY_COLORS` (18) both enumerate exactly the 18 master groups (analyst...volatility); 18 distinct HSL colors, no gray fallthrough. Verified by inspection per AC1's own structural-verification clause. The 4-color polish makes the former green/teal cluster legibly separable. |
| AC2 | PASS | `/frontend-dev` render `sscn-010-factorbank-group.png`: the Factor Bank tab shows column header "GROUP", filter label "Group:", filter option "All Groups". No user-facing "Category" label remains on the tab. Filter logic unchanged (auto-derives). |
| AC3 | PASS | `/frontend-dev` smoke 21/21 PASS (`result.json`); `bun run typecheck` exit 0; `bun run lint` exit 0, 0 errors (11 pre-existing other-pod warnings, zero in scope). |

Note: `FactorBankTab.tsx` renders the GROUP cells as plain text; the `CATEGORY_COLORS`
colored chips render in `ScannerHeaderPanel`'s factor table (via `getCategoryColor`). The
4-color polish improves those chips. Live rendering of the re-hued solvency/efficiency/
liquidity is gated on SSCN_DIVDEF.009 correcting the registry `category` values (today the
DIVZ factors carry the old wrong-11 values — growth/quality/systematic/yield/sentiment);
the polish is forward-looking and verified structurally. PARALLEL with .009 as the TO
specifies.

---

## Compiler Tools

| Tool | Phase | Result | Notes |
|------|-------|--------|-------|
| `comp-transform schema-check FactorBankTab` | 1 (before write) | PASS | Baseline: "All rendered fields match their response types." |
| `bun run typecheck` | 2 (before commit) | exit 0 | tsc -b --noEmit clean. |
| `bun run lint` | 2 (before commit) | exit 0, 0 errors | 11 pre-existing other-pod warnings; zero in `FactorBankTab.tsx` / `categoryOrder.ts`. |
| `comp-transform schema-check FactorBankTab` | 3 (after) | PASS | Identical to Phase 1 — the relabel is label-text only, no field/prop change. |
| `/frontend-dev` smoke | 3 (after) | 21/21 PASS | Relabel + color change broke nothing; lineage smoke stays green. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/SecurityScanner/tabs/FactorBankTab.tsx` | 3 "Category" -> "Group" relabels | Yes — DEV `7ef0f4a6` |
| `portal/src/pages/SecurityScanner/utils/categoryOrder.ts` | 4-color separability polish | Yes — DEV `7ef0f4a6` |
| `org/tier3_junior/0.3.4_RD_SecurityScanner/deliverables/page_inventory.xml` | RD core-doc update | RD-lane — RD commits under its own author |
| `org/tier3_junior/0.3.4_RD_SecurityScanner/logs/2026-05-20/sscn_divdef_010_factor_bank_group_relabel.md` | RD session log | RD-lane — RD commits |

---

## Current State

SSCN_DIVDEF.010 complete. Factor Bank tab relabel ("Group") + the 18-color separability
polish shipped to portal DEV (`7ef0f4a6`). All 3 ACs PASS; `/frontend-dev` smoke 21/21.
TO-premise mismatch caught at Phase 1 and re-scoped with COO confirmation — no wasted
no-op on categoryOrder.ts.

DEV only — PROD push is the bundled TO-4/`.006` DT lane (`.007` + `.008` + `.010`), gated
on `.009` close + Andrew DEV smoke.

## Next Steps

- [Dashboard Engineer] RAVC2 to `2.0.0_SA_COO` + CC `1.0.0_SA_CTO`; flip TO `<status>` to
  `complete` on RAVC2 send.
- [0.3.4_RD_SecurityScanner] Commit `page_inventory.xml` + RD session log under RD author.
- [DevOps 0.3.0_DT] Portal DEV `7ef0f4a6` joins the push-ready stack for the `.006` bundle.
