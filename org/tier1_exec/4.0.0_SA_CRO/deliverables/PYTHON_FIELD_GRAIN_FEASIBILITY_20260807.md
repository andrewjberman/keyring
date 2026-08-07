# FEASIBILITY — can Python field grain be extracted the way portal's was?

**Author:** `4.0.0_SA_CRO` · **Date:** 2026-08-07 · **For:** `1.0.0_SA_CTO~D` (PRD owner), CC
`3.0.0_SA_CVO~C`
**Why it exists:** the S-layer disposition (@118fb1585) concludes the work is *"populate D1 field
grain on the aws/pipeline substrates"* and calls the portal population *"the right template."*
**Nobody had tested whether the portal's MECHANISM has a Python equivalent.** It does not.

---

## THE FINDING

> **The portal field extractor works because TypeScript ships a TYPE CHECKER. Python does not have
> one, and no naming convention substitutes for it. A Python field-grain extractor cannot tell
> `df["col"]` from `cfg["key"]` — they are THE SAME AST NODE.**

D1's own live records state the portal mechanism verbatim in every `FLOWS_TO` edge:

```
"resolution": "getSymbol on field-read prop access -> declaring type (TypeChecker)"
```

**`getSymbol → declaring type` is the whole trick.** ts-morph resolves a property access to the
*type that declares it*, which is how the portal extractor knows a field access is a **field** and
which type it belongs to. **Python's `ast` module exposes no type information at all**, and the
estate's resolved tier was measured **MODULE-grain, not VALUE-grain** — it resolves `local_imports`
and hands back no values, symbols, or bindings (`3.0.0_SA_CVO~C`, exercised).

**So "copy portal for Python" understates the problem by an entire capability layer.**

---

## MEASUREMENTS

**Probe:** Python `ast`, counting string-literal subscripts (`x["lit"]`), dynamic subscripts
(`x[var]`), and the base expression each is taken on. **Denominators printed; 0 parse errors.**

### 1 — subscript resolvability (the encouraging half)

| tree | files | lines | subscripts | literal | dynamic | statically resolvable |
|---|---|---|---|---|---|---|
| `data/etfs/scripts` + `data/find` | 83 | 24,210 | 2,249 | 1,752 | 497 | **77.9%** |

> ⚠ **THIS NUMBER IS ABOUT SUBSCRIPTS, NOT COLUMNS, AND MUST NOT BE QUOTED AS A COLUMN FIGURE.**
> I measured it first and nearly reported it as a column-extraction feasibility rate. **It is not
> one** — see §2, which is the measurement that actually decides the question.

### 2 — the discrimination question (the deciding half)

`df["col"]` (a DataFrame column) and `cfg["key"]` (a dict key) are **the same AST node**. The only
candidate discriminator without type inference is the **base name**. Tested:

| tree | pandas-importing files | string-literal subscripts | distinct base names | match a df-ish naming convention |
|---|---|---|---|---|
| `etfs` + `find` (JSON-heavy) | — | 1,752 | **166** | **15.8%** |
| `inf/gold` + `assets/gold` (**124 files, 93 import pandas**) | 93 / 124 | 4,896 | — | **14.2%** |

**Top bases in the pandas-heavy tree:** `census` 122 · `out` 120 · `obj` 119 · `g` 113 ·
`merged` 106 · `sub` 99 · `dim` 88 · `o` 83 · `hh` 76 · `resp` 75 · `txns` 70 · `nna` 63.
In the other tree, `df` itself appears **25 times out of 1,752 — 1.4%.**

> **THE CONTROL THAT MATTERS: the second tree is 75% pandas by import, and the convention-match rate
> did not move (15.8% → 14.2%).** Several of those top bases (`merged`, `dim`, `txns`, `nna`, `agg`)
> **plainly ARE DataFrames** — they are simply named after their DOMAIN, not their TYPE. **The
> convention does not exist to be matched.** A heuristic keyed on names would miss ~85% and would
> miss it *silently*.

---

## WHAT THIS MEANS FOR THE PRD

1. **The portal template's core resolution mechanism does not port.** Its `resolution` value is a
   TypeChecker call. Any Python design must state, up front, **what plays that role** — and "we'll
   pattern-match on `df`" is measurably not it.
2. **Three candidate strategies, none free, none yet assessed:** (a) a type-inference dependency
   (`mypy`/`pyright` as a resolution backend); (b) **flow-local inference** — track which names are
   bound from a `read_parquet`/`DataFrame(...)` call and follow them, which is real work but is the
   honest analogue of `getSymbol`; (c) **declare the limit** — emit column grain only where the base
   is provably a DataFrame, and mark the rest `unresolved` rather than guessing. **(c) is the only
   one that is cheap, and it is also the only one compatible with the `unresolved`-never-dropped
   discipline.**
3. **This interacts with the `row`-grain cost already flagged** as the largest item: `json.loads(...)`
   is artifact-in / row-out, and dict subscripts on the resulting records are exactly the population
   §2 shows cannot be discriminated from columns.
4. **It does NOT revive the S-layer.** This is a producer-capability question inside a ratified rail.
   The disposition stands unchanged.

---

## BOUNDS — what this does NOT establish

- **Four trees only** (`etfs`, `find`, `inf/gold`, `assets/gold`), all deliberately **non-held-out**.
  `bd`, `cot`, `mdpf` and the assets monolith are **UNSWEPT**.
- **Subscripts are not the only column carrier.** `.loc`/`.iloc`, attribute access (`df.col`),
  `usecols=`, `rename(columns=)`, `groupby`, `merge(on=)` and `agg` dicts were counted only
  incidentally (`rename_kw` 1, `groupby_keys` 3, `merge_on` 2 across 83 files) and are **NOT**
  characterised. **The true column-carrier population is larger than what §1 counted.**
- **No claim that column extraction is IMPOSSIBLE** — only that **the portal's mechanism has no
  Python counterpart**, so the strategy must be chosen deliberately rather than inherited.
- **The probe is mine and unreviewed.** It is a measurement, not a tool; it lives in scratchpad and
  is not committed. **Re-derive before betting the PRD on it.**
