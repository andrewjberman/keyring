# AMGT_RESAPP -- the 39-outcome board (latest grade per FWD)

Compiled 2026-10-05 from the repo at CLOUD HEAD `930a3d2220`. Read-only. All paths are relative to
`org/missions/D5/AMGT/AMGT_RESAPP/`.

## Denominator

- **PRD:** `prd/AMGT_RESAPP_PRD.md` @`2de1ef2251`, `prd_version` v0.37, status RATIFIED.
- **The header's `endpoint_outcomes` list has 39 entries, FWD-1..FWD-39, with no gaps.** The ENDPOINT fence defines all 39.
- **RETIRED:** 0. The PRD retires no FWD.
- **RE-HOMED:** 9. FWD-21..FWD-29 moved to DSGN_AMGTV1 FWD-12..FWD-20 under Addendum C (v0.29, section C.1). C.1 says
  "this project's completion test reads FWD-21..FWD-29 as RE-HOMED, which is neither REALIZED nor dropped".
- **Qualified waits written in the fence:** FWD-35 (the terminal sign-in), FWD-36 (price 90/365, v0.35) and FWD-37 (earnings
  dates, v0.34).

## Sources searched

| set | files | grade-bearing hits |
|---|---|---|
| `ledger/` (every file: 68 ROUND_ANALYSIS files, rounds 1-69 with no round 34, plus packets, L9 files, never-widen halves and rulings) | 213 | 44 files carry REALIZED/REALISED |
| `surprise-channel/adjudications/ADJUDICATION_v1..v84.md` | 84 | 14 files carry REALIZED |
| `deliverables/**/COMPLETION_GRADES*.json` (glob over 2,245 tracked and 142 untracked files) | 0 | none exist |
| **Total searched for FWD-n mentions** | **297** | 880 output lines over 39 FWD ids (scanner: `scratchpad/fwd_scan.py`) |

- **Supporting reads:**
  - the round-51 re-grade evidence `deliverables/0.9.0_WK_AMGT_RESAPP~182/FWD_EVIDENCE_ROUND51.json` (zz-7);
  - the CTO audit `org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_ENDPOINT_COVERAGE_AUDIT_AMGT_RESAPP_20260925T0355Z.md`. The
    round-43 analysis cites it as the standing grade for FWD-1..20.
- **Order of sources:** round number for the analyses, version number for the adjudications, and the same day's commit time
  where the two meet.
- **Hand-filtered token trap:** RESAPP's ledger cites DSGN, CORPUS and HARVST outcomes as bare "FWD-n". Examples: round 63's
  "DSGN FWD-2, FWD-7 and FWD-24 are REALIZED", round 69's "DSGN's FWD-4, FWD-5, FWD-7 and FWD-8", round 67's "FWD-17's explicit
  zero row" (HARVST) and round 46's "FWD-12 limb 3" (CORPUS, per ADJUDICATION_v56). Every hit after round 51 on FWD-1..FWD-31 was
  read by hand. None of them is a RESAPP grade.

## The board

