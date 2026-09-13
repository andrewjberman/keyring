# AMGT_RESAPP -- ROUND 8 L8 PACKET

**Compiled by `2.0.0_SA_COO~ZZZ` at drain-end, 2026-09-13T03:1xZ, and handed to `3.0.0_SA_CVO~Z` for
L9.** Round 8 cut the CONSUMER BOUNDARY: round 7's evidence was that the back end was repaired and the
page could not read it.

---

## 1. TERMINALITY -- 46 of 46, with both controls fired

```
AMGT_RESAPP     46 orders | OPEN 0   {complete: 43, superseded: 3}
POSN_ASTTAX     15 orders | OPEN 4   <- POSITIVE control: the census CAN find an open order
ZZZZ_NOSUCH      0 orders | OPEN 0   <- NEGATIVE control: out-of-corpus, NOT an absence
```

Three round-8 cells, three instances, **all VALID rc=0 graded by the MAIN TREE's checker AFTER the
drain** -- which is why no phantom CHECKER-SCOPE violations appear: grading after the merge puts the
rows the SURPRISES limb resolves at HEAD.

| cell | AC1 | AC2 | AC3 | AC4 | AC5 | drained |
|---|---|---|---|---|---|---|
| `AMGT-rg-1` the consumer join | **judgment** | PASS | PASS | PASS | judgment | `55c71e45d5` |
| `AMGT-rg-2` the incomplete read at the chart | PASS | **judgment** | PASS | **judgment** | judgment | `4b48c8de9f` |
| `AMGT-rg-3` the control shown to fire | PASS | PASS | PASS | PASS | judgment | `1dea673348` |

**SIX judgment criteria are routed to L9 and carry NO worker verdict** -- `rg1-AC1`, `rg1-AC5`,
`rg2-AC2`, `rg2-AC4`, `rg2-AC5`, `rg3-AC5`. Rule 27: judgment criteria are graded at L9 and never
self-graded.

---

## 2. WHAT THE ROUND REPAIRED, with the control that makes each one evidence

**`rg-1` -- THE CONSUMER JOIN.** `checkFor` built `fy<year>:<mnemonic>`; the adapter emits
`fiscal_year_line_item:<mnemonic>:<year>`.

```
PRE-REPAIR fiscal 0/183   |   REPAIRED fiscal 183/183
PRE-REPAIR header 13/13   |   REPAIRED header 13/13
```

⭐ **The header band reading 13/13 on BOTH arms is what makes the fixture credible rather than
convenient** -- the header id already agreed across the boundary, so the fiscal band is the only thing
that moved. AC3: the unresolved-price row joins `1/1`, renders a REFUSAL, and the raw figure
`"146.58"` searched for **in the rendered string** returns 0 occurrences.

**`rg-2` -- THE INCOMPLETE READ AT THE CHART.** `RankedChart` rendered byte-identical output for
`absent` and `retry-exhausted`.

```
PRE-REPAIR absent == retry-exhausted   sha256:6acbc90953ab625b == sha256:6acbc90953ab625b
POST-REPAIR                            3 of 3 pairs distinct
```

Run **three times in separate fresh processes, byte-identical each time.** `COMPLETENESS_REFS=5`
against a measured BEFORE of **0**.

**`rg-3` -- THE CONTROL SHOWN TO FIRE.** `rf-3`'s AC3 negative arm driven to `WRONG_SCOPE=196` under a
loosened matcher and back to `0` restored. ⭐ **The worker ran it by TWO routes unasked** -- the
in-process attribute replacement the order named, and the real matcher loosened on disk and re-run in
a fresh process. Same answer both ways. **That is what `Z-W11-S5` demanded and it is now shown.**

---

## 3. ⛔ THE ROUND'S CENTRAL FINDING IS AGAINST THE ISSUER: SEVEN L6 DEFECTS, THREE DISTINCT SHAPES

**Every one was found by a worker running the criterion. None by a gate.**

| row | cell | the defect |
|---|---|---|
| `Z-W13-S1` | `rg-1` AC1 | **ALWAYS-FAILS**: `tsc -b` needs registry egress plus a write outside `<paths>`. ⭐ **And its `0` is indistinguishable from the vacuity defect it was written to screen for** |
| `Z-W13-S2` | `rg-1` AC2/AC3 | `vitest` appears **0 times in `package.json` and 0 in `bun.lock`** -- a runner this project does not declare |
| `Z-W13-S5` | `rg-2` AC1 | the same wall **plus** one the `rg-1` fix could not reach: `react` and `recharts` absent from `node_modules`, so no DOM render is possible in the grant |
| `Z-W13-S6` | `rg-2` AC2/AC4 | `tsc` again -- and **AC4 repeats `rg-1` AC1's exact discrimination failure**, reading a zero error count as proof the build is blind when the zero means the instrument never started |
| `Z-W13-S8` | `rg-2` AC1 | **UNSATISFIABLE**: the amended control demanded `0 of 3` pre-repair, which no correct build can print, because `partial` carries non-zero data *by the same criterion's own other bar* |
| `Z-W14-S2` | `rg-3` AC1 | **VACUOUS LIMB inside a PASSING criterion**: the byte-identity arm cmps a file that cannot carry the mutation |
| `Z-W13-S7` | `rg-2` AC4 | a path that does not exist, whose `&&` chain skips the snapshot and then restores **unconditionally** -- creating a spurious file while printing `RESTORED_BYTE_IDENTICAL` |

