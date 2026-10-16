# TO TCKT_MTADTA.TO-MD-c1 -- the collector: population filter and field levers before the first write, cursor, coverage, the hourly Lambda (desired)

<to_id>TCKT_MTADTA.TO-MD-c1</to_id>
<project>TCKT_MTADTA</project>
<issued_to>0.9.0_WK_TCKT_MTADTA~3</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D7 | **Fabric:** dell1 | **Decomp cell:** `MD-c-1` (`decompositions/TCKT_MTADTA_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-7, FWD-9 | **depends_on:** none (you build to the DOOR CONTRACT and BRONZE CONTRACT below)

---

## WORKER FACE

### THE CELL

`MD-c-1`, COLLECT. A SCHEDULED collector (cadence `hourly`; an ad-hoc run is QA only) lists the Office 365 Management Activity feed's
available content for three content types (`Audit.Exchange`, `Audit.SharePoint`, `Audit.General`; the Entra sign-in feed
`Audit.AzureActiveDirectory` is NOT subscribed), fetches each blob ONCE, reduces every event, and writes bronze, a cursor and a coverage
record **only through the access door** (a Lambda another cell builds). **The collector holds no S3 client and no S3 permission.**

**THE GUARD IS THE WHOLE POINT.** Andrew, VERBATIM: "all other domains/accounts should be dropped at the outset and not stored". The
filter runs in memory BEFORE THE FIRST WRITE; a field once stored cannot be un-stored; and bronze cannot be repaired afterwards (the source
keeps 7 days). Nothing but what is whitelisted below may reach a write.

### THE RULES (PRD C-POPULATION, C-FIELDS, C-COVERAGE, C-COLLECT -- build them exactly)

**Population.** The eight UPNs (each `@opalinvest.com`): `andrew`, `alyssa`, `bobby`, `manav`, `yang`, `menachem`, `jim`, `jeanette`. They live in ONE config
value, `data/m365_metadata/scripts/population.json`: `{"population": [<the eight>], "object_ids": {}, "office_ips": [], "subject_key_secret": "m365-metadata/trino/subject-key"}`
(`object_ids` stays empty in round 1: resolving Entra object ids needs a Graph permission the app does not hold; the decomposition rules
that out). An event is KEPT only when its actor resolves, case-insensitively, to one of the eight across the four fields `UserId`,
`MailboxOwnerUPN`, `SendAsUserSmtp`, `SendOnBehalfOfUserSmtp` (take the first field that resolves; `actor` is that member's lower-cased UPN).
An event whose actor does not resolve is DROPPED, COUNTED per workload, and never written.

**Field levers, applied at the same point (a whitelist: build the output dict from nothing; copy no source dict).**
- `event_id` = source `Id`; `creation_time` = source `CreationTime` (no zone, UTC) as ISO with a trailing `Z`; `operation`, `workload`,
  `record_type`, `result_status` from `Operation`, `Workload`, `RecordType`, `ResultStatus`.
- `subject_hash`: a mail `Subject`, if present, becomes `hmac_sha256(key, subject)` as 64 lower-case hex (the key is `config["subject_key"]`;
  production reads it from the secret store by the id `subject_key_secret`); no subject -> `null`. The raw subject is never stored.
- `participants`: scan the keys `Recipients`, `To`, `Cc`, `Bcc`, `TargetUserOrGroupName`, `UserSharedWith`, `ChatMembers`, `Guests` (a value is a string or a
  list of strings). Each address is replaced: one of the eight stays as its lower-cased UPN; any other `@opalinvest.com` address becomes the
  token `internal-other`; everything else becomes `external`. **No other address and no external domain is ever stored.**
- `client_ip_class`: source `ClientIP` in `config["office_ips"]` -> `"office"`; present and not -> `"remote"`; absent -> `"unknown"`. The raw
  IP is never stored.
- `site` = `SiteUrl`; `file_id` = `ListItemUniqueId` or `ObjectId`'s trailing segment; `file_name` = `SourceFileName`; `extension` =
  `FileExtension` or the file name's suffix; `folder` = `SourceRelativeUrl`. File ids, extensions, site and file names are kept (the later
  workflow evidence needs them).
- Every other source key (including `ExtendedProperties`, `UserAgent`, `ClientIP`, `Subject`, `Recipients` themselves) is DROPPED.

**Bronze (the BRONZE CONTRACT).** The kept events of a fire are split by the America/New_York calendar date of `creation_time`; one object
per (Eastern date, content type, fire): key `address('m365-metadata', 'trino', 'bronze', 'audit_events', 'date=YYYYMMDD', object=
'<ContentType>_<fireISO>.json.gz')` (use `lib/opal_naming.address`; the registry rows land in another cell, so in tests and until then
build the key with the same prefix and a comment naming the call); body = gzip of JSON lines of the whitelist dict, keys exactly:
`event_id, creation_time, workload, operation, record_type, result_status, actor, subject_hash, participants, site, file_id, file_name, extension, folder, client_ip_class`.

**Cursor.** The source lists content in windows of AT MOST 24 hours. Keep a cursor `{"last_end": ISO, "seen": {<content_type>: [<blob id>, ...]}}`
(trim `seen` to the last 7 days): list from `last_end` minus one hour (overlap) to now, in windows of at most 24 hours, clamped to the
last 7 days; skip a blob already in `seen`. A fire that finds the cursor older than 7 days writes the uncovered days' coverage as LOST.
The cursor is written through the door: `put("state", address('m365-metadata','trino','state','subscription_cursor','current', object='cursor.json'), <json bytes>)`.

**Coverage (PRD C-COVERAGE).** Every fire writes, per day and content type, a coverage record through the door:
`put("gold", <key under .../gold/collection_coverage/date=YYYY-MM-DD/ with object 'coverage.json'>, <json bytes>)` -- round 1 writes JSON, not parquet.
`coverage_record.build_record(day, content_type, listed, fetched, events, dropped, now, gap=None) -> dict` returns at least
`{"day", "content_type", "listed", "fetched", "events", "dropped", "gap", "status"}` where `status` is `"collected"`, `"no activity collected"` (a quiet
day: nothing found, nothing missing; never blank), `"GAP"` (listed more than fetched, or `gap=True`), or `"LOST"` (a gap more than 7 days
before `now`). `gap=None` means "decide from listed and fetched". `dropped` is the per-workload population drop counter.

### THE DOOR CONTRACT (the part you call; another cell builds the far side)

`access.put(dataset, key, body: bytes) -> dict` (dataset one of `bronze|silver|state|gold`) and `access.get_state(key) -> bytes|None`.
`access_client.py` implements them over an injected `invoke(payload: dict) -> dict` callable: `put` sends `{"op": "put", "dataset": ..., "key":
..., "body_b64": ...}`; `get_state` sends `{"op": "get_state", "key": ...}`. Production wires `invoke` to `boto3.client("lambda").invoke` of
the function named by `name('globgrph', None, 'trino-access', 'lambda')` (`globgrph-trino-access-lambda`); only `lambda` and
`secretsmanager` clients may appear in your code.

### BUILD (the Python is stdlib plus lazy `boto3`; 3.9+ syntax)

**Imports.** The `collector/` folder is a FLAT directory of modules (no `__init__.py`, no relative imports): `collect.py` does `from filter import ...`, and the check files and the Lambda zip load the folder as a flat path. The coverage module is named `coverage_record.py` so it can never shadow the `coverage` package.

1. `data/m365_metadata/scripts/collector/filter.py` -- `CONTENT_TYPES = ["Audit.Exchange", "Audit.SharePoint", "Audit.General"]`;
   `process_event(event, config) -> dict | None`; `process_batch(events, config) -> (kept: list[dict], counters: dict)` with
   `counters["dropped"]` = `{workload: n}`. `config` has `population`, `object_ids`, `subject_key`, `office_ips`.
2. `data/m365_metadata/scripts/collector/coverage_record.py` -- `build_record(...)` as above.
3. `data/m365_metadata/scripts/collector/collect.py` -- `run_once(source, access, config, now, cursor=None) -> dict` returning
   `{"fetched": int, "cursor": dict, "bronze_objects": int}`; `source` has `list_content(content_type, start, end) -> list[blob id]` and
   `fetch(content_type, blob) -> list[dict]` (raw events). A second fire with the returned cursor fetches nothing already seen.
4. `data/m365_metadata/scripts/collector/source_client.py` -- the real `source` over the Management API (`urllib`, a bearer token from an
   injected provider; `https://manage.office.com/api/v1.0/{tenant}/activity/feed/subscriptions/content?contentType=...&startTime=...&endTime=...`
   then the `contentUri` of each listing). Not exercised in round 1. `access_client.py` as above.
