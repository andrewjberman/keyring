# AMGT_HARVST round 4 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~Y`. **For:** `3.0.0_SA_CVO~Z` at L9.
**Copied:** `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z`, `0.0.0_AB_MSTR~Z`.
**Round issued** @`eec53bf76f` from the L5 recut v1.3 @`8cef65cc00`, cut from the round-3 analysis @`4bcd9e87ca`.

## THE ROUND IN ONE LINE

**1 of 1 terminal, 5 of 5 criteria PASS, ZERO writes of any kind, ZERO vendor calls -- and the round's real output
is a MEASUREMENT THAT KILLS AN INFERENCE the result invites, plus a third order defect of the issuer's caught
mid-flight.**

## 1. THE CELL

`HVST-u-1`: **18 of 18 classified, NOTHING labelled.** All 18 classify as `transport_json` by byte shape,
`undetermined 0`, and the population was DERIVED by reading metadata rather than from a key list. `write_calls 0`,
structurally enforced by a write-guarded client, with a positive control showing all five write methods RAISE when
tripped.

**AC5 is the part that matters:** the 18 ARE the store's entire `MISSING` bucket at OBJECT GRAIN --
`population_equals_missing_bucket True`, store census 232 = `as_received` 16 + `bbg-client-json` 115 +
`normalised_record` 83 + `MISSING` 18. **So they are already disclosed by a measurement of the objects, with zero
writes, exactly as `1.0.0_SA_CTO~Z`'s ruling @`4d7ef9f79e` said.**

## 2. THE SHAPE TEST -- and it KILLS the inference this cell's own result invites

**The invited inference:** all 18 are non-canonical JSON, and `normalised_record` means the harvester's own output,
so surely non-canonical shape is evidence the 18 are NOT harvester output.

**Measured by the issuer over the FULL label groups, not a sample of one:**

| group | n | canonical | non-canonical | not JSON |
|---|---|---|---|---|
| the 18 (`MISSING`, bronze) | 18 | 0 | 18 | 0 |
| `normalised_record` | 83 | **0** | **83** | 0 |
| `as_received` | 16 | 0 | 3 | 13 |

**`normalised_record` is 0 of 83 canonical.** The harvester's own output is NOT canonically serialised either, so
**the two populations are SHAPE-INDISTINGUISHABLE on the one test that could have separated them.** The inference is
dead, and the ruling is now stronger by measurement rather than by argument: it is not only that shape cannot
answer provenance in principle, it is that the one discriminator anyone would reach for returns the SAME answer for
both.

**`as_received` is 13 of 16 not JSON at all** -- the HTML paths -- which is why no shape rule generalises across
this field.

## 3. THE ISSUER'S THIRD ORDER DEFECT, caught mid-flight

Row `Z-S13`. **My order told the worker to PROPOSE a `received-form` value from a byte-shape read.** The field
records PROVENANCE -- whose bytes these are -- and shape cannot answer it. `RECEIVED_FORMS` has two legal values and
`put_article_bronze` DEFAULTS to `as_received`, so the cheapest correct-looking answer would have been a provenance
claim indistinguishable from a measured one, and AC2 would have graded it PASS.

**Struck by AMENDMENT 1 @`d384fc3fe5` before the worker produced any output.** The worker's report confirms it
worked from the amended order. **Three order defects now in this project -- `Z-S10`, `Z-S11`, `Z-S13` -- none caught
by a gate, all caught by reading the artifact after the gates said PASS, two only after the order was with a
worker.**

## 4. WHAT I FOUND BY COUNTING THE WRITERS, which the record had at N=2

`1.0.0_SA_CTO~Z` corrected its own ruling's ground to "two writers, one validator". **I ran the census rather than
reading the table: THREE modules, FOUR write sites.**

| site | value | consults the enum |
|---|---|---|
| `harvest_grammar.py:91` | caller's, validated at `:79` | YES |
| `harvest_grammar.py:114` | hardcoded `"as_received"` | legal by luck, not by check |
| `bloomberg.py:115` | `bbg-client-json` | NO |
| `bright_data_serp.py:124` | **`brightdata-raw-body`** | NO, and unnamed until now |

**`brightdata-raw-body` appears on ZERO of 2231 objects** -- code-reachable, never landed. **EXPOSURE, not
incident.** The clause says N is a number the half PRINTS; the record printed 2. No row filed and nothing asked,
per the CTO's instruction on the 115.

## 5. TWICE IN ONE HOUR MY OWN PRINT LABELLED A GROUP WRONG, AND THE DENOMINATOR CAUGHT IT BOTH TIMES

- I grouped by label over the WHOLE bucket and printed a row headed **"MISSING (the 18)"** whose own denominator
  read **99 of 2017.** The 2017 are mostly the SIBLING project's research-report objects.
- Re-scoped to publisher-source keys and printed the same heading against **n=105**, of which **87 are not JSON at
  all** -- silver parquet, never in scope.

**Only the printed denominator and the not-JSON count revealed either one.** The heading was confident and wrong
both times. **That is the fourth instance tonight of a denominator catching a wrong-domain read**, and it is the
reason the table in section 2 states every n.

## 6. WHAT DID NOT MOVE

- **`FWD-1` stays NOT REALIZED.** The cell says so in its own report. Three of five publishers remain unmeasured
  live, and the listing pages round 1 discarded are gone.
- **Nothing was labelled, written, deleted, or re-fetched.** No vendor call.
- **The S3-delete breach stays carried to Andrew and unadjudicated.** This round does not touch it and does not rest
  on it.
- **`Z-S1`'s backward half stays GRADUATED AND UNREMEDIATED** per the ruling, and this cell is the measurement that
  makes that a recorded state rather than an open question.

## 7. TWO ASKS

1. **Grade the round.** Five of five mechanical, no judgment criterion.
2. **Note that the shape test closes the last route anyone would try on `Z-S1`'s backward half.** If a future seat
   proposes deriving provenance from stored bytes, section 2 is the measurement that refuses it -- 0 of 83.

## 8. STATE

`dep_stage` EXECUTING to ROUND_CLOSE with this commit. One order terminal, zero worktrees, zero branches.
Drain commit recorded in the covering message.
