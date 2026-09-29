# AMGT_CORPUS ROUND 8 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~01:3xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND8_DRAIN_END_PACKET.md` @`895a999451` (read to EOF, 9,035 B), msg 26345.
**L7 RE-MEASURED not adopted:** `j-1`..`j-4` all `complete` on their LAST `<status>` tag at HEAD; exactly 1 criterion
carries `judgment="true"` (`j-1` AC3). Matches the packet.

---

## 1. L8 -- THE CHANNEL COMPILE

Through `_latest_dispositions`: **87 items, 36 UNDER_INVESTIGATION.** New since round 7: `Z-S50`..`Z-S53`, `Z-W3-S6`,
`Z-W1-S9`, `Z-W1-S10`, all issuer or worker rows named in the packet's s.5 (plus `Z-S50`, a `to-check` census note).

**THE HOLD, CORROBORATED ON TWO PLANES, NOT ADOPTED.** `Z-S53` disarms `Z-W1-S9` (ARMED) by holding the only
`dossier --write` writer. (i) No change-management entry for a CORPUS dossier rewrite exists since 2026-09-28 23:30Z.
(ii) This seat's own served read of `AZN_LN_Equity` at ~23:2xZ returned `cases.base.value = "Base Case"`, the pre-round
shape. ⚠ The packet's `objects 468` is **not printed** in `evidence/r8_close_runs.txt`; that figure is unverified here.

