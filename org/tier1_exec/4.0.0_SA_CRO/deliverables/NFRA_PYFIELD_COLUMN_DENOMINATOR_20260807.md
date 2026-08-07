# NFRA_PYFIELD TO-0 — THE COLUMN DENOMINATOR

**Author:** `4.0.0_SA_CRO` · **TO:** `NFRA_PYFIELD.TO-0.column-denominator` @189fd46f6b (issued
`2.0.0_SA_COO`) · **PRD:** `docs/architecture/NFRA_PYFIELD_PRD.md` v1.0 @004588f9cb
**Measurement vintage:** **2026-08-07T152209Z** · **pandas 2.3.3** · **Zero production code.**

---

## THE FIGURE

> **2,744 of 4,406** name-based string-literal subscripts are **columns** — **62.3%**
> **[95% CI 56.8% – 68.3%]**
>
> Composed as: **1,905 confirmed** + **1,894 undecidable × an audited column-rate per stratum**.
> Sampling rule: **first-per-file alphabetical, per stratum** (262 sites hand-read).
> Against the full population **including** the 491 expression-base subscripts (**4,897**):
> **56.0% [51.1% – 61.4%]**.

**Denominator grain: AST string-literal `Subscript` NODES.** Not lines, not files. This matters —
`comp-find` counts *lines* matching a regex and returns **4,336** for the same corpus. Neither
number is wrong; they count different things, and only one of them is a subscript population.

**⛔ THIS IS NOT AN ESTATE FIGURE.** Corpus, stated beside the number as required:
**SWEPT** — `data/inf/scripts/gold` + `data/assets/scripts/gold` (124 files, 0 parse errors).
**UNSWEPT** — `bd`, `cot`, `mdpf`, the assets monolith, and every `silver/` tree. The `etfs`+`find`
figures carried in the PRD on my predecessor's word are **still not re-derived** and are not used here.

---

## 1 — WHAT THIS REPLACES

Q2 measured **24.3% flow-local reach** and correctly refused to set a bar on it: 24.3% is a true
statement about **subscripts** and a meaningless one about **columns**, because much of the
unresolved mass was never a column. A bar of "resolve X% of columns" needed a column denominator.

**It now exists: ~2,744.** So the denominator for TO-1's acceptance bar is **not 4,896**. Roughly
**38% of the subscript population is not a column at all** and is *correctly* unresolved — a
recognizer that never touches it is not failing.

---

## 2 — METHOD, AND THE ONE THING IT REFUSES TO DO

Three artifacts, all committed and re-runnable:

| stage | artifact | what it does |
|---|---|---|
| extract | `scripts/pyfield_column_probe.py` | **evidence extractor, NOT a classifier** — per site: base, key, scope, store-vs-load, the attribute taken on the result, and the binding evidence for the base (param? loop over what? assigned from what shape?) |
| classify | `scripts/pyfield_classify.py` | the **stated decision procedure** over that evidence — three states, applied mechanically to 100% of sites |
| compose | `scripts/pyfield_denominator.py` | applies the **audited** correction rate to the undecidable mass, with Wilson intervals |

**The procedure never judges what it also selected.** The extractor gathers evidence; the procedure
decides; a hand audit measures the procedure's error. **The audit does not get to edit the
procedure** — folding these findings back into the rules would tune the scorer to its own eval
cases (Andrew-direct 2026-08-06) and would make the interval a fiction. So the measured error is
carried as a *rate with an interval*, not absorbed as a *fix*.

**Marker sets are DERIVED from the installed pandas API, never hand-drawn** (TO `<do_not>` rule 2).
`_DF_METHODS` was not lifted. Derived against **pandas 2.3.3**, universe `dir(DataFrame) ∪
dir(Series)` = **240**: `MINIMAL` = 3, `STRICT_DERIVED` = 227, `WIDE` = 233.

**Self-test: 19/19**, including a **mutant** (empty constructor set → the binding axis goes dark,
not green), a **negative control** (clean file → 0 sites, no error), and **both directions** of the
v1/v2 resolver split. *The self-test's first run failed — on my own assertion, not the code: I
expected 8 subscripts in a fixture that contains 6 (`on="k"` is a kwarg). The wrong expectation is
recorded in the file rather than quietly corrected, because the fixture count is the one number in
that test nothing else cross-checks.*

---

## 3 — THE THREE STATES, AND WHY THE THIRD IS NOT A FORMALITY

| state | n (name-based) | share |
|---|---|---|
| `column` | 1,905 | 43.2% |
| `not-column` | 607 | 13.8% |
| `undecidable-at-this-site` | 1,894 | 43.0% |

**Conflicting evidence resolves to undecidable, never to a verdict.** Absence of evidence is
undecidable, never "not a column."

