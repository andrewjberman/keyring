# L4-R REVIEW -- AMGT_RESAPP PRD, BRIEF half: v0.11 corrected in review; v0.13 SIGNED

**Reviewer:** `4.0.0_SA_CRO~Z`. **Deliveries:** v0.11 by `1.0.0_SA_CTO~Z` msg 23736 (19:36Z, half `14e406e0d673` @`9c8e04cd9a`);
v0.12 by msg 23746 (19:54Z, half `30d687e41b92` @`4de34f0d95`); v0.13 by msg 23757 (20:18Z, half `c0d38674e972`
@`1699960261`, confirmed with `prd_signoff_lib.half_hashes`). **Brief of record:**
`docs/briefs/amgt-resapp-security-analysis-20260910.md` @`19ce7d5b4d`.

## Outcome

- **v0.11:** two corrections returned (R1, R2 below) by message ahead of any stamp (msg 23744). v0.11 was never stamped:
  the CTO applied both and bumped to v0.12 within 20 minutes, together with Andrew's six card answers.
- **v0.12:** R1 and R2 verified CORRECTED at the pinned lines; the card-driven changes verified faithful to Andrew's words
  as recorded. Not stamped: v0.13 superseded it before the mechanical check reported.
- **v0.13: SIGNED.** Its brief-half changes (Andrew's SA terms clearance; the evidence moved out of the ratified text into
  s.10's closing list) are faithful. The mechanical check's findings are all PRE-EXISTING or non-contradictions and go to
  the CTO as corrections for the next bump, by pinned line (last section) -- none is new in this round's amendments.

PRD line numbers in R1, R2 and the faithful table are at `9c8e04cd9a` (v0.11).

---

## R1 (blocking) -- `C-DESCRIPTION-LINE`, PRD:1163-1170: the source order serves a revenue figure as the business description on 12 of 12 names

**The text:** *"(1) the first sentence of a VALIDATED drafted `company_description` section ... (2) else Bloomberg's
description field -- `CIE_DES`, else `CIE_DES_BULK` ... This REVERSES today's reader order ... so adding the field does
not replace a drafted description on the 12 names that have one."*

**Measured today** with the adapter's own `read_description` over the 12 names that have a drafted document
(`scoped_amgt.py:2538`, which serves `sections[company_description].sentences[0]`). **12 of 12 serve a sentence that is
not a description of the business:**

| name | what the description line serves today |
|---|---|
| Boeing | "Commercial Airplanes revenue was $41,494 million in 2025, versus $22,861 million in 2024 ..." |
| ASML | "Authorized share capital: total EUR126.0 million, split into 700,000,000 cumulative preference shares ..." |
| Petrobras | "Under the concession regime, royalties are established in the concession contracts at a rate of 10% ..." |
| Home Depot | "Consolidated net sales were $164.7 billion in fiscal 2025." |
| Valero | "Refining segment operating income was $4,040 million in 2025 versus $3,971 million in 2024 ..." |

The other seven (Alibaba, Costco, Halliburton, Intuit, Kimberly-Clark, Nu, SAP) are the same kind: a segment
revenue, geography share or legal-structure fact. The validation found the same on Caterpillar
(`INSTANTIATION_VALIDATION_REPORT_20260918.md` D23). **"VALIDATED" in the clause means the drafting document passed its
schema, not that the sentence describes the company**, so ranking the drafted sentence first makes today's defect the
contract.

**Correction:** (1) Bloomberg's `CIE_DES`, else `CIE_DES_BULK`, labelled as Bloomberg's; (2) else a drafted
`company_description` sentence ONLY if it passes a stated test that it describes what the company does (not a figure, a
share count or a legal term), marked machine with its evidence; (3) else ABSENT naming every probe. Until the pull adds
`CIE_DES`, the line reads ABSENT on names whose drafted sentence fails the test -- honest where today it is wrong. The
test's wording is the cut's to state; the ORDER is what this correction returns.

---

## R2 (blocking) -- `C-VERBATIM-GATE`, PRD:901-903: the figure on Andrew's card is from the wrong population

**The text:** *"Whether such a sentence is instead HELD is Andrew's decision (it would withhold roughly 40% of today's
drafted prose ...)"*.

