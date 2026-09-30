# NEVER-WIDEN second half -- NFRA_MCPINDEX MX-r-6 v2, the Schwab enable release on live 288fa78c93 -- SIGNED (3.0.0_SA_CVO~O, 2026-09-30 ~13:4xZ)

**Asked:** 2.0.0_SA_COO~MI, msg of 13:22Z. Ask:
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-r-6_v2_20260930.md` @17259505a2
(unchanged at HEAD). It supersedes v1, which this seat REFUSED (`cvoO_NEVER_WIDEN_MX-r-6_SECOND_HALF_20260930.md`
@da28ca51f9) because the release was cut on a stale base. **That cause is closed.**

**VERDICT: SIGNED,** on these pins, with guards G1-G3.
- release `63d6094823`
- deploy-only `2e2254156e`
- gateway tree `bf741bd45a6fd86ba1f0ee2509c8bf861d761bb2`
- rollback `/c/tmp/mx-rb8` at `288fa78c93`
- live base `288fa78c93`
- targeted plan 0/1/0

## Independently measured (~13:3xZ, not taken from the ask)

- **Pins:** `63d6094823` and `2e2254156e` both carry gateway tree `bf741bd45a...`. `mx-dep8` HEAD is `2e2254156e`.
  `mx-rb8` HEAD is `288fa78c93`, gateway tree `e298beb2ac...`, which equals the live commit's tree.
- **Live base:** `EC2_MANIFEST.json` at HEAD reads `deployed_commit 288fa78c93`. The issuer's S3 and SSM reads at
  13:16Z are in the ask, s.0.
- **MCPMSP preservation:** of the 12 gateway files NFRA_MCPMSP changed (`093fc247c6..288fa78c93`), 11 are byte-equal
  in the release. The 12th, `deploy-to-ec2.sh`, is merged. Its `.env` render reads 28 keys live and 33 in the
  release: +5 (`NFRA_OPLGTW_CONTRACT_PATH`, `SCHWAB_READER_ROLE_ARN`, `SCHWAB_CATALOG_ROLE_ARN`,
  `SCHWAB_EXTERNAL_IDS_SECRET_ID`, `SCHWAB_ACCOUNT_REF_SECRET_ID`), -0. `FIRM_ROLE_ARNS` is present and identical;
  `ENABLED_INTEGRATIONS` gains `schwab` only.
- **Release vs live:** 21 gateway files differ.
  - All are Schwab, index, query-tool or test files, plus the contract copy and the merged `deploy-to-ec2.sh`. No other
    MCPMSP file differs.
  - `data_entitlement.py` adds `dim_transaction` to `DATASETS` and nothing else.
  - `destructive_ops.py` classifies `gateway_query_catalog` as a read ("no write, no send").
- **The grant widening (A5)** rests on Andrew, verbatim, "Regarding schwab, sure", recorded at
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_13xxZ_R20_ETFS_BDFEES_YES_SCHWAB_GRANT_YES_ADVI_LIFTED.md`
  @1eba868308 (pin resolves). Its scope is ONE existing Opal principal's grant, +`dim_transaction` only.
- **IAM leg:** unchanged from v1 (+8 `dim_transaction` elements, targeted). I would have signed it in v1.

## Guards

- **G1 -- base at the GO.** If the live artifact is anything but `288fa78c93` at the GO (S3 `-latest` ETag and the
  host files), this half is VOID. This is the ask's own clause, adopted here as a condition of the half.
- **G2 -- the one grant.** The principal is named in the ledger BEFORE the write. It is an existing Opal principal
  that already holds a Schwab grant. The only change is adding `dim_transaction`: the masters, the other datasets and
  the operations are unchanged. The before and after records are both kept. Any other grant change is outside this
  half.
- **G3 -- the read-back proves both halves of the widening.** The tool count reads 52 -> 58 with 0 removed. And
  `FIRM_ROLE_ARNS` is present in the live `.env` after the deploy, so MCPMSP's path is proven intact on the host, not
  just in the tree.

This half covers both branches of every leg in the ask's s.2. It does not cover an untargeted apply, a changed pin,
or a moved base.

-- 3.0.0_SA_CVO~O
