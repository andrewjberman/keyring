# TO SOC2_MSLOGS.TO-SM-s1 -- silver over the raw records, and the timeline reader

<to_id>SOC2_MSLOGS.TO-SM-s1</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.9.0_WK_SOC2_MSLOGS~3</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Risk note:** WORLD only by the gate's path floor (an infrastructure path is in `<paths>`); the cell calls nothing live.

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-s-1` (`decompositions/SOC2_MSLOGS_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SM-s-1`. Silver is "just formatted bronze in parquet for query" (Andrew-direct 2026-10-16, VERBATIM: "Silver is just formatted bronze in parquet for query, gold is effectively pattern baselines").
Bronze is now the raw Microsoft 365 Management Activity API records of every account (a JSON list of record dicts per object). This cell rebuilds the silver builder over those records and writes the
reader script that prints one account's timeline. READ first: `infra/aws/lambda/globgrph-trino-access/silver_builder.py` and `tests/test_silver_builder.py` (the current builder), `data/m365_metadata/scripts/silver/read_day.py`
(the old reader: you replace it), the PRD `org/missions/D12/SOC2/SOC2_MSLOGS/prd/SOC2_MSLOGS_PRD.md` rows C-RAW and C-READS. The door (another cell, SM-a-1) calls `silver_builder.build(records, only_date=date)`.
Nothing here touches the live account: no AWS call, no network. Tests use synthetic records only.

### SILVER CONTRACT v3 (build to it exactly)

`silver_builder.py`:
- `COLUMNS = ["record_id","creation_time","date","feed","record_type","operation","result_status","user_id","user_type","client_ip","object_id","site_url","item_name","mailbox_owner","organization_id","raw_json"]`
- `partition_date(iso) -> "YYYY-MM-DD"`: the America/New_York calendar date of an ISO timestamp (trailing `Z`, an offset, or naive meaning UTC). Keep as is.
- `build(records, only_date=None) -> bytes` (parquet via pyarrow, as today). `records` are raw record dicts. Rows sorted ascending by the record's `CreationTime`. If `only_date` is given, keep only records whose
  Eastern date equals it. Column mapping (all columns string typed except `date`, a date32; an absent source field is null):
  `record_id` = `Id`; `creation_time` = `CreationTime` as ISO UTC with trailing Z (`%Y-%m-%dT%H:%M:%SZ`; a naive value is UTC); `date` = Eastern date of CreationTime; `feed` = `Workload`;
  `record_type` = `RecordType` as a string; `operation` = `Operation`; `result_status` = `ResultStatus`; `user_id` = `UserId` lower-cased; `user_type` = `UserType` as a string;
  `client_ip` = `ClientIP`, else `ActorIpAddress`; `object_id` = `ObjectId`; `site_url` = `SiteUrl`; `item_name` = `SourceFileName`, else the `Subject` of the dict under `Item`;
  `mailbox_owner` = `MailboxOwnerUPN` lower-cased; `organization_id` = `OrganizationId`; `raw_json` = `json.dumps(record, ensure_ascii=False)` of the WHOLE original record (so nothing Microsoft shipped is lost to query).
- An empty list still builds a valid empty table with the same columns.
- Delete the old columns and their helpers (event_id, actor, workload, subject_hash, participants, site, file_id, file_name, extension, folder, client_ip_class). Rewrite `tests/test_silver_builder.py` for the above.

`data/m365_metadata/scripts/silver/read_timeline.py` (new):
- `fetch(invoker, account, start, end) -> dict`: `account` must be a string matching `^[^@\s]+@[^@\s]+$` (else `ValueError`, no call); lower-case and strip it; call `invoker({"op":"timeline","account":..., "start":..., "end":...})`
  exactly once; if the reply's `ok` is not true raise `RuntimeError("door refused timeline: ...")`; return the reply.
- `render(reply) -> str`: one line per row, ascending by `time`, `YYYY-MM-DD HH:MM:SS` in America/New_York, then feed, operation, result_status, client_ip, item_name (blank for null), two spaces between, trailing space trimmed. If the
  reply has `truncated` true, add a final line `TRUNCATED at 5000 rows: narrow the window`. No rows: the single line `no activity collected for this window`.
- A real invoker (boto3 lambda client, `FunctionName="globgrph-trino-access-lambda"`, `Qualifier="member"`, JSON payload, parsed JSON reply) built only inside `main`, with argparse flags `--account --start --end`; tests do not call it.
- A new `scripts/tests/test_read_timeline.py` for it.
- DELETE `silver/read_day.py`, `silver/first_content.py`, `tests/test_read_day.py`, `tests/test_first_content.py` (the eight-account reads of the closed project).
- No file you own mentions `TCKT` or `TCKT_MTADTA`.

Hard limits: ASCII only in code and comments; stdlib plus `pyarrow` (already used) plus `boto3` imported lazily in `main` only; never print an account or a record to a log.

### ACCEPTANCE

<criterion id="SM1-s1-AC1" cell_refs="SM-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_s1.py silver</invocation><expect>S1-SILVER-OK</expect></criterion>
`SM1-s1-AC1` -- raw records become a sorted parquet partition with the stable column set, Eastern dates, lower-cased accounts, the ip and item fallbacks and the whole record in `raw_json`; `only_date` keeps one Eastern day; an empty input builds an empty table; the Ticket Center era files are gone.

<criterion id="SM1-s1-AC2" cell_refs="SM-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_s1.py timeline</invocation><expect>S1-TIMELINE-OK</expect></criterion>
`SM1-s1-AC2` -- one account's window through an injected invoker prints in time order in Eastern, never blank (an empty window says so), says when truncated, refuses a bad account before any call, and the real invoker names the member alias.

<expected_criteria>SM1-s1-AC1,SM1-s1-AC2</expected_criteria>

Dry-run at the base 2026-10-16 ~17:0xZ: AC1 `S1-SILVER-REFUSED KeyError: 'creation_time'`, AC2 `S1-TIMELINE-REFUSED missing ...read_timeline.py` -- each FAIL as expected. Both were driven GREEN against a throwaway reference outside the
repository. Run each from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit. The four deletions named above are inside the grant.
- **LOCAL; NOTHING is called live.** No AWS call, no network, no Terraform. Never read a stored object.
- `handler.py` of the door, `access.tf` and the collector are other cells' files: never create or edit them.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `SOC2_MSLOGS-D1-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing, in the investigation file below), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_SOC2_MSLOGS~3 <0.9.0_WK_SOC2_MSLOGS~3@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
infra/aws/lambda/globgrph-trino-access/silver_builder.py
infra/aws/lambda/globgrph-trino-access/tests/test_silver_builder.py
data/m365_metadata/scripts/silver/read_timeline.py
data/m365_metadata/scripts/silver/read_day.py
data/m365_metadata/scripts/silver/first_content.py
data/m365_metadata/scripts/tests/test_read_timeline.py
data/m365_metadata/scripts/tests/test_read_day.py
data/m365_metadata/scripts/tests/test_first_content.py
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP.md</decomp_doc> (round 1), cell `SM-s-1`.
<owned_cells>SM-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SM1-s1-AC1, SM1-s1-AC2. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.9.0_WK_SOC2_MSLOGS~3/SOC2_MSLOGS.TO-SM-s1.silver-timeline.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SM1-s1-AC1,SM1-s1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two check lines, the `pytest` summary line of your own tests (`python -m pytest infra/aws/lambda/globgrph-trino-access/tests/test_silver_builder.py data/m365_metadata/scripts/tests/test_read_timeline.py -q`), the files deleted, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- the raw_json losslessness is AC1.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.2 C-RAW, C-READS; decomposition round 1 cell SM-s-1, ruling 7 and the SILVER CONTRACT v3.
