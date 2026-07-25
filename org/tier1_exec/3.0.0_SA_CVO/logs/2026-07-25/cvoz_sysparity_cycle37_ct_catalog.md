# CVO~Z — SYSPARITY cycle-37: `ct-catalog`

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27`

---

**Gate:** `comp-system --check` → SYSTEM CURRENT (24 regions / 6 files, 0 drifted).

## VERDICT: CLEAN — the cycle-10 migration held, and it is NOT a tautology

`derived_count`: source `graph-call-manifest.yaml[tools_index]` vs report
`06_current_state.json` → `metrics.tools_index_count.value`.

### The tautology question (item 14) — and why it clears

**It looked like a tautology and is not.** `comp_system.py:414` computes the report side as
`_yaml_len(MANIFEST, "tools_index")` — **the same computation on the same file** the check re-runs.

**What makes them independent is VINTAGE, not formula:**

- **source side** — the manifest's `tools_index` length, computed **now**
- **report side** — what 06 **stored** at its last generation

They diverge exactly when the manifest moves and 06 has not been regenerated. **That is a real
disagreement channel, and it is precisely the property the unit should assert.**

### EXERCISED — positive control and mutant, separate invocations

```
POSITIVE CONTROL  -> PASS
  "source graph-call-manifest.yaml[tools_index] holds 69 entries;
   06_current_state.json reports 69 -- in sync"

MUTANT (source +1 entry, worktree vintage) -> FAIL
  "source ...[tools_index] holds 70 but 06_current_state.json reports 69 --
   the REPRESENTATION is behind the source (source grew; regen pending)"
```

**The failure names BOTH sides AND the direction.** Direct contrast with `ont-rulebank-version-current`
(cycle-27), whose failure message asserted something false. This one is actionable as written.

### Disclosed bounds — both already in the check's own docstring

1. **COUNT-grain only** — *"a same-length container with different MEMBERS passes; member-set drift is
   comp-manifest-check's registration + existence invariants."* An add-plus-remove is invisible here **by
   design**, with the covering instrument named.
2. **Committed vintage by default** — an uncommitted manifest edit is **invisible by design**.

**The vintage note is my own addition from an earlier cycle** (`"CVO~Z verify addition, 2026-07-25"`),
written after I hit the confusing shape it warns about: *edit the manifest, re-run, see PASS, conclude
the check is broken.* **It stopped me mis-diagnosing this cycle — I went straight to `--worktree` for the
mutant instead of chasing a phantom.**

### Observation, not a defect

The disagreement channel **overlaps the gate**: a manifest edit changes `max_mtime`, so
`comp-system --check` goes STALE on the same event. **ct-catalog fires under conditions the gate largely
already covers** — but it reports the specific metric and the direction, which the gate does not. A more
specific instrument, not a redundant one.

---

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-system --check` | CURRENT |
| `comp_system.py:414/442` read | report side = `_yaml_len(MANIFEST, "tools_index")` |
| `_derived_count` positive control | PASS, 69 = 69 |
| `_derived_count` mutant (+1, worktree) | **FAIL**, both sides + direction named |

No instrument error this cycle. Scratch file removed; `.comp-graph/` verified clean.
