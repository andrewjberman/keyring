# FIND_INSURE.024 — Phase 2A v0.1 Ranked Target List (IR-team product)

**Author:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-29
**Source run:** `.024` LIVE-DISPATCH loop, run_date 2026-05-27, subset=intent24 (Option B `dabb2e106`), 24 IMOs, 52 Lusha credits, 0 hard-halt.
**Gold artifacts:** `s3://opal-data-imo/corp/{slug}/gold/linkedin-scrape/2026-05-27/{_company_scored,employees_scored}.json` (24/24 verified landed).
**Scorer:** `score_linkedin_gold` v0.1; weights v0.1.

This is the Phase-2A v0.1 deliverable: IMOs ranked by org-chart-derived asset-management-transition signal, with decision-relevant employees surfaced for the IR team.

## Ranked target list (by company_score_linkedin, desc)

| # | IMO | Company score | Leaders | Max emp | Mean top-5 | Series-lic leaders |
|---|-----|--------------:|--------:|--------:|-----------:|-------------------:|
| 1 | preferred-marketing-associates | 0.3905 | 50 | 0.575 | 0.515 | 0 |
| 2 | eagle-strategies | 0.375 | 25 | 0.575 | 0.4375 | 0 |
| 3 | integrity-marketing-group | 0.35025 | 25 | 0.5375 | 0.4075 | 0 |
| 4 | lincoln-investment | 0.32525 | 50 | 0.4875 | 0.4075 | 0 |
| 5 | allianz-life | 0.32325 | 50 | 0.4875 | 0.3975 | 0 |
| 6 | american-equity-investment-life-insurance-company | 0.32325 | 25 | 0.4875 | 0.3975 | 0 |
| 7 | metlife | 0.32325 | 25 | 0.4875 | 0.3975 | 0 |
| 8 | pacific-capital-resource-group | 0.32225 | 45 | 0.4875 | 0.3925 | 0 |
| 9 | avantax-wealth-management | 0.32075 | 50 | 0.4875 | 0.385 | 0 |
| 10 | senior-market-sales | 0.31975 | 25 | 0.4875 | 0.38 | 0 |
| 11 | midland-national | 0.31625 | 25 | 0.4875 | 0.3625 | 0 |
| 12 | the-retirement-network | 0.31325 | 8 | 0.4875 | 0.3475 | 0 |
| 13 | national-life-group | 0.31275 | 25 | 0.4875 | 0.345 | 0 |
| 14 | futurity-first | 0.2895 | 50 | 0.425 | 0.385 | 0 |
| 15 | american-general-life-insurance-company-aig | 0.2625 | 25 | 0.375 | 0.375 | 0 |
| 16 | nationwide-financial | 0.2625 | 25 | 0.375 | 0.375 | 0 |
| 17 | gradient-financial-group | 0.262 | 50 | 0.375 | 0.3725 | 0 |
| 18 | sterlingbridge-partners | 0.2565 | 18 | 0.375 | 0.345 | 0 |
| 19 | lifepro | 0.2555 | 25 | 0.375 | 0.34 | 0 |
| 20 | hansen-brokerage | 0.24625 | 4 | 0.375 | 0.29375 | 0 |
| 21 | u-s-marketing-corporation | 0.2415 | 6 | 0.375 | 0.27 | 0 |
| 22 | unkefer-associates | 0.23225 | 25 | 0.3375 | 0.3175 | 0 |
| 23 | forward-strategies-insurance-brokerage | 0.18825 | 5 | 0.2875 | 0.2225 | 0 |
| 24 | annuity-solutions | 0.0 | 0 | 0.0 | 0.0 | 0 |

## Top decision-relevant employees (top 6 IMOs)

