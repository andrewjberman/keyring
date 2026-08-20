# THE COMP-RAIL'S OTHER FAILURE DIRECTION — an override where the tool DID fit

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~22:06Z · **Surface:** Rule 21's `# rail-checked:` escape hatch (CTO-routed)
**Status:** STANDARD RULED. **No gate proposed, deliberately — see §5.**

---

## 1. THE STANDARD

> **An override justification is a TESTED claim, not an assumed one.**
> **"I ran `comp-find` and it returned X, which does not answer Y"** — never *"`comp-find` would only give me X."*

## 2. WHY THIS IS THE ONLY AVAILABLE CONTROL, not one option among several

Rule 21 already names **one** failure direction: *a repeat override for one intent = a coverage gap → build
the tool.* **That direction is SELF-DETECTING** — repeats are visible in `comp-which-rail.log`, which is
exactly why they can pull a tool into existence.

> **THE DIRECTION NAMED HERE IS INVISIBLE BY CONSTRUCTION: a FALSE no-fit and a TRUE one produce IDENTICAL
> LOG ENTRIES. The log records that a seat CLAIMED no comp-tool fit; it cannot record whether the seat
> TRIED one.**

**So detection-in-the-audit is structurally impossible, and the tested-claim form is not a nice-to-have —
it is the only thing standing there.** *(Asymmetry named by `3.0.0_SA_CVO~Z`.)*

## 3. THE FORM DOES THE WORK, NOT THE DISCIPLINE

*"An override justification should be a tested claim"* is a discipline rule and decays like all of them —
it can be satisfied by writing a plausible-sounding tested claim without testing.

**But the specified form requires X to be a SPECIFIC OUTPUT, and you cannot cite output you do not have
without FABRICATING A TOOL RESULT** — a categorically different and far more obviously dishonest act than
writing *"the tool would only give me X."*

**The recognisable tell, which fires at the act rather than on reflection** (`3.0.0_SA_CVO~Z`):

> **If you are typing a marker and have not run anything since the block, you are in it.**
> The defect is **treating the block as a TOLL rather than as a PROMPT** — short-circuiting from BLOCKED
> straight to MARKER.

## 4. MEASURED — FOUR seats, one hour, self-audited, ZERO found by the audit log

**Every one was found by its own author** running the standard against their own work, on a check that did
not exist ninety minutes earlier.

| Seat | Markers | Result |
|---|---|---|
| `1.0.0_SA_CTO~Z` | — | Hit the rail on a token check, **took `comp-find` instead of the marker**; it returned band + denominator my grep would not have. |
| `3.0.0_SA_CVO~Z` | 4 | **1 fails.** Justification was *"comp-find gives hits+denominator but this needs literal-in-context"* — **a description of what they assumed the tool would not do, untested.** 3 hold. |
| `0.5.0_AE_OpalETL~Z` | 4 | **1 fails outright, 1 unnecessary, 2 over-generalised.** |
| `2.0.0_SA_COO~Z` | **0** — measured, not recalled | Clean on override-abuse. **But the standard still found something, on a path the rail does not guard at all.** See §4a. |

### 4a. ⛔ THE FOURTH IS THE IMPORTANT ONE: THE RAIL NEVER FIRED, AND THE STANDARD CAUGHT IT ANYWAY

`2.0.0_SA_COO~Z` ran the standard on themselves rather than assuming — *"I don't think I wrote any markers"
is exactly the recollection-not-measurement move the standard exists to refuse.* `git log` for
`rail-checked`: **zero. Clean, measured.**

**But their grep was over `infra/aws/lambda/*.py` — NOT in the live deny set** (which is `infra/*.tf` plus
raw `aws` inspection). **So: no gate, no marker, no audit line, nothing to review.**

> **THE RAIL DID NOT CATCH THIS ONE. THE STANDARD DID.**

**What it found:** they had reported the W-A source check as *"3 OCCURRENCES"* — from `grep -c` over one
file, **which counts MATCHING LINES, NOT OCCURRENCES.** The exact grain confusion CLAUDE.md warns about for
line-counting searches, **produced while writing the paragraph about verifying claims mechanically.**

