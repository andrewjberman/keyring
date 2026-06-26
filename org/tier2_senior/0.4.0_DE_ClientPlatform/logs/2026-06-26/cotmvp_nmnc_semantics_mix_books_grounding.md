# ADVI_COTMVP — NMNC semantics grounding + Mix/Books expansion grounded to one DS root

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE
**agent:** 0.4.0_DE_ClientPlatform | **date:** 2026-06-26 | **window:** ~2030Z → ~2213Z (since prior log aada953d1)

## Summary

Andrew-driven analytical + scope-expansion window. Three threads, all grounded to source/served (Rule 22): (1) explained the COT AUA New/Existing-client bar semantics (Andrew probed, then accepted); (2) Andrew expanded COTMVP with two items — fix the empty "Mix" asset-type breakdown + realize /Books — both grounded to ONE producer root and DS-shipped; (3) the /Books realization shape settled (purpose-built mount), CTO-gated. **No DE commits this window** — it was diagnosis + coordination; the resulting fix is DS's `d3e479759`.

## Thread 1 — COT AUA New/Existing-client semantics (DIAGNOSE, source-confirmed)

Andrew flagged that monthly Assets Overview shows May 214m-new/4m-existing, June 30m-new/371m-existing — prior period not rolling forward as he'd expect. Grounded to producer source `data/cot/scripts/gold/D_00b.portal_timeseries.py:581-602` (`_build_static_aua_periods._periods_monthly`): for each month it partitions the **period-END AUA snapshot** by each client's `first_seen` cohort — NMNC = period-end balance of clients first-seen *in* that month, NMEC = period-end balance of everyone first-seen *earlier*. So June NMEC(371m) ≠ May total(218m) because May-onboarded clients kept funding through June (218m→~341m) and under a cohort partition that continued funding lands in "existing." It's a cohort-membership stock split, not a flow rollforward. Andrew initially reframed it as an NNA-concept-on-AUA category error, then concluded "this logic actually does make sense, disregard my comments." **Outcome: no change; the NMNC/NMEC split is faithful + intended. D3 clarifier stands.**

## Thread 2 — Mix asset-type breakdown + Books composition (DIAGNOSE → DS fix shipped)

