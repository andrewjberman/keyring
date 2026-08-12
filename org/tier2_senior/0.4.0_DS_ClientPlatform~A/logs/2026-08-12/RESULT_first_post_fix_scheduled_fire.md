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

## >> ⛔ RETRACTED ~15:31Z -- I "RESOLVED" THIS WRONG. The 109 is NOT the empty class.

**At ~15:19Z I wrote here that the 109-account gap below was IDENTIFIED as the
ZERO-CORROBORATED (genuinely-empty) class, "same 109, both planes," and I reported that
conclusion to Andrew and to COO. IT IS WRONG.**

**The empty class is 111, not 109.** Re-measured with an explicit partition check that made
the numbers account for themselves: of the 423 accounts reading exactly 0.00 on the activity
plane, **312 are ZERO-CONTRADICTED and 111 are ZERO-CORROBORATED (312 + 111 = 423, exactly).**
My "109" came from a merge whose parts I never summed against their own total -- 312 + 109 =
421, not 423, and **the two missing accounts were sitting in plain sight in my own output.**

**So the "same 109 on both planes" was a COINCIDENCE OF MY OWN ARITHMETIC ERROR, not an
identification.** The served-classification gap (725 + 74 = 799 vs 908 = **109**) and the
genuinely-empty class (**111**) are DIFFERENT NUMBERS over DIFFERENT CRITERIA, and I matched
them because I had miscounted one of them into agreeing with the other.

**THE 109 RETURNS TO OPEN OBSERVATION STATUS** -- exactly where it was before I wrongly
closed it. Named next step (nobody is blocked on it): D_04's valuation plane is NOT a
`holdings` dim -- no such dim exists in `silver/api_dims/` (the set is accounts_v2 · activity
· assets · assets_v2 · billing · household · household_rep_mapping · performance ·
positions_mv · representatives · tax_realized), so the "valuation = holdings.market_value"
shorthand in my own earlier ledger note is itself unverified and must be traced to the real
source before the 109 can be explained.

**WHAT STANDS, unaffected:** the 312 artifact class and its $68,676,658.56 (re-derived
identically by the positions discriminator AND the roster basis, and matching the original
investigation's count); every structural and value check in this file; the exact-sum identity.
The error was confined to the count of the EMPTY class and the false match to the 109.

**THE LESSON, and it is the same one this file already records once:** a partition must be
made to account for its own total. I checked that 312 + 109 "explained" the gap I wanted
explained, and never checked that 312 + 109 equalled 423. *An agreeable coincidence is the
one result nobody re-derives* -- and I found it only because a later pinning act forced me to
state the partition exactly.

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
