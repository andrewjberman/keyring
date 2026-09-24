# CVO GRADE -- B08 pinned candidate `4599b05795` (`2.0.0_SA_COO~X`)

**Reviewer** `3.0.0_SA_CVO~Z`. **2026-09-23.** Under closer CONTRACT v1.0 s.5.

## VERDICT

| boundary | grade |
|---|---|
| **Read-only posture of `report_input.py`** | **PASS** (source census, a different instrument from the lane's I/O count) |
| **`I4_RUNTIME_JOIN.patch` applies to the current tree** | **PASS** (exercised: `git apply --check` at HEAD) |
| **Base currency of the candidate's own validation** | ⚠ **QUALIFIED -- 1,063 commits behind** |
| **`C1`-`C3` acceptance IDs** | **NOT_EVALUATED** -- no `B00`/`E0`, per s.2 LIVE FIRST |
| Deploy / cutover acceptance | **NOT CLAIMED, NOT GIVEN** |

## 1. ⚠ THE CANDIDATE'S BASE IS 1,063 COMMITS BEHIND THE SHARED TREE

Measured here:

- **merge-base with HEAD: `db3267d079`** (2026-09-23 16:41Z).
- **HEAD carries 1,063 commits the candidate does not.** The candidate carries 16 HEAD does not.
- **`0e9ed7b1d8` -- the 996-commit CLOUD integration -- is NOT an ancestor.** Neither is `1b1244cecf`.

⛔ **This is exactly the hazard `0.0.0_AB_MSTR~Z` named** -- *"worktrees cut from SITEZ before this point
are building against a tree missing those 996 commits ... it applies to every branch any of you is
holding."* The lane's message states *"Remote SITEZ remains `1b1244cecf`"*, which was true when the
branch was cut and **is stale now**: origin/SITEZ advanced to `0e9ed7b1d8` and HEAD is well past it.

**WHAT THAT DOES AND DOES NOT MEAN.** It does **not** invalidate the module. It **does** bound the
lane's own evidence: the 212 corpus tests, the Ruff pass and the six poisoned AST cases all ran against
a tree **missing those 1,063 commits**, so they certify the candidate **in its own base**, not in the
tree it will merge into. ⚠ **A green suite on a stale base is a real result about a different
population.** ⭐ **Mitigating, and measured rather than assumed: the H candidate by contrast DOES carry
`0e9ed7b1d8`, so this is a per-branch condition, not a fabric-wide one.**

## 2. THE I4 PATCH STILL APPLIES -- EXERCISED, NOT ASSUMED

The obvious consequence of a 1,063-commit gap is that the handoff patch no longer fits. **It does fit.**
`git apply --check` of `I4_RUNTIME_JOIN.patch` against **HEAD**: **applies clean.** The patch is small
(15 lines) and its target region in `scoped_amgt.py` is untouched by the intervening commits.
Corroborating that independently: `lib/research/api/scoped_amgt.py` is **byte-identical at
`dd91fd3126` and at HEAD** (sha256 `40c3ed25da2fab61`, 197,482 bytes).

⭐ **The lane's decision NOT to apply it itself is correct and is the contract working.**
`scoped_amgt.py` is `2.0.0_SA_COO~Z`'s sole writer under s.3; a consumer sends a pinned patch and the
owner integrates. That is what happened.

## 3. READ-ONLY POSTURE -- CORROBORATED ON A DIFFERENT INSTRUMENT

The lane reports 142 GET / 9 LIST / zero writes from its own measurement. **This seat did not re-run
that count** -- that would be repetition. Instead, a source census of the module at the pin
(`lib/research/corpus/report_input.py`, 135 lines):

- The only public entry is **`read_report_input(security_key, *, client=None)`**.
- I/O is funnelled through **`_ReadSnapshot`**, which exposes **`get_object`** and, in its
  `__getattr__`, **refuses any operation other than `list_objects_v2`** (`if name != "list_objects_v2"`).
- **No `put_object`, `delete_object` or `copy_object` appears anywhere in the module.**

**So the write-free property is structural rather than merely observed in one run** -- the wrapper
cannot express a write. That is a stronger claim than a call count, and it is reached by a different
route, which is why it counts as corroboration.

## 4. WHAT IS NOT GRADED, AND IS NEVER AN IMPLIED PASS

`C1`-`C3` stand **NOT_EVALUATED**, which is what the lane asked for and is correct under s.2: offline
closures grade nothing until `B00`/`E0` passes, and `E0` is UNGRADED for want of a captured trace.
Specifically **not** graded here: the retained `IMB_LN_Equity` adapter read (15 reports / 33 references);
the six externally poisoned cases; the failure-envelope no-partial-payload claim; the semantic producer
hashes, which the lane itself flags as carried rather than recomputed; PyArrow packaging; and the
authenticated/mounted rendering. **Silence on any of these is not consent.**

## 5. THE CROSS-LANE SEQUENCING POINT, WHICH IS NOW REALISED RATHER THAN HYPOTHETICAL

`I4_RUNTIME_JOIN.patch` adds a `bundle["corpus"]` key inside the thesis-bundle assembly of
`scoped_amgt.py` -- **the same file the no-span cutover repairs.** At 21:46Z `2.0.0_SA_COO~Z` reported
integrating it, with the Price handback, at `30102a6905`.

⭐ **That seat handled it correctly and said so explicitly:** *"Signed candidate ZIP remains unchanged;
no cloud mutation, direct Lambda update or current-source rebuild."* **Nothing is wrong here.** The
consequence belongs to the cutover review and is recorded as an addendum to it, not as a defect in this
candidate: the ZIP's source and the working tree have now diverged, so the rebuild path C2 relied on has
narrowed. See `AMGT_SCOPED_API_CUTOVER_C2_ADDENDUM_20260923_Z.md`.

## 6. SUMMARY FOR THE INTEGRATOR

**The module is sound on the boundary the lane asked to be graded**, and its read-only posture is
structural. **The one thing to carry forward is the base currency**: the candidate's green evidence was
produced on a tree 1,063 commits behind, so re-running the corpus suite **after** the merge -- not
before -- is what converts that evidence to the population it will actually live in. The patch itself is
verified to apply, so the merge is not expected to be eventful; the point is that the *tests* have not
yet spoken about the merged tree.
