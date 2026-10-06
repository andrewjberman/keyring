# AMGT_RESAPP ROUND 73 -- L8 + L9 -- FWD-31 REALIZED (board 18 of 30); FWD-18 and FWD-1 are served but not drawn by the page; FWD-5 readable but not branded; FWD-7's page not yet usable; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-06 ~05:4xZ
**Input:** `2.0.0_SA_COO~Z` `round73/DRAIN_END_PACKET.md` @`26c43d54cc` (63 lines, read to EOF), msg 29917. All eight orders are terminal. The deployed build is `satkY3HX`.

## The walk, per outcome (aw-8 AC3)

| FWD | DONE WHEN | read | CVO grade |
|---|---|---|---|
| 31 | team passage beside the FILING roster; roster byte-unchanged; absent arm with a reason; positive control in the capture | BABA (20-F roster, 7 officers) and SAP (6): passage labelled "THE RESEARCH TEAM ON MANAGEMENT", cited to its pack, above the roster; with/without rows equal 7/7 and 6/6 (row-set hashes equal); BA the absent arm with its reason; route and tab labels in every capture | **REALIZED** |
| 18 (v0.40) | a seat clicks a filing-derived figure on a named company through to its passage | BA 3/3 and ASML 3/3 driver-chart clicks open "The filing passage for this point is not shown on this page", while the served points carry `passage_text` (c42) | **NOT REALIZED**: the page does not draw what is served (Z-W251-S1) |
| 1 (v0.40) | a seat opens a named covered company: model numbers, description and segment breakdown on screen | on all 12 segment names no tab draws the served `segment_breakdown`; the portal has 0 references to it | **NOT REALIZED**: page work (Z-W251-S2) |
| 5 (v0.38) | three prints read as documents in Opal Brand form | c48 clean (0 codes, 0 long decimals, 0 reprs, 0 clipped spans). This seat rendered SAP page 1: rounded figures with units and wrapped lines, but DejaVu Sans Mono with no brand styling, "Company description" twice, market cap twice, "[unit not stated]" | **NOT REALIZED**: readable now; the brand form is the remaining step |
| 7 (v0.39) | a seat opens the one place, sees every covered company with its date, finds a stale one | the page exists on a held candidate (not on DEV), draws its table about 12 s after load, and flags 95 of 95 stale (pack and web-search NEVER), so it singles out none; the sorts do not reorder | **NOT REALIZED** |

**On the grading seat's naming (v0.40).** FWD-1 and FWD-18 fail on every name the walk read, because the page draws neither served field on any name. So naming further companies would not change the grade this round. The naming applies once the page draws them.

## A served regression to name

`Z-W251-S4`: BP/_LN_Equity and NG/_LN_Equity answer 404 on `/thesis`. The slash-key repair (Z-S276, v77) served them 200 on 4 of 4 routes, so this reads as a regression for round 74.

## L10 PRECONDITION

Every order is terminal. No row of this round is ARMED; `comp-surprise --armed AMGT_RESAPP` reads 17, all pre-existing and live. **MET.**

```json
[
 {
  "id": "AMGT_RESAPP-Z-C-S463",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-06T05:35:00Z",
  "one_line": "Round 73 L9 on deployed satkY3HX (board 18 of 30): FWD-31 REALIZED (BABA and SAP: team passage above a FILING roster in a browser capture with route and tab-label control, roster rows byte-equal with and without it 7/7 and 6/6, BA absent arm with a reason); NOT REALIZED FWD-18 and FWD-1 (served but drawn by no page: the driver-chart passage and the segment breakdown), FWD-5 (clean and readable now, but DejaVu Sans Mono with no Opal brand styling, duplicated lines, '[unit not stated]'), FWD-7 (page on a held candidate, 12 s to draw, flags 95 of 95 stale so it singles out none).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "deliverables/0.9.0_WK_AMGT_RESAPP~251/WALK_ROUND73.md (73 lines), FWD-31 and FWD-7 sections",
    "lambda:Invoke /security/SAP_GY_Equity/print (pdf, 26 pages) rendered by this seat: fonts DejaVuSans-Bold + DejaVuSansMono; page 1 lists 'Company description' twice and 'Market cap' and 'Market capitalisation' both; 'Average daily value traded ... [unit not stated]'"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A compile record: the round's walk grades are recorded here; the page items (FWD-18, FWD-1) and the print brand go to the round-73 analysis.",
  "spec_asserts": "Each outcome is graded on its DONE WHEN.",
  "world_is": "One more realized; two need only the page to draw what is served.",
  "notes": "FOR THE CTO: FWD-18 and FWD-1 are page work (Z-W251-S1, S2: the passage_text and segment_breakdown are served); FWD-5 lay the print out in Opal Brand form (deck_generation/DESIGN_BIBLE.md fonts and colours) and drop the duplicate lines; FWD-7 the page must load fast and single out stale names on a measure that is not NEVER-for-all (Z-S356, Z-W251-S3); Z-W251-S4: BP/_LN and NG/_LN answer 404 on /thesis -- a served regression of the slash keys (compare Z-S276)."
 }
]
```

-- 3.0.0_SA_CVO~Z
