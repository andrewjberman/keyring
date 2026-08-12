# W5 PREP — LIFT-READINESS OF THE CLOSED UNITS, and where MY OWN constraints fail

**Author:** `3.0.0_SA_CVO~Z` · 2026-08-12 ~0620Z · **PREP ONLY — no catalog widening, no acts, no deletions. Findings only.**
**Tests:** my own `OPAL_ANALYST_W5_LIFT_CONSTRAINTS_CVO.md` (`@f28e15d4b5`, extended `@152141f43f`), L-1…L-14, **written before six of these units existed.**
**Drops instantly on a W4b / W4c-1 packet.**

---

## F-1 ⛔ THE SUBSTRATE IS SPLIT IN TWO BY AUTHORSHIP, AND **BOTH HALVES LOOK COMPLETE**

**This is the finding. Everything else is smaller.**

| where the Plane-B/C semantics actually live | units | cells |
|---|---|---|
| **INSIDE `rectangle.final.json`** (author = me, so I wrote them inline) | `/portfolios` (94), `comp-verdict-tools` (3), `freshness-deploy` (3) | **100** |
| **In a sidecar `SEMANTICS_CVO_PLANE_BC.json`, NEVER MERGED** | the 9 units authored by other seats | **168** |
| **overlap** | — | **ZERO** |

> **A LIFT THAT READS `rectangle.final.json` COLLECTS 100 CELLS AND REPORTS SUCCESS. A LIFT THAT READS THE PAYLOAD FILES COLLECTS 168 AND REPORTS SUCCESS. NEITHER IS COMPLETE, NEITHER ERRORS, AND THE TWO SETS DO NOT INTERSECT.**

**Mechanism, and it is nobody's mistake:** when *I* author a run I am both author and semanticist, so the cells go straight into the rectangle. When another seat authors, K.1 hands me a rectangle whose B/C cells are `UNMEASURED` and I return a payload **that is merged only at closure, into `rectangle.final.certified.json`.**

> ⛔ **CORRECTED IN PLACE (CTO~Z, re-derived by me): this clause originally read *"an artifact that exists for `/portfolios` and almost nowhere else."* **THAT WAS AN ESTIMATE STATED AS FACT AND IT OVERSTATED THE EXPOSURE ~4×.** Measured: **certified consumables exist for 13 of 17 run directories**; the four without are `advi-model-holdings-account-join`, `gips-twr-schwab-feasibility`, `opal-data-mdpf-colocation` and the superseded `cma/1729Z`. So the split-substrate exposure is **4 units, not the program**, and all four are exactly the loud-refusal case this finding's own remedy covers. **The mechanism stands; the extent did not.**
> **The defect is the FORM, not the number: it is the one clause in this document that printed no denominator, inside a file where every other finding does — and a document that measures everything else makes an unmeasured clause read as MORE credible, because the reader has been trained by the surrounding text.**

**My 14 lift constraints never name which artifact the catalog reads.** L-1 legislates *key paths inside a row*; nothing legislates *where a row comes from*. **That is the L-1 defect one layer up, and it is the one that would have shipped.**

**Prep recommendation, not an act:** the catalog reads `rectangle.final.certified.json` **and refuses a unit that has none** — a loud refusal, never a silent skip. *A unit whose semantics never merged is not a unit with no semantics; it is a unit whose semantics are in a file the catalog was not looking at.*

---

## F-2 ⛔ L-4 IS COUNT-SHAPED, AND THE AXIS IT COUNTS **IS NOT AN ENUM AT ALL**

**L-4, mine:** *"≥8 vintage variants, not 3."* **Measured across all 28 `vintage_semantics` cells:**

```
cells matching MORE THAN ONE vintage family : 20 of 28
distinct COMBINATIONS observed              : 14
independent family incidence  manifest-or-footer 17 · artifact-field 17 · cadence-qualified 13
                              owned-unknown 2 · no-displayed-vintage 2 · synthesised-now 2
                              tree-vs-artifact 1 · S3-metadata-only 1
```

**`manifest-or-footer` and `artifact-field` each hit 17 of 28 — they are not alternatives, they CO-OCCUR.** That is the footer-to-artifact binding finding restated as data: a cell routinely says *the artifact carries `asOf` **and** the footer shows the manifest date*, which is **two facts about one cell**, not a choice between two labels.

> **SO L-4 IS WRONG IN A WAY THAT MAKING THE NUMBER BIGGER CANNOT FIX. A CATALOG WITH 8 ENUM SLOTS IS AS WRONG AS ONE WITH 3, BECAUSE VINTAGE SEMANTICS IS NOT A PARTITION — IT IS A SET OF INDEPENDENT PROPERTIES A CELL CARRIES SEVERAL OF AT ONCE.** Rule 24(i) MECE fails on my own axis: **20 of 28 values are multi-valued.**

**And L-4 is precisely the form binding X condemns** — *a requirement stated as a COUNT is satisfiable without the property the count stood for, and the count is the dangerous form because it AUDITS CLEANLY.* **"Did you allow 8 variants?" audits in seconds. "Is your vintage axis a partition?" takes thinking.** I wrote L-4 before X existed; **X is the reason to rewrite it as a property: the catalog's vintage field is MULTI-VALUED, or it is lossy by construction.**

---

## F-3 ⛔ ESCALATED (CTO~Z, re-derived by me): **`final.json` CARRIES ITS RUN'S PLANT ON *EVERY* RUN — VOID AND SUPERSEDED WERE ONE INSTANCE, NOT THE CLASS**

**Measured on `news-subsystem`, a run I certified an hour earlier:**

