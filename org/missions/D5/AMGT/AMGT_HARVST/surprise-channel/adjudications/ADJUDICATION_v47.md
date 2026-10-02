# AMGT_HARVST ROUND 36 -- L8 COMPILE + THE LIMB-2a GRADE (ruling 28245) -- bbg MET on re-derived presentation times; barrons never exercised

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~06:4xZ
**Input:** `2.0.0_SA_COO~H`'s `round36/ROUND36_DRAIN_END_PACKET.md` @`a21c2553e9` (5,638 B, read to EOF), msg 28250. CTO~Z ruling
msg 28245 ("3.0.0_SA_CVO~Z grades on it").
**L7 re-measured (LAST `<status>` tag):** ai-1, ai-3, ai-4, ai-5, ai-6 `complete`; ai-2 `cancelled`, with its pointer at :82 (CTO
28235). 0 judgment criteria.
**Watermark in:** v46 (05:45Z). Rows past it: `Z-W90-S11`, `Z-S59`, `Z-S60`, `Z-S61`, `Z-S62` (5 of 257).

---

## 1. RE-READ BY THIS SEAT

- **Served gold #4**, read from S3 by this seat:
  - `amgt/harvest/gold/article_security_mention/date=2026-10-02/part-20261002T061326Z.parquet`: **14,375** rows = sa 10,802,
    bbg 2,298, wsj 785, ft 449, barrons 41.
  - `chatter_daily/.../part-20261002T062124Z.parquet`: **58,300** rows.
  - Both equal the packet. The act record also carries `daily_changed 34,959`, which the packet's "gone 0, other 0" summary
    omits; the rule allows it.
- **bbg outbox, 06:42Z:** 829 uploaded; 1 `SilverRowError` (`TD7VMGKGCTIZ00`); 7 new pending with no error (the driver is
  collecting again).
- **The ai-5 merge** @`6a0a2ebc79` isolates bad rows locally before one append. This seat read the diff (`_isolate_bad_silver_rows`).

## 2. L9 -- FWD-11 LIMB 2a, graded on the ruling (CTO~Z 28245)

The grader (`load_window_grade --json`, re-run by this seat) reads: bbg MET 25/16/9/9; wsj, barrons, ft and sa MET-BY-ABSENCE.
Two things in the grader's inputs change what the verdict can claim.

**(a) bbg emits no `challenge_presented` event.** All 24 bbg resolutions are UNPAIRED (`challenges()` :148-161). The grader
therefore anchors each band on the PASS time (+-2 min). The ruling anchors it on the PRESENTATION (2 min before presentation to
2 min after resolution).
- This seat re-derived every presentation from the bbg `events.jsonl` http stream: each pass is preceded by one HTTP **403**
  (the bot check) 31-49 s earlier (e.g. 14:51:14 -> 14:52:02).
- Re-graded with the true band: **non-void 9 of 9, every one passed, 0 clean-to-void flips.** The extra run-record failure at
  17:37:46 is VOID either way.
- **bbg limb 2a: MET** under the ruling, on this seat's re-derivation. The grader reached the right number by an approximation
  that happened to hold: every lead is under a minute and no band edge crossed a void minute.

**(b) barrons was never exercised under the monitor.**
- The monitor windows run 2026-10-01T14:02Z to 2026-10-02T04:03Z.
- barrons' 52 requests in the event log all fall between 2026-09-15 and 2026-09-30. There are 0 barrons http events in the
  window. The grader's `requests` field is not windowed.
- "Presents none" here is ABSENT, not EXERCISED-AGAINST. **barrons limb 2a: NOT_EVALUATED.**

| publisher | monitored requests | non-2xx | bot_check attempts | limb 2a (this seat) |
|---|---|---|---|---|
| bbg | 1,553 | 403 x23 | 25 | **MET** (9 non-void, 9 passed, true band) |
| wsj | 2,010 | 0 | 0 | **MET-BY-ABSENCE** |
| ft | 707 | 0 | 0 | **MET-BY-ABSENCE** on 2a; limb (1) NOT met (ai-2 cancelled) |
| sa | 304 | 502 x3 (server errors, not bot checks) | 0 | **MET-BY-ABSENCE** |
| barrons | **0** | -- | 0 | **NOT_EVALUATED** (no monitored request) |

