# AMGT_RESAPP ROUND 45 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-28 ~21:0xZ
**Input:** `2.0.0_SA_COO~Z`'s `round45/DRAIN_END_PACKET.md` @`1b38420c10` (read to EOF, 5,336 B), routed here by
`1.0.0_SA_CTO~Z` at 20:40Z.
**L7 RE-MEASURED not adopted:** `tt-1`..`tt-4` all `complete` on their LAST `<status>` tag at HEAD `963fff9f5a`; exactly
1 criterion carries `judgment="true"` (`tt-3` AC2). Matches the packet. Across the project, 0 of 234 orders are pending or
staged (2 read `withdrawn`).

---

## 1. L8 -- THE CHANNEL COMPILE

Through `_latest_dispositions`: **633 items, 68 files read, `unknown: []`**; GRADUATED 299, DISMISSED_WITH_REASON 307,
UNDER_INVESTIGATION 27. **10 of the 27 gate the slug** (class BLOCKING or `hazard_standing` ARMED): the 9 carried at round 44
plus `Z-W163-S1`.

**Rows since round 44 (6):** `Z-S288` (mine), `Z-S289`, `Z-W163-S1`, `Z-S290`, `Z-S291`, `Z-S292`. The packet lists 4 of
them. The other two are `Z-S288` (this seat's own correction) and `Z-W163-S1`, whose disarm act `Z-S290` the packet does list.

### FWD-30 ON THE SERVED PLANE -- VERIFIED FROM THE TSV, NOT ADOPTED

`round45/close-run/served.tsv`: **95 rows, verdict OK 95 of 95, and `abs_missing` / `fig_missing` / `cit_missing` all 0 on
95 of 95.** This is the measurement round 44 lacked. `Z-S289` records that round 44's "95 of 95" rested on a predicate that
never tested `abs_missing` (86 of 95 dropped the posture absence). My v54 graduated `Z-S268` on that claim. **The graduation
stands, now on correct grounds**, and is re-stated below.

### DISPOSITIONS -- the 10 gating rows

**GRADUATED -- 3, each measured by this seat today:**

| row | measured |
|---|---|
| `Z-S236` (ARMED; its disarm names independent CVO acceptance) | This seat re-ran the row's own instrument (`measure_served.py`, run from a scratch copy so the CRO's evidence file is not overwritten) against deployed `vBSCqd71...Mrew=`: **12 of 12 documents 200 SERVED, 210 sentences, 0 no-span**, and the 401 no-firm control fired. ⚠ BOUND: `historical_text_sets_matched: 0`. The 12 texts were re-drafted after the row was filed, so this proves the SERVED state on the row's full population, not that the reader repair caused it |
| `Z-S251` (ARMED) | The row's own query re-run: `comp-find '0A1733\|10, ?23, ?51' portal/src portal/scripts` -> **10 hits across 1137 files**, all in the row's own allow-listed categories. **None of the eleven named prose sites, `ui-smoke.mjs:635` or `PrintExportAction.tsx:136` remains.** This matches `W165-S1` (1135 files then) |
| `W130-S1` (BLOCKING) | The fixtures file is TRACKED in portal (@`513bb3c5`, relocated under `__harness__/tests/`). The naming gate on it reads `1 seen, PASS 0 graded`. **The zero is the exemption, not blindness.** Control: the SAME bytes at a non-exempt path (`.../data/uiContractFixtures.json`) read **`REFUSE 48 graded`, rc=1** |

**CARRIED -- 7, each unremedied, each with its reason:** `Z-S237` (`.tools/safe-commit.sh` has no detached-HEAD limb: a
search for `symbolic-ref|detached` finds 0 hits) - `Z-S238` (the observability gap; its fix is expressly not authorised on the
row's word) - `Z-S248` (a Bloomberg-pipeline surface, another owner) - `Z-S255` (portal hooks; `0.0.0_AB_MSTR~Z`'s) -
`Z-W158-S1` + `Z-S276` (two arms still unmeasured) - `Z-W163-S1`: **disarmed by condition, not remedied**. No RESAPP order
is live (0 of 234), so no worker can be told to commit the gitlink. The remedy is the round-46 template (packet s.5 item 3).
⚠ `Z-S290`'s one_line says the template "no longer tells a worker" to move the gitlink, but its own `disarm_owner` and the
packet both say that change is still owed. **This disposition rests on the measured condition, not on that sentence.**

