# FIND_INSURE Phase 1 (web-scrape) — 99-IMO Universe-Run Completion Matrix

**Run date:** 2026-05-27 (pinned; the wall-clock default 2026-05-28 is an empty partition)
**TO:** FIND_INSURE.008 (AC7 inventory + AC9 telemetry + completion-matrix)
**Author:** 0.7.0_AE_CloudOps~A
**Generated:** 2026-05-28
**Phase 1 close commit:** d2033738c (CTO+COO joint RAVC2-Accept)
**Status:** post-close finalization (non-gating; Phase 1 already CLOSED)
**Machine artifact:** `s3://opal-data-imo/qa/stage2-universe-2026-05-27.json` (AC9 / AC-T1 deliverable; full per-IMO table)
**Taxonomy:** v3 | **Scoring weights:** v0.3 (both confirmed against deployed Lambda env + landed gold provenance)

## Coverage (AC7)

All **99** source-list IMOs (`serving/_meta/source-list-2026-05-27.json`) have a complete
bronze -> silver -> gold chain at run_date=2026-05-27. Verified by S3 inventory:

| Tier | Slugs at 2026-05-27 | Result |
|---|---|---|
| bronze/web-scrape (meta) | 99/99 | PASS |
| silver/web-scrape | 99/99 | PASS |
| gold/web-scrape/score.json | 99/99 | PASS |

- `(source-list slugs) - (gold slugs) = {}` (empty) -> 99/99 coverage, no gap.
- One extra gold slug (`carl-ostenson`) is a **legacy-slug alias** of the canonical
  `carl-ostenson-associates` (an old-taxonomy v1 pre-crawl seed); it is excluded from the
  canonical 99-universe accounting. Total physical gold slugs = 100 (99 canonical + 1 alias).

## Effective yield (AC9)

| Outcome | Count | Pct of 99 |
|---|---|---|
| **SCORED** (usable content, scorable) | 47 | 47.5% |
| **BLOCKED_UPSTREAM** | 52 | 52.5% |

Reconciliation: 47 + 52 = 99. Matches Phase 1 close note (d2033738c): "47/99 effective yield,
52 blocked_upstream = honest absent-data tail, not defect."

### Blocked-tail sub-classification (from bronze http_status)

| Sub-class | Count | Meaning |
|---|---|---|
| BLOCKED_HARD | 19 | Upstream fetch failed; `http_status: null`, no body retrieved |
| BLOCKED_SOFT | 33 | HTTP 200 returned but body was anti-bot interstitial / stub (gold detected no scorable content) |

The gold layer collapses both into `score_class=BLOCKED_UPSTREAM` (`wm_classification_reason=blocked_upstream`,
`page_count_scanned=1, matches=0, rollup=0`).

## Scoring distribution (the 47 SCORED IMOs)

| wm_classification | Count | Definition |
|---|---|---|
| **present** | 7 | Direct annuity/AM relationship prominent on site |
| **adjacent** | 17 | AM/annuity terms present but not the prominent positioning |
| **absent** | 23 | Pages scored but no AM-relationship signal (rollup=0) |

### present (7)

| slug | rollup | am_prominence | pages (scanned/match) | terms |
|---|---|---|---|---|
| avantax-wealth-management | 100 | 1.0 | 5/5 | 171 |
| lincoln-investment | 100 | 0.9415 | 25/24 | 341 |
| pacific-capital-resource-group | 100 | 1.0 | 44/44 | 542 |
| preferred-marketing-associates | 100 | 1.0 | 67/27 | 346 |
| futurity-first | 76 | 1.0 | 74/72 | 194 |
| the-retirement-network | 63 | 0.9798 | 17/17 | 103 |
| gradient-financial-group | 42 | 0.682 | 18/16 | 166 |

### adjacent (17)

Highest-to-lowest rollup: allianz-life (100), eagle-strategies (100), senior-market-sales (100),
national-life-group (86), midland-national (85), metlife (66), integrity-marketing-group (56),
forward-strategies-insurance-brokerage (49), nationwide-financial (37),
american-general-life-insurance-company-aig (35), lifepro (23),
american-equity-investment-life-insurance-company (20), u-s-marketing-corporation (18),
unkefer-associates (10), sterlingbridge-partners (7), hansen-brokerage (6), annuity-solutions (3).

