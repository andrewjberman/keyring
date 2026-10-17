# TO TCKT_EARLYWARN.TO-EWS-d1 -- deploy the Client Ops Early Warning runtime as ONE always-on container (fast-path)
<to_id>TCKT_EARLYWARN.TO-EWS-d1</to_id>
<project>TCKT_EARLYWARN</project>
<issued_to>0.7.0_AE_CloudOps~TM1</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-17 ~05:0xZ (row TCKT_EARLYWARN-D1-S1, BLOCKING, ruled by `1.0.0_SA_CTO~DELL1` msg 7335 (b)):** the BRIDGE bearer comes from site Z's gateway release and no secret holds it yet, so there is nothing to grant. DEPLOY NOW with the Schwab daily rules ON and the mail poller OFF. Requirement 3 stands unchanged (the cert secret only). The mail poller is off by LAUNCHER, not by a setting: `ews/` has no off mode (`config.py:46`, `bridge.py:203`), so the Dockerfile CMD composes `DailyRunner(store, silver.S3Source()).run_pending()` on a timer and never calls `build_poller` (your grant: the Dockerfile; no `ews/` change). Report in your final message that the store is SQLite on ephemeral task storage, so a restart re-runs `run_pending` from the first complete date, and the cost of that. When site Z names the bearer secret and its minter, widening the role to that one secret is its own amendment. Apply is released: requirement 6 proceeds.
**Directive:** D7 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `EWS-d-1` (FAST-PATH: the project runs no L1-L10 and carries no decomposition; the cell is this order) |
**outcome_ref:** runtime approved by Andrew, record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261016_1801Z_CLIENT_OPS_EARLY_WARNING_FAST_PATH.md` addendum 6 card 3 (VERBATIM "all recs approv ed"): "one always-on AWS container (~$10-15/mo) beside the gateway, routed to CloudOps (TCKT macro lane)" | **depends_on:** none

---

## WORKER FACE

### THE CELL

The Day 1 and Day 2 code of the Client Ops Early Warning is merged (`infra/aws/ec2/client-ops-early-warning/`, README there; commits up to ec8ff2668d). **Deploy it as ONE container and prove it runs, with nothing able to send.** Scope is exactly this deploy; the code is not yours to change.

**Requirements (the CTO's, `1.0.0_SA_CTO~DELL1` msgs 7313/7316; each one is a rule, not a hint):**
1. **One container**, always on, the cost class in the record (about $10-15 a month). Image built from `infra/aws/ec2/client-ops-early-warning/` (the entry point is the poller loop, `ews/poller.py` / `ews/bridge.py` `build_poller()`; `EWS_MODE` defaults to BRIDGE, keep the default).
2. **Reads, read-only:** the Schwab silver prefixes `s3://opal-data-assets/schwab/08335338/silver/` and `s3://opal-data-assets/schwab/08242234/silver/` (`s3:GetObject` and `s3:ListBucket` scoped to those two prefixes), nothing else in S3, and no S3 write of any kind.
3. **Secrets:** `secretsmanager:GetSecretValue` on `opal/ews/graph-app-cert` ONLY. The BRIDGE bearer (`EWS_MAIL_BEARER_SECRET_ID`): if the deploy needs it, STOP and file a BLOCKING surprise row naming the missing grant; do not widen the secret scope on your own.
4. **Nothing sends.** The task role has no `ses:*`, `sns:*`, `sqs:Send*`, no Teams or mail send, no outbound call to any customer-facing channel. The alert moratorium is lifted for this scope by Andrew's Teams ask, and the record says: nothing sends until he names the channel (open item).
5. **Names** come from `lib/opal_naming.py name()` only: `infra/aws/ec2/client-ops-early-warning/ews/names.py` `resource_names()` prints the task, role, items table, cursor table and schedule names. A builder REFUSAL is a missing registry row to add under `infra/logic/registry/` (CLAUDE.md rule 30), never a hand-typed name.
6. **Apply** through `safe-apply` (never bare `terraform apply`); open a NEVER-2 change-management ledger entry at the start (`org/critical_paths/change_management/` plus its sentinel in `org/critical_paths/.open_deploys/`) and close it at completion; commit the sentinel. If the deploy moves an image tag that another task family pulls, name every such family in the entry.
7. **If the container shares the gateway host** (`opal-gateway`, `i-07dccb1615503ac99`), tell `1.0.0_SA_CTO~Z` FIRST (a broker message, one ask, before the first apply). If it runs on its own task/host, say so in the report.
8. **Write the deploy manifest** `org/tier1_exec/0.7.0_AE_CloudOps~TM1/deliverables/EWS_DEPLOY.json` with exactly the keys `cluster`, `task_arn`, `role_arn`, `role_name`, `task_name`, `ledger_slug`; the checks below read it.
9. Report the monthly cost estimate and the sizing you chose.

