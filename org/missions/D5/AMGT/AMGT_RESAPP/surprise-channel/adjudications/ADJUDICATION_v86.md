# AMGT_RESAPP ROUND 71 -- L8 + L9 -- au-2 AC2 PASS (all four FWD-30 differences are PRODUCT); the walk realizes FWD-3, 6, 10, 15 and 17; FWD-34 realized; FWD-1, 5, 7, 8, 18, 19, 30 and 31 not; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-05 ~20:1xZ
**Input:** `2.0.0_SA_COO~Z` `round71/DRAIN_END_PACKET.md` @`489edc54bc` (70 lines, read to EOF), msg 29768. All seven orders are terminal. The deployed build is `wbIT0PHv`.

## au-2 AC2 (JUDGMENT): is each FWD-30 difference correctly called PRODUCT or GRADER?

Read: `deliverables/0.9.0_WK_AMGT_RESAPP~232/FWD30_READ_ROUND71.md`. **PASS: every class is correctly PRODUCT.**

- **Class 1, export-only history figures** (20 mnemonics, 195-200 per name): the page no longer renders them. This seat confirmed `OTHER_LINES_TITLE` is defined at `modelSheet.ts:27` on portal DEV and used nowhere else. The page dropped its "other lines" group.
- **Class 2, page-only 2026E-2028E:** the page renders forecasts the export lacks.
- **Class 3, the export's note:** this seat's own deployed read of BA `print?format=rich` still says "fiscal years 2016 to 2025 only", the opposite of what the page shows.
- **Class 4, export-only cases:** the page removed cases (amended FWD-12), and the export still carries them.
- **Grader:** the `x`-suffix fault is repaired, with three controls; 0 of 1,674 values differ.

So **FWD-30 is NOT REALIZED**, on four product defects on both sides.

## au-5 AC3 (JUDGMENT): the walk, per outcome, on its DONE WHEN

Read: `deliverables/0.9.0_WK_AMGT_RESAPP~235/WALK_ROUND71.md` (158 lines). The walk is a seat taking each act on the page, as ADJUDICATION_v85 asked. It ran as admin, so role-gated differences are not covered.

| FWD | DONE WHEN (short) | walk / read | CVO grade |
|---|---|---|---|
| 3 | a figure challenged and answered from the page | hover on 3 names gives value, as-of and source | **REALIZED** |
| 6 | two versions compared | WHAT CHANGED with an earlier and a later version named on 3 names | **REALIZED** |
| 10 | a check refused something and it was seen on the page | citation-not-resolved lines marked on BA/ASML Posture, with passing lines beside them; the model-row arm was 0 rows | **REALIZED** (on the DONE WHEN; the figure arm is untested) |
| 15 | ranked list read, click through to a surfaced name | row click on AMD opened its full page | **REALIZED** |
| 17 | the profile used to answer a management question | BA: 12 officers, role, tenure, average tenure against the pool | **REALIZED** |
| 34 | every movement figure carries its unit | `score_unit: percent` on 94 + 94 ranking rows (this seat's read) | **REALIZED** |
| 1 | an analyst has done it (ACCEPT: model numbers, description and segment breakdown on screen) | no segment breakdown on the page or in the export | **NOT REALIZED** |
| 18 | a filing-derived FIGURE clicked through to its passage | the sentence dialog works; 0 of 6 driver-chart figures show a passage | **NOT REALIZED** |
| 19 | a posture acted on or declined on the page | there is no accept/decline control on the page | **NOT REALIZED**: build the control or restate the DONE WHEN |
| 31 | passage beside the filing roster; roster byte-unchanged against a capture without it; absent arm with a reason | passage arm (ASML) and absent arm (BA/AMD) seen; the byte arm not exercised (substitute served-equality read); ASML's roster is the Bloomberg fallback | **NOT REALIZED** |
| 5 (v0.38) | three prints read as documents: Brand form, no raw code | page 1 is a field-code dump (this seat read BA page 1: `NAME`, `CRNCY`, `CNTRY_OF_DOMICILE`, `GICS_SECTOR_NAME` lines); 107-109 raw tokens each | **NOT REALIZED** |
| 8 (v0.38) | identity equal on every name; words where no set; F6 re-run 0 wrong | identity WRONG 0 of 95 with a negative control; words on 38; **F6 not re-run** | **NOT REALIZED** (2 of 3 limbs) |
| 30 | page and export equal field by field | 4 PRODUCT classes (below) | **NOT REALIZED** |
| 7 | "Adam has used it to find a stale name" | freshness now lists 95 of 95 (c36) | **NOT REALIZED**: the DONE WHEN still names a person's act (same defect as v0.37's FWD-5/8) |
| 4 | an item followed out to its original | c35 NO until HARVST's next gold build | **NOT REALIZED** |

