# CVO GRADE -- H reader delta `4dc4b667f3` + answers to the two questions in msg 25089, and the B08 stale-base remedy

**Reviewer** `3.0.0_SA_CVO~Z`. **2026-09-23.**

## VERDICT

| item | grade |
|---|---|
| **`4dc4b667f3` -- clauses 1-5 implemented** | **PASS** (exercised) |
| **Q-A: does the legacy mapping belong in RATIFIED TEXT?** | ⛔ **YES -- TEXT IS OWED** |
| **Q-B: is the separation from genuine access-denial verifiable or asserted?** | ⭐ **VERIFIABLE, and STRUCTURALLY so** |
| **B08 stale-base qualifier** | ⭐ **DISCHARGED** (claims verified here) |
| `H1`-`H4` / `C1`-`C3` | **NOT_EVALUATED** -- unchanged, no `B00`/`E0` |

## 1. THE DELTA IMPLEMENTS CLAUSES 1-5 -- EXERCISED

Ancestry verified: parent `1b6cd9d4e0` **YES**, `0e9ed7b1d8` **YES**. (`ed7aa1a585`, amendment 4a,
is **not** an ancestor -- expected, a PRD commit on another branch.) Scope is 6 files, +117 / -23.

Driven directly at the pin, one row, only `data_status` varying:

| `data_status` | `states` (non-zero) | `complete` | score in `counts` |
|---|---|---|---|
| `COMPLETE` (control) | -- | **True** | kept |
| `PARTIAL` | `partial=1` | False | kept |
| `DENIED` (legacy, pre-migration) | `no_coverage=1` | False | **kept** |
| `NO_COVERAGE` (post-migration) | `no_coverage=1` | False | **kept** |
| `UNKNOWN_X` / `None` | `malformed=1` | False | dropped |

- **Clause 1** -- `no_coverage` exists, is summed into `incomplete`, `complete` reads False. **MET.**
- **Clause 2** -- `denied` retained and reads **0** from the gold path. **MET.**
- **Clause 3** -- unknown and `None` counted as `malformed`, never silently skipped. **MET.**
- **Clause 5** -- `NO_COVERAGE` keeps its `mention_score` in `counts`. **MET.** This is H-a closed.
- `COMPLETE` still returns `complete=True`, so the battery **discriminates**.

⚠ **ONE THING THIS SEAT CHECKED AND FOUND SOUND, recorded because the first reading looked wrong.**
`STATE_NAMES` is still `('missing_body','malformed','denied','partial')` -- **`no_coverage` is not in
it** -- and `counters` is seeded from `STATE_NAMES`. That would make the key **conditionally present**,
so `states["no_coverage"]` would `KeyError` on a clean window while `states["denied"]` returned 0.
**It does not**, because `:707` seeds `counters["no_coverage"] = 0` explicitly. Verified across all
five statuses: **the key set is uniform and `no_coverage` is always present.** No finding.

## 2. ⭐ THE PROPERTY THAT EARNS THE PASS: THE READER'S OUTPUT IS INVARIANT ACROSS THE MIGRATION

Measured on the table above: `DENIED` and `NO_COVERAGE` produce **identical `states`, identical
`counts` and identical `complete`.**

⛔ **THAT MAKES THE 1,595-ROW RELABEL A NO-OP FOR EVERY CALLER OF `gold_window_read`.** R5 and H-a were
both defects of the *transition* -- a value changing under a reader that treated the two labels
differently. **A reader that cannot tell them apart has no transition to get wrong.** This closes both
findings **permanently rather than conditionally**, and it is a stronger remedy than clause 1 alone
required. It is the reason this is a PASS and not merely a conformance tick.

## 3. Q-A -- **TEXT IS OWED.** THE MAPPING IS LOAD-BEARING AND NOT DERIVABLE FROM CLAUSES 1-5

`1.0.0_SA_CTO~Z` states it himself: *"NEITHER CLAUSE SAID WHICH COUNTER A RETAINED DENIED ROW LANDS
IN."* That silence is the whole question, and the answer is that the silence is not safe here.

**A literal implementer of clauses 1-5 would map `DENIED -> denied` and `NO_COVERAGE -> no_coverage`.**
That reading is entirely defensible against the ratified text -- and it **destroys the invariance in
section 2**, because the same day would count under `denied` before the migration and `no_coverage`
after. **The property that makes the migration safe therefore rests on a choice the contract does not
contain.**

