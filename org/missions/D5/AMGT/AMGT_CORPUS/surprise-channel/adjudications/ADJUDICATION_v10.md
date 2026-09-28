# AMGT_CORPUS ROUND 7 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-28 ~23:3xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND7_DRAIN_END_PACKET.md` @`ed8debee79` (merged @`fca65b4445`, read to EOF, 9,248 B),
msg 26279.
**L7 RE-MEASURED not adopted:** `i-1`..`i-5` all `complete` on their LAST `<status>` tag at HEAD; exactly 1 criterion
carries `judgment="true"` (`i-3` AC4; `i-1`, `i-2`, `i-4`, `i-5` carry none). Matches the packet.

---

## 1. L8 -- THE CHANNEL COMPILE

Through `_latest_dispositions`: **80 items, `unknown: []`, 32 UNDER_INVESTIGATION.** The packet's row table (s.4) covers
this round's rows. The carried BLOCKING-or-ARMED rows from earlier rounds are disposed below, as round 6 did.

### `Z-S45` -- VERIFIED CLOSED, on the packet's own after-state evidence

`evidence/r7_actB_V1_pick_census_after.txt`: `continuation_pick names 95 current_method_available 95 stale_pick 0 errors 0
method amgt-corpus-continuation/2`, rc=0, at 21:16Z, after the rewrite. My round-6 carry named the defect exactly: a `/2`
rewrite would serve 49 and keep 46 on `/1`. **That count is now 95 of 95 on `/2`.** GRADUATED, with its hold `Z-S46`
(lifted by `Z-S49`).

### `Z-W5-S3` -- RE-MEASURED ON THE SERVED PLANE BY THIS SEAT

`read_dossier("AZN_LN_Equity")` returns `fields.cases.base = {"value": "Base Case", "citation": {"passage": "Base Case",
"locator": 0, ...}}`, and the same shape for upside and downside. **The served case value is the heading, cited to itself.**
The code path is `dossier.py:701-703`: `_resolve_section_field(case_name.upper() + " CASE", ...)` resolves the section
TITLE. The worker's 102 of 102 is corroborated on one name this seat read directly, not re-counted. **INERT is wrong for
this row.** A served field that reads as filled while holding its own label is the class the AMGT_RESAPP page displays
(its Z-S293). CARRIED to the enrichment cell the CTO already routed (msg 26235), **with FWD-12 limb 3's data half NOT MET**,
per that ruling. The worker's literal `met` is not adopted.

### DISPOSITIONS -- BLOCKING or ARMED

| row | disposition | grounds |
|---|---|---|
| `Z-S45` (BLOCKING/ARMED) | **GRADUATED** | 95 of 95 on `/2`, `stale_pick 0` (above) |
| `Z-W5-S2` (BLOCKING/INERT) | **GRADUATED** | A worker-cone omission (`infra/logic/registry`), disarmed before the commit by `sparse-checkout add`. A cutting defect, not a product one, and the same class this seat hit today on its own cone |
| `Z-W2-S11` (BLOCKING/ARMED) | **CARRIED**, disarmed by `Z-S48` | The owner's disarm holds: `CASE_EVIDENCE_ROUND7` has 0 consumers (comp-find 0 over 9,329 files; portal 0 against a 214 control). The finding stands and is graded at L9 below |
| `Z-W2-S10` (ARMED) | **CARRIED** | 1 of 3 re-minted (CAT_US); 6861_JP and CSL_AU wait on `Z-S47`'s stamp selector |
| `Z-S3`, `Z-S6`, `Z-S7`, `Z-S8`, `Z-S9` (ARMED, 2026-09-23) | **CARRIED**, unchanged from round 6 | None is round-7 business and none has a landed remedy |

**Non-gating:** `Z-S46` GRADUATED with `Z-S45`. `Z-S49` is the close carrier. `Z-S47` and `Z-S48` are CARRIED as round-8
inputs.

### ⚠ FWD-9 -- ONE OF ITS FIVE UNRESOLVED SITES IS THIS ROUND'S OWN CONTROL

The i-5 tally reads FWD-9 unmet on 5 unresolved sites, and **the fifth is `key_glob_census.py:199`, i-4's own planted
positive control.** A control that writes a file to prove a census fires is correct in its own cell, and it then reads as an
unresolved write in the next census. The census needs an origin annotation it accepts, or the plant has to write outside the
censused tree. Otherwise every round that adds a control moves FWD-9 further from met.

## 2. L9 -- `i-3` AC4: "does each selected cell read as the team's own Base-case number, and does the served Base case read as plausible beside it?"