The `am_prominence` dual-bar (v0.7.3) correctly separates present (high am_prominence, e.g. 1.0)
from adjacent (low am_prominence with high term volume, e.g. allianz-life am_prom=0.0117 on 2095 terms):
high raw term count without prominent positioning resolves to adjacent, not a false-present.

### absent (23)

1st-atlantic-insurance-group, agent-pipeline, atlantic-capital-group, beacon-strategies,
benefits-america, brokerage-plus, brokers-international, david-j-baum-associates, efpr-group,
fig-marketing, financial-independence-group, gordon-marketing, ideal-producers-group,
imperial-marketing, insurance-pro-marketing, insurance-solutions-group, interwest-insurance-services,
lga-global, locorr, national-insurance-marketing-corporation-nimc, pacific-advisory-group,
safe-harbor-financial, safe-money-resource.

## Null-accounting (the 52 blocked_upstream tail)

These IMOs produced gold artifacts (so coverage = 99/99) but carry a null AM verdict
(`wm_classification=null`) because no scorable content was retrievable.

**BLOCKED_HARD (19):** advisors-excel, annuity-fyi, baymark-insurance-partners, d-a-davidson-co,
fallon-financial-group, financial-security-associates, keystone-partners, liberty-bankers,
lincoln-financial-group, m3-insurance, pensionquote, premier-insurance-partners, redbird-agents,
ritter-insurance-marketing, schaefer-financial-group, shields-brokerage, simplicity-group,
trust-point, universal-producers-group.

**BLOCKED_SOFT (33):** aspida-associates, bmis-burton-marketing-insurance-services,
brant-phillips-agency, cambridge-investment-research, carl-ostenson-associates, ceritas-financial,
ces-consultants-in-estate-services, cfg-financial-group, cls-partners, concord-insurance-brokerage,
connect2advisory, crump-group, developers-marketing-corporation, echo-annuity, elco-financial-group,
highland-capital-brokerage, indexed-annuity-solutions, insurance-marketing-organization-imo,
j-p-farrell-corporation, marketpro-direct, mastermind-imo, mga-america, middleoak,
national-marketing-group, northstar-financial, osj-services, pacific-premier-group,
pas-producer-advisory-services, provision-brokerage, structured-asset-management,
the-preferred-annuity-group, truadvice-partners, v2-financial-marketing.

## AC8 — empty-body / blocked-rate gate

- Blocked-upstream rate = 52/99 = **52.5%**, exceeding the PRD AC-T2 threshold (5-10%).
- **Adjudication (eyes-open at Phase 1 close):** NOT a defect. These IMOs are genuinely
  anti-bot-protected insurance sites or have no AM-relationship web presence. Already accepted
  in the d2033738c close note as "honest absent-data tail."
- **Escape valve available:** `scraping_browser1` v0.3.0 source pre-built by AE 0.7~B at `40b18d724`.
  Reserved for Phase 2A re-probe of the tail if Andrew's Q1 subset-cut (top-quintile +
  Series-license mention) includes any blocked IMOs. Not a Phase 1 blocker.

## AC10 — deploy / IAM confirmation

- `find-insure-crawl-web` / `find-insure-parse-web` / `find-insure-score-web`: all deployed
  (LastModified 2026-05-28T05:48Z), runtime python3.9, role `find-insure-lambda-role`.
- `find-insure-score-web` env: `FIND_INSURE_TAXONOMY_VERSION=v3`, `FIND_INSURE_SCORING_WEIGHTS_VERSION=v0.3`
  — confirms the v1-leftover env-pin near-miss was fixed and the landed gold scores reflect v3/v0.3.
- `s3:PutObject` scope: empirically proven sufficient (99/99 bronze+silver+gold prefixes written).
- `comp-iam gaps`: No permission gaps detected (134 services, 74 roles scanned).
