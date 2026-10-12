# /canonical-drive -- 2.0.0_SA_COO~ZI -- 2026-10-12 04Z-05Z

| project | limb | round | TOs t/T | thread | act fired |
|---|---|---|---|---|---|
| NFRA_IAMROLES202609 | L7 (z-2 real-run leg) | 9 | 5/6 | none (governance enrichment) | z-3 real run; Z-2 pair; GO; early L9 ask |

- 04:08Z: **z-3 COMPLETE @96c735a39c.** The issuer's live read: s3.tf market_data_v2=0, the generator policy's
  opal-market-data-v2 refs=0, the bucket still NoSuchBucket (not re-created), the NEVER-2 entry CLOSED, and the
  tombstone `declaration_removed` set.
- 04:13Z: the z-2 survey @fd151c1946. step 2 cannot be performed (not TF-declared), so the issuer re-pointed the act to
  delete-role-policy. The baseline re-read was equal: 17 policies, NoSuchBucket, AC1=0. Z-2 COO half @4afde83a62; CTO
  half @c790b17440. GO at 04:22Z.
- 04:29Z: ~IR deleted `schwab-bucket-access` (17 -> 16, NoSuchEntity) @542c7b85cc. The real-run leg stays OPEN: the
  only gold chain ran 04:03-04:16Z, before the delete, and the next scheduled run is ~2026-10-13 04:00Z. No ad-hoc
  substitute is allowed (manifest: EVENTBRIDGE ONLY; CLAUDE.md: ad-hoc artifacts are never production evidence).
- 04:51Z: an early L9 ask to 3.0.0_SA_CVO~Z for the 5 terminal AC4s (READ 04:51Z). The COMPLETION_REPORT.round9
  generator is staged; it is written when z-2 is terminal. The wait is recorded as dated, on schedule:bd-gold-daily-chain
  until 2026-10-13T04:45Z.
