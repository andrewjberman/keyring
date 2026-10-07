# NFRA_CTLPLN -- the Dell identity root applied at site Z -- never-widen half (COO), `2.0.0_SA_COO~Z`, 2026-10-07 ~04:3xZ

**Authority:** Andrew, verbatim, relayed from the laptop CTO terminal ~04:2xZ by `0.0.0_AB_MSTR~Z` (msg 30565): "Where is the Dell
Keys? i want that issued". The route to site Z is MSTR~Z's msgs 30561 and 30565. **Pairs with:** the CTO half
`org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SIGNOFF_CTO_HALF_NFRA_CTLPLN_DELL_IDENTITY_SITEZ_APPLY_20261007.md`
@bbca23131f. **Executor:** `0.7.0_AE_CloudOps~RV`, order
`org/tier2_senior/0.7.0_AE_CloudOps~RV/task_orders/NFRA_CTLPLN.TO-DELL-1.dell-identity-apply-site-z.md`.

**This half covers leg (1) ONLY: the identity apply.** Leg (2), the two access keys, is `0.0.0_AB_MSTR~Z`'s act under the CTO
half's section 5. Leg (3), the agentbus root, is NOT covered by either half: `infra/aws/terraform/nfra-ctlpln-agentbus/` has 0
files at origin CLOUD `0ae63f9dbf` (its build order `NFRA_CTLPLN.TO-CT-b-3` reads pending).

## THE ACT

ONE `safe-apply` of `infra/aws/terraform/nfra-ctlpln-identity/` from a DETACHED worktree at EXACTLY origin CLOUD `0ae63f9dbf`
(the root's build commit `002f93bacd` is its ancestor), under ONE NEVER-2 entry. The plan is graded UNTARGETED first, and the
apply runs ONLY if the plan reads exactly `10 to add, 0 to change, 0 to destroy` with no `aws_iam_access_key`. Any other plan is a
STOP and a report; nothing is applied.

## THE BASE, read live by this seat at signing (~04:3xZ) -- and the rollback

| object | value at the base | rollback |
|---|---|---|
| user `cloudops-dell1-agent-user` | NoSuchEntity (`iam get-user`) | destroyed with the root |
| user `cloudops-dell2-agent-user` | NoSuchEntity | destroyed with the root |
| group `cloudops-dell-agents-group` | NoSuchEntity (`iam get-group`) | destroyed with the root |
| the three policies | declared in the root; not read live by this seat (the plan's 10-to-add is the measure) | destroyed with the root |
| the root's Terraform state | key `nfra-ctlpln-identity/tfstate` in `opal-313476888478-terraform-state`; no prior apply is known | -- |

**Rollback:** one `safe-apply` of a destroy of this root. It reaches only the ten resources the root created; nothing existing
references them. It is clean only while neither user holds an access key: once leg (2) has run, the key is deleted first.

## WRITERS OF WHAT MOVES (NEVER-1)

- **The ten IAM resources: N = 1 writer,** this root's apply. No other Terraform root and no script names these identities
  (the names are new; the base reads NoSuchEntity on all three principals).
- **Nothing existing moves:** no existing user, group, role or policy is in the root.

## WHAT THE IDENTITIES WILL BE ABLE TO DO (read from the three policy documents at `0ae63f9dbf`)

- `cloudops-dell-agent-deploy-policy` (the group's; 8 statements): Allow S3 object read/write/list on `opal-*`; Allow 32 deploy
  actions on `*` (Lambda code and configuration updates among them); Allow 3 SQS send actions on 4 named inbound queues; Allow 36
  read-only actions on `*` for a Terraform plan; and four Deny statements: every IAM write, every CloudTrail write, deletes on
  `opal-data-*`, and table and database deletes.
- `cloudops-dell1-agent-bus-policy` / `cloudops-dell2-agent-bus-policy` (one per user; 1 statement each): receive and delete on
  the user's OWN inbound queue prefix only (`agentbus-global-dell1-queue*`, `agentbus-global-dell2-queue*`).
- **The CTO half's section 3 names the reach this grant carries beyond its description** (code update on any Lambda reaches that
  Lambda's role; S3 put includes overwrite; `opal-*` is cross-firm). This half adopts that reading and adds nothing to it.
  It is for Andrew; it does not gate his order.
- **The two inbound queues the bus policies name do not have to exist for this apply** (a policy on a queue ARN pattern applies
  without the queue). They are leg (3)'s, which is not signed.

## EXPECTED OUTCOMES (both branches)

| check | before | expected after | if not |
|---|---|---|---|
| the plan | -- | exactly 10 to add, 0 to change, 0 to destroy; the ten addresses of the CTO half's section 1; no access key | STOP before any apply; report the plan as read |
| `tests/check_identity.py`, `tests/simulate_policy.py` | pass statically (the laptop's cell) | pass at `0ae63f9dbf` before the apply | STOP |
| `iam get-group` | NoSuchEntity | the group with exactly the two users | finish in-session or destroy the root; say which |
| `iam list-access-keys` per user | the user does not exist | 0 and 0 | a key that this apply did not create is a STOP and a row: something else wrote it |
| the three policies | absent | present, their documents equal to the JSON files' bytes | destroy the root |
| a partial apply (some of the ten created, an error on the rest) | -- | re-run the same `safe-apply` to converge; if it cannot, destroy what exists | the entry stays open until the state and the world agree |

## SIGNED

`2.0.0_SA_COO~Z`, 2026-10-07 ~04:3xZ, for leg (1) only, on the plan shape above.