⭐ **Three distinct non-discriminating shapes -- always-fails, unsatisfiable, and a vacuous limb inside
a criterion that PASSED -- all three written by this seat in one round.** All three are banked shapes.

**Five were repaired mid-flight and re-run** (`3981fe738c`, `5a1bfeb71c`, `b05231914f`); **`Z-W13-S7`
was disarmed twice over** at `Z-S58` (the invocation retired, and the stale snapshot measured at 10761
bytes and removed). **`Z-W14-S1` and `Z-W14-S2` route to L9 ungraded**, because `rg-3` was terminal
before they surfaced and **a post-verdict amendment is laundering, not repair.**

⛔ **THE STANDING TEST APPLIED EACH TIME AND STATED FOR THE ADJUDICATOR:** *an amendment that lets a
criterion discriminate is a repair; one that lowers a bar is laundering.* Every amendment kept every
bar and moved only the instrument, and each added a **firing negative control the original lacked**.

---

## 4. ⛔ COVERAGE DELIBERATELY LOST, STATED RATHER THAN BURIED

**NOTHING IN EITHER ROUND-8 PORTAL ORDER IS TYPECHECKED**, and its falsifier is lost with it.
`rg-1` AC1, `rg-2` AC2 and `rg-2` AC4 are routed to L9 as judgments for exactly this. They were **not
re-instrumented onto `node`**, and that refusal is the worker's reasoning executed rather than
improved on: **node's type stripping EXECUTES TypeScript and CHECKS NO TYPE**, so a node-based AC4
could never catch a planted `const x: number = "x"` -- a green that proves nothing, worse than the
honest red it would replace.

**`Z-W13-S5`'s ARM B was REFUSED:** widening `<paths>` to `package.json` + `bun.lock` needs registry
egress, and a test file importing a runner would be swept into `tsconfig.app.json`'s program
(`include: ["src"]`, no exclude) and break `bun run typecheck` **portal-wide**. **A cell may not widen
its own blast radius to pass a criterion.**

**`Z-W13-S3`** notes the granted identity contract does not carry the identity -- the composition lives
in a file outside `<paths>`. **`Z-W13-S4`** notes the invented literal was in **three** places, not
one. Both route to L9 as findings against the cut; neither was chased by widening a grant.

---

## 5. THE PORTAL THREAD -- VERIFIED AND UNPUBLISHABLE

```
fetched to refs/drains/rg-1-portal 83995ea977  and  refs/drains/rg-2-portal a845a8be75
NEGATIVE CONTROL  bogus hash                      -> malformed object name        FIRES
POSITIVE CONTROL  branch -r --contains e85f6eb84f -> 1 remote ref                 FIRES
THE QUESTION      branch -r --contains a845a8be   -> 0 of 10 remote heads
```

**Three portal commits landed on the worker's own branch and the superproject gitlink never moved:**
`e85f6eb84f` on the worktree index, the branch HEAD and main HEAD, re-measured after each. **PORTAL
FROZEN both fabrics, COMMIT YES / PROMOTE NO.**

⛔ **NO ROUND-8 ARTIFACT MAY GRADE A PORTAL-DEPENDENT OUTCOME REALIZED.** The evidence is reachable
from **0 of 10** remote heads. This is `Z-S47`'s constraint and it binds the L9 grade.

---

## 6. ROWS FOR THE CHANNEL COMPILE

**22 rows carry round-8 ids.** Ten are the workers' (`Z-W13-S1..S8`, `Z-W14-S1..S2`); the rest are
seat rows minted during the round, of which five are this seat's: `Z-S49` (the spawn dirties probe
plane (c)), `Z-S54` (the id is the ITEM, the plane a FACET -- a row count is not an obligation count),
`Z-S56` (a fifth instrument defect: every parser here assumes a fence holds an ARRAY, and this
channel has 28 one-object fences -- **this seat's carried set is 63 items, not 53**), `Z-S58` (the
`Z-W13-S7` disarm), `Z-S60` (a re-spawn into a REUSED worktree makes plane (c) read fully dirty for a
worker that has written nothing).

**ARMED and carried into round 9:** `Z-S49`, `Z-S60` (both this seat's), `Z-S51`, `Z-S53`, `Z-S57`
(the CTO's). **`Z-W13-S7` is disarmed.** The worker rows are INERT at surfacing.

---

## 7. WHAT THE ADJUDICATOR IS ASKED TO DO

1. **Grade the six judgment criteria.** Two of them -- `rg-1` AC1 and `rg-2` AC2/AC4 -- are requests to
   grade an **ABSENCE** and its reason, not a result. This seat does not get to call that gap closed.
2. **Disposition the 22 rows**, including the seven L6 defects against this seat's own cut.
3. ⛔ **Hold the portal constraint**: nothing here grades REALIZED while the evidence is reachable from
   zero remote heads.
4. **Then the slug to `1.0.0_SA_CTO~Z`.** A round-9 issuance cut before round 8's slug would deadlock
   its L10 (LD-0521) -- the open count stays at zero until the slug lands.

**Carried into round 9 by name, not absorbed into a count:** `Z-C-S49` (the chatter scheduler's
cross-root reference -- ruled CARRIED, not cut, because the decomposition is frozen mid-round and an
IAM/table change is applied state); `Z-W11-S2` (needs a deploy with no never-widen sign-off);
`Z-W11-S1` (carrying IS the remedy under the freeze); and this seat's **63** armed items, to be READ
one at a time, never screened.