**1. preferred-marketing-associates** — score 0.3905, 50 leaders
  - Audra Hartman Braski — Senior Vice President, Managing Director of Investment Services (c-suite, emp_score 0.575)
  - Charles Czachor — Senior Vice President, Investment Services, LGIP Investment Director (evp_svp, emp_score 0.537)
  - Jacob Correll — Vice President of Portfolio Management (vp_director, emp_score 0.487)

**2. eagle-strategies** — score 0.375, 25 leaders
  - Manuel Kakkanattu — Chief Information Officer, Vice President of Investments (c-suite, emp_score 0.575)
  - Abhijit Rai — Head of Technology Portfolio, Insurance and Annuities (vp_director, emp_score 0.487)
  - Deepa Soni — Executive Vice President and Chief Information Officer (c-suite, emp_score 0.375)

**3. integrity-marketing-group** — score 0.35025, 25 leaders
  - Christopher Cassidy — Senior Vice President of Wealth Management (evp_svp, emp_score 0.537)
  - Said Taiym — Chief Operating Officer (c-suite, emp_score 0.375)
  - Jose Alvarez — Chief Strategy Officer (c-suite, emp_score 0.375)

**4. lincoln-investment** — score 0.32525, 50 leaders
  - Chris Surrichio — Vice President of Investment Management and Research (vp_director, emp_score 0.487)
  - Rachelle Nelko — Designated Supervisor and Financial Advisor (manager, emp_score 0.425)
  - Robert Oliver — (Interim) Chief Information Officer (c-suite, emp_score 0.375)

**5. allianz-life** — score 0.32325, 50 leaders
  - Evan Powell — Principal Actuarial Analyst (vp_director, emp_score 0.487)
  - Jasmine Jirele — President and Chief Executive Officer (c-suite, emp_score 0.375)
  - Collin Bhojwani — Managing Director, Head of Allianz Life Ventures (c-suite, emp_score 0.375)

**6. american-equity-investment-life-insurance-company** — score 0.32325, 25 leaders
  - Andrew Rosenberg — Head of Investment Project Management and Strategy (vp_director, emp_score 0.487)
  - Alex Locke — Chief Product Officer (c-suite, emp_score 0.375)
  - Nicholas Volpe — Chief Technology Officer (c-suite, emp_score 0.375)

## Analytical notes (v0.1 scope-aware)

1. **Series-licensed-leaders = 0 across ALL 24 IMOs — EXPECTED, not a data gap.** PRD v0.7.2 NARROWED Lusha to org-chart-only (`/companies/search` + `/companies/enrich` + `/contacts/prospecting`); contact-reveal deferred to v0.7.3+ for credit conservation. Series-license detection requires contact-level reveal, which this tier does not pull. So the v0.1 ranking signal is driven by **title-keyword match + seniority class**, NOT Series-license. When contact-reveal lands (v0.7.3+), the `series_licensed_employee_count` dimension activates and will re-rank.
2. **Score compression (0.19–0.39 band).** With Series-license dimension dormant, the discriminator is title/seniority. The ranking is still meaningful — top IMOs (PMA, eagle-strategies, integrity) surface genuine investment-services / CIO / wealth-management leadership; the tail (forward-strategies 0.19, annuity-solutions 0.0) are sparse-org / no-match.
3. **`annuity-solutions` = no_company_match** (Lusha had no company record for `annuitysolutions.com`); 0 credits, 0-score gold artifact written for completeness. Candidate for domain-correction re-run if IR wants it covered.
4. **Leadership depth varies** (4–50): cap-tiering worked — `present` IMOs got cap50 deeper baskets, `adjacent` cap25. The leadership_count is the org-chart bench depth at page 0 (free), independent of prospecting cap.

## Provenance
- Machine-readable: `ranked_target_list.json` (24 IMOs, full top-3-employee detail per IMO) generated this cycle from the 48 verified S3 gold artifacts.
- Next leg (COO routing to CTO): Phase 3 consolidation into IR-team-facing serving tables, OR full-universe expansion. This v0.1 list is the 24-IMO Option-B scope deliverable.
