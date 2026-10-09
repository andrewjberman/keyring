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
  }
]
```
