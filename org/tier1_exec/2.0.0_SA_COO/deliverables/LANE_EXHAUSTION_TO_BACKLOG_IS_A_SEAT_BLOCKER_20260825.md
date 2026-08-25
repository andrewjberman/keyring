# ⛔ UNCLOSED TASK ORDERS ARE EXHAUSTING LANE LETTERS — SPRING CLEAN IS A SEAT-ALLOCATION BLOCKER, NOT HYGIENE

**found by:** Andrew, 2026-08-25 ~17:5xZ, from an operational symptom nobody had connected to the TO backlog
**measured by:** `2.0.0_SA_COO`, same turn
**status:** finding, recorded. **Remedy is CTO~X's spring clean, re-prioritised on this basis.**

---

## HIS WORDS, VERBATIM

> *"Yeah we need to really start cleaning out those TOs because theres so much shit piled up in there
> that now every time we spawn an agent we're spawning DS~N and so on because probably all the other
> ones have random stuff piled up."*

**He is right, and the mechanism is worse than pile-up.**

---

## THE MEASUREMENT

```
SERIALS / LANES CARRYING >=1 OPEN TASK ORDER

  0.4.0_DS_ClientPlatform      open=89   10 lanes   A,B,F,G,I,J,K,M,Z + base
  0.7.0_AE_CloudOps            open=76    8 lanes   A,B,D,E,G,H,Z + base
  0.8.0_AE_CloudComp           open=74    7 lanes   A,B,C,D,E,Z + base
  3.0.0_SA_CVO                 open=17    3 lanes   A,B + base
  1.0.0_SA_CTO                 open=15    1 lane    (base only)
  0.5.0_AE_OpalETL             open=14    3 lanes   B,Z + base
  0.4.0_DE_ClientPlatform      open=13    4 lanes   C,D,Z + base

  TOTAL distinct serials/lanes holding >=1 open TO:   58
  TOTAL open TOs attributed:                         364
```

*Predicate: non-complete by CLOSED-PREFIX match over `<status>` with the `**Status:**` markdown
fallback, `<issued_to>` serial extraction incl. tilde suffix. Reconcile denominators to `to-check`;
this is reported as a RATIO and a SHAPE, not as a competing total.*

---

## ⛔ THE MECHANISM

**One-project-per-Tier-2-instance** (Andrew-direct 2026-08-24) **+ task orders that are DONE but never
marked CLOSED** = **every lane letter is "dirty", so a fresh spawn must mint a new one.**

> **A TASK ORDER THAT FINISHED BUT WAS NEVER CLOSED PERMANENTLY CONSUMES A LANE LETTER.**

**Closure is a RECORD act with no immediate consequence to the seat that skips it** — so it is skipped
— **and the cost lands somewhere nobody was looking: at spawn time, on a different day, on a
different seat.** `DS` reached `~M` today and `~N` within the hour. **The alphabet is finite.**

### AND IT COMPOUNDS

**Context is per-instance.** Every burned lane is another partial picture of the same project. **The
fabric fragments in proportion to the backlog** — which is the fragmentation this day's P0 kept
colliding with (four seats, four partial views, six mutual corrections).

---

## ⛔ WHY THIS REFRAMES A WHOLE WORKSTREAM

`1.0.0_SA_CTO` measured this morning that **seats are the binding constraint**:

> *"FOUR EXECS AND ZERO TIER-2 WORKERS. Against that: 40 open TOs... Nothing on the board can move
> until seats exist. That is the binding constraint, not decomp capacity."*

**Spring clean is not adjacent to that problem. IT IS THAT PROBLEM.**

| framing | priority it earns |
|---|---|
| *"consistency debt / records tidiness"* | queued behind real work, indefinitely |
| **"the reason we cannot allocate a clean seat"** | **it is the seat supply** |

**CLASS A is the cheapest lane-letter recovery available:** open TOs sitting on projects **already
marked terminal** — `1.0.0_SA_CTO~X` measured **65 of 75 (87%) mechanical, 10 judgment**; my own
prefix-scan variant read 97/39 with **the same 10** in the judgment set. **It needs NO sovereign bar
and NO threshold ruling.**

⛔ **AND IT STILL RUNS THE PRE-FILTER:** TO-last-touched vs project-JSON-last-touched; the
newer-than-close set goes to a human read, never the sweep. **Closing those 10 blind would erase the
only evidence a project was closed prematurely** — `OPAL_ASSETS.BDMERGE-CONVERGE` reads *"pending —
go received"* on a project marked terminal.

---

## THE GENERALISABLE FORM

> **A record act with no immediate consequence to the actor, whose cost is paid later by someone
> else, will not be performed — and the estate will misread the resulting scarcity as a property of
> the resource rather than as unpaid debt.**

**We were minting new lanes as though lanes were scarce. Lanes are not scarce; CLEAN lanes are.** The
symptom presented as a spawn-naming quirk and is a closure-discipline defect two layers up.

*This is the same shape as the day's other findings: the object that cannot distinguish "never ran"
from "ran and refused"; the freshness field that moves over frozen content. **A signal that looks like
one thing and is produced by another, with nothing in the artifact saying which.***

---

## DISPOSITION

- **Remedy: CTO~X's spring clean S1/S2, re-prioritised on this finding.** No new work item minted.
- **`1.0.0_SA_CTO~X` CAN commit these** — verified against the resolver (`check_agent()` tilde-strip,
  RV-0030 F-003): **10 of 10 TO-bearing lanes**, despite reading 0 of 10 on a literal `permitted_agents`
  scan. **No lane enumeration or governance edit is needed.**
- **Not proposed here and not implemented:** any gate requiring TO closure. **That would be a new gate
  and needs Andrew's explicit word** (NEVER: no manufactured gates). *Recorded as a candidate only.*
