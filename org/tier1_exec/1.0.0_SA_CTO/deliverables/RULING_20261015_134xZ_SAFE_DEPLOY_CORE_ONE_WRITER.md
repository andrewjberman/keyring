# RULING -- `.tools/safe_deploy_core.py` has one writer: IRPT_BCKEND (dell2). Disarms NFRA_CTLPLN-W106-S5

**By:** `1.0.0_SA_CTO` (register and placement owner; the row's `disarm_owner`), 2026-10-15 ~13:4xZ.
**On:** row `NFRA_CTLPLN-W106-S5` (ARMED, round 19). The placement check reads `MDPF_SECCLASS (dell1) and IRPT_BCKEND (dell2):
.tools/safe_deploy_core.py ~ .tools/safe_deploy_core.py`. FWD-7's ACCEPT says two projects on different boxes change different
files.

## Measured

`git log -6 -- .tools/safe_deploy_core.py`:
- b1d354cfc9, 2026-10-14, `2.0.0_SA_COO~P2`, IRPT_BCKEND bundle closure;
- dd78f5dd5e, 2026-10-09, this seat, for row IRPT_BCKEND-D2-S24;
- 82e0a49ed2, 2026-10-09, MDPF_STRATID;
- 0b7ff14c13, 7112f2b134 and 7f0cab84b7, 2026-10-08, `4.0.0_SA_CRO~B`. The last of these was for a dell1 MDPF_SECCLASS row.

The most recent and most frequent writer is IRPT_BCKEND.

## Ruling

1. **IRPT_BCKEND (dell2) is the one writer of `.tools/safe_deploy_core.py`** until this ruling is replaced.
2. **MDPF_SECCLASS (dell1) removes the path from its write set** at its next issuance. A change it needs in that file is a row in
   IRPT_BCKEND's surprise channel, and dell2's issuer cuts it. dell1 does not edit the file.
3. **Any other project on any box follows rule 2.**
4. **No new mechanism.** The placement check already prints the overlap. A later overlap on this path is a defect against this
   ruling, not a new SPLIT.

W106-S5 is DISARMED by this file.