**Measured today** over the 12 served drafted documents (the same adapter reads, `quoted_spans` per sentence): **179 of
389 served sentences carry NO quoted span (46%); 210 carry one.** The "roughly 40%" is the validation names' figure (17
of 39 for CAT, 16 of 40 for CSL), not today's drafted prose. This sentence is the decision input on a card going to
Andrew, so it carries the served figure with its denominator.

**Correction:** "it would withhold 179 of today's 389 served drafted sentences (46%; measured 2026-09-18 over the 12
served documents)".

---

## Checked and faithful -- no correction

| clause | PRD lines | checked against | finding |
|---|---|---|---|
| `C-UNIT-MAP-MEASURED` v0.11 | 843-848 | Model brief s.1.1, s.5 item 1 | faithful; "a field whose unit is not measured stays REFUSED" is the right guard |
| `C-MODEL-FORECASTS` | 850-860 | Andrew ~18:4xZ verbatim; Model brief s.2 | faithful. Deferring the SA fallback to `C-SA-VENDOR-WORD` applies pre-existing ratified text and the vendor-egress law; it is not a new gate |
| `C-MODEL-WINDOW-AND-ROWS` | 862-873 | Model brief s.1.2-1.3, s.3, s.4 | faithful; the cases stay ABSENT pending Andrew, as the brief put it |
| `C-VERBATIM-GATE` (rest) | 895-900, 903-907 | validation report s.4, D18-D19 | faithful; the character-based rule and the two discriminating controls are right |
| `C-SERVER-SIDE-RANKING` v0.11 | 1133-1143 | Lead Panel brief F2, F3, item 8 | faithful |
| `C-PRICE-BREAKOUT-FLOOR` | 1149-1156 | Andrew's card B at this seat's recommendation (Lead Panel 8.2) | faithful, and it CORRECTS this seat's Lead Panel brief 8.2, which put the rule in `MIN_ABSOLUTE_JUMP`; the unsmoothed separate test is right |
| `C-PRICE-DAILY-LEG` | 1158-1161 | card A; Lead Panel 10.1 | faithful |
| s.10, the instantiation stages | 1587-1637 | Thesis brief s.8.5; the validation report s.2 and s.7 | faithful; `C-PRODUCTION-HOME`'s "a dry run writes nothing, anywhere" answers D24 and D26 |

---

## v0.12 -- the corrections and the card changes, verified (`git diff 9c8e04cd9a 4de34f0d95`, PRD only)

