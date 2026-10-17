# ETFS_RIVALS -- surprise channel, investigations (dell1's append file)

dell1's own append file for this project's channel. ETFS_RIVALS moved to dell1 on Andrew-direct ~01:5xZ 2026-10-09
(@a0db38c8ae). The site-Z rows before that move are in `INVESTIGATION_v1.Z.md`, which only site Z writes. Rows minted here carry
dell1's coordinate `D1-` (org/devices/DEVICES.json), so they cannot collide with that file's `Z-` rows.

```json
[
  {
    "id": "ETFS_RIVALS-D1-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-09T03:12:59Z",
    "one_line": "DISARM of ETFS_RIVALS-Z-S79 and ETFS_RIVALS-Z-S80 on their disarm owner's act (2.0.0_SA_COO~V1, commit c07077f4e1, word msg 1474): RIV-tw-1 J1 AMENDMENT 1 reads J1 only on the first scheduled run that REACHED the enrichment leg, so the 2026-10-08 run (exit 97, no session) reads UNVERIFIABLE, never PASS. The act is the one sentence S79's notes name as its disarm. J1 itself stays owed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit c07077f4e1 (2.0.0_SA_COO~V1), an ancestor of HEAD bc1ce7b850 (merge-base read by this seat 03:12Z): J1 at TO-RIV-tw-1 now carries 'AMENDMENT 1 ... J1 is read on the FIRST scheduled vehicle run that REACHED the enrichment leg -- its log carries the RIVALFUNDS ENRICHMENT STEP line, an enrichment exit code other than 97, and no vendor-session-failure line ... A run that did not reach the leg reads UNVERIFIABLE for J1, never PASS; the 2026-10-08 11:00Z run is such a run.' (printed from git show HEAD:<order>, one match)",
        "the same commit amends TO-RELAY-tw1-vehicle-log-20261009: the transcriber adds the verdict line '-- DID THIS FIRE REACH THE ENRICHMENT LEG? --' and the whole log is committed beside it as VEHICLE_LOG_20261009_1100Z.full.log",
        "S79 notes (@c086fcc096): 'the disarm is one sentence from the issuer -- that J1 is read on the first fire that REACHED the enrichment leg, not on the earliest date in the range'",
        "S80 (@eaf6d69c9a): disarm_owner moved to 2.0.0_SA_COO~V1 per 0.0.0_AB_MSTR~Z msg 32284"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "ETFS_RIVALS-Z-S79",
      "ETFS_RIVALS-Z-S80"
    ],
    "spec_asserts": "S79/S80: ARMED until the issuer states that J1 is read on the first fire that reached the enrichment leg; the CVO writes the disarm clock (surprise-row-gate R-15).",
    "world_is": "The issuer's statement is in the order at HEAD, and its predicate is sharper than the row asked for: it names the three conditions (STEP line, exit not 97, no session-failure line) and the four session-failure strings. The hazard S79 named (a non-reaching run consumed as a PASS) can no longer arise from J1's wording. What survives the disarm: (1) J1 is still owed, and the 2026-10-09 11:00Z fire reaches the leg only if the Terminal is signed in at 07:00 local; (2) a remediation row with the disarm clock is written at the round-28 slug, because a new remediation row is refused while task orders are open (2 pending at HEAD).",
    "notes": "Written as an investigation row because the surprise-row gate refuses a new remediation row mid-round (LD-0521); a REMEDIATION_v22 with this clock was refused at commit (2 of 128 orders not terminal) and withdrawn uncommitted. The remediation rows for S79 and S80, with disarm DISARMED at this row's surfaced_at, are owed at the next slug."
  },
  {
    "id": "ETFS_RIVALS-D1-S2",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~V1",
    "surfaced_at": "2026-10-09T04:02Z",
    "one_line": "The ruling that puts act 3's standing Bloomberg draw on MDPF_DEMQUE's books says the vehicle reads the queue's pause/stop state before each draw, but no such state exists to read and the history-owed step (tw-1 + tc-1) reads none: switching RIVALFUNDS_HISTORY_OWED to ask on the code as built would draw past a queue pause",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~V1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Ruling XA-20261009T033809Z-8c1a (1.0.0_SA_CTO on laptop, 2026-10-09T03:42:38Z, read with `xadj.py show`), condition 1: '2.0.0_SA_COO~Q1 enters the standing request before the first run. The queue may pause or stop it at its reserve, or when a higher tier needs the budget; the vehicle reads that state before each draw.'",
        "data/etfs/scripts/rivalfunds/enrichment_bloomberg.py `_history_owed` on branch wk-ETFS_RIVALS-22 @b0b65368fb (read in full at the simulated merge onto origin/box/sitez 37aefc2855): the only gate before a request is `bbg_budget.check_points`; no queue or request-state read.",
        "org/missions/D8/MDPF/MDPF_DEMQUE/prd/MDPF_DEMQUE_PRD.md: one Grep for standing / pause / stop / reserve near state / status / read returns 2 lines (:149 the backfill allowance arithmetic, :174 a corporate-actions sentence); no readable per-request state is specified. The ruling's condition 3 names a standing request as a new request shape for C-QUOTE at Q1's next round."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "XA-...-8c1a condition 1: before each history-owed draw the vehicle reads the standing request's queue state and draws nothing when it is paused or stopped.",
    "world_is": "No queue state for a standing request exists to read (MDPF_DEMQUE PRD), and the vehicle's history-owed step reads none. Acts 1 (aw-1 deploy) and 2 (tc-1 merge) draw nothing and are unaffected; act 3 (the switch-on) cannot meet condition 1 until (i) Q1 names where the state lives and (ii) a rivalfunds cell reads it.",
    "notes": "Disarm (this seat, now): act 3's order is not cut and RIVALFUNDS_HISTORY_OWED is not set to ask until both (i) and (ii) exist; the switch stays unset. The cell for (ii) is new work outside the frozen round-28 decomposition, so it is the CTO's to place (round 29 or an addendum); (i) is Q1's interface. Owner of the remedy: 1.0.0_SA_CTO~DELL1 places it; 2.0.0_SA_COO~Q1 names the state."
  },
  {
    "id": "ETFS_RIVALS-D1-S3",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~V1",
    "surfaced_at": "2026-10-09T04:26Z",
    "one_line": "`.tools/crossbox-call.py open` writes an ORDER's file under org/devices/crossbox/ and says to commit it, but org/devices/** is lane NFRA_CTLPLN_FAST_C and a COO issuer is not a permitted agent, so a COO cannot commit the ORDER site Z asked it to open; only a CTO has committed crossbox files so far",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "crossbox-call.py open, 2026-10-09T04:24:21Z: OPENED XB-20261009T042421Z-e448 and XB-20261009T042421Z-897f, each printing 'NEXT: commit org/devices/crossbox/<id>.json'",
        "safe-commit 04:24:51Z and 04:25:15Z: 'VIOLATION: org/devices/crossbox/XB-20261009T042421Z-897f.json -- lane=NFRA_CTLPLN_FAST_C ... agent=2.0.0_SA_COO~V1 not in permitted_agents' (org/git-author-override-audit.log, 2 BLOCK lines)",
        "git log -8 -- org/devices/crossbox/: 4 commits, all by 1.0.0_SA_CTO~DELL2",
        "site Z REC (0.0.0_AB_MSTR~DELL1 msg 1681) asked this COO to open the ORDER itself"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "An issuer opens a crossbox ORDER and commits it so the other box pulls it (crossbox-call.py NEXT line).",
    "world_is": "The lane on org/devices/** refuses a COO's commit of the ORDER file; the file sits uncommitted until a permitted seat commits it.",
    "notes": "Worked around by asking 1.0.0_SA_CTO~DELL1 to commit the two files; the order files themselves (e9fe72e427, e3b33d03c4) are committed. Remedy owner: the NFRA_CTLPLN lane's grantor (a lane-ANY carve-out for org/devices/crossbox/), not this seat."
  },
  {
    "id": "ETFS_RIVALS-D1-W23-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~23",
    "surfaced_at": "2026-10-09T06:10Z",
    "one_line": "RIV-wa-1 item 1 divides by every split row; the same event in two corporate_actions objects (stored row plus WS2-b's inferred row, or repeated across partition dates) would divide twice, so series() applies an identical (ex_date, ratio) row of a key once, MEASURED first; item 3's 'previous drawn price' leaves every later day a gap for a key whose level never returns, until a row is stored",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/price_series.py _adjustments(): dedupe on (ex_date, ratio) per key; tested by test_ws2_wa1_split_adjusted_series.py::test_the_same_event_read_twice_applies_once_and_the_measured_row_is_kept",
        "price_series.series(): last = (date, price) of the previous DRAWN point and a dropped day does not move it, as item 3 words it; the AC1 check (c) has one big-move day and cannot tell the two readings apart"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Item 1: every row with event_type split and an ex_date inside (start, end] divides every earlier price by its ratio, cumulative over several rows. Item 3: a drawn price more than 3x or under one third of the key's previous drawn price, with no applied row between them, is not drawn.",
    "world_is": "load() reads ALL objects under corporate_actions/date=<D>/ for the window, so one event can arrive more than once; adjusting by every copy would apply 15 x 15. The order does not say whether two identical rows are two events, so they are treated as one. Item 3 as worded compares to the last DRAWN price, so an unrecorded permanent level change (a real 70% fall, or a split nobody stored) leaves every later day a gap, which is the visible signal that a row is missing.",
    "notes": "Not disarmed because INERT: nothing is served until the issuer's real run. If two same-ratio same-day splits are ever real, or the gap should end after one day, the change is one line each in price_series.py. Owner: 2.0.0_SA_COO~V1 reads at the merge; the J1 grader sees the effect on the first page."
  },
  {
    "id": "ETFS_RIVALS-D1-W24-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~24",
    "surfaced_at": "2026-10-09T06:05Z",
    "one_line": "RIV-wb-1 check ws2-b.AC1 arm (c) requires the first search query for a nameless G4 candidate to contain 'Tokio Marine', but no frame the module is handed carries a name, so the module seeds a ticker-to-name map",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/ws2-b.AC1.py: G4 frame columns are security_id,date,px_close,currency (no security_name); arm (c) passes c[0] from detect() to lookup() and asserts 'Tokio Marine' in calls[0]",
        "no security name table for TKOMY or 8766 in data/etfs/scripts/rivalfunds (Grep 'Tokio Marine|TKOMY' over the package: 0 files); security_names.py reads a gold table through a sink, which lookup() is not given",
        "data/etfs/scripts/rivalfunds/dramatic_move.py NAME_SEED = {TKOMY, 8766} -> 'Tokio Marine Holdings'; lookup(candidate, search, names=) extends it; an unseeded nameless ticker is searched by its id form"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cell says a candidate carries security_name 'when the frame has one' and lookup builds its query from 'the security name (or id)'; arm (c) of the check nonetheless needs the company name in the first query for a candidate from a frame with no name.",
    "world_is": "A nameless candidate can only reach 'Tokio Marine' through knowledge held in the module, so a two-entry seed (the two live lines of the one company the cell was cut for) is in dramatic_move.py. The issuer's hookup at the merge should pass names= read from the gold security_names object (security_names.py) so any other nameless ticker is searched by company name; otherwise it is searched by its ticker id.",
    "notes": "Remedy owner: 2.0.0_SA_COO~V1 at the hookup (pass names= from gold/security_names); the seed stays as the floor."
  },
  {
    "id": "ETFS_RIVALS-D1-W26-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~26",
    "surfaced_at": "2026-10-09T06:35Z",
    "one_line": "Two G5 readers outside RIV-wd-1's paths do not skip the new `below_tolerance` action: publish_page.py's audit window loop lists every G5 row (only no_shares_moved and cash-equivalent rows are set aside) and ai_accounts.py's trade facts take every row with an est_notional_base; publish_page also pairs windows by consecutive report labels, not by gold_trade_schedule's last-new-report anchor",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~V1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/publish_page.py:535-545 (branch wk-ETFS_RIVALS-26): `for r in rows: if no_shares_moved(r) ... if cash_equivalent_trade(r, names) ... out.append(r)` -- no test on r['action']; render._trades then prints the action as the row's label (render.py:446)",
        "data/etfs/scripts/rivalfunds/ai_accounts.py:169-181: `trades = [r for r in _fund_rows(g5, fund_id) if ... _num(r.get('est_notional_base')) is not None ...]` -- no action filter, and the fact text prints `{r.get('action')}`",
        "gold_buying_trend.py:246 (`_SIGN.get(action)`), trade_markers.py:39 (`_SIDE.get(action)`) and render.py:2029 (`_TRADE_ACTIONS`) already skip an action outside entry/add/trim/exit, so those three need no edit; tests/test_wd1_tolerance_and_repeat.py::test_readers_skip_a_below_tolerance_row covers trade_markers",
        "publish_page.py:529-531 pairs `dates[i-1] -> dates[i]` (consecutive report labels); gold_trade_schedule.infer_windows now pairs a new report with the LAST NEW report (a repeat date is never a prior), so a G5 row's window_start can precede publish_page's d0 for the same window_end"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-wd-1 interface item 4: readers that count trades skip the rows items 1-3 exclude.",
    "world_is": "Three of the five readers skip by action already; publish_page.py (the audit page's window list and its per-window trade count) and ai_accounts.py (the T-facts) do not, and both are outside this order's <paths>. Once a G5 built at gold_trade_schedule/4 is served, a below_tolerance row would list as a trade on the audit and could enter an AI-prose fact.",
    "notes": "Hookup for the issuer (not edited here): in publish_page.py's row loop `continue` on action == 'below_tolerance' (counting it for RIV-wc-2's exclusion line), and in ai_accounts.py add `and str(r.get('action')) != 'below_tolerance'` to the `trades` list; decide whether publish_page shows the G5 row's window_start for a window after a repeat. No G5 at /4 is served before the merge, so the hazard is armed only for the merge-and-deploy order."
  },
  {
    "id": "ETFS_RIVALS-D1-S4",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~V1",
    "surfaced_at": "2026-10-09T06:43Z",
    "one_line": "The holdings calendar's `repeat` labels for CGIC 2026-10-01..10-06 are STALE, not the trade windows: each date's holdings_coverage row was written at that date's first pull (actual_report_date one report behind) and never rebuilt when canonical_shape for the date was re-captured with the new report, so the audit shows trades on days it labels repeat",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "gold holdings_coverage date=2026-10-02/05/06 holdings_coverage.parquet, CGIC: status repeat, actual_report_date 2026-09-30 / 2026-10-02 / 2026-10-05 (date=2026-10-01: repeat, 2026-09-30)",
        "gold canonical_shape newest object per date, CGIC: date=2026-10-02 holdings-20261006T123244Z (207 rows, extra_attributes.bloomberg.source_report_date 2026-10-02 on 207 of 207), date=2026-10-05 holdings-20261007T110910Z (205 of 205 = 2026-10-05), date=2026-10-06 holdings-20261008T122342Z (206 of 206 = 2026-10-06); summed non-cash quantity 143,709,123 / 143,735,023 / 144,078,055 (moving); date=2026-10-01: 0 CGIC rows",
        "Worker 0.9.0_WK_ETFS_RIVALS~26 (RIV-wd-1) concluded by code reading alone (no S3) that the windows were wrong; the objects above say the label is. RIV-wd-1's infer_windows reads the same source_report_date, so on these objects it keeps the trades: no harm"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "WS3 item 6: a day the calendar marks repeat carries no trade, and the calendar and the windows read the same object.",
    "world_is": "The windows read the re-captured holdings (new reports, real trades); the calendar keeps the first capture's verdict. The calendar must be rebuilt (or read source_report_date) when a date's canonical_shape is rewritten.",
    "notes": "Remedy: a WS3 cell in the second issuance (with item 8), on gold_holdings_coverage.py: classify from the newest canonical_shape object's source_report_date, or rebuild the date's coverage when canonical_shape is rewritten. Owner of the cut: 2.0.0_SA_COO~V1."
  },
  {
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~25",
    "surfaced_at": "2026-10-09T06:10Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "ETFS_RIVALS-D1-W25-S1",
    "one_line": "RIV-wc-1 cannot keep two script-size caps green: test_r24cu1_chart_frame_ticks_tip.py::test_script_shape (<= 7369+3000 = 10369 bytes) and test_r25mr1_marker_readout.py::test_script_growth_bound (<= 9348+600 = 9948 bytes) cap CHART_SCRIPT, which is 9502 bytes at the base and 10595 with the cell; neither test is in the order's <paths>",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "The order says 'every other test stays green' and its <paths> name only test_r21pl1 and test_r18tl1 as tests to update.",
    "world_is": "The cell (tradehead, a windowed tradelines, putTrades with the empty-window sentence, adjwords and the dialog line) adds 1093 bytes to the one script. r25mr1's cap (9948) leaves 446 bytes of growth and r24cu1's (10369) leaves 867; the 9502-byte base was already above r24cu1's pre-r25 figure of growth. AC1 passes; the rivalfunds suite ends at 3 failed, 918 passed, 6 skipped, and these two are 2 of the 3.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "pytest -q rivalfunds/tests from data/etfs/scripts at branch wk-ETFS_RIVALS-25: 'assert 10595 <= (7369 + 3000)' and 'assert 10595 <= (9348 + 600)'",
        "len(CHART_SCRIPT.encode()) at box/dell1 base render.py = 9502"
      ]
    },
    "notes": "Not edited: the two tests are outside <paths>. Remedy for the issuer: widen both caps to the new figure (a one-number edit each) in a later order or at the merge, or rule that the cell must shrink. Owner: 2.0.0_SA_COO~V1."
  },
  {
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~25",
    "surfaced_at": "2026-10-09T06:10Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "ETFS_RIVALS-D1-W25-S2",
    "one_line": "test_r15md1_chart_frame_and_script.py:63 pins the static placeholder \"The fund's trades over the last 365 days load with the chart.\", which the order's own interface item 1 ('No static text names 365 days') and AC1 arm (a) forbid; the test is not in <paths>",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "Item 5 lists test_r21pl1 and test_r18tl1 as the only tests that pin the old heading, and says every other test stays green.",
    "world_is": "AC1 arm (a) fails if '365 days' appears anywhere in _trade_list([]), so the placeholder had to become \"The fund's trades load with the chart.\"; test_r15md1::test_the_trades_are_in_the_frame_in_words_and_a_fund_without_one_says_so asserts the old sentence and now fails (third of the 3 suite failures).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "render.py HEADP / _trade_list at this branch; test_r15md1_chart_frame_and_script.py:63"
      ]
    },
    "notes": "Not edited (outside <paths>). The one-line fix is to replace the old sentence with the new one in that assertion. Owner: 2.0.0_SA_COO~V1."
  },
  {
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~25",
    "surfaced_at": "2026-10-09T06:10Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "ETFS_RIVALS-D1-W25-S3",
    "one_line": "Interface item 2 says tradelines returns the lines 'oldest first ... worded as today's tradelines', but today's tradelines is newest first with a trailing 'and n earlier trades' line capped at 20; the two cannot both hold",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "tradelines(markers, from) -> trade lines oldest first, worded as today's.",
    "world_is": "Chosen: the window's markers are capped at the 20 most recent, shown oldest first, and the 'and n earlier trade(s) in the last <window>.' line LEADS (the omitted trades are earlier than the listed ones); an empty window returns [] and putTrades writes 'No trades in the last <n> days.'. test_r18tl1 was re-pinned to this shape. AC1 does not grade the order.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "render.py CHART_SCRIPT tradelines; tests/test_r18tl1_trade_list_from_markers.py; tests/test_ws2_wc1_trade_list_scope.py"
      ]
    },
    "notes": "J1 (CVO) sees the shipped order. If newest-first was meant, a one-line change to the sort."
  },
  {
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~25",
    "surfaced_at": "2026-10-09T06:45Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "ETFS_RIVALS-D1-W25-S4",
    "one_line": "Removing the header Period row also removes what only that row carried: the per-fund '(nothing ranked)' state and grey rule, and the per-fund date pills; their CSS rules in render.py now match nothing",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "WS3 item 7: the header's PERIOD row is removed; the ranking panels' period controls and the 30/90/365 data stay; no other header row changes.",
    "world_is": "Four existing tests pinned the row's contents (test_crorv_layout period row, test_r8rn1 top switch with dates, test_r6ui2 empty-period state, test_r8rn1 clipped-pill dates, plus the short-label count 3 -> 2) and were re-pinned to the new page. The panels' own switch (rf-pswitch) carries neither the per-fund empty-state grey nor the date pills, so those two signals are gone from the page; the dead CSS selectors (.rf-controls label[for=rf-period-*] grey rule, .rf-dt) remain emitted. _period_states and _period_dates in render.py are now unused.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "render.py _controls at this branch; tests/test_crorv_layout.py, test_r8rn1_period_switch.py, test_r6ui2_ranking_panels.py"
      ]
    },
    "notes": "J1 (CVO) sees the shipped page. Dead CSS and the two unused helpers can go in a later render.py cleanup; not done here (widening)."
  },
  {
    "id": "ETFS_RIVALS-D1-S5",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~V1",
    "surfaced_at": "2026-10-09T07:36Z",
    "one_line": "CORRECTS D1-S4: for CGIC the two witnesses of a report's date DISAGREE by one trading day -- the Bloomberg sidecar's claimed_report_date lags the delivery date (10-05 capture claims 10-02, 10-06 claims 10-05) while canonical_shape stamps the rows' source_report_date with the delivery date -- so either the calendar's repeat labels are right and every CGIC trade window is dated one trading day late, or the labels are wrong; which one decides the fix",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Bloomberg bronze sidecars, requested_date -> status, claimed_report_date[CGIC]: 2026-10-02 batch-20261003T110629Z OK 2026-09-30; 2026-10-02 batch-20261004T110522Z OK 2026-09-30; 2026-10-02 batch-20261005T123303Z BAD-ANCHOR None; 2026-10-02 import-d12-idvz-pfoe ...20261005T054409Z OK None; 2026-10-05 batch-20261006T110635Z BAD-ANCHOR None; 2026-10-05 batch-20261006T123223Z OK 2026-10-02; 2026-10-06 batch-20261007T110832Z OK 2026-10-05 (7 sidecars read, 07:3xZ)",
        "gold canonical_shape newest object per date, CGIC extra_attributes.bloomberg.source_report_date: date=2026-10-02 -> 2026-10-02 (207/207), date=2026-10-05 -> 2026-10-05 (205/205), date=2026-10-06 -> 2026-10-06 (206/206); summed quantity moves each date (row D1-S4)",
        "gold_holdings_coverage.classify: actual < expected -> 'repeat' unless the fund is measured periodic; the calendar's actual is the sidecar claim (_bbg_obs), the windows' date is the canonical row date"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "One report date per capture, the same in the calendar and in the trade windows.",
    "world_is": "Two witnesses one trading day apart for every CGIC capture 10-02..10-06. D1-S4's reading (labels stale, windows right) assumed the canonical rows' date is the truth; it is unproven.",
    "notes": "Not cut: which witness is true is a data ruling (1.0.0_SA_CTO~DELL1). If the sidecar is true, the fix is the canonical rows' date (and every CGIC trade window moves back one trading day); if the rows are true, the fix is the calendar (classify on the rows' date, or treat a consistent one-day lag as new). RIV-wd-1's infer_windows reads the rows' date, so it follows whichever is fixed."
  },
  {
    "id": "ETFS_RIVALS-D1-S6",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~V1",
    "surfaced_at": "2026-10-09T08:15Z",
    "one_line": "RIV-we-1 (canonical source_report_date = the claimed as-of) is FORWARD-ONLY as deployed: build-canonical-shape names a revision by a digest of its INPUTS, not its code, and a replay that finds that revision already stored 'adds nothing', so every served canonical object (and the trade windows built on it) keeps the old date until history is deliberately rebuilt",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/gold_canonical_shape.py:945-956 at ba92996a72: `same` holds holdings-<rev>.parquet with rev from _revision_digest(chosen, g4); `hit` -> 'this revision is already gold: a replay adds nothing'",
        "real run 2026-10-09 ~08:0xZ (ws2/real_run_local.py --canonical, overlay of live objects): build-canonical-shape PARTIAL, written_new 0 over 16 report dates; build-trade-schedule written_new 0; we1_windows_compare: 0 dates changed for every one of 13 funds"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CTO ADDENDUM 2 @9f0a957c00: the CGIC trade windows move a trading day earlier.",
    "world_is": "After deploy, only captures with new inputs get the claimed as-of; served history (CGIC 10-02..10-08) keeps delivery-day dates.",
    "notes": "A history rebuild is a served write (canonical_shape and trade_schedule objects for the affected dates) under its own pair: either a forced replay that ignores the stored revision, or a revision digest that includes the gold code version. The issuer's local proof hides the served canonical objects from the overlay (--fresh-canonical) to show what the rebuild would write."
  },
  {
    "id": "ETFS_RIVALS-D1-W28-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~28",
    "surfaced_at": "2026-10-09T08:40Z",
    "one_line": "RIV-we-2: the G6 (flow_reconciliation) object cannot carry window_start_delivered / window_end_delivered -- its SCHEMA and finish_row live in gold_flow_reconciliation.py, outside this order's paths, so the pair rides on the recon dict and infer_recon's frame only",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/gold_flow_reconciliation.py:50-63 SCHEMA has no *_delivered column; finish_row (:88-90) takes only COLUMNS from the recon dict, so the parquet G6 row drops the pair",
        "data/etfs/scripts/rivalfunds/gold_trade_schedule.py: _pair_rows' recon dict carries window_start_delivered / window_end_delivered; infer_recon appends them after g6mod.COLUMNS (tests/test_we2_window_asof.py::test_recon_rows_carry_the_same_pair)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-we-2 interface item 2: the G5 schema gains the two columns; recon rows carry the same pair.",
    "world_is": "G5 parquet gains the pair; the served G6 parquet row does not (its schema is a file this order may not edit). The recon window_start / window_end DO move to the as-of dates, so G6 window_end and G5 window_end stay equal.",
    "notes": "To land the pair in the served G6 object, add the two date32 columns to gold_flow_reconciliation.SCHEMA (a later order that owns that file). Also unchanged by design: G5 `date`, `window_trading_days`, the window_widened flag, the corporate-action window test and the object address (date=<delivery day>) stay on the delivery days; only the labels window_start / window_end moved."
  },
  {
    "id": "ETFS_RIVALS-D1-S7",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~V1",
    "surfaced_at": "2026-10-09T08:45Z",
    "one_line": "CORRECTS D1-S5 (this seat's error): canonical_shape partitions are ALREADY dated by the vendor's claimed as-of, not the delivery day -- partition date=2026-10-05 holds capture 20261007T110910Z (requested 10-06, claims 10-05) -- so CGIC's trade windows were right all along; RIV-we-1/we-2 change nothing on real data, ADDENDUM 3's scoped rebuild has nothing to rebuild, and the only real defect is the calendar calling a consistently one-day-lagged fund 'repeat'",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Dry run (ws2/real_run_local.py --canonical --fresh-canonical at 598173c0fa, live reads, local writes): build-canonical-shape OK 27 written, 20915 rows; build-trade-schedule OK 26 written. Over every Bloomberg row of the rebuilt canonical (11 funds, 18,000+ rows): source_report_date != partition date in 0 rows; report_date_claim INFERRED in 0 rows",
        "CGIC: date=2026-10-02 object holdings-20261006T123244Z (sidecar requested 10-05, claims 10-02); date=2026-10-05 holdings-20261007T110910Z (requested 10-06, claims 10-05); date=2026-10-06 holdings-20261008T122342Z -- partition = claim in each",
        "we1_windows_compare after the rebuild: CGIC 1 of 25 dates changed, the 2026-08-31 range edge only; 7 funds 0 changed; 5 funds 1 changed (the same edge)",
        "D1-S5 compared the sidecar's REQUESTED date with the canonical PARTITION and read the partition as a delivery day; it is the as-of"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "D1-S5 / ADDENDUM 2: canonical rows carry the delivery day; CGIC windows must move a trading day earlier.",
    "world_is": "Partitions are the as-of; windows are already as-of dated. we-1's `delivered_on` records the partition (the as-of), not the delivery day: misnamed. The calendar (gold_holdings_coverage.classify) compares the claim with the REQUESTED day, so a fund whose file always lags one trading day reads 'repeat' every day.",
    "notes": "Remedies: (1) withdraw ADDENDUM 3's rebuild (nothing to rebuild); (2) we-1's delivered_on takes the capture's requested_date (or is dropped); (3) the calendar treats a capture whose claim is newer than the previous capture's claim as `new` (a lagged daily fund), keeping `repeat` for a claim equal to the previous one. Owner of the rulings: 1.0.0_SA_CTO~DELL1."
  },
  {
    "id": "ETFS_RIVALS-D1-S8",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~V1",
    "surfaced_at": "2026-10-09T12:25Z",
    "one_line": "The live prompt a1-chain/7 (aw-1, live 11:21Z) makes the Direction Verdict lead with the period's dates: both verdicts of a two-fund real run open 'From <date> to <date>, ...' -- a new shared lead, of the kind Andrew's comment 7 objects to",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ws3_item8_prep/ai_real_run_local.py (live reads, local writes, real model) at box/dell1 4d688f78a7+, page day 2026-10-08, funds CGIC and IDVZ, run 20261009T121734Z-ai: CGIC 'From 2025-10-07 to 2026-10-07, the long-run trend is only partly borne out by the ...'; IDVZ 'From 2026-01-02 to 2026-10-07, the direction verdict is mixed: the last 30 days both ...'",
        "0 S3 objects for that run_id (read back); the parquet is only under C:/tmp/wg1-base-run/layer",
        "Denominator: 2 funds of 13; the 13:00Z sweep's page is the first full read"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-aw-1: the two dates of the period are stated once in text. Andrew-direct comment 7: the verdicts should not all lead the same way.",
    "world_is": "The model meets the dates rule by opening with them, so every verdict may lead 'From <date> to <date>, ...'.",
    "notes": "Remedy in RIV-wg-1 (WS3 item 8, cut after the 13:00Z read): the generic-opening rule names a dated lead too; the dates stay in text, not as the lead. Read at the 13:00Z page with verdict_openers_check.py (dates collapse to one token). Owner: 2.0.0_SA_COO~V1."
  },
  {
      "id": "ETFS_RIVALS-D1-S9",
      "project": "ETFS_RIVALS",
      "fabric": "dell1",
      "surfaced_by": "2.0.0_SA_COO~V1",
      "surfaced_at": "2026-10-09T13:30Z",
      "one_line": "AI accounts print a small notional as '$0.0 million': WCMG and ETFT verdicts carry it three times each on the issuer's real run -- a figure that reads as zero for a real trade",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
          "status": "GROUNDED",
          "evidence": [
              "Real run 20261009T132214Z-ai (a1-chain/8, merged @3bd0c7c023, local writes): WCMG 'leaned away by $0.0 million' and two more; ETFT three; 0 of the other 11 funds",
              "ai_accounts._mn shows a notional in millions at one decimal, so any |v| < 50,000 displays as $0.0 million and the model copies the display form (SYSTEM rule 1)",
              "Denominator: 13 Direction Verdicts of one run; the 30-day accounts not counted"
          ]
      },
      "disposition": "UNDER_INVESTIGATION",
      "spec_asserts": "A figure in an AI account is the fact's display form and reads as the trade it names.",
      "world_is": "A sub-$50,000 notional displays as $0.0 million, which reads as no trade.",
      "notes": "Remedy candidates: _mn falls back to thousands ($42 thousand) under $0.05 million, or such trades are left out of the facts. A round-29 enrichment item; owner 2.0.0_SA_COO~V1."
  },
  {
      "id": "ETFS_RIVALS-D1-S10",
      "project": "ETFS_RIVALS",
      "fabric": "dell1",
      "surfaced_by": "2.0.0_SA_COO~V1",
      "surfaced_at": "2026-10-09T13:50Z",
      "one_line": "RIV-wb-1's dramatic-move lookup has NO production caller: no Lambda runs dramatic_move, no Lambda carries BRIGHT_DATA_API_KEY, and serp.py is not a staged package path -- so a deploy of HEAD serves wa-1's split adjustment only where a corporate-action row already exists, and none is written in production (Tokio Marine's 15-for-1 stays unadjusted)",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
          "status": "GROUNDED",
          "evidence": [
              "Grep 'dramatic_move' under data/etfs/scripts/rivalfunds (non-test) and infra/aws: only the module itself; the two other importers are issuer scripts (ws2/real_run_local.py, ws2/checks/ws2-b.AC1.py)",
              "boto3 get_function_configuration, 2026-10-09 ~13:4xZ: env names -- daily: RIVALFUNDS_AI_ENABLE, RIVALFUNDS_OPENAI_SECRET; the other four: none. No BRIGHT_DATA_API_KEY or BD_SERP_ZONE on any of 5",
              "infra/aws/lambda/etfs-pipeline/rivalfunds_package.py STAGED (7 paths) does not include data/find/dualbiz/scripts/serp.py, which dramatic_move.serp_search imports",
              "price_series._actions only READS gold corporate_actions; dramatic_move.write_rows is its only writer"
          ]
      },
      "disposition": "UNDER_INVESTIGATION",
      "spec_asserts": "Andrew-direct comment 1 (@9d08dd64d4): a dramatic move triggers a web search for a corporate action and an automatic refactoring of historical prices by the split multiple.",
      "world_is": "The lookup and the adjustment exist in code and were exercised only by the issuer's local real run; production has no caller, no key and no staged search client.",
      "notes": "Placement asked of 1.0.0_SA_CTO~DELL1: which Lambda runs the lookup (the sweep after canonical, or publish-page before price_series), the key as a Secrets Manager read (IAM limb) and serp.py staged. Owner: 2.0.0_SA_COO~V1."
  },
  {
    "id": "ETFS_RIVALS-D1-W32-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~32",
    "surfaced_at": "2026-10-09T14:20Z",
    "one_line": "The daily Lambda walks run_dag, not run_sweep: RIV-wi-1 item 2 names only run_sweep, and a call there alone would never run in production",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Grep run_sweep|run_dag under data/etfs/scripts: run_dag at sweep.py handler_entry; run_sweep only in tests/test_d1_sweep.py",
        "wi1_wiring_check.py reads run_sweep only (AC2 PASS), so it cannot see the run_dag wiring; tests/test_riv_wi1_sweep_lookup.py::test_run_dag_runs_the_lookup_once_before_the_first_publish does"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Cell item 2: sweep.run_sweep calls dramatic_move.run_for_day after the canonical / trade-schedule stages and before the day's publish.",
    "world_is": "sweep.handler_entry calls run_dag (data/etfs/scripts/rivalfunds/sweep.py handler_entry); run_sweep has callers only in tests. The lookup was wired into BOTH: run_sweep before its publish-page stage (AC2's literal read), and run_dag inside run_one(\"publish-page\"), once per walk, recorded in the outcome and in handler_entry detail.dramatic_move.",
    "notes": "Issuer: confirm the J1 read is on a run that goes through handler_entry/run_dag."
  },
  {
    "id": "ETFS_RIVALS-D1-W32-S2",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~32",
    "surfaced_at": "2026-10-09T14:20Z",
    "one_line": "serp.py cannot be staged alone: it imports _util.py and harvest.py from its own directory at module load, so STAGED stages the directory data/find/dualbiz/scripts",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/find/dualbiz/scripts/serp.py:30-32",
        "tests/test_riv_wi1_sweep_lookup.py::test_a_staged_lambda_tree_finds_and_imports_the_search_client copies STAGED into a temp tree and imports serp from _serp_dir() in a subprocess: PASS"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Cell item 4: STAGED stages data/find/dualbiz/scripts/serp.py.",
    "world_is": "data/find/dualbiz/scripts/serp.py lines 30-32 insert its own directory in sys.path then `from _util import fetch` and `from harvest import ...` (both stdlib-only files in that directory). A lone serp.py in a Lambda tree raises ImportError. rivalfunds_package.STAGED now carries the directory (13 files, 156K, stdlib-only) to the same relative path; wi1_wiring_check (b) accepts the file or its directory.",
    "notes": "The package zip grows by the directory's 156K (tests excluded by _IGNORE only for a directory named tests; test_registry.py rides along)."
  },
  {
    "id": "ETFS_RIVALS-D1-W32-S3",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~32",
    "surfaced_at": "2026-10-09T14:20Z",
    "one_line": "serp.py reads the SERP ZONE from a second Secrets Manager secret unless BD_SERP_ZONE is set, so the deploy pair needs that variable (or a second ARN) as well as RIVALFUNDS_SERP_SECRET",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/find/dualbiz/scripts/serp.py:213-242 and 413-414",
        "data/etfs/scripts/rivalfunds/dramatic_move.py serp_search"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Cell item 3: the key comes from BRIGHT_DATA_API_KEY or the secret named by RIVALFUNDS_SERP_SECRET (one GetSecretValue).",
    "world_is": "serp._bd_serp_zone() (serp.py:230-242) calls GetSecretValue on find-dualbiz/bright-data/serp when neither the cache nor BD_SERP_ZONE is set; dramatic_move.serp_search passes BD_SERP_ZONE through when present. Without it the Lambda role needs a read on that second secret too, else every search raises and counts as failed (no crash, no write).",
    "notes": "Applier contract: set RIVALFUNDS_SERP_SECRET (name or ARN of the key secret; raw string or JSON with api_key / bright_data_api_key / BRIGHT_DATA_API_KEY), grant the one-ARN secretsmanager:GetSecretValue, and set BD_SERP_ZONE (serp.py's own default zone is serp_opal) on the Lambda that runs the sweep (the daily one). Not set by this cell (out of bounds)."
  },
  {
      "id": "ETFS_RIVALS-D1-S11",
      "project": "ETFS_RIVALS",
      "fabric": "dell1",
      "surfaced_by": "2.0.0_SA_COO~V1",
      "surfaced_at": "2026-10-09T14:35Z",
      "one_line": "FOR FIND_INSURE's OWNER: the Bright Data key secret find-insure/bright-data/api-key (ARN suffix -7ojPkd) gains a SECOND consumer -- the etfs-rivalfunds daily Lambda (RIV-wi-1, its own deploy pair) reads it by exact ARN; a rotation or delete of that secret must reach ETFS_RIVALS",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
          "status": "GROUNDED",
          "evidence": [
              "CTO ruling ADDENDUM 7 @aa290d707e (msg 2555): option (a), GetSecretValue on exactly the -7ojPkd ARN, no copy; 'File a row in this project's channel telling FIND_INSURE's owner it now has a second consumer, so a rotation reaches both'",
              "find-dualbiz/bright-data/serp names api_key_secret = find-insure/bright-data/api-key (read 14:2xZ, key names only); data/find/dualbiz/scripts/serp.py _BD_API_KEY_SECRET defaults to the same secret",
              "Grant lands with RIV-wj-1 (gen_policies.py) under the RIV-wi-1 deploy pair; until that apply, the rivalfunds daily Lambda holds no grant on it"
          ]
      },
      "disposition": "UNDER_INVESTIGATION",
      "spec_asserts": "A secret's owner knows every consumer before a rotation.",
      "world_is": "find-insure/bright-data/api-key will have a consumer outside FIND_INSURE (and already serves find-dualbiz's serp.py by default).",
      "notes": "Owner to inform: FIND_INSURE's COO/CTO. Consumer of record: ETFS_RIVALS, 2.0.0_SA_COO~V1; env RIVALFUNDS_SERP_SECRET on etfs-rivalfunds-daily-lambda; policy statement GetSerpSecret in infra/aws/terraform/etfs-rivalfunds/policies/etfs-rivalfunds-daily-lambda.json."
  }
,
  {
      "id": "ETFS_RIVALS-D1-S12",
      "project": "ETFS_RIVALS",
      "fabric": "dell1",
      "surfaced_by": "0.7.0_AE_CloudOps~RV1",
      "surfaced_at": "2026-10-09T14:42Z",
      "one_line": "COO condition 5's snapshot asks for 20 trading days of holdings_coverage; the world holds 19 -- date=2026-10-09 does not exist, so CTO condition 8's per-key read has one key with no pre-image and no rollback bytes",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
          "status": "GROUNDED",
          "evidence": [
              "coverage_snapshot.py take C:/tmp/rv-ws23-covsnap 2026-10-09 20, run 14:40Z: 'SNAPSHOT: 19 of 20 keys saved', '2026-10-09: ABSENT'",
              "WS23_COVERAGE_SNAPSHOT_MANIFEST.json: 20 entries, 19 saved, 1 absent, absent day ['2026-10-09'] (sha256 6bbc0347ecc7abfe1fc9cf2b3a6dfe1173c858fdf6a2f94237150f6d69c1b3eb)",
              "the 2026-10-08 key reads {'gap': 11, 'new': 2}, so the two most recent partitions are the thin ones",
              "coverage_snapshot.py docstring: 'A missing key is recorded as absent', and compare prints 'was absent, now PRESENT' without counting it as a stop line"
          ]
      },
      "disposition": "UNDER_INVESTIGATION",
      "spec_asserts": "COO half condition 5: 'the applier copies every rivalfunds/etfs/gold/holdings_coverage/date=<D>/holdings_coverage.parquet for the 20 trading days ending 2026-10-09'. CTO half condition 8: 'each of the 20 snapshot keys is printed as unchanged or changed'.",
      "world_is": "19 of the 20 keys exist. date=2026-10-09 is absent at 14:40Z, after today's 13:00Z sweep. For that one key the condition 8 read cannot be unchanged-or-changed, and the condition 5 rollback has no bytes to restore: if the 2026-10-10 run creates it, the rollback for that key is 'delete or leave', never 'restore'. The other 19 keys carry full pre-images (bytes + sha256 + status counts), so the in-place writer's rollback is intact everywhere it has a prior state.",
      "notes": "Not a blocker and the apply proceeded: the snapshot instrument records absence by design, 2026-10-09 is inside the last-10-trading-day window G2 is allowed to write, and a first-ever write of an absent key is not a widening of served state. For L2 (the issuer's): grade 19 keys unchanged-or-changed, and grade 2026-10-09 separately as created-or-still-absent. Surfaced by the applier, 0.7.0_AE_CloudOps~RV1; disposition is the CVO's/issuer's."
  }
,
  {
      "id": "ETFS_RIVALS-D1-W34-S1",
      "project": "ETFS_RIVALS",
      "fabric": "dell1",
      "surfaced_by": "0.9.0_WK_ETFS_RIVALS~34",
      "surfaced_at": "2026-10-09T14:58Z",
      "one_line": "rivalfunds suite at the base has 1 failing test, test_r6ap1_ai_stage::test_policy_and_environment_split_and_committed_copy_is_current: it expects ONE secretsmanager action in the daily Lambda's generated policy, RIV-wj-1 (86c14e4b3a) added a second statement (GetSerpSecret)",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
          "status": "GROUNDED",
          "evidence": [
              "python -m pytest -q rivalfunds/tests from data/etfs/scripts, RIV-wk-1 branch: '1 failed, 999 passed, 6 skipped'; the failure is rivalfunds/tests/test_r6ap1_ai_stage.py:172 'sm[etfs-rivalfunds-daily-lambda] == [secretsmanager:GetSecretValue]' with 'Left contains one more item: secretsmanager:GetSecretValue'",
              "the test loads infra/aws/terraform/etfs-rivalfunds/gen_policies.py, which this cell neither reads nor edits (RIV-wk-1 touched price_series.py, dramatic_move.py and a new test only); git log of gen_policies.py: 86c14e4b3a RIV-wj-1 adds the GetSerpSecret statement",
              "not re-run at a clean base: the failure's path does not import either file RIV-wk-1 changed"
          ]
      },
      "disposition": "UNDER_INVESTIGATION",
      "spec_asserts": "RIV-wk-1 task order section 2: tests in rivalfunds/tests must keep passing.",
      "world_is": "One test, outside RIV-wk-1's paths, already fails at the base because RIV-wj-1 changed the generated policy without updating its assertion; the suite's final line is therefore 1 failed, 999 passed, 6 skipped with or without RIV-wk-1.",
      "notes": "Not fixed here: the test file belongs to no path of this order and the assertion change is RIV-wj-1's follow-through (the issuer decides)."
  },
  {
      "id": "ETFS_RIVALS-D1-S13",
      "project": "ETFS_RIVALS",
      "fabric": "dell1",
      "surfaced_by": "2.0.0_SA_COO~V1",
      "surfaced_at": "2026-10-09T15:50Z",
      "one_line": "round-close-check reads round 28 MAY-CLOSE with 8 of 8 judgment criteria GRADED, each 'by adjudication row ETFS_RIVALS-D1-C-S1' -- one 07:30Z row that grades none of wg-1/wh-1/wi-1 and HOLDS wa-1 and wd-1; the round is NOT closeable: wa-1 and wd-1 J1 HELD, wi-1 J1 needs the 2026-10-10 13:00Z sweep, tc-1 is unmerged, both deploy ledgers' L2 are open",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
          "status": "GROUNDED",
          "evidence": [
              "python .tools/round-close-check.py --project ETFS_RIVALS --round 28 at 15:4xZ: 'ROUND-CLOSE ... orders=15 judgment=8 graded=8 ungraded=0 ... verdict=MAY-CLOSE'; every JUDGMENT line cites ETFS_RIVALS-D1-C-S1",
              "ADJUDICATION_v1.dell1.md: D1-C-S1 (07:30Z) grades wc-1/wc-2 MET, wd-1 repeat NOT MET, wa-1 HELD; D1-C-S2 moves wd-1 to HELD; ADDENDUM 4 (wg-1 MET), ADDENDUM 5 (wh-1 MET) carry their own rows; wi-1 has no grade",
              "open ledgers: etfs-rivalfunds-ws23-dell1-20261009, etfs-rivalfunds-wi1-dell1-20261009 (L2 each); TO-MERGE-tc1 pending, b0b65368fb not in origin/box/sitez"
          ]
      },
      "disposition": "UNDER_INVESTIGATION",
      "spec_asserts": "round-close-check's MAY-CLOSE means every judgment criterion of the round is graded.",
      "world_is": "It matches a judgment criterion to any adjudication row of the project, so one early row reads as grading all eight.",
      "notes": "This seat closes round 28 on the artifacts, not on MAY-CLOSE. Owner of the instrument: .tools/round-close-check.py's lane (route via 0.0.0_AB_MSTR~DELL1 at the round-28 slug)."
  }
,
  {
      "id": "ETFS_RIVALS-D1-S14",
      "project": "ETFS_RIVALS",
      "fabric": "dell1",
      "surfaced_by": "0.7.0_AE_CloudOps~RV1",
      "surfaced_at": "2026-10-09T16:10Z",
      "one_line": "FOR THE COMP-RAIL OWNER: comp-find SILENTLY IGNORES a negative pathspec, so an agent told 'repo-wide search may resume except over <dir>' cannot comply by excluding -- the tool scans the restricted directory while the operator believes it is excluded; only POSITIVE scoping limits the corpus",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
          "status": "GROUNDED",
          "evidence": [
              "control run 16:09Z, term 'DENOMINATOR', two safe directories: (A) `comp-find --files 'DENOMINATOR' org/ref docs/architecture` -> 53 hit(s) across 513 file(s); (B) the SAME call plus ':!docs/architecture/**' -> 53 hit(s) across 513 file(s), byte-identical denominator; (C) positive scope `comp-find --files 'DENOMINATOR' org/ref` -> 1 hit across 27 file(s)",
              "B == A proves the exclusion had no effect; C != A proves the comparator is live and that positive pathspecs DO limit the corpus, so B's null result is the tool and not the test",
              "first seen 16:00Z on a different term ('SEAT_ROLES', org/ref, with and without ':!org/ref/**'): 6 hits / 27 files both ways",
              "CLAUDE.md rule 21: comp-find's DEFAULT corpus is `all` (tracked + untracked + gitignored minus a printed ephemeral floor), i.e. repo-wide unless positively scoped"
          ]
      },
      "disposition": "UNDER_INVESTIGATION",
      "spec_asserts": "CLAUDE.md rule 21 describes comp-find pathspecs without distinguishing positive from negative forms, and git pathspec semantics (which the rail's '--corpus' language borrows, including `git rc=128` for an out-of-worktree pathspec) admit ':!<path>' as an exclusion. An operator instruction of the form 'search may resume, except over <dir>' is therefore naturally executed as a negative pathspec.",
      "world_is": "The negative pathspec is accepted without error or warning and changes nothing: the directory is still scanned and its bytes still read. The exclusion fails OPEN and SILENTLY -- the most dangerous shape, because the denominator the tool prints looks authoritative and the operator has no signal. The only mechanism that limits the corpus is naming the directories to search positively.",
      "notes": "Owner to inform: the comp-rail / NFRA_COMPRAIL owner (docs/architecture/NFRA_COMPRAIL_PRD.md). Found while complying with a client-data prohibition relayed as 0.0.0_AB_MSTR~DELL1 msgs 2749 and 2768 via 2.0.0_SA_COO~V1 (msgs 2751, 2771), whose msg 2749 wording was exactly 'content search may resume, except over org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/'. This seat did NOT test the syntax against any restricted path -- the control was rehearsed on two harmless directories precisely because a fail-open exclusion would have performed the prohibited read. msg 2768's later wording, 'keep searches scoped to ETFS_RIVALS and infra paths', is already the SAFE positive form and needs no change. Suggested remedy for the owner: make comp-find either honour ':!' or REFUSE it loudly; a silently-dropped exclusion argument is the defect. No ETFS_RIVALS act depends on this row."
  },
  {
    "id": "ETFS_RIVALS-D1-S15",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-11T12:55Z",
    "one_line": "FALSE MAY-CLOSE: since 1.0.0_SA_CTO's fix efb0b41626 (06:18Z), `round-close-check.py --project ETFS_RIVALS --round 28` reads judgment=9 graded=9 verdict=MAY-CLOSE. Three of those nine J1s have no terminal grade from this seat: RIV-tc-1 is NOT MEASURED, RIV-wd-1 is HELD, and RIV-wi-1 has never been graded. The tool now counts any CVO row that MENTIONS an order's short id next to 'J1' as a grade. Round 28 must not be closed on this verdict.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~V1",
    "spec_asserts": "round-close-check.py docstring: every judgment criterion needs a row 'that names the criterion id' by a CVO-kind seat; GRADED is read as 'graded'. Spine L9: judgment criteria are graded at L9 by the CVO, never self-graded; L10 waits until every order of the round is terminal and every BLOCKING or ARMED row is dispositioned.",
    "world_is": "- Subject, box/dell1 @47962a23eb plus this seat's uncommitted row D1-C-S11 (which names no order slug), 12:5xZ: ROUND-CLOSE orders=21 judgment=9 graded=9 ungraded=0 verdict=MAY-CLOSE. Detail: TO-RIV-tc-1 J1 -> GRADED by D1-C-S3; TO-RIV-wd-1 J1 -> GRADED by D1-C-S1; TO-RIV-wi-1 J1 -> GRADED by D1-C-S8.\n- What those rows say: D1-C-S3 grades tc-1 J1 NOT MEASURED, because tc-1 was unmerged at the 10-09 run; D1-C-S7, S9, S10 and S11 keep it NOT MEASURED. D1-C-S1 grades wd-1 J1 NOT MEASURED, and D1-C-S2 moves it to HELD for the first page rendered with wf-1. D1-C-S8 says, verbatim, 'RIV-wi-1 J1 has no grade from this seat.' The tool reads that sentence as a grade.\n- Control, before the change: at 05:1xZ and 07:5xZ the same command at round 28 read graded=6 ungraded=3, listing these same three as UNGRADED. At that point orders were keyed by slug, so the short mentions did not match.\n- Mechanism: efb0b41626 reads seat-folder orders, and order['id'] now comes from <to_id> ('ETFS_RIVALS.TO-RIV-tc-1...'). The short form after '.TO-' ('RIV-tc-1...') and 'TO-'+short then enter the name pattern at :420-423. Any CVO row with 'J1' and 'TO-RIV-tc-1' or 'RIV-tc-1' anywhere in its JSON now grades it, whatever verdict the row states. The trap D1-C-S8 recorded (GRADED means named, not MET) has widened: a row that says it is NOT a grade now counts as one.\n- Also counted GRADED and not MET: wa-1 J1 (HELD, D1-C-S1/S2) and aw-1 J1 (NOT MET, D1-C-S4). With tc-1, wd-1 and wi-1, five of the nine round-28 J1s are not MET.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/round-close-check.py --project ETFS_RIVALS --round 28, box/dell1, 2026-10-11 12:5xZ (graded=9 MAY-CLOSE) vs 05:1xZ and 07:5xZ (graded=6, 3 UNGRADED)",
        ".tools/round-close-check.py :314 (id from to_id), :420-423 (name pattern); git log: efb0b41626 1.0.0_SA_CTO 2026-10-11 06:18",
        "surprise-channel/adjudications/ADJUDICATION_v1.dell1.md rows ETFS_RIVALS-D1-C-S1, S2, S3, S4, S8, S10, S11"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Disarm (2.0.0_SA_COO~V1): do not count round 28 closed on this tool's GRADED count. Read the verdict in each cited row. The disarm is done when the round-28 close cites per-criterion verdicts, or when the tool is fixed. Tool owner: 1.0.0_SA_CTO, author of efb0b41626, to rule. Suggested remedy: grade only on a row that DECLARES the criterion it grades (an 'adjudicates' field, which the selftest at :575 already uses) with a verdict value, never on a free-text mention. This seat's rows will name an order's full id only beside a terminal verdict, but older rows cannot be edited (append-only), so the fix belongs in the tool."
  },
  {
    "id": "ETFS_RIVALS-D1-W37-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~37",
    "surfaced_at": "2026-10-12T21:24Z",
    "one_line": "RIV-xc-1 frame_of: the sentence-initial word list (the a an in on over from between these this its it for with as at by) is matched case-insensitively, and every other capitalised token is <name>; so an all-caps token that spells a listed word (AT, IT, AS, BY) and a capitalised verb opening a sentence (Holds, Buys) both abstract to <name>, and two funds' frames can collide on shape alone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-xc-1 Interface 1 (round-29 cell text, ETFS_RIVALS_DECOMP): a token that begins with an uppercase letter and is not one of the sentence-initial words `the a an in on over from between these this its it for with as at by` is NAME-like. The text does not say whether the word match is case-sensitive, nor whether it is restricted to the first token of the sentence.",
    "world_is": "Built as a case-insensitive match (needed so that 'The' and 'Over' are excluded). Two results follow from the rule as written: frame_of('AT & T rose.') = 'at & <name> rose' (AT reads as the word 'at'), and frame_of('Holds 2 and 3 names.') = '<name> <n> and <n> names' (a capitalised verb is not on the list). A collision drawn on such a frame costs one correction whose reply stands; no grade changes. Measured in data/etfs/scripts/rivalfunds/ai_accounts.py frame_of, worktree wk-ETFS_RIVALS-37 at base d51a290175, uncommitted at filing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd data/etfs/scripts && python -m pytest -q rivalfunds/tests/test_riv_xc1_verdict_frame.py (worktree C:/tmp/wk-riv29-37, 2026-10-12 21:2xZ): 4 passed, after the expectations were set to the literal rule",
        "rivalfunds/ai_accounts.py frame_of, worktree wk-ETFS_RIVALS-37 at base d51a290175 (uncommitted at filing); the rule text is RIV-xc-1 interface 1 in the round-29 face"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "For the issuer to rule: whether the listed-word match should be case-sensitive or limited to the sentence's first token. No grade or prompt depends on the frame beyond one extra opening defect, so this is an observation, not a blocker. The cell's AC1 check passes as written under the literal rule."
  },
  {
    "id": "ETFS_RIVALS-D1-W35-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~35",
    "surfaced_at": "2026-10-12T21:30Z",
    "one_line": "RIV-xb-1 face says serp.classify_serp_attempt classes a 5xx as VENDOR; serp.py classes an HTTP status of 500 or more as TRANSPORT, so the 5xx branch of the client's own retry is unreachable. No effect on the policy built here: serp_search retries both kinds.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-xb-1 face (round 29, section 2 and the Measured line): 'serp.classify_serp_attempt classes a failure VENDOR (5xx or a vendor-error header), TRANSPORT (no HTTP status or a connection error) or CONFIG (a 4xx)'. serp.py's own docstring (classify_serp_attempt, :268-269) says 'kind VENDOR for a 5xx'.",
    "world_is": "data/find/dualbiz/scripts/serp.py:281-284: HTTP status None -> TRANSPORT; status >= 400 -> `CONFIG if 400 <= status < 500 else TRANSPORT`. So a real HTTP 5xx is TRANSPORT. VENDOR comes from an x-brd-status-code other than 200, an x-brd-error or x-brd-error-code header, or an empty body with a vendor header (:287-296). Because of :284, the 5xx clause of serp_brightdata_records' retryable test (:459-460, `kind == VENDOR and (captcha or 500 <= http_status < 600)`) cannot be true. Consequence here: none; serp_search retries VENDOR and TRANSPORT alike. Consequence for the failure text: a real 5xx reads 'SERP FAILED: TRANSPORT after 3 attempts', not VENDOR.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/find/dualbiz/scripts/serp.py@8a82ac76c1 :268-269 (docstring), :281-284 (code), :459-460 (dead 5xx clause)",
        "worktree C:/tmp/wk-riv29-35 at base 8a82ac76c1 (box/dell1), read 2026-10-12 21:2xZ"
      ]
    },
    "notes": "Recorded for the issuer; serp.py is out of this order's bounds and is not edited. The vendor client's owner decides whether the docstring or the code is the intent."
  },
  {
    "id": "ETFS_RIVALS-D1-W35-S2",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~35",
    "surfaced_at": "2026-10-12T21:30Z",
    "one_line": "serp_brightdata_records already re-attempts a captcha VENDOR failure twice inside the client, so the lookup-level retry built for RIV-xb-1 can make nine Bright Data requests for one search where the face's bound reads three.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-xb-1 face section 1: 'a result with status FAILED and failure.kind in (VENDOR, TRANSPORT) is retried, at most 2 retries (3 attempts)'. The face describes the client call as ONE call that the policy wraps (section 2: 'the default _call is the current body').",
    "world_is": "data/find/dualbiz/scripts/serp.py:396 (_PAGE_SLEEP) and :400 (retries: int = 2) and :459-463: inside serp_brightdata_records a VENDOR failure is re-attempted up to `retries` times when brd_error_code is 'captcha' (the 5xx clause is dead, see W35-S1), with no sleep between its attempts. serp_search (dramatic_move.py, this order) retries the whole client call twice with sleeps 1.0 and 2.0. Worst case per lookup search: 3 x 3 = 9 Bright Data requests for a captcha. The measured class in the face (HTTP 200, x-brd-status-code 502, expect_element) is not captcha and not 5xx, so the client does not retry it and the outer retry is its only retry. No test reaches this: every test injects _call.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/find/dualbiz/scripts/serp.py@8a82ac76c1 :396, :400, :459-463",
        "data/etfs/scripts/rivalfunds/dramatic_move.py serp_search in worktree C:/tmp/wk-riv29-35 (the RIV-xb-1 change, committed with this row)"
      ]
    },
    "notes": "Issuer to decide at the merge whether the outer retry should skip the captcha class, which the client already retries. Not changed here: the face fixes the policy and serp.py is out of bounds. Vendor spend is the concern; no live search runs in this cell (the face forbids one)."
  },
  {
    "id": "ETFS_RIVALS-D1-W35-S3",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~35",
    "surfaced_at": "2026-10-12T21:30Z",
    "one_line": "The package conftest replaces dramatic_move.run_for_day with a no-op in every test module that does not set REAL_DRAMATIC_MOVE = True. The face asks for the seam with the real run_for_day and does not name that flag; a new test that drives run_for_day silently exercises the no-op until the flag is set.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-xb-1 face section 1 (Checks) and section 4 AC2: the seam with the real neighbour run_for_day, exercised through serp_search with an injected _call.",
    "world_is": "data/etfs/scripts/rivalfunds/tests/conftest.py:31-32 (_no_live_dramatic_move_lookup): unless request.module.REAL_DRAMATIC_MOVE is True, run_for_day is monkeypatched to a no-op returning zero counts. The round29/checks file sits outside rivalfunds/tests, so it reaches the real run_for_day; a module inside the package does not. Measured: a first draft of the run_for_day test in rivalfunds/tests read candidates 0 and plan calls [] until the flag was set. The flag is set in test_riv_xb1_search_retry.py; no existing test was edited.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/tests/conftest.py@8a82ac76c1 :31-40",
        "pytest run of rivalfunds/tests/test_riv_xb1_search_retry.py in worktree C:/tmp/wk-riv29-35: 9 passed after the flag was set"
      ]
    },
    "notes": "Recorded for the round's test authors. The flag is the package's own mechanism, so no change is made to conftest.py (outside this order's paths)."
  },
  {
    "id": "ETFS_RIVALS-D1-W39-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~39",
    "surfaced_at": "2026-10-14T13:43:51Z",
    "one_line": "RIV-xc-2 rule 3, read as written, drops the colon of a stop-listed clause terminator; the cell's own example needs it kept",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-xc-2 rule 3: the tokens of FRAME_STOP are removed from the clause; the example 'Gamma Co stands out most: it was sold.' gives '<name> stands out:' (the colon survives).",
    "world_is": "Removing the token 'most:' by the rule as written also removes its colon, which gives '<name> stands out', not the example's '<name> stands out:'. The cell does not say where the colon goes. Implemented in ai_accounts.py frame_of step 3: a clause that ended in a colon keeps it on the last token that remains. With that, every example in the cell and check AC1 hold (1 passed, rc 0). The literal reading was reasoned from the token rule, not run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xc2_frame_family_check.py@ca6eedbb6d:78-80",
        "org/missions/D5/ETFS/ETFS_RIVALS/task-orders/ETFS_RIVALS.TO-RIV-xc-2.frame-families-and-stored-reason.md@ca6eedbb6d (section 1, rule 3 and the examples)"
      ]
    },
    "notes": "Judgement call by the worker. The CVO or the issuer should confirm the colon carry when the cell is re-read; the frame's shape depends on it."
  },
  {
    "id": "ETFS_RIVALS-D1-W39-S2",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~39",
    "surfaced_at": "2026-10-14T13:43:51Z",
    "one_line": "RIV-xc-2 does not say whether frame_still_shared is set when the one correction raises and the first reply stands",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-xc-2 step 5: a reply that STILL shares the family after the one correction is marked (frame_still_shared), not re-sent; shared_frame_with is stored whether or not the correction succeeded.",
    "world_is": "When the correction raises, the first reply stands and it still shares the family. The cell names the mark for 'after the one correction' and is silent on a correction that errored. Implemented: frame_still_shared is set, because the standing reply does share the frame; correction_error already records the failure (ai_accounts.py run_chain, still_shared). No test in this order exercises that path.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/ai_accounts.py (run_chain, the except branch and still_shared) at worktree wk-ETFS_RIVALS-39 HEAD ca6eedbb6d plus the uncommitted edit of this order",
        "org/missions/D5/ETFS/ETFS_RIVALS/task-orders/ETFS_RIVALS.TO-RIV-xc-2.frame-families-and-stored-reason.md@ca6eedbb6d (section 1, step 5)"
      ]
    },
    "notes": "Judgement call by the worker. A test for the errored-correction path would be an added assertion outside the cell's checks, so none was written."
  },
  {
    "id": "ETFS_RIVALS-D1-W41-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~41",
    "surfaced_at": "2026-10-14T14:02:22Z",
    "one_line": "The deploy packager does not stage data/mdpf/scripts/demque/, so in the deployed Lambda RIV-xe-1's _queue_state import fails and returns 'unreadable'; the ask path would then refuse every history-owed draw on the packaged function.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/etfs-pipeline/rivalfunds_package.py@c78a4c9722 STAGED tuple lines 33-43: staged are data/etfs/scripts/rivalfunds, lib/opal_naming.py, lib/trading_calendar.py, lib/research/identity, infra/logic/registry, org/standards/NAMING_SCHEMA.json, gold/etf_positioning_gold.py and data/find/dualbiz/scripts; a Grep of the file for 'mdpf|rivalfunds|data/' shows no data/mdpf entry",
        "rivalfunds_package.py@c78a4c9722 docstring line 17: the layer attached by the .tf carries pandas-pyarrow-requests only, so no other path supplies data/mdpf",
        "data/mdpf/scripts/demque/standing.py@c78a4c9722:79 read_state exists; the cell's reader works in the worktree only because the worktree carries data/ (AC2 6 passed, run from data/etfs/scripts)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-xe-1 interface (enrichment_bloomberg.py): _queue_state imports data.mdpf.scripts.demque.standing.read_state; the reader fails closed on ImportError (the cell's own words).",
    "world_is": "The packaged function's zip carries data/ only as data/find/dualbiz/scripts, so 'data.mdpf' is not found in the Lambda; the function-level catch returns 'unreadable', and every ask-mode draw refuses with 'queue state unreadable'. Fail-closed: no Bloomberg request, no spend. The switch RIVALFUNDS_HISTORY_OWED is OFF and this cell does not set it, so nothing is affected today. The test suite cannot see the gap because the worktree carries data/.",
    "notes": "Not fixed here: rivalfunds_package.py is outside this order's paths. Before the site-Z deploy of RIV-xe-1 (under 1.0.0_SA_CTO~Z's half) the issuer chooses between staging data/mdpf/scripts/demque/ (and whatever standing.py itself imports, not verified here) in STAGED, or redirecting the reader. A deploy-side import check would settle it."
  },
  {
    "id": "ETFS_RIVALS-D1-W42-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~42",
    "surfaced_at": "2026-10-14T14:05Z",
    "one_line": "RIV-xf-1 AC2 cannot pass as worded: request_plan(date) with no sink plans only the bloomberg_primary funds (7 of 13) with every gate on, so the check's expectation of the 13 funds in the plan fails once the two entries are gone (the base held 9: those 7 plus ACWI and IWM)",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/collector_bloomberg.py request_plan (base box/dell1, read at worktree wk-ETFS_RIVALS-42): docstring 'Without a sink s the issuer-first fallbacks cannot be checked, so the plan is the bloomberg_primary funds'; body sets wanted = universe_funds('bloomberg_primary') unless event funds is given",
        "measured in worktree C:/tmp/wk-riv-r30-42 after this cell's edits with RIVALFUNDS_LEG_ENABLE=1: request_plan('2026-09-29') funds = IDVZ, TXUE, BIDD, CGIC, INEQ, SCHY, PFOE (names 7); universe.funds() = 13; split_units(universe.funds()) is one unit at RIVAL_ROW_CAP (True)",
        "xf1_acwi_iwm_removed_check.py test_ac2 at this worker's post-edit tree: 1 failed, 'Right contains 6 more items, first extra item: PCLG'; the base run before the edit failed the same assertion with 'Right contains 4 more items' while the held set still had ACWI and IWM"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-xf-1 AC2 (cell section 4, check test_ac2): with every gate on, the holdings plan is the 13 funds in one unit, and no benchmark is queried on its own.",
    "world_is": "The no-sink holdings plan returns the bloomberg_primary funds only, 7 under every gate on. The 13-fund set is reached only through funds_for_day with a sink (issuer-first fallbacks), which the check does not call. The single-unit half holds. Removing the two entries cannot make the sinkless plan carry the six issuer-first funds, because request_plan is code outside this order's paths. Whether the served plan takes the sink path was not measured by this seat.",
    "notes": "Not worked around: the check and collector_bloomberg.py are outside this order's paths, and the expectation belongs to the issuer. The order stays open on AC2. Ruling needed from 2.0.0_SA_COO~V1 on whether AC2 reads the sink plan (funds_for_day) or the bloomberg_primary set, with 1.0.0_SA_CTO~DELL1 if the criterion changes."
  },
  {
    "id": "ETFS_RIVALS-D1-W40-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~40",
    "surfaced_at": "2026-10-14T14:02:24Z",
    "one_line": "RIV-xe-3 union reader resurrects a voided action: dramatic_move's actions-void-<revision> objects are read by load_actions as rows and never applied, so a void whose action sits in an older pull comes back under the union (the old latest-pull rule dropped it only by accident). price_series honors voids; the G5 reader does not.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~V1",
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-xe-3 cell (Interface): load_actions keeps every EVENT row from EVERY pull, de-duplicated on the action's own key. The cell names no void object and says every other function of the file is out of bounds.",
    "world_is": "The corporate_actions partition also holds dramatic_move VOID objects, actions-void-<revision>.parquet (dramatic_move.py:435-436 VOID_SCHEMA carries no row_kind, as_of or revision column; written at :463-468). price_series.py:216-256 (_voids, _actions) honors them and drops the named (revision, security_id) rows; gold_trade_schedule.py load_actions honors none. Probe (scratch, not committed): one action in pull r1, a void naming r1, a short pull r2 for the same security. The OLD reader returns ex_dates [2026-09-25] (r1 dropped by the latest-pull rule); the NEW reader returns [2026-06-01, 2026-09-25] with label r1+r2, so the voided r1 action is back in G5. Not measured against the live store (no S3 read).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/price_series.py@9a1ce314dc :216-256",
        "data/etfs/scripts/rivalfunds/dramatic_move.py@9a1ce314dc :435-436 and :463-468",
        "data/etfs/scripts/rivalfunds/gold_trade_schedule.py (worktree C:/tmp/wk-riv-r30-40, RIV-xe-3 edit, uncommitted at probe time) :983-1017",
        "scratch probe C:/tmp/wk-riv-r30-40/.scratch/void_probe2.py: OLD ex_dates ['2026-09-25'], NEW ex_dates ['2026-06-01', '2026-09-25'] label r1+r2"
      ]
    },
    "notes": "Form only. Whether load_actions applies voids is not a question the cell names and the CTO ruled the union; the issuer owns the merge and the xe-2 gate, so the disarm sits there. Not fixed by this worker: out of the cell's bounds."
  },
  {
    "id": "ETFS_RIVALS-D1-W40-S2",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~40",
    "surfaced_at": "2026-10-14T14:02:24Z",
    "one_line": "RIV-xe-3 cell names two row kinds (event, status) and gives no rule for any other row_kind; the worker applied the old latest-pull rule to every non-event row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-xe-3 cell (Interface): an EVENT row is kept from EVERY pull; a STATUS row follows the rule as it was. No rule is stated for a row whose row_kind is neither.",
    "world_is": "Producers write only event and status: enrichment_bloomberg.py:211 (status) and :233 (event); dramatic_move.py:257 (event). The rows that carry no row_kind are the void objects (dramatic_move.py:435-436); they reach the non-event branch with a NaN key and are dropped (scratch probe C:/tmp/wk-riv-r30-40/.scratch/void_probe.py: one row returned, the action). load_actions therefore reads every non-event row by the old rule (_is_event and the keep mask in gold_trade_schedule.py).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/enrichment_bloomberg.py@9a1ce314dc :211 and :233",
        "data/etfs/scripts/rivalfunds/dramatic_move.py@9a1ce314dc :257",
        "scratch probe C:/tmp/wk-riv-r30-40/.scratch/void_probe.py: OLD 1 row, NEW 1 row (the action; the void dropped by both)"
      ]
    },
    "notes": "Form only. No producer writes another kind today; the choice matters only for a future kind or a frame without the column."
  },
  {
    "id": "ETFS_RIVALS-D1-W40-S3",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~40",
    "surfaced_at": "2026-10-14T14:15:34Z",
    "one_line": "AMENDMENT 1 criterion AC4 cannot pass as written: its void names security_id 'a us equity' and must drop the 'A US Equity' rows, but price_series' normalisation (which the amendment says to reuse exactly) is case-sensitive, so the rows stay in both readers.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AMENDMENT 1 (order section 1) and check test_ac4: the void object names security_id 'a us equity' and the rows of pull 'full' for 'A US Equity' are dropped; the union reuses price_series._voids and the price_series normalisation exactly, without a copy.",
    "world_is": "price_series._norm_key (price_series.py:124-125) is strip and space-to-underscore, case-sensitive: 'A US Equity' gives 'A_US_Equity', 'a us equity' gives 'a_us_equity'. Scratch probe on the AC4 store (not committed): price_series._voids = {('full', 'a_us_equity')}; price_series._actions keeps ex_dates [2026-03-02, 2026-06-01, 2026-09-25]; load_actions keeps the same three (3 uris). The verbatim AC4 test therefore fails (1 failed) while the same void spelled 'A US Equity' drops the two rows (worker test test_ac4_mechanism_with_the_stored_key_spelling passes). dramatic_move.py:452-456 (void_rows) refuses a void whose revision and normalised security_id match no stored row, so no producer writes the lowercase spelling.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/price_series.py@9a1ce314dc :124-125 (_norm_key) and :223-234 (_voids)",
        "data/etfs/scripts/rivalfunds/dramatic_move.py@9a1ce314dc :452-456 (void_rows stored-row check)",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xe3_union_reader_check.py@d8ae1862ca :105-123 (test_ac4, void security_id 'a us equity' at :115)",
        "scratch probe C:/tmp/wk-riv-r30-40/.scratch/ac4_ps_probe.py: price_series and load_actions both keep ex_dates [2026-03-02, 2026-06-01, 2026-09-25]"
      ]
    },
    "notes": "Not fixed by this worker. A case-folded match would make load_actions honour more voids than price_series, which the amendment rules out. Needs the issuer's ruling: correct the AC4 void spelling in the check (the issuer's file, outside this order's paths) or rule case-folding for both readers. The order stays open on AC4 until then."
  },
  {
    "id": "ETFS_RIVALS-D1-S16",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~V1",
    "surfaced_at": "2026-10-14T14:43:03Z",
    "one_line": "An inferred split (actions-inferred-*) and Bloomberg's own row for the same split are two rows under the de-dup key (raw_event_type differs), so both survive and a price series or G5 flow can apply the split twice (CTO C1, msg 5612).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~V1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CTO half org/missions/D5/ETFS/ETFS_RIVALS/ledger/NEVER_WIDEN_R30_DEPLOY_CTO_HALF.md @35d1f02bc3, condition C1; CTO msg 5612",
        "price_series._actions (price_series.py:238-258) already reads EVERY object under corporate_actions/date=<D>/ (the inferred ones too) and applies every split row, so a Bloomberg row and an inferred row for one split already both apply on the chart; RIV-xe-3's union (gold_trade_schedule.load_actions, key security_id+event_type+raw_event_type+ex_date) extends the same exposure to G5 once deployed",
        "MEASURED 2026-10-14 ~14:1xZ (S3 LIST+GET, read-only): gold/corporate_actions holds 11 objects, all plain Bloomberg pulls (actions-<rev>); 0 actions-inferred-*, 0 actions-void-*; so no double application exists today"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "One split is one adjustment: a split the lookup finds on the web (dramatic_move.run_for_day, live since the wi-1 deploy 2026-10-09) and the same split Bloomberg later reports adjust a series once.",
    "world_is": "Both rows survive the readers. The inferred row's raw_event_type is the lookup's own text and Bloomberg's is the vendor's, so the (security_id, event_type, raw_event_type, ex_date) key never collides across the two sources. No inferred object exists in the live store today (measured), so the hazard has not fired.",
    "notes": "DISARM (this seat's, per CTO C1: no actions-inferred-* object stays until the fix deploys). There is no switch that stops the live lookup short of an environment-key change (a deploy outside the r30 plan), so the disarm is DETECT AND VOID: each drive tick lists gold/corporate_actions/date=* read-only; an actions-inferred-* object found is voided the same tick with `python -m rivalfunds.dramatic_move void --sink s3 --revision <rev> --security-id <sid> --reason <text>` through a CloudOps seat on this seat's word (append-only; the r30 pin makes load_actions honour voids, price_series already does). The lookup may re-find the next day; the loop repeats until the fix deploys. FIX: a round-31 cell, Bloomberg wins on (security_id, event_type, ex_date) in both load_actions and price_series; arms: a double reads one adjustment, an inferred-only row applies, today's store reads DELTA=0 (CTO msg 5612)."
  },
  {
    "id": "ETFS_RIVALS-D1-S17",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~RV",
    "surfaced_at": "2026-10-15T18:29:37Z",
    "one_line": "The 2026-10-15 page served CGIC and SCHY as not-updated (11 of 13 funds): the 11:04Z Bloomberg capture returned only '#N/A Requesting Data...' (1 row), its good retry landed at 14:35Z after the 13:00Z sweep built the page, and CGIC and SCHY report one day behind the other bloomberg_primary funds, so they fell to a 2 trading-day lag against the 1-day allowance.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-15/manifest.json (read 18:2xZ): funds_updated 11, funds_total 13, CGIC and SCHY latest_report 2026-10-12 vs expected 2026-10-14, lag 2 vs allowance 1 (row W5-S28), generated_at 2026-10-15T13:09:27Z, runtime etfs-rivalfunds-daily-lambda",
        "s3://opal-data-etfs/bloomberg/etfs/bronze/holdings/date=2026-10-15/: batch-20261015T110336Z-2026-10-14 holds 1 row ('#N/A Requesting Data...'), batch-20261015T143507Z-2026-10-14 holds 758 rows (landed 14:35Z)",
        "the date=2026-10-14 manifest (generated 2026-10-15T14:41:45Z) reads 13 of 13 with CGIC and SCHY latest_report 2026-10-13 and the other eleven 2026-10-14, so those two sit one day behind on a good capture",
        "no manifest for 2026-10-06..2026-10-14 pages shows a not-updated fund: the 10-08 hold of the same two funds was the signed-out Terminal (Z-S76)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A page day's funds all read updated when the 11:00Z capture lands; the 13:00Z sweep is the retry of the same day.",
    "world_is": "When the 11:00Z Excel capture fails, the 13:00Z sweep builds from the previous day's capture and CGIC and SCHY, one day behind by their source, exceed the freshness allowance. The retry that landed at 14:35Z reached no scheduled build for the 2026-10-15 page. Why Excel returned '#N/A Requesting Data...' is not determined by this seat (owner 0.0.3_BG_BBGTerminal).",
    "notes": "Read-only finding. Nothing here was republished. The next scheduled run is the page's next build; no round 31 is cut (project parks after round 30). Ruling needed only if Andrew wants a later same-day sweep after a failed 11:00Z capture; that is a new build, not this round."
  },
  {
    "id": "ETFS_RIVALS-D1-S18",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~RV",
    "surfaced_at": "2026-10-15T18:29:37Z",
    "one_line": "TXUE's two AI items of 2026-10-15 are served as Grounding FAIL: after the one allowed correction the model (gpt-5.4, prompt a1-chain/8) still wrote fact ids such as [C-R30-worst1] into text, observed and inferred (the wording check counts an id as the period code it contains) and wrote 'listed 30 day trades', which the figure check reads as an uncited figure.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/gold/research_hypotheses/date=2026-10-15/research_hypotheses-20261015T130018Z-ai.parquet: TXUE activity_30d and direction_verdict grounding FAIL, input_manifest corrections 1 each, model_version gpt-5.4",
        "data/etfs/scripts/rivalfunds/ai_accounts.py wording_check (:480-502) and _figures/_PERIOD_NAME_RE (:238-258): 'the last 30 days' is exempt, '30 day trades' is not; _figures on the stored inferred text returns ['$7.7 million','30','32.42']",
        "the same stage graded 13 of 13 PASS on 2026-10-12, 2026-10-13 and 2026-10-14 (sweep_read.py, prompt a1-chain/8 each day); 2026-10-15 is the first sweep on pin ea0e5025ac, and the r30 cells' diffs (xc-2 9cdb19164d reads) touch the frame and stored-reason path, not wording_check, _figures or the correction call",
        "the FAIL is shown on the page as 'Shown for audit, not a pass' (render.py :1743-1746), not served as a pass"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-aw-1: an AI account names its periods in words and cites every figure; one correction per item.",
    "world_is": "The checker did its job. The model did not follow the one correction on two TXUE items; the prompt's citation format ([id] in text) and the wording rule against ids in text pull against each other, and 24 of 26 items passed. Changing the model does not by itself change that pull.",
    "notes": "Not fixed by this seat: ETFS_RIVALS parks after round 30 and no round 31 is cut without Andrew. Whether to move the writer to another model is Andrew's call (his word 'GPT6 astra' carries no verified model id); a model change is a code or Terraform env change through a CloudOps seat."
  },
  {
    "id": "ETFS_RIVALS-D1-S19",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~RV",
    "surfaced_at": "2026-10-15T20:32:33Z",
    "one_line": "proof-of-spec-check's alignment limb reads only decompositions/ETFS_RIVALS_DECOMP.md, so a cell that lives in a round file (ETFS_RIVALS_DECOMP.round<N>.md) is reported as 'does NOT exist' and 11 task orders of this project read INVALID on a valid cell reference.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/proof-of-spec-check.py <instance> --governing-order <order> on the pending orders cb-1, dr-1, eg-1, gd-1, gf-1, gt-1, ln-1, nf-1, nm-3, rp-2, su-2 (2026-10-15 ~20:1xZ): each prints 'VIOLATION: alignment: cell_ref RIV-<id> ... does NOT exist in org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md'",
        "the project's decompositions folder holds 12 files (ETFS_RIVALS_DECOMP.md plus round1..round11); 146 distinct cell ids across them, read by deliverables/2.0.0_SA_COO~RV/round30/build_completion_report.py",
        "the 36 other pending orders read VALID under the same checker, so the gap is the cell lookup, not those instances"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A criterion's cell_ref resolves when the cell exists in any of the project's decomposition documents.",
    "world_is": "The alignment limb resolves cell_ref against the one named decomp_ref.doc. Eleven instances whose cell was moved to a round file read INVALID, so those orders cannot be flipped complete and the completion report lists them as not terminal-with-proof.",
    "notes": "Not fixed by this seat: the checker is not this project's. CTO ruling msg 6215: keep the 12 pending orders as they are, flip none without a VALID instance, file this row. iam-1 is the twelfth pending order and fails on schema (spec_ref group, artifact kind), a different cause."
  },
  {
    "id": "ETFS_RIVALS-D1-W43-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~43",
    "surfaced_at": "2026-10-15T21:17:29Z",
    "one_line": "RIV-ya-1's chart reader (price_series.series) applies the precedence rule to the actions frame that load() windows by object date partition, so a Bloomberg split whose partition lies outside the chart window is not seen: an inferred split of the same key inside the window then applies alone, not the Bloomberg ratio, and the cell's 'whatever the two ratios' claim holds only for the rows both readers see",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/price_series.py _actions at base 1af8b0dba8 line 246: `if m and lo <= m.group(1) <= hi and u.endswith(\".parquet\") and not _is_void_uri(u)` (the partition date filter over the window's lo and hi)",
        "data/etfs/scripts/rivalfunds/price_series.py load at base 1af8b0dba8 line 261: `return series(g4, g1, keys, start, end, actions=_actions(s, lo, hi))`, so series() sees only the windowed frame",
        "data/etfs/scripts/rivalfunds/gold_trade_schedule.py load_actions at 1af8b0dba8 line 986 lists EVERY corporate_actions object (no date window), so the G5 reader pairs across all partitions while the chart reader pairs within the window",
        "the round-31 check ya1_bloomberg_wins_check.py test_ac2 builds both rows in one frame passed straight to series(), so it cannot see the windowing"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-ya-1 interface item 2: the same rule over the actions frame before _adjustments, so a Bloomberg split and an inferred split of the same ex_date apply ONCE (the Bloomberg row) whatever the two ratios.",
    "world_is": "The rule is applied as specified to the frame series() is handed. load() hands it the object partitions dated inside [start, end], so a pair split across the window edge is not paired by the chart. No inferred object exists in the live store today (cell measured 0), so the case has not arisen; the G5 reader and the chart reader can disagree on which pairs exist.",
    "notes": "Not edited (price_series.load is outside this order's paths for a windowing change). Owner of the call: 2.0.0_SA_COO~RV at the drain; the choices are to read the corporate_actions prefix unwindowed for the chart's precedence pass (the G5 reader's shape) or to accept the window edge with the disarm's detect-and-void. The worker's pairing is over the frame it is given, as the cell words it."
  },
  {
    "id": "ETFS_RIVALS-D1-W44-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~44",
    "surfaced_at": "2026-10-15T21:16:48Z",
    "one_line": "The rivalfunds suite is not a clean regression net at base: 56 of the suite's tests fail on box/dell1 base (1af8b0dba8) before any RIV-yb-1 edit, so the cell's 'report the final line' reads red for reasons outside its two code sites.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd data/etfs/scripts && python -m pytest -q -p no:cacheprovider --color=no rivalfunds/tests on the worktree at HEAD 1af8b0dba8 with ai_accounts.py and ai_client.py restored to HEAD: '56 failed, 992 passed, 7 skipped' (.scratch/base_run.txt in the worker worktree)",
        "the same suite after the RIV-yb-1 edits with tests/test_r6ap1_ai_stage.py left at HEAD: '57 failed, 993 passed, 7 skipped'; the 56 base failures are unchanged and the one addition is recorded as ETFS_RIVALS-D1-W44-S3",
        "failing files include test_g6_gics_join.py, test_hp1_home_producer.py, test_i1_identity.py, test_i2_issuer_alias.py, test_r5b1_g1_windowed.py, test_riv_we1_claimed_as_of.py, test_r6ap1_ai_stage.py::test_policy_and_environment_split_and_committed_copy_is_current (outside the two client modules and the default-model string)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The rivalfunds suite (pytest from data/etfs/scripts) is the regression net for an AI-writer change: its final line is the cell's regression evidence, and a change that touches only the client request shape leaves the rest of the suite as it was.",
    "world_is": "At the base commit the suite already reads 56 failed and 992 passed; the failures sit in grouping, identity, windowed-build, policy-generation and claim-as-of tests that do not touch the AI client. The 56 pre-existing failures are unchanged by the RIV-yb-1 edits; the one failure the edits add is recorded as ETFS_RIVALS-D1-W44-S3.",
    "notes": "Not fixed by this seat: the 56 failures are outside RIV-yb-1's paths and the cell does not widen to them. The issuer decides whether the net is repaired before the merge."
  },
  {
    "id": "ETFS_RIVALS-D1-W44-S2",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~44",
    "surfaced_at": "2026-10-15T21:16:48Z",
    "one_line": "The worker worktree is a sparse checkout that omits org/surprise_channel: the investigation item schema the row gate names is tracked and indexed but absent on disk, so a worker cannot read it by path.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git config --get core.sparseCheckout in C:/tmp/wk-riv-r31-44 returns 'true'; ls org/surprise_channel returns 'No such file or directory'; git ls-files org/surprise_channel lists 43 indexed files",
        "git show HEAD:org/surprise_channel/schemas/investigation_item.schema.json reads the schema at 1af8b0dba8; git status shows no deletion of it, so the omission is the sparse cone, not a removed file",
        "the first-act check 'test -d org && test -d .tools && echo TREE-OK' passes, because org/ and .tools/ exist; the omission is below org/"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A worker worktree carries the org/ paths its task order names, and the schema that grades a surprise row is readable from the worktree by path.",
    "world_is": "The worktree carries org/missions/D5/ETFS and .tools but not org/surprise_channel; the schema was reachable only through git show at HEAD. This worker read the schema from HEAD to choose the enum values and did not alter the sparse setting.",
    "notes": "Not fixed by this seat: the sparse-checkout setting belongs to the worktree's creator, and the cell's write surface does not include it. The row gate (.tools/surprise-row-gate.py) reads the committed index, so the row itself is unaffected."
  },
  {
    "id": "ETFS_RIVALS-D1-W44-S3",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~44",
    "surfaced_at": "2026-10-15T21:16:48Z",
    "one_line": "BLOCKING: RIV-yb-1's required change makes data/etfs/scripts/rivalfunds/tests/test_r6ap1_ai_stage.py::test_rest_client_request_shape fail, and that file is not in the order's <paths>, so the fix cannot land under this grant.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "rivalfunds/tests/test_r6ap1_ai_stage.py lines 109-110 at HEAD 1af8b0dba8 assert the body {model: 'm', messages, response_format, temperature: 0.2}; with the RIV-yb-1 RestClient.chat the model 'm' is not a gpt-5 model and the key is omitted, so the assertion fails",
        "the order's <paths> lists data/etfs/scripts/rivalfunds/ai_accounts.py, ai_client.py, tests/test_riv_yb1_model.py and the investigation file; test_r6ap1_ai_stage.py is not among them, so the worker left it at HEAD and did not commit it",
        "cd data/etfs/scripts && python -m pytest -q -p no:cacheprovider --color=no rivalfunds/tests with the RIV-yb-1 edits and test_r6ap1 at HEAD: '57 failed, 993 passed, 7 skipped' (base 56 failed, 992 passed)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's write grant (<paths>) admits every file the cell's required change must touch, so the cell lands without a file outside its grant.",
    "world_is": "The one-line fix is to drop the temperature key from the expected body of test_rest_client_request_shape (the cell's own rule: temperature is sent only for a gpt-5 model, and the test uses 'm'). The file is outside the grant, so the worker did not commit it and the rivalfunds net reads 57 failed until the issuer admits the path or applies the one-line fix.",
    "notes": "Blocking on the regression net only: AC1 and AC2 pass with the grant as written. The issuer adds data/etfs/scripts/rivalfunds/tests/test_r6ap1_ai_stage.py to <paths> (or applies the fix at the merge) before the net reads clean. The worker did not override the grant."
  },
  {
    "id": "ETFS_RIVALS-D1-S20",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~RV",
    "surfaced_at": "2026-10-17T04:30:00Z",
    "one_line": "OBSERVATION: two securities in the rivalfunds universe carry a Bloomberg key with no yellow key ('HAL US', 'VLO US'), so no close is ever returned for them and each stays owed on 237 of 237 dates after batch rv-bf365-20261017.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO~RV/deliverables/backfill_20261017/owed_after_rv-bf365_20261017T04Z.csv @bc1c08e456: security_bloomberg 'HAL US' and 'VLO US' owed on 237 dates each outside 2026-09-29..2026-10-15, the same count as SBER RM and other never-priced keys",
        "every other US key in the same file ends in ' Equity' (e.g. 'SPCX US Equity', 'JAN US Equity')"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Every security_bloomberg in gold security_universe is a full Bloomberg key (ticker, exchange, yellow key) the market and history readers can ask for.",
    "world_is": "Two keys are 'HAL US' and 'VLO US' with no yellow key; ORDER 2 step 1 asks them and Bloomberg is expected to refuse them, so Halliburton's and Valero's curves stay empty until the key is repaired at its source (the holdings key mapping), not in the backfill.",
    "notes": "Found reading the post-backfill owed set for Andrew-direct 'completely filled'. Not fixed here: the producer of the key is the holdings mapping, a cell for the round-N list."
  },
  {
    "id": "ETFS_RIVALS-D1-W45-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~45",
    "surfaced_at": "2026-10-17T04:51:06Z",
    "one_line": "The rivalfunds suite is not clean at the RIV-za-1 base: two budget tests fail on the shipped bbg_budget.json (daily_ceiling_rows 400000), which the tests' own assertions do not accept; neither test is in RIV-za-1's <paths>",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "pytest -q rivalfunds/tests from data/etfs/scripts in worktree C:/tmp/wk-riv-r32-45 (HEAD 3e426f83ad plus RIV-za-1): final line '2 failed, 1061 passed, 6 skipped in 97.72s'; the two FAILED ids are test_r15bf1_market_range.py::test_budget_remainder_refuses_and_check_points_names_it and test_r9cb1_bbg_budget.py::test_shipped_config_keeps_a_reserve_below_the_measured_exhaustion",
        "the same two tests run alone also fail: test_r9cb1_bbg_budget.py:100 'assert cfg[\"daily_ceiling_rows\"] < 175000' reads 400000; test_r15bf1_market_range.py:90 'assert bb.remaining() == 137' reads 250137",
        "git show HEAD:data/etfs/scripts/rivalfunds/bbg_budget.json at 3e426f83ad: daily_ceiling_rows 400000, production_reserve_rows 30000; bbg_budget.py and that json are unchanged in the RIV-za-1 diff (git status: only enrichment_bloomberg.py and the new test file)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The round-32 regression net reads clean after a cell: the rivalfunds suite's final line carries no failure, and the shipped budget config keeps a reserve below the measured exhaustion (test_r9cb1 asserts a daily ceiling under 175000).",
    "world_is": "The committed budget config carries a 400000-row daily ceiling, and the two tests' expected values (a ceiling under 175000; 137 points remaining) match no committed config. Whether the ceiling was raised on purpose (the tests are stale) or lowered back (the config is wrong) is not visible from the code read.",
    "notes": "Not edited: bbg_budget.json and both tests are outside this cell's <paths>, and the cell's own tests pass (6 of 6). The issuer names which side is right at the merge; the owner of the budget ceiling is not named in the code. Owner to be named by 2.0.0_SA_COO~RV."
  },
  {
    "id": "ETFS_RIVALS-D1-S21",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~RV",
    "surfaced_at": "2026-10-17T06:25:00Z",
    "one_line": "OBSERVATION: the disarm statement for ETFS_RIVALS-Z-S84 and Z-S85 (ARMED on site Z, disarm_owner 2.0.0_SA_COO~V1, whose lane this seat holds) -- what this lane stops now, and the part of the disarm that is a served-page act it cannot take alone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S84 and Z-S85 read from origin/box/sitez org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md (fetched 2026-10-17 ~06:2xZ), relayed by 0.0.0_AB_MSTR~DELL1 msg 7372",
        "this lane holds ~V1's issuer seat: CTO ruling @f8191183f6 (drive log org/tier1_exec/2.0.0_SA_COO~RV/drive_log_20261015T21Z_desktop-hk1uu7n.md)",
        "the held-tr writer (RIV-za-1, @27ec89ad2a) asks _blp_historical_data(batch, fields, day, day) per date, the same historical request the BDH checks in Z-S85 grade as the correct values"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "An ARMED row is disarmed the same turn by its disarm_owner.",
    "world_is": "Disarmed by this lane now: (1) no ad hoc publish or republish of the rivalfunds page by 2.0.0_SA_COO~RV until the venue-date fix lands; (2) Z-S84's read-side fix shape is withdrawn by Z-S85 and is not cut; (3) ORDER 3 act 3 (held-tr publish) stays behind its CTO half, and its rows are historical-request closes per date, not the 11:00Z NYSE-T-1 snapshot. NOT disarmable by this lane alone: the page already serves the shifted non-US closes, and the next scheduled chain (2026-10-19 11:00Z, the first trading day) serves them again; holding that chain or serving it with a stated caveat moves served output, so it is routed to 1.0.0_SA_CTO~DELL1 with the fix cell (each close filed under its own venue's trading date, the affected history re-sourced by historical request).",
    "notes": "The disarm closes when the fix cell is merged and deployed or the CTO rules the 10-19 chain. Measured figures in Z-S85 are 0.0.3_BG_BBGTerminal's, not re-measured here."
  },
  {
    "id": "ETFS_RIVALS-D1-W46-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~46",
    "surfaced_at": "2026-10-17T06:44:24Z",
    "one_line": "Order RIV-zb-1 says three test files read eb.MARKET_HIST_FIELDS and follow the new value; rivalfunds/tests/test_r12pk1_parsekey_join.py::test_historically_answered_identifier_key_still_gets_its_parsekey fails at its line 67, which pins the separate PARSEKYABLE_DES-only pass the cell removes.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/tests/test_r12pk1_parsekey_join.py@7d385aab5f (line 67: assert [f for secs, f in calls] == [['PARSEKYABLE_DES']])",
        "worktree wk-ETFS_RIVALS-46 after the RIV-zb-1 change: pytest -q rivalfunds/tests -> FAILED test_r12pk1 ... one PARSEKYABLE_DES-only request, never a Bloomberg key"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-zb-1 interface (3): the reference request is sent for EVERY security of a past partition; the separate parsekey-only pass for historical identifier-keyed securities is no longer needed. Section 2: the three files that compare a stub's fields to eb.MARKET_HIST_FIELDS 'read the constant, so they follow the new value'.",
    "world_is": "The test asserts exactly one reference call whose fields are ['PARSEKYABLE_DES'] on a partition where a bloomberg-keyed security (NBIS US Equity) also needs a reference descriptor request, so the call-shape pin cannot hold under the rule. The file is outside this cell's write paths and is unamended; the test's other assertions pass.",
    "notes": "Amend line 67 at merge (the identifier-keyed security's parsekey is asserted on its one reference request). The parsekey_points == 2 and as_of_source_counts assertions in the same test still hold."
  },
  {
    "id": "ETFS_RIVALS-D1-W46-S2",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~46",
    "surfaced_at": "2026-10-17T06:44:24Z",
    "one_line": "Three history-owed tests fail on fixtures that let the daily pull's historical answer carry CRNCY: test_r27tw1_history_owed_leg.py::test_print_sends_and_writes_nothing_more, ::test_ask_lands_one_object_per_date_with_price_date, and test_r28tc1_topup_currency_and_page_day.py::test_a_security_priced_in_this_run_is_never_looked_up.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/tests/test_r27tw1_history_owed_leg.py@7d385aab5f (historical stub: if fields == eb.MARKET_HIST_FIELDS returns {f: 10.0 for f in fields}; reference stub returns {})",
        "data/etfs/scripts/rivalfunds/tests/test_r28tc1_topup_currency_and_page_day.py@7d385aab5f (same stub shape; reference returns {} except CRNCY for ['CRNCY'])",
        "worktree wk-ETFS_RIVALS-46 after the change: 'HISTORY OWED: owed 6 units, 3 securities, 2 dates; asked 0 (request off); currency lookups 3 (not sent); carried 6'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-zb-1 (2)-(3): a past partition's price group is the historical answer dated D (PX_LAST and total return only); every descriptor, CRNCY included, comes from the reference request. Section 2: these three files 'read the constant, so they follow the new value'.",
    "world_is": "Each fixture answers the daily pull's own historical request with every field of MARKET_HIST_FIELDS, so under the old seven-field group the answer carried CRNCY. Under the two-field group the answer carries no CRNCY; the reference stub returns {} for descriptors, the G4 currency is NULL, and the history-owed currency lookup runs (three lookups in r27tw1; D1 US Equity looked up in r28tc1). The fixtures encode the old rule and are outside this cell's write paths; unamended.",
    "notes": "The fixtures need the reference stub to return CRNCY for the daily pull's securities, or the test needs its expectation restated. Either edit is the issuer's at merge."
  },
  {
    "id": "ETFS_RIVALS-D1-W46-S3",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~46",
    "surfaced_at": "2026-10-17T06:44:24Z",
    "one_line": "rivalfunds/tests/test_r10eg1_refuse_empty.py::test_one_usable_lands fails: its reference stub files a PX_LAST for AAA on a past partition (DATE 2026-10-02), which the rule never files, so the revision is REFUSED (0 of 2 usable) where the test expects OK.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/tests/test_r10eg1_refuse_empty.py@7d385aab5f (answer lambda returns {PX_LAST: 5.0} for AAA only; DATE = 2026-10-02 is a past partition against the run date)",
        "worktree wk-ETFS_RIVALS-46 after the change: pytest -q rivalfunds/tests -> FAILED test_one_usable_lands - assert ('REFUSED' == 'OK'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-zb-1 (3) and (5): the reference request for a past partition never carries the price group and the reference PX_LAST is never filed under a past partition; the all-empty refusal (RIV-eg-1) counts a row with descriptors as usable, as today.",
    "world_is": "The test's one usable row is a reference PX_LAST on a past date. Under the rule that row has no descriptor and no price, so the whole revision is REFUSED. The test pins the old rule, sits outside this cell's write paths, and is unamended.",
    "notes": "At merge the test's usable row should carry a descriptor (for example GICS_SECTOR_NAME) rather than PX_LAST."
  },
  {
    "id": "ETFS_RIVALS-D1-W46-S4",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~46",
    "surfaced_at": "2026-10-17T06:44:24Z",
    "one_line": "rivalfunds/tests/test_r7nm2_security_name.py::test_past_date_historical_request_excludes_the_name_and_still_lands_historical fails (PARTIAL): it asserts the past-date historical request asks the ten-field set and that no reference request is sent ('no pull expected').",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/tests/test_r7nm2_security_name.py@7d385aab5f (line 42: reference stub raises AssertionError 'no pull expected'; line 45: set(asked['fields']) == set(TEN))",
        "worktree wk-ETFS_RIVALS-46 after the change: pytest -q rivalfunds/tests -> FAILED test_past_date_historical_request_excludes_the_name ... assert ('PARTIAL' == 'OK'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-zb-1 (2)-(3): the historical request for a past partition asks PX_LAST and total return alone, and the reference request is sent for EVERY security of a past partition (descriptors).",
    "world_is": "Under the rule the historical request asks two fields (the set-equality assertion fails) and the reference request is sent for the security, which the test's stub refuses, so the batch failure returns PARTIAL. The LONG_COMP_NAME-not-asked assertion still holds. The test pins the old rule, sits outside this cell's write paths, and is unamended.",
    "notes": "At merge the historical-field assertion restates to PRICE, and the no-pull stub becomes a descriptor response."
  }
]
```
