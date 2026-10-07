# ETFS_RIVALS -- ROUND 22 ANALYSIS (L10), with the deploy of rounds 15 to 22

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~18:1xZ.
**Slugs:** `3.0.0_SA_CVO~RV` msg 31145 (`ADJUDICATION_v23.Z.md` @8ee36f16f5) and msg 31250 (`ADJUDICATION_v24.Z.md` @665581ba62, the
served grades). The messages and the v24 summary lines were read; neither file was read line by line by this seat.
**Deploy:** `2.0.0_SA_COO~RV` msg 31244, record @dca1f916d9; CTO half
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_ETFS_RIVALS_R22_LAMBDA_DEPLOY_20261007.md` @19eb48bda5.

## 1. Where the product stands

Rounds 15 to 22 are LIVE at `beb13d39ff` since ~17:4xZ: the dialog charts, the trade markers, the 30 / 90 / 365-day tables.
- The apply: 0 add, 5 change, 0 destroy; 5 of 5 functions at 3,008 MB.
- One republish: 164.5 s, Max Memory Used 1,009 MB. The served page equals the prediction; 13 chart objects; 5,894 markers.
- Graded on the served page: pd-2 J1 MET; md-1 J1 MET on the served bytes; row Z-S55 holds; row C-S64 REMEDIATED (0 markers lost
  in 13 of 13 funds).

## 2. What is not yet shown

1. **The signed-in hop.** No seat has read the page or a chart through `mcp.opalinvest.dev/rivalfunds`. Ledger leg L3 is open
   and names Andrew's own look. md-1 J1's named oracle is that look, or a gateway access record of it.
2. **A full daily run on the new code.** The republish ran one stage. The 2026-10-08 11:00Z run and the 13:00Z sweep are the first
   full runs; their Max Memory Used and Duration are legs of the same ledger entry. Above 720 s is BLOCKING before the backfill.
3. **The enrichment change of round 20** in the working-tree vehicle (row Z-S62): first run 2026-10-08 11:00Z.
4. **Price history.** 98 of 690 chart frames read "No price history is stored for this holding yet". The backfill has not run.

## 3. Rulings

| # | subject | ruling | why |
|---|---|---|---|
| R1 | rows Z-S65 and Z-S66: 4 of 2,247 buttons open a dialog without their fund's section (META and ASML in GQGU's trade sentence) | One repair cell: the trade sentence links by the ONE key of round 22, as every other mention does. Its check is the publisher's own count reading 0 missing, and a build that would publish with the count above 0 is named in the cell's report. | The fault was served by this deploy with both halves stating it. The count read 3 and then 6 in earlier rounds and was not reported; the cell also says why the publisher's FAIL line did not reach a row. |
| R2 | row Z-S57: Meta in GQGU still under two keys | Carried to the same cell as R1 if it is the same cause; the issuer states whether it is. | One company under two keys is the cause R1 names. |
| R3 | 20 of 26 AI accounts name a month-to-date or year-to-date figure beside 30 / 90 / 365-day tables | They stand until the 2026-10-08 13:00Z sweep. After it, the same count is read again: 0 of 26 expected. If the sweep's accounts still name calendar periods, the prompt is the defect and it is one cell. | The accounts were written on the old tables. Whether the NEW accounts use the new windows is not known until the sweep. |
| R4 | the half's write set missed one object (`gold/input_census`) | Noted. The next half's write set is read from the code path, not from the prediction file. | One write-once object, no served effect. |
| R5 | the backfill | Unchanged order: read the DEPLOYED stage ignoring a backfill-marked row, then day 1 after that day's vehicle. Not before item 2 of section 2 reads under 720 s. | R1 of the round-20 analysis. |

## 4. ENRICHMENT LIST (round 23, one issuance by `2.0.0_SA_COO~RV`)

1. The trade-sentence key repair (R1, R2).
2. The read of the 2026-10-08 11:00Z run and 13:00Z sweep: memory, duration, row Z-S62, and R3's count.
3. The deployed-stage read for backfill-marked rows; then backfill day 1.
4. Close leg L3 on Andrew's look.

## 5. ACTS ONLY ANDREW CAN DO (cited)

- His own look at `mcp.opalinvest.dev/rivalfunds`: the sign-in is his (his login).

-- 1.0.0_SA_CTO~Z

## ADDENDUM 1, 2026-10-07 ~19:0xZ -- Andrew looked at the live page; the chart's UI joins round 23

Record, his words verbatim: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_190xZ_RIVALFUNDS_SMOKED_POPUPS_GOOD_CHART_UI_NEXT.md`.

- **Section 2 item 1 is met.** He opened the dialogs through the signed-in page and saw the charts. Ledger leg L3 closes on his
  report. He did not say he used the 30d / 90d / 365d switch, so that control has no reader yet.
- **Enrichment list item 5, round 23: the dialog chart's UI, three asks, his words.**
  1. The price and date read-out on hover is "much more focal, bold, and obvious".
  2. The tooltip on hover, most of all on a buy or sell marker, is "much more dramatic".
  3. "A box around the chart element itself with clear dates on x-ticks", with "a little more space".
- **How it is cut.** One cell, in `render.py` / `page_theme.py` only. "The mechanics are all there": no change to the price series,
  the markers, the windows or any gold table. The page stays under its 1,950,000-byte cap (served: 1,690,862).
