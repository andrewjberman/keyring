# TO TCKT_MTADTA.TO-MD-i1 -- the Entra-app registration script, the secret container, the subscription starter (all dry-run by default)

<to_id>TCKT_MTADTA.TO-MD-i1</to_id>
<project>TCKT_MTADTA</project>
<issued_to>0.9.0_WK_TCKT_MTADTA~2</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D7 | **Fabric:** dell1 | **Decomp cell:** `MD-i-1` (`decompositions/TCKT_MTADTA_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`MD-i-1`, IDENTITY. The audit feed is not Microsoft Graph. PRD C-APP: ONE new single-purpose Entra application holds
`ActivityFeed.Read` on the **Office 365 Management APIs**, app-only, consented ONCE by Andrew (Cloud Application Administrator). It is
single-tenant, holds NO Graph permission, and the gateway's `M365-MCP-Graph` and `M365-MCP-Login` apps are untouched. PRD C-SECRET: the
credential lives in the estate's secret store under the id **`m365-metadata/trino/api-credentials`**, read by id at run time, never
printed, logged, written to the repository or committed. PRD C-FIELDS (a): the Entra sign-in feed `Audit.AzureActiveDirectory` is NOT
subscribed; the content types are exactly `Audit.Exchange`, `Audit.SharePoint`, `Audit.General`.

**You build the scripts and the Terraform container. You run NOTHING live:** registering the app, the consent, putting the secret value and
starting the subscriptions are release acts after the drain (Andrew's consent is his own act).

### BUILD

1. **`data/m365_metadata/scripts/app/register_app.py`** (stdlib plus lazy `boto3`; Python 3.9+ syntax):
   - `SECRET_ID = "m365-metadata/trino/api-credentials"`.
   - `build_plan() -> dict` with exactly: `display_name` (`m365-metadata-trino-collector`), `signin_audience` (`"AzureADMyOrg"`),
     `permissions` (a list of ONE dict: `{"resource": "Office 365 Management APIs", "permission": "ActivityFeed.Read", "type": "Role"}`),
     `graph_permissions` (`[]`), `secret_id` (`SECRET_ID`).
   - `store_secret(sm_client, value) -> None`: ONE call, `sm_client.put_secret_value(SecretId=SECRET_ID, SecretString=value)`. The value
     is never printed, logged, formatted into any message or returned.
   - `main(argv)`: DRY-RUN by default (prints the plan, makes no call). With `--apply` it would register the app through Microsoft Graph
     under the caller's own delegated token (read from an environment variable, never from a file in the repo), look up the service
     principal and the `ActivityFeed.Read` app-role id FROM Graph at run time (never hard-code the ids), add the one role, create a client
     secret, and call `store_secret`. Print the application (client) id and the consent URL for Andrew; never the secret. This path is not
     exercised in round 1; write it so that the dry run and `build_plan` cover everything a reader needs to judge it.
2. **`data/m365_metadata/scripts/app/start_subscriptions.py`**:
   - `CONTENT_TYPES = ["Audit.Exchange", "Audit.SharePoint", "Audit.General"]`.
   - `run(call, apply=False) -> list`: returns a plan list of THREE entries `{"content_type": ..., "url": ...}` for
     `https://manage.office.com/api/v1.0/{tenant}/activity/feed/subscriptions/start?contentType=...` (the tenant id from an environment
     variable). With `apply=False` it makes NO call (the injected `call` is never invoked). With `apply=True` it POSTs each through `call`.
   - `main(argv)`: dry-run unless `--apply`.
3. **`data/m365_metadata/scripts/app/RUNBOOK.md`** -- the release acts, in order, as steps Andrew or a CloudOps seat can follow:
   check unified audit logging is on (`Get-AdminAuditLogConfig`, field `UnifiedAuditLogIngestionEnabled`; PRD Part V); run
   `register_app.py --apply`; Andrew grants admin consent at the printed URL; put the secret value; `start_subscriptions.py --apply`; note
   that first content may take up to 12 hours; how to read back the app's granted permissions (one permission, admin-consented). No
   secret value, tenant id or client id appears in the file.
