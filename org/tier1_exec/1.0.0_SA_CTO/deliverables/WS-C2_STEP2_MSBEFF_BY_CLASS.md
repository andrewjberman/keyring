# WS-C2 STEP 2 -- MSBEFF's 718 findings, typed BY CLASS

**Program:** NFRA_VELOCITY / CORE, WS-C2. **Author:** `1.0.0_SA_CTO~Z`. **2026-07-31.**
**Predecessors:** step 0 `@ee3673d89` (rev 3), step 1 (units-error correction landed).
**Corpus:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_MSBEFF/nl_structured/`.
**Fence:** `ADVI_PERFORMANCE` / `MDPF_GLOBAL` not drawn on, not opened.

**Method, per step 0's plan:** type the **CLASSES**, not the 718 items. Typing items individually
would re-derive an existing classification -- and the classification already exists as a governed
`verdict` field.

---

## S.1 THE DENOMINATOR -- AND THIS CORPUS HAS A CANONICAL ARTIFACT, WHICH THE OTHER DOES NOT

```
raw parse of nl_structured/*.jsonl ....... 1436
unique records ........................... 718     (every record appears EXACTLY twice, 0 appear once)
findings_merged.jsonl alone .............. 718     <- THE CANONICAL FILE
PHASE3's published claim ................. 718     EXACT MATCH
FAILED_COVERAGE: mine 253/718 = 35.2%  vs published "253/718 = 35%"   EXACT MATCH
```

The doubling is benign and fully explained: **`findings_merged.jsonl` is the merge; the six
`chunk_*.findings.jsonl` are its inputs.** Reading the directory sums a set with its own union.

> **CONTRAST WITH STEP 1, AND IT IS THE MOST USEFUL THING IN THIS SECTION.** The incident taxonomy has
> **five populations and no canonical artifact** -- its "210-row instance table" is a *proposed move*
> that does not exist. **MSBEFF has ONE canonical file and every published figure reproduces off it
> exactly.** Same program, same author-fabric, same week. **The difference is not rigour, it is whether
> a merge artifact was ever built** -- which is exactly MSTR~Z's root-cause finding, seen from the
> side where the artifact DOES exist.

*My raw parse doubled the corpus and I caught it by reconciling against PHASE3's published 253 -- a
denominator I did not control (L-2). The ratio was stable at 35.2% under both the doubled and the
deduped count, which is why a ratio-only check would have missed it.*

---

## S.2 THE NINE CLASSES, TYPED -- SEMANTICS GROUNDED BY SAMPLING, NOT BY NAME

| class | n | % | verdict | why |
|---|---|---|---|---|
| **FAILED_COVERAGE** | 253 | 35.2 | **RECALL -- not the rails** | *"comp graph does not index comp/ at function level"*, *"props-only components invisible to schema-check"*. What the tool COULD NOT SEE. |
| **WORKED** | 162 | 22.6 | **NOT A DEFECT** | *"schema-check --feature diagnosed the W3 OFC routing bug directly"*. Successes. |
| **GAP_NAMED** | 110 | 15.3 | **RECALL -- not the rails** | *"MCP/shell/hook infra uncovered by comp tools"*. A named absence of coverage. |
| **FRICTION** | 58 | 8.1 | **NOT A POSITION CLASS** | usability cost, not a wrong answer. |
| **FAILED_TOOL** | 39 | 5.4 | **NOT A POSITION CLASS** | the tool errored. Loud, not silent. |
| **FIXED_IN_FLIGHT** | 33 | 4.6 | **AN OUTCOME, NOT A CLASS** | repaired during use. |
| **MISROUTE** | 26 | 3.6 | **TYPED** | *"no tool exposes live EventBridge State"* -- a question typed at one tuple routed to a tool declaring another. **This is the tuple's own purpose.** |
| **STALE_SOURCE** | 20 | 2.8 | **TYPED -- `plane`** | *"graph vintage unsuitable for verifying own fresh changes; live primitives used"*. Projection-vs-live, exactly. |
| **SUBSTITUTED** | 17 | 2.4 | **BEHAVIOURAL -- not a tuple field** | see S.2.1 -- **I typed this wrong from its name.** |

### S.2.1 I MIS-TYPED ONE CLASS FROM ITS NAME, AND SAMPLING CAUGHT IT

**I initially typed `SUBSTITUTED` as `grain`** -- a proxy standing in for the thing, the M3 family. Then
I read instances: *"COO skipped mandated pre-TO comp-blast"*, *"COO reached for raw grep and rated it
positively"*, `layer=behavioral`. **It is an AGENT choosing the wrong instrument, not a measurement
substituting a proxy for a value.** Different object entirely.

> **A class name that reads like a mechanism is not a mechanism.** I was one step from folding 17
> findings into `grain` and inflating the tuple's coverage with a class that has nothing to do with
> position. **The sample cost two minutes and moved the headline number.**

---

## S.3 THE RESULT -- AND IT CORROBORATES STEP 0 FROM AN INDEPENDENT CORPUS

| bucket | n | % of 718 |
|---|---|---|
| **RECALL / coverage** (`FAILED_COVERAGE` + `GAP_NAMED`) | **363** | **50.6%** |
| NOT A DEFECT (`WORKED`) | 162 | 22.6% |
| Not position classes (`FRICTION`, `FAILED_TOOL`, `FIXED_IN_FLIGHT`) | 130 | 18.1% |
| **TUPLE-TYPED** (`MISROUTE`, `STALE_SOURCE`) | **46** | **6.4%** |
| Behavioural (`SUBSTITUTED`) | 17 | 2.4% |

> ### **HALF OF THE LARGEST CORPUS IN THE PROGRAM IS RECALL, WHICH THE RAILS DO NOT TYPE AT ALL.**
> ### **ONLY 6.4% IS TUPLE-TYPED.**

**This is step 0's boundary, re-derived from a corpus with a different author, a different method, and a
different subject matter.** Step 0 said the rails type WHERE AN ASSERTION SITS and do not type
INSTRUMENT FALLIBILITY. MSBEFF is 50.6% instrument fallibility -- *what a tool could not see* -- and the
rails are silent on all of it. **That is not a gap in the rails; it is WS-C7's entire subject, arriving
with a measured 363-finding mandate.**

**AND IT SHARPENS THE M2-HOMELESS ARGUMENT.** `FAILED_COVERAGE` at 35.2% is the single largest class in
either corpus, and it is a **recall** property -- so WS-C7 genuinely holds it. **M2 (shape-match, wrong
content) is a PRECISION property and WS-C7 still cannot hold that.** The two are adjacent and only one
has a home. *The corpus that most justifies building WS-C7 is also the corpus that shows WS-C7 will not
absorb M2.*

---

## S.4 RESIDUAL

- **First-pass typing against class DEFINITIONS + sampled instances, NOT against all 718.** Two samples
  per class is enough to catch a name-level error (it caught one) and **not** enough to establish class
  homogeneity. A class could be internally mixed.
- **`GAP_NAMED` is the row I am least sure of.** It may split -- a named gap in *coverage* is recall, but
  a named gap in *vocabulary* would be a WS-C1 signal. Not separated here.
- **`WORKED` at 22.6% deserves its own note:** nearly a quarter of the "findings" corpus records
  successes. Any statement of the form *"N findings"* that does not exclude them is inflated by 22.6%.
- The `layer` field (`mechanical` 80.5% / `semantic` 14.2% / `behavioral` 5.3%) is **unused here** and
  is a second axis worth crossing against `verdict` before WS-C3.
