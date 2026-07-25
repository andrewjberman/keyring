# CVO~Z — SYSPARITY cycle-35: `ont-vocab-referenced`

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27`

---

**Gate:** `comp-system --check` → SYSTEM CURRENT (24 regions / 6 files, 0 drifted).

## VERDICT: **DRIFTED — a ruling from this session is UNEXECUTED**

CTO~Z ruled at `170441Z` §3, verbatim:

> **"Ruled: drop `06_current_state.md` from `ont-vocab-referenced`'s FILES list."** … *"Denominator becomes 3, and the reader counting the list is no longer misled."*

**Measured now:** the FILES list still carries **four** entries, including `infra/system/06_current_state.md`.

### The entry is DEAD, not tautological — correcting the ruling's own premise

Per-file hits for `RULE_BANK|variance_dimensions|canon-patterns`:

| file | hits |
|---|---|
| `00_synthesis.md` | 3 |
| `01_substrate.md` | 6 |
| `03_comp_tools.md` | 1 |
| **`06_current_state.md`** | **0** |

The ruling's stated reason was that making the generator emit the reference **would** make the check
tautological. **The live state is one step short of that: 06 emits nothing, so the entry matches nothing.**
The ruling is still correct — dropping it is the right fix — but the defect it removes is a **dead entry
inflating the denominator**, not a tautology. **A reader counting four representation files believes four
carry the vocab reference; three do.**

### Why it stays invisible

`grep_present` passes if **any** listed file matches. Three files match, so the unit is **PASS** and the
dead fourth entry is undetectable from the verdict. **The check cannot report which of its own inputs
contributed.**

### Ruling not executed — grounded

`infra/system/scope_contract.json` last touched **`3272197a93` at 14:25Z** (`0.8.0_AE_CloudComp~B`).
The ruling was issued at **17:04Z**. **No modification since.**

## Routed

Execute the cycle-20 ruling — drop `06_current_state.md` from the FILES list → CTO~Z. **No estate change;
the vocab IS referenced in `/system` (3 files, 10 occurrences).** Only the denominator is wrong.

---

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-system --check` | CURRENT |
| per-file limb enumeration | 3 / 6 / 1 / **0** — isolates the dead entry the aggregate verdict hides |
| `git log` on the contract | last touched 14:25Z, ruling 17:04Z → unexecuted |

No instrument error this cycle. **One premise correction against the ruling I was verifying:** I expected
a tautological-because-generated match and measured **zero** — the entry is dead, which is a different
(and simpler) defect than the one the ruling describes.
