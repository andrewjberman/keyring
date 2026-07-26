# CVO~Z — SYSPARITY cycle-40: `eng-synthesis` — **REGISTER COMPLETE, 22/22**

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27`

---

**Gate:** `comp-system --check` → SYSTEM CURRENT (24 regions / 6 files, 0 drifted).

## VERDICT: `eng-synthesis` **CLEAN**

`00_synthesis.md`, 64 lines. Falsifiable content is mostly managed regions; I verified them against live
sources independently rather than trusting the gate's own verdict.

| managed value | live source | result |
|---|---|---|
| `rulebank_role_count` **14** | `RULE_BANK.yaml` `roles` → 14 | ✓ |
| `rulebank_relation_count` **10** | `relations` → 10 | ✓ |
| `rulebank_variance_count` **6** | `variance.labels` → 6 | ✓ |
| `ledger_union_count` **88** | verified live at cycle-31 | ✓ |
| cited commit `@a2cc8c7b1` | resolves, type `commit` | ✓ |

**Also clean on the propagation axis:** `comp-debris-ext` and `resource_heat_snap` each appear **0** times.

### Near-miss of my own — the wrong-population trap, caught

`len(d['variance'])` = **3**, against a doc value of **6**. I was one step from filing a discrepancy.
**The metric is `_yaml_nested_len(RULEBANK, "variance", "labels")`** (`comp_system.py:439`) — i.e.
`len(variance.labels)` = **6**. My 3 counted the dict's top-level keys (`labels`/`catalog`/`mechanism`).

**Same class as ~C's kuzu 20,419-vs-2,254 this morning: a correct count of the wrong population, which
would have rendered as a confident defect.** Caught by reading the computation before asserting the gap.

## THE CYCLE-39 RESIDUAL, NOW MEASURED — it is 5 files, not 2

At cycle-39 I flagged that the repair should sweep rather than patch the two sites I had landed on. **Run:**

| name | files | occurrences |
|---|---|---|
| `comp-debris-ext` | `03_comp_tools.md` (2), `05_learning_loops.md`, `07_maturity.md`, `README.md` | **5** |
| `resource_heat_snap` | `03_comp_tools.md`, `04_federated.md` (2), `05_learning_loops.md` | **4** |

**9 occurrences across 5 distinct files. I had examined 2 of the 5** — `04_federated.md`,
`07_maturity.md` and `README.md` were never opened by this sweep.

>> **The residual was 2.5x the sites I had found, and I only know that because I ran the sweep I had
>> recommended to someone else.** <<

## REGISTER COMPLETE — 22/22, all pointer-backed

**Every declared unit now carries a verdict with a stated denominator and a resolving artifact pointer.**

Tally across cycles 22–40: **13 CLEAN · 9 DRIFTED** (by my verdicts; cycles 16–19 predate the register
and were back-filled from the committed log).

**Standing exceptions, unchanged:** cycles 20–21 remain **UNRECORDED, not clean** — those verdicts died
with the killed session and CTO~Z ruled they must not be reconstructed.

---

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-system --check` | CURRENT |
| `RULE_BANK.yaml` structural read | roles 14 / relations 10 / variance.labels 6 — all match |
| `comp_system.py:439` computation read | resolved my 3-vs-6 as a wrong-population error |
| `git cat-file -t a2cc8c7b1` | `commit` |
| propagation sweep over `infra/system/*.md` | **5 files, 9 occurrences** |

**Denominator:** I verified 5 falsifiable claims in a 64-line doc. **I did not audit its prose sections
or the `5 classes` structural claim.**
