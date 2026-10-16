# TO TCKT_MTADTA.TO-MD-x1 -- the door's repair: invoked-alias gating, a key allowlist, list_state, two aliases with one principal each, ListBucket out of the Deny

<to_id>TCKT_MTADTA.TO-MD-x1</to_id>
<project>TCKT_MTADTA</project>
<issued_to>0.9.0_WK_TCKT_MTADTA~5</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D7 | **Fabric:** dell1 | **Decomp cell:** `MD-x-1` (`decompositions/TCKT_MTADTA_DECOMP_R2.md`) |
**outcome_ref:** FWD-1, FWD-6, FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`MD-x-1`, the DOOR repaired. Round 1 built the access Lambda `globgrph-trino-access-lambda` (`infra/aws/lambda/globgrph-trino-access/handler.py`) and its
Terraform (`infra/aws/terraform/trino/access.tf`). READ both first; you edit both. The CTO ruled on three rows of the first build (PRD v0.4 C-ACCESS,
`org/missions/D7/TCKT/TCKT_MTADTA/prd/TCKT_MTADTA_PRD.md`, row C-ACCESS; and `ledger/CTO_RULING_R1_LISTBUCKET_AND_COLLECTOR_INVOKER_20261016.md`):

- **D1-S5.** The collector's execution role is the door's ONE non-member invoker, on its OWN alias, and on that alias the door allows exactly three
  operations: `put`; `derive_silver`, which answers a row count and no data; and `get_state` on the subscription-cursor key alone. Every other read is
  refused. The group's members use the other alias. The door decides from the invoked alias. Each alias admits exactly one principal.
- **D1-S4.** `s3:ListBucket` is NOT denied (a Terraform refresh of the bucket needs it). A listing shows table names, dates and sizes, so NO key
  segment may ever carry a person, an address or a file name. The door enforces that with a key allowlist.
- **D1-W3-S2 / D1-W1-S8.** Keys and prefixes must equal `lib/opal_naming` output; a test proves it.

### THE DOOR CONTRACT v2 (fixed by the decomposition; build to it exactly)

`handle(event, context=None, s3=None, log=print, silver_reader=None, silver_builder=None) -> dict`, `key_ok(dataset, key) -> bool`, `PREFIX`.
The alias is the last colon-separated field of `context.invoked_function_arn` when that ARN has 8 fields
(`arn:aws:lambda:<region>:<acct>:function:<name>:<alias>`). An unqualified ARN, an alias other than `collector` or `member`, or `context is None`
means NO operation is served: every op answers `{"ok": false, "error": ...}`.

| op | `collector` alias | `member` alias |
|---|---|---|
| `put {dataset, key, body_b64}` | served for datasets `bronze`, `state`, `gold` only, when `key_ok` | refused |
| `derive_silver {date}` | served; the answer is exactly `{"ok": true, "rows": n}` and nothing else | served (same answer) |
| `get_state {key}` | served ONLY when `key` is the cursor key | served for a key under `state/` or `gold/collection_coverage/` |
| `list_state {prefix}` | refused | served for a prefix under `state/` or `gold/collection_coverage/` only; answers `{"ok": true, "keys": [...]}` |
| `get_day {person, date}` | refused | served (round 1's behaviour: one of the eight, the person's rows in time order) |
| any other op, or a get of bronze | refused | refused |

`key_ok(dataset, key)` is a FULL MATCH against these grammars (bucket prefix `m365-metadata/trino/`), and nothing else is admitted; `..` is never admitted:
- bronze `bronze/audit_events/date=\d{8}/Audit\.(Exchange|SharePoint|General)_\d{8}T\d{6}Z\.json\.gz`
- silver `silver/activity_events/date=\d{4}-\d{2}-\d{2}/data\.parquet`
- state `state/subscription_cursor/current/cursor\.json`
- gold `gold/collection_coverage/date=\d{4}-\d{2}-\d{2}/coverage_\d{8}T\d{6}Z\.json`

`derive_silver` keeps round 1's behaviour (read every bronze object of the Eastern date, `silver_builder.build`, rewrite that silver partition). Every
call writes ONE log line `op=<op> outcome=<ok|refused|absent|error>`: never a body, a key, a person or an alias value. `lambda_handler` passes `context`
to `handle`.

### BUILD

1. **`infra/aws/lambda/globgrph-trino-access/handler.py`** -- the contract above. The constants stay; add `key_ok`, the alias gate and `list_state`.
2. **`infra/aws/lambda/globgrph-trino-access/tests/test_handler.py`** -- rewrite for the contract: each cell of the table above (served and refused),
   the fail-closed contexts, the key grammar (accepted: one builder-made key per dataset; refused: a file name, an address, a `person=` segment,
   a foreign prefix, `..`), `list_state` limits. The tests compare the module's `PREFIX` and a key per dataset with `lib.opal_naming.address(...)`
   output (the registry rows `m365-metadata` and `trino` landed in round 1; `lib/` is in your worktree).