The TO warns that **zero undecidable would be a finding against the classification**. The inverse
question is just as sharp, so I asked it: **is 43% undecidable the corpus's ambiguity, or my
analyzer's weakness?** Those are completely different claims and a single rate conflates them.

**Answer, measured: overwhelmingly my analyzer.** Of the 68 undecidable sites in the audit sample,
**67 were decidable by a human reading the call site**; exactly **one** was genuinely ambiguous
(`e["date"]`, an `enumerate` element of an unresolved iterable — nothing at the site separates a
dict record from a Series row).

**So the honest reading of 43% is: the site-local evidence my probe collects is insufficient, not
that the corpus is a coin-flip.** That distinction is load-bearing for TO-1 — it says the remaining
mass is *reachable* by a stronger resolver, not lost.

---

## 4 — PER-STRATUM (reported separately; a pooled figure hides which stratum carries the uncertainty)

| stratum | n | procedure: col / not / undec | audited column-rate of the undecidables | est. columns |
|---|---:|---|---|---:|
| **S-A usage-only** | 481 | 83 / 2 / 396 | **97.1%** [85.5–99.5] (34 of 35) | **468** [421–477] |
| **S-B usage+binding** | 583 | 583 / 0 / 0 | — (fully decided) | **583** |
| **S-B2 binding-only** | 972 | 972 / 0 / 0 | — (fully decided) | **972** |
| **S-C neither-axis** | 2,370 | 267 / 605 / 1,498 | **30.3%** [17.4–47.3] (10 of 33) | **721** [527–976] |
| **S-D expr-base** | 491 | 7 / 0 / 484 | **not extrapolated** | — |

**S-D is excluded from the estimate deliberately, not overlooked.** `f()["x"]`, `d["a"]["b"]` —
a name-keyed heuristic cannot attempt these *by construction*. They are a **structural floor on
unresolvability** (PRD §2.4) and belong in TO-1's coverage declaration from day one.

**Almost all of the uncertainty lives in S-C.** Its interval is ±225 sites; every other stratum is
tight or exact. Any effort to narrow the published figure should go there and nowhere else.

---

## 5 — WHAT THE AUDIT MEASURED (262 sites, first-per-file alphabetical per stratum)

**Procedure-decided sites: 194 hand-checked, 194 held. Zero false positives, zero false negatives.**

- **123 `column`** — all correct. One was actively challenged rather than waved through:
  `lib/aor_resolution.py:724`, where `pd.Series(res['fold_mode'])` looks like defence against a
  dict. An adjacent comment about `.isna().any()` on an **EMPTY FRAME** confirms `res` is a
  DataFrame; the wrapper is empty-frame defence. Verdict stood.
- **71 `not-column`** — all correct. The sharpest one is `runners_49f/tests/test_c01_*.py:29`:
  `d = dict(base)` builds a per-row **dict** whose keys are `d_aua`, `nna_total` — and four lines
  later `pd.DataFrame(out)` turns those same strings into **columns**. *The identical key name is a
  dict key on one line and a column on another. That is the discriminator problem in four lines.*

**Procedure-undecidable sites: 68 hand-adjudicated** → 44 column, 23 not-column, **1 genuinely
ambiguous**. Per-site records (locus + verdict + one-line reason) in
`pyfield_to0/hand_adjudication.json`.

---

## 6 — THE SENSITIVITY TEST, CASHED OUT (this was the point of the ~507 band)

The PRD's worry about `WIDE` was *"not a dict method ≠ is a DataFrame — a list, an object, or a
custom class also qualifies."* **Measured, and it is largely unfounded on this corpus:**

- **`MINIMAL` (228 sites): 228 of 228 classified column — 100%.** A clean positive control.
- **The marker band — `WIDE` minus `MINIMAL`, 836 sites** (the re-derivable form of the PRD's
  ~507): **438 column / 2 not-column / 396 undecidable**, and the audit resolves the undecidables at
  **97.1%** column.
- **So usage-side `WIDE` membership predicts column-ness at ~97% here.** The one false signal in the
  whole sample is `composed["dates"].index(last_measured)` — **`.index` is a `list` method**, and
  `index` is also a DataFrame attribute, so the marker fired on a list. *That is exactly the failure
  mode the PRD predicted, and it occurred once in 35.*

**Consequence for the PRD's bound.** Its honest bound was *"≥228 by unambiguous markers, ~1,016 on
CRO's set, ≤1,247 by any-non-dict-method."* The measurement says **the upper end of that range was
much closer to right than the lower end** — `WIDE` is a good predictor, not an over-claim. The
column population (~2,744) is **larger than every figure in that range**, because the binding side
and the neither-axis stratum contribute columns the usage axis never sees.

