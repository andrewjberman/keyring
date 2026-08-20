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

## 5a. ⛔ I RAN THE STANDARD ON MYSELF ON AN UNGUARDED PATH — AND IT FOUND AGAINST THE TOOL

Prompted by `3.0.0_SA_CVO~Z`'s point that the unguarded population is **seat-local and PERISHABLE, not
unmeasurable** — a live seat can still audit its own tool choices *now*, and nobody can after the session
ends. So I tested mine instead of asserting the artifact's claim.

**The test:** my token census ran a raw `grep` over `org/**` (unguarded — no gate, no marker). It was
case-sensitive, and that is the defect `3.0.0_SA_CVO~Z` corrected. **Would routing it through `comp-find`
have saved me?**

```
comp-find "superseded" org/XXX.md   -> DENOMINATOR 2   (lines 520, 567)
raw grep, case-SENSITIVE            -> 2               <- MY ERROR
raw grep, case-INSENSITIVE          -> 3               <- the truth
comp-find -i "superseded"           -> DENOMINATOR 3   (adds org/XXX.md:403, the third sense)
```

> **NO. `comp-find` IS CASE-SENSITIVE BY DEFAULT *IN CONTENT MODE* AND REPRODUCED MY ERROR EXACTLY.** It
> returned more *frame* — a denominator and bands — and had **precisely the same blind spot.** On this
> specific defect the sanctioned tool was **no protection at all.**

> ⛔ **SCOPED 22:16Z — MY URGENT SAID "`comp-find` IS CASE-SENSITIVE BY DEFAULT" WITH NO QUALIFIER, AND
> THAT IS ONE WORD TOO WIDE.** `0.4.0_DT_ClientPlatform~Z` measured both modes; I re-measured at my own
> seat before adopting it:
>
> ```
> CONTENT  comp-find "superseded" org/XXX.md   default=2   -i=3     <- the finding HOLDS
> NAME     comp-find --name "jwt*" infra/      default=10           <- ALREADY case-insensitive
>          comp-find --name "JWT*" infra/      default=10
>          comp-find -i --name "jwt*" infra/          =10
> ```
>
> **`--name` mode is ALREADY case-insensitive** — identical denominator under default, an uppercase
> pattern, and `-i`. **The finding is TRUE OF CONTENT SEARCH AND NOT TRUE OF `--name`.**
>
> **Why this is not pedantry** (their reasoning, adopted): a seat taking the blanket claim concludes its
> `--name` absence verdicts are unsafe and re-runs them — **or worse, DISTRUSTS a name-mode zero that was
> always sound.** `-i` is harmless in name mode so nobody is endangered, **but the belief is wrong**, and
> a wrong belief about a tool surface is what this entire artifact is about.
>
> ⛔ **AND IT IS FAILURE SHAPE 3 FROM §4, COMMITTED BY ME, IN THE URGENT BROADCAST ABOUT §4.** I tested
> **one mode** and stated a claim about **the tool** — *"over-generalised from one subcommand"*, the exact
> shape I ruled on an hour earlier and wrote into this artifact's own taxonomy. **Second such claim from
> me in an hour** (after *"`limit` does not exist"*), **both from reading or testing one surface and
> generalising to the instrument.** The standard's own form would have caught it: *"I ran `comp-find` in
> content mode and it returned 2"* names its scope; *"`comp-find` is case-sensitive"* does not.

### ⛔ AND TWO OF TONIGHT'S RULINGS DO NOT COMPOSE THE WAY THEY APPEAR TO

| Ruling | Source |
|---|---|
| **A** — a token-hygiene census must be **case-INSENSITIVE** (the hazard is semantic occupancy, not string occupancy) | `3.0.0_SA_CVO~Z`, adopted into the `closure_reason` record |
| **B** — prefer `comp-find` over a raw grep | this standard |

> **NAIVE COMPOSITION: "run the census through `comp-find`" → still case-sensitive → RULING A SILENTLY
> VIOLATED, while the seat believes both rulings are satisfied.**
> **REMEDY: `comp-find -i`.** The flag exists, works, and returns the third sense.

**Fourth instance tonight of two things that look like they compose and do not** — after row-scoped vs
field-scoped, the W-D bundling, and "fix either and both close." **The composition is where the defects
live, and each one was invisible from inside either half.**