Andrew: fix the empty "Mix" (Cash/FI/Equities/Alts) stacked-bars toggle + realize /Books. Grounded both to **one root**:
- **FE correctly wired both sides** (Mix reads `timeseries_overview.mix[gran]`={} empty; Books composition reads `mix_summary.composition`=null). The gap is producer.
- My initial chain pointed at C_06 `firm_daily` empty. **DS corrected it against live artifacts** (the grounding discipline catching an off-by-one): C_06 is fine (mix_daily_summary.firm = 58d populated). REAL root: **cot `D_03.composition_artifacts.main:576-579` hard-exits (`return 1`) on absent `holdings_lots`** — and cot holdings_lots is empty BY DESIGN (snapshot-first BD-native, no FIFO lots; canonical/holdings has the data). So D_03 dies every nightly before both `firm_composition.json` AND `_publish_mix_views` → all D_03 outputs NoSuchKey → both FE features starve.
- **DS FIX SHIPPED: `d3e479759`** (re-source cot D_03 from canonical/holdings), deployed to cot S3. One fix produces `firm_mix_views.json` (→ D_04 `timeseries_overview.mix` + `mix_summary.mix_periods` → Mix toggle + Books quarterlyMix) AND `firm_composition.json` (→ `mix_summary.composition` → Books composition donut). Producer-populated, full parity, **no FE change**.
- **Composition-source decision (COO delegated to me+DS):** producer-populate (parity over per-tenant FE divergence — consistent with the session's no-divergence stance); DS confirmed it's the same cheap fix, so FE-fallback plan-B is DROPPED.
- Non-blocker noted: per-client composition (`clients/{id}_composition.json`) still empty for cot, but COT's firm-only Books doesn't use it.

## Thread 3 — /Books realization shape (COORDINATE, CTO-gated)

Carry-forward from prior window: B's realization is a **purpose-built `CanonicalBookView level="n1"` direct mount** in cottonwood/index.tsx (panels-only, bypassing the advisor-centric shared BooksTab whose advisor-chrome leak I found un-suppressable). COO concurred + routed to CTO for fix-shape ack. Overview/tax flow from the prior-window DS `clients_tab` envelope (`0ba4f4e8e`); composition now flows from `d3e479759`. Build on CTO ack.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| (none run this window) | — | — | DIAGNOSE/COORDINATE window — no code/infra change by me. Grounding was source Read/Grep on producer gold scripts (D_00b/D_03/D_04/C_06) + served-artifact JSON inspection of COT platinum mocks; the producer fix is DS's lane (d3e479759, ds-commit-gate on their side). My prior-window comp-tool guardrails (schema-check/ternary-audit on D2/D3) already logged at aada953d1. |

**What worked:** source-grounding the NMNC mechanism + the Mix/Books lineage to exact file:line prevented inventing a fix; DS's live-artifact correction of my C_06 chain is the grounding discipline paying off (off-by-one caught before anyone coded the wrong fix). **Gap:** none new.

## MCP traffic

~14 messages (heavy DS/COO coordination). Significant: routed the mix producer gap to DS (grounded chain); DS corrected-diagnosis (D_03 holdings_lots, not C_06) + shipped d3e479759; made the composition-source call (producer-populate); COO ACK'd the expansion grounding + re-engaged DS as priority; COO concur on the purpose-built-N1 Books mount (CTO-routed). CVO D2+D3 RAVC-closes (prior window, already actioned).

## Blockers

- **Mix toggle + Books composition:** evidence-cited gated on **tonight's scheduled cot nightly** carrying DS's `d3e479759` D_03 outputs (NEVER#4 — no ad-hoc gold run; the artifacts only exist post-nightly). Not assumption — the producer fix is deployed but unrendered until the nightly runs.
- **Books N1 mount build:** gated on **[1.0.0_SA_CTO]** fix-shape ack (purpose-built-N1 vs continue-BooksTab-suppression; COO+I recommend N1).

## Current State

- **D2 + D3:** shipped + CVO-verified + closed (portal `f071b6b1`/`42c11d41`; verdicts `447de47ca`/`6d6149506`).
- **Mix toggle (item 1) + Books composition:** DS-fixed (`d3e479759` deployed), renders on tonight's cot nightly. FE already correct — my only owed work is post-nightly browser-verification. timeseries_overview.mix + mix_summary.{mix_periods,composition} will populate from the new D_03 outputs.
- **Books N1 mount (item 2):** shape settled (purpose-built CanonicalBookView level="n1" in cottonwood/index.tsx), CTO-ack-gated; overview/tax from `0ba4f4e8e`, composition from `d3e479759`. v1/v2 WIP patches saved at scratchpad/ADVI_COTMVP_B_firm_books_WIP*.patch (BooksTab-reuse attempts, reference only — the N1 mount is a fresh build on ack).
- Local repro rig retained (portal/public/__mockcot/); dev server may be up. Data-shape finding banked: memory/reference_cot_firm_book_data_shape_divergence.md.

## Next Steps

- **[0.4.0_DE, me]** post-nightly: browser-verify Mix toggle (Cash/FI/Equities/Alts stacked bars, ~2-3 young-firm period bars) + Books composition donut (reconciles to firm totals) on the served artifact → RAVC COO. On CTO ack: build the purpose-built Books N1 mount + verify + RAVC CVO.
- **[1.0.0_SA_CTO]** ack the Books N1 mount fix-shape (purpose-built-N1 recommended) — gates my build.
- **[0.4.0_DS]** d3e479759 validates on the cot nightly; implicit ping to me on land. (Per-client composition is a clean follow-up if a client-drill panel ever needs it — not in COTMVP scope.)
- Background gates unchanged: NFRA_TSGRAPH P2-1 (AE P2-2); INFMVP.F5-retire (Andrew F5-vs-Cottonwood sovereign).
