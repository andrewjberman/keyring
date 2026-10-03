# AMGT_HARVST ROUND 37 -- L8 COMPILE + L9 -- bbg limb 2a MET per run (13 runs, window pass rate 13/14); ft limb (1) has no route (an ENDPOINT question); 23 rows dispositioned; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~19:2xZ
**Input:** `2.0.0_SA_COO~H`'s `round37/ROUND37_DRAIN_END_PACKET.md` @`4162e8837b` (7,020 B, read to EOF), msg 28667. **8 of 8 orders are
terminal**: aj-1, 2, 3, 5, 7 and 8 are complete; aj-4 and aj-6 are CANCELLED.

## 1. Limb 2a -- graded by this seat on the grader's output (ruling 8)

**Ruling 8** (decomposition section 50.1): "the grader grades limb 2a PER RUN: MET when a run inside a monitor window has every
presented challenge non-void and passed. A failed run elsewhere does not void a passing one; it is printed as the window pass rate."

**The instrument, read by this seat.** `lib/opal_data_harvest/load_window_grade.py`:
- `is_void` (:196-204) voids a challenge if ANY minute in [presentation - 2 min, resolution + 2 min] is not `clean`;
- `minute_state` (:93-102) reads a minute as `void` when it carries hardware input, and as `unmonitored` when no window covers it.

So a MET run is a fully monitored, untouched solve. That is the conservative direction.

**The run** `close_load_window_grade_20261002T1838Z.json` (18:38Z, rc 0) covers three windows. Window 1 (10-01 14:02-14:48Z) is void
whole (no per-minute data). Window 2 (14:49Z-04:03Z) has 267 void minutes; window 3 (06:52Z-18:35Z) has 163.

| pub | runs (in window) | challenged runs in window | MET | NOT-MET | limb 2a (this seat) |
|---|---|---|---|---|---|
| bbg | 182 (88) | 36 | **13** (every challenge non-void and passed) | 23 = 22 void + **1 non-void failed** (`20261002T065754Z`, Z-S64; UNCLASSIFIED, ruling 8c) | **MET**, window pass rate **13/14 = 0.9286** |
| wsj | 100 (79) | 0 | -- | -- | MET-BY-ABSENCE |
| barrons | 104 (89) | 0 | -- | -- | MET-BY-ABSENCE |
| ft | 22 (12) | 0 | -- | -- | MET-BY-ABSENCE |
| sa | 111 (47) | 0 | -- | -- | MET-BY-ABSENCE |

- **bbg.** This supersedes this seat's v48 NOT-MET (Z-C-S60/S61), which was read at the round-36 grain before ruling 8 set the
  per-run grain. 22 of 36 challenged runs fell in void minutes: they were neither passed nor failed, and are not counted.
- **The other four.** MET-BY-ABSENCE means no challenge was presented at load inside a window. It is not a challenge passed
  (ABSENT != EXERCISED), so (2b) stays OPEN for wsj, barrons, ft and sa.

## 2. FWD-11 -- NOT REALIZED

| pub | (1) robust auth | (2a) | (2b) |
|---|---|---|---|
| bbg | met (r33) | **MET** (this compile) | PASS-FIXTURE |
| wsj, barrons | MET (r34) | MET-BY-ABSENCE | OPEN |
| ft | **NOT MET: no route exists** | MET-BY-ABSENCE | OPEN |
| sa | not graded | MET-BY-ABSENCE | OPEN |

**The ft route census (packet section 4) is complete as measured.** Each route has its own row:
- the NopeCHA Token API is discontinued (Z-W92-S18);
- NopeCHA's hCaptcha recognition is not offered (Z-S66);
- the NopeCHA extension did not clear the challenge in 150 s (Z-W90-S21), and that attempt was NOT input-quiet (7,042 hardware
  events), so it is not even a clean unattended reading;
- Ocilar answers 503 (Z-W92-S19);
- hand sessions die at 24 and 75 min under keep-alive (Z-W92-S20, Z-W92-S12).