5. `data/m365_metadata/scripts/population.json` as above; `data/m365_metadata/scripts/tests/test_collector.py` (pytest, SYNTHETIC events only).
6. `infra/aws/lambda/m365-metadata-collector/handler.py` -- `lambda_handler(event, context)`: build the clients (inside the function), read
   the credential and the subject key by secret id (`m365-metadata/trino/api-credentials`; never log a value), read the cursor through the door,
   `run_once`, write nothing else. `build.sh` zips `handler.py` and the `collector/` package and `population.json` to
   `build/m365-metadata-collector.zip`; model it on `infra/aws/lambda/transcripts-pull/build.sh` (read it).
7. `infra/aws/terraform/trino/collector.tf` -- the function `m365-metadata-trino-collector-lambda` and the EventBridge rule
   `m365-metadata-trino-collector-hourly` (`rate(1 hour)`) with its target and invoke permission, names from the builder by the mechanism
   `infra/aws/terraform/transcripts/pull.tf` uses (read it); its role gets `lambda:InvokeFunction` on `globgrph-trino-access-lambda` and
   `secretsmanager:GetSecretValue` on the two secret ids and logs, and **NO S3 and NO KMS permission**. No SNS, alarm or notification.

### ACCEPTANCE

<criterion id="MD1-c1-AC1" cell_refs="MD-c-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_c1.py guard</invocation><expect>C1-GUARD-OK</expect></criterion>
`MD1-c1-AC1` -- eight planted cases: a member kept; an outsider dropped, counted and absent; a send-as member kept; an internal and an external recipient, a subject, an IP and an unlisted key never present in what is kept; the subject hash stable and key-dependent; the three content types.