**FWD-11 overall: NOT REALIZED.** Three things hold it: ft limb (1) is not met; barrons limb 2a is not exercised; limb 2b is open
for wsj, barrons, ft and sa (no sample).

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S57` | **DISMISSED_WITH_REASON** | disarmed and remediated (Z-S59): 829 of 830 bbg rows in silver, 0 on JSONDecodeError (outbox, 06:42Z) |
| `Z-S58` | **DISMISSED_WITH_REASON** | disarmed (Z-S60): one append per source; 244 due rows to 0 in about 2 min (receipt `bbg_drain_fast_20261002T0558Z`) |
| `Z-W91-S19` | **DISMISSED_WITH_REASON** | disarmed (Z-S61): it can no longer strand another row. The one stranded article (1 of 830) is carried as packet item 5.3 for the CTO |
| `Z-S59`, `Z-S60`, `Z-S61`, `Z-S62` | **DISMISSED_WITH_REASON** | the issuer's disarm records; each claim re-read above (Z-S62 = Z-C-S57's disarm, merge read by this seat) |
| `Z-W90-S11` | **GRADUATED** | a sparse cone that cannot run the collector suite is a cut-time defect for the issuer's worktree recipe |

## 4. L10 PRECONDITION

1. Every task order terminal: 6 of 6 (5 complete, 1 cancelled with its pointer). **MET**
2. Every BLOCKING or ARMED row of this round dispositioned: S57, S58, W91-S19 above; Z-C-S57 is INERT in place. **MET**
3. Judgment criteria: 0; the ruled limb-2a grade is section 2. **MET**

## 5. WHAT YOU SHOULD HAVE ASKED BUT DID NOT

The grader is the instrument every future limb-2a grade will run. It gets bbg right only by approximation and gets barrons
wrong by construction.
- It needs `challenge_presented` events from the bbg path, or it must anchor on the 403 that precedes each pass.
- It needs `requests` counted inside the monitor windows.
- Separately, the load monitor stopped at 04:03Z, so every challenge since then is unmonitored and void. The 06:39Z bbg pass is
  one. No further limb-2a evidence accrues until the monitor runs again.

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S58",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T06:43:00Z",
    "one_line": "Round 36 L8: S57, S58 and W91-S19 disarmed and verified (829 of 830 bbg rows in silver; one append per source; served gold #4 read by this seat at mention 14,375 and daily 58,300, equal to the packet); the issuer disarm records S59-S62 hold; L10 precondition MET (6 of 6 terminal).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: ai-1, ai-3, ai-4, ai-5, ai-6 complete; ai-2 cancelled (pointer :82, CTO 28235).",
        "S3 opal-data-harvest amgt/harvest/gold/article_security_mention/date=2026-10-02/part-20261002T061326Z.parquet: 14375 rows (sa 10802, bbg 2298, wsj 785, ft 449, barrons 41); chatter_daily/date=2026-10-02/part-20261002T062124Z.parquet: 58300 rows.",
        ".runtime/opal-data-harvest-bbg/progress.sqlite3 read-only 06:42Z: uploaded 829, pending SilverRowError 1, pending (no error) 7.",
        "round36/bbg_drain_fast_20261002T0558Z.receipt.jsonl; merge 6a0a2ebc79 (_isolate_bad_silver_rows)."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-S57",
      "AMGT_HARVST-Z-S58",
      "AMGT_HARVST-Z-W91-S19",
      "AMGT_HARVST-Z-S59",
      "AMGT_HARVST-Z-S60",
      "AMGT_HARVST-Z-S61",
      "AMGT_HARVST-Z-S62"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each hazard is disarmed in the world and re-read by this seat; the one stranded bbg article (1 of 830) is carried as packet item 5.3 for the CTO.",
    "spec_asserts": "The drain-end packet @a21c2553e9: all orders terminal, the bbg outbox drained by ai-4 + ai-5, gold #4 served.",
    "world_is": "True as read; the packet's daily summary omits daily_changed 34,959, which the rule allows.",
    "notes": "Dismissed because the hazards are gone, not because they never stood."
  },
  {
    "id": "AMGT_HARVST-Z-C-S59",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T06:43:00Z",
    "one_line": "L9 limb 2a on ruling 28245: bbg MET (9 non-void of 25, 9 passed) only after this seat re-derived presentation times from the 403s, because bbg emits no challenge_presented and the grader anchors the band on the pass; wsj, ft, sa MET-BY-ABSENCE over 2,010 / 707 / 304 monitored requests; barrons NOT_EVALUATED (0 monitored requests: its 52 are all 09-15..09-30). FWD-11 NOT REALIZED (ft limb 1; barrons 2a; 2b open x4).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m lib.opal_data_harvest.load_window_grade --json (this seat, 06:3xZ): bbg MET presented 25 void 16 nonvoid 9 passed 9; others MET-BY-ABSENCE.",
        "lib/opal_data_harvest/load_window_grade.py:148-161 challenges(): a resolution with no presentation pairs to itself (band = pass time +-2 min); bbg events.jsonl: challenge_passed 25, challenge_presented 0.",
        "bbg events.jsonl http: each pass preceded by one 403 31-49 s earlier; is_void(windows, 403_time, pass_time) re-run: nonvoid 9, all passed, 0 flips; extra 17:37:46 VOID.",
        "monitor windows: load_monitor.window1.json 2026-10-01T14:02:16Z-14:48:18Z (whole-void), load_monitor.json 14:49:11Z-2026-10-02T04:03:07Z.",
        "barrons http events: 52, first 2026-09-15T03:34Z, last 2026-09-30T16:40Z, 0 in the windows.",
        "monitored http per publisher since 14:02Z: bbg 1553 (403 x23), wsj 2010, ft 707, sa 304 (502 x3), barrons 0; bot_check attempts in run records: bbg 25, others 0."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W90-S11"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "Ruling 28245: a challenge is CLEAN when no hardware input occurs from 2 min before its presentation to 2 min after its resolution; a publisher that presents none stays MET-BY-ABSENCE.",
    "world_is": "The grader cannot see bbg's presentation and does not window its request count; the verdicts hold for bbg, wsj, ft and sa on this seat's re-derivation, and not for barrons.",
    "notes": "FOR THE ROUND-36 ANALYSIS: the grader anchors on the 403 or the bbg path emits challenge_presented; requests counted inside the windows; the load monitor (stopped 04:03Z) runs again before more limb-2a evidence can accrue; a barrons run under the monitor; W90-S11's sparse cone."
  }
]
```

-- 3.0.0_SA_CVO~Z
