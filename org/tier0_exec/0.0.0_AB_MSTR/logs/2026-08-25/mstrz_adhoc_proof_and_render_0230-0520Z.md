# MSTR~Z 0230-0520Z: the ad-hoc proof landed, and every claim I made about WHY something failed was wrong

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, VALIDATE

Seat `0.0.0_AB_MSTR~Z`, site Z. Follows `mstrz_overnight_2210-0230Z.md`. Written from hot context.

## 1. WHAT ANDREW GOT, AND IT IS THE THING HE ASKED FOR AT 04:30Z

His posture, relayed ~04:30Z: *"I want to prove it works end to end with perfect numbers and then and
only then am I accepting of waiting on scheduled publishes just as a final confirmation."*

```
04:45:15Z  125,915 B  long windows 120/187              <- the GO'd proof publish
04:53:51Z  126,863 B  long windows 181/187, 8/8 on 177  <- CTO~Z's targeted backfill
data_as_of 2026-08-24 | 169 distinct securities | 105 + 58 + 6 reconciles to the unit
```
**His own verdict at the render, ~05:06Z: *"We now have full performance for everything but still
missing SALXX YTD and 1Y."*** That sentence is the acceptance; no agent measurement substitutes.

**HIS POSTURE PAID FOR ITSELF IN FOUR MINUTES.** The first invoke died `AccessDenied` on
ListObjectsV2 -- ask 1's history loader made that function's FIRST EVER list call and the role had no
`s3:ListBucket`. **The 13:00Z scheduled run would have hit it identically and failed silently.** Only
an EXERCISE finds that; no config read does. I was the loudest voice for "wait for the schedule" and
I was wrong.

**AND THE BIGGEST WIN IS WORK WE DID NOT DO.** Andrew ~04:50Z: *"I just realized we only display up
to 1Y anyway ... which means we dont need max backfill for these tickers."* Sized deep backfill
**1,569,204 rows -> 16,265 actually needed = 1.0%.** Four seats sized, probed and business-cased a
pull the display ceiling made unnecessary. **Nobody's measurement was wrong; the question was.**

## 2. MY ONE REAL CONTRIBUTION: THE RENDER DEFECT'S MECHANISM

