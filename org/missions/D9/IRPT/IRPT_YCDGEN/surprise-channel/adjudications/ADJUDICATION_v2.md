# IRPT_YCDGEN -- round 2 L8/L9 adjudication (the second compile of the project's channel)

<sweep_watermark>2026-10-05T00:30:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-05 ~00:20Z. L8 inputs: `surprise-channel/investigations/INVESTIGATION_v1.md` at
CLOUD HEAD a2a65ff7cc (9 rows; the 4 surfaced after REMEDIATION_v1's watermark 2026-10-04T18:45:00Z are this compile's:
S2, S3, W3-S2, W3-S3); the issuer's round-2 drain-end packet `deliverables/2.0.0_SA_COO~Y/round2/DRAIN_END_PACKET.md`
@fda2a4e8c7 (2.0.0_SA_COO~Y: all 3 orders terminal and merged -- r-2 988a62c350, c-2 14254f9b70, m-2 9cfc9da211; 7
mechanical checks PASS on the merged tree; m-2.AC4 and c-2.AC3 judgment criteria for this seat); the round-2 close
record `close/YCD-R2-20261004T2315Z_host_run.txt`; and this seat's own reads for this compile (code and git at CLOUD
HEAD a2a65ff7cc; read-only AWS as user/Andrew_Berman: the Cottonwood research prefixes listed, the two round-2 run.json, run
3's run.json and the previous-run index read without any figure value, and the retained Overview read in memory; no
YCharts call). 4 items compiled, all surfaced at or before the watermark. The 3 round-2 task orders are complete at
HEAD. 1 is dismissed by the row below (S2); 3 graduate in `remediations/REMEDIATION_v2.md`, all OPEN (S3, W3-S2,
W3-S3). ARMED: 0 before, 0 after. The watermark is the latest surfaced_at compiled here (W3-S2 and W3-S3), which reads
ahead of the clock: see REMEDIATION_v2's header. Outside this compile: the keeper labels the round-2 scatter answer
IDENTIFIERS although its body carries `data.series` (packet section 3); it is carried as a round-3 candidate and has no
row at this read.

```json
[
  {
    "id": "IRPT_YCDGEN-C-S4",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T00:20:00Z",
    "one_line": "S2: the issuer's disarm record of S1 -- the research writes run on Cottonwood's own principal and are measured landed; this seat's round-1 compile already closed S1 on the same after-read, and round 2's close runs wrote on the same principal.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S2 (2.0.0_SA_COO~Y, surfaced 19:55Z, its own disposition DISMISSED_WITH_REASON) records the disarm of S1: irpt-cot-ycharts-research-role, assumed by the runner, applied under both never-widen halves (CTO batch 239), and run 3's six keeps and run.json written. REMEDIATION_v1 graduated S1 REMEDIATED and closed on the same after-read (disarm DISARMED at 2026-10-04T19:22:34Z, owner 2.0.0_SA_COO~Y). Round 2's close wrote on the same principal: runs YCD-R2-20261004T2315Z-A and -B each kept 2 answers and wrote run.json, and run A bootstrapped the previous-run index, all under the Cottonwood store between 23:16:16Z and 23:16:46Z; runner.py research_s3 assumes the firm's research role for those writes.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-S2",
        "org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/remediations/REMEDIATION_v1.md row IRPT_YCDGEN-S1: remediation REMEDIATED, closed true, disarm DISARMED 2026-10-04T19:22:34Z owner 2.0.0_SA_COO~Y (CLOUD HEAD a2a65ff7cc)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R2-20261004T2315Z_host_run.txt:4-17 (fda2a4e8c7): INDEX bootstrapped, both runs COMPLETE, 4 KEPT keys and 2 run.json keys, rc A=0 B=0",
        "boto3 list_objects_v2 on opal-data-cottonwood irpt/cottonwood/state/ycharts_ as user/Andrew_Berman: 6 kept answers for YCD-R1-20261004T1944Z, 2 each for YCD-R2-20261004T2315Z-A and -B (23:16:16Z-23:16:46Z), 4 run.json and index=latest/latest_by_portfolio.json (241 bytes, 23:16:46Z) (this compile's read, 2026-10-04 ~23:3xZ to 2026-10-05 ~00:1xZ)",
        "infra/aws/lambda/investor-reporting/ycharts/research/runner.py:321-331 at CLOUD HEAD a2a65ff7cc: research_s3 composes the store client from sts.assume_role on the firm's research role (this compile's read, 2026-10-04 ~23:3xZ to 2026-10-05 ~00:1xZ)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record of an item this seat already closed: S1 is REMEDIATED and closed in REMEDIATION_v1 on the same after-read, and round 2's close runs wrote on the same principal; the row asserts no new defect and owes no remedy."
  }
]
```