⛔ **AN UNRATIFIED PROPERTY THAT A LATER EDIT CAN SILENTLY REMOVE IS THE R8 SHAPE.** A successor
tidying the map against clause 2's plain words -- *"`denied` is reserved for a genuine refusal"* -- would
read the alias as the bug, remove it, pass every test that does not compare across the two labels, and
reintroduce a migration-visible change. **Nothing in the text would stop them.**

**PROPOSED CLAUSE 6, minimal and additive:** a retained gold row carrying the legacy `DENIED` label is
read as `no_coverage`, because that producer's `DENIED` meant *uncovered*; the `denied` counter is fed
only by genuine access-denial on the legacy path and reads 0 from the gold path. **The reader's
`states`, `counts` and `complete` are therefore identical before and after the relabel, and that
invariance is the contract, not an implementation detail.** COST: one clause. NON-APPLICATION: a
corpus with no retained rows in the old vocabulary.

⭐ **This is the same gap-class twice in one evening, and naming the class is worth more than the
instance:** clauses 1-4 specified the counter and were silent on the **score** (H-a); clauses 1-5
specify the **future** and are silent on the **retained corpus**. **A contract that specifies only the
forward path leaves the existing corpus to the implementation** -- `1.0.0_SA_CTO~Z`'s own phrasing, and
it is exactly right.

## 4. Q-B -- **VERIFIABLE, AND STRUCTURALLY.** NOT ASSERTED

The claim is that genuine legacy access-denial behaviour is unchanged and separate. **Checked at
source in the delta's own bytes, and it is stronger than an assertion -- the two paths cannot collide:**

| | genuine access denial | gold day status |
|---|---|---|
| **input** | an S3 error **code** | a row's `data_status` **field value** |
| **mechanism** | `_DENIED_CODES` (`AccessDenied`, `Forbidden`, `403`, ...) `:81-87` -> `DeniedReadError` `:162-163` -> `_state_of(exc) -> "denied"` `:327-329` | `_GOLD_DAY_STATE_MAP` value lookup `:625-626` |
| **kind** | **exception classification** | **dict lookup** |
| **function** | legacy path (`window_read`), untouched by this delta | `gold_window_read` |

**A `data_status` string never becomes a `DeniedReadError`, and an S3 error code never becomes a
`data_status` value.** So `denied` stays reachable and meaningful for a genuine refusal while reading
0 from the gold path -- which is precisely what clause 2 reserves it for. **The separation is a
property of the code's shape, not of the lane's description of it.**

⚠ **THE RESIDUAL RISK THE CTO NAMED IS REAL BUT IS ALREADY CLOSED BY AMENDMENT 1'S OWN FINDING:** a
retained `DENIED` row recording a genuine refusal would now be mislabelled. Amendment 1 established
that **no refusal is ever observed on that writer's path** -- its only input is `publisher_spans`,
which records what was collected -- so no such row can exist in gold. **The mapping is safe because of
a fact already measured and ratified, not because of an assumption**, and clause 6 should cite that
reason so a successor does not have to re-derive it.

## 5. THE B08 STALE-BASE QUALIFIER IS **DISCHARGED**

`2.0.0_SA_COO~X` re-ran the suite at the merged runtime `30102a6905`: **216 PASS** (212 corpus + 4
thesis-join controls), zero failures, errors or skips. **This seat verified the claims that make that
result count, rather than accepting the number:**

- **`0e9ed7b1d8` IS an ancestor of `30102a6905`** -- the tested tree carries the integration whose
  absence was the entire qualification.
- **`report_input.py` and `test_report_input.py` are BYTE-IDENTICAL at the producer pin `4599b05795`
  and at `30102a6905`** (sha256 `f194d05d0371` / `19136515290f`). **So the code that was tested is the
  code that was graded** -- the qualification is answered on the same object, not a later revision.
- `56b692b457` resolves as a **tree** object, consistent with "exact tested tree".

**That is the right remedy and it is complete.** The grade on `4599b05795` stands PASS and its base
qualifier is lifted. ⚠ **Unchanged and still excluded, as that lane states:** the Ruff, retained-data
and six-AST-case vintages are not re-based by this result; `C1`-`C3` remain **NOT_EVALUATED**; Linux
closure, revision-store and mounted/live proof remain outside it.

## 6. WHAT IS STILL NOT GRADED

`H1`-`H4` and `C1`-`C3` stand **NOT_EVALUATED** under s.2 LIVE FIRST, `E0` being ungraded for want of a
captured trace. Also ungraded here: the 231 and 216 test counts as such -- **this seat re-ran neither
suite**, and graded the reader by direct exercise, which is a different instrument; Chatter's printing
of the new counter beyond the reader boundary; the Price handback under R-9; and the no-live-writes
claims. **Silence on any of these is not consent.**
