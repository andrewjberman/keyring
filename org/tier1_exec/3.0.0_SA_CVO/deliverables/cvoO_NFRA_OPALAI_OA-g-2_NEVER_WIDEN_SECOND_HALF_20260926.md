# OA-g-2 -- never-widen sign-off, SECOND (non-acting) half: SIGNED

Signer: `3.0.0_SA_CVO~O`, a non-acting seat. It neither issues nor deploys this release. Recorded 2026-09-26 ~18:2xZ.
Asks: `1.0.0_SA_CTO~O` msg 26107 (14:37Z) and `2.0.0_SA_COO~O` file 20260926T172801Z (deadline 21:05Z).
Authority: Andrew's arming term, "Served output still moves only under a never-widen sign-off (CTO half + a second,
non-acting half)" (`ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md`). Tier 1 was paused at ~14:3xZ and resumed on
Andrew's "resume tier 1" (0.0.0_AB_MSTR~Z relay, 16:18Z). This half was written after the resume.

**The act this half covers, and nothing wider:** the opal-gateway narrow release of branch
`rel-nfra-opalai-portal-grant-gateway` @df724ef284 onto the live base c5f8099440. It is
`NFRA_OPALAI.TO-OA-g-2.portal-grant-release` as amended @2ae3e0a96d. The CTO half is
`deliverables/1.0.0_SA_CTO~O/RULING_OA-g-2_RELEASE_SIGNOFF_20260926.md` @321a726fc6. This half does NOT sign OA-g-3,
the write of a portal-only grant for Alyssa Keith. That write is a separate served act and needs its own two halves.

## Blast radius, re-read by this seat rather than taken from the CTO half

| claim | this seat's read, 2026-09-26 ~18:1xZ | holds |
|---|---|---|
| exactly 5 files, gateway only | `git diff --stat c5f8099440 df724ef284 -- infra/aws/ec2/opal-gateway`: admin_grants.py, asker_scope.py, data_entitlement.py, ops/schwab_entitlement_admin.py, tests/test_portal_grant.py (411+/18-). The whole-tree diff outside the gateway is empty | yes |
| base = the live release | c5f8099440 is an ancestor of df724ef284. Live: `opal-gateway-latest.tar.gz` ETag fc23bd5d = `opal-gateway-c5f8099440.tar.gz`; EC2_MANIFEST deployed_commit c5f8099440; public `/mcp` 401 (the gateway's own refusal); 0 open deploy entries for this act | yes |
| a record without `portal_channels` parses exactly as v1.1 | `data_entitlement.py:233-237` @df724ef284: the scope must be exactly the six v1.1 dimensions, or those six plus `portal_channels` | yes |
| **DELTA = 0 at GO: no record carries `portal_channels`** | a full read-only scan of `gateway-access-state-table`: 141 items, no LastEvaluatedKey; record types oauth_refresh_family 129, oauth_client 4, operator_audit 4, principal_profile 3, other 1; **0 items carry `portal_channels`, and 0 are data_entitlement records at all**. OA-g-3 has not run | yes, re-measured 4 h after the CTO half |
| writers of the property (NEVER-1: N writers = N rules) | the operator path `ops/schwab_entitlement_admin.py` (`prepare`/`activate`) is the one rule; the MCPORTAL grant writer calls the same functions and is not deployed | 1 rule, read |

## Guards at GO, read from the amended order @2ae3e0a96d

- The rollback trigger polls `/health` ON THE HOST over SSM, not the public URL, which always answers 302
  (`TO-OA-g-2:66-68`, the NFRA_OPALAI-Z-W8-S3 / Z-S28 fix). Not 200 within 90 s rolls back to c5f8099440.
- The rollback's halt gate is pre-acknowledged at arm time when STOP = 0 (`:59`). The accepted residual: a STOP that
  arrives between arm and rollback is not re-read. Rolling back is the safe direction.
- The MCP tool list is compared before and after on the host (`:70`). The CTO half's 46 = 46 must hold.
- The NEVER-2 ledger is opened before the upload and closed after it.

## Verdict

**SIGNED**, for the act above as bounded here. Both branches were read from the producer's rule. With today's table,
every grant takes the unchanged v1.1 path. After a portal-only record is written, only that person's answers narrow,
and that write is OA-g-3's to sign.

-- 3.0.0_SA_CVO~O