---

## 7 — DIVERGENCES FROM THE PRD'S FIGURES (reported, not silently adopted — TO `<if_mismatch>`)

| figure | PRD | mine | disposition |
|---|---:|---:|---|
| name-based subscripts | 4,406 | **4,406** | **reproduces EXACTLY** (third independent probe) |
| files / parse errors | 124 / 0 | 124 / 0 | reproduces |
| `MINIMAL` usage hits | 228 (5.2%) | **228 (5.2%)** | **reproduces EXACTLY** |
| total string subscripts | 4,896 | **4,897** | **+1. Not a double-count** — verified: 0 non-unique `(file,line,col,key,base)`. 152 shared *loci* are chained subscripts (`d["a"]["b"]["c"]`) that legitimately share a start column. The two prior probes agree with each other, so the residual single site is most likely mine. 0.02%; moves nothing here. |
| `WIDE` usage hits | 1,247 (28.3%) | 1,064 (24.1%) | differs. Mine counts a marker only where the attribute is taken **directly** on the subscript result. |
| binding-side reach | 1,214 (27.6%) | **434 (v1) / 1,555 (v2)** | **see below — this is the finding, not the nuisance** |
| S-A usage-only | 596 | 481 | follows from the two above |
| the "~507" band | ~507 | **836** | the PRD's band is bounded by `MID`, **a hand-chosen set that no longer exists** (scratchpad-only, lost with its session). It cannot be reproduced. I substituted the **re-derivable** band `WIDE − MINIMAL` = 836, which is a **superset** — so this census strictly dominates the one requested. |
| neither-axis | 2,596 | 2,370 | follows |

### ⚠ 7.1 — THE BINDING-SIDE NUMBER IS A PROPERTY OF THE RESOLVER, NOT OF THE CORPUS

On one identical population of 4,406 sites:

| resolver | binding reach | what it seeds on |
|---|---:|---|
| **v1** (mine, constructor-only) | **434 — 9.9%** | in-scope `pd.*` constructors, propagated |
| **PRD's spike** | 1,214 — 27.6% | (between the two) |
| **v2** (mine) | **1,555 — 35.3%** | + DataFrame-typed **parameter annotations** + **one-hop local return** summaries |

**A 3.6× swing from two cheap, sound additions.** Neither is type inference; both are things the
author already wrote down (`txns: pd.DataFrame`, `def mk() -> pd.DataFrame`).

> **This is the binding-side twin of the marker-set finding, and it deserves equal weight.** The PRD
> established that the *column floor* moves **5.5×** with the marker set. This establishes that
> *binding-side reach* moves **3.6×** with the resolver. **Both headline numbers are properties of
> the instrument.** An acceptance bar of "resolve X% of columns" is therefore **unstateable without
> pinning the resolver**, exactly as the floor was unstateable without pinning the marker set —
> and the PRD only closed the second half.

---

## 8 — WHAT THIS MEANS FOR TO-1's ACCEPTANCE BAR (a statement of fact, not a gate)

**I am not gating anyone.** Nothing waits on my signature; no seat is held. The only true dependency
is narrow: TO-1's bar was *unstateable* until a denominator existed. It exists.

1. **The denominator is ~2,744 name-based (interval 2,504–3,008), not 4,896.** A bar written against
   the subscript count understates the recognizer by ~38 points before it runs.
2. **The bar must name its resolver and its marker set**, or it is not reproducible (§7.1).
3. **491 expression-base sites are unreachable by construction.** They belong in `Coverage.unresolved`
   from day one and must never be scored against the recognizer as misses.
4. **~1,894 sites need more than site-local evidence** — but 67 of 68 audited were human-decidable,
   so this is reachable analyzer headroom, not corpus noise. The two cheapest wins are already
   measured: **parameter annotations and one-hop local return summaries**.
5. **`.iterrows()` is not an edge case: 257 sites.** A recognizer that treats loop variables as
   records will mis-call every one — `row['col']` on an `iterrows` row **is** a column access.

---

## 9 — BOUNDARY DECLARATION (`boundary_declaration`, four parts — the ratified form)

Adopting the ratified vocabulary rather than re-coining beside it (`comp-estate --definitions`;
`column` / `field` / `subscript` are **not** ratified terms, so no conflict — but
`denominator_grain`, `boundary_declaration`, `known_negative` are, and are used here as defined).

- **`address_space`** — what this COULD have found: 124 files → 4,897 string-literal subscript nodes
  → 4,406 name-based. `denominator_grain` = subscript nodes.
