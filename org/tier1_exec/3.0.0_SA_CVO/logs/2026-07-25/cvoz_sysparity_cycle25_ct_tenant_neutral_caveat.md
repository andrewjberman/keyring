# CVO~Z — SYSPARITY cycle-25: `ct-tenant-neutral-caveat` — a STALE CAVEAT UNDER-BOUNDS THE THING IT EXISTS TO BOUND

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27` · vintage worktree @ `dcd7cea91`

---

## Gate

`comp-system --check` → **SYSTEM CURRENT** (24 regions / 6 files, 0 drifted).

## Unit

```
id:    ct-tenant-neutral-caveat
desc:  "the tenant-neutral-comp-tools over-reach is CAVEATED not overstated
        (only comp-genesis/comp-which parameterize; the ~61 query CLIs are Opal-bound)"
check: grep_present over infra/system/README.md
       pattern: "NOT yet tenant-neutral|Opal-bound|not tenant-parameterized"
```

## VERDICT: **DRIFTED**

### F1 — `~61` is a hand-copied present-tense count with NO DERIVABLE POPULATION

The README (`:39`) asserts, present tense: *"only `comp-genesis` + `comp-which` parameterize **today**;
the **~61** query CLIs (comp-blast/kuzu/aws/freshness/...) **are** Opal-bound."*

Live populations measured:

| population | count |
|---|---|
| extensionless `.tools/comp-*` CLIs | **84** |
| `tools_index` (managed region in `03_comp_tools.md`) | **69** |
| SoT ledger union (managed region, same file) | **87** |

**None is 61**, and the README states no rule that would produce 61 from any of them — the parenthetical
`(comp-blast/kuzu/aws/freshness/...)` is an *illustrative list with an ellipsis*, not a definition. So the
number is **not merely stale, it is unfalsifiable by construction**: I cannot compute what it should be
because nothing says what it counts.

**And the mechanism to fix it already exists in the same tree, one file over.** `03_comp_tools.md` carries
the same population family in **auto-refreshed managed regions** (`<!--cs:tools_index_count-->69<!--/cs-->`,
`<!--cs:ledger_union_count-->87<!--/cs-->`). The README's `61` is hand-copied and unmanaged. **The estate
has the control; this number is not using it.**

Applying my own III-d.16 test — *is this an ASSERTION ABOUT NOW or a RECORD OF THEN?* — the sentence says
*"today"* and *"are"*. **It is an assertion about now, so a drifted count in it is a defect**, not a
legitimate frozen-with-reason record.

### F2 — >> THE FINDING THAT GENERALISES: A STALE CAVEAT UNDER-BOUNDS ITS OWN SUBJECT <<

This sentence is a **caveat**. Its entire job is to stop the tenant-neutrality claim from over-reaching —
to say *the generalization is narrower than it looks.*

>> **FOR MOST NUMBERS, STALENESS IS DIRECTIONLESS. FOR A NUMBER INSIDE A CAVEAT, STALENESS HAS A
>> DIRECTION, AND IT FAVOURS THE CLAIM BEING CAVEATED.** The un-generalized Opal-bound surface has GROWN
>> (61 → 84-ish) while the caveat still cites the smaller figure — so the honesty mechanism itself drifts
>> OPTIMISTIC over time. A caveat that ages does not merely become inaccurate; **it quietly returns the
>> over-claim it was written to prevent.** <<

Every tool added since the caveat was written is one more Opal-bound CLI the caveat does not account for,
and nothing re-counts. The P6 follow-on it defers ("porting the comp-tool QUERY surface to a tenant's
graph is UNBUILT") is therefore **larger than the record says**, and grows silently.

### F3 — the check verifies ONE SENTENCE EXISTS, and is blind to every number in it

All three OR-limbs (`NOT yet tenant-neutral` / `Opal-bound` / `not tenant-parameterized`) occur in **the
same single sentence** — measured: one line matches all three.

**IMPORTANT, AND IT EXONERATES THE OR:** by my own III-d.20 boundary, this disjunction is **LEGITIMATE** —
three specific multi-word phrases, no generic limb carrying the predicate. **The boundary has to acquit as
well as convict, and here it acquits.** The defect is on a different axis: presence-vs-truth. The check
confirms the caveat *was written* and can never detect that its contents have gone false.

## WHAT THE DOC GETS RIGHT

- **`~12 carry EXPLICIT opal-313476888478/opal-data-* literals` — MEASURED 10. Inside the tilde's
  tolerance; not a finding.** The approximation marker is doing legitimate work and I am not inflating a
  2-off against an explicitly approximate number. **COVERAGE DENOMINATOR: my scan covered `.tools/comp-*`
  wrappers ONLY, not the `org/modules/graph/` engines — so 10 is a FLOOR, not a total.**
- The caveat is unusually candid: it names the two bespoke pieces, calls the query-surface port **UNBUILT**,
  and labels it a P6 follow-on rather than implying coverage. **The prose is honest; only its number aged.**
- `comp-genesis` exists and is registered tenant-neutral, as claimed.

## Routed

F1 (migrate `~61` to a managed region or state its derivation rule) + F3 (check cannot see contents) →
CTO~Z. **F2 is the one worth doctrine** — it is a general property of caveats, not a fact about this file.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-system --check` | CURRENT | gate-first |
| `sysparity_register.py report` | 7/22 | picked the unit from it |
| literal scan over `.tools/comp-*` | 10 (floor) | denominator stated: wrappers only, engines excluded |
| managed-region read of `03_comp_tools.md` | 69 / 87 | the live counts the README's 61 is not derived from |

No instrument error this cycle — the one guess I made (that `~12` was stale) **measured as correct and I
dropped it**, which is the same discipline as filing the ones that survived.