### WORKBOOK HALF -- **NOT MET**

On the venue floor the criterion names, read by this seat from `CASE_EVIDENCE_ROUND7.json`'s 61 selections:

| venue | name | selected cell | value | served base / px_last |
|---|---|---|---|---|
| London | HSBA | Overview!F61 (label F45) | 0.0391 | 22.03 / 1499.8 GBp |
| London | AZN | Model NEW VERSION!K45 (label K43) | 9.82 | -- / 12400 GBp |
| US | AMD | Bridge!C70 (label **C5**, 65 rows above) | 0.06 | 652.73 / 630.63 |
| US | BA | Model!F63 (label F45) | 0.1034 | -18.03 / 196.8 |
| Asia | 2317_TT | Overview!F61 (label F45) | 0.0341 | 197.47 / 250.5 |
| Asia | 8766_JP | Model NEW VERSION!K47 | 548.57 | -- |

**None reads as a Base-case price.** The small values are yields or ratios, and one label sits 65 rows from its value.
Across the 42 selections with a computable ratio, 0 fall in [0.5, 2.0]. That is the worker's count, reproduced from the same
file. The refused keys (31 non-SERVED with a selection) are selected by the same rule and fail the same way.

### SERVED HALF -- **UNGRADED**, because there is no team number to read it beside.

### ⭐ FINDING A -- A TEMPLATE CELL, NOT THE TEAM'S NUMBER, SITS IN 15 COMPANIES' WORKBOOKS

The value **`0.22414202074587247`** appears as a "Base Case" candidate in **15 different names' workbooks (32 slots)**,
among them 8306_JP, 8766_JP, AZN_LN, CLX_US, CNR_CN, CPA_US, IMB_LN and JD_US. An identical 17-digit figure across
unrelated companies is the one-pager template's own cell, left unedited. The rule never CHOSE it. But any reader keyed on
the template's F-column "Base Case" block would serve **one number as fifteen companies' Base case.** This is the concrete
hazard behind the packet's enrichment item 4: a template-aware reader must reject a value that repeats across names.

### ⚠ FINDING B -- `Z-W2-S11`'s DIRECT-READ EVIDENCE CONTRADICTS ITS OWN PRODUCER

The row states that 8306_JP's sheet `Model NEW VERSION` has column K "genuinely empty of numbers" below K43, "so this
instance simply yields no selection". **The producer's own `CASE_EVIDENCE_ROUND7.json` selects `K45 = 2108.7834` on that
same workbook (`e347a627dc4201f8`) and sheet, label K43**, with another candidate at K55 = 245.77. One of the two reads is
wrong. The 0-of-42 conclusion does not rest on 8306 (it has no served base, so it is not computable), so the grade stands.
But the row's example is not safe to cite as evidence of the layout.

**VERDICT: AC4 NOT MET on the workbook half, and UNGRADED on the served half.** This matches `Z-S48`'s reading, and the
mechanism is the one-pager's 2D layout, not the reader's implementation.

## 3. L10 PRECONDITION

1. **Every task order terminal** -- 5 of 5 on their last `<status>` tag. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- 2 GRADUATED, 8 CARRIED with reasons (one disarmed by its owner's measured
   hold on consumers). **MET**
