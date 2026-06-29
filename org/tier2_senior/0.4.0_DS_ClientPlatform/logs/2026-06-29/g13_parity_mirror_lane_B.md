# Session Log (delta) — 0.4.0_DS_ClientPlatform~B — G13 parity self-diff + mirror rebuild

**archetype:** VALIDATE
**secondary_archetypes:** TRACE (D_00c branch-trace), IMPLEMENT (mirror rebuild), COORDINATE (CVO TO-4 contract)
**serial:** 0.4.0_DS_ClientPlatform~B · **date:** 2026-06-29 · **window:** since to7_addendum log (1602Z) -> 1616Z

## Summary

Took COO next-pick (a): support CVO's Wave-2 G13-vs-BD-served parity. Proactively self-diffed, branch-traced the served semantics, CVO set the contract, rebuilt G13 to the field-for-field mirror. Commit `4af4f2029`.

## What happened

1. SELF-DIFF (F5, verify my own deliverable vs served): my G13 credited_aua ($174M Travis) vs BD-served total_aua ($355M) = ~2-4x gap across top advisors. Found BD total_aua sum = $5.31B (~3.3x firm) = RAW per-role over-credit; the 3-case split lives in fee_breakdown, NOT total_aua.
2. BRANCH-TRACE (Rule-22 mechanism, closed CVO's caveat): D_00c L590 served total_aua = tagged_aua = (tagged_aua_counts).get(advisor) or row.total_aua; tagged_aua_counts built raw-per-role at L865 (melted_dedup_acct groupby advisor sum total_aua). Split path (L935 _compute_split_weight) feeds fee_breakdown only.
3. CVO TO-4 CONTRACT CALL: (a) field-for-field MIRROR (cutover never-widen -> portal must render identically incl. the deliberate over-credit). NOT Class-C divergence.
4. REBUILT G13 to mirror: raw total_aua (headline) + role_breakdown (per-role raw aua/nna/counts + fee split) + fee_breakdown (3-case split = fee_paying.aua, conserved) + ranks. Sharp checks: fee_paying conserves $1.591B drift $0.00; role_breakdown ties total_aua drift $0.00. Travis canonical total_aua $348.0M vs BD $355.5M (~98%, residual = book-scope held-away).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| (read-only boto3) | BD employee_leaderboard.json structure + sum(total_aua) + role_breakdown | PASS | served-artifact grounding (F5); characterized raw vs split |
| Grep/Read | D_00c.portal_leaderboard.py tagged_aua branch-trace | PASS | L590/865/935/1077 -- mechanism grounded (Rule-22) |
| ds-commit-gate | build_gold_partner_analytics.py | PASS | py_compile+AST+ruff clean |

- **What worked:** verifying my own G13 vs the served artifact caught a fundamental target mismatch BEFORE CVO's harness; the branch-trace closed CVO's not-branch-traced caveat.
- **What failed:** my first G13 was built to the split quantity (conserved) when the served HEADLINE is raw-over-credit -> rebuilt to carry both.
- **Gap found:** none new.

## Blockers

None. (CVO field-for-field parity verdict pending — verification handoff.)

## Current State

G13 = served-leaderboard mirror, served canonical/schwab/gold/partner_analytics/date=2026-06-24 (commit 4af4f2029): total_aua (raw, sum $4.96B/3.12x), fee_paying_aua (split, $1.591B/$0.00 drift), role_breakdown JSON (ties total_aua $0.00), ranks. 158 advisors. The full Wave-2 advisor-parity substrate is now complete: enriched dim + curated-override layer + worksheet + split-weighted + mirror G13. Registered LIVE, IDLE.

## Next Steps

- **[3.0.0_SA_CVO]** field-for-field parity verify of G13 vs BD-served (netting BD to the Schwab/Class-D subset) -> Wave-2 leaderboard parity verdict.
- **[Andrew, via COO]** populate the override worksheet -> curated splits flow to fee_paying via the next dim build.
- **[2.0.0_SA_COO]** next dispatch (PFMG_TAXSMA S0) once Wave-2 parity verdict lands.
