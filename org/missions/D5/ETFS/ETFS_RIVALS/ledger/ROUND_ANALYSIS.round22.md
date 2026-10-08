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

## ADDENDUM 4 -- ROUND 25 ANALYSIS (2026-10-07 ~23:5xZ), on `3.0.0_SA_CVO~RV` slug msg 31476 (`ADJUDICATION_v30.Z.md` @e3cc04e7bb)

**rg-1 J1 NOT MET. Nothing was applied. mr-1 J1 MET (210 of 210 hovers).**

**R9 of ADDENDUM 3 read the fault BACKWARDS, and so did rows Z-S69 and Z-S70.** They said 430 good closes of 2026-09-29 were
being dropped. The CVO's hand read of one figure (C1 of the CTO half) found the object filed under 2026-09-29 holds 09-30's
closes: 47 of 57 dollar closes equal the funds' 09-30 valuations; MediaTek in CGIC reads +1.22 percent where the fund's own
09-29 return is -7.36. The readers ignoring that object was protecting the page. The repair as built would have put next-day
closes on 2,418 table rows and 408 chart points, and every count in its pair was consistent with itself.

**The read of every object** (`2.0.0_SA_COO~RV` msg 31479, row Z-S71 @bff3ec2e7f): ONE object is mis-dated, not all. 2026-10-01
matches its own date 31 of 31; 10-02, 10-05 and 10-06 match their own dates on most closes. The `as_of` column is the PULL day,
not the close's day.

**Rulings.**
- **R11.** This seat's term "a close is kept only where its as_of equals its partition date" (msg 31477) is WITHDRAWN: it would
  have kept the wrong object and dropped three right ones (msg 31480).
- **R12.** An object whose name carries no capture time is read as today, one object by the newest revision; the union applies
  to timed objects. No served figure moves. The 2026-09-29 live-pull object is NAMED as mis-dated in the reader's test and in
  row Z-S71.
- **R13, binding FWD-24.** Every object a writer adds carries, per close, the trading date the close belongs to, and the reader
  keeps a close only where that date equals the partition date. No year of closes is written without it. PRD `C-OWED-GRAIN` is
  amended to say so at this seat's next PRD act.
- **R14.** A never-widen pair that moves served FIGURES carries one figure read by hand against a source the producer did not
  write. Counts that agree with each other are not that read. Cost: one figure per pair. Non-application: a pair that moves no
  number a reader sees.

**ENRICHMENT LIST.** Round 25, re-cut: the readers' grain under R12; mr-1 may ship alone, render-only, under its own pair. Round
26: FWD-24's owed step and writer under R13, the request off.

-- 1.0.0_SA_CTO~Z

## ADDENDUM 5 -- ROUNDS 25 TO 27 (2026-10-08 ~06:0xZ), on `3.0.0_SA_CVO~RV` slugs 31525, 31548 and 31592 (`ADJUDICATION_v33`, `v34`, `v35.Z.md`)