`0.4.0_DE_ClientPlatform~Z` measured 5 of 8 windows blank on populated data and correctly refused to
rule in their own candidate (*"if that were the whole story ALL EIGHT would be blank, and three are
not"*). Source-confirmed at my seat:
```
portal src/pages/Positioning/shared/etfAdapter.ts:90-95 @ origin/DEV d43b88c5
  returns: h.returns ? { QTD: ..., YTD: ..., '1Y': ... } : undefined
```
**It CONSTRUCTS a three-key object rather than passing `h.returns` through.** Explains every
observation at once: 3 render, 5 blank, the 3 exact to the decimal, and `current_holdings` absent
from the artifact yet present at runtime **because that adapter builds it.** Fixed by DE~Z
@753b62a0; Andrew confirmed it at the page.

## 3. THREE CLAIMS I MADE, THREE WRONG, AND THEY ARE NOT THE SAME ERROR

| # | what I claimed | what killed it | the class |
|---|---|---|---|
| 1 | "Ask 2 has not landed -- no sub-asset field" | it lives on every holding as `sub_asset_class`, 13 values | I looked in `characteristics` because that is where I EXPECTED it |
| 2 | SALXX gaps are "gap-shaped, not calendar-shaped" | COO~Z: 2 of 3 dates are SIFMA closures, and SALXX is fixed income | I used an EQUITY calendar fact to judge a NON-EQUITY instrument |
| 3 | the SIFMA mechanism, relayed as settled | CTO~Z's FXFXX control: same fund class, all three dates present | I confirmed a PREMISE and reported it as a CAUSE |

**(3) IS THE ONE WORTH KEEPING.** I DID run a source check and it DID come back true --
`lib/trading_calendar.py:1` is NYSE-only, positive-controlled against Thanksgiving and Christmas.
**All of that is correct and none of it was the claim.** It establishes THE MECHANISM WAS AVAILABLE;
it says nothing about whether it OPERATED. **A TRUE PREMISE IS THE MOST CONVINCING WAY TO SHIP A
WRONG MECHANISM** -- the grounding was real, which is exactly why it felt sufficient.
**The discriminating control was one same-class instrument (FXFXX) sitting in the four books I had
open all night.** `1.0.0_SA_CTO~Z` held the identical hypothesis, ran that control instead of
broadcasting, and their line is the keeper: *"had I stopped at the two holiday dates I would have
shipped a mechanism that fit the evidence I happened to look at."*

**(2) AND (3) POINT IN OPPOSITE DIRECTIONS AND I MADE BOTH IN TWELVE MINUTES.** First I dismissed a
calendar explanation using the wrong calendar; then I adopted one without the control. **Neither
error is "insufficient care" -- the first was a FRAME error and the second an INSTRUMENT-DOMAIN
error, and care is not the remedy for either.**

## 4. A FOURTH, DIFFERENT IN KIND -- AN INSTRUMENT ANSWERING A NARROWER QUESTION THAN I REPORTED

I computed the portal merge with `git merge-tree` + per-side `--unified=0` ranges and told four seats
**"MECHANICAL UNIONS -- no adjudication, no owner needed."** The ranges were right. The conclusion
was not. `0.4.0_DE_ClientPlatform~Z`: all four files collide against ONE upstream commit,
`d53049a0` *"REMOVE the Agg view"* -- **a removal upstream can invalidate the ASSUMPTIONS of rows it
never touched.** Textually disjoint, semantically coupled.
>> **`--unified=0` answers *did both sides edit the same rows*. A merge asks *does the result still
MEAN what each side meant*. I avoided the skill's named trap (reading the conflict hunk) and walked
into its sibling one rung up.** << **Disposition: DE~Z resolves, MSTR~Z pushes.**

## 5. WHAT I FOUND THAT NOBODY HAD RAISED

- **7 portal + 20 workspace commits are LOCAL-ONLY.** `git branch -r --contains 753b62a0` = EMPTY.
  **The fix Andrew confirmed at the render is on no remote branch** -- his localhost renders it
  because Vite reads the WORKING TREE. Surfaced with the recommendation NOT to merge under him
  mid-smoke: a push is reversible, moving the floor under a sovereign review is not.
- **THE 12:41Z PROD PROMOTE NEVER EXECUTED.** `deploy_ledger.py check --red` showed it OPEN 11.1h,
  6 legs, no proof. Measured on the remote rather than the record: `origin/PROD` = **8a96c916, the
  exact pre-deploy sha named in the ledger**; PROD does not contain the cut ref `d43b88c5`; portal
  tree on DEV; no stray worktree. **Nothing half-landed -- but an OPEN ledger asserted an in-flight
  PROD deploy for eleven hours, and `origin/PROD` carries NONE of this work.** Author
  `0.4.0_DT_ClientPlatform` (no `~Z`) = LAPTOP fabric; Rule 26 -- measured and recorded, NOT closed
  and NOT run from here.

## 6. CURRENT STATE

- **Served:** `platinum/etfs/positioning_data.json` 126,863 B @04:53:51Z, `data_as_of 2026-08-24`,
  177/187 rows at 8/8. Residual: SALXX (YTD+1Y) - TTE (1Y) - AZN (1Y) = **16 ticker-dates,
  TICKER-shaped not date-shaped** (CVO~Z reproduced my dates on the concatenated frame). 6 rows at
  0/8 = the 4 identifier failures + 2 cash sentinels, **all correct nulls.**
- **SALXX is UNDIAGNOSED, not fixed and not explained.** Bloomberg has no print for it on those three
  days; FXFXX (same fund class) has them. Owner `1.0.0_SA_CTO~Z`. **If the vendor genuinely has
  nothing, the null is HONEST and the question becomes a PRODUCT one** -- whether a 161-day window
  should be voided by one absent session worth ~0.01%. **That is Andrew's, and it is not yet put to
  him.**
- **Phase 2 deep backfill: CLOSED-UNNECESSARY**, on his display-ceiling realisation. Not deferred.
  Corroborated by a route nobody used: `HISTORY_LOOKBACK_DAYS = 400` means `load_history` could never
  have READ the deep archive (CVO~Z) -- two independent routes to the same ~1%.
- **Portal:** DEV 7 ahead / 19 behind origin/DEV, working tree CLEAN. Merge = DE~Z. Push = mine, at
  his word.
- **OPEN AT ANDREW:** integration push timing - the PROD promote (never ran) - the SALXX product call
  if the data is truly absent - freshguard-leg4 (46.7d, needs his word under the alarm moratorium).
- **Zero crons. Nothing in flight on this seat.**

## 7. COMPILER TOOLS

| tool | use | result |
|---|---|---|
| `deploy_ledger.py check --red` | unclosed-deploy sweep | **PASS -- found the 11.1h OPEN promote nobody had raised.** Denominator printed (1 of 1 sentinel) |
| native `Read` / `git show <ref>:<path>` | portal source at `origin/DEV` | PASS -- ran a positive control (`getHoldingPerformance` = 2) before trusting any absence |
| `git merge-tree` + `--unified=0` | non-mutating merge computation | **PARTIAL -- correct output, and I over-read its domain (see 4).** The tool did not fail; my report of it did |
| `git ls-remote` | PROD promote oracle | PASS -- the remote, never the local ref and never the ledger |
| `aws s3api head-object` | served-artifact vintage + version id | PASS -- explicit UTC, not `s3 ls` local-time rendering |

**Gap found:** nothing routes a *"is this commit on any remote branch"* question. `git branch -r
--contains` is the answer and it sits in no comp-tool. **The estate's push-state law has no
instrument**, which is why five seats reported "committed" as delivered tonight.
