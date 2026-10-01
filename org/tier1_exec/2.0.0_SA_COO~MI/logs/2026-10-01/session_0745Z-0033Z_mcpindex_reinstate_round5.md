# 2.0.0_SA_COO~MI -- session log -- 2026-09-30 07:45Z -> 2026-10-01 00:33Z -- NFRA_MCPINDEX reinstatement, round 5

**archetype:** COORDINATE
**secondary_archetypes:** DEPLOY, VALIDATE

## Summary

The seat was respawned on Andrew's order to bring MCPINDEX back online, and round 5 was cut from 1.0.0_SA_CTO~O's
reinstatement rulings B1-B9 (@4e598ab7be) against PRD v0.6 (@e91ce9a0d5).

Delivered:
- **Schwab enabled on the gateway, live.**
- **Tools completed on CLOUD:**
  - `gateway_query_catalog` (query_v0 as an MCP tool);
  - Schwab `dim_transaction`;
  - `etfs_get_positioning` (ETF);
  - `blackdiamond_list_fees` (BD).
- **Alyssa's first Schwab grant.**

One incident: the v2 release overwrote another seat's gateway release. It was rolled back the same hour, and the
stale-base guard was built into the deploy script.

## Work done

1. **Respawn and startup.** `/watcher`, registration, inbox (30 of 30 READ), startup protocol. `/canonical-drive` cron
   re-armed off the LIVE_ARMS pairing row.
2. **Round-5 issuance** @b2ead0491d, drained @2cae2db258. Seven cells:
   - MX-s-15, MX-q-3, MX-r-6;
   - MX-a-8, MX-t-13, MX-r-7;
   - MX-t-12 (held).
   Fan-out 3 chains, cap 8. Every build check dry-run read FAIL at base.
3. **Completed this round, each re-graded by the issuer on the branch and drained:**
   - MX-a-8 @2f81e5aa77;
   - MX-s-15 @46587d5134;
   - MX-q-3 @b26d0b3ae0;
   - MX-t-10 (round 4) @29a40f5d4c;
   - MX-t-13 @d3b0efe5c6.
4. **MX-r-6, the Schwab enable release.**
   - v1 was VOID: the base moved under it, and I had signed the COO half on a base I did not re-measure.
   - v2 was deployed over 2.0.0_SA_COO~RV's 4ce7946426 and ROLLED BACK under plan A (CTO msg 27224). ~RV
     restored the host; this seat rolled back IAM through safe-apply (0/1/0). Row Z-S68.
   - v3 was cut by REF on 4ce7946426, carrying the `DEPLOY_BASE_REF` stale-base guard (6/6 tests). Halves: COO
     @20599c0c29, CTO @c0308f8b75, CVO @5c54630648.
   - GO on Andrew's "recs approved, proceed" (@2bd24e1ac6). LIVE 42c52ed4d9 at 18:33:41Z. Ledger closed @9a9bccc871.
   - Branch drained @d805cc536b.
5. **Alyssa's Schwab grant** (Andrew "agreed" @29bc46d827, scope per @2bd24e1ac6). Written at 19:15:29Z via the
   admin tool as `opal-gateway-access-admin`. Record @c9be59c0c7.
6. **R20 path.**
   - The LEGACY-READ waiver cannot admit NEW literals (row Z-S65).
   - Andrew's naming exception (@1eba868308) required the gate edit cb4296f508. MSTR~Z's pull of it was refused
     once, then landed at 7d50db9064.
   - This seat computed 8 r20_exception entries (@b9d1b053bc); the CTO landed them (@0d71a22887).
   - That un-held MX-t-10, MX-t-13 and MX-r-7.
7. **MX-t-12 (advi):** released by Andrew, then held again. The naming limb refuses the key, and the objects are a
   frozen twin. Carried to L10 (Z-S67).

## MCP traffic

About 60 messages handled. Significant ones:
- **CTO rulings:** 27022, 27068, 27114, 27132, 27162, 27198, 27224, 27231, 27303, 27365, 27367, 27415.
- **Signers:** CVO refusal 27131 and signings.
- **Gateway coordination:** COO~O 27307/27389, ~RV 27202/27206/27213/27230, MSTR~Z 27258/27269/27339, ~MS 27444.
- **Sent:** asks for 3 sets of never-widen halves; the incident escalation (27204/27222); the gateway hold and its
  release.

## Files Modified

See the commit messages (41 commits by this author since 07:40Z). Key ones:
- issuance b2ead0491d;
- amendments a73e9cf57e, a1437edaf7, 2c73ff3923, 4b0265036a, fa51666958, af90a84e00, fc97abbdf7, d4753af0d2,
  0b0a6f8157, 4f7032da3b, b0f54d5a1f;
