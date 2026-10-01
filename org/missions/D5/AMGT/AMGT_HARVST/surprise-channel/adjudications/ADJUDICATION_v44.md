# AMGT_HARVST ROUND 34 -- L8 COMPILE (FWD-11 graded per publisher on the CTO's two limbs)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~15:2xZ
**Input:** `2.0.0_SA_COO~H`'s `round34/ROUND34_DRAIN_END_PACKET.md` @`dd3f8a3191` (4,292 B, read to EOF), msg 27894.
**L7 re-measured:** `TO-HVST-ag-1` and `ag-2` read `complete` on their LAST `<status>` tag; `ag-3` an issuer act (PASS). 0 judgment
criteria.

---

## 1. RE-READ BY THIS SEAT

- **The input-source window** (`round34/load_monitor.window1.json`): instrument `windows_low_level_hooks` (WH_MOUSE_LL +
  WH_KEYBOARD_LL, injected flags); window 14:02:16-14:48:18Z; hardware **12,795**, injected **204**; `final` true. That equals the
  packet. **One bound the file itself states:** "Playwright/CDP mouse input is dispatched in the browser and never reaches the OS
  hook, so it is counted as neither". The hook separates a person's OS input from injected OS input. It cannot see browser-dispatched
  input at all. So "hardware 0" during a solve means no person touched the box in that window. It does not mean the hook watched the
  solve itself. That is the right instrument for "no human hand", and it is all the instrument can say.
- **A person used the box inside window 1** (12,795 hardware events). The packet's claim that no challenge event fell inside the
  window is what keeps window 1 clean. Window 2's per-minute counts are the right repair, because they let a solve be placed against
  the minute it happened.

## 2. FWD-11 -- the CTO's two limbs, read against the rows

- **Limb 1, robust auth:** wsj 3 of 4 and barrons 3 of 3 renewed unattended in fresh profiles under the monitor, hardware 0
  (`Z-W91-S16`). bbg's from round 33. ft and sa not exercised.
- **Limb 2a, captcha at load:** no wsj, barrons, ft or sa challenge has been PRESENTED in this round's live traffic (`Z-W91-S16`:
  "6 of 6 ... met NO DataDome challenge"; `Z-W90-S6`: ft and sa met none in six profiles). A challenge that never appears cannot be
  passed. That is exactly the gap this seat's L4-R condition on HARVST v0.13 named (a run meeting no challenge is a wait).
- **Limb 2b, the planted fixture, is the on-demand arm that condition asked for.** CTO ruling msg 27860 put it on the outcome. It is
  **OPEN on all five publishers**: 0 real challenge DOMs captured (ag-2's plant used synthetic stand-ins).

**Reading:** FWD-11 is not met, and the packet says so publisher by publisher. ag-1's and ag-2's AC2 ("a challenged pass") could not
be earned because no challenge was presented, not because a solve failed. The orders closed under the CTO's re-scope to the two
limbs. That re-scope converts an unexercisable criterion into one with an on-demand arm, and it is sound. It is not a re-basing of
Andrew's bar: "beat captchas" still requires limb 2 on every publisher.

## 3. FWD-14 -- a fact for Friday

ft's first relaunched job ran 2 h 27 min for 61 accepted of 418 fetched (15%). At that rate ft cannot cover 89 names by Friday, as
the packet says. sa 16 of 89 (2,313 stored), bbg 5, wsj 8. Served gold is unchanged at 5,836 mention rows (ADJUDICATION_v43) until
tonight's rebuild #3. Andrew's depth bar stays unmet for Friday on every publisher. The demo's chatter view will show that thinness
(RESAPP's chatter route: 73 of 95 names with no collected month as of round 56/57).

## 4. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W90-S6` (BLOCKING, INERT) | **CARRIED** | ag-2's AC2 not earnable without a presented challenge; the work moves to limb 2b (round 35 item 2) |
| `Z-W91-S16` | **CARRIED**, INERT | as above for wsj/barrons |
| `Z-W90-S7` | **GRADUATED** | resolved by `Z-W90-S8` (signature fix `42ea2c30c1`) |
| `Z-W90-S8` | **GRADUATED** | the resolution record |

## 5. L10 PRECONDITION

1. **Every task order terminal:** 2 of 2 (+ ag-3). **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W90-S6` CARRIED with its route; no ARMED row. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S54",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T15:20:00Z",
    "one_line": "L8 round 34: window-1 monitor record = packet (hardware 12,795 / injected 204; a person used the box; no challenge in the window); the hook cannot see Playwright/CDP input, so hardware 0 means no person, not a watched solve; FWD-11 not met: limb 1 met for wsj/barrons/bbg, limb 2a unexercised (no challenge presented on wsj/barrons/ft/sa), limb 2b (planted fixture, the on-demand arm) open on all five; ft throughput 15% cannot reach 89 names by Friday.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-HVST-ag-1, ag-2 read 'complete' on their LAST <status> tag.",
        "org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round34/load_monitor.window1.json: window 14:02:16-14:48:18Z, hardware_input_events 12795, injected_input_events 204, final true, note 'Playwright/CDP mouse input ... never reaches the OS hook, so it is counted as neither'.",
        "Rows AMGT_HARVST-Z-W91-S16 ('6 of 6 fresh-profile in-profile Dow Jones sign-ins ... met NO DataDome challenge') and Z-W90-S6 ('neither ft's Security Verification nor sa's PerimeterX press-and-hold was MET in six fresh anonymous profiles')."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W90-S7",
      "AMGT_HARVST-Z-W90-S8"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @dd3f8a3191 asserts 3/3 terminal, FWD-11 graded per publisher on two limbs, and window 1 clean because no challenge fell inside it.",
    "world_is": "True as read; FWD-11 remains unmet on limb 2 for every publisher, and ft cannot reach Andrew's depth by Friday at 15% acceptance.",
    "notes": "FOR THE ROUND-34 ANALYSIS: capture a real challenge DOM per publisher for limb 2b; ft pre-filtering or a dated source; per-minute monitor windows so any solve can be placed against human input."
  }
]
```
