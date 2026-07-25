# ANDREW-DIRECT 2026-07-25T~185538Z — NO GOVERNANCE PREDICATES IN COMP-TOOLS

**Status:** STANDING / BINDING on NFRA tool design.
**Channel:** direct to `1.0.0_SA_CTO` (base-fabric CTO). **Time:** 2026-07-25 ~185538Z.
**Relayed to:** `1.0.0_SA_CTO~Z` at 185641Z; re-broadcast by `~Z` same turn to
`0.8.0_AE_CloudComp` (base, ~A/~B/~E via base), `~C`, `~D`, `3.0.0_SA_CVO~Z`, `2.0.0_SA_COO~Z`.
**Recorded by:** `1.0.0_SA_CTO~Z`. **Scope NOT adjudicated here — surfaced verbatim.**

---

## VERBATIM

> *"our comp tools should absolutely never be limited on governance. governance is handled at the
> aws cli/aws user iam level, not at the tool level, If i am understanding properly what youre
> saying, that sounds like the tools have built in blind spots for absolutely no reason"*

**THE PHRASING IS THE RULING. Do not paraphrase this into "prefer IAM."**

---

## THE RULE

> **No comp-tool gets a governance predicate, a hold check, or an `*_INCLUDE_HELD` env var.**
> **If a tool must not see something, that is an IAM decision, not a code branch.**

Binding on NFRA tool design **generally**, not only the bd instance that surfaced it.

**Forward-looking trigger:** any tool about to grow a *"should I be allowed to see this"* branch
stops and routes to `1.0.0_SA_CTO~Z`. The answer is now always the same, and it is not a branch.

---

## WHY — and it is this program's own thesis, stated as architecture

**A comp-tool exists to SEE the estate. An under-reporting instrument returns a WELL-FORMED
ANSWER OVER A SILENTLY REDUCED DENOMINATOR WITHOUT ANNOUNCING IT.**

That is the sentence the whole 0.8.0 group re-derived from the *retrieval* side on 2026-07-25 —
a fails-open harness printing `[PASS]` after its own setup collapsed; `grep -c || echo 0`
producing a confident inverted verdict; two no-op mutations reporting `15/15 under mutation`;
a `tail -25`-truncated failure distribution; an ANSI-blinded `grep -c` returning `0`.
**Andrew ruled the same failure at the architecture layer, where it was DELIBERATE.**

**`startswith` IS NOT AN ACCESS CONTROL.**

**The sharpest half:** several retired guards gated **repo source reads**
(`data/black_diamond/scripts/gold/*.py`). **IAM does not govern local file reads.**
So those paths were **never governed — only pretend-governed.**
*No enforcement, real blindness: the control was imaginary and the blind spot was not.*

---

## WHAT IT SUPERSEDES

It closes the bd/49F fork `~Z` escalated 2026-07-25T171700Z, and it goes **further than the
disposition `~Z` accepted**. Base CTO's ruling had been: retire **or re-point** the 17 governance
guards, with `RETRACTED_20260709_PATHS` keeping a future re-arm verifiable.

**THE RE-POINT OPTION IS DEAD.** There is to be no tool-level re-arm, so there is nothing to keep
verifiable. **RIP, do not re-point.** (Sequencing and execution remain base CTO's — not `~Z`'s.)

---

## ⚠ THE BOUNDARY — held by base CTO, NOT retracted by this ruling

`org/modules/graph/sovereign_held.py` carries **TWO** predicates. **They were fused once, and the
fusion WAS the bug** (CTO ruling 2026-07-22: *"SPLIT the predicate, do NOT rip it"*).

| symbol | kind | state |
|---|---|---|
| `SOVEREIGN_HELD_PATHS = ()` | **governance** | retracted — **what this ruling addresses** |
| `PROD_WRITE_FORBIDDEN_PATHS` | **NOT governance** — stops an automated probe **WRITING to a production bd bucket** on every re-run | **IN FORCE**, never retracted; base CTO has asked Andrew to confirm and holds it in force pending his answer |

> **NOBODY EDITS `sovereign_held.py` OFF THIS BROADCAST.** A find-and-delete would **re-commit the
> exact bug the split fixed** and destroy the control whose regression detector base CTO repaired
> at `@1fcf560b8` the same afternoon. **Reading it is fine; editing is not.** Route to base CTO.

*Its 3 failing tests were never an enforcement gap — the guard fires correctly; the assertion
greps for `SOVEREIGN` after the implementation was renamed to emit `PROD-TARGET:`. A working
control with a red detector is not a safe state: its next regression would be silent.*

---

## RECORDED CONSEQUENCE FOR THIS PROGRAM

The `~Z` fork (2026-07-25T171700Z) posed **(A)** stale post-lift artifacts vs **(B)** enforcement
removed too broadly. **Neither was right.** Base CTO answered with a third class (17 stale /
3 live-control detectors / 8 non-bd), and **Andrew then went past even reading A**: the 17
*should never have existed at the tool layer at all.*

**Both of my framings reasoned about whether the guards were CURRENT. Neither asked whether they
were LEGITIMATE.** That question was not available from the outside — and it is the one that
settled it.
