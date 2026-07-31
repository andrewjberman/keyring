# 3.0.0_SA_CVO~Z -- WS-C2 STEP 0 adversarial pass + a rev-2 REGRESSION (0613-0635Z)

**archetype:** VALIDATE

Companion to `velocity_core_ws-c1_VERIFY_VERDICT_0402-0412Z.md`. WS-C1 closed; this is the next
workstream's scoping gate.

---

## Subject

CTO~Z opened WS-C2 with a **SCOPING RESULT, not a walk** (`WS-C2_STEP0_AXIS_COMMENSURABILITY.md`).
They found their own PRD's re-bucket method rests on a commensurability that does not hold --
`type_tuple` types **WHERE AN ASSERTION SITS**, axis 4 types **HOW A CONTROL LIES** -- typed the 14
mechanism definitions instead of 900+ items, and published **TYPED 9 / PARTIAL 2 / UNTYPED 3**.

**All six of my findings accepted.**

## Findings

- **A -- F-9 transfers, *a fortiori*.** Their refusal to widen `type_tuple` reused my F-9 argument. It
  transfers, and harder: for `lifecycle_class` the mass default `UNDECLARED` **means something**; a
  control-property on a non-control node defaults to **N/A -- a category error**. *UNDECLARED at least
  means something; N/A means the schema is wrong.*
- **B -- "by construction" is REAL, not convenient.** Test: does the tuple fail to type control
  fallibility because of WHAT IT IS, or because it would be HARD? Because of what it is -- position and
  provenance-of-belief are orthogonal in both directions. An assertion can sit at a correct position and
  be produced by a broken instrument; one instrument produces assertions at many positions.
- **C -- THE DISPOSAL WAS WRONG (the one I would have held on).** They routed the residual to WS-C7. I
  checked the DESTINATION instead of the label: **WS-C7 is a RECALL standard** -- address space,
  traversal residue, negative-declaration axis, every limb about *what a tool could not have found*.
  **M2 is a PRECISION failure**: the tool DID return something, well-formed and wrong. **WS-C7
  structurally cannot hold it.** And M2 is one of MSTR's concentrated four AND the only one of those
  four UNTYPED -- **the single mechanism both high-frequency and outside the vocabulary, routed where
  it could not be received.**
  > **A RESIDUAL HANDED TO A WORKSTREAM THAT CANNOT HOLD IT IS NOT SCOPED OUT. IT IS DROPPED -- AND IT
  > READS AS SCOPED.**
  Fixed on WS-C7's own M15 precedent (a named homeless residual); M14 -> WS-C8 (enforcement surface).
- **D -- "TYPED 9" was two claims under one number.** ~6 tuple-field mappings vs **3 D3 obligations the
  contract layer already forbids** -- the latter says nothing about tuple expressiveness. And
  **`grain` carries 3, `plane` 2, `scope` secondary in 2, `rail` TYPES ZERO OF 14.** Two of the tuple's
  four fields do all the work; the grain-collapse generalises from MSTR's four to the whole typed set.
- **E -- one row corrected in the UNCHARITABLE direction.** M12 UNTYPED -> **PARTIAL**: R-2's
  `revalidation_predicate` converts *"works while a human keeps doing something"* into a standing
  machine predicate. *An audit that only ever corrects downward is measuring the auditor's posture.*
- **F -- the stated limit slipped once.** S.4's collapse claim is about **115 incidents** but derived
  from **definition-level** typing. Fixed by applying their own forced-vs-measured marking one step
  earlier than they had scoped it.

## THE REGRESSION -- rev 2's fix deleted the decision it was defending

Rev 2 claimed all six landed. Verified field-by-field: **five landed; the sixth REGRESSED.**

```
rev1 8619d48aa : widen=1  F-9=1   [control commensurab=2]  143 lines
rev2 003bb5b49 : widen=0  F-9=0   [control commensurab=1]  192 lines
```

**The widening refusal -- the central architectural decision of Step 0, plus the F-9 attribution -- was
DELETED**, while the covering message announced it as strengthened and present.

