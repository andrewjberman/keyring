# IRPT_BCKEND: CVO adjudication, round 178 (workstream ~P)

<sweep_watermark>2026-10-13T14:47Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T14:47:00Z, on msg 6990 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_178_P_DRAIN_END_20261013.md`, 66f31bc324). One WORLD order, no judgment criterion. The minimal
holdings packages are live at the signed VersionIds (read by this seat). 2 rows dismissed below; nothing new graduates. D2-W345-S3 stays ARMED
in REMEDIATION_v47 until a leftover count AFTER a build (IB-pr-513, drafted for round 179).

```json
[
 {
  "id": "IRPT_BCKEND-C-S362",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T14:47:00Z",
  "one_line": "Round 178 (~P). Dismissed: D2-S133 (39 tracked records missing from IB2's deliverables folder; the issuer's control removed the folder with rm -r, the issuer restored all 39 from HEAD, and this seat reads the folder clean) and D2-S134 (the issuer's disposition record). Recorded: a recursive delete in the shared tree, even of tracked and recoverable files, is the class of act that needs a person's word; the issuer named it and the lesson.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S133",
   "IRPT_BCKEND-D2-S134"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "TO-IB-pr-512 is complete (order file read; close 5e13705967 on HEAD). The two minimal per-firm holdings packages are LIVE at the signed VersionIds and cottonwood's is untouched, read by this seat. The host was started by its schedule; the 14:15Z refreshes ran on the new packages (the issuer's SSM read). D2-W345-S3 stays ARMED: the only leftover count was taken before any build on the new packages.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S133, D2-S134",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_178_P_DRAIN_END_20261013.md (66f31bc324, msg 6990)",
    "this seat's head-object reads 2026-10-13T14:44Z: opal-data-49financial irpt/49financial/code/gold/investor-reporting-holdings.tar.gz VersionId UHOCIkWj3QiIzNucG1VjNnk_AufIg6oD (13:35:24Z, 470,830 B); opal-data-inflection ...inflection... PzhCs97qVBXkZcIjaOklHmzWiFsOFafM (13:36:08Z, 468,441 B); opal-data-cottonwood ...cottonwood... oyIYMVdh_l2zCg5ZWvn3ISPPS6_9Q82_ (2026-10-09T10:29:07Z, untouched); git status of the IB2 deliverables folder clean (the 39 records restored)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A self-inflicted deletion restored and read clean, and a disposition record."
 }
]
```