3. **`infra/aws/terraform/trino/access.tf`** --
   - the Deny's `data_actions` loses `s3:ListBucket` and `s3:ListBucketVersions` (every object data action stays);
   - `aws_lambda_function.access` gets `publish = true`;
   - `aws_lambda_alias.collector` and `aws_lambda_alias.member` (names `collector` and `member`; `function_name = aws_lambda_function.access.function_name`;
     `function_version = aws_lambda_function.access.version`);
   - the group policy `aws_iam_group_policy.invoke` grants `lambda:InvokeFunction` on `aws_lambda_alias.member.arn` ALONE (not the function ARN);
   - one `aws_lambda_permission` admitting the collector role on its alias: `statement_id = "AllowCollectorRoleOnItsAlias"`, `action = "lambda:InvokeFunction"`,
     `function_name = aws_lambda_function.access.function_name`, `qualifier = aws_lambda_alias.collector.name`, `principal = aws_iam_role.collector.arn`
     (`aws_iam_role.collector` is declared in `collector.tf`, another cell's file, same root: reference it, never declare it);
   - the header comment states the alias design (ruling 2 of the decomposition) and the residuals in plain words;
   - nothing else changes; no wildcard principal; no alarm or notification resource.

### ACCEPTANCE

<criterion id="MD2-x1-AC1" cell_refs="MD-x-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_x1.py alias</invocation><expect>X1-ALIAS-OK</expect></criterion>
`MD2-x1-AC1` -- the collector alias serves put, derive_silver (a count only) and the cursor read, and nothing else; the member alias serves the reads and never a put; an unqualified, unknown or absent context is refused; a key carrying a file name is refused; every call is logged without a person or a file name.

<criterion id="MD2-x1-AC2" cell_refs="MD-x-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_x1.py tf</invocation><expect>X1-TF-OK</expect></criterion>
`MD2-x1-AC2` -- `access.tf` has the two aliases, a published function, the group policy on the member alias alone, the collector role's resource permission on its alias, and no ListBucket in the Deny.

<criterion id="MD2-x1-AC3" cell_refs="MD-x-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_x1.py keys</invocation><expect>X1-KEYS-OK</expect></criterion>
`MD2-x1-AC3` -- the key allowlist admits exactly the builder's keys for the four datasets and refuses a person, an address, a file name and a foreign prefix.

<expected_criteria>MD2-x1-AC1,MD2-x1-AC2,MD2-x1-AC3</expected_criteria>

Dry-run at the base 2026-10-16 ~08:3xZ: AC1 `X1-ALIAS-REFUSED ...` (the round-1 handler serves by op, not by alias), AC2 `X1-TF-REFUSED s3:ListBucket ... still in the Deny; no aws_lambda_alias ...`,
AC3 `X1-KEYS-REFUSED AttributeError: ... no attribute 'key_ok'` -- each FAIL as expected. AC1 and AC3 were driven GREEN against a throwaway reference outside the repository.
Run each from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **WORLD by the gate's path floor; NOTHING is applied or called live.** No `terraform apply`/`init` against the backend, no AWS call, no S3 access,
  no Lambda invoke. `terraform fmt -check` on your file is welcome (no network).
- `collector.tf` and `silver_builder.py` are other cells' files: never create or edit them.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `TCKT_MTADTA-D1-W5-S<k>`, in
  the investigation file below), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_TCKT_MTADTA~5 <0.9.0_WK_TCKT_MTADTA~5@opal.agent>"`, `-F` a message file you write with
  the Write tool, and `-- <paths>`.

<paths>
infra/aws/lambda/globgrph-trino-access/handler.py
infra/aws/lambda/globgrph-trino-access/tests/test_handler.py
infra/aws/terraform/trino/access.tf
org/missions/D7/TCKT/TCKT_MTADTA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP_R2.md</decomp_doc> (round 2), cell `MD-x-1`.
<owned_cells>MD-x-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: MD2-x1-AC1, MD2-x1-AC2, MD2-x1-AC3. Instance at `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.9.0_WK_TCKT_MTADTA~5/TCKT_MTADTA.TO-MD-x1.door-repair.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> MD2-x1-AC1,MD2-x1-AC2,MD2-x1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three check lines, the `pytest` summary line of your own tests, the diff nature of `access.tf` (the lines added and removed, by resource), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: RUN at the apply (MD-r-1, `iam simulate-principal-policy` on the collector role); blind to the live plane until then.
comp-adversary: DECLARED-NOT-APPLICABLE -- findings inlined: the CVO's remediation rows D1-S5 and D1-S4 (REMEDIATION_v1) and the CTO's rulings.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.4 C-ACCESS and C-RESIDUAL; CTO rulings msgs 6585, 6590, 6591; decomposition round 2 cell MD-x-1, rulings 2-4 and the DOOR CONTRACT v2.