**NON-GATING rows this round:** `Z-S289` GRADUATED (its remedy is tt-1 + tt-2, measured above). `Z-S288` GRADUATED (my
correction is absorbed by that measurement). `W165-S1` GRADUATED (it asked for this seat's read, given above). `Z-S292`
CARRIED, the disposition the CTO named as mine: INERT, the remedy is the round-46 harness cell, and the close run avoided it
by reading the PUBLISHED gitlink in an isolated worktree. `Z-S291` and `Z-S290` CARRIED as notes. `W136-S1` DISMISSED (a
prose miscount in a closed order's text, with no grading consequence).

## 2. L9 -- `tt-3` AC2, GRADED ON THE RENDER

**The criterion:** *"does each served value read as a price in a named currency, the same on both surfaces?"* The sample
exists because my round-44 grade found that clauses (b) and (c) were unreachable. **Both are now reachable, and that part of
the fix is real.**

### (a) A NAMED CURRENCY -- **PASS, 3 of 3**

The page shows RKT `7386.63633 GBp`, AMD `652.7344928 USD` and GOOGL `537.6961078500001 USD`, each beside a Price tile in the
same unit.

### (b) THE SAME ON BOTH SURFACES -- **PASS, 3 of 3, read by this seat on the three `model.png`**

Each render's Base case line matches `AC4_SAMPLE.json`'s `base_line` byte for byte. The renders' headers read `Sep 26, 2:50 /
2:52 PM`, so these are **fresh captures (18:50-18:52Z), not round 43's replay**. That lifts the round-44 bound. The control
reads 18 of 18 states. ⚠ BOUND: the captures were taken under `LK9h47ju...`. This seat verified that tt-1's code diff
(`270064be9b^1..270064be9b`) is **2 hunks, both inside `_posture_markdown`**. It did NOT diff the whole deployed closure of
`vBSCqd71...`.

### (c) READS AS A PRICE -- **PASS IN FORM, 3 of 3; WITH A METHODOLOGY FINDING THE BAND CANNOT SEE**

Ratios to `px_last`: RKT 1.500, AMD 1.035, GOOGL 1.563, all inside `[0.33, 3.0]`. **As written, the criterion is met.**

⛔ **But the value is built from two inputs on different bases, and one of them carries no basis field.** The formula is
`BEST_EPS (FY1) x median(PE_RATIO)`. The served `consensus_eps` input carries `{value, mnemonic, fiscal_period,
fiscal_year, period_end_date, source}` and **no `basis`**, while every `fiscal_year_figures` row beside it does carry one.
**`PE_RATIO` measurably tracks the GAAP series:** AMD 2023 `PE_RATIO` = 229.06, against `PX_LAST/IS_EPS` = 278 and
`PX_LAST/IS_COMP_EPS_ADJUSTED` = 55.6. `BEST_EPS` behaves like an ADJUSTED figure (INFERRED from magnitude, not measured):
AMD's 7.472 is 1.79x its last adjusted year (4.17) and 2.80x its last GAAP year (2.67).

**On a same-basis proxy this seat built** (median of `PX_LAST / IS_COMP_EPS_ADJUSTED` over the served years; INFERRED, not
the producer's rule):

| name | served base | ratio | same-basis proxy | ratio |
|---|---|---|---|---|
| AMD | 652.73 USD | 1.035 | ~415.6 USD | ~0.66 |
| RKT | 7386.6 GBp | 1.500 | ~5942 GBp | ~1.21 |
| GOOGL | 537.70 USD | 1.563 | ~511.6 USD | ~1.49 |

⭐ **AMD was chosen for clause (c) because its ratio "sits close to 1". Its closeness to 1 is produced by the basis mismatch.**
On a same-basis construction it reads ~0.66, which is still inside the band. **The band is necessary but blind to this: it
would pass AMD either way.** Where GAAP and adjusted EPS are close (GOOGL), the two constructions agree.

⚠ **GOOGL, UNGRADED on one input:** `BEST_EPS` FY1 18.943 is **1.75x** its last closed adjusted year (10.81), and that one
input drives GOOGL's 1.56. Checking it needs a vendor read, which this seat does not hold. It is recorded, not graded.

**VERDICT: AC2 PASSES (a) 3 of 3, (b) 3 of 3 on fresh captures, and (c) 3 of 3 as the criterion is written.** The
methodology finding goes to the analysis. It is not held against the round, because the Base-case formula is a methodology
choice, and the served page itself says the case methodology is "to be discussed with Andrew".

**Still visible and carried by the packet (item 4):** `537.6961078500001 USD` -- the raw float repr, round 43's second defect.

## 3. L10 PRECONDITION

1. **Every task order terminal** -- 4 of 4 on their last `<status>` tag. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- 10 gating: 3 GRADUATED on this seat's own measurements, 7 CARRIED with
   reasons (one disarmed by a measured condition). **MET**
3. **Every judgment criterion graded** -- 1 of 1, on the render, with its bounds and one input UNGRADED by name. **MET**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S423",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-28T21:00:00Z",
    "one_line": "L9 round 45: tt-3 AC2 PASSES -- (a) currency named 3 of 3, (b) same on both surfaces 3 of 3 on FRESH post-rs-2 captures, (c) reads as a price 3 of 3 as written. But the Base case multiplies BEST_EPS, which carries no basis field and behaves as adjusted, by a trailing PE_RATIO that measurably tracks GAAP; AMD's ratio 1.035, the reason it was sampled for (c), is ~0.66 on a same-basis proxy, and the [0.33, 3.0] band passes it either way. L8: FWD-30 verified from the TSV at 95 of 95 with abs_missing 0; Z-S236, Z-S251 and W130-S1 graduated on this seat's own re-measurements; Z-S268's graduation re-grounded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: tt-1..tt-4 all read 'complete' on their LAST <status> tag at HEAD 963fff9f5a; exactly 1 criterion carries judgment=\"true\" (tt-3 AC2). Project-wide, 0 of 234 orders are pending or staged; 2 read 'withdrawn'.",
        "L8: _latest_dispositions reads 633 items over 68 files, unknown []; GRADUATED 299, DISMISSED_WITH_REASON 307, UNDER_INVESTIGATION 27, of which 10 are BLOCKING or ARMED. Rows since round 44: Z-S288, Z-S289, Z-W163-S1, Z-S290, Z-S291, Z-S292 (6); the packet lists 4 of them.",
        "FWD-30 VERIFIED, NOT ADOPTED: round45/close-run/served.tsv has 95 rows; verdict OK 95 of 95; abs_missing, fig_missing and cit_missing are 0 on all 95. That is the measurement Z-S289 shows round 44 lacked, so Z-S268's v54 graduation stands, re-grounded on this TSV.",
        "Z-S236 GRADUATED: the row's own instrument (measure_served.py, run from a scratch copy so the CRO's SERVED_CENSUS.json is untouched) against deployed vBSCqd71wGn1GNOpaWGKr+KdI6t+zo3QVovzEd9Mrew= (last_modified 2026-09-26T23:35:04Z) reads 12 of 12 documents 200 SERVED, 210 served sentences, 0 no-span, and the no-firm control returns 401. BOUND: historical_text_sets_matched is 0, so the texts were re-drafted after filing; this proves the served state on the row's full population, not the repair's causality.",
        "Z-S251 GRADUATED: the row's own query, comp-find '0A1733|10, ?23, ?51' portal/src portal/scripts, returns 10 hits across 1137 files (SURFACED 7, CONFIG 1, TEST 2), all in the row's own allow-listed categories; none of the eleven named prose sites, ui-smoke.mjs:635 or PrintExportAction.tsx:136 is present.",
        "W130-S1 GRADUATED: the fixtures file is tracked in portal since 513bb3c5, under __harness__/tests/. The naming gate on it reads '1 seen, PASS 0 graded', rc=0. Control: the same bytes rewritten to a non-exempt path (portal/src/pages/SecurityAnalysis/data/uiContractFixtures.json) read 'REFUSE 48 graded', rc=1. The zero is the exemption operating, not a blind gate.",
        "CARRIED 7: Z-S237 (a search of .tools/safe-commit.sh for symbolic-ref|detached returns 0 hits, so the limb does not exist); Z-S238; Z-S248; Z-S255; Z-W158-S1 + Z-S276; Z-W163-S1, disarmed by the measured condition (0 live RESAPP orders) with its remedy owed as the round-46 template. Z-S290's one_line says the template 'no longer tells a worker' to move the gitlink, which contradicts its own disarm_owner and packet s.5 item 3, so this disposition rests on the condition, not on that sentence.",
        "L9 (a) PASS 3 of 3: the renders show RKT 7386.63633 GBp, AMD 652.7344928 USD and GOOGL 537.6961078500001 USD, each beside a Price tile in the same unit.",
        "L9 (b) PASS 3 of 3, read by this seat on round45/real-run-<key>/model.png: each render's Base case line equals AC4_SAMPLE.json's base_line byte for byte; the render headers read Sep 26 2:50/2:52 PM, and _provenance.captured_at is 18:50:45Z / 18:52:48Z / 18:52:52Z, so these are fresh captures and the round-44 replay bound is lifted. BOUND: the captures were taken under LK9h47ju...; this seat verified tt-1's code diff (270064be9b^1..270064be9b) is 2 hunks, both in _posture_markdown, but did not diff the full deployed closure of vBSCqd71.",
        "L9 (c) PASS 3 of 3 in form: ratios to px_last are RKT 1.500, AMD 1.035, GOOGL 1.563, all inside [0.33, 3.0].",
        "METHODOLOGY FINDING: the served model_cases.base.inputs.consensus_eps carries value, mnemonic BEST_EPS, fiscal_period, fiscal_year, period_end_date and source, but NO basis field; every fiscal_year_figures row carries 'basis'. PE_RATIO tracks the GAAP series: AMD 2023 PE_RATIO 229.06, against PX_LAST/IS_EPS = 147.41/0.53 = 278 and PX_LAST/IS_COMP_EPS_ADJUSTED = 147.41/2.65 = 55.6. BEST_EPS behaves as adjusted (INFERRED from magnitude): AMD 7.472 is 1.79x its last adjusted year 4.17 and 2.80x its last GAAP year 2.67.",
        "SAME-BASIS PROXY (INFERRED, this seat's construction, not the producer's rule): median of fiscal-year PX_LAST / IS_COMP_EPS_ADJUSTED times the same BEST_EPS gives AMD ~415.6 USD (ratio ~0.66) against the served 652.73 (1.035); RKT ~5942 GBp (~1.21) against 7386.6 (1.500); GOOGL ~511.6 USD (~1.49) against 537.70 (1.563). AMD was sampled for clause (c) because its ratio 'sits close to 1', and that closeness is produced by the basis mismatch; the band passes AMD either way.",
        "UNGRADED BY NAME: GOOGL BEST_EPS FY1 18.943 is 1.75x its last closed adjusted year 10.81 and drives GOOGL's ratio; checking it needs a vendor read this seat does not hold.",
        "NON-GATING: Z-S289, Z-S288 and W165-S1 GRADUATED on the measurements above; Z-S292 CARRIED (INERT; the round-46 harness cell; the close run avoided it by reading the published gitlink in an isolated worktree); Z-S291 and Z-S290 CARRIED as notes; W136-S1 DISMISSED_WITH_REASON in the companion row."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S236",
      "AMGT_RESAPP-Z-S251",
      "AMGT_RESAPP-W130-S1",
      "AMGT_RESAPP-Z-S268",
      "AMGT_RESAPP-Z-S288",
      "AMGT_RESAPP-Z-S289",
      "AMGT_RESAPP-W165-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @1b38420c10 asserts 4 orders terminal and VALID, FWD-30 met on the served plane at 95 of 95 with absences missing 0, the page render PASS on 3 of 3 names with a control on 18 of 18 states, the Model case line unchanged by tt-2, and 4 new rows.",
    "world_is": "All of that is true as re-measured. The packet does not carry three things. First, 2 more rows since round 44 (Z-S288, Z-W163-S1). Second, three ARMED/BLOCKING carried rows are now remedied on their own instruments (Z-S236, Z-S251, W130-S1). Third, clause (c) passes because the band cannot see a GAAP/adjusted basis mismatch: AMD's near-1 ratio, the reason it was sampled, is ~0.66 on a same-basis proxy.",
    "notes": "FOR THE ROUND-45 ANALYSIS, three items. (1) THE BASE-CASE BASIS. The cheapest mechanical move is to carry 'basis' on consensus_eps, as every fiscal_year_figures row already does, so a consumer can refuse a mismatch. Whether the multiple should be taken on the same basis as the EPS is a METHODOLOGY choice, and the page already routes case methodology to Andrew; this row names the mismatch and does not choose. (2) THE BAND IS NOT A PLAUSIBILITY ORACLE FOR THIS FORMULA: it passed AMD at 1.035 and would pass it at 0.66. A round-46 judgment criterion on the Base case should name the basis of each input, not only the ratio. (3) GOOGL's FY1 consensus at 1.75x its last adjusted year is one vendor read from graded; it rides the next authorised Bloomberg use, never a new ask from this seat."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S424",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-28T21:00:00Z",
    "one_line": "W136-S1 dismissed: a prose miscount (13 named checks, 'CHECKS-OK 12 of 12') in a CLOSED order's text; the mechanical grade ran against the instance's own expect, so there is no grading or code consequence.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The row's own text (hazard_standing INERT): the discrepancy is in AMGT-rl-7's narrative sentence, and the grade runs against the instance's own expect, never the order's narrative count.",
        "tt-4's measurement (deliverables/0.9.0_WK_AMGT_RESAPP~165/CARRIED_ROWS.json) re-ran the harness and records the row's closes_when as a disarm carrier noting the prose-only nature and folding the row. This row is that carrier."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-W136-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A task-order prose artifact with no code or grading consequence; the order is closed.",
    "spec_asserts": "W136-S1 stands UNDER_INVESTIGATION.",
    "world_is": "Nothing is left to investigate: the order is closed and its grade never read the miscounted sentence.",
    "notes": ""
  }
]
```
