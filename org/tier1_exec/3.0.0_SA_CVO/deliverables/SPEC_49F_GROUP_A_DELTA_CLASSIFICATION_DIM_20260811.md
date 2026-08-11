# 49F GROUP-A SPEC DELTA -- the canonical asset-classification dim (A_07)

**Author:** 3.0.0_SA_CVO · **2026-08-11 ~1605Z** · **archetype:** IMPLEMENT (design)
**Commission:** CTO 160241Z -- mix_summary is BLOCKED-ON-INPUT because neither `fact_sec` (74 cols)
nor `dim_asset` (29 cols) carries class columns; bd's served mix derives from ETFClassifier machinery
(regex + DynamoDB `bd-securities`) living OUTSIDE the A/B/C canonical plane. The pattern has no home
for asset-class classification -- this delta adds it. **Queued behind parity; mix_summary stays a
declared BLOCKED-ON-INPUT exclusion at P1 close, does not gate it.**

---

## THE GRAIN DECISION (Rule-24, ANSWERED FROM THE MACHINERY -- not assumed)

**ONE classification dim for ALL firms, ASSET-GRAIN, FIRM-INDEPENDENT.** The classification is an
ASSET-TRUTH, not a firm-policy -- measured at source (`data/black_diamond/scripts/gold/lib/etf_classifier.py`):
- `classify(ticker, asset_name) -> asset_class` keys on the ASSET (ticker/name). **There is no
  firm/partner parameter anywhere in `classify()`.**
- The classes are intrinsic SECURITY-TYPE properties: the regex families are structured-note /
  buffered / annuity (alt), cash/sweep/money-market (cash), coupon-rate+maturity / bond keywords
  (fixed_income) -- what the security IS, not how a firm treats it.
- A bond is a bond, a sweep fund is cash, a buffered ETF is alt, regardless of who holds it. Two
  firms holding the same ticker MUST classify it identically -- a per-firm dim would let the same
  CUSIP be equity at one firm and alt at another, which is a defect, not a policy.

So: firm-independent asset-grain dim. **The one caveat that is NOT a grain question but a POPULATION
one:** the current substrate is the `bd-securities` DynamoDB table (bd-populated), and the classifier
is MULTI-HOMED today (bd/cot/partners each carry a copy of `etf_classifier.py` + the DynamoDB
variants under yang_pipeline) -- so a security cot/inf holds that bd never saw is uncovered. The
canonical dim is asset-grain (one dim) but its POPULATION must be the UNION of all firms' held
securities (from the positions/holdings canonicals), not bd's table alone.

## A_07 -- THE ARTIFACT

| Field | Spec |
|---|---|
| Script | `a07_dim_asset_classification.py` (NEW) -- the dim PRODUCER, run at build time |
| Inputs | the ETFClassifier LOGIC ported (regex families + the `bd-securities` DynamoDB content materialized at build) x the UNION of held tickers/cusips across all firms' B_01 canonical_positions | 
| Output | `dim_asset_classification` -- grain (security_key = ticker/cusip), columns: `asset_class`, `classification_source` (dynamodb-ticker / dynamodb-alias / regex-name / override), provenance (`source_pipeline`, `_ingested_at`, `_classifier_vintage`) |
| The rule this delta exists to enforce | **THE DYNAMODB SCAN HAPPENS AT BUILD TIME, IN THE DIM PRODUCER -- NEVER IN AN EMITTER.** Emitters (D-group mix_summary) read the MATERIALIZED dim, a pure canonical-plane parquet read. A classifier inside a gold emitter couples gold to a serving-plane store and double-homes the definition (COO's ratified program law) |

## THE TWO CONSTRAINTS, INHERITED AS RULED

1. **PORT, NEVER REBUILD (build-ladder rung 2):** the estate HAS this machinery and it produces the
   currently-served mix. A_07 RELOCATES its home onto the canonical plane -- same regex, same
   DynamoDB content, materialized. Rebuilding classification logic fresh is prohibited; so the delta
   ports `etf_classifier.py`'s `classify()` verbatim into the dim producer, and the multi-homed
   copies (bd/cot/partners) COLLAPSE to this one canonical home on their next touch (the emitters
   repoint to the dim; the lib copies deprecate -- consumers first, then the lib, per the retire-order law).
2. **SINGLE HOME + PROVENANCE + ITS OWN ACCEPTANCE BATTERY** (proof contract): A_07 is one producer,
   its output is the one classification authority, and per the A_03 lesson it ships WITH acceptance
   ids (below) so it is never built with zero coverage.

## ACCEPTANCE (machine-checkable -- A5-A07 ids, so the coverage check finds them)

- **A5-A07-COVERAGE**: every held security across all firms' canonical_positions resolves to a class
  or lands UNCLASSIFIED-LOUD (0 silent nulls); denominators printed (classified / unclassified /
  total held).
- **A5-A07-PARITY-VS-SERVED**: on the bd overlap set, A_07's class per ticker == the currently-served
  ETFClassifier output (the PORT is faithful -- a ported classifier that reclassifies is a rebuild in
  disguise; this is the differential control that catches it).
- **A5-A07-NO-EMITTER-DYNAMODB**: a grep-class assertion that no D-group emitter imports/calls
  ETFClassifier or boto3-dynamodb -- the coupling this delta exists to remove, mechanically enforced.
- **A5-A07-SOURCE-CENSUS**: `classification_source` distribution printed (how many via dynamodb-ticker
  vs alias vs regex vs override) -- so a shift toward regex-fallback (DynamoDB coverage decaying) is
  visible, not silent.
- **A5-A07-DETERMINISM**: two same-input runs byte-identical; **A5-A07-PROVENANCE**: cols + vintage
  stamp present.

## SCOPE / BOUNDARIES

This delta adds the A-plane home; it does NOT build mix_summary (that is D-group's emitter, which now
has a canonical input). It does NOT rule the cot/partners lib-copy DEPRECATION timing (retire-order,
consumers-first -- a follow-on). The `_classifier_vintage` stamp exists because the DynamoDB content
changes; a stale-vintage dim is a finding, not silent drift (same discipline as the pinned-delta
stale-pin). Firm-independence is asserted at build: if any security ever needs a firm-specific class,
THAT is a new axis and a Rule-24 event, not a silent per-firm fork of this dim.

-- 3.0.0_SA_CVO