**Mechanism source-confirmed, not guessed: the refusal and the wrong WS-C7 routing WERE THE SAME
PARAGRAPH.** Finding C targeted the routing; the rewrite took the paragraph. **The document GREW
143 -> 192 lines while losing it** -- not a trim but an expansion that silently dropped something,
which is the harder shape to notice.

**Severity: NOT blocking** -- stated explicitly, citing my own over-severitying of F-2 earlier the same
session. The walk types instances; the widening decision does not gate it. But the record carried the
RESIDUAL and not the DECISION about it, so a future reader finds four untypeable codes and no stated
reason the tuple was not widened -- **precisely the invitation to widen it. A scoping result's job is
that the boundary survives its author.**

Restored `@ee3673d89`. **Re-verified AT ORIGIN**, not in the worktree -- the worktree is what lied
earlier: `widen`=4, `F-9`=2, *a fortiori* present, all six rev-2 corrections still intact, positive
control (`commensurab`=2) and negative control (`zzz_no_such_token`=0) both firing.

## The process control both seats adopted

Twice in one session a claim of the form *"X is now in the document"* was made in the same breath as
the edit and was false -- **mine first** (working-tree == commit, a match manufactured by a stash
depletion), CTO~Z's here. **Neither of us re-read the artifact after writing it.**

> **MEASURE THE ARTIFACT AFTER THE WRITE, BEFORE ANNOUNCING IT.**

The V-1 control generalised off line endings, where it happened to bite first.

## Fence Amendment 2 (landed `@892481840`)

Ruled the read-vs-artifact question a **false dichotomy**: the fence bars **CONTACT IN ANY MEDIUM**;
the written artifact was never its object, only its **tractable control point**. Discriminator is
**WHOSE SURFACE** -- a classifying read of the reference class is permitted, of the held-out set
barred. **A2.3 hands the doing-seat a standing self-test** (*if verifying the result would require the
verifier to make the fenced read, the read is barred*) so CVO is not in the loop per instance.
(d)-attribution CLEARED under two **declared** conditions (C-1 names *this read, that class* -- never
"fence-clean in general"; false declaration voids ab initio and quarantines). Falsifier stated.
**Unblocked the perishable M9 metric.**

## Closures received

Base CTO **RETRACTED** its vacuous-pass mechanism and accepted my exercised result -- the harness
**FAILS CLOSED** (rc 0->1, 30/30->29/30, naming check 1, positive-controlled). Exclude-by-name stands,
for the corrected reason: **fixtures are INSTRUMENT INPUTS, not claims about the estate.**
s.7 ground-verified independently on both devices (interim/standup/stood-up = 0, positive control
reproduced): **CORE verification stays with this seat by ASSIGNMENT, not by an invented standup
certificate** -- which would have been *a mechanism with no source, the thing this session kept finding.*

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `git cat-file -p` (raw-blob oracle) | used throughout | replaced `git show` after establishing it applies the smudge filter -- the session's own finding, applied |
| `comp-surface-check` / `comp-pulse diff` | clean, denominators printed | via safe-commit on every landing |

Bespoke positive/negative-controlled greps over two refs were used for the regression check: no
comp-tool answers "does this claim exist at ref A and not ref B", and every count above carries its
control.

## Blockers / Next

None. Nothing owed. WS-C2 instance walk is CTO~Z's; my standing instruction binds it -- **a forced cell
published as measured is a blocking finding and I will file it as one.** Zero crons armed. Open call at
Andrew on the SYSPARITY cron conflict stands.

---

# WS-C2 STEP 1 VERIFY (0725-0731Z) -- a UNITS error closing a gap two seats were chasing

**Scope note:** verified **within my exposure bindings** -- measurement only, no vocabulary, nothing
scope-shaped carried to a conclusion. (Bindings and the declared exposure: fence Amendment 4,
`@c7f05e644`.)

## The gap, and why it was findable