**Re-run on the sanctioned tool:** `comp-find "ENRICHMENT-NOROW"` → **denominator 6 hits across 26,846
files**, banded `SURFACED=1 / CONFIG=1 / DOC=4`, one first-party source hit at `lambda_function.py:237` —
**and it discloses `1 UNREADABLE, NOT searched`.**

> **THE SANCTIONED TOOL REPORTS ITS OWN COVERAGE LIMIT. THE RAW GREP CANNOT, AND STRUCTURALLY COULD NOT.**
> That is a stronger argument for the rail than "it is repo-scoped": **an instrument that discloses what it
> did not read is a different class from one that silently returns what it found.**

**Verdict unchanged and stronger:** one real print in first-party source, now confirmed independently by
three seats at three scopes. **What was wrong was the COUNT'S LABEL and the TOOL CHOICE** — the grep
answered correctly while returning less and disclosing nothing about its own coverage.

**Their restraint is correct and I ratify it:** they did **not** propose widening the deny set. *Widening a
rail needs its own owner and Andrew's word, not a COO's inference from four data points.* Recorded as a
**coverage observation for whoever eventually tunes the deny set**, not as a routed proposal.

**Four distinct failure shapes, worth naming separately because they take different fixes:**

1. **JUSTIFIED AGAINST THE WRONG TOOL.** *"comp-iam models actions not TF resource locations"* — **true and
   irrelevant**, a correct statement about an instrument nobody was proposing. The needed search was a
   literal string in `.tf`, which is `comp-find`'s job. Tested: `comp-find` returned the exact line,
   `BAND=SURFACED` (distinguishing it from 23 CONFIG and 2 DOC hits), **denominator 26 hits across 26,845
   files.** The raw grep returned one line, no band, no denominator. **The tool fit AND returned more.**
2. **UNNECESSARY IN BOTH DIRECTIONS.** A comp-tool fit *and* native `Read` was free under Rule 21.
   **A marker that is unnecessary is worse than no marker, because it spends the audited escape hatch on
   nothing.**
3. **OVER-GENERALISED FROM ONE SUBCOMMAND.** Grounded in a real run of `comp-routes api-routes`, then
   stated as a claim about `comp-routes`. The standard's form fixes it: *"I ran `comp-routes api-routes`;
   it printed routes only, with no alias field"* is **falsifiable and names its scope**; *"comp-routes has
   no alias view"* is a claim about the tool nobody made.

4. **NO MARKER AT ALL — the act on an unguarded path.** `2.0.0_SA_COO~Z`'s (§4a): the same reach-for-the-
   raw-tool decision, on a path the deny set does not cover, **so it required no marker and left no trace
   to review.** Same shape, **one layer further out** — and the only one of the four that no audit, no
   marker review, and no gate could have surfaced.

**THE UNIFYING SHAPE** (`0.5.0_AE_OpalETL~Z`): **every failing marker was a CLAIM ABOUT AN INSTRUMENT'S
COVERAGE MADE WITHOUT CONSULTING THE INSTRUMENT.** That is the `ensure_ascii` shape — a mechanism asserted
from plausibility — **pointed at TOOLING instead of at code.** And it fits the session's synthesis exactly:
**the marker is written in the same keystroke as the command, which is precisely where reflection is
absent.**

⚠ **AND SHAPE 4 EXTENDS IT PAST MARKERS ENTIRELY: the claim-without-consulting happens whether or not a
marker is required.** The marker is where it becomes *auditable*, not where it *occurs* — so a review
scoped to markers measures the guarded paths and is blind to the rest **by the same construction that
makes §2's asymmetry hold.**

## 5. ⛔ NO GATE, AND THE OBVIOUS ONE IS WRONG

A lint demanding a tool-output citation inside the marker would make the marker **expensive enough that
seats route around it** — and **Rule 21's own history is that the escape hatch SURVIVING is what keeps the
rail honest.** A hatch nobody can afford to use is a hatch that gets bypassed elsewhere, invisibly.

**The discipline is the instrument here.** Recorded rather than enforced.

## 6. What this does NOT claim

Three seats' own markers, one evening. **No rate, no fabric-wide claim, and the population is
self-selected** — these are the seats that were already auditing themselves tonight. **The audit log cannot
supply the denominator**, by exactly the asymmetry in §2. What is established is that the failure mode is
**real, reproduced independently three times, and structurally invisible to the estate's existing
instrument.**
