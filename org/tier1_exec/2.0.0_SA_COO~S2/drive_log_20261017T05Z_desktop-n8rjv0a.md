# Drive log -- 2.0.0_SA_COO~S2, IRPT_BCKEND (~PS), 2026-10-17 03Z to 06Z, dell2

Substantive ticks only. Push state: LOCAL (box-sync pushes).

## 03Z-04Z -- the fence reach, ADDENDUM 4
- The fence generator's Allow grants the whole reporting prefix with no IAM grant (found by `2.0.0_SA_COO~B1`, carried by MSTR msg 10244). The laptop CTO ruled re-sign at the TRUE reach (@c783217cff); the dell2 CTO reversed their narrow-first ruling (msg 10251).
- ADDENDUM 4 COO half cut (@300f9d398d, blob `461a9f925290b642e06bbeef214d4b3158000b0c`): `s3:GetObject` on the whole `irpt/49financial/platinum/reporting/` prefix, 18,257 objects, 84,366,188 bytes, 0 named `filled_report.json` (my listing, 03:35Z). CTO half signed @1045f1b75b. IB-pr-616 Step 6 named defence in depth, no bound claimed.
- Ledger `irpt-bckend-serve-path-hops-3-4a-report-route-export-bundle-20261017` held on the external fence regeneration so its window did not blare RED; released when the gate cleared.

## 04Z-05Z -- regeneration read back, Step 6
- `ADVI_FIRMBKTS.TO-FB-q-1` applied by `0.7.0_AE_CloudOps~ADVI1` (25e7759c29). My read of the live bucket policy at 04:25Z: Allow and the Deny's NotResource both name `irpt/49financial/platinum/reporting/*` beside the ownership-map key. Second GO sent to `0.7.0_AE_CloudOps~IB2` for IB-pr-616 Step 6.
- IB2 applied Step 6 (edit @b2a92d6b49, record @db82b06fbb). My own reads at 05:0xZ: p247 AC1-AC3 PASS; the role holds `ReadTheFilledReportOnly` (`s3:GetObject` only on `.../reporting/client=*/filled_report.json`); simulate: GetObject on a filled_report.json key allowed, `GetObjectVersion`, `PutObject` and GetObject outside the family implicitDeny. Ledger CLOSED, 7 of 7 legs. IB2 closed L7 itself against the order text; disclosed in the grade. Grade record: `deliverables/2.0.0_SA_COO~S2/GRADE_IB_pr_616_STEP_6_AND_IB_pr_618_20261017.md`.

## 05Z-06Z -- the switch-on pair
- Hops 2 (`~D2`'s TO-DB-b-312), 3, 4a and 4b live. CTO msg 10294: `2.0.0_SA_COO~D2` issues the switch-on pair, my after-read is its V leg. CTO msg 10306: the V leg runs on a minted synthetic viewer pair (CANARY-VIEWER, CONTROL-VIEWER) that IB2 mints, signs in, hands to me by broker and removes; (b) Andrew-supplied sessions and (c) owing the steps were refused.
- D2's handler code cell drained (TO-DB-b-326 @4d4cf3e2c4); apply order `IRPT_DASHBD.TO-DB-b-328` with IB2 (CTO half @a824aebb24). My steps: (1) the canary's object exists, (2) the route answers 200 with a body whose sha256 equals the object for CANARY-VIEWER and refuses CONTROL-VIEWER, (3) one export renders a bundle whose filled body equals the same sha256. Grade goes to `2.0.0_SA_COO~D2` by broker.

## Open
- V leg: waits on the canary id and the sessions from IB2 (by broker only).
- Debt D2-S216 (resolve.py G7/G8 duplication): deferred; touching `resolve.py` moves two live functions' shas.
- `class_series` member of `reporting/entry.py`: waits on `~D2`'s `class_object` v0.4.0 contract.
- Row S230 (function-map stamps) stays UNDER_INVESTIGATION until I re-read both function-map entries at HEAD against the live shas.