- **`traversal_residue`** — what it COULD NOT reach: **491 expr-base sites** (enumerated, not
  estimated); every `silver/` tree; `bd`/`cot`/`mdpf`/assets-monolith; non-subscript column carriers
  (`.loc`, `.iloc`, attribute access, `usecols=`, `rename(columns=)`, `merge(on=)`, agg dicts —
  PRD Q4, **uncounted here, so the true carrier population is LARGER than 4,897**).
- **`presentation_residue`** — what it found and did not show: nothing. All 4,897 per-site verdicts
  are in `verdicts_v2.jsonl`; all 68 hand adjudications in `hand_adjudication.json`.
- **`failure_direction`** — where this is wrong, it **over-reports columns** in S-A (a `WIDE` marker
  firing on a list, measured at 1-in-35) and is **widest in S-C** (±225). The interval is the honest
  carrier; the point estimate alone is not.
- **`known_negative`** — a case that came out the other way: `composed["dates"].index(...)`, where
  the usage marker fired and the base was a list. Stated so the 97.1% is not read as 100%.

---

## 10 — HONEST RESIDUE

- **My hand adjudications are judgements.** Recorded per-site with reasons so they can be
  re-derived, but a second reader could differ on some of the 68 — most plausibly in S-C, which is
  also where the interval is widest.
- **The +1 subscript** (4,897 vs 4,896) is unexplained. It is 0.02% and moves nothing, and I would
  rather leave it named than round it away.
- **The audit is 262 of 4,406 (5.9%).** The intervals reflect that and nothing more; they do **not**
  cover the risk that my *procedure* and my *audit* share a blind spot, since both are mine. A
  second seat re-deriving even one stratum would close that, and it is the cheapest available check.
- **`comp-which` has no route for this intent** — recorded as a coverage gap, not worked around
  (§ Compiler Tools in the session log).

---

## APPENDIX — artifacts

| file | what |
|---|---|
| `scripts/pyfield_column_probe.py` | evidence extractor + 19-assertion self-test (**requirement 5**: the spike probe, committed and re-derivable) |
| `scripts/pyfield_classify.py` | the stated three-state decision procedure |
| `scripts/pyfield_denominator.py` | Wilson-interval composition |
| `deliverables/pyfield_to0/sites_v1.jsonl` · `sites_v2.jsonl` | raw evidence, both resolvers |
| `deliverables/pyfield_to0/verdicts_v2.jsonl` | **4,897 per-site records** — locus, verdict, one-line reason (**requirement 2**) |

> **⚠ READING THE `.jsonl` FILES — line 1 is an in-band `_header`, so `wc -l` = records + 1.**
> `verdicts_v2.jsonl` is **4,898 lines = 1 header + 4,897 site records**; of those records,
> **4,406 are name-based and 491 are expr-base**. A count taken over the whole file therefore
> includes the header and reports one too many, and a count taken over *all* records answers a
> different question from the headline, which is scoped to the **name-based** domain.
>
> *This is a documented property, not a trap — recorded because it already cost something: COO's
> independent re-derivation read 4,898 records / 492 expr-base, and briefly disagreed with this
> deliverable, before their own scan tripped over the header and resolved it. The header is
> deliberately kept IN BAND: the two designs fail in opposite directions, and a sidecar's failure is
> the worse one for THIS artifact — a file that can be moved, copied or quoted **without** its
> grain, corpus, resolver and vintage is exactly the frameless denominator this TO existed to
> prevent. An off-by-one that is caught in ten minutes by the frame sitting in row 1 is the cheap
> failure direction.*
| `deliverables/pyfield_to0/audit_v2.jsonl` | the 262-site systematic audit sample |
| `deliverables/pyfield_to0/hand_adjudication.json` | the 68 hand verdicts with reasons |

Re-run end to end:

```bash
python org/tier1_exec/4.0.0_SA_CRO/scripts/pyfield_column_probe.py --self-test
python org/tier1_exec/4.0.0_SA_CRO/scripts/pyfield_column_probe.py \
    data/inf/scripts/gold data/assets/scripts/gold --root . --resolver v2 \
    --out org/tier1_exec/4.0.0_SA_CRO/deliverables/pyfield_to0/sites_v2.jsonl
python org/tier1_exec/4.0.0_SA_CRO/scripts/pyfield_classify.py \
    org/tier1_exec/4.0.0_SA_CRO/deliverables/pyfield_to0/sites_v2.jsonl \
    --out org/tier1_exec/4.0.0_SA_CRO/deliverables/pyfield_to0/verdicts_v2.jsonl \
    --audit-out org/tier1_exec/4.0.0_SA_CRO/deliverables/pyfield_to0/audit_v2.jsonl
python org/tier1_exec/4.0.0_SA_CRO/scripts/pyfield_denominator.py
```
