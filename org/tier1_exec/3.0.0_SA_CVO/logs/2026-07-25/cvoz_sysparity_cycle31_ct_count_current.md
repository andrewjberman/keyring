# CVO~Z — SYSPARITY cycle-31: `ct-count-current`

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27`

---

**Gate:** `comp-system --check` → SYSTEM CURRENT (24 regions / 6 files, 0 drifted).

## VERDICT: CLEAN — no defect found

Unit checks two managed metrics: `tools_index_count`, `ledger_union_count`. I re-derived both from source
independently rather than trusting the `metric_current` verdict.

### Live source vs rendered

| metric | live source | rendered | sites | result |
|---|---|---|---|---|
| `tools_index_count` | **69** (`graph-call-manifest.yaml` `tools_index` length) | **69** | 1 | **MATCH** |
| `ledger_union_count` | **88** (`comp-coverage-map.yaml` union) | **88** | 4 | **MATCH** |

Ledger union composition: `tools`=36, `meta_tools`=52, **overlap=0** → 88.

### The 69-vs-88 delta reconciles exactly

`03_comp_tools.md` explains the delta as *"meta/enforcement/harness + newer-not-yet-projected tools."*
Measured:

```
ledger-but-not-tools_index : 19   (= 88 - 69 exactly)
tools_index-but-not-ledger :  0   (no orphan in the index)
```

**`comp-arity`** (landed today): in `meta_tools` = **True**, in `tools` = False, in `tools_index` = **False**
— i.e. a newer-not-yet-projected tool, exactly as the doc's explanation predicts.

### Denominator / observation

`ledger_union_count` renders at **4 sites across 3 files**; `tools_index_count` renders at **1 site**.
Not a defect — recorded as a coverage fact.

---

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-system --check` | CURRENT |
| independent re-derivation from both YAML sources | 69 / 88, both MATCH |
| managed-region scan across `infra/system/**` | 5 rendered occurrences, all consistent |
| set-diff of ledger vs tools_index | 19 / 0, delta reconciles |

**One tool error of mine:** first parse assumed `tools`/`meta_tools` were name-keyed dicts; they are lists
of dicts (`TypeError: unhashable type: 'dict'`). Fixed by printing the structure before parsing. Loud
failure, no wrong result produced.
