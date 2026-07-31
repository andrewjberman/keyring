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
