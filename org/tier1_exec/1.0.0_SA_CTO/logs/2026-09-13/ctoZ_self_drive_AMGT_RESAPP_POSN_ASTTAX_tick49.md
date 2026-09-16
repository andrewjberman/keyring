# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 49 (covers ticks 48-49)

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-13T05:36:55Z**
Tick 47's log is `@ef9ab54f5d`, committed `2026-09-13T01:17:2xZ-04:00` (author time, not the
filename). **Tick 48 wrote no log of its own and said so; it is folded in here.**

> **THE ROUND-3 L10 LOOP CLOSED END TO END IN TWENTY MINUTES, AND THE GAP IT FOUND IS GONE.**
> `UNCOVERED = { FWD-4, FWD-6 }` at 05:0xZ -> `UNCOVERED = EMPTY` at 05:36Z.

---

## 1. THE COVERAGE GAP IS CLOSED -- MEASURED, NOT REPORTED

```
19 cut orders (was 15 at the L10) · 6 declared · UNCOVERED = EMPTY
FWD-1 16 · FWD-2 4 · FWD-3 1 · FWD-4 1 · FWD-5 2 · FWD-6 2
control: run-time generated, absence-verified before use, NOT printed -> 0, discriminates
  FWD-4 <- TO-U2-1.one-colour-per-class-the-same-everywhere
  FWD-6 <- TO-U1-1.derive-the-readers-and-grade-the-five-class-bar  +  TO-U2-1
```
**The chain ran in order and none of it was forced:** slug `@c89c0e45a2` -> this seat's L10 finding
two outcomes unserved in three rounds -> addendum v0.6 -> `4.0.0_SA_CRO~Z` re-signs the brief half in
two minutes -> `2.0.0_SA_COO~Z` recuts with cells for both. ⭐ **`U1-1`'s own name -- *derive the
readers* -- is `Z-C-S55`/`Z-S42`'s third-surface ruling arriving as a cell**, which is the ruling and
the coverage gap closing as the single defect s.3 said they were.

## 2. TICK 48 -- THE SCOPE QUESTION, ANSWERED FROM A PRECEDENT RATHER THAN A PREFERENCE

`2.0.0_SA_COO~Z` held round 4 to ask (22280) whether **measure-and-price** satisfies *"round 4 must
cover FWD-4 and FWD-6"* -- cells that read portal source and price the change, writing no byte under
`portal/`. **It reads narrower, and asking before cutting was right.**

The discriminator was not this seat's judgment: `AMGT_RESAPP.TO-AMGT-rh-1`, cut by the sibling lane
under the same freeze the same night, **already grants write paths inside the submodule** while
forbidding promote, push, DEV/PROD merge and gitlink moves -- *"Commit yes, promote no"*, with `AC5`
verifying the gitlink mechanically. Those four forbidden acts are exactly the ones the relay names;
**writing source is not among them.** And Andrew's own framing settles the rest: *"the only thing
between the build and a person is the promote itself"* is not true of a frontend that has only been
priced. **FWD-4 and FWD-6 are EXERCISED bars — measurement cannot approach them**, and pricing cells
would be covering without serving, the exact failure s.2 exists to name.
⚠ **Stated as a reading of what the freeze COVERS, never a lift**, and it does not answer the card
that seat put to Andrew at 05:14Z about the promote. Landed as `ROUND_ANALYSIS.round3` s.7
`@d7261cf29c`.

## 3. ⛔ AND MY OWN ANSWER WAS INCOMPLETE -- s.7a `@29978b9399`

s.7 said a portal commit is PERMITTED. **It never said where that commit must be REACHABLE FROM.**
`2.0.0_SA_COO~ZZZ` supplied the coordinate (22289, `Z-S70` `@cede63a639`) and this seat reproduced it
with its own controls:

```
a845a8be75  (AMGT round 8's portal repairs, 14 commits)
  git branch -a --contains ...... 0          <- reads exactly like work never done
  git for-each-ref --contains ... refs/drains/rg-2-portal    (ONE ref, and NOT a branch)
  is-ancestor of origin/DEV ..... NO
POSITIVE CONTROL same run: for-each-ref --contains on local HEAD 30ca034bba -> 10 refs;
  is-ancestor origin/DEV origin/DEV -> YES.      The zeros are REAL zeros.
```
**A lane that merges portal work FROM BRANCHES and pushes DEV drops those fourteen commits with no
conflict, no refusal and no gitlink disagreement** -- because the gitlink never pointed at them
either. s.7a now carries the companion instruction: reachable from a ref a peer's merge will
traverse; `branch --contains 0` is **not** evidence work was never done; and **the gitlink moves
ONCE, at promote**, after both lanes' portal commits are merged inside the submodule.

⭐ **The sequencing question I raised dissolves, and better than I posed it.** While neither lane
moves the gitlink there is no contention on the shared value at all — disjoint paths inside the
submodule do not write it. **The risk was never concurrent writing; it is a later merge that cannot
see one lane's work.** That reframing is `2.0.0_SA_COO~ZZZ`'s and it is sharper than the question.

⚠ **AND IT EXPOSED A GAP IN A BANKED MEMORY**, extended rather than duplicated: the
wrong-domain-control entry's remedy read *"`git log --all`, or `git for-each-ref refs/heads/`"* —
**and `refs/heads/` also returns zero here.** One ref-namespace too narrow, in exactly the way `ps -p`
was one process-namespace too narrow earlier tonight. **A remedy scoped to where you got caught leaks
one namespace over**, twice in one night, on two different surfaces.

## 4. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 2 RESERVED · NO PITCH   (all-reserved tell does not fire)
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 projects, 2 of 14 live directives)
  AMGT_RESAPP  EXECUTING  REACHABLE  1 OPEN of 47 -- rh-1, the served route
  POSN_ASTTAX  EXECUTING  REACHABLE  8 OPEN of 19 -- round 4 CUT, FWD-4/FWD-6 now covered
  UNREACHABLE: 0     HELD-AT-STOP: not reached
```
**Nothing is owed by this seat.** Both L10s are answered; POSN's PRD reads ADMITTED at v0.6 with both
halves SIGNED current; the next CTO limb on either project is the round-4 / round-9 slug, and neither
exists. **Push state:** `origin/SITEZ d7261cf29c`, local ahead 4 at the read. `HEAD:portal
e85f6eb84f`, unmoved. No TO cut, no dispatch, no apply, no retag, no deploy, no promote.

## Compiler Tools

The coverage subtraction re-run after the recut, with a **run-time-generated, absence-verified,
unprinted** control · `rh-1`'s `<paths>` block read as the precedent that answered the scope question ·
`git branch -a --contains` **paired with** bare `git for-each-ref --contains` and an
`is-ancestor` positive control, in the submodule clone · `git ls-files -s portal` against
`git -C portal rev-parse HEAD` as the live gitlink-vs-submodule-HEAD discriminator · `prd-signoff.py
status` read at the moment of acting · landmark greps to verify a section survived an in-place
amendment, one of which returned a false 0 on case and was re-run case-insensitively rather than
believed · `safe-commit.sh -F` with non-shell-written message files · short send subjects.
