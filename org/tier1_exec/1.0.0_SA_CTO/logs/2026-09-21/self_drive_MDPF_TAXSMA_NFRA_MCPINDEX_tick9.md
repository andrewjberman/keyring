# /self-drive ticks 8-9 -- ⛔ **my own framing nearly laundered 7 failures, and it was caught with minutes to spare**

**Seat:** `1.0.0_SA_CTO` · laptop · CLOUD · **UTC** 2026-09-21 ~06:3xZ
**Arming record:** `ANDREW_DIRECT_20260921_005xZ_...md` @`07b8a03ec3`, §8 @`57751941a0`
**State:** ARMED · cadence 30m · job `2efc77bf`

---

## 0. HEADER FIGURES -- EACH FROM A CALL IN THESE TICKS, ON THE GATE'S RESOLVER

| figure | value |
|---|---|
| `MDPF_TAXSMA` | **19 OPEN of 27** · `EXECUTING` · flags `-` |
| `NFRA_MCPINDEX` | **38 OPEN of 38** (`MX-c-1` now `blocked`, correctly) · `EXECUTING` |
| legacy-root orders, both | **0 / 0** |
| live COO lanes / cap | **3 / 3** |
| unread | **0** |

## 1. ⛔⛔ THE NEAR-MISS: A CELL GETS CUT FROM THE FRAMING, NOT FROM THE POPULATION

My round-7 L10 §5(3) called the status-word item **"BOOKKEEPING, NOT RE-WORK."** `3.0.0_SA_CVO` then measured
the population I had described: **all SEVEN of those orders carry a FAILING criterion. 7 of 7.**

`2.0.0_SA_COO~B` had cut `IB-rth-3` faithfully from that frame; its line 22 read *"edit ONLY its `<status>`
field's leading word **to a terminal value**."* I read the order at HEAD rather than by its title and sent
the correction at `98990`.

⭐ **THE MARGIN WAS MINUTES.** `2.0.0_SA_COO~B`: *"The first `rth-3` HAD ALREADY COMMITTED all 7 orders ->
`complete` on its branch (`5402759b7f`) and was running its battery. I TaskStopped it ... the branch was
undrained and is now DISCARDED. **No failure was laundered.**"*

⛔ **THE DEFECT IS MINE AND THE ISSUER SAID SO PRECISELY:** *"the word 'bookkeeping' in my read of the L10 is
what I cut too literally."* My literal words were *"reconcile or note"*, which admits the right answer --
**and the FRAMING is what travelled into a worker face.** ⭐ **A CTO's adjective becomes a worker's act, two
artifacts downstream, with nobody re-reading the adjective.** COST: one sentence written at the population's
grain rather than at the summary's. NON-APPLICATION: an analysis nothing is cut from.

**The ruling `2.0.0_SA_COO~B` executed verbatim (`9dd9cd70a3`):** per-order honest word; `complete` ONLY on a
bound expressly permitting completion with a disclosed FAIL; `superseded` ONLY where a later round actually
re-cut, read as a fact; **else leave non-terminal and record why** -- and `R78-AC1` now passes by **naming**
the residual, never by flipping a failing order.

## 2. ⛔ THE BLIND SPOT HAS ALREADY FIRED, AND MY "0 OPEN OF 79" WAS AN OVER-COUNT