| row | disposition | grounds |
|---|---|---|
| `Z-W1-S9` (ARMED) | **CARRIED, disarmed by the hold** | Reproduced below; lifts with a table-aware rule |
| `Z-S52` | **GRADUATED** | The owner's correction of `Z-W2-S11`'s 8306 example, which is my round-7 FINDING B: the producer's rows under K43 read `[2028, 2108.7834, 1.378...]`. The contradiction is resolved on the record |
| `Z-W1-S10` | **GRADUATED** | An absent `method_version` keeps the inputs-only no-op; `j-4` AC2 reads `stale_pick 0` of 95 |
| `Z-S53`, `Z-S51`, `Z-W3-S6`, `Z-W5-S3` | **CARRIED** | the hold, and three analysis inputs (s.4 re-derive decision; the six keys' adjusted-EPS gap; heading-only values unchanged because the rewrite is held) |
| `Z-W2-S11`, `Z-W2-S10`, `Z-S3`, `Z-S6`..`Z-S9` | **CARRIED**, unchanged from round 7 | no landed remedy |

## 2. L9 -- `j-1` AC3: "does each served case read as the team's own written case for that name?"

The served rewrite did not run, so this seat ran the **as-built rule itself** (`dossier._resolve_case_field`, the same
function `build()` and `--case-census` call) on two names. It did not grade from the census line alone:

| name | upside | base | downside |
|---|---|---|---|
| ADBE_US | heading_only -> ABSENT | heading_only -> ABSENT | **body, 794 chars**: `2026E ... 2030E` x3, then `EPS 24.16 ... 27.78`, `Multiple 16.0x ... 9.0x ... 6.0x`, `Price 416 ... 233 ... 143 ...` |
| AZN_LN | heading_only -> ABSENT | heading_only -> ABSENT | **body, 556 chars**: the same 15-column table, `Multiple 25.0x / 17.0x / 12.0x` |

**VERDICT: NOT MET.** Downside receives all three cases' numbers, and Upside and Base are served ABSENT, on both names.
**Not one served case reads as that case.** The packet's mechanism is reproduced exactly: the three case headings are the
ROW LABELS of a 3-case x 5-year scenario table on page 0, so "text under the heading" is a table-body read, and only the last
label has anything after it.

⭐ **THE ROUTE TO YES IS SOUND, AND ONE PRECONDITION IS ALREADY MET.** The team's numbers are present, positional and
citable. ADBE's Price-2026 column reads `416 / 233 / 143` (Upside / Base / Downside), a monotone ordering that is itself a
plausibility signal. For the GBP name, **the currency unit survives extraction:** AZN's table carries **U+00A3 (£) 30 times**,
once after each EPS and Price value. A table-aware rule can therefore serve `{metric: {year: value}}` **with its unit**, which
is the currency-scale class this program has been bitten by twice.

⚠ Stated because I nearly filed it the other way: the character first rendered as `?` in this seat's terminal (cp1252). The
codepoint census, not the display, is the reading.

## 3. FOR THE ROUND-8 ANALYSIS (the rulings are the CTO's)

1. **Adopt the packet's table-aware case rule** (s.3), with two additions this grade supports: carry the unit read from the row
   (the £ above), and print the per-name Upside >= Base >= Downside ordering as a census column, not a refusal.
2. **`Z-S51` is a cross-project SERVED decision.** AMGT_RESAPP's `case_rule.py` now moves 48 of 48 served ratios here. It is the
   same Base-case rule this seat flagged at RESAPP round 45 for pairing adjusted EPS with a GAAP P/E. Whether that pairing was
   fixed in `b56fef3032` should be read before re-deriving under it.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 4 of 4. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- `Z-W1-S9` carried under a hold corroborated on two planes; the rest carried
   as in round 7. **MET**
3. **Every judgment criterion graded** -- 1 of 1: NOT MET, by this seat's own run of the rule. **MET**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S11",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T01:35:00Z",
    "one_line": "L9 round 8: j-1 AC3 NOT MET, by this seat's own run of the as-built rule on ADBE and AZN -- Upside and Base are served ABSENT, and Downside receives the whole 3-case x 5-year table (794 and 556 chars). The team's numbers are positional and citable (ADBE Price-2026 416/233/143), and AZN's table carries U+00A3 30 times, so a table-aware rule can serve each case WITH its unit. Z-S52 (my round-7 finding B, corrected by its owner) and Z-W1-S10 graduate; Z-W1-S9 is carried under a hold corroborated on two planes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: j-1..j-4 all read 'complete' on their LAST <status> tag at HEAD; exactly 1 criterion carries judgment=\"true\" (j-1 AC3).",
        "L8: _latest_dispositions('.', 'AMGT_CORPUS') reads 87 items, 36 UNDER_INVESTIGATION. New since round 7: Z-S50, Z-S51, Z-S52, Z-S53, Z-W3-S6, Z-W1-S9, Z-W1-S10.",
        "HOLD corroborated: no change-management entry for a CORPUS dossier rewrite exists since 2026-09-28T23:30Z (git log over org/critical_paths/change_management), and read_dossier('AZN_LN_Equity') at ~23:2xZ returned cases.base.value 'Base Case'. The packet's 'objects 468' is not printed in evidence/r8_close_runs.txt, whose census lines read 'dossier_pick names 95 current_method_available 0 stale_pick 0' and 'case_census names 95 slots 285 body 34 heading_only 68 absent 183 sum 285'.",
        "L9, this seat's own run of dossier._resolve_case_field (the function build() and --case-census call): ADBE_US_Equity upside heading_only, base heading_only, downside body len 794 beginning '2026E 2027E 2028E 2029E 2030E' x3 then 'EPS 24.16 27.86 32.15 35.56 39.33 24.37 ...' and 'Multiple 16.0x x5, 9.0x x5, 6.0x x5' and 'Price 416 446 514 569 629 233 247 283 318 347 143 148 159 ...'; AZN_LN_Equity upside heading_only, base heading_only, downside body len 556 with 'Multiple 25.0x x5, 17.0x x5, 12.0x x5'.",
        "UNIT: the AZN downside text holds non-ASCII codepoints {U+00A3: 30}; repr of '9.08 \\u00a3 10.24 \\u00a3'; report 'ASTRAZENECA Research Pack 2026 06 17_v1.pdf' locator 0. The terminal rendered it as a replacement glyph under cp1252; the codepoint census is the reading.",
        "Z-S52 GRADUATED: its evidence cites CASE_EVIDENCE_ROUND7.json workbook.rows for 8306_JP_Equity, sheet 'Model NEW VERSION', K43 'Base Case', below [2028, 2108.7834, 1.3782161070420165], which is exactly the contradiction ADJUDICATION_v10 FINDING B raised against Z-W2-S11.",
        "Z-W1-S10 GRADUATED: the packet's j-4 AC2 reads 'dossier_pick names 95 current_method_available 95 stale_pick 0' at the worker tip, and the no-op for an absent method_version is covered by j-1 AC1's 12 passing tests."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S52",
      "AMGT_CORPUS-Z-W1-S10"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @895a999451 asserts 4 orders terminal and VALID, the dossier rewrite HELD because the case headings are row labels of a scenario table, and j-1 AC3 read as NO as built.",
    "world_is": "True as re-measured by this seat's own run of the rule on two names. The team's case numbers are present and positional, and the GBP table carries its unit (U+00A3 x30), so the table-aware route can serve each case with its currency. The packet's 'objects 468' figure is not in its cited evidence file.",
    "notes": "FOR THE ROUND-8 ANALYSIS: (1) the table-aware case rule of packet s.3, plus the unit read from the row and a non-enforced Upside >= Base >= Downside census column; (2) before re-deriving under AMGT_RESAPP's case_rule.py (Z-S51), read whether b56fef3032 fixed the adjusted-EPS x GAAP-P/E pairing this seat flagged at RESAPP round 45 (ADJUDICATION_v55)."
  }
]
```
