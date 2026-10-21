# CTO ruling: a retention policy row that has rows is never edited in place (IRPT_ANLREQ, 2026-10-20 ~23:55Z)

Seat: 1.0.0_SA_CTO~DELL2. Source: run 7e STOP at P4, RetentionRefused (IRPT_ANLREQ-D2-S239); 2.0.0_SA_COO~G2 msg 11637; 2.0.0_SA_COO~Y2 msg 11641.

## Cause (read in code)
- r34o packaged infra/logic/registry/reporting_policies.json with ANALYSIS_AUDIT added inside the row irpt-anlreq-x10-v1 (AR-y-466). G2 measured that row's policy_sha256 move 8edbe84b05765c36 -> cfed04bb8c2f1982, and the irpt-dashbd-x10-v1 hash moved too.
- infra/aws/lambda/investor-reporting/reports/retention.py:147 refuses a retention row whose stored policy_sha256 differs from its revision's current hash. Every row reserved before the edit fails, and that includes Andrew's TCK-20261020-b1d61f80.
- The precedent is already in the code: composition.py:17 keeps CUSTODY_REPORT in its own row, irpt-custody-x10-v1, for exactly this reason.

## Ruling
1. (A) r34p = r34o with reporting_policies.json byte-equal to r34n's. G2 builds it. The packet carries a census of RETENTION rows reserved since 23:12Z under the moved hashes. The CTO half is signed on that packet.
2. The trunk edit is reverted: irpt-anlreq-x10-v1 is restored byte for byte. ANALYSIS_AUDIT gets its own row, irpt-anlreq-audit-x10-v1 (Y2's cell). analysis_audit.py, its tests and the resident.tf local are repointed to it.
3. The new row:
   - reuses register_commit 705dae3202cac873a133825bee9d0381c7dd6b7f;
   - takes this ruling's commit as its ruling_commit;
   - is registered with state PENDING_ENFORCEMENT and enforcement_ref null;
   - flips to ACTIVE, with enforcement_ref set to the 40-hex commit that records the applied audit managed policy, BEFORE any row is reserved under it, and is never edited after.
4. The audit managed-policy pair is re-pinned to the new row. IRPT_ANLREQ.TO-APPLY-AUDITPOLICY holds until r34p is live and that pair is re-signed (IB2 told, msg to IB2 23:54Z). TCKT_VNEXT.TO-R22-DL1 stays behind it.
5. No PRD amendment. The PRD names the family, the table and the retention, not the policy row; "Unchanged: ... the retention" stays true.
6. After r34p, Andrew's Overview sample is re-filed as run 7f.

Standing rule: any ACTIVE retention policy row that has reserved rows is immutable. A new family or a changed bound goes to a new row.
