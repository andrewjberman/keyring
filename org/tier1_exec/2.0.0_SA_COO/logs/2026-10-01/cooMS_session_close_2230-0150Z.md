# 2.0.0_SA_COO~MS -- NFRA_MCPMSP round 2: issuance, first drains, the release join -- session close 2026-09-30 ~22:30Z -> 2026-10-01 01:50Z

**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT, VALIDATE

Lane `~MS` (no lane folder exists; filed under the base-serial folder). Project NFRA_MCPMSP (D6), L5-L7, round 2.
Wind-down on Andrew's word (2026-10-01 ~01:45Z: "great lets wind down this session ... write a /log").

## Summary

Round 2 cut and issued in ONE issuance: 14 task orders covering the CTO's round-1 analysis E1-E5 plus E6 (added by the
CTO's amendment 27426 before the issuance). 7 workers were spawned on the chain heads, and 9 orders are merged to CLOUD.
The internal reader role is LIVE. A drain full-suite diff caught one regression from round 2 (MS-r-1's resolver broke
`tests/test_deploy_base_guard.py`). MS-r-1 is re-opened; its fix is built and passing in the worker's tree but NOT
committed (see Blockers). The narrow release MS-d-2 is the next act; it is waiting only on MS-r-1.

## Work done (commits; all by 2.0.0_SA_COO~MS unless noted; all LOCAL, see push state)

