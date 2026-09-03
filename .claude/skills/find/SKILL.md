---
name: find
description: Surface dual-business / insurance producing-agency leads by Case (A/B/C) and geography and render a ranked card list: `/find Case A Georgia`. Runs the FIND_DUALBIZ recall->evaluate->filter chain. Use on `/find ...` or asks to find, surface or pull leads, prospects, agencies or firms by case and region. Pair: `/target` takes a result into Lusha. DS-owned; data/find/dualbiz/.
---

# /find -- surface dual-business / insurance producing-agency leads

`/find <Case> <Geo>` is the catchall. It **discovers new firms**, scores them, filters
to your Case + geography, and prints a **ranked card display** in chat. One line in,
a clean leaderboard out.

```
/find Case A Georgia
/find Case B Southeast US
/find Case C Florida          (insurance-only greenfield -- see Case-C note)
/find Southeast US            (all cases, ranked)
```

## What the cases mean (Jim Reed framework -- readiness, NOT quality; all valuable)

| Case | Meaning | Signal |
|------|---------|--------|
| **B** | wealth/asset language **and** disclosure footnote present -- dual-business confirmed | `wm_classification=present` |
| **A** | language present, no disclosure -- wealth intent, warming up | `adjacent` |
| **C** | insurance-only, no securities -- **greenfield prospect, still valuable** | `absent` |

## Parse the query

- **Case** -> A / B / C (omitted = all cases).
- **Geo** -> a US state (`Georgia`->GA) OR a region preset (`Southeast US`->southeast;
  also south/northeast/midwest/west/southwest). Omitted = nationwide.

## The chain (run in order)

**1. RECALL -- find NEW ones (BrightData SERP; pre-authorized this workstream).**
Reverse-search the disclosure strings of the in-scope providers, geo-qualified. Use the
working engine (`serp_opal`); the free DDG path is blocked (HTTP 202).
```bash
# geo-scoped sweep of provider disclosure strings -> harvested file
python data/find/dualbiz/scripts/serp.py --engine brightdata --pages 3 \
    --out data/find/dualbiz/config/serp-harvested-$(date -u +%Y-%m-%d)-<geo>.json
# (for a targeted aggregator, run its RIA string: e.g. "offered through Brookstone Capital Management" Florida)
# PROVIDER-AGNOSTIC discovery (data-driven, finds firms beyond the seed roster) -- anchors on the
# disclosure phrase ("advisory services offered through", ~66% near-universal) x category vocab x geo:
python data/find/dualbiz/scripts/serp.py --discover <Geo> --engine brightdata --pages 2
python data/find/dualbiz/scripts/registry.py --merge <that-file>     # additive into S2 registry
```
- **Case C needs a DIFFERENT lever** -- disclosure reverse-search can't reach insurance-only
  firms (no footnote). For Case C, recall via geo + insurance-vocabulary search of producing
  agencies (NOT the disclosure strings). If `/find Case C ...`, say so and use the insurance-vocab
  query set, not the disclosure set.
- Recall costs modest SERP credits. If the operator only wants existing data, skip step 1.

**2. EVALUATE -- scrape + score the (expanded) universe.**
```bash
python data/find/dualbiz/scripts/pipeline.py --date $(date -u +%Y-%m-%d)
```
Run in the background (it scrapes the whole registry; WHOIS stage is slow). It derives each
firm's `state`, so geo filtering works after this.

**3. FILTER -- by case + geo.**
```bash
python data/find/dualbiz/scripts/cases.py --case <A|B|C> --state <GA> --group-by-case
python data/find/dualbiz/scripts/cases.py --case B --region southeast        # region preset
```

**4. ENRICH + RENDER -- the card display.**
For the top ~10-15 rows, read each firm's harvested silver text
(`.runtmp/dualbiz/<date>/silver/<slug>/<date>/page.json`) and write a ONE-LINE grounded
description + a short impression. Then render the cards (see format).

## Card display format (/draw house style)

Render the ranked result as boxed monospace cards in a single fenced block:

```
/find Case B -- Georgia          12 firms (B only) | ranked by tier -> ins density -> sec density -> score
================================================================================
 #1  FAIRWAY FINANCIAL PARTNERS                                   [Case B] GA
     score 181  ins 6 / sec 9   RIA: Simplicity Wealth   fairwayfp.com   age 1y
     Full planning shop, process-driven; strongest dual-business signal in GA.
--------------------------------------------------------------------------------
 #2  OGLESBY WEALTH STRATEGIES                                    [Case B] GA
     score 171  ins 5 / sec 3   RIA: Simplicity Wealth   oglesbywealthstrategies.com
     Planning-led (AssetLock, Asset-Map, VaR); advisory-forward. Strong target.
--------------------------------------------------------------------------------
 ...
================================================================================
 Case mix: B=12  |  filtered from N scored  |  flags: <dedupe/geo/aggregator notes>
```

Rules for the cards:
- Rank number, FIRM (caps), `[Case X]` badge, state on the title row.
- Line 2 = the numbers: score, ins/sec density, named RIA/provider, domain, domain age.
- Line 3 = the one-line grounded description + impression (from the site text -- never invented).
- **Flag, don't hide:** aggregators/providers that aren't producing-agency targets, geo
  mislabels (site says another state), dedupes (same operator across domains), and denylist
  noise (news/CDN hosts). Call them out in the footer; drop them from the ranked cards.
- Keep it scannable; offer `/target <firm>` on anything they like.

## Cost gates
- Recall `--engine brightdata` = modest SERP credits (pre-authorized for this workstream).
- Everything else (evaluate, cases, render) is free + idempotent.
- The expensive enrichment (people/emails) is `/target`, not `/find`.

## Provenance
- Pipeline: `docs/architecture/FIND_DUALBIZ.md`; project `org/projects/FIND_DUALBIZ.json`.
- Scripts: `serp.py` (recall) -> `registry.py` (S2) -> `pipeline.py` (evaluate) -> `cases.py` (filter).
- Case framework: Jim Reed Teams 2026-06-26 (segmentation, not a quality filter).
