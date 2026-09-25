# AMGT_RESAPP ROUND 41 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-25 ~04:2xZ
**Input:** `2.0.0_SA_COO~Z`'s `DRAIN_END_PACKET.md` @`99c271fb15` (read to EOF), msg 25859.
**L7 state, RE-MEASURED not adopted:** `rp-1` terminal on its LAST `<status>` tag; 4 acceptance criteria,
**1 carrying `judgment="true"`** (AC4), matching the packet.

---

## 1. L8 -- THE CHANNEL COMPILE

Denominator **2**. **Both CARRIED**, neither closed:

| row | disposition here |
|---|---|
| `Z-W158-S1` | **CARRIED** -- 2 of 89 keys carry a literal `/`. A standing exposure no act of this round reaches; the remedy is in the identity layer |
| `Z-S276` | **CARRIED** -- the disarm owner's read BOUNDS it (16 AMGT routes single-segment, 106 read, **0 greedy**, so a raw `/` key matches no route) but names **two arms still unmeasured**: the encoded path, and the page's key encoding. A row with open arms is not a closed row |

## 2. L9 -- `rp-1` AC4, GRADED

**The criterion:** *"for each row, does it name an EXPORT defect, a PAGE defect or a DATA gap?"* The packet
offers its three classes as **input and explicitly not as the grade** -- correct, and the reason this
grade could be independent.

⭐ **THE ISSUER READ 2 OF 84 AND COUNTED THE OTHER 82. IT DID NOT NEED TO: `rp-1.AC4.log` CARRIES PER-NAME
COUNTS FOR ALL 84**, so the classification is computable from the table itself. Done here over the printed
denominator:

| class | measured over 84 | packet |
|---|---|---|
| export **DROPS** a page absence (`abs_missing>0`) | **80** | 80 ✓ |
| export **ADDS** absence lines (`abs_extra>0`) | **83** | "820 extra lines", no name count |
| export **ADDS** figures (`fig_extra>0`) | **12** | 12 ✓ |
| export **DROPS** a page figure (`fig_missing>0`) | **1** (`9433_JP_Equity`) | 1 ✓ |
| citation differences | **0** | not stated |
| **falling outside all four** | **0** | -- |

**MECE by subtraction from the printed denominator: zero rows uncovered.** The packet's classes are
exhaustive, and two counts it did not state are now measured.

⭐ **AND THE 84 ARE NOT 84 PROBLEMS -- 72 OF THEM ARE TWO SHAPES:**

```
  (abs_page 16, abs_rich 20, extra 5,  missing 1)  ->  37 names
  (abs_page  5, abs_rich 20, extra 16, missing 1)  ->  35 names
```
**The export emits ~20 absence markers regardless of what the page shows (5 or 16).** That is the
structural form of the packet's class-2 diagnosis -- one marker per empty section, unconditionally, against
the page's single empty-state panel -- and it is now measured across the population rather than inferred
from two names.

### The answer AC4 asks for

**All four classes are EXPORT-side**, under FWD-30's clause *"NOTHING in the export that is not on the
page"*, which is **directional**: it constrains the export against the page. The **58 of 89 pages showing
zero figures** are a **DATA gap** -- a defect of neither surface.

⚠ **AND THE PAGE-SIDE READING IS NAMED RATHER THAN SMUGGLED IN.** The packet offers that one is possible
for each class. It is -- a page collapsing ~20 absences into one panel could be said to under-disclose --
**but that is a DESIGN question the fence does not settle**, and answering it inside a conformance grade
would import a judgment the criterion never asked for. Recorded for the analysis; not graded here.

### ⭐ THE FINDING OF THE ROUND, AND IT IS THE ISSUER'S OWN SENTENCE

> *"Why BA passed: it exercises none of the three classes. Round 40's single-name pass was true, and was
> also the one name that could not show them."*

**Round 40 graded FWD-30 REALIZED on the one name structurally incapable of exhibiting any of the three
defects.** The round-40 L10 bounded it correctly -- *"REALIZED for the exercised name and UNMEASURED for
the other 88"* -- so the bound held. What is new is that the single sample was not merely unrepresentative
but **unfalsifiable**: BA has a fully drafted thesis, a landed management object and a comparable, so none
of the three classes could fire on it.

⭐ **A SAMPLE OF ONE CANNOT BE JUDGED UNREPRESENTATIVE UNTIL THE POPULATION IS MEASURED** -- which is what
this round did, and why 1 of 89 became 5 of 89.

## 3. BOUNDS

1. **The population is the SUPERSEDED 89-name snapshot** (`universe.json`, read 2026-09-10T23:18Z). The
   live group reads 94. The packet discloses this plainly and says so: *"This round measures the snapshot,
   not the live group."* The five-name residue -- GOOGL, LLY, PWR, UNH, AMD -- waits on Andrew's carded
   word. ⚠ **Those five are the folders added SINCE the snapshot, i.e. the sub-population most likely to
   behave differently**, which is exactly where a preflight blind to existing state last surprised this
   estate.
2. **The figure axis is only meaningfully exercised on 31 of 89.** 58 pages show zero figures, so an OK
   there "would say little about figures", as the packet states.
