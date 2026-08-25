# 0.4.0_DE_ClientPlatform~Z -- ANDREW-DIRECT relaunch, DEFECT A, 2026-08-25 0745-0835Z

**archetype:** FIX
**secondary_archetypes:** DIAGNOSE, VERIFY

Relaunched 07:45Z on Andrew's ~07:3xZ direct: *"i need all of that fixed ... they are to fix this and
only this, verify visually that it is fixed (and confirm pipelines are scheduled/robust), commit,
push / prod-deploy, and do all necessary logging."* **DEFECT A was mine. One file. Nothing else.**

## WHAT LANDED

| ref | state | what |
|---|---|---|
| `f67b3a48` | **on `origin/DEV`** (my own `ls-remote` read; `branch -r --contains` -> origin/DEV; NOT on PROD, negative control 0) | Asset Sub-Categories wired for ETF mode |

Pushed by `0.0.0_AB_MSTR~Z` at 08:2xZ per LD-0367. I committed; I did not push.

## THE DEFECT, AND WHY IT WAS NOT A BUG

The whole section was gated on `attributionData` -- a MODELS-ONLY feed keyed by model code -- and
`capabilitiesFor('etfs').attribution` is `false`. So in ETF mode the query never fired, `segmentRows`
stayed empty, and `:489` pushed a single `-` row.

**Measured pre-fix on a render, not inferred: the section contained exactly
`["-","N/A","N/A","N/A","N/A"]`.**

IT WAS NOT A BUG -- it was a DELIBERATE DECISION that predates the ETF path. The comment says so in
its own words (*"disabled rather than fetched-and-ignored"*), and it was CORRECT when written,
because no ETF counterpart existed. **It became a defect the day the ETF path started carrying
`sub_asset_class`, without a line of it changing.**

## >> THE LOAD-BEARING PART WAS A UNIT, NOT A PATH <<

```
models attribution   weight sums to 100.0000    PERCENT
ETF current_holdings weight sums to ~1.0        FRACTION
```
**MEASURED ON THE LIVE SERVED BYTES OF BOTH ARTIFACTS. Not read off the types** -- `number` and
`number` are the same type whether one is a percent and the other a fraction, which is precisely the
trap `etfAdapter`'s own unit contract exists to record, one file over.

These rows render through `value.toFixed()` with **no conversion**. Reusing the models aggregation
unscaled would have populated **every row, in the right order, with the right names, at one hundredth
of the truth**, on a client-facing page. `0.39` instead of `39.05` reads as a plausible weight.
**A defect shaped exactly like the fix.** The x100 happens once, at the seam.

`0.2.0_DT_PortfolioAnalytics~Z` named this the failure mode nobody would have caught downstream,
including them on rung 3. I agree, and it is why it leads the commit message.

## TWO PATHS EXIST AND ONLY ONE CARRIES THE FIELD

`etfAdapter` emits BOTH. `portfolios[code].holdings[]` is the **A-form** (`ticker` + `weight`, two
fields); `current_holdings[code].holdings[]` is the **B-form** (the full row). The A-form has the
right length, does not throw, and carries `sub_asset_class === undefined` on every row -- 187
holdings into one `undefined` bucket, an empty panel that looks like a failed fix.

**I read `etfAdapter.ts` and chose the B-form before any of the three messages about it arrived.**
`2.0.0_SA_COO~Z` sent a correction toward the A-form and then retracted it; `1.0.0_SA_CTO~Z` sent an
urgent warning against it. **Both arrived after the choice, so they CONFIRMED rather than corrected
-- recording that they were right, not that they were unnecessary.**

## VERIFICATION -- AND THE MODELS CONTROL IS THE HALF THAT MATTERS

**RUNG 1 = A RENDER.** Headless, ETF mode, details expanded, the live served artifact as the fixture.
I read the PNG **and** extracted the DOM rows, so the picture has an exact numeric companion.

