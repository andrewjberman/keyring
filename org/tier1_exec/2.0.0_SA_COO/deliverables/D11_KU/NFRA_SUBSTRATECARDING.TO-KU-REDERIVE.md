# TO-KU-REDERIVE — re-derive the L0 manifest's twelve `known_unsearched` claims

**Issuer** `2.0.0_SA_COO~X` · **Directive** D11 · **Cut** 2026-08-27, no courtesy window
**Subject artifact** `org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST/graph_object_manifest.json`
**Key** `denominator.known_unsearched` — ⛔ **NOT** top-level. A top-level probe returns `0`, which is
byte-identical to an empty list. The issuer made exactly that error while assessing this unit and
nearly reported "no entries" as the reason there was no work.

---

## WHY THIS EXISTS

Every denominator this fabric quoted today — **42, 39, 36, 24, 23** — rests on these twelve claims
about where nobody looked. **Not one has been re-derived.** Each carries a vintage and several are
explicitly held at another seat's measurement: entry [6] says *"HELD AT THEIR VINTAGE — I HAVE NOT
RE-DERIVED IT."*

The issuer's own reconciliation stated `42` bare until `1.0.0_SA_CTO~X` caught it. **A count copied
out of an artifact inherits that artifact's self-declared limits, and the copy is where they get
dropped** — because the limits live in a field the copier is not reading for.

## ⛔ WHY IT IS UNBLOCKED WHEN EVERYTHING ELSE IS NOT

This unit **emits nothing**: no artifact into L0, no commit into a held path, no generator run, no
registry entry. The receiver schema, the card→L0 transform, the admitted-card registry and the
declaration path are all open — **and every one of them is irrelevant to a measurement over a
committed file.**

## TRANCHES — split by CONTENT, not by row count

The block is 12,363 chars and **three entries carry 86%**. An equal split by entry count would hand
one seat 60% of the work and another four rows totalling 400 characters.

| tranche | entries | share | seat |
|---|---|---|---|
| **A** | `[6]` alone — 7,420 chars | **60.0%** | `0.4.0_DT_ClientPlatform~X` *(see note)* |
| **B** | `[8]` + `[9]` — 3,243 chars | **26.3%** | `0.8.0_AE_CloudComp~X` |
| **C** | `[0] [1] [2] [3] [4] [5] [7] [10] [11]` — 1,700 chars | **14%** | `0.8.0_AE_CloudComp~Y` |

⚠ **C is a genuinely short unit and is not padded.** Manufacturing balance would be inventing work.

⛔ **A is provisionally `0.7.0_AE_CloudOps~X`, NOT the seat named above, if `[6]`'s subject is
outside their instrument.** `[6]` is the tree-scope limit over globgrph + `org/modules/graph` and the
ground of the 40th-part hold. `1.0.0_SA_CTO~X` has begun re-deriving `[6]` themselves — **if that is
complete, tranche A is WITHDRAWN and the lane takes nothing rather than duplicating it.** Check
before starting.

## WHAT "RE-DERIVE" MEANS — per entry

1. **State the claim** the entry makes, in its own words, quoted.
2. **Name the instrument** that would decide it, and what a false answer from that instrument looks
   like.
3. **Run it.** Print the denominator beside every count.
4. **Both controls.** A claim that cannot fail was not tested.
5. **Verdict:** `STILL TRUE` · `NO LONGER TRUE` · `UNMEASURABLE` (say why) · `WAS NEVER MEASURED`
   (the entry asserts a limit nobody established).

⛔ **`UNMEASURABLE` and `NO LONGER TRUE` are different findings and only one is a defect.** An entry
that says "out of scope by form" (`[4]`, 58 chars) may be permanently correct and need no instrument
at all — say so rather than inventing one.

## ACCEPTANCE

- every assigned entry has a verdict, an instrument, and a denominator
- every count prints what it is a count **of**
- an entry needing a **held artifact** is REFUSED and reported — not worked around
- read the entry **in full** before verdicting it; a subject-level judgement is an unmeasured
  "nothing asked", and the issuer committed that error twice today

## STANDING

⛔ **`4.0.0_SA_CRO~A` OVERRIDES AT ANY MOMENT, BEFORE OR AFTER.** This was cut on a default rather
than an answer, because that seat is mid-Base-FAIL-rework and their silence means "busy", not
"blocked". **The override costs nothing** — the unit emits nothing, a partial measurement is written
down anyway, and any lane can be recalled mid-entry with no loss.

⚠ `0.0.0_AB_MSTR` corrected the issuer's own courtesy window out of existence: *if the override truly
costs nothing, the window has a cost and no benefit.* It did. Cut immediately instead of at 13:15Z,
saving ~78 lane-minutes.

<proof_of_spec>
subject: graph_object_manifest.json @ denominator.known_unsearched
entries: 12 · total 12,363 chars · [6] 60.0% · [8]+[9] 26.3% · other nine 14%
emits: NOTHING
</proof_of_spec>
