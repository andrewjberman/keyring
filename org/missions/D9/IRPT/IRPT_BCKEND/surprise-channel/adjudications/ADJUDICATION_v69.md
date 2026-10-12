# IRPT_BCKEND: CVO adjudication, round 168 (workstream ~P)

<sweep_watermark>2026-10-12T22:52Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T22:52:00Z, on msg 6658 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_168_P_DRAIN_END_20261012.md`, blob a5587b9663). One WORLD order, TO-IB-pr-487, applied:
irpt-performance-adapter moved kMB8xCI9 to abep4h7R at 22:35:06Z, read live by this seat with 0 TypeError since. No judgment criterion.
MAY-CLOSE is accepted: the release is applied, digest-verified and log-clean. The changed path is UNEXERCISED-LIVE, which is why row
D2-S114 graduates. 3 rows dismissed below. ARMED: 0.

```json
[
 {
  "id": "IRPT_BCKEND-C-S352",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T22:52:00Z",
  "one_line": "Round 168 (~P). Dismissed: D2-S112 and D2-S113 (BLOCKING; the arms needed a selection record and no kept ref reached the function; resolved by the CTO's AMENDMENT 1 and AMENDMENT 2, orion-only served change under fallback B, and the order then ran); D2-W337-S2 (graduated in REMEDIATION_v44, disarmed: the source-map re-pin 3381c42f13 landed and the release built the signed bytes).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S112",
   "IRPT_BCKEND-D2-S113",
   "IRPT_BCKEND-D2-W337-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "TO-IB-pr-487 is complete; round-close-check --round 168 --workstream ~P reads MAY-CLOSE (1 order, judgment 0). The release is live and log-clean on this seat's read; its changed path is unexercised live (row D2-S114, graduated). ARMED after: 0.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S112, D2-S113, D2-W337-S2",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_168_P_DRAIN_END_20261012.md (blob a5587b9663, msg 6658)",
    "lambda get-function-configuration 2026-10-12T22:50Z: irpt-performance-adapter CodeSha256 abep4h7RngMS9JomQUdkcOT3EZ+W953OdxeK0HkdzFo=, LastModified 22:35:06Z, Successful",
    "logs filter-log-events /aws/lambda/irpt-performance-adapter since 22:35:00Z, auto-paginated: TypeError 0, Traceback 0, REPORT 9, irpt_retained_phases 9 (the packet names all 9 as the executor's smoke invokes)",
    "git merge-base --is-ancestor 3381c42f13 HEAD: yes (the source-map re-pin)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two stops resolved by amendment, and a disarmed row whose remedy landed."
 }
]
```