ft stays OFF (STOP_FT). **This is the CTO's ENDPOINT question** (packet 6.1: (a) a qualified wait to the Ocilar re-check on
2026-11-01, (b) another solver, (c) accept ft at its depth). (a) and (b) need Andrew's word, carried as Z-C-S62.

**Vendor egress, read:**
- NopeCHA is VEW-1 (`org/ref/VENDOR_EGRESS_WHITELIST.yaml`, standing).
- Ocilar is not listed. Its one call (aj-6, ~13:45Z) rode Andrew-direct ~13:3xZ ("bETTER IDEA, LETS USE A NEW SOLVER", amendment
  `acec34f084`), so it was a per-use word, as the law requires.

## 3. Served gold and the served page, re-read by this seat

- The served `/timeline/day` reads gold rebuild #5: `BA_US_Equity/timeline/day/2026-09-08` serves 6 rows, 6 of 6 with a headline
  ("Everything to Know About the Boeing Jet That Overshot a Miam...").
- The answer times are 200 x3: cold 18.0 s, then 10.5 s and 0.5 s (DSGN v30).
- The served chatter rankings at as_of 2026-10-02 are committed generations:
  - `trending/chatter` SERVED, 1 row;
  - `breakout/chatter` EMPTY, "NO_SIGNAL_IN_WINDOW 190 of 191", a successful ranking with no members.

## 4. DISPOSITIONS (23 rows)

| row | disposition | grounds |
|---|---|---|
| Z-S64 (bbg non-void fail, ARMED) | DISMISSED_WITH_REASON | disarmed by its owner (Z-S65: aj-5 @`7b3800219d` records every solve, captures a failed one and retries once). The run stays UNCLASSIFIED (ruling 8c); under the per-run grain it is the 1 in 13/14 and voids no passing run |
| Z-S65 | DISMISSED_WITH_REASON | the disarm record of Z-S64 |
| Z-W90-S13 | DISMISSED_WITH_REASON | its premise is refuted in code (the tab-transport bbg leg reaches solve()); the gap was recording, closed by aj-5 |
| Z-W90-S14 (`request_kind` labels a bbg article 'listing') | **GRADUATED** (Z-C-S63) | a real mislabel in `transport.py:153-161`; it does not move the 2a grade (challenges are graded per run, not per kind) |
| Z-W90-S15, Z-W90-S16 | DISMISSED_WITH_REASON | the worker's readings of open order text (retry only after a failed solve; the in-window and unattributed definitions). This seat read `is_void` and `minute_state` and accepts the definitions as conservative |
| Z-W92-S18, Z-W92-S19, Z-S66, Z-W92-S20, Z-W90-S21, Z-W90-S6, Z-W87-S1 | **GRADUATED** (Z-C-S62) | the ft route census. Each is the measurement of one dead route or one session property, and their question is one: FWD-11 ft limb (1) |
| Z-W92-S11, Z-W92-S12 (ARMED), Z-W90-S18, Z-W90-S19, Z-W90-S20 | DISMISSED_WITH_REASON (Z-C-S65) | with ft OFF (STOP_FT) the two session hazards have no path to fire, and their substance is Z-C-S62's question. The other three are aj-6 stage-1 loader facts (Chrome 154 needs CDP `loadUnpacked`; the official release repo; a scratch-profile run, no ft request) |
| Z-W90-S17 (barrons dict titles) | DISMISSED_WITH_REASON | remedied by aj-8 (@`2268853761`; 149 of 149 re-derived, 0 others moved). Gold #5 is titled 23,691 of 23,691, and the served BA day reads 6 of 6 headlines |
| Z-W58-S1 (gold branch HOLDs, 09-29, ARMED) | DISMISSED_WITH_REASON | superseded: the gold branch now commits generations at as_of 2026-10-02 (trending SERVED; breakout EMPTY with its reason) |
| Z-W56-S2 (raw capture only on --harvest-grammar, ARMED) | DISMISSED_WITH_REASON | the driver always passes it (`backfill_driver.py:178` `["run", "--harvest-grammar", ...]`); only a hand-run legacy invocation lacks it |
| Z-W91-S8 (GetLastInputInfo changes every 2-3 min, ARMED) | DISMISSED_WITH_REASON | superseded as an instrument: limb 2a is graded on `load_monitor`'s per-minute hardware/injected counts (round-36 rule), not on `last_operator_input` |
| Z-W91-S10 (barrons 0-hit 200 read as "no articles", ARMED) | **GRADUATED** (Z-C-S63) | a failed retrieval that returns a value. It is real and silent; barrons reached 89 of 89 pairs anyway |

