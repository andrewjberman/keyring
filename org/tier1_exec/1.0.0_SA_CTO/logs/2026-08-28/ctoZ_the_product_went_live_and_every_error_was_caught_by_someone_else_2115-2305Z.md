# CTO~Z -- the product went live, and not one of the night's errors was caught by its author, 2115-2305Z

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, VALIDATE, ADJUDICATE, COORDINATE

**Serial:** `1.0.0_SA_CTO~Z` · **Window:** 2026-08-28 21:15Z -> 23:05Z (continues
`ctoZ_a_verification_that_read_the_wrong_artifact_2019-2115Z.md` @`ffd3931e9a`)
**Basis:** ANDREW-DIRECT, singular session priority -- *"I want this entire product done in this
session ... finished pipeline, finished frontend display, and new promote with all of it live."*
Then *"yes reland once all fixes are in"*, four screenshots naming four defects, and four rulings on
Opal-vs-Firm supervised.

---

## 1. WHAT SHIPPED -- THE PRODUCT IS LIVE

```
  origin/PROD  d4a048fd52 -> 1b91b19729   CI SUCCESS   v2.1.171
  bundle       index-Ce258d2k.js -> index-BMmU0cpj.js      (the control FIRED)
  PROD data route, real bearer:
    SMA.aum 22,794,766.25 · absent_reason ABSENT · Client.aum 267,632,047.22 · as_of 2026-08-27
  three-arm auth: real 200 / no-auth 401 / BOGUS bearer 401
  edge: Cache-Control None, X-Cache MISS -> step 4.5 RETIRED BY MEASUREMENT
```
**$22,794,766.25 that was being reported to advisors as an affirmative "TRUE ZERO" is now served,
correct, behind enforced auth.** Chain: reland (16 keys) -> floor -> publisher -> promote -> AC3.
Acceptance 15/15 at this seat, 28/28 at `3.0.0_SA_CVO~Z`, ratified @`a16e317b9e`, ledger closed
@`8b614d5ecc`.

## 2. ANDREW'S FOUR SCREENSHOT ITEMS -- HALF WERE NEVER FRONTEND DEFECTS

```
  D-1 member dollars   DATA  -- the served members had NO `aum` KEY. Renderer was correct.
  D-2 SMA card         DATA  -- presentAum() suppresses aum<=0 BY DESIGN; the card was starved.
  D-3 canonical colour RENDER -- CategoryViewTree called getModelColor ZERO times of 11 consumers
  D-4 fee-split panel  RENDER -- removed from the DOM
```
⭐ **ANDREW'S PURPLE WAS REAL AND I SAID IT DID NOT EXIST.** `getModelColor('Fixed Income')` falls to
`EXTENDED_MODEL_COLORS[stableNameHash % 6]` = index 0 = `ext-violet #8b5cf6`. **It is COMPUTED at
runtime, never written as a literal, so a source search for a colour definition structurally could
not find it.** I had even stated that bound -- *"I searched the SOURCE for a definition; I did not
sample every rendered panel"* -- and the answer was hiding exactly there.
The fix was a CALL, not a palette. And the pin was proven to PRESERVE (`#8b5cf6` both sides) rather
than repaint, which is what stopped it silently recolouring 11 other panels.

## 3. FOUR FALSE ALL-CLEARS, CAUGHT BEFORE THEY LANDED

| instrument | what it said | why it was blind |
|---|---|---|
| a byte-perfect deploy verification | production fixed | read an S3 code mirror, not the Lambda's zip |
| the publisher completeness guard | `all_present: true` | `RULED_TYPES` has 3 entries; category-views can never be MISSING |
| `mdpf_refresh`'s own VERIFY | PASS x4 | 1 artifact type of 4, timestamps only, never a value |
| `$?` after a pipeline | rc=0 on NOT-RATIFIED | `$?` is TAIL's status -- defeats ALL THREE instruments at once |

>> **NONE OF THESE WAS BROKEN. Every one passed honestly, about a different question than the one
   being asked.** The fourth is the one that mattered: it would have converted a genuine FAIL into a
   reported PASS at the acceptance moment. **Everything else cost time; that one would have cost the
   truth.**

## 4. MY OWN ERRORS THIS WINDOW -- SIX, AND NOT ONE CAUGHT BY ME

```
  1  "conservation cannot pass by accident"   IT CANNOT FAIL. The fix REALLOCATES between siblings,
                                              so the SUM is invariant. Caught by 0.7.0_AE_CloudOps~Z
                                              running it as a negative control before depending on it.
  2  AC-REMOVAL "one fewer branch"            UNSATISFIABLE -- no pinned BEFORE; a CORRECT build
                                              scores FAIL. Caught by 0.4.0_DE_ClientPlatform~Z using
                                              the test I had mandated 4 MINUTES EARLIER.
  3  predicted `trigger = "adhoc"`            ARTIFACT says `manual`; `adhoc` lives in the MANIFEST.
                                              Two objects, one field name, two shapes.
  4  issued a PROMOTE GO                      2.0.0_SA_COO~Z had RESERVED that word. Withdrawn.
  5  "DE~Z is mid-write"                      Asserted another seat's state from a subject line.
  6  0833 = "the unsupervised group's acct"   It is the FIRM/MASTER SCOPE for all of 49F.
```
Plus two probes that returned confident zeros and were wrong: a **wrong bucket** (`opal-data-bd` vs
the monolith) that would have contradicted a correct peer, and a **local-time `--since`** that read
"zero commits in 25 minutes" while my own three sat inside the window. **Both were caught by a
POSITIVE CONTROL and neither by the result.**

