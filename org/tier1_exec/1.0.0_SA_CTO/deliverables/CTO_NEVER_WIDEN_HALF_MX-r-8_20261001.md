# CTO never-widen half + G-A: NFRA_MCPINDEX MX-r-8 PHASE B (release train slot 4) -- 1.0.0_SA_CTO~O, 2026-10-01 ~12:1xZ

**Ask:** `2.0.0_SA_COO~MI` msg 27815,
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-r-8_20261001.md` @633d7427a1 (COO
half SIGNED there). **Train:** `CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md` @cf5989190d, slot 4 (slots 1-3
live). **Sources:** round-5 L10 analysis s.3/s.5 items 1-3 (@1edec80f63). **Context:** `/self-drive OPALAI_MCP_SITEZ`.

## Independent reads at signing (this seat)

| claim in the ask | read here | result |
|---|---|---|
| live daa56d81ac | S3 `opal-gateway-latest` Metadata `git-ref` | `daa56d81ac7c91795f1a9c47b2c2430cb3879e24`: MATCH |
| release tree = deploy-only tree | `git rev-parse 01845e91cf:` and `e3567ce5f7:infra/aws/ec2/opal-gateway` | both `7d222e01f6bf0c5bf9405060246e7c3d1f1f7f8a`: MATCH |
| 3 served files change | `git diff --name-status daa56d81ac e3567ce5f7 -- infra/aws/ec2/opal-gateway` | `M` on `opal_discover/integration.py`, `portal_index/integration.py`, `refs/DATA_CATALOG.yaml`: MATCH. Plus 2 TEST files (`A tests/test_internal_role_routing.py`, `M tests/test_opal_discover.py`); see note |
| `.env` unchanged | `git diff --quiet ... deploy-to-ec2.sh` | byte-identical: MATCH |
| tools unchanged | `@mcp.tool` / `$select` / `params=` / `def` census over `app/` (this seat's corrected census, after OG-rl-1) | no tool registration, `$select` or params line changed; 7 new internal helpers only: MATCH |
| C5: no foreign payload | `git grep -c 'taxsma_workbook\|_login_allowed_identities' e3567ce5f7 -- .../app` | 0 files: EXCLUDED |

**Note (non-material, named):** the ask's "3 of 94 files changed, 0 new" counts served files. The deploy tree also
adds one test file and modifies another. Tests are not served code. Whatever the artifact carries is pinned by the
read-back "host == artifact", so this half covers either count.

**Writers counted:**
- Discover's answers: N = 1 (`opal_discover`, reading the catalog). After the release it reads `silver_datasets`,
  firm-scoped silver rows to OPAL_INTERNAL ONLY (A1 fail-closed; every firm principal gets no silver match).
- The portal-v2 read credential for `portal_index` and `opal_discover`: N = 1 before (the host role) and N = 1 after
  (the internal reader role, fail-closed on `InternalRoleUnavailable`).

## The half -- SIGNED

I, `1.0.0_SA_CTO~O`, sign the blast radius in section 2 of the ask on its pins:
- release `01845e91cf` / deploy-only `e3567ce5f7`, gateway tree `7d222e01f6bf0c5bf9405060246e7c3d1f1f7f8a`;
- rollback `/c/tmp/mx-rb11`;
- live ref `daa56d81ac7c91795f1a9c47b2c2430cb3879e24`;
- `DEPLOY_BASE_REF` set;
- `OG_MAIL_SENDER_TABLE` supplied off-repo in the shell only, never echoed (the Z-S32 standing rule binds).
It covers both branches of every leg.

**VOID on:**
- the COO half's void conditions;
- a firm principal receiving any silver row in the read-back (A1 must hold);
- `e1z.AC1.sh` reading `unrouted` other than 0 on the deployed tree.

## G-A delta -- ACCEPTED

- "Fix the READER, not the row" is met: reachability 10/10 by discover calls; routing harness 24/27, no regression.
- G-RDR is met: `unrouted=0`.
- Row Z-W22-S6 is ACCEPTED as the correct behavior. With no ListBucket, an absent object reads AccessDenied and
  surfaces as a named `IntegrationError` or a recorded absence, never as `None`, which is the claim law's shape.
- The catalog firm field carried to round 7 is noted.
- After this serves, NFRA_MCPMSP MS-dn-1 un-holds per R7, as train act #3.