3. **Deployed bytes named and invariant:** CodeSha256 `pmH20bb+...nXZo=`, 445 of 445 route invokes 200.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 1 of 1. **MET**
2. **Every round-41 row dispositioned** -- 2 of 2, both carried with named reasons. **MET**
3. **Every judgment criterion graded** -- 1 of 1, over the full 84 rather than the 2 read. **MET**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S419",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-25T04:25:00Z",
    "one_line": "L9 round 41: AC4 graded over ALL 84 NOT_OK rows rather than the 2 the issuer read, because the log carries per-name counts -- the four defect classes are MECE with ZERO rows uncovered, citations are clean on 84 of 84, and 72 of the 84 collapse into just TWO signatures. And round 40's single-name FWD-30 pass was on the one name structurally incapable of exhibiting any of the defects.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: rp-1 terminal on its LAST <status> tag; 4 acceptance criteria, 1 carrying judgment=\"true\" (AC4), matching the packet.",
        "THE ISSUER READ 2 OF 84 AND COUNTED 82, AND DISCLOSED THAT PLAINLY. It did not need to: rp-1.AC4.log carries per-name counts for every one of the 84 (fig_page/fig_rich/fig_missing/fig_extra, cit_*, abs_page/abs_rich/abs_missing/abs_extra), so the classification is computable from the table. Computed here over the printed denominator of 84.",
        "THE FOUR CLASSES, MEASURED OVER 84: export DROPS a page absence 80 (packet 80); export ADDS absence lines 83 (packet gave a line count, 820, but no name count); export ADDS figures 12 (packet 12); export DROPS a page figure 1, 9433_JP_Equity (packet 1). CITATION DIFFERENCES: 0 across all 84 -- the one axis that is clean everywhere, worth naming because it is the part that works. ROWS FALLING OUTSIDE ALL FOUR: 0, so the packet's classes are EXHAUSTIVE by subtraction from the printed denominator.",
        "AND THE 84 ARE NOT 84 PROBLEMS: 72 of them are TWO signatures -- (abs_page 16, abs_rich 20, extra 5, missing 1) on 37 names and (abs_page 5, abs_rich 20, extra 16, missing 1) on 35. The export emits ~20 absence markers REGARDLESS of whether the page shows 5 or 16. That is the structural form of the packet's class-2 diagnosis, measured across the population instead of inferred from two names.",
        "THE ANSWER AC4 ASKS FOR: all four classes are EXPORT-side under FWD-30's clause 'NOTHING in the export that is not on the page', which is DIRECTIONAL -- it constrains the export against the page. The 58 of 89 pages showing zero figures are a DATA gap, a defect of neither surface.",
        "THE PAGE-SIDE READING IS NAMED AND NOT SMUGGLED IN. A page collapsing ~20 absences into one empty-state panel could be said to under-disclose, and the packet offers that reading for each class. But that is a DESIGN question the fence does not settle, and answering it inside a conformance grade would import a judgment the criterion never asked for. Recorded for the analysis, not graded here.",
        "THE FINDING OF THE ROUND IS THE ISSUER'S OWN SENTENCE: 'Why BA passed: it exercises none of the three classes. Round 40's single-name pass was true, and was also the one name that could not show them.' Round 40 graded FWD-30 REALIZED on the one name structurally incapable of exhibiting any of the three defects -- BA has a fully drafted thesis, a landed management object and a comparable. The round-40 L10's bound held ('REALIZED for the exercised name and UNMEASURED for the other 88'); what is new is that the sample was not merely unrepresentative but UNFALSIFIABLE. A sample of one cannot be judged unrepresentative until the population is measured, which is what this round did.",
        "BOUNDS. (1) The population is the SUPERSEDED 89-name snapshot read 2026-09-10T23:18Z; the live group reads 94 and the packet says plainly 'this round measures the snapshot, not the live group'. The five-name residue GOOGL/LLY/PWR/UNH/AMD waits on Andrew's carded word -- and those five are the folders ADDED since the snapshot, the sub-population most likely to behave differently, which is exactly where a preflight blind to existing state last surprised this estate. (2) The figure axis is meaningfully exercised on only 31 of 89, since 58 pages show zero figures. (3) Deployed bytes named and invariant: CodeSha256 pmH20bb+L1Kcejf4MKS4tVt+tCIPgeHwSZAsTe+nXZo=, 445 of 445 route invokes answering 200."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @99c271fb15 asserts one order terminal and VALID, a served export across the 89-name snapshot reading 5 OK and 84 NOT_OK, three export defect classes read on two names and offered as input rather than as the grade, and two new rows.",
    "world_is": "All of that is true as re-measured. The three classes are exhaustive over the 84 and two of their name-counts were not stated; a fourth axis, citations, is clean on every row; and 72 of the 84 reduce to two signatures, so the defect count is a shape count rather than a name count.",
    "notes": "BOTH ROWS CARRIED AND NEITHER CLOSED: Z-W158-S1 is a standing exposure no act of this round reaches, and Z-S276 BOUNDS it usefully (0 greedy routes of 106 read) while naming two arms still unmeasured -- the encoded path and the page's key encoding. A row with open arms is not a closed row. ⭐ FOR THE ANALYSIS: the largest thing this round changes is not the 5-of-89 number but what it says about the PREVIOUS one. FWD-30 was REALIZED last round on a single name, correctly bounded as unmeasured for the other 88, and that name turns out to be the only one of the 89 on which none of the three defects could have fired. The bound was honest and the sample was still the worst possible draw -- which is an argument for measuring a population before trusting a pass, not for distrusting the seat that bounded it."
  }
]
```
