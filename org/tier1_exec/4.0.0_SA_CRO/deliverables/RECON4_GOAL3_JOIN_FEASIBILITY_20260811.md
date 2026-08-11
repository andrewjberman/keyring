# RECON-4 -- GOAL-3 JOIN FEASIBILITY: model-holdings account grain vs the ADVI account spine

**Author:** 4.0.0_SA_CRO · **2026-08-11, 0530-0545Z** · **archetype:** TRACE + VALIDATE
**Commission:** the collective-recon mandate @07c6f68bf4 (RECON-4), verdict routed to CTO + COO per
CTO's oversight frame 053919Z; feeds goal 3 of the four-month structure (@dedd7bdeab companion).
**Run record (schema-VALID):** `workflows/atom_decomposition/runs/advi-model-holdings-account-join/20260811T0530Z/`
-- 3 entities x 8 fields, census (DERIVED from cells post-amendments, CVO census-drift catch @4918e8b48f) 21 MEASURED / 1 INFERRED / 2 NOT_MEASURABLE. Read-only; DRY,
UNCERTIFIED (CVO certifies). **No account values left scratchpad -- counts, formats, rates only.**

<a name="domain-bar"></a>**Domain bar:** expected variance = per-firm key-format differences.
FINDING class = a firm whose join is structurally impossible or whose input does not exist. The
verdict is deliberately per-firm; a single aggregate feasibility claim would be the two-grain error.

## THE VERDICT, FIRM BY FIRM (believed-vs-actual, the required shape)

**Item 3 believed (the goals brief): account-level matching is a join/aggregation problem over the
existing consolidated-staging logic, applied firm-by-firm. Actual: THREE DIFFERENT PROBLEMS, one
per firm** -- measured on the newest feed partition vs the newest ADVI accounts artifact per firm:

| Firm | Feed key (measured) | Spine key (measured) | Overlap | Verdict |
|---|---|---|---|---|
| **08335338 ADVI (49F)** | 36-char UUID, 7,230 distinct -- **it is the SmartX `allocationId`**, mapped at `wsb_49f_smartx_model_aua.py:167`; `custodian` hardcoded `None` at `:169` with the feeder's own comment *"not exposed on the SmartX allocation row"*; `household_id` all-null | `silver/fact_acc` `account_id`: 10-digit Schwab number, 7,239 distinct (date=2026-08-07) | **0.0%** -- exact, digit-normalized, and last-8 all zero | **RESOLVED ~0551Z -- MEASURED JOIN PATH AT 99.8%** (~A, at-rest, zero egress): feed.account_id -> `fact_allocation_account_map.allocation_id` -> `.account_number` -> **zfill(10)** -> fact_acc.account_id (BOTH DENOMINATORS, per COO 055328Z: MAP side 5,701 of 5,715 distinct account_numbers matched = 99.8 percent; SPINE side 5,701 of 7,239 fact_acc accounts matched = 78.8 percent -- the spine-side remainder is accounts in NO model, an EXPECTED asymmetry, not a miss; residual on the map side = 12 nine-digit entries + 2 misses, flagged). The direct-feed verdict STANDS (0.0% without the map hop); the fix is a JOIN through the map table, never a feeder change |
| **Inflection** | short numeric ids, FULL RANGE len 2-14 (matched set len 2-4; the 11 unmatched ARE the len-12-14 long tail -- CVO cert recompute), 561 distinct (feed 2026-08-06) | `gold/dimensions/accounts_dimension_latest` `account_id`, 869 distinct (written 08-10) | **98.0%** (550/561), exact, no normalization | **JOINABLE TODAY** on the native key. Rollup keys (advisor_assignments, client_dimension) already sit spine-side. Residual: 11 accounts (2.0%), cause open (closed/vintage-skew/book-definition candidates) |
| **Cottonwood** | **NO PIPELINE FEED exists** -- `model_aua_positions` partitions are exactly {49financial, inflection}, full 116-object enumeration. **ANDREW-DIRECT CORRECTION ~0547Z, verbatim: "Cottonwood does have a model holdings feed via the Black Diamond Rebalance endpoint" -- the VENDOR SOURCE exists; what is absent is the ingest leg.** RCN-0001 note: the rebalancer-models endpoint family was one of the teardown's five [BODY-NOT-CAPTURED] gaps -- schema capture there is the named opening move | n/a | n/a | **SOURCE EXISTS, PIPELINE ABSENT.** Goal 3 for cottonwood still sequences behind goal 1 (the custom-model pull IS the ingest leg, and the Rebalance endpoint is its scouted mechanism); cot-BD egress is standing-LIFTED so the endpoint is probeable. When the feed exists: BD is RELATIONSHIP-grain (Andrew 08-04) -- the account test needs the collapse discipline |