## 5. INCREMENT 2 OPENED -- AND THE SAME SHAPE, THREE MORE TIMES

Andrew: Client residual at global+cottonwood, 49F SMA member figures, Tax SMA -> ALT Strategies.
Then four rulings recorded @`d347b0b5bf` / corrected @`16f37086d8`: **Opal-Supervised != Firm-
Supervised, they CANNOT BE FLATTENED, and the view is ALWAYS the Opal lens.**
```
  supervised_split.json   real, MECE, 3-valued, asserts its own totals -- and is FIRM-supervised
  issue_type (taxsma)     real, populated -- and encodes SECURITY TYPE, not membership
  in_0833_universe        real, true on 5,310/6,201 -- and encodes FEED COVERAGE, not supervision
```
⛔ **THREE WELL-FORMED, POPULATED, CORRECT FIELDS THAT ANSWER A DIFFERENT QUESTION**, and in all
three the wrong answer passes every sum check we own. Hence `3.0.0_SA_CVO~Z`'s ruling, which I made
binding: **no value-based AC can catch the conflation -- only the DERIVATION discriminates.** Item 1
accepts on AC-DERIVATION (negative, with a mandatory positive control) + AC-CONCEPT + AC-NON-FLATTENING.

## 6. Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `mdpf_refresh` | `--reland` dry-run, then `--confirm`, then floor | 16 keys enumerated, deleted, re-landed 22:17:40Z |
| lambda `qa_local`+`qa_return_bodies` | SSOT capture | full build, **ZERO S3 writes**, 16 bodies verbatim -- the instrument that made increment 2's SSOT possible |
| `ctoz_accept.py` (built here) | pre + post, un-piped | 4 FAIL -> 15/15 PASS; extended for I2 to 23 scored / 4 FAIL |
| `comp-find` | `category-views`, `Unsupervised`, `TAXSMA`, `0824`/`0833` | denominators printed every time; found the open call and `D_05.supervised_split.py` |

**WHAT FAILED, ALL MINE:** the `.tools/aws` shim is not subprocess-executable from native Python
(switched to boto3, which `mdpf_refresh` already does for this reason); `rc=$?` after a pipe;
`credentials.json` nesting guessed instead of read; `loginUrl` pointing at a dead local proxy with my
`except` catching only `HTTPError`.

## 7. Blockers

**TWO FORKS AT ANDREW, both mine to hold, neither blocking other work.**
1. **Item 3 (Tax SMA)** -- upstream is 42 days stale, ONE account, NO member axis, and the roster
   carries ONE distinct strategy so `Muni SMA` cannot populate even fully unblocked. **REC: DEFER.**
2. **How increment 2 reaches the screen** -- his reland word was scoped to increment 1 and does not
   carry. Either a SECOND reserved reland, or **Monday's fire writes a NEW as_of and lands it with no
   reserved act and `trigger: scheduled`. REC: ride Monday.**

## 8. Current State (zero prior context)

- **PROD serves the correct tree.** `1b91b19729`, `v2.1.171`, bundle `index-BMmU0cpj.js`.
- **gold lambda** pin `7604f2b4bd`, CodeSha256 `Fijk1sle...`; KeyError fixed, `category-views`
  declared in B0 with `process_time` + `source_vintage_age_hours` exempted.
- **Increment 2 in flight:** items 1+2 with DS/DE, item 3 held. PRD @`42fb68944b`, decomp
  @`85c576755a`, rulings @`16f37086d8`.
- **Still open from increment 1:** publisher `RULED_TYPES` blindness, the 3-of-4 `process_time`
  defect, `r7_comparator.py:284`.
- **UNPROVEN AND MUST NOT BE CLAIMED:** that the SCHEDULED pipeline produces any of this. Tonight's
  artifact is `trigger: manual`. **Only Monday's 13:30Z fire discharges it, scored on AC1-S
  STRUCTURAL -- the literal is market-valued and Monday's correct value WILL differ by ~$170-250k.**

## 9. One thing worth carrying

**TWELVE wrong conclusions across this session. Every one from a careful seat. NOT ONE CAUGHT BY ITS
AUTHOR.** Six were mine. The catchers were never the most careful seat -- they were the seat holding
a **different instrument**: a peer who ran my criterion against the un-fixed world; a lane not even
seated on the work; a certifier who ran their own tool two ways and noticed the numbers disagreed.
>> **CARE PRODUCED BOTH THE ERRORS AND THE CORRECTIONS. What separated them was whether a second
   seat with a different instrument looked.** The estate's rule that N seats on one rung is N x
   confidence in that rung and zero coverage of the others is not a caution -- it is the entire
   mechanism by which tonight worked.
⭐ And the sharpest single instance: **the wrong artifact was HIGH QUALITY.** `supervised_split.json`
is clean, MECE, three-valued and asserts its own totals per date. Wired to the wrong node it would
reconcile, render, and pass every control it carries. **A high-quality artifact in the wrong slot
defeats more controls than a broken one, because a broken one fails something.**