**What is live.** mr-1 (the marker read-out) since 00:10Z, J1 MET on the served page. rg-2 (the readers' grain, narrowed) since
01:41Z at CLOUD `0576fb051f`: 0 moved rows, the page byte-identical, J1 MET on the served plane. The deployed code is a commit of
CLOUD again. CTO halves: `CTO_HALF_ETFS_RIVALS_R25_MR1_ONLY_DEPLOY_20261007.md` @86a90330bc,
`CTO_HALF_ETFS_RIVALS_R26_RG2_READERS_DEPLOY_20261008.md` @e081a672d4.

**Round 27** (the request OFF): ho-1 J1 MET -- the history-owed step reads **742 securities and 184,600 units owed over 251
dates**, reconciled by the CVO's own run to the closes held on four dates, three units by hand. rk-1 J1 MET: 0 moved rows.
tw-1 (the top-up writer behind a switch) is built and NOT merged; its J1 cannot be measured until it is. Its merge is signed at
both ends (`CTO_HALF_ETFS_RIVALS_R27_TW1_MERGE_20261008.md` @d969c62f46) and waits on the 2026-10-08 11:00Z run being read.

**Rulings.**
- **R15.** The merge of a file the scheduled vehicle runs is a deploy on this box and carries a pair, even with its switch off.
- **R16.** The switch `RIVALFUNDS_HISTORY_OWED` is set nowhere on this box (process, User, Machine, the scheduled task's
  definition: this seat's read). `ask` waits on Andrew's recorded answer. `print` is ruled by this seat on an ask naming where the
  variable would be set.
- **R17, before `ask` is ever set:** the writer stores each close's currency and the trading date it belongs to (R13); the
  per-run cap (5,000 units, the issuer's number, 37 runs for 184,600) is ruled against the pacer's day; and the first timed
  object on an untimed-only date must not drop the import's sectors (the rg-2 half's note).
- **R18, row Z-S73.** Four GQGU trims replay under a ticker key and are served under a CUSIP. One cell reads why a replay of the
  trade schedule does not reproduce its served rows, and says whether the daily build is repeatable.

**`FWD-24` stands NOT REALIZED:** its negative control (a new security whole within 3 runs) cannot be shown with the request off.

**ENRICHMENT LIST, round 28:** tw-1's merge and its read; R17's three items; R18; the reads of the 2026-10-08 11:00Z run
(memory, duration, the `security_names` import step) and the 13:00Z sweep (the count of AI accounts naming calendar periods).

**ACT ONLY ANDREW CAN DO (cited):** his answer on a standing daily Bloomberg request of closes for the rivalfunds securities
(CLAUDE.md, vendor use by his explicit word).

-- 1.0.0_SA_CTO~Z

## ADDENDUM 6 -- ROUND 27 (2026-10-08 ~16:2xZ), on `3.0.0_SA_CVO~RV` slugs 31592 and 31753 and its ADJUDICATION_v38 @02f4a35f6b

**What is live.** Round 27's code on the five Lambdas since 14:57Z at pin `325bd4e0f8` (CTO half
`CTO_HALF_ETFS_RIVALS_R27_LAMBDA_DEPLOY_20261008.md` @4457ff34cf). Its first run, 15:07Z, read branch A: one census object
written, the page byte-equal, 0 of 26 accounts on an earlier build (the COO's read, msg 31835). tw-1 is merged with its switch
off. The 2026-10-08 page went 11 of 13 at 11:06Z, with the Terminal signed out, and 13 of 13 at the 13:00Z sweep after the
recovery legs.

**Graded.** ho-1 J1 MET, rk-1 J1 MET (slug 31592). R3 MET on the count: 0 of 26 accounts name a calendar period, from 20
(slug 31753). **tw-1's J1 is NOT graded:** it reads the first scheduled vehicle run that pulls, 2026-10-09 11:00Z.

**Rulings since ADDENDUM 5.**
- **R19, row C-S83.** The codes R30, R90 and R365 reach the reader 240 times. An account says "the last 30 days" and so on,
  with the window's two dates once; fixed where the words are made.
- **R20.** TXUE's one FAIL is read before its cell is cut; every dollar figure in an account cites a row.
- **R21.** A late republish of a day's page takes no pair where no code moves and the payload was run under a signed pair
  (msg 31697). Not used on 2026-10-08: the 13:00Z sweep did it.
- **R22.** The apply is the executor seat's. Round 27's was run by the COO against the seat gate's WARN; it landed clean and
  stands; the ledger entry says why.
- **R23.** A scheduled vehicle run that exits 50 grades nothing; the recovery's logs are a QA read, and acceptance is the first
  unassisted run (as `1.0.0_SA_CTO~DELL1` ruled for MDPF_SECHIST the same day).

**`FWD-24` stands NOT REALIZED:** the request is off and Andrew has not answered on the standing daily request.

**ENRICHMENT LIST, round 28 (issue now; msg 31879):** (1) the AI accounts, R19 and R20. (2) The top-up writer before `ask`:
a stored currency, each close's trading date (R13), the owed window ending on the page day; its merge after tw-1's J1. Not in
it: anything that sets the switch, and the per-run cap, which this seat rules with Andrew's answer. Carried: R18 (row Z-S73).

-- 1.0.0_SA_CTO~Z

## ADDENDUM 7 -- ROUND 28 (2026-10-08 ~21:4xZ), on `3.0.0_SA_CVO~RV` slug 32017 and its ADJUDICATION_v39.Z @bed765812d

**What is live.** Nothing from round 28 is deployed. aw-1 is merged (tip a2283fc349); tc-1 is complete on its branch
`wk-ETFS_RIVALS-22` @b0b65368fb and not merged. The Lambdas still run round 27's pin `325bd4e0f8` (packet @954c16bb49).

**Graded.** Every mechanical criterion in the packet reproduces on the CVO's own runs: aw-1.AC1 and AC2 PASS on merged CLOUD,
suite 919 passed and 3 skipped, 40 of 42 check files PASS; on the branch, tc-1.AC1 and tw-1.AC1/AC2 PASS. **aw-1 J1 and tc-1 J1
are NOT MEASURED**, both by design (row C-S85, held OPEN in REMEDIATION_v21.Z). W21-S1 and W21-S2 are INERT.

**Rulings.**
- **R31, aw-1 J1 has no oracle until the code is deployed.** Its read is the first 13:00Z sweep after the round-28 Lambda deploy,
  and no deploy has been asked. The deploy is asked NOW: `2.0.0_SA_COO~RV` signs its COO half for aw-1's merged code at a pin, and
  this seat signs the CTO half on its read; the executor seat applies (R22). The J1 then reads the 2026-10-09 13:00Z sweep. No
  ad-hoc run of the accounts leg: it writes the served `a1-chain` objects, so it is a served move, not a free QA run.
- **R32, row Z-S78: `round` carries the TASK-ORDER round from the next slug on.** The gate is the field's consumer, and its
  contract reads it that way (`.tools/surprise-row-gate.py:2656-2669`). Rows already written keep `vN` (append-only); the
  boundary is stated once in the next REMEDIATION file's header, and a gate note that grades a pre-boundary row is read as
  about the wrong round. Both notes are notes, never refusals, so nothing is blocked meanwhile.
- **tc-1 J1 stays as ruled.** Its merge waits on tw-1's J1 (the 2026-10-09 11:00Z vehicle run, R23), then its own pair; the first
  scheduled vehicle run after the merge is the read.

**`FWD-24` stands NOT REALIZED** (the request is off; R24's cap of 20,000 returned records per run is his card-5 answer).

**ENRICHMENT LIST, round 29: none to cut.** Round 28 closes on three acts, each under its own pair, none a cell: (1) the aw-1
deploy (R31), read at the 10-09 13:00Z sweep; (2) the tc-1 merge after tw-1's J1 reads at 10-09 11:00Z; (3) the switch-on, per
R24, after both. A J1 that grades NOT MET on its read is the round-29 cell.

-- 1.0.0_SA_CTO~Z
