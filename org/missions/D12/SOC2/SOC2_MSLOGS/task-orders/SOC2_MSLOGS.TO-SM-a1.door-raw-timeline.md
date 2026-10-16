# TO SOC2_MSLOGS.TO-SM-a1 -- the door: write-once raw bronze, audit_events frozen, timeline, recollect, and the right to invoke the collector

<to_id>SOC2_MSLOGS.TO-SM-a1</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.9.0_WK_SOC2_MSLOGS~2</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-a-1` (`decompositions/SOC2_MSLOGS_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-6, FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SM-a-1`, the DOOR changed for the raw store. The access Lambda `globgrph-trino-access-lambda` (`infra/aws/lambda/globgrph-trino-access/handler.py`, Terraform
`infra/aws/terraform/trino/access.tf`) is the only way into the bucket `opal-data-trino`. Today it serves eight named accounts' day reads over a reduced table. The project is now about
exposure after an account is hacked (Andrew-direct 2026-10-16, VERBATIM: "It should have a globgrph iam group that can read/write/do ops in there, and if we want to know things about it,
we drive/query that lambda."), and bronze becomes the raw records of EVERY account. READ first: the handler (its docstring is the v2 contract), `tests/test_handler.py`, `access.tf`, and the
PRD `org/missions/D12/SOC2/SOC2_MSLOGS/prd/SOC2_MSLOGS_PRD.md` rows C-ACCESS, C-SWITCH, C-READS. Nothing here touches the live account.

### THE DOOR CONTRACT v3 (fixed by the decomposition; build to it exactly)

`handle(event, context=None, s3=None, log=print, silver_reader=None, silver_builder=None, lambda_client=None, now=None) -> dict`, `key_ok(dataset, key) -> bool`, `PREFIX`. The alias gate is
unchanged: the alias is the last field of `context.invoked_function_arn` when it has 8 fields; an unqualified ARN, an unknown alias or `context is None` serves NO op.

| op | `collector` alias | `member` alias |
|---|---|---|
| `put {dataset, key, body_b64}` | datasets `bronze`, `state`, `gold` when `key_ok` | refused |
| `derive_silver {date}` | served; answers exactly `{"ok": true, "rows": n}` | served (same answer) |
| `get_state {key}` | the cursor key alone | a key under `state/` or `gold/collection_coverage/` |
| `list_state {prefix}` | refused | a prefix under `state/` or `gold/collection_coverage/` |
| `timeline {account, start, end}` | refused | served (below) |
| `recollect {start, end}` | refused | served (below) |
| `get_day`, any other op, a get of bronze | refused | refused |

**Bronze grammar.** `key_ok("bronze", key)` is a FULL MATCH of `m365-metadata/trino/bronze/audit_records/date=\d{8}/<id>\.json\.gz` where `<id>` matches
`[0-9]{10,30}\$[0-9]{10,30}\$audit_[a-z]+\$Audit_[A-Za-z]+\$[A-Za-z0-9]+` (a Management API contentId; ASCII only). The old `bronze/audit_events/...` grammar is DELETED from
`key_ok` (that table is FROZEN: no put to it, ever; reads and listing of it are not affected because no op reads bronze). Silver, state and gold grammars are unchanged. `..` is never admitted.
A person, an address or a file name can never sit in a key.

**Write-once.** For dataset `bronze`, `put` first `s3.head_object(Bucket, Key)`; if the object exists the answer is `{"ok": false, "already_stored": true, "error": "exists"}`, nothing is written,
the outcome is logged `refused`. Only a missing object (head raises) is written. State and gold puts overwrite as today.

**Derive.** `derive_silver(date)` (YYYY-MM-DD, Eastern) lists the bronze partitions `audit_records/date=<D>` AND `date=<D+1>` (yyyymmdd), reads each object, `gzip.decompress` then
`json.loads` (the body is a JSON list of raw records), concatenates the records, calls `silver_builder.build(records, only_date=date)` and writes
`silver/activity_events/date=<date>/data.parquet` (SSE KMS as today). Answer exactly `{"ok": true, "rows": n}` with n the records handed to the builder. (Another cell, SM-s-1, makes `build` keep
only records whose Eastern date is `date`; you pass `only_date`.)

**timeline.** Request `{account, start, end}`: `account` a string containing `@`; `start`, `end` ISO-8601 strings; `end` after `start`; the window at most 31 days; otherwise
`{"ok": false, "error": "window"|"account"}` and no S3 call. The door asks `silver_reader.timeline_rows(s3, bucket, SILVER_PREFIX, account, start, end)` for row dicts, sorts them by `time`
ascending, returns the first 5000 as `{"ok": true, "rows": [...], "truncated": len(rows) > 5000}`. Row keys: `time` (the record's creation_time, ISO UTC with Z), `feed`, `operation`,
`result_status`, `client_ip`, `item_name`, `user_id`, `record_id`. The default reader (class in the handler module, used when `silver_reader` is None) reads, with `pyarrow.parquet` over
`io.BytesIO(body)` (the Lambda's pandas layer carries pyarrow; import lazily), every silver partition `date=<d>` for each Eastern date d the window touches, the columns record_id,
creation_time, feed, operation, result_status, client_ip, item_name, user_id, keeps rows whose `user_id` equals `account.lower()` and whose creation_time is in `[start, end)`, and maps
`creation_time` to `time`. A missing partition is an empty list, never an error.

**recollect.** Request `{start, end}` and NOTHING else (any other key, such as `body_b64` or `records`, is refused: a member never supplies bytes). Valid when both are ISO strings, `end` is after
`start`, `start` is not older than 7 days before `now` (ISO string, the injected clock; `lambda_handler` passes the current UTC time). On valid input call
`lambda_client.invoke(FunctionName=os.environ["COLLECTOR_FUNCTION"], InvocationType="Event", Payload=json.dumps({"recollect": {"start": start, "end": end}}).encode())` once and answer
`{"ok": true}`; on invalid input answer `{"ok": false, "error": "window"|"fields"}` and invoke nothing. `lambda_handler` builds `boto3.client("lambda")` and passes it.

**Logging.** Every call writes ONE line `op=<op> outcome=<ok|refused|absent|error>`: never a body, a key, an account, a file name or an alias. `KNOWN_OPS` = put, get_state, list_state, timeline,
recollect, derive_silver. Remove `UPNS`, `MEMBERS`, `_get_day`, `_DaySilverReader.read_day_rows` and every mention of the eight accounts.

### access.tf

- The door's execution-role policy (`aws_iam_role_policy.access`) gains ONE statement: `lambda:InvokeFunction` on `aws_lambda_function.collector.arn` ALONE (Sid `InvokeTheCollectorForRecollect`).
  `aws_lambda_function.collector` is declared in `collector.tf`, another cell's file in the same root: reference it, never declare it.
- `aws_lambda_function.access` `environment.variables` gains `COLLECTOR_FUNCTION = aws_lambda_function.collector.function_name`.
- Nothing else changes: the group policy stays on the member alias alone with its MFA condition; the bucket Deny's `data_actions` and their absence of `s3:ListBucket` stay; no wildcard
  principal; no alarm or notification resource. Replace `TCKT_MTADTA` in this file's comments with `SOC2_MSLOGS`, and drop narrative that names the old project's cells.

### Tests

Rewrite `tests/test_handler.py` for the contract: every cell of the table (served and refused) on both aliases and on the three fail-closed contexts; the bronze grammar (accepted: a key made
by `lib/opal_naming.address("m365-metadata","trino","bronze","audit_records","date=20261015", object="<contentId>.json.gz")`; refused: a file name, an address, a `person=` segment, a foreign
prefix, `..`, the old `audit_events` key); write-once; derive over two partitions; `timeline` limits and truncation; `recollect` rules including a member-supplied body. Replace `TCKT_MTADTA` in files you own.

### ACCEPTANCE

<criterion id="SM1-a1-AC1" cell_refs="SM-a-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_a1.py ops</invocation><expect>A1-OPS-OK</expect></criterion>
`SM1-a1-AC1` -- the member alias serves `timeline` (any account, in time order, capped at 5000 with truncated) and `recollect` (the door invokes the collector asynchronously and never takes bytes); `get_day` is gone on every alias; the collector alias is served neither; bad windows are refused; the rest of the alias matrix and the log discipline hold.

<criterion id="SM1-a1-AC2" cell_refs="SM-a-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_a1.py bronze</invocation><expect>A1-BRONZE-OK</expect></criterion>
`SM1-a1-AC2` -- a second write to an existing bronze key is refused as already stored and changes no byte; the frozen `audit_events` table accepts no write; derive reads two day partitions and passes `only_date`; the key grammar admits the builder's `audit_records` key and refuses a name, an address and a bad partition.

<criterion id="SM1-a1-AC3" cell_refs="SM-a-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_a1.py tf</invocation><expect>A1-TF-OK</expect></criterion>
`SM1-a1-AC3` -- `access.tf` lets the door role invoke the collector function alone, sets `COLLECTOR_FUNCTION`, keeps the bucket Deny without `ListBucket` and the group policy on the member alias alone, and names no Ticket Center project.

<expected_criteria>SM1-a1-AC1,SM1-a1-AC2,SM1-a1-AC3</expected_criteria>

Dry-run at the base 2026-10-16 ~17:0xZ: AC1 `A1-OPS-REFUSED TypeError: handle() got an unexpected keyword argument 'lambda_client'`, AC2 `A1-BRONZE-REFUSED TypeError: handle() got an unexpected keyword argument 'now'`, AC3
`A1-TF-REFUSED the door role policy must allow lambda:InvokeFunction on aws_lambda_function.collector.arn alone; ...` -- each FAIL as expected. All three were driven GREEN against a throwaway reference outside the repository.
Run each from the repository (worktree) root (the checks import `lib/opal_naming.py` from it).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **WORLD by the gate's path floor; NOTHING is applied or called live.** No `terraform apply`/`init` against the backend, no AWS call, no S3 access, no Lambda invoke. `terraform fmt -check` on your file is welcome (no network).
- `collector.tf`, `silver_builder.py`, the collector package and the registry are other cells' files: never create or edit them.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `SOC2_MSLOGS-D1-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing, in the investigation file below), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_SOC2_MSLOGS~2 <0.9.0_WK_SOC2_MSLOGS~2@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
infra/aws/lambda/globgrph-trino-access/handler.py
infra/aws/lambda/globgrph-trino-access/tests/test_handler.py
infra/aws/terraform/trino/access.tf
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP.md</decomp_doc> (round 1), cell `SM-a-1`.
<owned_cells>SM-a-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SM1-a1-AC1, SM1-a1-AC2, SM1-a1-AC3. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.9.0_WK_SOC2_MSLOGS~2/SOC2_MSLOGS.TO-SM-a1.door-raw-timeline.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SM1-a1-AC1,SM1-a1-AC2,SM1-a1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three check lines, the `pytest` summary line of your own tests (`python -m pytest infra/aws/lambda/globgrph-trino-access/tests/test_handler.py -q`), the diff nature of `access.tf` (lines added and removed, by resource), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: RUN at the release (SM-r-1 `s1_check_r1.py applied` reads the door role policy and both alias Denies live); blind to the live plane until then.
comp-adversary: DECLARED-NOT-APPLICABLE -- the CVO's write-once negative arm is AC2; the member-supplies-no-bytes rule is AC1.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.2 C-ACCESS, C-SWITCH, C-READS; decomposition round 1 cell SM-a-1, rulings 3-7 and the DOOR CONTRACT v3.