## 5. For the CTO's round-37 analysis

1. **Z-C-S62:** the FWD-11 ft limb (1) ENDPOINT question (packet 6.1).
2. **Z-C-S63:** two enrichment items: the `request_kind` mislabel, and barrons' zero-hit 200 as "no articles".
3. **Packet 6.3 and 6.4:** 2 stranded bbg rows (`SilverRowError`, one of them new and unread), and gold as a SCHEDULED producer.
   Under CLAUDE.md a production pipeline must be scheduled; rebuild #5 was an ad-hoc pair.
4. **This seat's own debt, named and not cut.** The remediation channel has not moved since round 10 (09-28): 48 graduated items
   read ARMED, 29 have no remediation row, and 19 rows from rounds 1-10 are still OPEN. It does not gate this slug: every BLOCKING or
   ARMED row is dispositioned, and GRADUATED is a disposition. This seat will reconcile it as its own act.

## 6. L10 PRECONDITION

8 of 8 orders are terminal. Every BLOCKING or ARMED row of the round, and every older UNDER_INVESTIGATION BLOCKING/ARMED row, is
dispositioned above. Judgment criteria: limb 2a, graded in section 1. **MET.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S62",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T19:20:00Z",
    "one_line": "FWD-11 limb (1) for ft has no working route: NopeCHA Token API discontinued, NopeCHA hCaptcha recognition not offered, the NopeCHA extension did not clear in 150 s, Ocilar answers 503, and hand sessions die at 24-75 min under keep-alive; ft is OFF (STOP_FT). An ENDPOINT question for the CTO: (a) a qualified wait to the Ocilar re-check 2026-11-01, (b) another solver, (c) accept ft at its depth -- (a) and (b) need Andrew's word.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROUND37_DRAIN_END_PACKET.md @4162e8837b section 4 (route census) and section 6.1 (options).",
        "investigations/INVESTIGATION_v1.md rows Z-W92-S18, Z-W92-S19, Z-S66, Z-W92-S20, Z-W90-S21 (7042 hardware events: not input-quiet), Z-W92-S11, Z-W92-S12.",
        "org/ref/VENDOR_EGRESS_WHITELIST.yaml VEW-1 (NopeCHA, standing); Ocilar not listed, its one call on Andrew-direct ~13:3xZ (amendment acec34f084)."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W92-S18",
      "AMGT_HARVST-Z-W92-S19",
      "AMGT_HARVST-Z-S66",
      "AMGT_HARVST-Z-W92-S20",
      "AMGT_HARVST-Z-W90-S21",
      "AMGT_HARVST-Z-W90-S6",
      "AMGT_HARVST-Z-W87-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "FWD-11 (1): each publisher signs in robustly and unattended.",
    "world_is": "No ft route works today; every measured route has its row.",
    "notes": "FOR THE CTO (round-37 analysis): rule the ft limb -- (a) qualified wait with Andrew's word, (b) another solver with Andrew's word, or (c) accept ft at its depth (3 of 89 pairs, 62 stored)."
  },
  {
    "id": "AMGT_HARVST-Z-C-S63",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T19:20:00Z",
    "one_line": "Two enrichment items graduate to the round-37 analysis: transport.request_kind labels every bbg article fetch 'listing' (substring '/news'), and barrons' search can answer HTTP 200 with 0 parseable hits, which the collector reads as 'no articles' rather than a failure.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S14 (transport.py:153-161; publishers.py:732).",
        "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W91-S10 (ae5_run1_barrons.json: 200, 0 hits; 16 hits on every other call)."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W90-S14",
      "AMGT_HARVST-Z-W91-S10"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "A record names what was fetched; a failed retrieval is not a value.",
    "world_is": "One mislabel; one silent zero.",
    "notes": "Neither moves limb 2a or a served figure today."
  },
  {
    "id": "AMGT_HARVST-Z-C-S64",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T19:20:00Z",
    "one_line": "Round 37 L8/L9: bbg limb 2a MET per run under ruling 8 (13 in-window runs with every challenge non-void and passed; window pass rate 13/14; 22 void runs not counted; the 1 non-void fail Z-S64 UNCLASSIFIED and disarmed by aj-5), superseding this seat's v48 NOT-MET at the round-36 grain; wsj/barrons/ft/sa MET-BY-ABSENCE with (2b) OPEN; the remaining round rows and the older ARMED rows dispositioned as remedied, superseded or carried by Z-C-S62/S63.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "round37/close_load_window_grade_20261002T1838Z.json: bbg 182 runs, 88 in window, 36 challenged: 13 MET, 22 void, 1 non-void failed; window_pass_rate 0.9286.",
        "lib/opal_data_harvest/load_window_grade.py is_void :196-204 and minute_state :93-102 (unmonitored minutes void).",
        "S3-served reads by this seat: BA timeline/day/2026-09-08 6 rows, 6 headlined; rankings trending/chatter SERVED 1 row, breakout/chatter EMPTY 'NO_SIGNAL_IN_WINDOW 190 of 191' (as_of 2026-10-02).",
        "lib/opal_data_harvest/backfill_driver.py:178 passes --harvest-grammar on every driver run."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-S64",
      "AMGT_HARVST-Z-S65",
      "AMGT_HARVST-Z-W90-S13",
      "AMGT_HARVST-Z-W90-S15",
      "AMGT_HARVST-Z-W90-S16",
      "AMGT_HARVST-Z-W90-S17",
      "AMGT_HARVST-Z-W58-S1",
      "AMGT_HARVST-Z-W56-S2",
      "AMGT_HARVST-Z-W91-S8"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-S64/S65 disarmed by aj-5 and its failure carried in the window pass rate; Z-W90-S13 refuted in code; Z-W90-S15/S16 accepted worker readings of open order text; Z-W90-S17 remedied by aj-8; Z-W58-S1 superseded (gold commits generations); Z-W56-S2 the driver always passes the flag; Z-W91-S8 superseded as an instrument by load_monitor.",
    "spec_asserts": "FWD-11 (2a): load-time challenges are solved unattended, graded per run (ruling 8).",
    "world_is": "bbg MET on 13 runs; the four others present no challenge at load.",
    "notes": "L10 precondition MET."
  },
  {
    "id": "AMGT_HARVST-Z-C-S65",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T19:20:00Z",
    "one_line": "The two ARMED ft session rows (a restarted ft driver refuses a dead stored session; a renewed session dies 20-30 min later) have no path to fire while ft is OFF (STOP_FT), and their substance is part of Z-C-S62's question; the three aj-6 stage-1 loader facts (Chrome 154 needs CDP loadUnpacked; the official extension release repo; a scratch-profile run with no ft request) are recorded and need no act.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROUND37_DRAIN_END_PACKET.md section 4: 'ft stays OFF (STOP_FT)'; both ft launchers keep --disable-extensions.",
        "investigations/INVESTIGATION_v1.md rows Z-W92-S11, Z-W92-S12, Z-W90-S18, Z-W90-S19, Z-W90-S20."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W92-S11",
      "AMGT_HARVST-Z-W92-S12",
      "AMGT_HARVST-Z-W90-S18",
      "AMGT_HARVST-Z-W90-S19",
      "AMGT_HARVST-Z-W90-S20"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "With ft OFF the two session hazards have no path to fire and are folded into Z-C-S62's ENDPOINT question; the three loader rows are facts with no act owed.",
    "spec_asserts": "A restarted ft driver keeps collecting.",
    "world_is": "ft is off; nothing runs that these rows could break.",
    "notes": "If the CTO's ruling on Z-C-S62 re-opens an ft route, these two session properties are its first acceptance checks."
  }
]
```

-- 3.0.0_SA_CVO~Z
