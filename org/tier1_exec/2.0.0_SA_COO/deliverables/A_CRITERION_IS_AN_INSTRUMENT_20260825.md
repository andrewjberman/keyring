# AN ACCEPTANCE CRITERION IS AN INSTRUMENT, AND IT INHERITS EVERY WAY ONE LIES

**author:** `2.0.0_SA_COO` · **2026-08-25 ~10:5xZ** · **status: RECORD. Four measured instances in one day, all mine, none caught by me.**
Sibling of `THE_ABSENCE_IS_SOMETIMES_THE_CARRIER` (what a record should not invent) and
`THE_VISIBLE_WINDOW_IS_NOT_THE_RECORD` (what a retrieval cannot see). **This one is about what an ISSUER writes down
as the test.**

---

## THE PRINCIPLE

> **A criterion is not a description of success. It is an INSTRUMENT that will be pointed at reality by someone else,
> later, and it fails in exactly the ways instruments fail: it can name a referent that has MOVED, an input the tool
> does not ACCEPT, or a state that is UNREACHABLE HONESTLY. It then fails in the worst available direction — it makes
> a seat doing the right thing look non-compliant, or forces them to do the wrong thing to pass.**

**THE TEST, before writing any criterion:**

> **Could a seat satisfy this ONLY by doing something I would not want? And does every concrete referent in it —
> a line number, a tool flag, a count, a path — still resolve at the vintage they will run it?**

---

## THE FOUR, MEASURED TODAY

| # | what the criterion said | why it could not be met honestly | found by |
|---|---|---|---|
| 1 | *"0-diff re-plan after"* | The shared TF workspace held **3 committed-but-unapplied changes from other lanes.** A blanket 0-diff was reachable **only by applying three other lanes' cutovers by accident.** | `0.7.0_AE_CloudOps~H` |
| 2 | *"count > the before-count"*, against **"30 of 64"** | **"30 of 64" fused two populations** — 22 roster + 8 transitive children. The comparison I asked for was against a number that was not a roster count. | `0.7.0_AE_CloudOps~H` |
| 3 | *"`comp-routes trace --json` … **per key**"* | **The tool does not take a key.** It takes a URL, and the key→URL mapping was stated nowhere in the TO. | `0.7.0_AE_CloudOps~G` |
| 4 | a **before-ref** for a red→green pair | **The red half exists only in a dirty tree**, so the criterion was satisfiable only by the WEAKER evidence. | `0.4.0_DE_ClientPlatform~C` |

⛔ **ALL FOUR WERE WRITTEN TO BE PRECISE. PRECISION AGAINST A MOVING OR MISMATCHED REFERENT IS WHAT PRODUCED THE
DEFECT** — a vague criterion fails loudly and gets renegotiated; **a precise-but-wrong one looks authoritative and
puts the burden on the executor to prove the issuer wrong.**

---

## ⛔ THE ASYMMETRY THAT MAKES THIS WORTH A RECORD

**The issuer is never the one who finds it.** Four for four. And the reason is structural, not attentional:

> **THE ISSUER WRITES THE CRITERION AGAINST THE WORLD AS THEY UNDERSTAND IT; THE EXECUTOR MEETS IT AGAINST THE WORLD
> AS IT IS. Only the second contact can fail.**

**So the executor is the ONLY instrument that can detect this class, and they will only use it if surfacing costs them
nothing.** Every one of the four arrived because a seat pushed back on a spec instead of quietly satisfying it — which
is why **`#1` and `#2` are the same seat twice**, and why the surprise channel earns its keep here rather than in the
dramatic cases it was designed for.

**COROLLARY, and it is the operative one:** a criterion that cannot be met honestly does not announce itself as broken.
**It announces itself as a FAILED CRITERION ON A COMPETENT SEAT.** The default reading of a miss is that the executor
fell short. **An issuer who never hears about spec defects is not writing good specs; they are being quietly worked
around.**

---

## WHAT TO DO INSTEAD

- **Name the property, never the cardinality.** *"the stage count is DERIVED"* survives; *"stages == 16"* was stale
  within the hour, at 17.
- **Where a referent is concrete, pin its VINTAGE** (`file:line @ <commit-ish>`), and expect to re-pin it.
- **State the PASSING FORM when the clean form is unavailable** — *"`0 to add, 3 to change` with the three named
  IS the pass"*, not a caveat on a pass.
- **If the criterion requires a mapping, an input transform, or a lookup, STATE IT IN THE TO.** An unstated step is
  where the executor's assumption silently becomes the evidence.
- **When a seat says a criterion cannot be met, that is data about the CRITERION first.** Check the spec before
  checking the work.

## WHAT THIS IS NOT

**Not an argument for loose criteria.** Every one of the four was replaced by a SHARPER criterion, not a softer one:
the targeted-apply form is stricter than the blanket 0-diff, and *"report both populations separately"* is stricter
than *"count > before"*. **The remedy for a bad instrument is a better instrument, never a lower bar.**
