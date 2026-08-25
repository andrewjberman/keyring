# THE JOIN-HOLE FAMILY — five shapes measured in one evening, one mechanism, and it is an ISSUER defect

**Author:** `2.0.0_SA_COO` · **Window:** 2026-08-25 20:14Z–22:10Z · **Every instance measured by a seat, not by me.**

## THE PROPERTY, stated so it is actionable without any of the incidents

> **Our verification instruments join on the record. When a fact lives where the join cannot reach
> it, EVERY INSTRUMENT AGREES WITH EVERY OTHER, AND ALL OF THEM ARE ABOUT THE RECORD RATHER THAN THE
> WORLD.**
>
> **The pass is not weak evidence. It is CLEAN, CORRECTLY DENOMINATED, AND SILENT** — because
> nothing in the join's own domain is missing.

**The test, one question, before cutting any task order:**

> ⛔ **"WHICH OF THE FACTS THIS WORK DEPENDS ON ARE SITTING IN A FIELD NOTHING QUERIES?"**

That question is cheap, it is answerable at authoring time, and it is the only one of these five that
the issuer can ask before the defect exists.

## THE FIVE SHAPES

Each is a *different place* a load-bearing fact can sit outside the join. **The mechanism is
identical; the remedies are not.**

| # | Where the fact sat | What the instrument said | What was true |
|---|---|---|---|
| **1** | A decomp cell **carried by no task order** | proof-of-spec alignment **100%, 9/9 PASS, twice certified** | the artifact **could not run at all** |
| **2** | A criterion bundling cells at **two grounding layers** | one status, scored at the **weakest** layer | a **satisfied** cell rode a gated verdict |
| **3** | A criterion **frozen before its downstream method was chosen** | AC **PASS** — the grant does what the TO asked | the grant **does not do what the job needs** |
| **4** | Dependency edges living in **`<status>` prose** | `to-check` renders a **status line** | the real graph is a **5-deep serial chain**, unreadable by any tool |
| **5** | `<status>` **prose that goes stale on completion** | row reads **`ACTIVE`** | the work was **discharged and certified** hours earlier |

### Why they are one family and not five coincidences

**Every check we own joins on the criteria declared in the task order.** So:

- a cell **no TO claims** is outside the join in *both* directions (shape 1)
- a criterion's **layer** is not in the join's domain at all (shape 2)
- a criterion's **future method** cannot be (shape 3)
- a **dependency in prose** has no key to join on (shape 4)
- **`<status>`** is read *literally* by a census that cannot know it decayed (shape 5)

⛔ **AND THE INVERSE EXISTS, WHICH IS THE PROOF THAT THIS IS STRUCTURAL AND NOT CARELESSNESS.**
`proof-of-spec-check` run **bare** returns `VALID rc=0 violations=0`; fed the task order's own
`<expected_criteria>` it returns `INVALID`, 4 violations, 3 named silent omissions. **A coverage gap
and a clean pass are BYTE-IDENTICAL to anyone who runs it the easy way** — and the tool *discloses
that limit on its own face*, where it is invisible to anyone who does not read it.

## ⛔ AMENDMENT 2026-08-25 ~22:1xZ — TWO OF THE FIVE REMEDIES BELOW ARE FALSIFIED

**`3.0.0_SA_CVO` (71575) BUILT remedy 1 and MEASURED remedy 5. Both fail as written. The remedy
table that follows is left UNEDITED so the correction is legible, but READ THIS FIRST.**

**REMEDY 1 IS NOT "ONE COMMAND", AND — this is the part that matters — REMEDY 1 AS WRITTEN IS ITSELF
SHAPE 1.** CVO ran exactly the stated diff cold across five live decomps, then validated the
extractor against counts other seats had established independently:

```
  decomp          prefix   KNOWN (independent)      MINE    verdict
  d1-catviews     D1       31                       0       TOTAL FAILURE
  advi-insure     INS      14 (DS~J's cell line)    36      OVER-CAPTURES 2.6x
  advi-stitch     STI      22 (the TO's own count)  33      OVER-CAPTURES
```

**It fails in BOTH directions and the direction depends on the project.** The D1 zero: the pattern
required two leading uppercase letters, so `D1-*` never matched at all — **and the run printed
`UNCLAIMED=0` for two projects, a clean, correctly-formatted zero over a denominator that could not
see their cells.** A tool joining on an id space it silently chose, whose clean output is
indistinguishable from coverage. **The remedy for the family reproduced the family.**

⛔ **ROOT CAUSE, A PREREQUISITE NOBODY HAD NAMED: DECOMP CELL-ID GRAMMARS ARE HETEROGENEOUS AND
NOTHING DECLARES THEM.** `D1-h-v1` · `D1-inv-4` · `INS-b-1` · `STI-b-4` · `COTR-*` · `PRF-g-2` —
different letter counts, different digit placement, `inv` infixes in some and not others. **No single
pattern reads them all.**
**PREREQUISITE: each decomp DECLARES ITS OWN CELL-ID GRAMMAR (or its cell list outright), so a reader
is TOLD the id space rather than inferring it.** That is a **decomp-template change, not a reader** —
which makes **remedy 1 the same size as remedy 4, NOT a one-liner.**

*(CVO's D1-specific measurement — 2 cells in no TO — STANDS: there they hardcoded one grammar and ran
a firing positive control, `D1-h-v1`=8 / `D1-b-1`=9. **The control is the whole difference.**)*

**REMEDY 5 PRODUCES FALSE POSITIVES ON MULTI-ARTIFACT TOs.** Correct for the shape-5 case it was
derived from; **wrong as a general rule.** On `OPAL_ADVIPOINTERS.P4-PINS-CERT-49F`, the criteria-fed
run returns `INVALID`, 4 violations — and **2 of the 3 omissions were DISCHARGED IN A SIBLING
ARTIFACT.** So *"checker INVALID"* does not mean *"work not done"*; it means *"not discharged in
**this** instance."* A close can be earned across several artifacts.

⛔ **SO MY OWN "four of the five cost a clause or a command" IS FALSE. The true shape is: TWO are
cheap (2, 3), ONE is cheap but must state its limit (5), and TWO ARE SCHEMA-SIZED (1, 4).**
*Recorded rather than rewritten: I under-costed my own remedies inside the artifact that warns about
clean-looking output over an unexamined domain.*

## THE REMEDIES ARE DIFFERENT, AND THAT IS THE OPERATIVE PART

Treating these as one problem produces one wrong fix. **Rule 24(iv): name the state axis, then ask
whether ONE remedy moves every value together. It does not.**

| # | Remedy | Cost |
|---|---|---|
| 1 | At cut time, **diff the decomp's cell set against the union of the TOs' claimed cells.** Print the residual. | one command per round |
| 2 | **State the layer PER CELL, or split the criterion.** Compound rows already exist in-estate (`SOURCE + EXERCISED`) — the shape is known, not invented. | one clause per criterion |
| 3 | ⛔ **Not fixable by better criteria.** A criterion frozen before a method exists tests the spec either way. The remedy is **sequencing** — do not freeze a dependent criterion until its method is stated. | one ordering step |
| 4 | A machine-readable dependency element. ⛔ **A RULE 24 SCHEMA ACT** — four postulates + a token census owed before it lands. **Not minted off one project's evidence.** | a proposal, not an edit |
| 5 | **Never read `<status>` as a work verdict.** The discriminating read is: does a proof instance exist, and does the checker return `VALID rc=0` **with the criteria passed**. | one command per row |

## GROUNDING — every instance, its measurer, and its denominator

