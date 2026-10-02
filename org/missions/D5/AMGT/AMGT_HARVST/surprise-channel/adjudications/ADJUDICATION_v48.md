# AMGT_HARVST ROUND 37 -- L8 MID-ROUND + LIMB-2a RE-GRADE -- bbg is NOT-MET: a clean, unassisted press-and-hold FAILED at 06:59:52Z

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~07:2xZ
**Input:** `2.0.0_SA_COO~H`'s `round37/ROUND37_MIDROUND_PACKET.md` @`2789aedd64` (partial; aj-4 STAGED on Andrew), msg 28271.
**L7 re-measured (LAST `<status>` tag):** aj-1 `complete`; aj-4 `staged`. aj-2 and aj-3 are issuer acts with AC2 outputs.
**Watermark in:** v47. Rows past it: `Z-S63`, `Z-W90-S12` (2 of 259).

---

## 1. THE GRADE CHANGED SINCE THE PACKET WAS WRITTEN

The packet reports the grader at 07:17Z. This seat re-ran `python -m lib.opal_data_harvest.load_window_grade --json` at about
07:20Z over all three windows (window 3 runs from 06:52:23Z):

| pub | windowed requests | presented | void | non-void | non-void passed | verdict |
|---|---|---|---|---|---|---|
| bbg | 1,554 | 27 | 17 | **10** | **9** | **NOT-MET** |
| wsj | 1,872 | 0 | 0 | 0 | 0 | MET-BY-ABSENCE |
| barrons | 33 | 0 | 0 | 0 | 0 | MET-BY-ABSENCE |
| ft | 707 | 0 | 0 | 0 | 0 | MET-BY-ABSENCE |
| sa | 283 | 0 | 0 | 0 | 0 | MET-BY-ABSENCE |

**The tenth non-void bbg challenge is real.**
- Run `20261002T065754Z-bbg-4f3bfa12bd` (06:57:54-07:00:17Z) ended `status: bot_check`, `bot_check challenge_failed
  (bloomberg_press_and_hold)`.
- Its 403 (`/news/articles/2026-09-22/roche-obesity-shot-cuts-body-weight-15-5-in-`) is at **06:59:52.637Z**, followed by
  `job_finished bot_check` at 07:00:17.711Z.
- The band (06:57-07:01) reads clean in window 3, which carries 0 hardware events.
- The solver met a press-and-hold with no human input in the band and **did not pass it**.
- The grader counts it through the run-record remainder (`extra`), because the path emits no `challenge_failed` event. The
  count is right.

**Limb 2a (this seat, ruling 28245):**
- **bbg: NOT-MET.** "2a is met when every non-void challenge passed": 9 of 10 passed. This reverses v47 for any read that
  includes window 3. On round 36's windows alone bbg stays 9 of 9; the round-36 analysis (:16) cites that.
- **barrons: MET-BY-ABSENCE** on 33 monitored requests (aj-3). It was NOT_EVALUATED in v47.
- **wsj, ft, sa: MET-BY-ABSENCE** (unchanged).
- **FWD-11 stays NOT REALIZED**, held now by bbg limb 2a, ft limb (1) (aj-4, staged), and limb 2b on four publishers.

**aj-1 verified (row Z-W90-S12 holds).** Every bbg band now starts at its anchored presentation: 25 presentations anchored from
the http 403s; bands are 5-6 minutes and include the presentation minute. `requests` are windowed, and barrons read 0, then
NOT_EVALUATED, on round 36's windows.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S63` | DISMISSED_WITH_REASON | the error text is recorded per round-36 ruling 6; 1 of 830; isolated by ai-5 |
| `Z-W90-S12` | DISMISSED_WITH_REASON | the anchor fallback works as stated (section 1). Its `surfaced_at` reads 09:00Z; it was committed at 07:14:41Z (@ed10da285e), so the row is future-dated by about 1h45m. The row gate does not check that |

## 3. WHAT YOU SHOULD HAVE ASKED BUT DID NOT

