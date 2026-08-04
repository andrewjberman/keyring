# RCG Cycle-3 Mechanical Evidence Sweep — OBSERVED only, zero labels assigned

**Author:** 4.0.0_SA_CRO, 2026-08-04 ~1325Z
**Protocol:** RCG_CYCLE3_ADJUDICATION_PROTOCOL_20260804.md @d504050e5 (s.7 step 2, run in
parallel under the Andrew-direct GO relayed @ff160d0b5; tranche-1 adjudication still gated
on CTO~B's protocol ack)
**Machine table:** RCG_CYCLE3_EVIDENCE_TABLE_20260804.json (same dir; per-tree signals +
citations)

## Denominators (every scan printed its own)

408 candidate files / 88 lambda function-trees (predicate re-derived at run time).
Registry: 194 function entries, 178 distinct source_dirs. Live plane: 194 functions
(fully-paginated list-functions dump, NextMarker absent -- materialized-list count).
Orphan TF scan: 390 tracked .tf files.

## Verdicts (protocol s.2 table)

| Verdict | Trees | Files | Meaning |
|---|---|---|---|
| LIVE (a+b+c agree) | 54 | 318 | registry + TF + live all confirm |
| DIVERGENT (signals disagree) | 28 | 75 | NOT label calls -- Rule-4 drift findings, routed to CTO~B |
| ORPHAN (absent everywhere) | 6 | 15 | ARCHIVE-eligible pending s.4 build-recipe pass |

ORPHAN trees: cloudfront_market_generator, mdpf-manifest, news_scanner,
schwab-bronze-freshness, security-sweep-daily, smartx_query.

## The DIVERGENT class decomposes into four distinct defects (the finding half)

**(i) Registry+live agree, TF signal unverified (~17 trees)** -- e.g.
access-anomaly-scanner, cost-anomaly-scanner, ec2-auto-shutdown-enforcer, all seven
seeking-alpha functions, sentiment_query_api. Mostly registry entries missing/unverifiable
`tf_file` metadata while the function demonstrably exists. Least alarming; still Rule-4
metadata debt.

**(ii) TF-declared but neither registered nor live (7 trees)** -- artifacts, finbert (10
files), lib, shared, opal-assets-absence-check, portal_authorizer,
precompute_market_metrics. CAVEAT: lib/shared/artifacts are support dirs my tree grain
lumped, not function trees (grain note for adjudication). finbert and portal_authorizer
are the real members: Terraform declares them, nothing runs -- declared-but-unapplied or
deleted-live.

**(iii) Live + TF but ABSENT from the registry (3)** -- inf-gold-trigger,
m365-ms-ingest-liveness, public-data-router. Direct Rule-4 gaps ("every Lambda has an
entry"); CI drift detection is blind to exactly these.

**(iv) Registry crosswalk error (1)** -- live `opal-trending-image-generator` exists, but
the registry's source_dir points at `trending_image_selector/` while
`trending_image_generator/` (4 files) matched nothing until a prefix-tolerant recheck.
Initially misread as ORPHAN by my own prefix-blind name guess -- the false-orphan was
caught by re-checking with substring tolerance; banked as a sweep-instrument lesson.
Either the source_dir is wrong or the generator tree is dead code; the registry cannot
say which. Adjudication must resolve this one from the TF/live side, not the registry.

## What happens next (unchanged from protocol)

No labels landed from this sweep. Tranche-1 adjudication starts on CTO~B's protocol ack:
ORPHANs get the s.4 build-recipe pass before any ARCHIVE verdict; DIVERGENT items route
to CTO~B as drift findings (they are evidence about the ESTATE, not about the labels);
LIVE trees settle KEEP-at-HIGH or transfer to the MIGRATE/layer-refactor spec. Model
blindness held: no p_archive consulted.
