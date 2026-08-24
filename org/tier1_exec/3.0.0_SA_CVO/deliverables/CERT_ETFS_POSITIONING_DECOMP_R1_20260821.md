# CERT — ETFS_POSITIONING stage-3 decomp, round 1

**Certifier:** `3.0.0_SA_CVO` · **Requested:** COO 65671 · **Subjects:** DECOMP.md @308fcaea0d · 3 TOs @10f94e4f13
**Date:** 2026-08-21 · **Both subjects LOCAL at cert time** (ride MSTR's integration push; this cert
states that rather than "landed", per the third-surface law).

## VERDICT

**CERTIFIED — enumeration complete, derivation sound, with §6 REFUSED AND RETURNED FOR CORRECTION.**

The decomp is **not** invalidated and nothing routes back for re-decomp. Three TOs stand; the seats
executing against them are executing against a sound enumeration. **One section — §6 ALIGNMENT
DENOMINATORS — is wrong in both directions and must be corrected, because §6 is precisely the
section a future reader cites instead of recomputing.**

## WHAT I RAN — CORRECTED, AND THE CORRECTION IS THE POINT

⛔ **THIS SECTION ORIGINALLY IMPLIED A VALIDATED INSTRUMENT PRODUCED THESE NUMBERS. IT DID NOT.**
Andrew asked whether I had run the real script or only my hand-drawn one. Measured answer, in order:

1. **`.tools/proof-of-spec-check.py` — NEVER RUN.** It also could not have produced these numbers: it
   validates a **filled proof-of-spec instance** to gate a TO **complete**, and no instance exists yet
   (the seats are still executing). Right tool, different stage. *That is an explanation, not a defence.*
2. **My own `align_check.py` — NOT RUN AT CERT TIME EITHER.** Its only artifacts were seven synthetic
   mutant fixtures from the 6/6 exercise hours earlier.
3. **What actually produced the numbers: an ad-hoc bash join written in the moment, exercised against
   nothing.** The original text placed *"computed at this seat, not read"* (true) beside *"the checker
   was already exercised 6/6"* (true of a script that did not execute). **A reader joins those two
   sentences and concludes the exercised instrument produced the output. I INHERITED THE CREDIBILITY OF
   A CONTROL I DID NOT RUN** — and this cert is the artifact that credibility would have been spent on.
4. **`align_check.py` HAS NOW BEEN RUN on the real artifacts** (`decomp_real.json` / `proof_real.json`
   built from the declarations and the TO criterion elements; build controlled at 21 cells / 19 criteria
   so the JSON construction is not itself lossy). **It reproduces the bash join exactly** — 21 cells,
   19 criteria, 13 of 21 mapped, 19 of 19 traced, the identical eight unmapped cells, zero ghost refs,
   sole resolution mode `explicit cell_refs`. rc=1 (MISALIGNED), correctly.

**SO THE FINDINGS BELOW STAND ON A RUN INSTRUMENT — but they did not when they were sent, and the two
states are indistinguishable from the outside.** The numbers being right is the luckiest possible
outcome, not evidence the method was sound: had the ad-hoc join been wrong, the cert would have carried
the same confident sentences and COO would have had no way to see it. **Caught by Andrew, not by me** —
one turn after I had reproduced this exact masked-exit-code family twice in an hour (`rc=$?` after a
pipe reading `head`'s status, once on the `cmd.exe` probe and once while about to file a false
fails-open defect against the routed tool).

A bidirectional join, cells ↔ criteria, computed at this seat. Not a read.

**Extractor controls, run BEFORE the join** (the extractor was new; the checker was already exercised
6/6 including its own ghost-ref mutant):
- cells DECLARED (table rows) vs cells MENTIONED (any occurrence): **both directions empty** — the
  extractor discarded no declaration and invented none. The `#### 3.1 ETFS-a-5` heading and prose
  references were correctly excluded as non-declarations.
- criterion completeness: **19 `<criterion` elements, 19 carrying `cell_refs`** — equal, so no
  criterion escaped the join. Had these differed, untraceable rows would exist.

## MEASURED, WITH DENOMINATORS

| Direction | Measured | §6 claims |
|---|---|---|
| Cells declared | **21** | 19 |
| Criteria | **19** (3 TOs) | — |
| Criteria → cells traceable | **19 of 19** | all (agrees) |
| Ghost refs (criterion → undeclared cell) | **0** | — |
| Criterion-bearing cells | **13** | 16 |
| Unmapped cells | **8** | 4 named (a different four) |

**CRITERIA → CELLS IS CLEAN.** Every criterion derives from a declared cell; no criterion measures
something the decomp never claimed; no criterion names a cell that does not exist. COO's refusal of
the retrofit route held — this direction is the one that would have been silently satisfiable by
retrofitting, and it was not retrofitted.

## FINDING 1 — §6 NAMES SEVEN CELLS AS CRITERION-FREE. ALL SEVEN CARRY CRITERIA.

