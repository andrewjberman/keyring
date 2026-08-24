# CERT — D1_CATVIEWS stage-3 decomp

**Certifier:** `3.0.0_SA_CVO` · **Requested:** COO 66128 · **Subject:** `workflows/atom_decomposition/runs/d1-catviews/20260824T132611Z/DECOMP.md` @3b103f1298
**Date:** 2026-08-24 · **Subject is LOCAL at cert time** (rides the integration window; stated rather than called landed).

## VERDICT

**CERTIFIED on the ENUMERATION. The criteria→cells direction is NOT YET EVALUABLE and I am recording
that as its own state rather than as a pass or a failure.**

## MECHANICAL

| | measured | COO stated |
|---|---|---|
| cells declared | **14** | 14 |
| mentioned-but-not-declared | **∅** | — |
| declared-but-never-mentioned | **∅** | — |
| criteria carrying `cell_refs` | **0** (no TOs cut) | 0 |

⛔ **MY EXTRACTOR WAS WRONG TWICE BEFORE IT WAS RIGHT, AND THE FIRST WRONG ANSWER WOULD HAVE
FALSELY REFUTED THE EXACT THING COO BUILT IN RESPONSE TO MY LAST REFUSAL.** It required a
backticked cell id in a leading table cell — the format of the *previous* decomp. `D1-inv-1/2/3` are
declared in **bold** (`| **D1-inv-1** |`), so my first pass reported **11 of 14** and the three
missing were precisely the invariant cells COO cut first on my own ETFS finding. **A shell "fix"
then broke it the other way (3 of 14, backtick eaten by quoting) before a Python re-implementation
gave 14 with both symmetric differences empty.** *I encoded one document's formatting as if it were
the schema; that is the instrument-domain class, self-caught, third time today.*

## THE ZERO IS VACUOUS, NOT SATISFIED — AND MY OWN CHECKER CANNOT SAY SO

COO asked me to refuse a vacuous pass rather than compute over an empty set. **They are right, and
it exposes a defect in my instrument that I am recording here rather than in a postmortem.**

With **0 criteria**, `align_check.py` reports **14 unmapped cells / MISALIGNED / rc=1**. That is
arithmetically true and **framed wrong** — it reads as *the decomp failed alignment* when the true
state is *no task orders exist yet, so the direction has no domain*. **My checker cannot distinguish
NOT-YET-EVALUABLE from MISALIGNED, and both render identically.** Same missing-state-value shape as
the two I reported earlier today (my channel schema's absent disarm state; the deploy ledger's
absent HELD state) — **three instances in one day of an enum lacking a value for a state that
actually occurs.**

**So the certified statement is: cells→criteria is UNEVALUATED, by construction, and correctly
disclosed by the author before I could raise it.**

## THE SOVEREIGN-WORD QUESTION — COO DID NOT NARROW, AND THE STRUCTURE IS WHY

COO flagged this as the one to refuse on. **I read Andrew's words at source rather than COO's
characterisation of them.** Verbatim (2026-08-24 ~12:4xZ):

> *"the project to bring in the model portfolios new taxonomy needs to be figured out … come to a
> definitive ruling on how to **handle** Primary vs Custom Models as a bifurcation of 'Models',
> which means we should probably beeline to figure out 'SMAs' 'Client' and the others."*

**"How to HANDLE" and "how to INCORPORATE" are execution verbs.** The 08-19 gate had already ruled
the stored 5-enum, Models = Primary + Custom as a MECE partition, SMA as the display word for stored
`strategy`, and Client = Advised + Residual — and the registry module is built. **COO's reading is
the better-grounded one.**

⛔ **BUT THE DECIDING POINT IS NOT THAT THEIR READING IS RIGHT — IT IS THAT THEY DID NOT DECIDE IT.**
They made the open question a **CELL** (`D1-g-1`) instead of a footnote. **Turning an ambiguity into
a visible, ownable unit of work is the opposite of narrowing a sovereign word** — narrowing would be
resolving it silently and proceeding. A fresh seat reading his words cold *would* reasonably start
re-deriving the taxonomy, and the cell is what stops that without pre-empting him.

**Residual ambiguity, stated because it is real and is HIS to close, not ours:** *"come to a
definitive ruling"* can read as *rule it again* rather than *execute the existing ruling
definitively*. **Nothing in the decomp forecloses either reading** — which is exactly why it
certifies. If he means the wider one, `D1-g-1` is where it lands.

## WHAT I DID NOT INDEPENDENTLY RE-DERIVE

**COO's (e)-axis correction** — measuring the axis as HARDCODED-MODEL-VOCABULARY with three values
(per-firm 1, per-vintage 4, per-served-artifact 4) where the PRD said "per-firm". **I did not
re-run that census.** On its face it is an **axis correction, not a scope widening**: a per-firm
cell would have enumerated one site and missed six, which is a collective-exhaustiveness failure
against the declared layer. **Certified as a stated measurement, not as one I reproduced.**

Also not re-derived: the SERVED_MODEL_NAME false-defect (7 vs 5 entries, differing hashes, each
verified against its own served artifact). **Recording a false defect *as* a false defect is the
behaviour that stops it being re-filed** — third instance today of that save.

## AGAINST MY PRE-STATED BAR

- **Enumeration: PASS.** Invariant cells cut *before* artifact cells, on the ETFS lesson that an
  enumeration over artifacts cannot see an invariant between planes. `D1-inv-1` turning out to be
  the project's real content is evidence the correction was right, not a coincidence.
- **Dark cell `D1-f-1`: PASS, not a CE failure.** The 15/85 node placement is genuinely the thing
  Andrew's word leaves open; it exists with a class named.
- **Postulate (iv): PASS as a declared FAILURE** on BUILT/MINT/OPEN-RULING, shipped as a failure
  with the non-moving values named.
- **Reduced-cohort disclosure: PRESENT** on the face.

**Nothing blocks. No TOs are affected because none are cut.**

— `3.0.0_SA_CVO`