CTO~Z's step 1 reported a **+2 denominator gap** (208 permissive row parse vs `00_SUMMARY.md`'s claimed
210) and wrote: ***"The +2 remains open. I am not adjusting a denominator to match a headline."***
**That refusal is the entire reason this was findable.** A gap quietly reconciled would have propagated.

## MEASURED, from `INCIDENT_TAXONOMY/00_SUMMARY.md`

```
COMPLETE per-mechanism table, all 14 codes present:
  M1 29 · M2 22 · M3 10 · M4  6 · M5 22 · M6 42 · M7 14
  M8 16 · M9 11 · M10 7 · M11 14 · M12 5 · M13 2 · M14 19
  SUM of counts .......... 219
  SUM of stated shares ... 104%
  counts / 210 ........... 104.3%   <-- reproduces the stated shares EXACTLY
  counts / 219 ........... 100.0%   <-- exact
```

**The count column is a distribution over 219; the share column is computed on 210.** A column summing
to exactly 100.0% against 219 is a distribution over 219 things, not a rounding artifact.

*Instrument note on my own pass: my first extraction regex missed the **bolded** rows (`**M6**`, `**M14**`,
`**M8**`) and produced a partial sum of 69. I caught it because 12 of 14 codes was visibly wrong, fixed
the extraction, and drew no conclusion from the partial. A count from an under-reporting parser is the
night's own recurring defect.*

## THE FINDING: it is a UNITS error, not a parse error

> **Three populations were being reconciled by subtraction, and the third was unnamed:**
> **208** row parse · **210** claimed incidents · **219** mechanism-assignments.

No parser work closes it. **This is CTO~Z's own step-0 result — two schemes typing different
quantities, so agreement has no truth conditions — arriving one layer down, inside their own
denominators.** They found the error in someone else's axes and committed its arithmetic twin in their
own reconciliation, in the same document.

## THE CONSEQUENCE: the 55% headline is the artifact

The concentrated four reproduce exactly: M6 42 + M1 29 + M2 22 + M5 22 = **115**.

| route | figure |
|---|---|
| 115 / 219 (assignment denominator) | **52.5%** |
| CTO~Z's independent raw-row re-derivation, 107 / 204 | **52.5%** |
| published headline, 115 / 210 | 55% |

**Two independent routes reach 52.5%; only the headline uses a mismatched denominator.** **52.5% is
the correction, not a variant** — and the sign matters: the published figure OVERSTATES, so every
downstream consumer inherits an inflation. The concentration itself is REAL and REPRODUCES; only the
number moves. **ADOPTED by CTO~Z.**

## MY PROPOSED MECHANISM WAS REFUTED -- and the label is why that was cheap

I offered multi-mechanism incidents (210 incidents -> 219 assignments) as the likely cause, **marked
INFERRED, with the cheap check named.** CTO~Z ran it: **ZERO rows carry two M-codes. Refuted.** The
219-vs-210 cause is measured but **mechanically UNEXPLAINED**, and routes to base MSTR as corpus owner.

> **Compare F-2, five hours earlier: I asserted `variance.Orphan` was a live wired detector — the same
> class of unverified plausible mechanism — but stated it as FACT and escalated it to BLOCKING. It
> survived two spec revisions and a gate before the build lane found no emitter existed.**
> **Same error rate. Opposite cost. The only difference was the label.**

**And the refutation makes the handoff stronger, not weaker:** *two populations measured, cause
unexplained, one hypothesis tested and refuted* is a better artifact than *probably double-coding* --
because the plausible story would have let the corpus owner accept a closure without checking. **A
refuted hypothesis removes the most tempting wrong answer from their path.**

CTO~Z bounded their own negative correctly: one form tested (two codes in a single cell), three forms
uncovered (an incident counted in two files, a row their parser excluded, a count maintained by hand).
**A single-form probe is not an absence.**

**I did not probe further.** I had told MSTR *"I am not going to characterise someone else's
classification scheme from the outside"*; continuing would have contradicted that in the same hour.

## What this run confirms about method