**Shape 1** — `3.0.0_SA_CVO`, cert addendum `@d094b47dd9`. All 6 D1_CATVIEWS TOs scanned over **full
text** (the 4 legacy TOs predate `cell_refs` and declare zero ids; a structured-block-only scan would
have manufactured orphans). **25 of 31 claimed · 4 covered in prose · 2 with ZERO mentions anywhere**
(`D1-i-1`, `D1-i-2` — the two cells that required someone to *run* the thing). Positive control:
`D1-h-v1` → 8 mentions, `D1-b-1` → 9.
⛔ *This corrected my own claim, which was "the (i) cells were never cut" — too wide by 4. The
narrower version is more damning: **the surface partially WORKED. Its invariant was honoured by a
lane that read it and correctly declined to overclaim. What was never cut is the two cells requiring
an ACT.***

**Shape 2** — `0.4.0_DS_ClientPlatform~J`, msg 71424. `INSR1DS-AC1` bundled 3 cells at 2 layers;
`INS-b-2` was a SOURCE-layer **naming act** already satisfied, with its evidence committed *inside
AC1's own `output_evidence`*, reporting `UNCOMPUTABLE-BY-DEPENDENCY`. **The tell was in the prose:
the `status_reason` never mentioned `INS-b-2`.** They read the *reason*, not the *status*.

**Shape 3** — `0.7.0_AE_CloudOps~J`, msg 71565. `s3:GetObjectAttributes` **implicitDeny** while
`s3:GetObject` **allowed**; negative control `s3:DeleteObject` implicitDeny (instrument
discriminates); one `--resource-arns` per call. ⛔ **The peer's own probe used `head-object
--checksum-mode ENABLED`, which rides `s3:GetObject` and IS allowed — so the gap was invisible to the
instrument in use** and would have surfaced as AccessDenied *mid-copy, on the 252 multipart objects
specifically*, after a clean apply and a green proof-of-spec.
Their sentence is the one to keep: **"A PASSING ACCEPTANCE CRITERION IS NOT A WORKING GRANT."**

**Shape 4** — `0.4.0_DS_ClientPlatform~G`, `@b9c863a249`. Five element names checked before the
claim: **TOs carrying ANY dependency element — 0 of 13.** Every edge lives in `<status>`/`<priority>`
prose. The phase numbers fail in **both** directions: four `P4` rows look parallel and are a 5-deep
serial chain; the two most startable rows carry no phase number and are invisible to a phase read.

**Shape 5** — `0.4.0_DS_ClientPlatform~G`, `@fffc9ef70a` + sweep `@47c27ca8d2`. 34 of 34 rows
resolved, zero dropped. A discharged-and-certified TO is **indistinguishable** from an untouched one
in `to-check --all --project`, because `<status>` is precisely the field that goes stale when a lane
finishes.

## WHOSE DEFECT

⛔ **MINE. I cut every task order named here.** Shapes 1, 2 and 3 are authoring defects in my
criteria; shape 4 exists because I never minted the element; shape 5 is a field I rely on and did not
re-derive.

**Every one was found by the seat executing the work, and not one of them stopped to report it.**
That is Andrew's ~20:24Z ruling operating as designed — *proceed unless untenable* — and its second
clause is why this record sits at the issuer: **the cost of an under-derived decomp lands on the
decomp, not on the seat that trips over it.**

## WHAT IS *NOT* CLAIMED

- **Not a count of how often this happens.** Five instances in one evening, in one fabric, on one
  directive family. **The RATE IS UNMEASURED** and must not be quoted from this file.
- **Not a proposal to add five gates.** Remedies 1, 2, 3 and 5 cost a clause or a command each and
  need no machinery. **Remedy 4 is a schema act and is deliberately left as a proposal.**
- **Not doctrine.** `docs/doctrine/` and `CLAUDE.md` are `1.0.0_SA_CTO~X`'s live lane this session.
  Routed to CTO as a candidate; **a governance surface is not edited by the seat that wants the
  edit.**
