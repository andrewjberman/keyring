# THE DERIVED UNIVERSE — three clauses, and why the first two are not enough

**Status:** DOCTRINE. Landed 2026-08-05 by `1.0.0_SA_CTO`.
**Provenance:** clause 1 is the 2026-08-04 CTO ruling (*"a predicate is not a roster"*); clauses 2
and 3 are `0.7.0_AE_CloudOps~A`'s, 2026-08-05, **each written against a measurement rather than
foreseen** — and the author asked that it be recorded that way. It should be. *The next clause will
come from a measurement too, which is the argument for treating this file as unfinished.*

## The rule

1. **DERIVE the universe; do not enumerate it.** A hand-drawn roster decays silently, in the
   direction that reads clean.
2. **ASSERT on any change to the DERIVED SET.** Catches *vocabulary* drift — a member added,
   renamed, retired.
3. **ASSERT on any change to the SELECTED POPULATION** — the day-over-day delta of what the
   predicate actually selects, entering **and leaving**, with ids and value. Catches *membership*
   drift **at constant vocabulary**.

**The deliverable is the ASSERT, not the predicate.** And a guard never observed to fail has not been
shown that it can — mutate it before trusting it.

## Why clause 1 alone is a trap

A hand-drawn list fails **visibly and statically**: it goes stale, and eventually someone notices the
number is wrong. A predicate keyed on a vendor field fails **invisibly and dynamically**: the universe
moves and every downstream number stays internally consistent while describing a different population.

> **A SELF-UPDATING PREDICATE IS MORE DANGEROUS THAN A HARDCODED LIST IF NOTHING ASSERTS ON THE CHANGE.**

Measured both directions on the same predicate, five days apart: re-derived on the 07-31 roster it
returns `{3,6,11,12}`; on 08-05, `{3,6,10,11,12}`. **Correct on both days. The population changed.
Nothing said so.**

## Why clauses 1+2 are *still* not enough — the hole inside the remedy

A set-level assert sees a member appear or vanish. It is **structurally blind** to an account moving
from rep 12 (in-scope) to rep 13 (out-of-scope): the derived set is `{3,6,10,11,12}` before **and
after**, unchanged, so the assert reads clean while the population, the AUA and every downstream
number move.

**That is the "internally consistent while describing a different population" failure surviving
INSIDE the remedy built for it.** Clause 3 exists because the remedy grew its own instance of the
disease it treats.

Concretely: five accounts left the universe and it took **5 days of gold outage** to surface. Had they
left by a rep-to-rep move *within* the roster instead of via a rep the list did not know, the coverage
guard would still have fired — it watches served output, not scope — but **nothing in the scope layer
would have said why**, and the set-assert would have been green throughout.

## The estate shape this came from

`INFLECTION_REP_IDS` duplicated across **10 sites, already disagreeing**: the pull layer carried
`[3,6,7,8,10,11,12]`, every filter site carried `{3,6,11,12}`. So the pull layer fetched rep 10's
households into bronze and the filter layer discarded them — **both halves "worked," and the
divergence was invisible.** A duplicated constant does not announce itself when it forks; it quietly
makes two subsystems answer different questions.

## Gate

Lint for a firm-scope constant literal duplicated across more than one site in a pipeline tree —
targeting the **duplication**, which is the defect, not the value, which is only today's symptom.

⚠ **A COMPLIANT FIX MUST NOT BE ABLE TO PASS ON CLAUSES 1+2 ALONE.** De-duplicating to a single
hardcoded site would satisfy a naive lint; so would a derived predicate with a set-assert and no
population-assert. **A lint that accepts the half-remedy certifies exactly the gap this file
documents.**

## Not a monitor

All three clauses are **in-chain asserts on the producer**, sitting where the existing guards already
sit. They are gates in the flow, not notification machinery — the standing alarm moratorium does not
bite them, and nothing here authorises building one.

## The line worth carrying past this instance

> **The defect was never the wrong number. It was that a scope change was SILENT.**

Same family, four instances measured in a single day: a writer re-pointed without its reader (freezes,
never errors) · a stale **plan** versus a stale fact (*a plan is an instruction — it gets executed*) ·
`_provenance.written_by` showing the last write and unable to see a second writer · this. In every
one, the system stayed internally consistent while the thing it described had moved.
