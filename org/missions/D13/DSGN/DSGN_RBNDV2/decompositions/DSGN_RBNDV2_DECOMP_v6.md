# DSGN_RBNDV2 -- DECOMPOSITION (L5) -- ROUND 6, THE BORDER SWEEP AND THE FOOTER SOURCE CASING (PRD v0.1)

```json
{
 "project": "DSGN_RBNDV2",
 "directive": "D13",
 "macro": "DSGN",
 "fabric": "laptop",
 "decomp_version": "v6",
 "step": 5,
 "prd_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/prd/DSGN_RBNDV2_PRD.md@e71a48e4b0 (v0.1, RATIFIED; both halves signed)",
 "round_analysis_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/ledger/ROUND_ANALYSIS.round5.md@be73778002 (1.0.0_SA_CTO; CTO msg 109445)",
 "author": "2.0.0_SA_COO~RB",
 "round": 6,
 "rectangle": "the CTO's round-5 enrichment items 1 and 2: (1) the border-white/N class sweep with the Trending Topics regression first, before and after list printed, one walk; (2) the footer source-name casing sweep; item 3 (Andrew's next page and call 002b) is cut only on his words",
 "cells": 2,
 "chains": 1,
 "join_cells": 0,
 "portal_base": "feature/dsgn-rbndv2-light @d0cb67d0 (local, no upstream, never pushed)",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~RB`. **Input:** the CTO's round-5 analysis (msg 109445) over the CVO's L9 grades (`ADJUDICATION_v6.md`, six of six MET). **Frozen at the cut.**

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

Denominator: the CTO's three round-6 items. Item 1 PLACED as `RV-y-1`. Item 2 PLACED as `RV-y-2`. Item 3 (Andrew's next page's comments and the answer to `002b`) HELD with its condition (his words); FWD-4 (heat maps) HELD (his answer, owed at this terminal). Remainder after subtraction: item 3 and FWD-4, held.

**Measured cause of item 1 (source read at d0cb67d0):** round 4's stylesheet block at `portal/src/index.css` lines about 593-615 maps every `.border-white\/N` to `var(--rb-rule)` inside a light surface, so a component that kept `border border-white/10` from its dark-ground days (the Trending Topics row, `ExecutiveSummary.tsx` about line 989) is boxed again. Population in the Market Overview scope: about 70 occurrences in 6 files (`ExecutiveSummary.tsx` 11, `FearGreedModal.tsx` 7, `IndexPerformanceModal.tsx` 3, `KeywordSentimentModal.tsx` 23, `MarketRegimeModal.tsx` 4, `RSIModal.tsx` 12) plus 2 in `SentimentGauge.tsx` (owned by `RV-y-2`'s file set, so left to the walk); the whole portal holds 622 occurrences in 119 files, which Andrew's page-by-page walk reaches page by page. **Measured cause of item 2:** footer strings are written as `'Source: Global news.'` (`SentimentGauge.tsx` 128) and `'Source: Financial news.'` (`ExecutiveSummary.tsx` 245, 264); round 5 removed the forced uppercase, so a footer now shows its string as written.

## 2. THE CELLS -- 2 (round 6)

| cell | what it builds | serves | writes | risk | class |
|---|---|---|---|---|---|
| `RV-y-1` | every `border-white/N` in the Market Overview scope is classified KEEP (control, one-sided rule, hairline, floating popover) or DROP (a boxed row or card) and the DROP ones become `border-transparent`; the Trending Topics row first; the before and after list is a deliverable | FWD-3, FWD-5 | the ten `market-performance` components other than `SentimentGauge.tsx`, `src/pages/MarketPerformance/`, `src/__tests__/dsgn-rbndv2/` | LOCAL | worker |
| `RV-y-2` | every footer source string obeys proper capitalization ("Global News"), found by a sweep and held by a test over every non-test source file | FWD-3, FWD-5 | `SentimentGauge.tsx`, `ExecutiveSummary.tsx` (the two footnote lines), `src/pages/`, tests | LOCAL | worker-light |

## 3. PLACEMENT, EDGES, BATTERY

One chain: `RV-y-2` depends on `RV-y-1` (both write `ExecutiveSummary.tsx`; `RV-y-1` owns the file's borders, `RV-y-2` only its two footnote strings), so the cells are spawned one after the other and merged each before the next worktree is cut (disk is at 91 percent used). The closing proof is the COO's live walk of `/market`: the Trending Topics rows' computed border colour, the controls' borders kept, the footers' source names; then the CVO's grade and Andrew's eye (DEC-5). comp-iam, comp-schedule: not applicable. comp-adversary: no other order is open; rule 20 graph check: portal source only.

## 4. RULE 24 FOUR-POSTULATE RECORD

(i) MECE over the CTO's list by subtraction (section 1). (ii) One grain: a source-file class per cell. (iii) One intent per cell: the white-alpha border class in the Market Overview scope (y-1); the footer source-name casing (y-2). (iv) State coherence: y-1 moves only the all-sides `border border-white/N` of container elements (and its hover form) to transparent and leaves controls, one-sided rules, hairlines, popovers, the stylesheet rule and every colour; y-2 moves only the case of letters in footer strings and leaves the footer layout, the `PanelFooter` component and every source word.

## 5. FINDINGS FOR THE CTO (at the cut)

- The sweep is scoped to the Market Overview page's files because that is the page Andrew has walked; the stylesheet rule that made the borders visible is not touched, since controls and hairlines rely on it. The 622 occurrences elsewhere in the portal follow his pages as he walks them.
- Footer casing is held by a test that reads every string literal beginning `Source: ` in non-test source, so a future lower-case source name fails the suite.

## ADDENDUM 1 (2026-10-15 ~17:0xZ, 2.0.0_SA_COO~RB, issuer ruling inside its own decomposition) -- cell `RV-y-3`, a direct act

Found at the round-6 drain of `RV-y-1`: (a) `tsc -p tsconfig.app.json --noEmit` from the portal root reports `TS2769` in `src/__tests__/dsgn-rbndv2/rb-5-x5.hover-resolve.test.ts:30` (`maxBuffer` is not a known option of the `execSync` type used there); the COO's merge-time typecheck for the round-4 and round-5 drains ran `tsc --noEmit -p .`, whose root `tsconfig.json` checks no source file (it holds project references), so it printed rc=0 against an empty check; the correct instrument is `tsc -p tsconfig.app.json --noEmit` (or `tsc -b`), and the COO's drain checks use it from here on; (b) `rb-6-y1.border-sweep.test.ts` reads its list from the workspace tree, so run from the portal alone it fails three arms.

| cell | what it builds | serves | writes | risk | class |
|---|---|---|---|---|---|
| `RV-y-3` | the x5 test typechecks; the sweep list lives in a portal fixture and the y1 test reads it there; a new test holds both | FWD-3, FWD-5 | `src/__tests__/dsgn-rbndv2/` | LOCAL | worker-light (direct act, round-less, about 20 product lines) |

Gate limb that graded the addendum: none graded the modification (a direct-act order is round-less; the gate's limb for a newly added order checked the order's grammar, `<decomp_ref>` and preflight). Write set disjoint from `RV-y-2` (its own new test file in the same folder, a different file). The correction of the COO's earlier typecheck claim is stated in the round-6 close record.

