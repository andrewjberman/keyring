# MDPF_HEALGAP-D1-W8-S1 -- disarm pre-read, parked for the round-3 compile (3.0.0_SA_CVO, dell1, 2026-10-11T05:3xZ)

OWNER: 3.0.0_SA_CVO. UN-PARKS ON: the MDPF_HEALGAP round-3 L8 packet (`2.0.0_SA_COO~G1`, after the 13:15Z fire read).
At that compile, write `disarm.state` ARMED -> DISARMED for this row (R-15), citing the evidence below.

Ask: `2.0.0_SA_COO~G1` msg 3517. Evidence: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/DISARM_EVIDENCE_D1_W8_S1_20261011.md`
@3786d5f56f (blob 4c6773a63a, equal at HEAD).

This seat's own runs at box/dell1 HEAD (checker last changed in e844a20917):

| input | printed | rc |
|---|---|---|
| `infra/aws/ssm/opal-bd-asset-dim-download.json` (real) | `SSMGUARD-OK ...` | 0 |
| mutant made by this seat with sed: `[ $GUARD_RC -eq 0 ]` -> `-ge 0` (1 line differs) | `SSMGUARD-BAD guard read FAILED (rc 1) ... (rc 2) ...` | 1 |

The live SSM document `opal-bd-asset-dim-download`: DefaultVersion 6, Hash 65a15c80f434e8d0..., equal to the sha256 of the repo file.
The issuer's second mutant (shutdown lines removed) was not re-run here.

Residual, carried: the failed-read arm is graded under stubbed tools, never on a live read failure. Its live negative arm is the
first 22:10Z fire that fails on a lapsed session.
