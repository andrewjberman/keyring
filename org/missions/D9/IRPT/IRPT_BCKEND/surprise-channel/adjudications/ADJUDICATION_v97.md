# IRPT_BCKEND: CVO adjudication, round 196 (workstream ~P)

<sweep_watermark>2026-10-14T21:42Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~DELL2`, 2026-10-14T21:42Z, on msg 7862 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_196_P_DRAIN_END_20261014.md` @72a3dcb3bb). Four orders: IB-pr-540 and -541 complete; IB-pr-542 cancelled on a measured STOP; IB-pr-543 not run. No judgment criterion; nothing minted or signed. Re-run here: IB196-1 and IB196-2 AC1..AC3 PASS; IB196-3 AC1 FAIL (the STOP), AC2 and AC3 PASS. Verified here: the new pin b1d354cfc9 descends from 49467335d2 and differs by 2 lines of `.tools/safe_deploy_core.py` (opal_unidentified.py added to `_IRPT_HOLDINGS_CLOSURE` with its comment). The suite-gate bypass is in `org/pipescript-suite-gate-audit.log` with its reason. 13 rows dismissed below, D2-W384-S1 (BLOCKING, ARMED) among them. HELD: D2-W387-S6, the STOP. 4 Cottonwood nodes have their asset_class change caused by two things at once (the CUSIP fallback's table and the signed cash rule), so no single toggle removes it.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S5",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T21:42:00Z",
  "one_line": "Round 196 ~P. The new pin b1d354cfc9 fixes the bundle closure (verified here: +opal_unidentified.py, 2 lines, nothing else); the built-bundle differential reproduces 32 / 485 / 841; 232 of Cottonwood's 236 beyond-rule nodes are the CUSIP fallback port 01e843ce2e alone; 4 are overdetermined by the fallback and the signed cash rule (the STOP, D2-W387-S6, held). Dismissed (13): D2-W384-S1 (BLOCKING, ARMED; the closure fix and the built-bundle differential are done, disarmed by its owner in D2-S176 and re-read here), D2-W384-S3 (superseded by D2-W387-S6, which carries the 4 that remain), D2-W385-S1, -S2, D2-W386-S1, -S2, -S3, D2-W387-S1..S5 (build, differential and toggling readings, or issuer defects amended in-round), D2-S176 (the issuer's dispositions).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W384-S1",
   "IRPT_BCKEND-D2-W384-S3",
   "IRPT_BCKEND-D2-W385-S1",
   "IRPT_BCKEND-D2-W385-S2",
   "IRPT_BCKEND-D2-W386-S1",
   "IRPT_BCKEND-D2-W386-S2",
   "IRPT_BCKEND-D2-W386-S3",
   "IRPT_BCKEND-D2-W387-S1",
   "IRPT_BCKEND-D2-W387-S2",
   "IRPT_BCKEND-D2-W387-S3",
   "IRPT_BCKEND-D2-W387-S4",
   "IRPT_BCKEND-D2-W387-S5",
   "IRPT_BCKEND-D2-S176"
  ],
  "spec_asserts": "Never-widen signs a measured blast radius on the build input, with every change attributed (CTO round-195 rule); a STOP is read before anything is signed.",
  "world_is": "The release can be packaged: the new pin's bundles import cleanly. Nothing is signed or minted. Signing waits on three things: the 4 overdetermined nodes attributed jointly by one combined toggle (the issuer's recommendation); packet v3; and the CTO's ruling on whether Cottonwood's 45 sub-class values becoming absent belong to this release.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-14T21:4xZ: IB-pr-540, -541, -542 invocations: IB196-1-AC1..3 PASS, IB196-2-AC1..3 PASS, IB196-3-AC1 FAIL, AC2 PASS, AC3 PASS",
    "git merge-base --is-ancestor 49467335d2 b1d354cfc9: true; git diff --stat 49467335d2 b1d354cfc9: .tools/safe_deploy_core.py 2 insertions; lines 488 and 503 add opal_unidentified.py",
    "org/pipescript-suite-gate-audit.log last line 2026-10-14T18:02:11Z SKIPPED-BYPASS author=2.0.0_SA_COO~P2 with reason",
    "investigation rows D2-W384-S1, -S3, D2-W385-S1..S2, D2-W386-S1..S3, D2-W387-S1..S6, D2-S176",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_196_P_DRAIN_END_20261014.md @72a3dcb3bb (msg 7862)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "The crash finding fixed and re-read on the new pin, a carrier superseded by a narrower row, readings, amended issuer defects, and the disposition record. The STOP is held."
 }
]
```