| commit | what |
|---|---|
| 94817979f9 | decomp v2 (round 2, 13 cells, 6 chains) -- prior window, cited for context |
| b90073c197 | ISSUANCE: 14 TOs + 31 check files + decomp addenda R2.8 (E6 -> MS-s-1) and R2.9 (10 cell ids renamed to the gate grammar `PREFIX-[a-z]{1,4}-[a-z]?\d+`) + row Z-S4; fanout N=7 of M=7, cap 8 |
| 9ebe03c465 | drain MS-sh-1 (agent sender-gate hook); opal_ai local DEV ff 61841f5 -> 32abfdb |
| c699184c33 | drain MS-ig-1 (app/internal_role.py; query_v0 via INTERNAL_READER_ROLE_ARN, unset = today's client) |
| ae2bceeeda | drain MS-r-1 first pass (R-4 mcportal at manifest commit, R-5 run_release_suites.sh) |
| bd3fc6fcc1 | drain MS-s-1 (safe-apply naming plan stage renders the targeted/planfile plan; 5/5 arms, base bytes 1/5) |
| 9de4e18403 | amend MS-rq-1 A1 (sender fields from entry args, never `user`) |
| 4da9321aa8 | drain MS-c-1 (reader census + 9-key DELTA baseline) -- channel conflict union-resolved |
| 44eb9726cf | amend MS-sg-1 A1 (four suites' fakes get member emails); MS-ir-1 handed; MS-dn-1 AC3 rewritten |
| b3f544ae45 | issuer status flip MS-ig-1 |
| 6e44ef41c6 | drain MS-ir-1 (internal reader role tf + firm Deny tf, Deny NOT applied) |
| 6dde3d31e1 | hand MS-ir-2 (targets named) |
| 1bcc2f6fd8 | drain MS-rq-1 (owned-gated refusal list + approve) |
| e8b9a3adaa | drain MS-sg-1 (gateway sender gate) -- channel conflict union-resolved |
| 968a6aa074 | issuer status flip MS-sg-1 |
| 5962217f50 | amend MS-r-1 A1 (re-opened on the drain suite diff) + check r1.AC3 |
| e719b4e6ad | drain MS-ir-2 (internal reader role LIVE; ledger closed) |
| 4daa5094ae | fix MS-r-1 order: stale first status tag -> history comment (unblocks row Z-W5-S1) |

## Task order state (round 2, 14 orders)

| order | slot | state |
|---|---|---|
| MS-c-1 census | ~1 | complete, merged |
| MS-ir-1 role + Deny tf | ~1 | complete, merged |
| MS-ir-2 role apply | ~1 | complete, merged; role LIVE |
| MS-ig-1 query_v0 route | ~2 | complete, merged |
| MS-sg-1 gateway sender gate | ~3 | complete, merged |
| MS-rq-1 refusal routes | ~4 | complete, merged |
| MS-r-1 release tooling | ~5 | RE-OPENED (A1); fix built and passing in /c/tmp/ms-5, uncommitted (order unblocked at 4daa5094ae) |
| MS-d-2 narrow release | ~5 | staged; inputs all merged except MS-r-1 |
| MS-dn-1 the Deny | ~5 | staged, HELD: G-RDR (MCPINDEX round 6), G-NW-E1 (never-widen pair), MS-d-2 live |
| MS-sh-1 agent hook | ~6 | complete, merged |
| MS-rn-1 replayable run | ~6 | staged, HELD: G-MSPID (Andrew "Not yet"), G-MSPCL |
| MS-sv-1 live refusal arm | ~6 | staged, HELD: G-MSPID, MS-d-2 live, MS-rn-1 session |
| MS-rx-1 replay | ~8 | staged behind MS-rn-1 |
| MS-s-1 safe-apply targeted plan | ~7 | complete, merged |

## Verification (issuer re-grades, each in the worker's own worktree before merge)

- Every merged order: all its checks re-run by the issuer, all PASS (lines in each drain commit message).
- LIVE reads: role `arn:aws:iam::313476888478:role/gateway-global-internal-reader-role` trust = `opal-gateway-role`
  only (iam get-role, read live); simulate: firm + global keys allowed on the role, gateway AssumeRole allowed, gateway
  still reads the firm key, no Deny policy attached.
- DELTA control (check e1z.AC3, rewritten): host-served bytes via `app.query_v0._fetch_capped` == S3 bytes read the
  same minute, 9 of 9 (SSM b7ccb688) -- the state the Deny must keep.
- Drain full gateway suite (`tests/`, AUDIT_PATH temp): base b90073c197 = 45 failing ids; merged e8b9a3adaa = 50. NEW =
  6, all `tests/test_deploy_base_guard.py` (MS-r-1); FIXED = 1 (`test_entitlement_admin::test_ogz2_ac08`); the other 44
  pre-existing (schwab_*, principal_cutover, data_entitlement_guard, deploy-adjacent, 3 asker ids that pass in isolation).

## Compiler Tools

| tool | use | result |
|---|---|---|
| comp-find (via Grep) | sibling-order census of `.tools/safe-apply.sh`, gateway test paths; status-tag census | PASS -- 2 LGIC orders named safe-apply, both complete |
| .tools/to-pipeline-gate.py (via safe-commit) | issuance + 5 amendments | FAIL then PASS -- refused 34 cell-id violations (renamed), then a literal `<status>` inside amendment prose |
| .tools/naming-gate.py | check e1t.AC1 dry-run + worker runs | PASS |
| iam simulate (`sim` helper) | e1a/e1z checks | PASS |
| comp-iam | not run: the rail pointed to it for one trust-document read; ran the raw read with a rail-checked marker (comp-iam reconciles policies, not a role's trust doc) |

What worked: dry-running every check at base caught 3 of my own check defects before any worker used them (host .env
not shell-sourceable; multi-line program mangled by json.dumps in SSM; native Python cannot open MSYS paths read from a
file). What failed: two order edits of mine tripped gates by side effect (a literal status tag in prose; a re-opened
order keeping its first status tag, which owned-paths-validate reads -- row Z-W5-S1). Gap: the seating lint parses
`0.9.0_WK_NFRA_MCPMSP~n` as `0.9.0_WK_NFRA` (ANNOUNCE mode, 14 false findings at the issuance).

## MCP traffic

4 significant: received CTO 27426 (E6 + G-MSPID "Not yet"; acked); sent `2.0.0_SA_COO~MI` 27444 (G-RDR ask); received
27445 (G-RDR = MCPINDEX round 6 first cell, preconditions internal_role.py + role live; acked); sent 27445-reply
(both preconditions met: c699184c33, role live at e719b4e6ad).

## Blockers

- **MS-r-1 (BLOCKED, evidence-cited; row NFRA_MCPMSP-Z-W5-S1):** the worker's two source edits are UNCOMMITTED in
  `/c/tmp/ms-5` (`deploy-to-ec2.sh` resolver reads the manifest with python json via cygpath; `tests/test_deploy_base_guard.py`
  rig fixture writes EC2_MANIFEST.json with mcportal_commit = m1, no assertion change). With them in place AC1 7 passed,
  AC2 resolved a3bff71ffa, AC3 6 passed. safe-commit refused the commit because the order's FIRST `<status>` tag still
  read complete. My fix (the stale tag -> a history comment, one tag `pending`) LANDED at 4daa5094ae, after a peer
  merge by `0.0.0_AB_MSTR` (origin/CLOUD 68e15a70df into CLOUD) closed. The order is now unblocked; what remains is the
  worker's own commit of its two edits.

## Current State (zero-context handoff)

- Branch CLOUD @ b40689cb0e (local). **Push state: LOCAL** -- origin/CLOUD @ 68e15a70df (ls-remote read 01:50Z); b90073c197,
  6e44ef41c6 and e719b4e6ad are NOT ancestors of it. opal_ai local DEV @ 32abfdb (not pushed). No push is mine (G-PUSH).
- LIVE in AWS: `gateway-global-internal-reader-role` + `gateway-global-internal-reader-policy` + the gateway's
  `gateway-global-internal-assume-policy` (ledger `org/critical_paths/change_management/20261001T0110Z_nfra-mcpmsp-r2-internal-role_deploy_completion.md`, CLOSED).
  The firm Deny (`mcpmsp_gateway_firm_deny.tf`, `aws_iam_role_policy.gw_firm_deny`) is NOT applied.
- Gateway host still runs 42c52ed4d9 (MCPINDEX's); none of round 2's gateway code is deployed yet (MS-d-2).
- Worktrees: /c/tmp/ms-1 (~1, done), ms-2 (done), ms-3 (done, ff to e8b9a3adaa), ms-4 (done), ms-5 (MS-r-1 uncommitted
  edits -- DO NOT remove), ms-6 (slot ~6, held orders, nested opal_ai), ms-7 (detached at b90073c197, used for the base suite run).
- Checks: `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/` (32 files + _root.sh).
- Surprise channel `INVESTIGATION_v1.Z.md`: rows to disposition at L10 -- Z-S4, Z-W1-S9/S10, Z-W3-S3..S6, Z-W4-S3, Z-W5-S1, Z-W7-S1.

## Next Steps

1. [2.0.0_SA_COO~MS] Respawn slot ~5 to `git merge CLOUD` (picks up 4daa5094ae) and commit its two edits in /c/tmp/ms-5,
   re-grade r1.AC1-AC3, merge, re-run the full suite diff (expect 44 base-only failures, 0 new).
2. [2.0.0_SA_COO~MS] Hand MS-d-2 to slot ~5 (narrow release from the deployed commit re-read at spawn; item 0 the
   admin_refusals hookup; `.env` gains INTERNAL_READER_ROLE_ARN and an EMPTY MSP_CALLING_IDENTITIES).
3. [2.0.0_SA_COO~MI] G-RDR as round 6's first cell (both preconditions sent).
4. [1.0.0_SA_CTO~O] + [2.0.0_SA_COO~MS] the never-widen pair G-NW-E1 for MS-dn-1 after MS-d-2 is live.
5. [Andrew] G-MSPID (the MSP calling identity) and G-MSPCL gate MS-rn-1 / MS-sv-1 / MS-rx-1; not a gate on anything else.
6. Round end: L8 packet; one slug to [1.0.0_SA_CTO~O] only after every order is terminal and every row dispositioned.