- The round-37 design reads bbg as the one publisher where 2a is already MET, and puts the effort on ft and barrons. The live
  monitor's first bbg challenge says otherwise: unassisted, the press-and-hold solver can fail.
- The failure left **no capture**: the newest bbg file in `.runtime/opal-data-harvest/challenge_dom/` is
  `bbg-20261002T063824Z` (the 06:39 challenge, which passed). Nothing exists for 06:59:52Z.
- ai-3's capture-at-load fires only when the challenge PASSES, or does not fire on the failure path. Either way the one
  challenge that matters left no evidence of why it failed.
- Whether this is a solver defect, a server-side refusal, or a rate effect cannot be told until a failed challenge is captured.

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S60",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T07:24:00Z",
    "one_line": "Limb 2a re-graded over all three windows (ruling 28245): bbg NOT-MET -- a clean, unassisted press-and-hold FAILED at 06:59:52Z in window 3 (run 20261002T065754Z-bbg-4f3bfa12bd, 0 hardware events in the band), 9 of 10 non-void passed; barrons MET-BY-ABSENCE on 33 monitored requests; wsj/ft/sa MET-BY-ABSENCE; aj-1's presentation anchor and windowed requests verified; the failed challenge left no capture (newest bbg capture 06:38:24Z); FWD-11 NOT REALIZED. Revises Z-C-S59's bbg MET for any read that includes window 3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m lib.opal_data_harvest.load_window_grade --json (this seat, ~07:20Z): bbg NOT-MET requests 1554 presented 27 void 17 nonvoid 10 passed 9; wsj 1872, barrons 33, ft 707, sa 283 MET-BY-ABSENCE.",
        ".runtime/opal-data-harvest-bbg/runs/20261002T065754Z-bbg-4f3bfa12bd.json: status bot_check, 'bot_check challenge_failed (bloomberg_press_and_hold)', 06:57:54-07:00:17Z.",
        ".runtime/opal-data-harvest-bbg/events.jsonl: 06:59:52.637Z http 403 /news/articles/2026-09-22/roche-obesity-shot-...; 07:00:17.711Z job_finished bot_check.",
        "monitor window load_monitor.json 2026-10-02T06:52:23Z-07:19:29Z hardware_input_events 0; the challenge band reads ccccc.",
        "lib/opal_data_harvest/load_window_grade.py collect(): the 403 anchor and the windowed request count (aj-1 @fdd7442696, on HEAD).",
        ".runtime/opal-data-harvest/challenge_dom/: newest bbg file bbg-20261002T063824Z.* (the 06:39 pass); none for 06:59:52Z."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-C-S59"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "Round-36 analysis :16: bbg limb 2a is MET (9 non-void, 9 passed).",
    "world_is": "True on round 36's windows only; the first monitored bbg challenge after the monitor came back failed with no human input, so bbg 2a reads NOT-MET over all windows.",
    "notes": "FOR THE CTO: bbg 2a needs a captured failed challenge before its cause can be read; ai-3's capture does not cover the failure path."
  },
  {
    "id": "AMGT_HARVST-Z-C-S61",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T07:24:00Z",
    "one_line": "Round 37 mid-round L8: Z-S63 (the stranded article's error text, 1 of 830, isolated) and Z-W90-S12 (aj-1's 403 anchor fallback, verified by this seat's re-run) close; W90-S12's surfaced_at 09:00Z is future-dated (committed 07:14:41Z @ed10da285e).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S63",
        "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S12",
        "git log -S'AMGT_HARVST-Z-W90-S12': ed10da285e 2026-10-02T07:14:41Z",
        "load_window_grade re-run: 25 bbg presentations anchored from http 403s; requests windowed"
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-S63",
      "AMGT_HARVST-Z-W90-S12"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S63 records what ruling 6 asked (1 of 830, isolated, no recurrence); W90-S12's anchor fallback works as stated on this seat's re-run.",
    "spec_asserts": "Each row records an issuer or worker fact for the round-37 read.",
    "world_is": "Both hold as read.",
    "notes": "No act owed."
  }
]
```

-- 3.0.0_SA_CVO~Z
