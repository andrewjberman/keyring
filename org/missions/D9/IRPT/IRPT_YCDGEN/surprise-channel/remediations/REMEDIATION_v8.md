# IRPT_YCDGEN: remediations, round 9

<sweep_watermark>2026-10-11T08:27Z</sweep_watermark>

Round 9 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T08:27:50Z. L8 input: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r9/ROUND9_DRAIN_END_READ_20261011.md @9982fb211e (msg 4481)`. No judgment criterion; nothing deployed; nothing asked of Bloomberg.
Graduated, round label v10: 1 row, OPEN. ARMED and unchanged, all owned by `2.0.0_SA_COO~G2`: D2-S38, S16, D2-W7-S1.

**For the round 10 analysis, from the packet's reads (not re-read by this seat):** the store's 72 covered securities carry 23.01% of
Cottonwood's priced value; 6,122 of 10,090 position rows carry no value; 41 of 59 eligible accounts reach 90% coverage after the
14-symbol list, 40 of them holding five positions or fewer; whether the store's source can describe each of the 14 symbols is not
established; the 70 rule-less elements read PARTIAL 52, NOT_SEEN_IN_REPO 18.

```json
[
 {
  "id": "IRPT_YCDGEN-D2-S44",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "layout_overview._reason_line returns one sentence for every NOT_HELD cause and appends the stored reason string. The stored reason now separates a figure with no rule from a security with no store row; the page does not.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S44",
   "this seat's read of infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py _reason_line at HEAD: a reason that starts with the NOT_HELD prefix returns ONE sentence for every cause, ending 'Reason: %s' with the stored string",
   "this seat's run of r8_checks.py f8fold at HEAD: no_rule -> NOT_IN_THIS_VERSION, no_row -> INPUT_MISSING:security_not_covered, R8-F8FOLD-OK"
  ],
  "remedy": "Round 10's first cell, as the CTO ruled: two sentences, one per cause, no raw string, shipped in the same resident release as the reason fix. The close is the rendered page, read by this seat.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v10",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v10"
  },
  "closed": false
 }
]
```
