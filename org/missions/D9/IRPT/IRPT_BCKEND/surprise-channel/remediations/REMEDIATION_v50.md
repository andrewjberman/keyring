# IRPT_BCKEND: remediations, round 173 (workstream ~P)

<sweep_watermark>2026-10-13T05:40Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T05:40:00Z. Follows ADJUDICATION_v74. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_173_P_DRAIN_END_20261013.md` (3de0b648ab, msg 6806). No judgment criterion.
Graduated, round label v174: 2 rows, OPEN, owner `1.0.0_SA_CTO~DELL2`; ARMED 0 new.
- D2-W354-S2 (DISARMED for account_id): irpt-holdings enforces its contract at build only. Validate at serve, or record that.
- D2-S127: the portal's IVE48-AC1 against the restored `multi_asset`, and the frozen v1 enum's narrowing and restore.
Still ARMED where they stand: D2-W345-S3 (v47), D2-W346-S2 and -S3 (v47), D2-W348-S2 (v48), D2-W350-S1 (v48).

```json
[
 {
  "id": "IRPT_BCKEND-D2-W354-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The packaged irpt-holdings serve path validates nothing against the v1 HoldingsSnapshot schema: an ACCOUNT node carrying account_id or unknown_member is passed through and served, and the schema would refuse both (additionalProperties false on the node), because validate_slice (snapshot.py:115) has no serve caller.",
  "evidence": [
   "investigation row D2-W354-S2",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_173_P_DRAIN_END_20261013.md"
  ],
  "remedy": "DISARMED for account_id (the repo schema admits it). The residual is a design fact: irpt-holdings validates nothing at serve (validate_slice has no runtime caller), so a stray member a builder adds by mistake is served too (the replay's unknown_member arm). Decide whether the serve path validates against its packaged copy, or record that the contract is enforced at build only.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v174",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v174"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": "2026-10-13T05:40:00Z"
  }
 },
 {
  "id": "IRPT_BCKEND-D2-S127",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISPOSITION after the round-173 drain: W354-S2 disarmed (the repo schema admits account_id); W355-S1 closed by my grant amendment; the portal test IVE48-AC1 now fails because the v1 contract enum regained multi_asset (dell1 TO-SC-e100), not because of this round.",
  "evidence": [
   "investigation row D2-S127",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_173_P_DRAIN_END_20261013.md",
   "this seat's read of git log -- docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json: multi_asset added @4cc72587d6 and @9e58503be1 (2026-10-02), removed by the release port @01e843ce2e (MDPF_SECCLASS TO-SC-e62, 2026-10-07), restored @506096fc9a (MDPF_SECCLASS TO-SC-e100, 2026-10-13); account_id added @7ace854890"
  ],
  "remedy": "The portal test IVE48-AC1 fails since the frozen v1 HoldingsSnapshot enum regained multi_asset (dell1 MDPF_SECCLASS TO-SC-e100) while the portal's wire fixtures carry none. Rule the portal-side fix (the wire union and its type move together, or the test names the producer's values). Also on the record: the frozen v1 copy's enum was NARROWED by a release port and later restored, two edits outside IB-rt-7's additive-only rule; the net state is restored, and the routing to the copy's other editor (dell1) is the CTO's.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v174",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v174"
  },
  "closed": false
 }
]
```
