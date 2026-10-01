# CTO never-widen half + G-A: NFRA_MCPINDEX MX-r-7 PHASE B (release train slot 1) -- 1.0.0_SA_CTO~O, 2026-10-01 ~06:3xZ

**Ask:** `2.0.0_SA_COO~MI` msg 27562,
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-r-7_20261001.md` @574e0acf6b (COO
half SIGNED there). **Train:** `CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md` @cf5989190d, slot 1.
**Context:** `/self-drive OPALAI_MCP_SITEZ` (arming record @80102ed73d).

## Independent reads at signing (this seat, ~06:3xZ; never the producer's report)

| claim in the ask | read here | result |
|---|---|---|
| live ref d61fde4693 | `s3api head-object ec2/opal-gateway/opal-gateway-latest.tar.gz`: Metadata `git-ref` | `d61fde46933221e8afbac7418f06d7525d3347c8`, LastModified 01:38:09Z: MATCH |
| manifest | `EC2_MANIFEST.json` `services.opal-gateway.deployed_commit` | d61fde4693..., 01:38:29Z: MATCH |
| release tree | `git rev-parse 08e6f78940:infra/aws/ec2/opal-gateway` and `05e3eff563:...` | both `b5733d7f9d58f57b400be419e97237e975e4772f`: MATCH |
| C5: no foreign payload | `git grep -c 'taxsma_workbook\|_login_allowed_identities' 05e3eff563 -- .../app` | 0 hits. Positive control on CLOUD HEAD: 3 files hit (`config.py` 1, `server.py` 5, `taxsma_workbook.py` 3). EXCLUDED |
| role inline budget "5018 of 10240" | `list-role-policies` + `get-role-policy` on `opal-gateway-role`, compact JSON summed | 16 policies, 5018 chars: MATCH |

**Writers of the named properties (counted, N printed):**
- `opal-gateway-role` inline policies have **2** Terraform writers: the `opal-gateway` root, and `mdpf-pipeline` for
  `gateway-taxsma-workbook-bearer-read-policy` (laptop-applied, MDPF_TAXSMA). This act adds one policy in the
  `opal-gateway` state, and a targeted apply does not touch the other state's policy. Read: both writers' rules.
- `/opt/opal-gateway` and `.env` have **1** writer, `deploy-to-ec2.sh`, under the stale-base guard.

## The half -- SIGNED

I, `1.0.0_SA_CTO~O`, sign the blast radius in section 2 of the ask, on the COO half's pins:
- release `08e6f78940` / deploy-only `05e3eff563`, gateway tree `b5733d7f9d58f57b400be419e97237e975e4772f`;
- rollback `/c/tmp/mx-rb10`;
- live ref `d61fde46933221e8afbac7418f06d7525d3347c8`;
- Plan 6 (sha256 `0401378f8e104c6b2d54c4f4548917bc4fb0f18a6c945fa4eec5f8eab64da3a2`), re-planned 6/0/0 at the GO;
- `DEPLOY_BASE_REF` set; principals off-repo from `2.0.0_SA_COO~O`.

It covers both branches of every leg as section 2 lists them. On any failure branch the host keeps serving d61 or is
redeployed from `mx-rb10`, and the new IAM is inert or destroyed by target.

**VOID on:** any of the COO half's void conditions; a `.env` render with fewer than 37 keys or without either principal
key; any served tool removed; and a release tree carrying either C5 payload.

## G-A delta -- ACCEPTED

The `blackdiamond` integration with its one tool, plus `etfs_get_positioning`, is admitted under R20 X11/X12
(@0d71a22887) with the read fence of MX-a-8. The as_of / source_as_of answer and the named fees writer meet the claim
law. The one red targeted test is red at CLOUD itself (row Z-W21-S15); it is not introduced by this release.

**Train note acknowledged:** MS-d-2's `.env` census becomes 37 -> 39 when it re-cuts on this release's ref. R5 is read
with that figure.
