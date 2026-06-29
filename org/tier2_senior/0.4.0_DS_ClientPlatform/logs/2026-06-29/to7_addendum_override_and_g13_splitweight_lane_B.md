# Session Log (delta) — 0.4.0_DS_ClientPlatform~B — TO-7 addendum: override layer + G13 split-weighting

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE (CTO arch-gate, CVO formula, base-DS co-own), VALIDATE
**serial:** 0.4.0_DS_ClientPlatform~B · **date:** 2026-06-29 · **window:** since to7_dim_enrichment log (1544Z) -> 1602Z

## Summary

TO-7 addendum (Andrew chose BD-base + thin curated override for splits) + the G13 Wave-2 parity step, both COMPLETE:
- Candidate worksheet for Andrew — commit `9df40ac04`.
- Curated split-override mechanism (CTO arch-gated) + G13 split-weighted leaderboard — commit `04d295bd8`.

## Curated split-override layer (IMPLEMENT, CTO arch-gated)

COO amend: gate the MECHANISM on CTO's shape arch-gate; worksheet proceeds in parallel.
- Sent CTO the shape (precedence/provenance/Andrew-artifact); CTO GO + 3 refinements, ALL honored:
  - R1 PER-ROLE provenance: `{role}_split_source` per split-model role (dim is wide -> per-row was insufficient).
  - R2 FAIL-LOUD validation: rejects (loud+logged) bad role / split not in [0,100] / account-not-in-dim / post-override account split-sum not ~100 (+/-5). Tested vs 4 deliberately-malformed rows -> all rejected, 0 applied.
  - R3 enrichment coupling: no-op+log on roles the dim lacks (dim has all 5 via TO-7).
- Store: `data/canonical/schwab/config/advisor_split_overrides.csv` (git-tracked = audited; empty = clean no-op) + README. Worksheet generator = `build_dim_advisor_role.py --worksheet`.
- Worksheet deliverable: 1364 accounts / 2178 rows / $433.6M candidate AUA, ranked, blank corrected_* cols for Andrew.

## G13 split-weighted leaderboard (IMPLEMENT)

CVO grounded the formula from source (D_00c.portal_leaderboard.py:876-927 = Andrew's 3-case NORMALIZED rule). Rebuilt G13 (schema 2.0) = advisor-grain credited leaderboard:
- fee_paying(role)=billable AND split_pct>0; Case1/Case3 proportional among fee-paying, Case2/fallback equal split. credited_aua=account_aua*weight.
- account_billable bridged BD->Schwab (fee gate).
- 158 advisors; CONSERVATION sharp-check PASS: sum(credited_aua)=total account AUA, **drift $0.00**.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-pipescript io | build_dim_advisor_role.py | N/A (expected) | NOT-FOUND -- canonical not graph-indexed (documented); mandate attempted |
| ds-commit-gate | dim + G13 (several passes) | PASS | caught F841/E702 ruff on the override loop -> fixed |
| ruff | build_dim_advisor_role.py | PASS (after fix) | unused var + semicolons cleaned |
| (read-only boto3) | worksheet AUA-enrich, fail-loud test, account_billable bridge | PASS | live-S3 grounding |

- **What worked:** the fail-loud validation caught all 4 malformed test rows; G13 conservation came out exact ($0.00 drift) first try.
- **What failed:** initial WORKSHEET_PATH had one too few `..` (landed in data/docs/) -> fixed to 4.
- **Gap found:** none new.

## Blockers

None. (CVO parity-test of G13 vs BD-served D_00c is pending — a verification handoff, not a blocker.)

## Current State

Wave-2 advisor-parity SUBSTRATE complete: enriched dim (TO-7) + curated-override layer (CTO-gated, empty/no-op until Andrew fills) + split-weighted G13 (D_00c parity). Served at canonical/schwab/{silver/dim_advisor_role, gold/advisor_attribution, gold/partner_analytics}/[asof|date]=2026-06-24. Override store + worksheet committed. Commits this window: 9df40ac04 (worksheet), 04d295bd8 (mechanism+G13). All pushed CLOUD. Registered LIVE, IDLE.

## Next Steps

- **[3.0.0_SA_CVO]** parity-test G13 (canonical/schwab/gold/partner_analytics) vs the BD-served D_00c leaderboard -> Wave-2 advisor parity verdict.
- **[Andrew, via COO]** populate the override worksheet (corrected splits) -> paste into advisor_split_overrides.csv -> next dim build flips those to curated-override.
- **[0.4.0_DS_ClientPlatform]** (base) co-own review of the override-mechanism diff (04d295bd8); G11-G13 daily-wiring is base-DS lane (D4 cadence open).
- **[2.0.0_SA_COO]** next dispatch (PFMG_TAXSMA S0 resumable) once Wave-2 parity loop closes.
