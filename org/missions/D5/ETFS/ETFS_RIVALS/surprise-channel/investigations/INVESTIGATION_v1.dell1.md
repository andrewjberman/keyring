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
  }
]
```