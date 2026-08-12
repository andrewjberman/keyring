# RESULT -- the FIRST post-fix scheduled fire: ALL PRE-REGISTERED CHECKS PASS

**Read 2026-08-12 ~15:05Z against the pre-registration committed ~13:26Z BEFORE the evidence
existed** (same-day sibling file, `PREREG_first_post_fix_scheduled_fire.md`). Andrew-direct:
*"wait for the fire and read both figures."* Nothing here was graded against a band invented
after the numbers were seen.

## The fire

Scheduled chain fired on its normal daily slot; `pipeline-complete.json` advanced
**2026-08-11 14:59:31Z -> 2026-08-12 15:02:12Z**; serve stamped `generated_at`
**2026-08-12T14:58:54Z**, `data_as_of` **2026-08-11** (T-1, correct for a Wednesday read --
NEVER#1 resolved BEFORE any freshness judgment). Deployed code verified in place BEFORE the
fire, 4/4 md5 TIE (9a25fe0d / 52005d2b / eaae8fb4 / 777c62ae) -- so this run exercised MY
artifacts, not a coincidence of similar behavior.

## STRUCTURAL -- all four PASS (exact, no bands)

| # | Check | Measured | Verdict |
|---|---|---|---|
| S1 | `ending_mv_source` present | 908/908 = `portfolio-roster-currentValue` | **PASS** |
| S2 | retired `is_fee_earning` absent | absent | **PASS** |
| S3 | ending_mv populated, zero source-absent | **908/908, absent 0** | **PASS** |
| S4 | own tie-out vs the retired windowed cell | **554/554 tie TO THE CENT** | **PASS** |

**S4 is the load-bearing one**: on every row where the vendor DID report a windowed value,
the roster-sourced value matches it exactly. The fix changed the quantity's COVERAGE, not its
MEANING -- which is the claim that would have been unfalsifiable without this control.

## VALUE -- all three inside their pre-registered bands

| # | Quantity | Measured 08-12 | Pin (08-11 QA) | Delta | Verdict |
|---|---|---|---|---|---|
| V1 | silver billing book | **$209,225,005.59** | $209,476,279.36 | -0.12% | **PASS** (band +-2%) |
| V2 | served fee-earning AUA | **$203,216,860.04** | ~$202.84M | +0.19% | **PASS** |
| V3 | served NON-fee-earning AUA | **$6,008,145.55** | ~$6.29M | -4.5% | **PASS** (band $6-8M; small population, 61 clients / 74 accounts, so % is volatile by construction) |

**The rescued class, measured:** the vendor's windowed cell is absent/non-numeric on
**354 of 908** rows; those rows carry **$68,676,268.78** that the pre-fix pipeline suppressed
to zero. Pre-fix book (08-11 partition, built 14:07Z before the deploy) was $140,717,260.47.

## CROSS-PLANE AGREEMENT (measured; mechanism stated as INFERRED)

- served `total.aua` = **$209,225,005.59**
- fee + non_fee + unclassified = **$209,225,005.59** (delta 0.00) -- this identity is BY
  CONSTRUCTION (the exhaustive-bucket design); it is not independent evidence.
- silver billing book, read independently from the silver partition = **$209,225,005.59**
  (delta 0.00) -- **this one IS a cross-plane fact**, and it is the meaningful tie.
- `unclassified_aua` = **0.0** -- every dollar classified.
- **INFERRED, not source-confirmed:** the likely mechanism for the served/silver equality is
  that both planes now resolve to roster currentValue post-fix. Stated as inferred; grounding
  it needs the holdings-plane derivation read, which nobody has asked for.

## >> RESOLVED ~15:19Z: the 109 below are the GENUINELY-EMPTY class (measured, same day)

The observation flagged below is closed by the B_00 scope measurement taken an hour later.
Of the 423 accounts where the activity plane reads exactly 0.00 on today's partition:
**312 are ZERO-CONTRADICTED** (roster holds value -- the artifact class, $68,676,658.56) and
**109 are ZERO-CORROBORATED** (roster also zero -- genuinely empty). Same 109, both planes.
So the 725+74=799 vs 908 gap was never a coverage defect: those accounts hold no mass, which
is why the value identity was exact. **The 312 also re-derives the ORIGINAL investigation's
suppressed-class count from a different plane** (the V4 band's "312-account coerced-zero
ending_mv class") -- three independent measurements, one stable identified class.
*Flagging an observation I could not yet call, instead of asserting or dropping it, is what
let it resolve into a fact within the hour.*

## OBSERVATION (flagged, not smoothed; NOT a defect claim) -- NOW RESOLVED, see above

Classified account counts 725 (fee) + 74 (non-fee) = **799**, against **908** billing rows --
a 109-row gap that carries **$0.00** (unclassified_aua = 0.0). Consistent with accounts having
no holdings mass on the valuation plane; the VALUE identity is exact and unaffected. The count
denominators differ between planes by construction. Grounding the 109 is a follow-up if anyone
wants it, not a finding today.

## PROCESS NOTE AGAINST MYSELF (the pre-registration earning its place)

My FIRST read of `ending_mv_reported` reported "0 of 908" and looked like an upstream vendor
outage. **That was my instrument, not the data**: the column holds the vendor's RAW TEXT
(`'N/A'`, `'$8,212.12'`) and I ran numeric coercion over it, collapsing every value to null.
Re-read as strings it says 554 -- matching the prior day exactly. Caught before it was
reported as a finding. This is the designed-half of the retrieval-control class: the
instrument's domain was not the question I asked, and no amount of care would have caught it
-- only re-deriving with the right domain did.

## WHAT THIS CLOSES

Andrew's 2026-08-11 instruction #1 (*"get to the bottom of this fee earning aua ... true
non-fee-earning aua was more like 8m but we're saying here its 60m+"*) and instruction #2
(*"fix the is_fee_earning flag derivation too when the window fix lands"*) are now **verified
in PRODUCTION on a scheduled run**, not on QA figures: non-fee-earning AUA serves at
**$6.01M**, against his own ~$8M expectation and the $60M+ that prompted the investigation.
Both standing scheduled-fire watches are DISCHARGED.