4. **`data/m365_metadata/scripts/tests/test_app.py`** -- pytest: the plan has the single permission and no Graph permission; the secret
   value never appears on stdout or stderr; the subscription dry run makes no call.
5. **`infra/aws/terraform/trino/identity.tf`** -- TWO `aws_secretsmanager_secret` containers, each name taken from a local (the
   builder's `grade()` reads them CONFORMANT once the registry rows land; do not call the builder for them, no builder function emits secret
   ids): the app credential `m365-metadata/trino/api-credentials`, and the subject-hash key `m365-metadata/trino/subject-key` (the
   collector's HMAC key for mail subjects; its value is a random 32-byte string put at the release act). Each has a short description and a
   30-day recovery window. **No `aws_secretsmanager_secret_version`, no `secret_string`, no value of any kind.** No
   SNS, alarm or notification resource.

### ACCEPTANCE

<criterion id="MD1-i1-AC1" cell_refs="MD-i-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_i1.py app</invocation><expect>I1-APP-OK</expect></criterion>
`MD1-i1-AC1` -- one permission, app-only, single tenant, no Graph permission, the ruled secret id, and the secret value never printed.

<criterion id="MD1-i1-AC2" cell_refs="MD-i-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_i1.py subs</invocation><expect>I1-SUBS-OK</expect></criterion>
`MD1-i1-AC2` -- three content types, none of them the sign-in feed, and no call without `apply`.

<criterion id="MD1-i1-AC3" cell_refs="MD-i-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_i1.py tf</invocation><expect>I1-TF-OK</expect></criterion>
`MD1-i1-AC3` -- `identity.tf` declares the secret container and no secret value.

<expected_criteria>MD1-i1-AC1,MD1-i1-AC2,MD1-i1-AC3</expected_criteria>

Dry-run at the base 2026-10-16 ~06:5xZ: AC1 `APP-REFUSED missing ...register_app.py`, AC2 `SUBS-REFUSED missing ...start_subscriptions.py`,
AC3 `I1-TF-REFUSED no identity.tf` -- each FAIL as expected. Run from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **WORLD by the gate's path floor; NOTHING is run live.** No Microsoft, Graph, Management API or AWS call; no `--apply`; no
  `terraform apply`/`init`. Tests use synthetic values only; no tenant id, client id or secret is written anywhere.
- The Terraform file is one of four in the root `infra/aws/terraform/trino/`; you write ONLY `identity.tf`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `TCKT_MTADTA-D1-W2-S<k>`), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_TCKT_MTADTA~2 <0.9.0_WK_TCKT_MTADTA~2@opal.agent>"`, `-F` a message
  file you write with the Write tool, and `-- <paths>`.

<paths>
data/m365_metadata/scripts/app/register_app.py
data/m365_metadata/scripts/app/start_subscriptions.py
data/m365_metadata/scripts/app/RUNBOOK.md
data/m365_metadata/scripts/tests/test_app.py
infra/aws/terraform/trino/identity.tf
org/missions/D7/TCKT/TCKT_MTADTA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP.md</decomp_doc> (round 1), cell `MD-i-1`.
<owned_cells>MD-i-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: MD1-i1-AC1, MD1-i1-AC2, MD1-i1-AC3. Instance at `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.9.0_WK_TCKT_MTADTA~2/TCKT_MTADTA.TO-MD-i1.app-secret-subscriptions.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> MD1-i1-AC1,MD1-i1-AC2,MD1-i1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three check lines, the plan dict printed by `register_app.py` (dry run), the `pytest` summary line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: DECLARED-NOT-APPLICABLE for this cell -- it creates no AWS principal; the Entra permission is read back at the release act.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round. Release acts 2-3 (decomposition) carry the consent card to Andrew when this order drains.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.2 C-APP, C-SECRET, C-FIELDS (a), SURFACE MANIFEST R1 C3, OPEN AT ANDREW (the consent); decomposition cell MD-i-1.
