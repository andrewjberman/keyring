# FIND_INSURE.024 — FINRA-Enriched Ranked Target List (IR-team product, (b)-depth)

**Author:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-29 (FINRA-enriched revision — supersedes the pre-FINRA v1 snapshot)
**Source:** `.024` Option-B universe (24 IMOs), org-chart-scored + **FREE FINRA BrokerCheck series-license enrichment** (Andrew sovereign 2026-05-29; chain-event wired bronze→silver→gold, commit 7453d085c; full-24 backfill 0 Lusha credits).
**Machine product:** `s3://opal-data-imo/serving/contacts-target-2026-05-27.json` + per-IMO `corp/{slug}/gold/linkedin-scrape/2026-05-27/`.

The series-license dimension (previously dormant — Lusha carries no license data) is now ACTIVE via FINRA BrokerCheck. This fundamentally re-ranks the universe: IMOs with FINRA-registered securities/advisory reps (the asset-management-transition signal) separate cleanly from annuity-only marketers.

## Ranked target list (FINRA-enriched company_score_linkedin, desc)

| # | IMO | Score | Series-licensed | Top licensed reps (CRD) |
|---|---|--:|--:|---|
| 1 | preferred-marketing-associates | 0.858 | 29 | Brett Weeden (S24/S63/S65/S7, CRD 4913375); Audra Hartman Braski (S24/S63/S7, CRD 4741233); Caleb Walter (S6/S63/S65/S7, CRD 6551405) |
| 2 | lincoln-investment | 0.793 | 26 | Nancy Heffner (S24/S6/S63/S65/S7, CRD 1484471); Chris Surrichio (S24/S6/S7, CRD 2473601); Christina Charbonneau (S24/S51/S6/S63/S66/S7, CRD 2197821) |
| 3 | integrity-marketing-group | 0.630 | 3 | Christopher Cassidy (S24/S66/S7, CRD 5206879); Michelle Stockman (S24/S53/S6/S66/S7, CRD 5010490); Tom Dempsey (S24/S6/S63/S65/S7, CRD 4063929) |
| 4 | gradient-financial-group | 0.563 | 6 | Jon Vanorden (S66/S7, CRD 5270047); Nicole Alexander (S65, CRD 4249833); Leo Carton (S6/S63/S65/S7, CRD 1289027) |
| 5 | allianz-life | 0.466 | 4 | Jasmine Jirele (S24/S26/S6, CRD 4180840); Michael Brazys (S24/S7, CRD 5223949); Gordon Collins (S26/S63/S7, CRD 4691983) |
| 6 | american-equity-life | 0.387 | 1 | Mark Mullings (S24/S26/S6/S63/S7, CRD 3272512) |
| 7 | eagle-strategies | 0.375 | 0 | — |
| 8 | futurity-first | 0.361 | 1 | Curtis Carey (S66/S7, CRD 5723594) |
| 9 | midland-national | 0.348 | 1 | Spencer Halgerson (S6/S63, CRD 6846771) |
| 10 | metlife | 0.323 | 0 | — |
| 11 | pacific-capital-resource-group | 0.322 | 0 | — |
| 12 | avantax-wealth-management | 0.321 | 0 | — |
| 13 | senior-market-sales | 0.320 | 0 | — |
| 14 | the-retirement-network | 0.313 | 0 | — |
| 15 | national-life-group | 0.313 | 0 | — |
| 16 | nationwide-financial | 0.293 | 1 | — |
| 17 | american-general-life-aig | 0.263 | 0 | — |
| 18 | sterlingbridge-partners | 0.257 | 0 | — |
| 19 | lifepro | 0.256 | 0 | — |
| 20 | hansen-brokerage | 0.246 | 0 | — |
| 21 | u-s-marketing-corporation | 0.242 | 0 | — |
| 22 | unkefer-associates | 0.232 | 0 | — |
| 23 | forward-strategies-insurance-brokerage | 0.219 | 1 | — |
| 24 | annuity-solutions | 0.000 | 0 | — (Lusha no_company_match) |

## What changed vs the pre-FINRA v1

The v1 ranking compressed everything into 0.19–0.39 (title/seniority only). FINRA series-license activation decompressed it: the top 2 (PMA 0.86, lincoln-investment 0.79) are now clearly separated — both are broker-dealer/RIA-affiliated IMOs with 26–29 registered, Series-licensed reps (a strong asset-management-transition signal). The pure annuity/insurance-marketing tail (lifepro, aig, unkefer, hansen) stays ~0.25 with 0 licensed reps.

## Enrichment provenance + honesty (per-company `finra_enrichment.disposition_breakdown`)

Three dispositions, surfaced so a 0-license firm reads correctly:
- **enriched_with_license** — firm+name matched in BrokerCheck WITH Series licenses (the signal).
- **no_finra_record** — matched-name not in BrokerCheck = genuinely non-registered (e.g. tech/IT execs) = a TRUE negative, not missing data.
- **no_firm_match_recall_miss** — name found but the BrokerCheck firm didn't match the IMO name. This is the **IMO-marketing-name vs registered-BD-name gap** (a rep at an IMO often registers through a separate broker-dealer). v1 is precision-first (Andrew rule: company + name must BOTH match); the **v2 firm_aliases IMO→affiliated-BD map** will close this tail and likely lift several mid-table firms.

## Method

- Source: `api.brokercheck.finra.org` (public, no-auth, JSON; zero credit cost).
- Per pulled person: `/search/individual?query={name}` → firm-match on `ind_current_employments[].firm_name` → CRD → `/search/individual/{CRD}` → state/product/principal exam categories.
- Match rule (Andrew 2026-05-29): company + name BOTH match, else not counted.
- Full-24 enrichment: 661 contacts, 76 firm+name matched, 73 series-licensed, **0 Lusha credits** (in-place backfill over existing .024 bronze).
