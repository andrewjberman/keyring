# IRPT_DASHBD round 64 -- L9 grade of the rule-24 record (DB-b-120: the tie-out as a sixth claimed value; method row 3 in the contract)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T06:12:21Z. Row IRPT_DASHBD-D2-S9.
**Input:** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~95/ROW3_AND_TIEOUT_CLAIM.json` (msg 4237 (rounds 63 and 64 drained @e4a88b23d6, @915e48125f)).

**Verdict: SOUND.** The tie-out tolerance takes the same claim as the five thresholds, and the claim set stays at four members.

| postulate | finding |
|---|---|
| MECE over the declared domain | Holds. The domain is how the writer knows each non-constant value it writes; six values, each placed. The tie-out is given to the writer by another cell, so `held` when present and `absent` when not. No fifth way of knowing is added |
| same grain | Holds. One value of one method row, like the five |
| one axis, one intent | Holds. The claim answers how the writer knows the value, nothing about whether a tie-out passed |
| which values a remedy does not move | Holds. Running the tie-out moves that value and its claim and none of the five |

This seat re-ran both checks (PASS) and the test folder (160 passed), and ran the name census the record limits to its own
scope: the new column name has no collision in the repo.

## Two things the record does not say

- **`threshold_claims_source` describes the five thresholds only.** For the tie-out, a defaulted claim and a stated one are not
  told apart. Today this loses nothing: a present tie-out is `held` either way. It would matter only if a writer were ever allowed
  to state `measured` or `inferred` for it.
- **The producer builds the column name by concatenation** (`TIEOUT_VALUE + "_claim"`), so a name census finds the column in the
  contract and the tests and not in the producer. A reader hunting the writer by that name will not find it.

## What it closes

- The contract lists method row 3 (0.5.0; rows 1, 2, 3). That closes row D2-W93-S3, which this seat was holding to graduate, and
  one of the three conditions on the Cottonwood mint. Still open for the mint: what the pair states about a priced bond day.
- Round 63's reader census (10 readers of the returns manifest, 0 strict) was not re-read by this seat.
