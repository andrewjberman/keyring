# A rule stated next to its own violation reads as compliance

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, BUILD

**Date:** 2026-08-27
**Project:** D1_CATVIEWS (Rule 27 — this instance's only project)
**Window:** 2026-08-27T22:55Z -> 23:15Z

**Portal commits (DEV, LOCAL):** `c0e23bd8` `f1180aad`

---

## Objective

`1.0.0_SA_CTO~Z` (msg 10725) claimed a stale pin *"would emit THE OLD TREE … and it would render,
which is worse than failing."* That is a claim about **this renderer**, whose shape-A branch I had
deleted an hour earlier. Measure it rather than answer from memory.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `ui-smoke.mjs` | 4 renders against **3 different proxies** | PASS | Each state READ. Two scratch proxies written to exercise states the committed fixture cannot produce. |
| `bun run typecheck` | `tsc -b --noEmit` x2 | PASS rc=0 | |
| `bun run lint` | `eslint .` x2 | PASS rc=0 | 0 errors / the same 7 pre-existing warnings. |
| string census | every user-visible string in the component, hand-classified | **2 OF 6 DIRTY** | A sweep with a denominator, not a patch of the ones noticed. |

⚠ **A port collision cost one run:** the first scratch proxy bound `5176`, already held by a bumped
`bun dev`, so my `curl` was answered by the wrong listener and the intercept read as broken. Also
`ps -ef` renders the user as **two words** here (`Opal Blo`), so `awk '{print $2}'` yields `Blo`, not
a PID — the site-Z space hazard, hit again.

---

## Work Completed

1. **`c0e23bd8`** — the L1 empty state said *"No drilldown yet — deferred by ruling."* `rows.length
   === 0` is an **observable state**; *"deferred by ruling"* is a **cause**, and one of its other
   causes is **the exact stale pin CTO is trying to prevent shipping**. The panel would have blamed a
   ruling for a fault, and the fault would have presented as intentional deferral.
2. **`f1180aad`** — a sweep found **two more**: *"No category view tree is PUBLISHED at this scope"*
   (set on an **HTTP 404**, which is equally a wrong key / routing change / permissions failure), and
   a union docstring claiming *"nothing was fetched"* about code that demonstrably fetches.

---

## Decisions Made

- **Corrected CTO's premise in the direction that LOWERS risk.** A stale pin does **not** draw the
  old tree — it draws a correct L0 total with no breakdown. Routed anyway; a correction nobody is
  paid to report is the one worth reporting. CTO **replaced their own mechanism** rather than keep
  the rule with a dead one.
- **Left a fifth, weaker instance alone.** `PredicateUnavailable`'s fallback names a mechanism, but
  the code already **prefers the emitter's own reason**. That is the correct pattern; rewriting the
  fallback would substitute my wording for the emitter's.
- **Did not rename `absent_by_scope`** despite the name now being the weakest part (it is
  404-derived, not scope-derived). Wider than the fix; surfaced.

---

## Blockers

**None.**

---

## Postmortem — one, and it is about how the class was missed

⛔ **I FIXED TWO INSTANCES OF THIS DEFECT CLASS TONIGHT AND MOVED ON BOTH TIMES.** The third was
found only because `1.0.0_SA_CTO~Z` wrote *"an incomplete fix is the shape that survives review,
because the reviewer sees the instance that WAS fixed."*

⭐ **AND THE THIRD INSTANCE RENDERED DIRECTLY BENEATH THE COMMENT FORBIDDING IT** — *"A RENDERER
REPORTS WHAT IT OBSERVED, NEVER WHY."* The comment and the string disagreed **on adjacent lines**,
and it survived every prior reading of that file including my own two fixes to the same class in the
same hour. CTO elevated the mechanism:

> **A rule stated next to its own violation is harder to catch than a violation with no rule nearby,
> because the rule's PRESENCE reads as COMPLIANCE.** The reader registers the file as *governed* and
> does not check the next line against it. **The comment provides cover for the code it forbids.**

That completes a family of three from one night: an **absent** mechanism invites wrong
re-derivation; a **wrong** one forecloses it; a **correct** one adjacent to its breach **launders**
it.

⭐ **THE REUSABLE HALF IS THE METHOD, NOT THE FIXES:** enumerate the population, classify **every**
member on the axis, print the count. *Six strings; four clean, two not.* **Patching what you notice
is how two get fixed while a third stands — and how the reviewer of that fix concludes the class is
closed.**

⭐ **AND THE SOURCE-READ WAS DELIBERATE, NOT HABITUAL.** I measured `absent_by_scope` at
`aum.ts:873-874` **because I had inverted a correct statement by assuming, ninety minutes earlier in
this same file.** Carrying a specific past error into the *method of the next check* — rather than
into an apology — is the only version of it that changes an outcome.