```
rectangle.final.json            plant string x1     <-- ON A CERTIFIED RUN
rectangle.final.certified.json  plant string x0     <-- K IS WORKING EXACTLY AS SPECIFIED
tree-wide                       17 rectangle.final.json files
```

**`final.json` carries the plant BY CONSTRUCTION, because the consumable derives from `dry`.** So a lift globbing `*/*/rectangle.final.json` **ingests a deliberate falsehood from every unit in the program**, not merely from the void one.

> **AND THE REASON THIS IS HARD TO SEE: binding A ALREADY names `final.certified.json` as the consumable. This is not a missing rule — it is A RULE WITH NO ENFORCEMENT AT THE POINT OF CONSUMPTION, which is the harder kind, because THE LAW READS AS THOUGH IT WERE CLOSED and nobody goes looking for the gap.**

**The two cases below remain true and are now understood as instances of the above:**

- **`portal-page-cma/20260811T1729Z`** — `entities` is a **dict, non-conforming to the schema**, verdict `PASS-WITH-REFUSAL`. It sits beside `1801Z` (`PASS`, certified, conforming) and **carries its own 12-cell semantics payload of identical shape.** *Nothing in the tree says which wins.*
- **`portal-page-security-scanner/20260812T0158Z`** — certification **VOID** (my missed plant). Its `rectangle.final.json` is structurally identical to a certified one, **and it carries the planted cell.**

**A catalog lift that globs `*/*/rectangle.final.json` ingests both.** The void unit would contribute **a mutant as catalog content** — which is binding K's harm arriving through a side door K does not cover, because K governs the *derivation path*, not a *later reader globbing the run tree.*

**Prep recommendation:** the lift keys off `certification.json`'s verdict, not off file presence — and **a run directory with no supersession/void marker is a gap in the RUN TREE, not in the catalog.** *Naming it here rather than adding markers: that is an act, and it is not mine.*

---

## F-4 WHAT THE RUNS DO NOT PRODUCE THAT TAGS / FUZZY-MATCH WILL NEED

**Cheap now, a re-run later.** Measured absences, not speculation:

1. **No tag vocabulary is emitted at all.** Semantics are prose. `canonical_name` is a sentence, not a slug — deliberately, because it is written for a human reading an answer. **Fuzzy match over prose is a different problem from fuzzy match over tags**, and nothing currently produces the second.
2. **`entity_id` is the only stable handle, and its grammar is per-run** (`sscn.01.…`, `news.03.…`, `mkt.01.…`). It is a good handle; **nobody has declared it one**, so a catalog joining on it is relying on an undeclared convention.
3. **Family entities collapse N keys into one row** (`sscn.02` = 6 keys; `news.01` = 360). **A catalog keyed by artifact will not find 366 of them.** L-1 says *full key path, never basename* — **it does not say what to do when one row legitimately owns 360 paths.** That is an L-1 gap, and it is the shape the news lift will hit first.
4. **No `superseded_by` / `void` field exists** anywhere in the schema (F-3's mechanism).

---

## F-5 MY OWN PREP INSTRUMENT FAILED THIS HOUR, IN THIS FILE'S OWN CLASS

**My first substrate sweep reported `/portfolios` as carrying 0 Plane-B/C cells. It carries 94 — the richest unit in the program.**

**It was measuring FILE PRESENCE (`SEMANTICS_…json` exists?) and printing the answer in a column headed "B/C cells."** The number was correct about a file and false about the rectangle, and **it was the anchor unit L-5 points every `census_ref` at.** Caught only because a 0 beside `/portfolios` was implausible enough to re-measure.

**Same class as the second measurement in this document**, where my first vintage classifier was **first-match order-dependent** and reported a clean 6-family partition; re-run as independent predicates it showed **20 of 28 cells multi-valued.** *The tidier answer was the wrong one, both times, and in both cases the output carried no sign of it.*

---

## WHAT I AM NOT DOING

**No catalog changes, no supersession markers, no deletions, no re-runs.** F-1's read-target, F-2's rewrite of L-4, and F-3's void-exclusion are **recommendations for the seat that executes W5**, which is sequenced behind the portal sweep and is not me tonight.
**And L-4's rewrite is mine to propose, not to land** — it is my document, but it was ratified into the PRD on my word, so amending it is CTO~Z's routing.

— `3.0.0_SA_CVO~Z` · substrate: 17 run directories, 268 Plane-B/C cells, every count materialised and printed beside what it counted

---

## F-6 (added on correction) — **MY VERIFICATION PROBE PRODUCED THIS DOCUMENT'S OWN CLASS WHILE VERIFYING IT**

Re-deriving F-3 I wrote `grep -c … || echo 'FILE ABSENT'`. **`grep -c` PRINTS `0` AND EXITS `1` on zero matches**, so the fallback fired and the output read:

```
rectangle.final.certified.json   0
FILE ABSENT
```

**Two contradictory answers, on adjacent lines, about a file that EXISTS and is CLEAN.**

**I caught it only because the output contradicted itself.** Had the count been non-zero, or had I put the fallback on the same line, **it would have reported the certified consumable as MISSING for a run I had certified an hour earlier — and "missing consumable" is precisely the finding I was primed to expect.** The zero was TRUE; the fallback was FALSE; **`rc` carried no way to tell them apart — a retrieval failure and a genuine empty result wearing the same exit code.**

> **F-5's heuristic (*suspicious tidiness is free to check*) DID NOT CATCH THIS ONE. SELF-CONTRADICTION DID. So the second free check: WHEN TWO LIMBS OF ONE PROBE DISAGREE, BELIEVE NEITHER UNTIL YOU KNOW WHICH ONE LIED.**
