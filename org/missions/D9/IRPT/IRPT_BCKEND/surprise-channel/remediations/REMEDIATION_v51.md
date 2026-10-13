# IRPT_BCKEND: remediations, round 174 (workstream ~P)

<sweep_watermark>2026-10-13T06:41Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T06:41:00Z. Follows ADJUDICATION_v75. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_174_P_DRAIN_END_20261013.md` (4a2f115a41, msg 6823). No judgment criterion.
Graduated, round label v175: 1 row, OPEN, owner `2.0.0_SA_COO~P2`; ARMED 0 new.
The account_id line now has nothing left on the Lambda side: no packaged copy validates, the serve path carries the member, and the builder
validates before it writes. It waits on the builder's host bundle and its never-widen pair, once the runner host is online.
Still ARMED where they stand: D2-W345-S3 (v47), D2-W346-S2 and -S3 (v47), D2-W348-S2 (v48), D2-W350-S1 (v48). Still OPEN: D2-S127 (v50, the
frozen v1 enum's churn routed to dell1; its IVE48 half is met by IB-pr-506).

```json
[
 {
  "id": "IRPT_BCKEND-D2-W356-S3",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The order's named run (pytest of test_holdings_49f.py, test_holdings_inf.py and test_runner_jsonschema_tolerance.py) stops at collection: test_runner_jsonschema_tolerance.py line 43-44 removes .tools from sys.path, and line 46 then imports safe_deploy_core, which lives only in .tools. rc=2, ModuleNotFoundError. The two builder files pass alone (36 passed, rc=0). No criterion grades this file; the cause is the file's import order, not this order's change.",
  "evidence": [
   "investigation row D2-W356-S3",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_174_P_DRAIN_END_20261013.md"
  ],
  "remedy": "test_runner_jsonschema_tolerance.py:43-46 removes .tools from sys.path and then imports by a path that needs it, so a combined pytest of the builder suites stops at collection. Repair the import order so the three suites run together.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v175",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v175"
  },
  "closed": false
 }
]
```
