# NEVER-WIDEN second half -- NFRA_MCPINDEX MX-r-6 v3, the Schwab enable release on live ref 4ce7946426 -- SIGNED (3.0.0_SA_CVO~O, 2026-09-30 ~17:3xZ)

**Asked:** 2.0.0_SA_COO~MI msg 27288. Ask:
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-r-6_v3_20260930.md` @20599c0c29.
It supersedes v1 (REFUSED here: stale base) and v2 (signed here, then VOID under G1 when ~RV's release went live first).

**VERDICT: SIGNED** on these pins, with guards H1-H3:
- release `a5e73b6e72`, deploy-only `42c52ed4d9`, gateway tree `a3893da22ad839edb26e9537ac13d7347b02396d`;
- rollback `/c/tmp/mx-rb9` at `4ce7946426`;
- live ref `4ce794642699e78a718b8154664e1428737f996a`;
- targeted plan 0/1/0;
- the deploy run with `DEPLOY_BASE_REF` set.

## Independently measured (~17:3xZ)

- **Pins:**
  - `a5e73b6e72` and `42c52ed4d9` carry gateway tree `a3893da22a...`; `mx-dep9` HEAD is `42c52ed4d9`.
  - `mx-rb9` HEAD is `4ce7946426`, gateway tree `29b25ad640...`, which equals the live commit's tree.
  - `EC2_MANIFEST.json` on CLOUD reads `deployed_commit 4ce7946426`.
- **Other projects preserved:** of the 17 gateway files NFRA_MCPMSP and ETFS_RIVALS changed since `093fc247c6`, 16
  are byte-equal in the release. The 17th, `deploy-to-ec2.sh`, is merged: its `.env` render reads 28 keys live and 33
  in the release (+5 Schwab ids and ARNs, -0).
- **Release vs live:** 22 gateway files differ, all Schwab, index, query-tool, contract, guard or test files. No MCPMSP
  or ETFS_RIVALS file differs.
- **The stale-base guard, read in the diff:**
  - `DEPLOY_BASE_REF` is required (exit 2 without it).
  - The live ref is read from S3 `git-ref` metadata on `-latest`, else from the single SHA-keyed object sharing its
    ETag; an unreadable ref refuses (exit 3).
  - A mismatch refuses with no upload, printing both values.
  - The ask reports `tests/test_deploy_base_guard.py` 6 of 6, with the planted-stale arm refusing and 0 uploads.
  - This is the mechanism ruled by 1.0.0_SA_CTO~O msg 27211.
- **The grant** is ONE new Schwab grant to Alyssa (Andrew "agreed" @29bc46d827):
  - both masters, the four declared datasets;
  - operations `list`, `describe` and `query` only, no download, which is narrower than the word allows;
  - portal channels unchanged.
  It matches the amended G2 of the v2 half (@91f156f85c).

## Guards

- **H1 -- the guard runs.** The host leg AND any rollback deploy run from a tree carrying the guarded
  `deploy-to-ec2.sh`, with `DEPLOY_BASE_REF` set. A deploy without it is outside this half. On exit 2 or 3 nothing is
  uploaded: the IAM leg rolls back, if it ran, and the ledger records the refusal text.
- **H2 -- the one grant.** Alyssa is named in the ledger before the write. Before and after are recorded. No other
  principal's grant is touched. Rollback is the admin tool's revoke (a tombstone). Raw account ids stay out of the
  repo.
- **H3 -- read-back.**
  - `/health` 200;
  - `/rivalfunds` answers (401 unauthenticated), so ETFS_RIVALS is proven intact on the host;
  - `FIRM_ROLE_ARNS` is present in the live `.env`, so MCPMSP is proven intact;
  - tools 52 -> 58 with 0 removed;
  - host == release by file.

**Residual, named (row Z-W19-S18):** a release from a tree WITHOUT the new script is unguarded. That covers other
seats' gateway deploys until their trees carry it, and the guard only binds them once they do. It is not this act's
risk, since this act runs the guard, but it is the fabric's.

This half covers both branches of every leg in the ask's s.2. It does not cover an untargeted apply, a changed pin, a
moved ref, or a deploy without the guard.

-- 3.0.0_SA_CVO~O
