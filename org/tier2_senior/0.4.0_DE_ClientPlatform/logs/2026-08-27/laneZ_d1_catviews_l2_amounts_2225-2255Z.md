# I inverted a comment that was already right, and my generic weight function was sound arithmetic about a world that does not exist

**archetype:** BUILD
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE

**Date:** 2026-08-27
**Project:** D1_CATVIEWS (Rule 27 — this instance's only project)
**Window:** 2026-08-27T22:25Z -> 22:55Z

**Portal commits (DEV):** `e56f3a80` (ON ORIGIN) · `20373baa` (LOCAL at last read)
**Workspace commits (SITEZ, LOCAL):** `c053078269`

---

## Objective

Andrew-direct ~22:3xZ: *"the drilldowns show AUM amounts and also are visually structured a little
better with colored dots on the left and asset value on the right and no parentheticals needed."*
Build it, record it, and route the half that is not this lane's.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `bun run typecheck` | `tsc -b --noEmit` x2 | PASS rc=0 | 13.2s, build-mode band. Not re-run for the fixture-only commit — it could not have changed the answer. |
| `bun run lint` | `eslint .` | PASS rc=0 | 0 errors / the same 7 pre-existing warnings. |
| `comp-find` | `-i "category-views.fixture" --all` | PASS | 6 hits / **27,312 scanned**, all inside `.frontend-dev/`. The denominator is the point. |
| `ui-smoke.mjs` | 5 renders, `--select` x4, `--click` x3 | PASS | Every state READ. One `--click` failure's DIAGNOSTIC was the finding (`$0.00`, no `M`). |
| `safe-commit.sh` | 3 commits, two repos | PASS | |

---

## Work Completed

1. **`e56f3a80`** — L2 rows take the L1 idiom: dot left, name, amount right. `(third bucket)` and both
   editorial asides removed. `MdpfCategoryMember.aum` added, **optional + nullable**.
2. **`c053078269`** — the Andrew-direct recorded verbatim.
3. **`20373baa`** — fixture member amounts re-derived to match the sovereign record.

⭐ **His two instructions were connected, and that is what made the third safe.** The L2 caption
existed under COO render rule 67612 because the list carried **no numbers of its own** beside an L1
figure that was not about it — *the adjacency lied*. Per-member amounts remove the precondition, so
the caption would be **FALSE under amounts, not merely redundant**. `2.0.0_SA_COO~Z` ruled RETIRE and
said the rationale **corrected their own first reading** of their own rule.

---

## Decisions Made

- **Surfaced the caption retirement to its owning office instead of just doing it.** Retiring another
  office's control is theirs to confirm.
- **Did not edit `formatAUM`.** Shared exported helper, correct in general. Named for Andrew.
- **Did not invent UI for `absent_reason`.** Then discovered the question itself was mine, not his.
- **Volunteered that my own fixture is not independent evidence** — it was derived from
  `mdpf_category_registry.py`, so a match with the served artifact is *the producer agreeing with a
  restatement of itself*. COO amended `TO-P1-AE` on it before the AE lane compared anything.

---

## Blockers

**None.** Per-member `aum` is an **EMIT gap** (the consolidator already carries the grain), routed to
the DS lane. Client still has no L2 anywhere in the record — Andrew's.

---

## Postmortem — three, and they are not the same error

**1. ⛔ I INVERTED A COMMENT THAT WAS ALREADY TRUE, COMMITTED IT, AND BROADCAST IT TO THREE SEATS.**
`aum.ts` said a no-members node *"renders no tile at all."* **True.** I rewrote it to say the opposite
and shipped that at `875182fc`. **How:** I grepped the renderer for `members_present` /
`render_state` / `absent_reason`, found it reads **none** of them, and inferred the card must
therefore render. Suppression does not run through those flags — the emitter sets `aum = 0.0` in the
*same branch*, and **the zero carries the suppression** through the presence predicate. **Two
sufficient paths to one outcome; I checked the one I had searched for and concluded from its
absence.** Measured by *rendering* the scope, which was available the whole time.
⛔ **And the question I escalated off it was manufactured by it** — "should a zero node render?" was
already answered in code. Withdrawn from the sovereign queue. `1.0.0_SA_CTO~Z` elevated the mechanism
to a rule; `3.0.0_SA_CVO~Z` added the sharper mirror: **a true conclusion with a WRONG mechanism is
worse than one with none — an absent mechanism propagates as a gap, a wrong one as a citation.**

**2. ⛔ MY WEIGHT FUNCTION WAS SOUND ARITHMETIC ABOUT A WORLD THAT DOES NOT EXIST.** To give every
member an amount I split each bucket across **all** its members. Total, exact, count-agnostic, no
special cases — **and it asserted cottonwood holds PFOE/IDVZ/PFDE and that every firm holds IDVZ and
PFDE SMAs**, against three of his statements. ⭐ **The genericity was the defect:** the function had
no way to express *"this firm holds none of that."* I verified the invariant I had built and never
asked whether the output contradicted the record. **A fixture is not exempt because its figures are
invented** — three seats read this file as the shape contract, and an invented *tree* teaches the
wrong one.

**3. A count-keyed table silently SKIPPED two buckets**, leaving exactly the drilldowns the change
exists to populate rendering `--`. Caught by reading the writer's own per-bucket output rather than
its exit code. The rewrite asserts **coverage with a printed denominator**.

⭐ **THE ONE THAT WENT RIGHT, AND IT IS THE SAME SHAPE THREE TIMES.** `1.0.0_SA_CTO~Z` raised a
fixture-fallback hazard; I measured my own artifact against it — **zero `src/` references with a
positive control on the sweep**, not under `publicDir`, served out-of-process at the transport layer —
and then **exercised** the acceptance arm rather than leaving it written: proxy killed, panel renders
*"Category views are not available at this scope."*, never a number, and the same route renders three
cards with the proxy up, **so the instrument was shown capable of both answers**. Hazard withdrawn and
upgraded into a four-part reusable test. **Postmortems 1–3 are all "I reasoned instead of measuring";
this is what the same half-hour looks like when the measurement comes first.**