| FWD | title (one line) | latest grade | source (vintage) | evidence |
|---|---|---|---|---|
| FWD-1 | First-draft pack for a covered name, no spreadsheet or terminal | NOT_REALIZED | ROUND_ANALYSIS.round51 s.3 (zz-7, CVO-corrected v61) | unmeasurable: a human act; enabling state served on 96 of 96 |
| FWD-2 | Same pack for a never-covered name, by typing its ticker | NOT_REALIZED | round51 s.3 (zz-7) | unmet: an uncovered form resolves UNRESOLVED; nothing is pulled |
| FWD-3 | Analyst can defend every number on the page | NOT_REALIZED | round51 s.3 (zz-7); earlier round36 / ADJUDICATION_v44 "unblocked in mechanism, NOT REALIZED" | unmeasurable: a human act; 33,828 figures carry basis, vintage and source |
| FWD-4 | Recent commentary read without leaving the page | NOT_REALIZED | round51 s.3 (zz-7) | unmeasurable; 2 feed items across 96 names in the 30-day window |
| FWD-5 | Adam forwards a printed pack unchanged | NOT_REALIZED | round51 s.3 (zz-7) | unmeasurable; the PDF is 13 pages and no forward is recorded |
| FWD-6 | Returning analyst can say what changed | NOT_REALIZED | round51 ruling 1 (CVO v61 corrected met to unmet) | the compare is served, but the portal has no versions/compare surface (routed to DSGN) |
| FWD-7 | Adam sees which covered names have gone stale | NOT_REALIZED | round51 s.3 (zz-7) | unmet: /freshness holds 53 of 96 live-library keys |
| FWD-8 | The comparison block is about the company on the page | NOT_REALIZED | round51 s.3 (zz-7) | unmeasurable: "an analyst who distrusted it has stopped" is a person's act |
| FWD-9 | Machine prose is never mistaken for a firm view | REALIZED | round54 s.3 ("REALIZED, standing"); first listed at round51 | 210 of 210 drafted sentences carry the machine marker (zz-7 met) |
| FWD-10 | A figure that failed its check is visible as failed | REALIZED (flagged) | round51 ruling 2 ("It stays met"); audit cited by round43 ("1 REALIZED" = FWD-10) | check_face REFUSE 15,947 rendered; **omitted from the round51-54 REALIZED lists** (see disagreements) |
| FWD-11 | Social discussion admitted by a written rule | NOT_REALIZED | round51 s.3 (zz-7) | unmet: 0 social items on 96 of 96 names |
| FWD-12 | Each input's source shown, and any one re-run alone | NOT_REALIZED | round51 s.3 + ruling 1 (zz-7) | unmet: the ledger has no page surface; classes_with_a_stage 0 |
| FWD-13 | Everything on one page is about the same company | REALIZED | round54 s.3 ("REALIZED, standing") | identity agrees across 6 routes on 96 of 96 (0 disagreements) |
| FWD-14 | The lists the page depends on do not rot silently | NOT_REALIZED | round51 s.3 (zz-7) | unmet: list owners UNASSIGNED (C-NO-CONTACT, Andrew names the owner) |
| FWD-15 | PM sees a ranked list of names worth looking at, and clicks through | NOT_REALIZED | round51 s.3 (zz-7) | unmeasurable: a PM's act is not recorded |
| FWD-16 | The page top says what the company is and today's items | NOT_REALIZED | round51 s.3 (zz-7) | unmeasurable; the description renders 96 of 96, the social line has no source |
| FWD-17 | Who runs the company, and their tenure | NOT_REALIZED | round51 s.3 (zz-7); round37-39 "HELD on rk-49" | unmeasurable; roster served on 9 of 96 |
| FWD-18 | Filings read for the analyst; the one driver chart | NOT_REALIZED | round55 s.1 (ae-2 read, no grade written); round51 zz-7 unmeasurable | ASML chart served from its filing with 3 points; **the promised REALIZED grade was never written** |
| FWD-19 | What this company means for Opal (Posture) | NOT_REALIZED | round51 s.3 (zz-7) | unmeasurable; posture served on 33 of 96 |
| FWD-20 | House forward view and its Divergence from the street | NOT_REALIZED | round51 s.3 (zz-7) | unmet: divergence ABSENT on 96 of 96; the house forecast is not built |
| FWD-21 | Thesis on one screen under one dark band | RE-HOMED | PRD v0.29 s.C.1; round52-54 s.3 | moved to DSGN FWD-12; was REALIZED at round37-39 |
| FWD-22 | Headline figures as labelled tiles | RE-HOMED | PRD C.1; round52 s.3 | moved to DSGN FWD-13; zz-7 unmet (0 Stat tiles after the DSGN redesign) |
| FWD-23 | Each drafted sentence keeps its evidence, folded | RE-HOMED | PRD C.1; round52 s.3 | moved to DSGN FWD-14; zz-7 unmet |
| FWD-24 | Model sheet as a table; a refusal as one line | RE-HOMED | PRD C.1; round52 s.3 | moved to DSGN FWD-15; round52-54 still list it "REALIZED (pre-re-home)" |
| FWD-25 | Comparable set shows present columns; absent ones openable | RE-HOMED | PRD C.1; round52 s.3 | moved to DSGN FWD-16; listed "REALIZED (pre-re-home)" |
| FWD-26 | Posture verdict as a headline, reasons as cards | RE-HOMED | PRD C.1; round52 s.3 | moved to DSGN FWD-17; listed "REALIZED (pre-re-home)" |
| FWD-27 | Lead Panel controls read as the Dashboard's | RE-HOMED | PRD v0.30 C.1 placement line (round52 ruling 1, after CVO v62 PARTIAL) | moved to DSGN FWD-18 ("no DSGN owner before v0.4") |
| FWD-28 | Every panel renders one of four designed empty states | RE-HOMED | PRD C.1; round52 s.3 | moved to DSGN FWD-19; was REALIZED at round37-39 |
| FWD-29 | The render check passes and can fail | RE-HOMED | PRD C.1; round52 s.3 | moved to DSGN FWD-20 (map: none); was REALIZED at round39 |
| FWD-30 | Export gives a usable artifact, field-equal to the page | NOT_REALIZED | round54 ruling 3 + s.3 | the value clause is REALIZED (96 of 96, 32,468 values, 0 differing); held on Adam's forward (round51 ruling 3) |
| FWD-31 | The team's MANAGEMENT passage beside the filing roster | NOT_REALIZED | round51 s.3 (zz-7) | unmet: the passage is served on 47 of 96 and the tab does not render it beside the roster |
| FWD-32 | Monthly chatter per covered name, no name withheld | REALIZED* | round60 s.1 ("Friday feed COMPLETE on the served plane"); ADJUDICATION_v69 + v72 | deployed: 95 rows, 0 zero cells, BA September = 20 |
| FWD-33 | A name's latest price and chatter every day; breakout reads breakout | REALIZED* | round60 s.1; round57 s.1; v68/v69 | T-1 fallback serves 2026-09-29 with `stale_trading_days` 1 |
| FWD-34 | Every movement figure is served in percent | REALIZED* | round60 s.1; round57 s.1; v69 | ASML breakout 9.21396 %, a different row from trending 10.2907 % |
| FWD-35 | Price ranking covers every covered name with a signed 30-day return | REALIZED | ADJUDICATION_v70 (round 58; CVO "True ... FWD-35"); round58 s.1; round60 s.1 | scheduled 07:00 ET generation: 94 rows + 1 excluded = 95, stale 0 (Branch A) |
| FWD-36 | Lead-panel routes answer 30/90/365-day windows, with tone | REALIZED | ROUND_ANALYSIS.round68 s.2 (CVO ADJUDICATION_v82) | tone from `chatter_window` on 95 of 95, 0 "holds no row"; price 90/365 real since round66 |
| FWD-37 | Timeline markers: coverage events and earnings releases | NEVER_GRADED | none at outcome level; the interim check c11 is in ADJUDICATION_v77 (round 64) | BA: 1 coverage_event; earnings_release absent "no earnings dates are pulled yet" (qualified wait) |
| FWD-38 | The served data on one page agrees with itself | NOT_REALIZED | limb grades only: (b) round65 s.1 REALIZED; (d) round67 s.2 PASS; (a)/(c) via c12/c13 at round64 (v77) | no whole-outcome grade; round68 adds only FWD-36 and FWD-39 to REALIZED |
| FWD-39 | Timeline serves a word cloud from the name's own coverage | REALIZED | ROUND_ANALYSIS.round68 s.2 (CVO ADJUDICATION_v82) | 6 own-name leaks read 0; census over the 199 cloud-serving names |

