# FIND_INSURE.024 — FINRA-Enriched Ranked Target List (IR-team product, (b)-depth)

**Author:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-29; **revised 2026-06-01** (PMA reclassified off the #1 slot — see revision note below)
**Source:** `.024` Option-B universe (23 insurance IMOs + 1 reclassified adjacent-WM record), org-chart-scored + **FREE FINRA BrokerCheck series-license enrichment** (Andrew sovereign 2026-05-29; chain-event wired bronze→silver→gold, commit 7453d085c; full-24 backfill 0 Lusha credits).
**Machine product:** `s3://opal-data-imo/serving/contacts-target-2026-05-27.json` + per-IMO `corp/{slug}/gold/linkedin-scrape/2026-05-27/`.

The series-license dimension (previously dormant — Lusha carries no license data) is now ACTIVE via FINRA BrokerCheck. This fundamentally re-ranks the universe: IMOs with FINRA-registered securities/advisory reps (the asset-management-transition signal) separate cleanly from annuity-only marketers.

> **REVISION 2026-06-01 (DS~C):** `preferred-marketing-associates` has been MOVED OFF the #1 insurance-IMO slot. A provenance trace confirmed the slug resolved (via an upstream source-list #79 wrong-domain pairing) to **PMA Financial Network** — a municipal/public-sector RIA/BD at pmanetwork.com, NOT the insurance IMO it was named for. Per CTO ruling 162518Z + COO off-slot GO, it is reclassified OUT of the insurance-IMO universe and preserved separately below (data + score intact; it is the legit Prudent Man Advisors $6.19B deep-drill). The insurance-IMO ranked list below is now **23 IMOs, lincoln-investment at #1**. (Universe-DEFINITION question — whether FIND_INSURE formally expands to adjacent WM/AM targets — is with Andrew; this revision implements the binding off-slot data-correctness fix either way.)

## Ranked target list — insurance-IMO universe (FINRA-enriched company_score_linkedin, desc)

| # | IMO | Score | Series-licensed | Top licensed reps (CRD) |
|---|---|--:|--:|---|
| 1 | lincoln-investment | 0.793 | 26 | Nancy Heffner (S24/S6/S63/S65/S7, CRD 1484471); Chris Surrichio (S24/S6/S7, CRD 2473601); Christina Charbonneau (S24/S51/S6/S63/S66/S7, CRD 2197821) |
| 2 | integrity-marketing-group | 0.630 | 3 | Christopher Cassidy (S24/S66/S7, CRD 5206879); Michelle Stockman (S24/S53/S6/S66/S7, CRD 5010490); Tom Dempsey (S24/S6/S63/S65/S7, CRD 4063929) |
| 3 | gradient-financial-group | 0.563 | 6 | Jon Vanorden (S66/S7, CRD 5270047); Nicole Alexander (S65, CRD 4249833); Leo Carton (S6/S63/S65/S7, CRD 1289027) |
| 4 | allianz-life | 0.466 | 4 | Jasmine Jirele (S24/S26/S6, CRD 4180840); Michael Brazys (S24/S7, CRD 5223949); Gordon Collins (S26/S63/S7, CRD 4691983) |
| 5 | american-equity-life | 0.387 | 1 | Mark Mullings (S24/S26/S6/S63/S7, CRD 3272512) |
| 6 | eagle-strategies | 0.375 | 0 | — |
| 7 | futurity-first | 0.361 | 1 | Curtis Carey (S66/S7, CRD 5723594) |
| 8 | midland-national | 0.348 | 1 | Spencer Halgerson (S6/S63, CRD 6846771) |
| 9 | metlife | 0.323 | 0 | — |
| 10 | pacific-capital-resource-group | 0.322 | 0 | — |
| 11 | avantax-wealth-management | 0.321 | 0 | — |
| 12 | senior-market-sales | 0.320 | 0 | — |
| 13 | the-retirement-network | 0.313 | 0 | — |
| 14 | national-life-group | 0.313 | 0 | — |
| 15 | nationwide-financial | 0.293 | 1 | — |
| 16 | american-general-life-aig | 0.263 | 0 | — |
| 17 | sterlingbridge-partners | 0.257 | 0 | — |
| 18 | lifepro | 0.256 | 0 | — |
| 19 | hansen-brokerage | 0.246 | 0 | — |
| 20 | u-s-marketing-corporation | 0.242 | 0 | — |
| 21 | unkefer-associates | 0.232 | 0 | — |
| 22 | forward-strategies-insurance-brokerage | 0.219 | 1 | — |
| 23 | annuity-solutions | 0.000 | 0 | — (Lusha no_company_match) |

## Adjacent WM/AM targets — OUT of the insurance-IMO universe (preserved separately, NOT ranked as IMOs)

| Entity | Score | Series-licensed | Note |
|---|--:|--:|---|
| PMA Financial Network (was slug `preferred-marketing-associates`) | 0.858 | 29 | Brett Weeden (S24/S63/S65/S7, CRD 4913375); Audra Hartman Braski (S24/S63/S7, CRD 4741233); Caleb Walter (S6/S63/S65/S7, CRD 6551405). **Muni/public-sector RIA/BD (pmanetwork.com), reps under PMA Securities/PTMA — NOT an insurance IMO.** Reached via upstream source-list #79 wrong-domain pairing; it is the legit Prudent Man Advisors ($6.19B) deep-drill Andrew directed. Kept as an adjacent-WM record per CTO 162518Z; keep-vs-drop + universe-expansion is Andrew's call. |

## What changed vs the pre-FINRA v1

The v1 ranking compressed everything into 0.19–0.39 (title/seniority only). FINRA series-license activation decompressed it. Within the insurance-IMO universe, **lincoln-investment (0.79, 26 licensed) is the clear #1** — a broker-dealer/RIA-affiliated IMO with a strong asset-management-transition signal — followed by integrity-marketing-group (0.63) and gradient-financial-group (0.56). The pure annuity/insurance-marketing tail (lifepro, aig, unkefer, hansen) stays ~0.25 with 0 licensed reps. (The former #1, PMA at 0.86/29-licensed, is now reclassified out-of-universe as PMA Financial Network — see the adjacent-WM section above.)

## Enrichment provenance + honesty (per-company `finra_enrichment.disposition_breakdown`)

Three dispositions, surfaced so a 0-license firm reads correctly:
- **enriched_with_license** — firm+name matched in BrokerCheck WITH Series licenses (the signal).
- **no_finra_record** — matched-name not in BrokerCheck = genuinely non-registered (e.g. tech/IT execs) = a TRUE negative, not missing data.
- **no_firm_match** — name found but the BrokerCheck firm didn't match the IMO name. **UPDATE 2026-06-01:** an empirical probe (lincoln 18 + gradient 30 of these reps re-queried) showed they SCATTER across unrelated national firms (Charles Schwab, Merrill Lynch, Morgan Stanley, Edward Jones, LPL...) with no affiliated-BD cluster — i.e. mostly name-collisions + LinkedIn-current-company ≠ FINRA-current-employment. So this class is **mostly precision-correct rejection, NOT a recoverable recall miss.** The broad v2 firm_aliases IMO→BD map was therefore **SHELVED** (a broad alias map keyed on the scatter injects false positives for ~0 real recovery). Findings of record: `docs/briefs/find-insure-alias-recall-empirical-findings-20260601.md`. Precision-first (Andrew rule: company + name BOTH match) stands.

## Method

- Source: `api.brokercheck.finra.org` (public, no-auth, JSON; zero credit cost).
- Per pulled person: `/search/individual?query={name}` → firm-match on `ind_current_employments[].firm_name` → CRD → `/search/individual/{CRD}` → state/product/principal exam categories.
- Match rule (Andrew 2026-05-29): company + name BOTH match, else not counted.
- Full-24 enrichment run: 661 contacts, 79 firm+name matched, 73 series-licensed, **0 Lusha credits** (in-place backfill over existing .024 bronze). Of these, PMA Financial Network (now the out-of-universe adjacent-WM record) carries 29 series-licensed; the **23-IMO insurance universe therefore carries 44 series-licensed** (73 − 29).
