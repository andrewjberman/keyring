# 2.0.0_SA_COO~O -- drive log 2026-10-12 13:4xZ - 2026-10-13 01:5xZ (opal_bloomberg)

Event-driven; no cron. NFRA_OPLGTW round 35, applier 0.7.0_AE_CloudOps~Z.

## Landed

- **OG-ap-12 (grant + schwab per-family drain): ledger CLOSED 23:44:23Z; issuer ap12.AC1 PASS.**
  - Policy `opal-assets-silver-dlq-access` updated in place, v1 -> v2, 7 attachments unchanged.
  - The schwab-role simulate on `sqs:ChangeMessageVisibility` reads allowed.
  - Live schwab is the OG-ap-11 build `YeLm...` (`OPAL_BUILD_COMMIT` a11240c01c).
  - AC2 is graded on the 2026-10-13 12:15Z sweep.
- **OG-ap-13 (teams-bearer narrow, from OG-tb-1): COMPLETE; ledger CLOSED 00:58:47Z; issuer ap13.AC1 and ap13.AC2 PASS.**
  - Policy v4 -> v5, `ReadPlatformKeys` 31 -> 30 ARNs.
  - dell1 simulate on the bearer: implicitDeny; on the kept-ARN control: allowed.
  - Census source granted=false @5e58a617e7.
  - Receipt @c7d4d1f4f1. Relay to laptop 2.0.0_SA_COO~C and 1.0.0_SA_CTO asked of 1.0.0_SA_CTO~Z, since neither is on
    this broker.

## Rulings

- **Z-S98 (OG-ap-12 A1 @d78be8e6c2):** the description edit is struck. It forced replacement of a policy attached to 7
  roles, which contradicts the order's own plan bar. The applier was right; the defect was the issuer's.
- **Z-S99 (OG-ap-13 A1 @fed356e1cb):** the census source commit took the audited override `NFRA_CTLPLN_FAST_C`, one
  commit, census files only. The authority was COO condition A(a) plus the laptop CTO's recorded consent.

## Applier stall

- 0.7.0_AE_CloudOps~Z sat on a stale weekly-limit screen from 14:17Z; message 33522 was OFFER-EXHAUSTED.
- [STUCK] went to 0.0.0_AB_MSTR~Z at 22:03Z. It was revived at 22:05Z (MSTR msg 33525), so no re-seat was needed.
- The 8 h open ledger was missing bookkeeping, not a stranded act: the grant applied at 14:16:11Z.

## Next, on gates

1. Plant before about 12:10Z, then the 12:15Z sweep, then OG-ap-12 AC2. The issuer re-runs it.
2. OG-bd-1 is held on Andrew's BD admission call (row Z-W57-S2).
3. When every order is terminal, the round 35 L8 packet goes to 3.0.0_SA_CVO~Z.
4. Parked on NFRA_CTLPLN (laptop): `cloudops-dell-agent-platform-secrets-policy` is at 5 of 5 versions, so a prune is
   due before that root's next apply.
