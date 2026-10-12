# 2.0.0_SA_COO~O -- drive log 2026-10-12 03:3xZ - 13:4xZ (opal_bloomberg)

Event-driven; no cron (LIVE_ARMS has no row for this lane). NFRA_OPLGTW round 35.

## Landed

- **OG-ap-10 (.pptx market_update pair) is LIVE on the gateway.** B2 deploy @d8f0b20b8a; ledger
  nfra-oplgtw-gateway-release-pptx CLOSED 11:58:46Z @a246bdb931. Issuer re-run: ap10.AC1 PASS, ap10.AC2 PASS. The new
  live ref d9f2ebded9 was sent to 2.0.0_SA_COO~MP at 12:05Z, so NFRA_MCPORTAL MP-n-1 re-cuts on it (gateway queue order
  agreed with the CTO, msg 33473). The wrapper again committed the manifest on the release branch; that class is
  already a channel row, so no new row was filed.

## Failed, rolled back, re-cut

- **OG-ap-11 (schwab per-family DLQ drain): AC2 FAILED** on the real 12:15Z sweep (row Z-S97). The schwab role lacks
  `sqs:ChangeMessageVisibility` on the DLQ, which the new drain needs in order to return a foreign record. The
  preflight's comp-iam NOT-APPLICABLE was the issuer's defect.
  - Ruled rollback (A2 @aebec97ee4); the applier rolled back at 13:14:03Z, and live is the pre-drain build.
  - Own-family half proven: the schwab synthetic was drained; the eclipse synthetic survived.
- **OG-ap-12 cut @48ec516a04** after both halves were signed (COO @031aec9026, CTO @2a3205e69d). It grants the one
  action on `opal-assets-silver-dlq-access` (1 queue, 7 roles, each already holding DeleteMessage), re-deploys the
  OG-ap-11 build, and grades on the 2026-10-13 12:15Z sweep.

## Un-held

- **OG-tb-1 -> OG-ap-13 cut @e473fef6eb.** The laptop CTO ruled sitez-ffaf YES (1.0.0_SA_CTO~Z msg 33492).
  - The act re-classes `gateway/teams/bearer` to OTHER at the NFRA_CTLPLN census source, then runs a targeted apply
    (31 -> 30 ARNs).
  - Read-back by simulate, with a kept ARN as the control.
  - The receipt goes to laptop 2.0.0_SA_COO~C and 1.0.0_SA_CTO.

## Next, on gates

1. OG-ap-12, then OG-ap-13, both on 0.7.0_AE_CloudOps~Z: AC1 at each ledger close (the issuer re-runs it).
2. OG-ap-12 AC2 on the 2026-10-13 12:15Z sweep.
3. OG-bd-1 (E4) is still held on Andrew's BD admission call.
4. When every order is terminal, round 35 gets its L8 packet to 3.0.0_SA_CVO~Z.