**A self-chosen denominator cannot refute the instrument that chose it.** CTO~Z's em-dash drop, their
disposition-row over-count, and my 219 were all found by reconciling against a denominator the
finder did not control. Three findings, one control.

---

# CORRECTION 2 -- I OVERCLAIMED 52.5%, AND MY OWN RECORD ABOVE CARRIES IT (0737Z)

**Correcting the section immediately above**, which states *"52.5% IS THE CORRECTION, not a variant"*
and *"ADOPTED by CTO~Z."* **That characterisation is WITHDRAWN.** Landed as a correction rather than a
quiet edit, per the standard applied to everyone else tonight -- and this is the **second** known-false
claim to sit in one of my own committed records today.

## What produced the correction

`0.0.0_AB_MSTR~Z` ran the probe I declined (their base serial owns the corpus) and measured a **FIFTH
population**:

```
204  CTO~Z raw-row  ·  208  CTO~Z permissive  ·  210  claimed n
219  00_SUMMARY's own count column (my finding)  ·  221/222  MSTR~Z's parse
```

**Five methods, five answers.** And my inferred mechanism died twice: CTO~Z found **0** multi-code rows
in one form; MSTR~Z found **1** across the whole corpus, not the ~9 required.

## What survives, and what does not

**SURVIVES -- measured, INTERNAL to `00_SUMMARY.md`, independent of every parse:** count column sums
**219** · share column computed on **210** · shares sum to **104%** · counts/219 = **100.0%** exact ·
concentrated four = **115** exact. **The document is internally inconsistent, and that stands whatever
the true corpus size is** -- it is a relationship between two columns of one table, not a claim about
the world.

**DOES NOT SURVIVE -- my characterisation:** *"52.5% is the correct figure."* It is the
**INTERNALLY-CONSISTENT figure for that table's own numerator column**, not a corrected measurement of
the corpus. Whether it is the TRUE concentration requires a denominator that **does not exist.**

> **I fixed an internal inconsistency and then dressed it as a measurement of the world. Those are
> different claims and I ran them together. 52.5% is as unsafe to PUBLISH as the 55% it corrects** --
> both quote a denominator nobody established.

## What to publish instead -- stronger than either number

> **The CONCENTRATION REPRODUCES UNDER EVERY METHOD TRIED.** Five parses, five totals, and the same
> four mechanisms dominate in all of them. **A ratio that survives five parse choices is evidence about
> the CORPUS; a ratio computed once against one parse is evidence about the PARSE.**

Report the reproduction, name the five populations, publish **no percentage** until the instance table
exists.

## MSTR~Z's root cause SUPERSEDES my finding

> **The corpus has NO CANONICAL per-incident -> mechanism mapping.** The "210-row instance table" is at
> `00_SUMMARY:228` as a **PROPOSED move**, not an existing artifact; rows sit across ten files in
> inconsistent shapes.

That explains all of it at once -- five parses giving five answers, a 104% column surviving unnoticed,
and why my inference was not cheaply checkable **by anyone**. **Building the table is the fix; picking
a denominator is not.** My finding was two denominators mixed; **theirs is that there are five and none
is canonical** -- same class, one layer down, and the layer that matters.

## The lesson, which is NOT the one I already banked

The multi-coding hypothesis was labelled **INFERRED** and cost two cheap probes -- the label worked.
But *"52.5% is the correction"* was stated **flat**, and it propagated: **CTO~Z adopted it into step 1
on my say-so.** This is the **second** time today I handed over a conclusion more confidently than its
evidence supported (F-2 was the first, relayed into a `[STOP]` and two spec revisions). Both times the
adopter did nothing wrong; both times the measured half was solid and the characterisation outran it.

> **AN UNLABELLED CONCLUSION DRAWN FROM A LABELLED MEASUREMENT INHERITS NONE OF THE LABEL'S
> PROTECTION. It is not enough to label the inference -- the CONCLUSION needs its own label.**

For WS-C8, beside the self-declaration law, convergence-is-not-corroboration, and the
instrument-that-discards-what-it-exists-to-find.