- **How it is graded.** Mechanical: the x-axis carries dated ticks in every window; the chart sits in a bordered frame; the
  hover read-out's type size and weight are above the body text's, stated as numbers. JUDGMENT, by `3.0.0_SA_CVO~RV` on the
  served page and never by the issuer: hovering a buy or sell marker shows what was traded, when and for how much without
  reading small text. Then Andrew's own look, which is the acceptance.
- **Order in round 23:** this cell and the trade-sentence key repair (R1) are the two page cells; both ship in one deploy
  after the 2026-10-08 11:00Z run has read under 720 s. (REPLACED at 19:0xZ by msg 31267: the repair deploys today as its own
  act; a render-only deploy does not wait for the 11:00Z run. The chart cell is round 24.)

-- 1.0.0_SA_CTO~Z

## ADDENDUM 2 -- ROUND 23 ANALYSIS (2026-10-07 ~19:4xZ), on `3.0.0_SA_CVO~RV` slug msg 31320 (`ADJUDICATION_v25.Z.md` @61f0469fd2)

Round 23 was one cell, RIV-ks-1, the trade-sentence key repair (R1). ks-1 J1 MET on the round's real run: 0 of 2,247 buttons
without their fund's section; exactly 4 buttons differ from the served page. Row Z-S63 REMEDIATED (5 of 5 functions at 3,008 MB).
Rows Z-S65 and Z-S66 stay OPEN until the repair is served. Its deploy is signed at both ends (CTO half
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_ETFS_RIVALS_R23_KS1_DEPLOY_20261007.md` @e1c74f75b3) and had not been reported
done at this writing.

**Rulings.**
- **R6.** Row Z-S57 (Meta in GQGU under two keys) is not the cause R1 repaired, by the issuer's trace. It is its own cell in
  round 24: one company, one key on the page.
- **R7.** The price-history backfill records each day's draw in `bbg_budget` before its day 1 (msg 31291). The Terminal's ledger
  does not see it today, and the pacer `0.0.3_BG_BBGTerminal` orders it third of four claims on the day's allowance.

**ENRICHMENT LIST, round 24** (one issuance by `2.0.0_SA_COO~RV`):
1. The dialog chart's UI, Andrew's three asks (ADDENDUM 1). JUDGMENT graded by `3.0.0_SA_CVO~RV`; then his own look.
2. Row Z-S57 (R6).
3. The served grade of the repair, with the count of mentions that became plain text (the CTO half's condition).
4. The read of the 2026-10-08 11:00Z run and 13:00Z sweep (round-22 list item 2), unchanged.
5. The backfill's ledger line (R7); then the deployed-stage read; then backfill day 1.

-- 1.0.0_SA_CTO~Z

## ADDENDUM 3 -- ROUND 24 ANALYSIS (2026-10-07 ~21:5xZ), on `3.0.0_SA_CVO~RV` slugs 31412 and 31430 (`ADJUDICATION_v28.Z.md`, `v29.Z.md`)

**Withdrawn since ADDENDUM 2:** R6 (row Z-S57 needed no cell: the afternoon's deploy had removed the fault; the CVO closed the
row, msg 31349) and R7 (the backfill does record in `bbg_budget`; it had no line because it has never run, msg 31325).

**Round 24** was one cell, RIV-cu-1, the dialog chart's UI on Andrew's three asks. cu-1 J1 MET before the deploy and again on the
served page of 21:26Z. Live at `f9f8334ef6`; CTO half `deliverables/CTO_HALF_ETFS_RIVALS_R24_CHART_UI_DEPLOY_20261007.md`
@db4ab8faec. 32 keys written, all under the page day and its state record; one script, one fetch.

**Rulings.**
- **R8.** The two faults the CVO noted (the read-out keeps the last curve position while a marker is pointed at; a top marker's
  tooltip covers the read-out) are one cell, `render.py` only.
- **R9, row Z-S69 with its correction Z-S70 (BLOCKING, ARMED).** Every reader of `security_market` keeps ONE object per date. On
  2026-09-29 the object kept is an import with no price and the live pull is ignored: 430 closes unused, 355 chart entries
  drawing that day from the fund's own valuation. The readers' grain is repaired NOW, ahead of FWD-24's other cells. Its rule:
  per security and date, non-backfill first, live over import, later capture time, later as-of, name last; and a close, its
  currency, its date and its source come from ONE object (msg 21:46Z). Its deploy carries a never-widen pair with a before and
  after of the rankings and the three period tables for every fund.
- **R10, PRD v0.19 (`FWD-24`, ADMITTED @2914a61989).** No year of closes is written by any route before R9's repair is deployed and
  graded, the one-time backfill included. The standing Bloomberg request stays switched off until Andrew's recorded answer.

**ENRICHMENT LIST.** Round 25, one issuance, both cells today: R9's readers' grain; R8's read-out repair. Round 26: FWD-24's
history-owed step and top-up writer, the request off. Beside both: the reads of the 2026-10-08 11:00Z run and 13:00Z sweep.

**ACT ONLY ANDREW CAN DO (cited):** his answer on a standing daily Bloomberg request of closes for the rivalfunds securities
(CLAUDE.md: no vendor call without his explicit per-use word; PRD ADDENDUM G.2).

-- 1.0.0_SA_CTO~Z
