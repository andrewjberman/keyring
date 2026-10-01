# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-01 07Z (host opal_bloomberg)

Lease FULL, round 5, limb L7 -> L8, thread y.

## Decisions closed this span

- **Train TF act #1 APPLIED.** 06:52Z, safe-apply: "6 added, 0 changed, 0 destroyed".
  - The simulate allows the secret read on the resource-policy plane and the AssumeRole with the ExternalId. All
    negative controls deny.
  - 2.0.0_SA_COO~O was told at 07:02Z; OG-pr-1 act #2 may follow.
- **MX-r-7 LIVE.** opal-gateway 05e3eff563 since 07:13:52Z.
  - Ledger `nfra-mcpindex-r5-bd-release` CLOSED 7/7.
  - Drained @1232c96dc7.
  - Issuer re-grade on CLOUD: r7.AC1 PASS 23/23, r7.AC2 PASS 7/7 ids, proof VALID.
- **Row Z-S70** (@9a97a21d9f) rules Z-W21-S18..S23:
  - no ExternalId rotation;
  - the untracked-root apply accepted;
  - discover's silver_datasets gap carried to L10.
- **Train slot 2 handed** to 2.0.0_SA_COO~MS (MS-d-2, `.env` 37 -> 39, `DEPLOY_BASE_REF`=05e3eff563).
- **r7.J1 material**, through this seat's principal session (Andrew): ETF routes to `etfs_get_positioning`; the BD
  fees question is catalogued:false.
- **MX-r-6 complete** on re-grade against live 05e3eff563. r6.J1 is Alyssa's (a person).
- **Row Z-S71** disarms Z-S68.
- **Round-5 drain-end packet** @81887e8ae8 sent to 3.0.0_SA_CVO~O. It lists 7 enrichment candidates for the L10 slug.

## Owed / blocked

- r6.J1: Alyssa's cold run (a person).
- L9: 3.0.0_SA_CVO~O on a8.J1 / r6.J1 / r7.J1.
- The L10 slug follows the CVO's adjudication. MX-t-12 is carried there.
- Cleanup of the drained worktrees and /c/tmp release trees (mx-rel7..10, mx-dep7..10, mx-rb7..10) is left for an
  operator-confirmed pass, because recursive deletion needs confirmation.

## Compiler Tools

- `proof-of-spec-check.py` VALID on r-6 and r-7.
- `safe-merge.sh`: the drain, with the row gate over the merged index.
- `deploy_ledger.py`.
- No comp-tool fit the live S3/SSM reads.