| change | v0.12 text | verdict |
|---|---|---|
| R1 `C-DESCRIPTION-LINE` | Bloomberg `CIE_DES` / `CIE_DES_BULK` FIRST; a drafted `company_description` sentence second, ONLY past a stated describes-the-business test (wording the cut's); else ABSENT naming every probe; this seat's 0-of-12 measurement cited | CORRECTED as returned |
| R2 `C-VERBATIM-GATE` | "179 of 389 sentences (46%, measured 2026-09-18 ...)" over the served documents, the validation names' 17/39 and 16/40 beside it | CORRECTED as returned |
| card 4 (HOLD) | a sentence with no verbatim span is HELD, never served, counted in the split | faithful: REC was HOLD, his word *"Agreed, yes."* |
| card 5 (Base) | Base = consensus EPS x the security's own trailing-median P/E, each input sourced; Upside/Downside ABSENT, "methodology to be discussed with Andrew" | faithful: the card's REC formula, his word *"Base. I think the upside and downside cases can be discussed on methodology."*; no seat picks a spread |
| card 1 (SA) | the `SA_FALLBACK` cells of `C-MODEL-FORECASTS` authorized by name; a SCHEDULED refresh still waits on `C-SA-TERMS-BEFORE-SCHEDULE` | faithful: *"Yes use SA thats fine"*, with the card's own (b) keeping the terms read first |
| card 2 (Lusha) | no credit ceiling INSIDE the validation, read as scoped to it | faithful and read narrow, as the record states |
| `C-VALIDATION-NAMES` | Lusha and SA authorized inside the validation | faithful to cards 1-2 |

Card mapping checked against `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md`
@`4de34f0d95`, which quotes his words and each card's REC.

---

## The mechanical check -- BRIEF COVERAGE against the brief at its pin

Read by a subagent of this seat at `9c8e04cd9a` against the brief at `19ce7d5b4d`, with the half hash confirmed through
`prd_signoff_lib` as the positive control (`14e406e0d673`). No v0.12 or v0.13 hunk touches the sections it graded (s.2,
s.3's older clauses, s.4-s.6, 9a-2), so the reading carries to v0.13; line numbers below are at `9c8e04cd9a`.

**v0.13 changes to this half, verified:** `C-MODEL-FORECASTS` and the `C-SA-VENDOR-WORD` table record Andrew's ~20:0xZ
*"I have already clarified SA ToS, we are good ..."* as satisfying `C-SA-TERMS-BEFORE-SCHEDULE` for exactly the two SA
paths lifted at v0.12 -- faithful and no wider. The evidence list appended to s.10 carries the moved measurements verbatim.

### Findings -- all non-blocking for this signature, returned as corrections for the next bump

1. **There is no BRIEF COVERAGE section.** 21 brief headings (title, PART I-VII, O1-O12, III-B) against 0 entries in the
   PRD, searched case-insensitive over this and the 12 prior versions; the search's positive control finds the section in
   63 other files. **This is the state this PRD was signed in at v0.7:** the v0.6 L4-R's coverage-map ground was answered
   with 9a-2 (a map of Andrew-directs and CRO connection briefs), and `4.0.0_SA_CRO~W` signed it. O1-O12 are carried in
   the ENDPOINT's SOURCE lines (the ratified-text half), so the brief's outcomes do reach the cells. 12 of 21 headings are
   never cited in the brief half (PART I, III, IV, VI, VII; O1-O5, O8), and F8-F10 are cited nowhere. **Correction for the
   next bump:** a BRIEF COVERAGE section, one entry per brief heading, carrying content.
2. **Content dropped where a clause cites the brief:** the six mnemonics behind `C-UNIT-MAP-MEASURED` (`brief:190-193`);
   `C-BLOOMBERG-BASIS`'s `EBITDA_ADJUSTED` ~1% vs EBITDA 7-10% and 32 of 35 on SAP (`brief:184-186`); O7's "gap between
   covered and current" (`brief:46-47`, PRD:1250); O9's five limbs (`brief:55`, PRD:1252); the six classes' questions
   (`brief:144-149`); s.5 carries 4 of PART V's 11 bullets with `127.0.0.1:8194` and the 2-attempt budget flattened
   (PRD:1274-1318); PART VII's scanner-liveness and CapIQ bullets (`brief:307-310`) are carried nowhere.
3. **"48 of 54 packs" (PRD:945; at v0.13 also :958 and :1272) overstates the brief,** which says "54 one-pagers"
   (`brief:200`) and "Whether the stale peer set (F6) reaches the PRINTED packs is UNVERIFIED ... Nobody should conclude
   packs shipped wrong" (`brief:300-302`). The PRD's own s.6 (PRD:1328-1330) agrees with the brief. Pre-existing.
4. **Stale internal lines:** s.5 PRD:1318 "Nobody has decided" (paywalled sources) against PRD:1049-1052 "Somebody now has,
   in part"; PRD:882-883 and :1326 "measured on ONE security" against the three pilots at PRD:843. Pre-existing.
5. **Metadata:** PRD:1340 "330 lines" (the brief is 337); PRD:236 v1 "15,429 bytes" (`git cat-file -s` 15,440); PRD:237 and
   241-242 call `19ce7d5b4d` "working-tree only", but it is an ancestor of both HEAD and origin; PRD:818's "verbatim" quote
   changes the case of `brief:103`.
6. **Considered and NOT a contradiction:** PRD:929 / :1324 (v0.13 :942 / :1345) say no QUALIFICATION threshold is set; the
   v0.11 price floor (+5%) and minimum-signal counts are Andrew-ruled RANKING rules in s.3b, a different domain. A
   one-line cross-reference would stop a reader conflating them.
7. **For the other half, on the record:** the ENDPOINT's "III-B bar 1..6" citations (PRD:264, 281, 297, 304, 319, 328) point
   at PART III's six bars (`brief:118-129`); III-B has six classes and no bars.

## Verdict: SIGN v0.13's brief half (`c0d38674e972`)

The round's amendments to this half are faithful to Andrew's words and to the panel briefs; this seat's two corrections
landed as returned; and nothing the mechanical check found was introduced by v0.11-v0.13. Holding round 14 for
pre-existing documentation gaps the half was already signed with would cost the round without changing a cell.
