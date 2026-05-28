# work_1654Z — FIND_INSURE.024 pagination fix (Andrew-flagged): page-loop + bench-depth total, canary-GREEN

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, VALIDATE

**Agent:** 0.1.0_DS_MarketIntelligence~C — /work tick on CVO Andrew-flagged finding @c7e018619 (+ COO DRIVE)

## Headline
My v3 contacts_prospecting reconstruction had dropped pagination → the .024 run captured page-1-only per company (≤25, the per_imo cap) + discarded the available-total. Fixed: page-loop + capture pagination.total (the leadership-bench-depth indicator Andrew wants). Canary-GREEN. 24-rerun gated on COO's basket-cap # (per-result billing makes full-roster prohibitive).

## Fix
- lusha_client.contacts_prospecting: wire {"pagination":{"page","size"}} into the body (empirically the v3 shape — top-level page/size/pages/limit all 400-rejected). The page/page_size params were previously dead.
- crawl_linkedin_bronze: prospecting is now a page-LOOP — accumulate until basket_cap / short-page (last) / available-total. Captures pagination.total → result.leadership_contacts_available + prospect_pages_fetched. DEFAULT prospect_basket_cap=25 (= prior behavior, no unauthorized spend; total still captured) — deeper basket is an explicit event opt-in.

## Billing finding (CVO open-Q answered)
Prospecting is PER-RESULT (~1 credit / 25 results; canary 25→1, earlier 40→2). So the TOTAL (Andrew's bench-depth want) is FREE on page 0; a deeper BASKET is per-result-expensive — allianz total=3404 ⇒ full roster ~136 credits/co ⇒ thousands across 24 = prohibitive. Recommended COO a modest cap (50) since the curated list is top-5/co (re-ranked by employee_score × am_domain, not Lusha order).

## Canary-1 (allianz-life, default cap)
page-loop OK (1 page, cap respected), **leadership_contacts_available=3404 captured**, 2 credits. Bronze 60/60, self-test 6/6, client 14/14, ds-commit-gate clean.

## Commit
863532171 (lusha_client + bronze + test).

## Gated
24-IMO rerun + deeper-basket cap GATED on COO's cap # (raise prospect_basket_cap + cost-gate ceiling together) — BLOCKED-ASK 165406Z with the cost math. Then rerun + re-emit Deliverable-6 → CVO re-verify. Minor (deferred): crawl_linkedin_bronze is a misnomer (API not crawl).

## Compiler Tools
None — external-API pagination/billing investigation + bronze page-loop; gold-only re-score path, no SSM.

## Discipline
- canary-first (COO + stub-fixtures-encode-false-premise discipline): single-IMO real-API validation before the 24 rerun; billing empirically confirmed not assumed.
- Rule 15 (__future__ first) intact; ds-commit-gate + safe-commit. Default cap = no unauthorized spend; deeper rerun gated on COO cap.

— 0.1.0_DS_MarketIntelligence~C 2026-05-28T1654Z [work-cycle:0007]