## THE FOUR CONSEQUENCES FOR THE PROGRAM (information, not rulings)

1. **ANSWERED ~0551Z (~A 054928Z + 055138Z): the map table exists and the path is measured.** `smartx/platform/silver/fact_allocation_account_map` (daily, 7,262 rows) carries allocation_id -> 8-digit Schwab account_number; the form bridge to fact_acc is zero-padding; end-to-end 99.8%. COO can decompose the 49F build TO. *(Original text preserved below for the record of what was open at delivery:)* The 49F path needs one new fact before any build: does a SmartX surface expose
   allocation->custodian-account? The feeder's comment says the allocation row does not; whether
   ANOTHER endpoint does is **unverified. CORRECTED 0546Z (COO caught my too-narrow read): the live probe is NOT
   egress-gated -- SMARTX is on the standing LIFTED list, and the work is Andrew's collective-recon
   mandate, so both wire and work are authorized. My original "vendor-egress-gated" line was the
   too-narrow grant read whose failure mode presents as a legitimate blocker and stalls quietly**. This is a RECON-2-adjacent question -- ~A's 49F archetype run should carry it as
   a cell. If no endpoint exposes it, item 3's 49F leg needs an identity source outside SmartX.
2. **Inflection is the existence proof** that item 3's design is right wherever the key survives
   the feed: 98% native-key join, rollup spine already in place. It can prototype the overlay first.
3. **The goal-1 -> goal-3 dependency is now measured, not assumed:** cottonwood's item-3 leg cannot
   start before item 1 lands its feed -- **and per Andrew's ~0547Z correction the source side is
   already there (BD Rebalance endpoint), so item 1 is an INGEST build, not a data hunt; the
   [BODY-NOT-CAPTURED] rebalancer-models schema gap from RCN-0001 is its first capture target.**
4. **A naming defect worth fixing at the source:** the feed column NAMED `account_id` carries an
   allocation UUID -- name-vs-content, the exact class the field-registry discipline (2a) exists to
   kill. Plus one live trap defused: feed 7,230 rows vs spine 7,239 accounts -- near-identical
   counts over fully disjoint keys (Rule 10: never read count parity as identity parity).

## BOUNDARIES

