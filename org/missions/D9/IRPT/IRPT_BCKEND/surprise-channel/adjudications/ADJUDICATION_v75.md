# IRPT_BCKEND: CVO adjudication, round 174 (workstream ~P)

<sweep_watermark>2026-10-13T06:41Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T06:41:00Z, on msg 6823 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_174_P_DRAIN_END_20261013.md`, 4a2f115a41). Two orders, no judgment criterion. PRD v0.53's ratified
half was signed first (org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_PRD_v0.53_RATIFIED_TEXT_REVIEW_20261013.md @d08f9f408e): the builder validates before its only write, and the serving function does not. 12 rows dismissed below (one
of them REMEDIATION_v50's D2-W354-S2); 1 graduates in `remediations/REMEDIATION_v51.md`. No new ARMED row.
Also recorded: the issuer caught a contradiction between a CTO ruling and Andrew's 2026-10-07 word (six classes, no multi_asset) and put it to
the CTO, who withdrew the ruling. That is right: a seat relays Andrew's word, never adjudicates around it.

```json
[
 {
  "id": "IRPT_BCKEND-C-S358",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T06:41:00Z",
  "one_line": "Dismissed: Round 174 (~P). D2-W356-S1 (the validation call is in run_firm, which main calls; this seat read :3133, :3158 and :3224), D2-W356-S2 (land writes its local_out debug files before its hook, and its only production caller validates first; nothing reaches S3 unvalidated), D2-W357-S1 (BLOCKING; closed by AMENDMENT 1, row D2-W357-S3), D2-W357-S4 and -S5 (BLOCKING; refusals under a withdrawn direction, superseded by the CTO's six-class ruling RE 6818, which keeps Andrew's 2026-10-07 word), D2-W357-S2, -S6, -S7, -S8 (a tsc invocation note, the close request, the regeneration's two changes, the suite count), D2-S128 (the issuer's disposition record), and REMEDIATION_v50's D2-W354-S2 (DISARMED; its remedy, 'record that the contract is enforced at build only', is met by PRD v0.53, signed by this seat at the call site).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W356-S1",
   "IRPT_BCKEND-D2-W356-S2",
   "IRPT_BCKEND-D2-W357-S1",
   "IRPT_BCKEND-D2-W357-S2",
   "IRPT_BCKEND-D2-W357-S3",
   "IRPT_BCKEND-D2-W357-S4",
   "IRPT_BCKEND-D2-W357-S5",
   "IRPT_BCKEND-D2-W357-S6",
   "IRPT_BCKEND-D2-W357-S7",
   "IRPT_BCKEND-D2-W357-S8",
   "IRPT_BCKEND-D2-S128",
   "IRPT_BCKEND-D2-W354-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "IB-pr-505 and IB-pr-506 are complete (order files read); drains 50fc1010d5 and 7c14d46b59 and amendments 8207e46109, e06aa7cb6a and cbcc4a88b8 are on HEAD. PRD v0.53's ratified half is SIGNED (org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_PRD_v0.53_RATIFIED_TEXT_REVIEW_20261013.md @d08f9f408e). The portal keeps six classes (Andrew-direct 2026-10-07), with the contract bytes unchanged. No new ARMED row.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W356-S1, D2-W356-S2, D2-W357-S1, D2-W357-S2, D2-W357-S3, D2-W357-S4, D2-W357-S5, D2-W357-S6, D2-W357-S7, D2-W357-S8, D2-S128, D2-W354-S2",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_174_P_DRAIN_END_20261013.md (4a2f115a41, msg 6823)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_PRD_v0.53_RATIFIED_TEXT_REVIEW_20261013.md @d08f9f408e"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Readings, refusals superseded by a ruling that keeps Andrew's word, a grant gap closed by amendment, and a remediation met by signed text."
 }
]
```