I carded `_proof_terminal`'s MEASUREMENT-vs-REFUSAL-TO-RUN blind spot on **one** instance
(`f1c469829c`). `3.0.0_SA_CVO` applied my own discriminator to its seven: `rt-6` (*"3 BLOCKED ... rest on a
premise this order's `<paths>` cannot reach"*), `rtf-14` (*"(c) AND (d) ARE NOT RUN"*), and ⛔⛔ **`rtf-7`,
whose own `status_reason` says *"the order stays open"* while the predicate counts it terminal** -- the
artifact and the instrument disagreeing **in writing**.

**So the L10's `0 open of 79` is wrong by at least three**, amended at `0c61487438` under R-43. ⚠ **Bounded:
round 7's four cells carry their own proofs and PASSes, none is in this set, and the round-7 adjudication
stands. The wrong figure is PROJECT-level round-6 residue no round ever re-examined.**
**Card now: 1 instance → ≥4 across 2 projects**, and the remedy sharpened -- all seven say *"BLOCKED"*,
*"NOT RUN"*, *"stays open"* **in prose inside `status_reason`, in no field a consumer can reject on.** ⭐
**That is this estate's own "a value must carry its claim" with the CONSUMING HALF MISSING: the fix is a
FIELD, not a cleverer reader of prose.** Still carded, not patched -- the predicate prevents a measured
20-row hostage incident and a schema+gate change at 06:2xZ under a no-new-seats hold is the worst trade.

## 3. `NFRA_MCPINDEX` W1-S1 / W1-S2 RULED, THEN CORRECTED BY MEASUREMENT

**W1-S1:** Option A adopted -- the CRITERION is right, the CUT was wrong; a `<paths>` grant that cannot cover
its own criterion is an internal contradiction in the order, not a spec change. Bound tightened because one
path is the ONE catalog home: **post-revert diff ASSERTED empty, not eyeballed.**

⭐ **`2.0.0_SA_COO~M` then declined to amend and ASKED**, because my ruling said two paths and its read made
three. **Measured: the basis does not hold.** `REPORT_DIR` occurs **exactly once** in `emit_catalog_v02.py`
-- its own definition, **with no use**. The writer is `validate_catalog_v02.py:31`, and **`AC4` never runs the
validator**. Denominator: 3 hits across 1,158 files. **Grant stays TWO** (`de8bf648cd`).
⭐ **THE KEEPABLE: A DEFINED CONSTANT IS NOT A USE** -- and a census by NAME returns a confident hit on the
definition itself. Grep for USES. ⚠ **And my own "exactly two" was RIGHT FOR THE WRONG REASON:** I took it
from the worker's row without reading the emitter at all.
**W1-S2:** `FABRIC`, per-proof, no 38-order amendment -- `NFRA` is not in the schema's `firm` enum, so all 38
proofs would derive **UNPARSED**, and the schema says *never guessed*.

## 4. ⭐ THE PATTERN OF THESE TWO TICKS

**Every single correction came from a peer measuring what I asserted, and every one of my errors was in the
SUMMARY rather than in a measurement:**
- "bookkeeping" -- a frame, not a figure, that cut a cell.
- "0 open of 79" -- a figure I inherited from a slug without re-deriving.
- "exactly those two paths" -- taken from a worker's row without reading the code.
- "caught at 1 of 38" (tick 8) -- generalised from an instance that **was not a member of the class**.

⛔ **THE MEASUREMENTS HELD; THE SENTENCES AROUND THEM DID NOT** -- which is the same shape as the disk
projection two ticks earlier, and the same shape `3.0.0_SA_CVO` convicted itself of at `98965`. **The fabric's
correction rate is high because peers re-measure; that is the control, and it is working in both directions.**

## 5. COMPLETION TEST

**NOT DONE -- 0 of 2.** Both `active`/`EXECUTING`, both **REACHABLE**, 0 UNREACHABLE. Open calls at Andrew:
**2**, unchanged (the five Schwab tools; the Gateway rollback-repair owner). **No TO cut, no seat spawned, no
apply.** The no-new-seats hold is untouched.
**Push state: LOCAL** -- `f1c469829c`, `0c61487438`, `de8bf648cd`, this log. Only `0.0.0_AB_MSTR` pushes.

## Compiler Tools

`_open_tos_for_project` (gate resolver, both roots) · `git show HEAD:<order>` read at HEAD rather than by
title · `sed -n` at cited lines on `emit_catalog_v02.py` (`:40-46`, `:733-737`) · `comp-find 'validation_report'`
(3 of 1,158, with bands) · `git ls-files` tracked-check · `json` over the `MX-c-1` proof instance ·
`safe-commit` x3.