- asks 3084e75259, 17259505a2, 20599c0c29;
- the rollback ledger 249b9233a6 / 4b14925ac4;
- grant record c9be59c0c7;
- R20 entries b9d1b053bc;
- drive logs.

## Deployment Sequence and Verification

- **v2 (14:41:23Z) ROLLED BACK.**
  - Host restored by ~RV at 15:23:02Z: 80/80 files, /rivalfunds 401.
  - IAM: safe-apply "Apply complete! Resources: 0 added, 1 changed, 0 destroyed." Read at 15:59:18Z: dim_transaction
    explicitDeny on both masters; targeted re-plan "No changes".
- **v3 (18:33:41Z) LIVE.**
  - Read-back SSM b6da75a0 (18:44:59Z): /health 200, /rivalfunds 401, ENABLED_INTEGRATIONS 6 ids incl schwab,
    FIRM_ROLE_ARNS kept, tools 52 -> 58, host 87/87 == artifact.
  - r6.AC1 PASS and r6.AC2 PASS.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-iam role | PARTIAL | opal-gateway-role resolved; gateway-schwab-read-role "no match" (TF index gap), so the APPLIED plane was read with iam simulate-principal-policy |
| to-pipeline-gate --rounds | PASS | rounds 2/3/4 = 7/7/9 orders before the cut |
| naming-gate --diff (dry runs) | PASS | the decisive instrument for the R20 path; a scratch false-RAISE (sparse cone missing LEGACY_SERVED_PATHS.json) was caught and re-run |
| deploy_ledger.py list/open/close | PASS | 20 of 20 sentinels scanned on each read |

**What worked:** the naming gate's own functions (`r20_exception_ok`, `--diff`) settled the waiver questions exactly.
**What failed:** none of the comp tools resolve the reader role by name.
**Gap found:** nothing guarded a gateway deploy against a moved base. That is now closed by the
`deploy-to-ec2.sh` `DEPLOY_BASE_REF` guard.

## Blockers

- **MX-r-7 (BD + ETF release):** BLOCKED on sequencing. COO~O's OG-t-2 deploys first; both of its halves are signed
  (@51df60aa1a, @045f6886d9), and the gateway still reads 42c52ed4d9 at 00:17Z. Ask sent to ~O (msg at 23:58Z).
- **r6.J1:** BLOCKED on a person. Alyssa's cold run needs her, in a fresh session with only the MCP connected.
- **MX-s-14 (round 4):** waits on its scheduled fires (B6).

## Current State

- **Gateway** i-07dccb1615503ac99 runs 42c52ed4d9: Schwab enabled, 58 tools.
  - `DEPLOY_BASE_REF` guard in `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
  - Contract `org/standards/NFRA_OPLGTW_CONTRACT.json` lists dim_transaction.
- **IAM:** gateway-schwab-read-role allows dim_transaction on both masters.
- **Grant:** gateway-access-state-table, Alyssa (6810043e/ad037ea5) at revision 2.
- **Round 5:**
  - complete: a-8, s-15, q-3, t-13, and t-10 (round 4);
  - r-6 LIVE, with J1 open;
  - r-7 ready to cut;
  - t-12 held for L10.
- **Worktrees:** wk-mcpindex-r5-15/-19/-20/-21 (all drained). Scratch trees: rb-gw-4ce7946, ng-r20-scratch,
  /c/tmp/mx-* release trees.
- **Push state:** LOCAL. Site-Z push is pending Andrew's word through 0.0.0_AB_MSTR~Z.

## Next Steps

1. [2.0.0_SA_COO~MI] When [2.0.0_SA_COO~O] reports OG-t-2 landed:
   - cut MX-r-7 PHASE A by REF on its ref (worker ~21);
   - ask for the halves;
   - deploy with DEPLOY_BASE_REF.
2. [Andrew / Alyssa] r6.J1 cold run: one Schwab position question and one transaction question.
3. [2.0.0_SA_COO~MI] After MX-r-7 and r6.J1, compile the round-5 L8 packet for [3.0.0_SA_CVO~O]. It carries:
   - t-12 (the advi source plus an R20 for advi);
   - the Schwab catalog row (CTO 27367);
   - the r6.AC1 slug defect (Z-W19-S20);
   - FWD-8 via Bloomberg.
4. [2.0.0_SA_COO~MI] Round 6, first cell: G-RDR, routing portal_index and opal_discover through MCPMSP's internal reader
   role (CTO 27414). Preconditions: [2.0.0_SA_COO~MS]'s internal_role.py merge hash, and the role applied.
5. Clean up the drained worktrees and scratch trees (rb-gw-4ce7946, ng-r20-scratch, the wk-mcpindex-r5-* worktrees
   once their branches are fully merged).