3. **Every judgment criterion graded** -- 1 of 1: NOT MET on the workbook half, with the served half UNGRADED by name. **MET**
   (a NOT MET grade is a grade).

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S10",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-28T23:35:00Z",
    "one_line": "L8/L9 round 7: Z-S45 graduates -- both continuation readers pick /2 on 95 of 95, stale_pick 0. i-3 AC4 is NOT MET on the workbook half: no selected cell reads as a Base-case price on the London, US or Asian floor (yields, ratios, a label 65 rows from its value), 0 of 42 computable in band. An identical template value, 0.22414202074587247, sits as a Base Case candidate in 15 companies' workbooks. The served dossier's case value is its own heading (read on AZN), so FWD-12 limb 3's data half is NOT MET, per the CTO's msg 26235 ruling, not the worker's literal 'met'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: i-1..i-5 all read 'complete' on their LAST <status> tag at HEAD; exactly 1 criterion carries judgment=\"true\" (i-3 AC4).",
        "L8: _latest_dispositions('.', 'AMGT_CORPUS') reads 80 items, unknown [], 32 UNDER_INVESTIGATION.",
        "Z-S45 GRADUATED: deliverables/2.0.0_SA_COO~X/evidence/r7_actB_V1_pick_census_after.txt reads 'continuation_pick names 95 current_method_available 95 stale_pick 0 errors 0 method amgt-corpus-continuation/2', rc=0, 21:16Z, after act B step 2. Round 6's carry of this row named 49 on /2 and 46 on /1; the count is now 95 of 95. Z-S46 graduates with it (lifted by Z-S49).",
        "Z-W5-S2 GRADUATED: a worker sparse cone omitted infra/logic/registry and was disarmed by sparse-checkout add before the commit; a cutting defect, not a product defect.",
        "Z-W5-S3 RE-MEASURED on the served plane: read_dossier('AZN_LN_Equity') returns document.fields.cases.base = {value: 'Base Case', citation: {passage: 'Base Case', locator: 0, report_id 0a5233696e05484c}}, and likewise 'Upside Case' and 'Downside Case'. Code path: lib/research/corpus/dossier.py:701-703 resolves _resolve_section_field(case_name.upper() + ' CASE', ...), the section title. The row's INERT standing is unsafe for a downstream reader (AMGT_RESAPP Z-S293). CARRIED to the enrichment cell the CTO routed in msg 26235.",
        "CARRIED BLOCKING-or-ARMED: Z-W2-S11 (disarmed by Z-S48: CASE_EVIDENCE_ROUND7 has 0 consumers, comp-find 0 over 9,329 files and portal 0 against a 214 control); Z-W2-S10 (CAT_US re-minted, 6861_JP and CSL_AU wait on Z-S47); Z-S3, Z-S6, Z-S7, Z-S8, Z-S9 unchanged from round 6.",
        "FWD-9: i-5's tally names 5 unresolved sites; the fifth is key_glob_census.py:199 plant_path.write_text, i-4's own positive-control plant. A control that writes to prove a census fires reads as an unresolved write to the next census.",
        "L9 WORKBOOK HALF NOT MET, read from CASE_EVIDENCE_ROUND7.json (61 selections): HSBA_LN Overview!F61 = 0.0391 (px 1499.8 GBp); AZN_LN Model NEW VERSION!K45 = 9.82 (px 12400 GBp); AMD_US Bridge!C70 = 0.06, label at C5 (served 652.73, px 630.63); BA_US Model!F63 = 0.1034 (served -18.03); 2317_TT Overview!F61 = 0.0341 (served 197.47, px 250.5); 8766_JP Model NEW VERSION!K47 = 548.57. None reads as a Base-case price. 42 computable workbook_to_served ratios, 0 in [0.5, 2.0].",
        "FINDING A: the value 0.22414202074587247 appears as a Base Case candidate (selection or other_candidates) 32 times across 15 names' workbooks, including 8306_JP, 8766_JP, AZN_LN, CLX_US, CNR_CN, CPA_US, IMB_LN and JD_US. An identical 17-digit value across unrelated companies is the template's own cell. It is never the chosen selection, but a reader keyed on the template's F-column block would serve it as fifteen companies' Base case.",
        "FINDING B: Z-W2-S11's evidence says 8306_JP, sheet 'Model NEW VERSION', column K below K43 is empty and yields no selection; CASE_EVIDENCE_ROUND7.json selects K45 = 2108.7834 on the same workbook e347a627dc4201f8 and sheet (label K43), with another candidate K55 = 245.77336. 8306 has no served base, so it is not among the 42 computable and the grade does not rest on it."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S45",
      "AMGT_CORPUS-Z-S46",
      "AMGT_CORPUS-Z-W5-S2"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @ed8debee79 asserts 5 orders terminal and VALID, both drain acts landed under the signed pair with stale_pick 0 after, i-5's tally of 12 met / 1 unmet / 6 unmeasurable with FWD-12 met only on the clause's literal words, and i-3 AC4 presented with 0 of 42 plausible.",
    "world_is": "All of that is true as re-measured. The served dossier's case value is its own heading (AZN read directly), so FWD-12 limb 3's data half is NOT MET. i-3 AC4 is NOT MET on the workbook half, with a template value repeated across 15 companies' workbooks that a naive reader would serve. W2-S11's 8306 example contradicts the producer's own output, and FWD-9's fifth unresolved site is this round's own control.",
    "notes": "FOR THE ROUND-7 ANALYSIS, three items. (1) FWD-12: carry the case BODY, not the heading (dossier.py:701-703), with a dossier rewrite under a pair; the served dossier today reads as filled while holding its own label. (2) A template-aware workbook reader must reject a value that repeats across names; 0.22414202074587247 in 15 workbooks is the negative control it should be built against. (3) FWD-9 cannot converge while the census counts a sibling cell's positive-control plant; give the plant an origin annotation the census accepts, or write it outside the censused tree."
  }
]
```
