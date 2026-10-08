# NFRA_CTLPLN -- every cell 2.0.0_SA_COO~C holds or plans, with write paths (for the CRO overlap check)

**Author:** `2.0.0_SA_COO~C`, 2026-10-08 ~17:2xZ. **Asked by:** `1.0.0_SA_CTO` msg 107015 (Andrew-direct ~17:1xZ, no duplication
with the three CROs). Scope of this lane: NFRA_CTLPLN only (the four-device control plane). Times are UTC and are estimates.

Shorthand: `ID/` = `infra/aws/terraform/nfra-ctlpln-identity/`; `ORDER` =
`org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-a-1.dell2-sendcommand-grant.md`; `SC` =
`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`; `DLV14` =
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~14/`.

## In flight

| # | Cell | State | Worker / worktree | Write paths | Expected finish |
|---|---|---|---|---|---|
| 1 | **CT-a-1 cell 2, grant widen** (AMENDMENTS 16, 17): 28 platform keys incl. `opal/mcp/graph-read-token`; audit-trail resource policy; audit-trail bucket policy; protected-function permissions; agentbus queue policy | BUILT. Plan measured by the issuer, read-only, 17:2xZ: `2 to add, 3 to change, 0 to destroy`. Proof row for AC5 being rewritten | worker `0.9.0_WK_NFRA_CTLPLN~14`, `C:/tmp/wk-ctlpln-16`, branch `wk-NFRA_CTLPLN-16` | `ID/dell_deploy_policy.json`, `ID/dell_create_policy.json`, `ID/dell_respol_policy.json`, `ID/iam.tf`, `ID/modules/routes_policy/`, `ID/tests/` (simulate_policy, check_identity, derive_vendor_secrets, vendor_secrets_census.json, derive_respol_actions, derive_protected_functions, render_routes_policy), `DLV14`, `ORDER`, `SC` | merge ~17:4xZ; both halves ~18:0xZ; apply by `0.7.0_AE_CloudOps` ~18:3xZ |
| 2 | **TO-APPLY for cell 2** (to be cut) | not cut | `0.7.0_AE_CloudOps` (Codex seat, laptop) | `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/`, `org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_*`, `org/critical_paths/change_management/`, `org/critical_paths/.open_deploys/`; the AWS IAM policies of the Dell group (nothing else in AWS) | ~18:3xZ |

## Parked (ordered)

| # | Cell | State | Worker / worktree | Write paths | Expected finish |
|---|---|---|---|---|---|
| 3 | **CT-a-1 cell 1, routes Deny off** (AMENDMENT 15; item 5) | PARKED by CTO ruling 106987 until cell 2 applies; the earlier worker died in the reboot with uncommitted edits on disk | none live; `C:/tmp/wk-ctlpln-14`, branch `wk-NFRA_CTLPLN-14` @cf65c77a41 | `ID/routes.tf`, `ID/modules/routes_policy/`, `ID/tests/simulate_policy.py`, `ID/tests/check_identity.py`, `ID/tests/render_routes_policy.py`, `DLV14`, `ORDER`, `SC` | start ~18:3xZ; apply ~20:0xZ |
| 4 | **CT-a-1 cell 3, IAM create/change on the Dell group** (item 4) | not cut; after cell 1 applies | none | `ID/dell_deploy_policy.json` (`DenyEveryIamWrite`, `DenyPassRoleExceptNamed`), `ID/dell_create_policy.json`, `ID/tests/`, `DLV14`, `ORDER`, `SC` | ~22:0xZ |

## Open, not cut (carried)

| # | Cell | Source | Write paths (expected) | Expected finish |
|---|---|---|---|---|
| 5 | **C-KIT-PYTHON: the kit leaves out awscli** (the kit's wheel writes `Python312\Scripts\aws.cmd`, which `.tools/aws.cmd` resolves first) | CTO msg 106960 (from dell1); REC: drop awscli from the kit | `org/devices/kit_python_required.json`, `org/devices/kit_python_census.py`, `org/devices/kit_python_pack.py`, `org/devices/test_kit_python.py`, `requirements.txt` only if the kit reads it there | after cell 4, or earlier on a free slot; ~1 h of work |
| 6 | **PutSecretValue narrowing** (Dells can overwrite any secret through the create policy) | handoff CARRIED | `ID/dell_create_policy.json`, `ID/tests/` | not scheduled; folds into cell 3 if the CTO agrees |
| 7 | **Pack per destination** (files carry a destination; a pack per box; proof that a box ignores another's files) | CTO msg 106843, row S26 | `org/devices/intake/` (intake_closure.py, intake_receive.py and their tests) | not scheduled |
| 8 | **Kit verifier normalisation** | row S22 | `org/devices/kit_python_*.py`, `org/devices/test_kit_python*.py` | not scheduled |
| 9 | Two stale comment lines above `apply_respol_allow` (they say "default (false)") | handoff CARRIED | `ID/iam.tf` | rides cell 1 |

## Closed this session

- `NFRA_CTLPLN.TO-GRAPH-1` (graph F3): CANCELLED @38282471e7, no fire (msg 107003). Graph F1 ships inside cell 2.

## Overlap notes for the CROs

- Nothing in this list touches `.tools/`, `.claude/skills/`, `.gitattributes`, `kill-maint.ps1`, `safe-commit.sh`, `/integrate`,
  the graph code (`infra/aws/globgrph/`), or any git configuration: the GitOps, GC and graph fast-fix surfaces are not written here.
- Shared surfaces this lane appends to: the project surprise channel `SC` (append-only).
- Worktrees this lane holds: `C:/tmp/wk-ctlpln-16` (live), `C:/tmp/wk-ctlpln-14` (parked, holds uncommitted edits: do not reap).