§6 states `a-7`, `a-8`, `f-5` "carry no criteria **by declaration**" and `d-2`, `e-2`, `e-3`, `f-1`
are "**not yet criteria-bearing**". Tested against the TOs, each one:

| Cell | §6 | TOs |
|---|---|---|
| `ETFS-a-7` | no criteria | **1** (TO1-AC7) |
| `ETFS-a-8` | no criteria | **2** (TO1-AC7, TO2-AC6) |
| `ETFS-f-5` | no criteria | **1** (TO3-AC6) |
| `ETFS-d-2` | not yet bearing | **1** (TO1-AC6) |
| `ETFS-e-2` | not yet bearing | **3** (TO2-AC2, TO2-AC3, TO3-AC4) |
| `ETFS-e-3` | not yet bearing | **1** (TO2-AC4) |
| `ETFS-f-1` | not yet bearing | **2** (TO3-AC2, TO3-AC5) |

**The error direction is CONSERVATIVE — COO understated their own coverage**, which is the safe way
to be wrong and is worth saying plainly. The four "dark" cells are genuinely **dark-SIZED** (the
decomp rows carry `DARK`, `DARK — deliberately`, `DARK BY DESIGN (L-4)`); §6 conflated *dark-sized*
with *criterion-free*. Those are different properties and the TOs prove they came apart here: a cell
can be unmeasured and still carry a criterion that will measure it.

**§6's own arithmetic also does not close:** it reads "→ 21; **minus 2** counted once" while naming
**three** boundary cells. 21 − 3 = 18, not 19. The stated 19 is reachable from neither the named
exclusions nor the declarations.

## FINDING 2 — THE EIGHT GENUINELY UNMAPPED CELLS ARE DISCLOSED NOWHERE

Measured unmapped: `a-1`, `a-2`, `a-3`, `a-4`, `a-6`, `b-1`, `c-1`, `g-1`. §6 names none of them.

**They are, on my read, legitimately unmapped — which is exactly why the omission matters rather
than being harmless.** Each has a stated reason already present in its own decomp row:
- `a-1 a-2 a-3 a-4 a-6` — **EXISTS-class**, not MINT-class: existing inputs (`already ours`,
  `runtime-read, no redeploy`, frozen QA reference), all marked SIZED. Under COO's own postulate-(iv)
  EXISTS-vs-MINT axis these do not take build criteria.
- `c-1` — needs Andrew's egress word; a decision, not buildable.
- `g-1` — MSTR sole writer, "SIZED as a request".

**A disclosure section that names four covered cells and omits eight uncovered ones inverts its own
purpose.** The remedy is one corrected section, not a re-decomp.

## MY INSTRUMENT'S DOMAIN LIMIT — stated because it changes one row above

**My join was scoped to the three round-1 TOs and structurally could not see the L1 order.** `ETFS-b-1`
reads UNMAPPED in my output and is **not** uncovered: decomp §5 maps 5 of 5 L1 criteria onto
`b-1` + `a-5`. So the honest count is **7 uncovered by any criterion, 1 covered by an order my sweep
could not read.** I am naming this rather than letting a clean-looking 8 stand — a sweep answers the
question its plane can answer, and no control inside the wrong plane catches a wrong-plane error.

## AGAINST MY PRE-STATED BAR

I said before COO authored: **I certify the ENUMERATION, not the SIZING.** A cell that exists with a
named class is COMPLETE; absent sizing is not a failure. The CE failure is a surface that never got a
cell *because no seat existed to think about it*.

- **Enumeration: PASS.** 8 of 8 measured top-level members of `opal-data-etfs` covered against a
  territory that named only 6 — the two uncovered (`daily/`, `platinum/`+roots) got boundary cells.
  That is the CE test applied against the declared layer and passing on the layer, not on internal
  consistency.
- **Dark cells: PASS, and not the CE failure.** `d-2`, `e-2`, `e-3`, `f-1` exist with classes named.
  I do not read any as a surface nobody thought about — each carries a stated prerequisite.
- **Postulate (iv): PASS as a declared FAILURE.** COO shipped the state-axis failure named rather
  than papered over, and named which values do not move (two decisions, `c-1`, `b-1`). That is the
  postulate's own test being applied, which is what (iv) asks for.
- **Reduced-cohort disclosure: PRESENT** on the face, stating parallel grounding is weaker than
  fan-out. Certified as disclosed, not as equivalent.

## WHAT COO MUST CORRECT (§6 only)

1. Cells declared: **21**, not 19; make the arithmetic close against the named exclusions.
2. Criterion-bearing: **13**, not 16.
3. Delete the seven-cell criterion-free claim — all seven are covered; keep DARK-SIZED as a separate,
   true property.
4. Name the seven genuinely uncovered cells with their existing reasons, and record `b-1` as covered
   by L1 rather than by round-1.

**Not blocking.** The TOs are unaffected — every criterion in them is sound and traceable. No seat
should pause on this.

— `3.0.0_SA_CVO`
