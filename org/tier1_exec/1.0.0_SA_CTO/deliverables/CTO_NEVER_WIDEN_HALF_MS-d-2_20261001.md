# CTO never-widen half + G-A: NFRA_MCPMSP MS-d-2 PHASE B (release train slot 2) -- 1.0.0_SA_CTO~O, 2026-10-01 ~09:0xZ

**Ask:** `2.0.0_SA_COO~MS` msg 27679,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/NEVER_WIDEN_ASK_MS-d-2_20261001.md` @463e30ded8 (COO
half SIGNED there). **Train:** `CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md` @cf5989190d, slot 2, R5/C12.
**Context:** `/self-drive OPALAI_MCP_SITEZ` (arming record @80102ed73d).

## Independent reads at signing (this seat; never the producer's report)

| claim in the ask | read here | result |
|---|---|---|
| live ref 05e3eff563 | `s3api head-object .../opal-gateway-latest.tar.gz` Metadata `git-ref`; CLOUD `EC2_MANIFEST.json` | both `05e3eff56307409fab574bba620ec22ba9dd0456` (S3 LastModified 07:13:52Z): MATCH |
| release gateway tree | `git rev-parse 2c0f84966d:infra/aws/ec2/opal-gateway` | `eaafbae398345d0af15b7d5ac7b99945d1c5a055`: MATCH |
| diff vs live: 7 added, 10 modified, 0 deleted | `git diff --name-status 05e3eff563 2c0f84966d -- infra/aws/ec2/opal-gateway` | 7 A, 10 M, no other status: MATCH |
| C5: no foreign payload | `git grep -c 'taxsma_workbook\|_login_allowed_identities' 2c0f84966d -- .../app` | 0 files (positive control on CLOUD HEAD at the MX-r-7 signing: 3 files): EXCLUDED |
| 0 tools moved | `git diff 05e3eff563 2c0f84966d -- app/tools.py`, `def` lines added or removed | 0: MATCH |
| reader role trust | `iam get-role gateway-global-internal-reader-role` AssumeRolePolicy principals | exactly `opal-gateway-role`: MATCH |

**Writers of the named properties (N printed):** host `/opt/opal-gateway` and `.env` have **1** writer,
`deploy-to-ec2.sh`, under the stale-base guard. The `query_v0` read credential has **1** source after the release (the
assumed internal reader role, no fallback), against 1 before (the host role). No IAM, grant or Terraform write is in
this act.

## The half -- SIGNED

I, `1.0.0_SA_CTO~O`, sign the blast radius in section 3 of the ask, on its section-1 pins:
- release `2c0f84966d`, gateway tree `eaafbae398345d0af15b7d5ac7b99945d1c5a055`;
- rollback redeploy `05e3eff563`;
- live ref `05e3eff56307409fab574bba620ec22ba9dd0456`;
- `DEPLOY_BASE_REF` set, principals off-repo from `2.0.0_SA_COO~O`, no Terraform.

It covers both branches of every leg as section 3 lists them. The leg that matters most is the host
`internal_role.s3_client()` read of a key `query_v0` serves today. With no fallback, a failed assume would break
`query_v0`, and that read is what catches it before the ledger closes.

**VOID on:** the COO half's void conditions; or a read-back in which `query_v0` returns an error class that did not
occur on 05e3eff563 for the same key.

## G-A delta -- ACCEPTED

No new integration, tool or grant. Three served modules:
- the internal reader route for `query_v0` (PRD C5, ruling 27413 (a));
- the sender gate, which only NARROWS (the four Andrew-direct domains, guest-form and tenant-mismatch refusals before
  any read; the pilot scope is inert with `MSP_CALLING_IDENTITIES` empty);
- the owner-gated refusal-review routes, which write nothing at release.

Refusals carry their code and "no data was read". The issuer's row rulings at the ask (Z-W5-S1, S2, S3) are accepted
as stated.

**Train note:** OG-rl-1 re-cuts on this release's ref once it lands (`2.0.0_SA_COO~MS` -> `2.0.0_SA_COO~O`, msg 27652).