REALIZED* = the grade line reads "COMPLETE on the served plane" (round 60, CTO, on the CVO's reads across rounds 57-60). The
REALIZED token is never written for these three. Their claim is weaker than the token.

## Totals (denominator 39)

| grade | count | FWD |
|---|---|---|
| REALIZED (token written) | 6 | 9, 10 (flagged), 13, 35, 36, 39 |
| REALIZED* (completion language only) | 3 | 32, 33, 34 |
| RE-HOMED | 9 | 21-29 |
| NOT_REALIZED | 20 | 1-8, 11, 12, 14-20, 30, 31, 38 |
| NEVER_GRADED | 1 | 37 |
| RETIRED | 0 | -- |
| **sum** | **39** | |

- **Strict reading (the CTO's own lists, REALIZED token only, FWD-10 excluded): 5 REALIZED** (FWD-9, 13, 35, 36, 39).
- **Broad reading:** 9 REALIZED of 30 gradeable outcomes, since 39 less the 9 RE-HOMED leaves 30.
- **NOT_REALIZED splits as follows:**
  - unmet: 8 (FWD-2, 6, 7, 11, 12, 14, 20, 31);
  - unmeasurable human act with the precondition present: 10 (FWD-1, 3, 4, 5, 8, 15, 16, 17, 18, 19);
  - a person's act outstanding on a met served clause: 1 (FWD-30);
  - graded only by limb: 1 (FWD-38).
- **Vintage:** 19 of the 20 NOT_REALIZED grades date from round 51 (zz-7, 2026-09-30). Only FWD-38 is newer (round 67). No full
  pass over FWD-1..FWD-31 has run since round 51.

## Disagreements and gaps (same vintage, or a promised grade never written)

1. **FWD-10, round 51, same file.** Ruling 2 says "It stays met" and needs no person's act. The audit cited at round 43 graded it
   REALIZED. But the REALIZED lists at rounds 51, 52, 53 and 54 read "FWD-9, 13, 24, 25, 26" and omit it.
2. **FWD-24/25/26, rounds 52-54, same section.** These sections list them as "REALIZED ... hold (as of their pre-re-home grades)"
   beside "FWD-21..29 are RE-HOMED". PRD C.1 says the completion test reads RE-HOMED, which is neither REALIZED nor dropped.
3. **FWD-9 and FWD-13: the "hold as before" has no prior grade.**
   - The audit cited at round 43 graded both NOT_REALIZED.
   - Round 51 lists them as REALIZED "as before". No RESAPP analysis or adjudication between rounds 43 and 51 grades them REALIZED.
   - The only intervening record is uu-1/zz-7 "met", and those files say the state is "not a grade of the outcome".
4. **FWD-18.**
   - Rounds 52-53 say it "is graded REALIZED at the next FWD sweep, once read on the page".
   - Round 54 says the sweep "grades FWD-18 REALIZED or not".
   - Round 55 records the read (ae-2, 3 points) but writes no grade. ADJUDICATION_v67 holds no FWD-18 grade.
5. **FWD-30.**
   - The PRD's ENDPOINT says to grade the DONE WHEN and never the ACCEPT. The DONE WHEN's value clause is REALIZED (round 54),
     but the whole is held on Adam's forward, which is ACCEPT text (round 51 ruling 3).
   - Round 51 calls the forward "a person's act, not Andrew's". Round 54 calls it "Andrew's side".
6. **FWD-36.**
   - Round 66 says its price limb "is graded on" the daily job's post-run read after 2026-10-04 11:00Z.
   - Round 68 grades REALIZED on the tone limb and cites no such read. The PRD's FWD-36 fence still carries the v0.35 QUALIFIED
     WAIT text, although Andrew's word lifted it (round 65 addendum 2).
7. **FWD-32/33/34.** These carry completion language only, with no REALIZED token. Round 68 says "the remaining outcomes stand as
   the round-66 board carried them", but round 66 holds no board.
8. **FWD-38.** All four limbs read PASS or YES between rounds 64 and 67, but no seat graded the outcome whole, and round 68 does
   not add it to REALIZED.
9. **FWD-37.** It is never graded as an outcome. Its interim branch passed check c11 at round 64. Its earnings path waits on the
   CORPUS Model-block pull.

Round 69's analysis (@`0bdf5b47ae`) promises this board as its section 6. That section is not yet in the file.
