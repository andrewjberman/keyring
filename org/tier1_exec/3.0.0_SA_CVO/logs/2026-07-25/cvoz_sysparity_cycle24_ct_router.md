# CVO~Z — SYSPARITY cycle-24: `ct-router` — the cycle where the estate was STRONGER than its record

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27` · vintage worktree @ `084ca2f76`

---

## Gate

`comp-system --check` → **SYSTEM CURRENT** (24 regions / 6 files, 0 drifted). Proceed.

## Unit

```
id:    ct-router
desc:  "router / comp-which documented"
check: { type: grep_present, files: [infra/system/03_comp_tools.md], pattern: "comp-which|router" }
```

## VERDICT: **DRIFTED** — but for the OPPOSITE reason to every prior cycle

### F1 — the check violates the OR-boundary I landed 20 minutes ago (III-d.20)

`comp-which|router` mixes a **PROPER NOUN** with **GENERIC VOCABULARY**. Per the boundary: such a
disjunction **has the sensitivity of the generic term.** Measured: `comp-which` = 4 hits, `router` = 2.
**Delete every `comp-which` mention in the file and the check still passes on `router`**, a word that
appears in ordinary prose about routing.

**First live application of that boundary, and it lands on a unit in my own register.** This is the
`ct-catalog` shape (`catalog|tools_index|ledger`) that cycle-10 migrated off — same defect, unmigrated,
flagged per the flag-as-hit policy.

### F2 — the doc UNDER-represents an instrument that is far stronger than its one parenthetical

`03_comp_tools.md` names the routing-quality harness **once**, in a parenthetical at line 26 — *"(the log
COMPROUTE + the routing-quality harness read)"* — and characterises nothing about it.

What the instrument actually is (`.tools/comp-which-routing-test.py`, 1,600 lines):

| property | measured |
|---|---|
| organic cohort | **562 distinct real user questions**, frozen — drawn from **9,100 route events / 740 distinct questions / 563 organic singletons** |
| frozen-not-derived | *"A cohort re-derived from an append-live log is not a population, it is a timestamp, and the regression it reports is uninterpretable"* |
| negative control | 40 seeded gibberish questions |
| positive control | a declared known-good query |
| `TOPK = 3` | **"Andrew-direct: k=3, NEVER 1. Not a tuning knob."** |
| `UNEVALUABLE` | a distinct outcome that **must never fold into MISS** — *"a false 'does not route' is worse than an honest 'could not confirm'"* |
| self-consistency disclaimer | cohort C is *"a SELF-CONSISTENCY check, NOT a coverage measurement, and it must never be read as one — exactly the anti-correlated design this harness was rewritten to stop reporting as a headline"* |

**None of that is represented.** A reader of the doc learns the rail's enforcement tiers in fine detail
and learns essentially nothing about how routing quality is measured or what its limits are — while the
same doc **makes a routing-quality claim of its own** (the `1.85` datum, cycle-22 F4).

>> **EVERY PRIOR CYCLE FOUND A DOC CLAIMING MORE THAN THE ESTATE DELIVERS. THIS ONE FOUND THE ESTATE
>> DELIVERING MORE THAN THE DOC CLAIMS — and that direction is not harmless. It leaves a well-built,
>> carefully-caveated instrument invisible to the readers most likely to misuse the thing it measures,
>> and it means a hand-measured one-off number sits in the doc where the instrument's own output should.** <<

## THREE HYPOTHESES, THREE REFUTATIONS — the real story of this cycle

I formed three findings this cycle and **the implementation killed all three.** Recording them because the
refutations are the content:

1. **"The harness doesn't run the real router"** — from a comment saying `_run_comp_which` is *"unused by
   the live path."* **FALSE.** The live path flipped to a **warm** runner that still executes the real
   comp-which; the old subprocess version is deliberately retained as *"the only independent oracle"* for
   a post-flip regression check. Good engineering, documented in place.
2. **"Self-routing is a tautology nobody noticed"** — **FALSE, and pre-empted in writing.** The authors
   named it, scoped it as cohort C, and explicitly forbade reading it as coverage. My finding would have
   been a re-discovery of a disclosed limitation, presented as new.
3. **"Nothing measures routing against real user phrasings"** — **FALSE.** Cohort R is 562 organic
   questions off the live rail log.

**Two of my three would have been filed against an instrument whose authors had already written down the
exact limitation I was about to report.** The only thing that stopped each was reading the implementation
instead of the fragment that suggested the hypothesis.

>> **A DISCLOSED LIMITATION IS EVIDENCE OF RIGOUR, AND RE-DISCOVERING IT AS A FINDING PUNISHES THE
>> DISCLOSURE. If I file it as new, the rational response is to disclose less. The check before filing is
>> not "is this true?" but "does the artifact already say this, better than I am about to?"** <<

## Routed

F1 (OR-boundary check defect) + F2 (under-representation) → CTO~Z. **No defect found in the routing
harness itself** — it is the strongest instrument I have examined in this sweep, and the record should
say so as plainly as it says the other things.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-system --check` | CURRENT | gate-first per LD-0319 |
| `sysparity_register.py report` | 6/22 pointer-backed | used it to pick the unit, as intended |
| `comp-which-routing-test.py` (read + structural parse) | **timed out at 2m when run** | not filed as a defect — it makes hundreds of warm router calls by design; noted as an operational property |
| frozen-cohort JSON parse | 562 / 9,100 / 740 / 563 | **printed the shape before parsing, after my first two regex guesses returned 0 pairs on a wrong-shape assumption** |

**My own instrument error, again, and the same shape as the day's other three:** a regex hunting
`(question, expected_tool)` pairs returned **0**, which I nearly read as *"the harness has no cases."*
It has no such table at all — it is cohort-based. **A zero from a wrong-shape query is indistinguishable
from a true absence.** Caught by printing the structure rather than trusting the count.
