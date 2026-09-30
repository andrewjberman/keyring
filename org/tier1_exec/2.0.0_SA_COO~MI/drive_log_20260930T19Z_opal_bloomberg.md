# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-09-30 16Z-19Z (host opal_bloomberg)

Lease FULL, round 5, limb L7. Thread y.

## Decisions closed this span

- **MX-r-6 A6 @4f7032da3b:** v3 re-cut by REF on 4ce7946426, carrying the stale-base guard.
  - ~19 cut it: release a5e73b6e72 / deploy-only 42c52ed4d9.
  - ETFS_RIVALS' 5 files are byte-equal; MCPMSP's are preserved (11 of 13 byte-equal, 2 merged).
  - The guard (DEPLOY_BASE_REF) passes 6/6 tests. Tools 52 -> 58.
- **Issuer base read 17:16:54Z** (manifest + S3). v3 ask + COO half @20599c0c29. CTO half @c0308f8b75; CVO half
  @5c54630648 (H1-H3).
- **The CTO held the GO for COO~O's Part D;** COO~O released it (msg 27307).
- **Andrew-direct "recs approved, proceed"** (@2bd24e1ac6), on this seat's /open-calls:
  - the v3 GO;
  - Alyssa's grant = all accounts under both masters, four datasets, list/describe/query.
- **v3 LANDED.**
  - IAM targeted apply 0/1/0 at 18:27Z.
  - Upload of 42c52ed4d9 at 18:33:41Z. The guard matched 4ce7946426 at both reads.
  - Read-back at 18:44:59Z: /health 200, /rivalfunds 401, 6 ids, FIRM_ROLE_ARNS kept, tools 52->58, host 87/87 ==
    artifact.
  - r6.AC1 and r6.AC2 PASS; row S20 notes that AC1 reads the v2 slug.
  - Ledger v3 CLOSED @9a9bccc871. Gateway hold released to CTO/CVO/~RV/~O.
- **Alyssa's Schwab grant ACTIVE at 19:15:29Z** (revision 2).
  - Written through the admin tool as opal-gateway-access-admin, after a no-write `prepare` diff.
  - 2 masters; 7,477 + 7,559 accounts (hashes only); 4 datasets; list/describe/query; 10 portal channels unchanged.
  - Record @c9be59c0c7. Temp credentials and raw ids deleted from the scratchpad.
- **R20.**
  - MSTR~Z's first pull was refused on a laptop row (S219).
  - This seat computed the 8 r20_exception entries against the frozen bytes, in a scratch worktree at origin
    (@b9d1b053bc; all pass r20_exception_ok).
  - MSTR~Z's second pull landed the gate edit on site-Z CLOUD (7d50db9064).
  - The CTO is asked to land the entries, which un-holds MX-t-10, MX-t-13 and MX-r-7.
- **Drain of wk-nfra_mcpindex-5-19 @d805cc536b** (49 files). Three conflicts:
  - the manifest's gateway fields -> the branch side (live truth);
  - deploy-to-ec2.sh -> exactly the deployed release's bytes (CLOUD + 87 added, 3 changed);
  - the channel -> union of rows.
  - A peer's staged AMGT_HARVST order was unstaged per safe-merge; their working file was untouched.

## State at ~19:3xZ

- Round 5: MX-s-15, MX-q-3, MX-a-8 complete. MX-r-6 is LIVE with ACs PASS; J1 needs Alyssa's cold run.
- HELD:
  - MX-t-13 and MX-r-7 (awaiting the CTO's entries);
  - MX-t-12 (to L10).
- Round 4: MX-t-10 (entries); MX-s-14 (fires).

## Compiler Tools
- None. The reads were S3, SSM (via the worker), `deploy_ledger.py`, a DynamoDB query, `terraform plan`, the naming
  gate's `--diff`, and the admin tool's `prepare`.
