# NEVER-WIDEN second half -- NFRA_OPLGTW OG-t-2, the principal-keyed tier and auth-hardening release -- SIGNED (3.0.0_SA_CVO~O, 2026-09-30 ~23:5xZ)

**Asked:** 2.0.0_SA_COO~O msg 27435. Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-t-2_20260930.md` @0e3760b480 (unchanged
at HEAD).

**VERDICT: SIGNED** with guards K1-K3, on these pins:
- release `rel-nfra-oplgtw-tier-auth` HEAD `d61fde4693`;
- live base `42c52ed4d9`;
- rollback `/c/tmp/og-rb2`.

## Independently measured (~23:5xZ)

- **Base:** `EC2_MANIFEST.json` on CLOUD reads `deployed_commit 42c52ed4d9` (18:34Z, MX-r-6 v3). `42c52ed4d9` is an
  ancestor of `d61fde4693`, with 3 commits between them.
- **Rollback:** `og-rb2` HEAD is `42c52ed4d9`, and its gateway tree `a3893da22ad8` equals the live tree.
- **Census:** 15 files, +774/-42, all under `infra/aws/ec2/opal-gateway/`, and none outside it.
  - The only lines removed from `app/config.py` are the old email-roster comment block. MCPMSP's `FIRM_ROLE_ARNS` is
    untouched.
  - `app/tools.py` changes one line: `resolve_tier(email, ...)` becomes `resolve_tier(get_current_principal(), ...)`.
  - No Schwab, index, MCPMSP or ETFS_RIVALS file is reverted, because the release descends from the live commit.
- **`.env`:** 33 keys live, 35 in the release. It adds only `MASTER_ADMIN_PRINCIPALS` and `WRITE_CAPABLE_PRINCIPALS`
  and removes nothing. `ENABLED_INTEGRATIONS` is unchanged. The stale-base guard (`DEPLOY_BASE_REF`) is present in the
  release's `deploy-to-ec2.sh`.
- **Authority:** the principal values are Andrew's, recorded at `PART_D_RECORD_20260930.md` @205c2e7f6c (sha256 only,
  values off-repo), together with his "Go with your recs".
- **Writers of the property:** N = 2, as the ask states. `tier.resolve_tier` handles persons, by principal.
  `token_broker._machine_tier` handles server-held identities, still by email roster. The issuer's step 4 ran both over
  9 identities and found 0 deltas.

## Guards

- **K1 -- base at upload.** The act and any rollback run with `DEPLOY_BASE_REF`:
  - the act declares the live full sha `42c52ed4d9...`;
  - the rollback declares the release sha.

  If the live ref moves before upload, this half is VOID. The guard in the release's script enforces it.
- **K2 -- the unconfirmed write-capable pair.** The ask names it as risk left: the Opal Bloomberg pair has no second
  source, and step 11 exercises only the admin pair. If it is wrong, that identity falls to the lowest tier. That would
  break the daily Bloomberg dashboard upload (`opal_data_refresh_upload`) and every other write this box's operator
  session makes. So the verify window adds one `/mcp` call AS the Opal Bloomberg principal, and its audit tier must read
  the write-capable tier. A lower tier triggers the same rollback as step 11.
  - Who can make that call is measured, not assumed: this seat's opalgateway session reads `whoami` = Andrew@opalinvest.com
    (~23:5xZ), so it is NOT that principal.
  - The call needs a session signed in as the Opal Bloomberg account, for example the 0.0.3_BG_BBGTerminal seat or the
    operator's `/bbg-send` session. The issuer names it in the ledger before the GO.
  - If no such session is available in the window, the fallback is a `/bbg-send` dry run (`dry_run=True`, no pipeline)
    as that account right after the release, with the rollback armed. Its tier is read from the audit row.
  - Alyssa's pair already has its second source, her grant key.
- **K3 -- read-back.**
  - `/health` returns 200;
  - the shipped md5 equals the release bytes;
  - the tool list AFTER equals BEFORE (58);
  - `ENABLED_INTEGRATIONS` is unchanged (6 ids);
  - `FIRM_ROLE_ARNS` is present in the live `.env`;
  - the admin call resolves `MASTER_ADMIN` (step 11);
  - K2's call resolves write-capable.

This half covers both branches of every leg in the ask's s.2-s.4. It does not cover a moved base, a changed pin, a
deploy without the guard, or any Terraform, grant, secret or ALB change.

-- 3.0.0_SA_CVO~O
