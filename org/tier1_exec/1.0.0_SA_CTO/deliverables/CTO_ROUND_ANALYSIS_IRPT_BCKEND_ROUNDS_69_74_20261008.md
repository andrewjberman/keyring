# IRPT_BCKEND -- ROUND ANALYSIS, rounds 69-74 (sweeps 15-16, workstream P)

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~05:3xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1213), ADJUDICATION_v33 @b370c21f68 (with v30-v32), REMEDIATION_v24.
- Every IRPT_BCKEND order is terminal (IB-pr-343 to IB-pr-360), with 0 judgment criteria.
- W142-S4 is closed end to end.

## 1. State

- **The export exposure is closed:** the fail-closed read is live and the receipt back-fill is done.
- **S382** (the first real Opal export) is OPEN by design. It is discharged by the first real export, or by Andrew's F1 retry once
  release 1 lands.
- **S388** (the AnalysisReport wire drift) is OPEN, ruled additive v1 (msg 03:27Z), with `~G2`'s contract-first cell owed.
- **Five rows are REMEDIATED and wait on their releases:**
  - W152-S1: X-1, release 2;
  - W162-S1 and W163-S1: the custody read route and print, waiting on the custody release and the PROD print promote;
  - W145-S2: finalize wiring;
  - W165-S2: wire regeneration to tmpdir, waiting on portal DEV.
- **ARMED:** S334, W140-S1, W145-S2 and W165-S2. Their disarms are owed by `2.0.0_SA_COO~P2`.
- **What waits outside this lane:** dell2's grants (laptop `~C`, not started per msg 1212) gate release 1 and the BD-session work.
  Release 1 is signed (@d2d2859a2a) and waits only on the `ssm:GetParameter` grant.

## 2. ENRICHMENT -- round 75, ONE issuance by `2.0.0_SA_COO~P2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **The four ARMED rows disarmed or re-justified** | (1) each row's disarm act is run and its evidence printed, or the row is stated as still ARMED with the one act that disarms it and that act's owner; ARMED after the round is printed with a denominator | LOCAL |
| E2 | **The custody release packet** (the IRPT_CUSTDY hop-5 path): P-c1 to P-c3 plus the `custody-report-read` route (W162-S1), as ONE release pair | (1) the release census at one pin lists every changed member against its owner; (2) both branches and rollback hashes per function; the after-reads are a refused other-firm read and an Opal read of one custody report by ref | SERVED |

The PROD promote of the print page (IB-pr-356 at 63b9382a, after DEV) stays Andrew's word, and it follows E2's release. X-1's release
2 and its repin wait on the filer entitlement (Andrew).

-- 1.0.0_SA_CTO~DELL2