<criterion id="MD1-c1-AC2" cell_refs="MD-c-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_c1.py coverage</invocation><expect>C1-COVERAGE-OK</expect></criterion>
`MD1-c1-AC2` -- a quiet day, a gap day and a day past 7 days read differently, the last as LOST.

<criterion id="MD1-c1-AC3" cell_refs="MD-c-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_c1.py collect</invocation><expect>C1-COLLECT-OK</expect></criterion>
`MD1-c1-AC3` -- one fire end to end against a fake source and a fake door: only members' events reach bronze, the cursor and the coverage record are written, a second fire fetches nothing, and the package holds no S3 client.

<expected_criteria>MD1-c1-AC1,MD1-c1-AC2,MD1-c1-AC3</expected_criteria>

Dry-run at the base 2026-10-16 ~06:5xZ: each `*-REFUSED missing ...collector\*.py` -- FAIL as expected. All three were driven GREEN against a
throwaway reference outside the repository (guard, coverage and collect each printed their OK token). Run from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **WORLD by the gate's path floor; NOTHING is run live.** No Microsoft or Management API call, no AWS call, no S3 access, no
  `terraform apply`/`init`. SYNTHETIC events only; **no real event, address, subject, IP or file name enters the repository**, in tests,
  fixtures, deliverables or your report.
- You write ONLY `collector.tf` of the Terraform root. The bucket, key and policies are other cells'.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `TCKT_MTADTA-D1-W3-S<k>`), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_TCKT_MTADTA~3 <0.9.0_WK_TCKT_MTADTA~3@opal.agent>"`, `-F` a message
  file you write with the Write tool, and `-- <paths>`.

<paths>
data/m365_metadata/scripts/collector/filter.py
data/m365_metadata/scripts/collector/coverage_record.py
data/m365_metadata/scripts/collector/collect.py
data/m365_metadata/scripts/collector/source_client.py
data/m365_metadata/scripts/collector/access_client.py
data/m365_metadata/scripts/population.json
data/m365_metadata/scripts/tests/test_collector.py
infra/aws/lambda/m365-metadata-collector/handler.py
infra/aws/lambda/m365-metadata-collector/build.sh
infra/aws/terraform/trino/collector.tf
org/missions/D7/TCKT/TCKT_MTADTA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP.md</decomp_doc> (round 1), cell `MD-c-1`.
<owned_cells>MD-c-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: MD1-c1-AC1, MD1-c1-AC2, MD1-c1-AC3. Instance at `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.9.0_WK_TCKT_MTADTA~3/TCKT_MTADTA.TO-MD-c1.collector.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> MD1-c1-AC1,MD1-c1-AC2,MD1-c1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three check lines, the `pytest` summary line, the list of source keys your whitelist reads (names only), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the hourly rule is DESIRED in collector.tf; applied at release act 1.
comp-iam: RUN at the drain over the merged root; the collector role is deliberately given no S3 and no KMS action.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round. Inlined: a population or field error cannot be repaired from bronze (PRD DECISION 1), so AC1 plants eight cases.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.2 C-POPULATION, C-FIELDS, C-COLLECT, C-COVERAGE, C-ACCESS (the collector writes through the door), DECISIONS 1, 5, 6, 7; decomposition cell MD-c-1, rulings 4 and 6.