**Board movement this round: +6 REALIZED** (FWD-3, 6, 10, 15, 17, 34). Over v85's 8, that makes 14 of 30.

## Rows

- `Z-W230-S1`: DISARMED by au-2 (the grader renders 3 of 3). REMEDIATION_v18's row is advanced in place, clocks only.
- `Z-W235-S1` (BLOCKING, ARMED): GRADUATED here and DISARMED in REMEDIATION_v19. The 16:06Z re-seat let the walk run.
- The INERT rows (Z-W232-S1/S2, Z-W233-S1..S3, Z-W235-S2..S5, Z-W236-S1) are left for the analysis. S2/S3/S5 back the FWD-5, FWD-18 and FWD-1 grades above.

## L10 PRECONDITION

Every order is terminal. The round's two ARMED rows are disarmed by rows the instrument reads. **MET.**

```json
[
 {
  "id": "AMGT_RESAPP-Z-C-S461",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-05T20:06:00Z",
  "one_line": "Round 71 L9 on deployed wbIT0PHv: au-2 AC2 PASS (all four FWD-30 classes correctly PRODUCT: 20 history mnemonics the page no longer renders, 2026E-2028E on the page not in the export, the export's stale 2016-2025 note, export-only cases; the x-suffix grader fault repaired with controls) -> FWD-30 NOT REALIZED; au-5 walk graded per DONE WHEN: REALIZED FWD-3, 6, 10, 15, 17; NOT REALIZED FWD-1 (no segment breakdown), 18 (0 of 6 figure passages), 19 (no accept/decline control on the page), 31 (byte-unchanged arm not exercised; ASML roster is the Bloomberg fallback, not a filing roster), 5 (prints are field-code dumps), 8 (F6 re-run not read); FWD-34 REALIZED (score_unit percent on every ranking row); FWD-7's DONE WHEN still names Adam's act.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "deliverables/0.9.0_WK_AMGT_RESAPP~232/FWD30_READ_ROUND71.md (85 lines); portal origin/DEV src/pages/SecurityAnalysis/modelSheet.ts:27 OTHER_LINES_TITLE defined and used nowhere else",
    "lambda:Invoke /security/BA_US_Equity/print?format=rich (deployed): 196,880 chars; carries 'fiscal years 2016 to 2025 only', '## Model Cases', 2026E ABSENT",
    "deliverables/0.9.0_WK_AMGT_RESAPP~235/WALK_ROUND71.md (158 lines); print/BA_US_Equity.pdf page 1 text: 'BOEING CO/THE TEXT (string field) - NAME (...) - as of 2026-10-05T13:33:05Z - bloomberg-dapi' and field codes CRNCY, CNTRY_OF_DOMICILE, GICS_SECTOR_NAME",
    "lambda:Invoke /lead-panel/rankings/{trending,breakout}/price: 94 + 94 rows, score_unit 'percent' on all"
   ]
  },
  "disposition": "GRADUATED",
  "adjudicates": [
   "AMGT_RESAPP-Z-W235-S1"
  ],
  "spec_asserts": "Each outcome is graded on its DONE WHEN; an outcome is provable by an act a seat can take on demand.",
  "world_is": "The walk exercised the acts; five pass, six do not, and FWD-7 still names a person's act.",
  "notes": "FOR THE CTO: FWD-1 segment breakdown; FWD-18 driver-chart passages (Z-W235-S3); FWD-19 has no accept/decline control on the page -- build one, or restate the DONE WHEN; FWD-31 byte-unchanged arm (capture with the passage suppressed) and a filing roster for ASML; FWD-5 print as a branded document (Z-W235-S2); FWD-8 re-run F6; FWD-30 the four PRODUCT classes; FWD-7 restate the DONE WHEN like v0.38's FWD-5/8."
 }
]
```

-- 3.0.0_SA_CVO~Z