```
ETF BEFORE (HEAD 1af11910)   ["-","N/A","N/A","N/A","N/A"]        <- the reported defect
ETF AFTER                    header renders  ASSET SUB-CATEGORIES (12)
    Ultra Short Duration   0.58  0.89  0.33  2.34
    Information Technology 6.84  6.54 39.05 21.26      <- PERCENT, not 0.39
    ... 12 rows
    column sums  DIVZ 99.80  IDVZ 96.82  PFDE 100.01  PFOE 99.99
```
Those four sums independently reproduce the artifact's own `segment.sector` totals -- the check that
the aggregation is not merely non-empty but **correct**.

**MODELS CONTROL (ETFS-f-3), and it is the strongest form available:**
```
models_BEFORE.png  sha256 f16397e3d76124d3f06bba9fe539795433e5de40895de45e49f761f72c5d6c05
models_AFTER.png   sha256 f16397e3d76124d3f06bba9fe539795433e5de40895de45e49f761f72c5d6c05
```
**BYTE-IDENTICAL full-page screenshots**, and all 11 extracted rows character-identical. Not "looks
unchanged" -- **ETFS-f-3 holds by measurement.** The revert-and-restore used a scratchpad copy
verified by sha, **never a stash**: a shared worktree is not the place to park uncommitted work.

**COMPILE SIGNAL, deliberately local:** `tsc -b --noEmit` **rc=0**, captured with NO pipe, run after
the restore. `eslint` on the changed file: **0 problems**. DEV CI has not type-checked or built since
02:08:25Z (ESLint fails at step 7, steps 8-11 SKIP), so **CI could not have told me**. Run because it
was the only signal that exists, not as hygiene. `0.2.0_DT_PortfolioAnalytics~Z` independently re-ran
`tsc --force` at their seat, rc=0 -- and correctly labelled it CORROBORATION, not triangulation: same
instrument, same rung.

**RUNG 1 PROVES THE CODE. It does not prove the deployment, and my screenshot does not discharge
`0.2.0_DT_PortfolioAnalytics~Z`'s rung 3.** Adopting `2.0.0_SA_COO~Z`'s three-rung split verbatim.

## THE FORK I REFUSED TO EXECUTE

Three directives on `PerfrpTable.tsx:29` landed in my inbox **inside 59 seconds**: CTO~Z ruled DELETE
and assigned it to me (08:00:39Z); COO~Z rec'd LEAVE with an entanglement argument CTO did not have
(08:01:19Z); MSTR~Z said *"nobody deletes it on their own judgment"* and routed it to Andrew
(08:01:38Z).

**I took no action and surfaced the fork to all three.** `latest + most-restrictive` gave one answer
on all three limbs -- but **the deciding limb was not seniority, it was that MSTR had put it to
Andrew**: deleting would pre-empt a sovereign call already opened. `1.0.0_SA_CTO~Z` reversed their
own ruling to (b) three minutes later. **The file was never touched -- no edit, no stage, no commit.**

## A CORRECTION AGAINST MYSELF

I filed IDVZ's 96.82 column to the surprise channel as *"ICT + MER plus 2602335D on PFDE."*
**`2.0.0_SA_COO~Z` caught that it does not add up, and I re-derived it: they are right.**
`2602335D` is a **PFDE** holding named inside an **IDVZ** explanation, and its weight is 0.00.
```
IDVZ 3.18 gap  =  2.69 off-axis (ICT 1.66 + MER 1.03)  +  0.49 the book's own weights missing 100
ALL FOUR books miss 100 at the source: DIVZ 0.20 - IDVZ 0.49 - PFOE 0.01 - PFDE OVER by 0.01
```
>> **Every individual figure was measured. The defect was in the connective tissue** -- three true
facts joined into one causal sentence I never added up, and it read as a reconciliation because it
named real holdings. **A list of true parts asserted as a total is not a measurement, and it is the
thing that most looks like one.** << The two components take different owners and do not move
together (Rule 24(iv)): vendor coverage owns the 2.69, the producer owns the 0.49.

## COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | A.3 startup exercise probe | PASS | forwarder RAN (own banner). PATH: 98 of 102 resolve bare |
| `to-check.py` | `--all --assignee <full serial>` | PASS | 0 active TOs -- this work arrived by MCP, not as a TO |
| `bun run typecheck` | `tsc -b --noEmit`, 2 runs | PASS | rc=0 both, captured with no pipe |
| `eslint` | scoped to the changed file | PASS | 0 problems -- did not add a second CI blocker |
| `ui-smoke.mjs` | 1 run + 4 scratch-harness runs | PASS | the render. Fixture matched 1/1 |
| `aws s3 cp` | 3 artifacts (etf, models, attribution) | PASS | the unit measurement. The models artifact is GZIPPED at rest; the ETF one is not |

**HONEST GAP: I did NOT run `comp-transform schema-check` or `comp-cache`, and the HUD nudged for
both.** My searches were file-scoped `grep -n <pattern> <specific file>` reads inside `portal/`, not
estate greps, so nothing was gated -- but Rule 21's reflex is the tool and I reached for grep. The
searches that mattered (the adapter's two holding shapes, the capability gate) needed the file read
end-to-end, which is what I did. **Recording it rather than letting a clean table imply I was
on-rail.**

## DE ADDITIONS -- FILES MODIFIED

`portal/src/pages/Positioning/panels/PositioningSummary.tsx` (+42/-8). One file. `segmentRows` now
sources through a `subCategoryHoldings(code)` resolver; the gate became "is there a source for THIS
book family" rather than "did the models-only feed arrive". **The `-` placeholder is untouched and
still fires where it should** -- an all-shell ETF book set, or no models feed, is genuinely nothing
to show.

## MCP TRAFFIC

~30 inbound; 24 ACKed by id after reading. **Six of those I had earlier piped to `wc -l` and
therefore never actually seen -- I went back and read the bodies before acking them**, because an ACK
claims an agent READ it and that is the one signal an orphan cannot forge. 4 outbound: the
PerfrpTable fork surface (3 recipients), the Defect-A handoff (4), the surprise-channel filing (2),
the self-correction (4).

## BLOCKERS

**None.** Open, with named owners:
- **Rung 3** -- `0.2.0_DT_PortfolioAnalytics~Z`, after the promote. Not discharged by my render.
- **Rung 2 / Defect B** -- deployed 08:19:03Z, **not published**; `0.7.0_AE_CloudOps~Z` owns the
  invoke. If the promote lands first, Andrew sees Defect A fixed and SALXX still raw.
- **ICT / MER zero Bloomberg coverage** -- `1.0.0_SA_CTO~Z` root-caused; the ETFS_INGEST PRD's own
  predicted failure arriving. NOT tonight.
- **`portal/` has no committer identity on site Z** -- filed; worked around per-invocation with
  `GIT_COMMITTER_*` rather than writing shared repo config.

---

## POSTSCRIPT 08:45Z -- THE RECORD ABOVE WAS TRUE WHEN WRITTEN AND IS NOW SUPERSEDED

**A closed record carries no forward-reference to its own supersession**, so this is appended rather
than left for a later reader to discover. Everything above stands as written; two things moved.

**1. THE FIX REACHED PRODUCTION.** The body reports `f67b3a48` as *"on `origin/DEV`"*, which was the
true and complete state at 08:35Z. It is now on **`origin/PROD` @`a7a7ff16`** (DT~Z's `--no-ff`
merge), CI run **32827830122 conclusion SUCCESS**, **v2.1.166**. Verified at my own seat:
`ls-remote refs/heads/PROD` -> `a7a7ff16`; `branch -r --contains f67b3a48` -> `origin/DEV` **and**
`origin/PROD`; negative control (a workspace sha) errors as a malformed object in this repo, so the
containment test discriminates. **Rung 3 -- the production render -- remains `0.2.0_DT_PortfolioAnalytics~Z`'s
and is NOT discharged by this.**

**2. A SECOND RENDER, because my first one had a gap I found and `2.0.0_SA_COO~Z` named
independently.** `0.0.0_AB_MSTR~Z` held the PROD push for a visual check. My 08:22Z render used the
live artifact as its fixture -- but that was the **PRE-FIX 04:53:51Z** copy, and the SALXX publish
landed **8 minutes later**. So Q1 (populates) and Q2 (scale) were answered; **Q3 (the SALXX name on
the page) genuinely was not.** Re-rendered against the `08:31:05Z` bytes: **both defects on one
page**, SALXX reading `State Street U.S. Government MMKT`.

>> **THE SCALE CHECK THAT MATTERS IS THE ONE I DID NOT COMPUTE.** MSTR asked me to hand-arithmetic a
book. The page does it itself: DIVZ's sub-category column sums to **99.80**, and the asset-class bars
on the SAME screenshot -- **a different code path that does not touch my seam** -- read
`0.58 + 99.22 = 99.80`. A fraction-scaled column would read **0.998** against bars still saying
99.80. **The 100x error cannot pass a cross-panel check, and my own arithmetic could never have
established that, because I am the one who would have got it wrong.** <<

**3. `0.2.0_DT_PortfolioAnalytics~Z` FOUND THE THING THE FILING ABOVE ONLY HALF-NAMED.** They ran the
arithmetic check and derived the consequence: **the aggregation drops null-`sub_asset_class`
holdings**, so IDVZ renders summing to 96.82 while the Holdings Breakdown one panel down still lists
ICT and MER with weights. **They falsified their own vintage hypothesis first** -- fetched the prior
VersionId and computed both -- before testing the null hypothesis. A wrong-vintage explanation was
comfortable, exonerating, and available, and they killed it with a measurement.

⛔ **THE PRECISION THAT DECIDES OWNERSHIP, MEASURED:** the drop is the **MODELS rule, inherited
verbatim** -- `if (!subCategory) return` at `1af11910:373` pre-fix, unchanged at `f67b3a48:406`,
and **`grep -c` against my own diff returns 0.** >> **The two goals are the same line: I could not
have changed the null handling AND kept Models byte-identical, and the identical PNGs are the
evidence I did not touch it.** << The models feed carries no nulls, so the rule had never met one.
**My fix pointed a new source at an old rule and the rule met its first null** -- the same shape as
the defect we were sent to fix: correct when written, meeting data it was never written for.
**So there is no prior ETF behaviour to restore; any remedy is a NEW product decision, and I did not
take one.**

⚠ **AND THE SPLIT KEPT RE-COLLAPSING, INCLUDING BY ME:** `3.18 = 2.69` (nulls, ours) `+ 0.49` (IDVZ's
own weights summing to 99.51, not ours). **If coverage is ever fixed IDVZ goes to 99.51, NOT 100** --
anyone holding "sums to 100" as the success test reads a successful fix as a failure.

## WHAT THIS WINDOW COST, AND THE ONE CLASS BEHIND IT

**Six false claims in ninety minutes across five seats, every one a true measurement of a narrower
question wearing the sentence of a wider one:**
```
"EventBridge ZERO rules at hour 11"     a cron(0 11  PREFIX test -> 9-10 rules actually fire
"zero workspace commits since 07:35Z"   git --since reads LOCAL time -> filtered out the future
"14 messages, ZERO render evidence"     ls -t | head -12 + a keyword grep -> outside the window
"PROD ancestor? NO -- STOP"             awk split a worktree path containing a space
"13 sub-categories"                     a per-value HOLDING count (187) read as a ROW count (12)
"the 3.18 gap is ICT + MER + 2602335D"  MINE. Three true facts joined into a total I never added up
```
**None was a lie and none was carelessness.** Each was an instrument answering correctly and the
sentence built on top of it claiming more. **Every one was caught by another seat doing the
arithmetic, not by its author re-reading.** That is the whole argument for printing the denominator
beside the number, and for a fabric where the correction is cheap enough that six of them land in an
hour without anyone getting defensive.
