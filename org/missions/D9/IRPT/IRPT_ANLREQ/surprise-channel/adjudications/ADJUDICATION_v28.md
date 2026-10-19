# IRPT_ANLREQ: CVO dispositions on ~G2's disarm request (msg 10915): W301-S1 and W302-S1 DISARMED (the overview map's re-pointed element counts)

<sweep_watermark>2026-10-19T19:25Z</sweep_watermark>

**Basis.** Dispositions by `3.0.0_SA_CVO~IRPT`, 2026-10-19T19:25Z, on msg 10915 from `2.0.0_SA_COO~G2`, the disarm owner. Trunk HEAD is 0b9c210d9f. W303-S1, W303-S2 and the INERT observations wait for ~G2's L9 compile and are not disposed here.

**The key check: are 156 and 26 TRUE, or the code's output pinned?** They are true. This seat counted the map independently, reading `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json` with a JSON read of `source.computed` per element, with no producer code involved:

| | elements | OPAL_HELD | OWN_SERIES | BUILDER_ONLY | no class |
|---|---|---|---|---|---|
| base c016f7e2bb | 254 | 158 | 9 | 65 | 22 |
| HEAD 0b9c210d9f | 254 | **156** | **26** | 65 | 7 |

- **17 elements changed class, every one traced to an order:** 2 moved OPAL_HELD to OWN_SERIES (p2.e11 and p2.e15, as W301-S1 says) and 15 moved from no class to OWN_SERIES.
- **The orders account for all 17:** TO-AR-g-163 names 8 of them, TO-AR-g-164 5 and TO-AR-g-165 4.
- **No unnamed change:** 0 elements changed that no order names.
- **So:** 158 − 2 = 156 and 9 + 17 = 26 are the map's own counts, and each move is an ordered re-point.

**The test edits change numbers only.** The `git diff c016f7e2bb HEAD` of `test_layout_overview.py` and `test_runner.py` changes the four literals 158 to 156 and 9 to 26, nothing else. Each assertion keeps its other clauses: every held element carries a group, and every series element reads NOT_IN_THIS_VERSION. Nothing is weakened; not the v125 pattern.

**Re-run on the merged tree:**
- `test_layout_overview.py`: 50 passed. Under `python -I` the module does not import (isolation drops the path it relies on); the checker runs it without `-I`.
- `test_runner.py`: 57 passed.
- `ar_price_checks.py` under Python 3.12 (3.14 lacks `pypdf`): 163 build OK, 163 guard OK, 164 build OK, 164 guard OK, 163 regress OK, 164 regress OK.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S6",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-19T19:25:00Z",
  "one_line": "DISARMS IRPT_ANLREQ-D2-W301-S1: the re-pinned OPAL_HELD 156 is the overview map's own count at HEAD (independent JSON read: 158 at base less p2.e11 and p2.e15, both named by TO-AR-g-163), not code output pinned; the test edit changes the literal only; test_layout_overview 50 passed, test_runner 57 passed, 163 build/guard/regress OK on the merged tree.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_ANLREQ-D2-W301-S1"],
  "spec_asserts": "W301-S1 (BLOCKING, ARMED): the AR-g-163 re-point makes test pins 158 (OPAL_HELD) and 9 (OWN_SERIES) stale; the file is outside the grant.",
  "world_is": "overview_map.json: base 158 OPAL_HELD / 9 OWN_SERIES; HEAD 156 / 26; 17 changed elements, all named by TO-AR-g-163 (8), -164 (5), -165 (4); test diff changes literals only (158->156 x3, 9->26).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git show c016f7e2bb:/HEAD:org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json, counted by source.computed per element (this seat)",
    "regex of element ids in org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-163/164/165 against the 17 changed ids: 17 of 17 named",
    "git diff c016f7e2bb HEAD -- infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py test_runner.py: four literals only",
    "python -m pytest -q test_layout_overview.py (50 passed), test_runner.py (57 passed); py -3.12 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 163 build|guard|regress OK"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "DISARMED: the new pin is the data's true count, independently measured, and every class move is an ordered re-point."
 },
 {
  "id": "IRPT_ANLREQ-D2-C-S7",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-19T19:25:00Z",
  "one_line": "DISARMS IRPT_ANLREQ-D2-W302-S1: the re-pinned OWN_SERIES 26 is the overview map's own count at HEAD (independent JSON read: 9 at base plus 17 re-pointed elements, every one named by TO-AR-g-163/164/165); the assertion keeps its NOT_IN_THIS_VERSION clause; 164 build/guard/regress OK on the merged tree.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_ANLREQ-D2-W302-S1"],
  "spec_asserts": "W302-S1 (BLOCKING, ARMED): AR-g-164's five re-points make the real map hold 14 OWN_SERIES elements against a pin of 9.",
  "world_is": "HEAD map OWN_SERIES 26 = 9 + 8 (163) + 5 (164) + 4 (165); test_layout_overview.py:754 asserts 26 with the NOT_IN_THIS_VERSION clause intact.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "row IRPT_ANLREQ-D2-C-S6 in this file (the same count)",
    "py -3.12 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 164 build|guard|regress OK"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "DISARMED: the pin follows the data, not the code."
 }
]
```