### ACCEPTANCE

<criterion id="EWS-d1-AC1" cell_refs="EWS-d-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/TCKT_EARLYWARN_Q1/EWS_CHECKS/ews_check.py running</invocation><expect>EWS-RUN-OK</expect></criterion>
<criterion id="EWS-d1-AC2" cell_refs="EWS-d-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/TCKT_EARLYWARN_Q1/EWS_CHECKS/ews_check.py iam</invocation><expect>EWS-IAM-OK</expect></criterion>
<criterion id="EWS-d1-AC3" cell_refs="EWS-d-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/TCKT_EARLYWARN_Q1/EWS_CHECKS/ews_check.py ledger</invocation><expect>EWS-LED-OK</expect></criterion>

<expected_criteria>EWS-d1-AC1,EWS-d1-AC2,EWS-d1-AC3</expected_criteria>

`EWS-d1-AC1` -- the manifest's names equal what `name()` builds, and the one task reads RUNNING with one container. `EWS-d1-AC2` -- the role, SIMULATED (read-only `iam simulate-principal-policy`), may read the one secret and the two silver prefixes, and may not read any other secret, write S3, read bronze, or send. `EWS-d1-AC3` -- the ledger entry is closed and its sentinel committed. Run each from the repository root. At the base: `EWS-BAD FileNotFoundError: no deploy manifest at ...EWS_DEPLOY.json` on all three. The positive arms are unexercised until your first deploy; if a check misfires on a correct deploy, file a surprise row naming the line, and do not weaken it.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Read-only against Schwab silver; no write to any Schwab, Outlook or client store; the BRIDGE reads one mailbox (Andrew's) through the gateway as the record's addendum 4 allows, and nothing else.** No new alarm, notification, SNS topic, SES identity or Teams post. No change to `ews/` source. No `terraform apply` outside `safe-apply`. No rebase of a shared branch.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `TCKT_EARLYWARN-Z-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended to the investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
infra/aws/terraform/client-ops-early-warning/
infra/aws/ec2/client-ops-early-warning/Dockerfile
infra/aws/ec2/client-ops-early-warning/.dockerignore
infra/logic/registry/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/tier1_exec/0.7.0_AE_CloudOps~TM1/deliverables/
org/missions/D7/TCKT/TCKT_EARLYWARN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_EARLYWARN/decompositions/TCKT_EARLYWARN_DECOMP.md</decomp_doc> (FAST-PATH: the one-cell declaration file), cell `EWS-d-1`.
<owned_cells>EWS-d-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: EWS-d1-AC1, EWS-d1-AC2, EWS-d1-AC3. Instance at `org/missions/D7/TCKT/TCKT_EARLYWARN/deliverables/0.7.0_AE_CloudOps~TM1/TCKT_EARLYWARN.TO-EWS-d1.deploy-one-container.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> EWS-d1-AC1,EWS-d1-AC2,EWS-d1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the sizing and monthly cost, whether the container shares the gateway host (and the message to `1.0.0_SA_CTO~Z` if so), the three checks' output, the ledger entry, the manifest, commits and push state.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the runtime polls on its own clock (5 minutes in BRIDGE mode); no EventBridge or Windows schedule is created by this order.
comp-iam: RUN the role is the order's whole IAM surface; AC2 simulates it, and the lane runs comp-iam on the role after the apply.
comp-adversary: DECLARED-NOT-APPLICABLE the deploy is graded by a live RUNNING read and a read-only policy simulation.
risk: WORLD -- a new always-on container with read access to client custodial data; nothing it does leaves the account.
direct_act: false -- a seat order to the TCKT CloudOps lane, rule 34.
</preflight>

Source: CTO `1.0.0_SA_CTO~DELL1` msgs 7313 and 7316 (the ask re-routed to the issuer `2.0.0_SA_COO~Q1` because `~S1` is not live); record addendum 6 card 3. FAST-PATH on Andrew-direct 2026-10-16 ~18:0xZ; project registered @b6f505b393 with no PRD and no COO.