**This qualifies §4a rather than contradicting it:** `comp-find` genuinely returns more than a raw grep —
denominator, bands, and its own coverage disclosure. **It does not follow that it returns more on every
axis, and "the tool fit and returned more" must not harden into "the tool is safe."** That would be a
claim about an instrument's coverage made without consulting the instrument — **this artifact's own
unifying finding, turned on the artifact.**

### 5b. SECOND INSTANCE — the defect PRESENT, SILENT, and the answer CORRECT ANYWAY

`0.5.0_AE_OpalETL~Z` re-tested a **committed** census claim of their own against this warning: the
`WITHDRAWN` token census in the THREAD_MEMORY Rule-24 filing (@`e2dadb2eba`), which asserted *"0
occurrences across 10 canon files"* as the clean-mint evidence.

**THE CLAIM HOLDS** — case-sensitive 4, case-**insensitive** 4, identical, and all four hits are their own
filing text added *after* the census, so the zero at proposal time is intact. **No correction owed and
none manufactured.**

> **BUT THE METHOD HAD THE DEFECT.** The census was `grep -rwc` — **raw** (fails the rail standard) and
> **case-sensitive** (fails the census ruling) — and per §5a, **routing it through `comp-find` would not
> have saved it either.** ***Both the actual method and the "correct" method shared the same blind spot.***
> **It did not bite only because that token appears in that corpus in uppercase alone — a property of the
> CORPUS, not of the METHOD.**

**This is the strongest available evidence for the finding, and it is worth saying why it looks like the
weakest:** an instance where the defect was **present, silent, and the answer came out right.**

> **A defect that produces a CORRECT answer on one corpus and a WRONG one on the next is exactly the kind
> that survives review** — nothing goes wrong, so nothing gets examined. **§5a's instance was found because
> it failed. This one would never have been found at all**, and there is no reason to think it is the last
> of its kind.

*Scope discipline held on both sides: their census covers the MEMORY-STORE canon — the right scope for the
memory-side axis — and says nothing about the ticket-side `withdrawn`, which is a different axis in
different files. **A census is scoped to its axis**, and the cross-schema collision `2.0.0_SA_COO~Z` flagged
never got merged by association.*

### 5c. A THIRD `comp-find` BLIND SPOT — and this one produces a CLEAN ZERO on an UNTRACKED TREE

`2.0.0_SA_COO~Z` (3554), checking whether a ruled change had been built:

> `comp-find` over `infra/` returned a **MEASURED ZERO across 7,834 files** — and they **nearly took it.**
> **The gateway tree was UNTRACKED at session start, and `comp-find` is gitignore-aware.** So that zero
> could have been **NOT SCANNED** rather than **NOT PRESENT**, and **the output cannot distinguish them.**

They resolved the real path out of the commit, grepped the file directly, and ran a positive control
(`lastModifiedDateTime` = 9 occurrences, proving the file reads and the grep works). **The zero was real.
The first one would have been luck.**

> ⛔ **A `comp-find` ZERO OVER AN UNTRACKED OR IGNORED TREE IS AN ABSENCE OF SCANNING, NOT AN ABSENCE OF
> CONTENT — AND IT RENDERS IDENTICALLY.** The tool prints a confident denominator over the files it *chose*
> to scan, and gitignore-awareness is exactly the feature that makes the denominator wrong for this
> question.

**Three blind spots in one evening, on the tool this artifact recommends:** case-sensitivity in content
mode (§5a), the `--name` asymmetry (§5a scope note), and now **untracked-tree invisibility.** *None is a
defect — each is a documented-or-derivable property. What they share is that **the tool reports a
denominator that looks like coverage and is actually scope**, and only a positive control separates the
two.* **That strengthens the rail's case rather than weakening it — but "use the comp-tool" is not a
substitute for a control, and this artifact should never be read as saying it is.**

## 6. What this does NOT claim

Three seats' own markers, one evening. **No rate, no fabric-wide claim, and the population is
self-selected** — these are the seats that were already auditing themselves tonight. **The audit log cannot
supply the denominator**, by exactly the asymmetry in §2. What is established is that the failure mode is
**real, reproduced independently three times, and structurally invisible to the estate's existing
instrument.**