Newest-partition sampling (one per firm side); 49financial feed = the only 49F firm partition;
inflection residual cause unmeasured; the SmartX endpoint question not yet probed (carried in RECON-2 at ~A;
probe AUTHORIZED per the 0546Z correction -- the original egress-gated claim was WRONG); cottonwood spine cells NOT_MEASURABLE absent an input; L2 trigger-grain cells
(CTO's oversight note 5) belong to the per-firm pipeline decomps (RECON-2/3/5), not this join run.

## POST-CERT ADDENDUM (2026-08-11 ~0600Z) -- COTTONWOOD RE-GRADED A SECOND TIME: THE INGEST ALREADY EXISTS AND RUNS DAILY

Certified state above said SOURCE-EXISTS-PIPELINE-ABSENT (Andrew's BD-Rebalance correction). Following
the teardown's own July-21 note ("Opal already pulls the Cottonwood Rebalancer daily"), measured at rest:
**the ingest EXISTS, LIVE, THREE TIERS DEEP** under `opal-data-assets/blackdiamond/cottonwood/`:
bronze `rebalancer_models` (21) + `rebalancer_model_detail` (561) + `rebalancer_accounts` (105), newest
2026-08-10 06:00Z, daily completion markers in `meta/` through 08-10 · silver `fact_model_roster` /
`fact_model_definition` / **`fact_model_assignment`** / `fact_model_blend` (21 daily partitions each,
date=2026-08-10) · gold `dim_model_portfolio` (13, newest 08-10 13:00Z) -- the SAME tables RECON-1
measured the MDPF floor consolidator reading.

**And `fact_model_assignment` is ACCOUNT-GRAIN with the join key aboard:** 921 rows / 21 cols incl.
`account_number` (921 distinct; len 9 x662 + len 11 x86, digit-rate 0.84), `account_id` (8-digit BD
internal), strategy/program names, SMA/UMA flags. So cottonwood's goal-3 input is not "absent" and not
merely "source-exists" -- **the account-grain model-assignment table lands daily already.** The
remaining cottonwood question collapses to the SAME measurement as the other two firms: `account_number`
vs the cottonwood ADVI account spine (spine identification + overlap = the follow-up cell; BD
relationship-grain collapse discipline still applies downstream). Goal 1's "custom model pull" is
therefore an EXTENSION of a live puller (Custom-model scanning of Opal constituents), not a fresh
ingest build. Believed->actual across three generations in 70 minutes: NO-INPUT -> SOURCE-EXISTS
(Andrew) -> INGEST-EXISTS-LIVE (at-rest measurement) -- each correction smaller than the last because
each denominator was stated. This addendum post-dates cert @4918e8b48f and is flagged to CVO for
delta-certification; nothing certified above is contradicted -- the feeds-plane absence remains true.

## POST-CERT ADDENDUM 2 (2026-08-11 ~0607Z) -- THE COT JOIN TEST LANDED: STRUCTURED ZERO; THE THREE-FIRM MEASUREMENT SET IS COMPLETE

~A ran the cot overlap on the identified spine (grounding: their 060710Z result, both denominators
printed): spine `accounts_dimension_latest.account_id` = 927 distinct, uniformly 11-digit; FMA
`account_number` = 921 distinct with a MESSIER length distribution than the headline (9x662, 11x86,
10x48, 8x30, 7x9, 6x4, 5x1, **plus ~100 prose-length values of 15-50 chars -- content contamination
in a KEY column**, a name-vs-content finding for the 2a census beyond form-families). **Join: 0.0%
at EVERY tested form** incl. same-length 11x11 subsets -- these are DIFFERENT NUMBERING SYSTEMS, not
formats of one number (contrast 49F, where zfill bridged at 99.8%). **VERDICT: MEASURED-NO-DIRECT-
JOIN; an INTERMEDIARY table is required.** Candidates in ~A's likelihood order, deliberately not
chased (design-relevant selection belongs to RECON-5a's inventory): (a) the `rebalancer_accounts`
bronze family (105 objects AT REST -- checkable without egress), (b) cot custody fact_holdings'
Relationship x Account linkage, (c) the BD account-detail surface if it carries both ids.

**GOAL 3's COMPLETE PER-FIRM DESIGN FACT, closing the item-3 recon input:** the account overlay
needs THREE DIFFERENT identity mechanisms -- inflection NATIVE KEY (98.0%) · 49F ONE-HOP MAP +
zfill (99.8%) · cottonwood INTERMEDIARY-REQUIRED (measured zero, candidates named). A single
uniform join design was never available; the measurement program has now said so per-firm with
denominators, which is exactly what the build spec needs to not discover it mid-build.

## POST-CERT ADDENDUM 3 (2026-08-11 ~0615Z) -- DELTA-CERT CORRECTIONS FOLDED (@da62a742c5): END-TO-END IS 99.65%, AND THE TWO UNIVERSES ALIGN BY COINCIDENCE, NOT CONSTRUCTION

**Figure correction (CVO delta-cert, adopted):** my addendum-1 "end-to-end 99.8%" mislabeled a LEG
as the whole. Decomposed: FEED->MAP = 7,220/7,230 = **99.86%** (CVO-measured, previously unclaimed)
x MAP->SPINE = 5,701/5,715 = **99.8%** => **TRUE END-TO-END = 7,205/7,230 = 99.65%** -- 25 feed
allocations reach no spine account. Residual split corrected: **3 x len-8 + 11 x len-9** (my "12
nine-digit + 2 misses" total agreed, split did not). Anyone quoting the 49F path quotes **99.65%
end-to-end** or a LABELED leg rate, never bare "99.8%".

**CVO's routed unknown, answered at source:** map-universe vs feed-universe is **COINCIDENCE-BY-
PIPELINE-ALIGNMENT, NOT CONSTRUCTION.** The map's producer derives its rmid universe from the day's
BRONZE LISTING (`smartx_conversion.py:260-268` -> `_list_entity_ids(s3, bucket, "model")`); the wsb
feeder derives its universe from the REGISTRY filter (models carrying `smartx_model_id`,
`wsb_49f_smartx_model_aua.py:125-146`). Two independent derivations that currently align because
the upstream puller is registry-driven -- they drift independently if the puller's scope widens or
the registry moves between pulls, and the 25-allocation FEED->MAP gap is plausibly this class (or
intra-day pull timing; cause UNMEASURED, parked with the other residual families). **The 99.86% leg
is stable only while puller and registry stay in lockstep -- a shared-derivation caveat the join
spec should carry as a one-line precondition, not discover on the first drift.**

**Specimen banked (CVO's own instruments bitten):** `fact_allocation_account_map` itself carries the
name-vs-content defect -- its `account_id` column holds a SmartX UUID while `account_number` holds
the Schwab digits; CVO's first two computation passes joined the wrong column and returned a clean
0.0% before a length-distribution print caught it. Third live specimen for the 2a registry, and
empirical proof that per-table key-hygiene grading (addendum-2's lesson) is not optional.
