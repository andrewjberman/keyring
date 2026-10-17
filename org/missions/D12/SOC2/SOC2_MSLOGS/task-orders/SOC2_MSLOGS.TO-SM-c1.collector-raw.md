# TO SOC2_MSLOGS.TO-SM-c1 -- the collector switches to raw: every account, four feeds, bronze byte-for-byte into audit_records, a raw-era cursor, a recollect window

<to_id>SOC2_MSLOGS.TO-SM-c1</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.9.0_WK_SOC2_MSLOGS~7</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Risk note:** WORLD only by the gate's path floor (an infrastructure path is in `<paths>`); the cell calls nothing live.

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-c-1` (`decompositions/SOC2_MSLOGS_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SM-c-1`. The hourly collector (a Lambda, `infra/aws/lambda/m365-metadata-collector/handler.py`, over the package `data/m365_metadata/scripts/collector/`) pulls the
Microsoft 365 Management Activity API and today keeps only eight named accounts, reduced to a few fields. The project's purpose has changed (Andrew-direct 2026-10-16,
VERBATIM): "the premise is if any opal user is hacked, we want to be able to know the exposure; what was seen, what the duration period was, its really about disaster
recovery/remediation." So the collector must now store EVERY account's records, whole, exactly as Microsoft ships them. READ first: `collect.py`, `source_client.py`,
`access_client.py`, `coverage_record.py`, `filter.py`, `population.json` (at `data/m365_metadata/scripts/`), the handler, `build.sh`, `scripts/app/start_subscriptions.py`,
and the tests `scripts/tests/test_collector.py` and `test_app.py`. The PRD is `org/missions/D12/SOC2/SOC2_MSLOGS/prd/SOC2_MSLOGS_PRD.md` (C-POPULATION, C-RAW, C-COLLECT, C-SWITCH,
C-COVERAGE); the decomposition's rulings 2-6 and the COLLECTOR CONTRACT v3 are inlined here. Nothing in this cell touches the live account: no AWS call, no network, no Terraform.

### THE COLLECTOR CONTRACT v3 (build to it exactly; the checks drive it with synthetic values)

- **Feeds.** New module `raw_records.py`: `CONTENT_TYPES = ["Audit.Exchange", "Audit.SharePoint", "Audit.General", "Audit.AzureActiveDirectory"]` and `parse_blob(raw_bytes) -> list`
  (UTF-8 JSON list of record dicts; it is used only to COUNT records). The collector keeps NO filter, population, field lever, subject key or office-address list: delete `filter.py`
  and `scripts/population.json`; the handler and `collect.py` stop reading them; `build.sh` stops copying `population.json`. The words `population`, `subject_key`, `office_ips`,
  `SUBJECT_KEY`, `process_batch` and `TCKT` appear in no collector module and not in the handler.
- **Source.** `source_client` gains `fetch_raw(content_type, blob_id) -> bytes`: the HTTP body exactly as served (no decode and re-encode, no re-serialisation). Keep `list_content`
  (`[{"id","created"}]`). The old parsing `fetch` may go.
- **Bronze.** One object per blob. `collect.bronze_key(day, blob_id)` returns `m365-metadata/trino/bronze/audit_records/date=<yyyymmdd>/<blob_id>.json.gz` where `day` is the Eastern
  calendar date (America/New_York, via the helper already in `coverage_record.py`) of the blob's listed `created` time. The body is `gzip.compress(raw, mtime=0)`: gunzip returns the
  served bytes unchanged. Put it with `access.put("bronze", key, body)`.
- **Already stored is success.** `access_client.AccessClient.put` returns the door's reply dict when it says `ok` OR `already_stored`, and raises only on other refusals. The collector counts
  `already_stored` in `already_stored` (not `fetched`, not `failed`); an exception from one blob's fetch or put counts in `failed` and the run continues with the other blobs.
- **Cursor.** `{"era":"raw","last_end":<iso>,"seen":{content_type:{blob_id:created}},"derive_pending":[<yyyy-mm-dd>,...]}`. A cursor that is `None`, or whose `era` is missing or not `"raw"`
  (every cursor stored today), is a COLD START: list the whole 7 days ending at `now` and fetch every blob, ignoring the old `seen`. A raw cursor lists from `last_end` minus the existing
  overlap and skips ids already in `seen`. `seen` is trimmed by age to 7 days, as today. `last_end` advances only past blobs that landed (stored or already stored), as today. Keep today's
  time budget (`budget_seconds`), partial-save and parallel-fetch (`max_workers`) behaviour and the `complete` flag.
- **Coverage.** Per fire, per Eastern day and content type, as `coverage_record` builds it today, with these fields: `listed`, `fetched`, `already_stored`, `events` (records counted by
  `parse_blob` for blobs fetched this run), `gap` (true only when `listed` exceeds `fetched + already_stored`), `status`, and `era: "raw"`. The document also carries `recollect: true|false`.
  Written with `access.put("gold", fire_key, ...)` as today.
- **Derive.** After the puts, call `access.derive_silver(d)` once for each date in the union of `derive_pending` from the cursor and, for every Eastern day `D` that received a bronze object
  this run, `D` and `D-1`; ascending order, each date once. If `clock()-start >= budget_seconds + 45` stop deriving and save the undone dates in the cursor's `derive_pending`; a derive
  reply with `ok` false also stays pending. The cursor drains `derive_pending` over later fires.
- **Recollect.** `run_once(..., window=(start_iso, end_iso))` lists ONLY inside that window, fetches every listed blob regardless of `seen`, writes coverage documents with `recollect: true`,
  derives as above, and does NOT write the cursor (no `access.put("state", ...)`); it returns the cursor argument unchanged. The handler's `parse_recollect(event, now) -> (start, end)` reads
  `event["recollect"]`; it raises `ValueError` when start or end is not a string, end is not after start, start is older than 7 days before `now`, or the span exceeds 7 days. When the event
  has a `recollect` key the Lambda handler runs window mode with the parsed window; otherwise it runs a normal fire. Keep `MAX_WORKERS = 8` and the time-budget safety margin.
- **Feed start script.** `scripts/app/start_subscriptions.py` starts all four `CONTENT_TYPES` (the same four as `raw_records`); delete its `EXCLUDED_CONTENT_TYPES` and the assertion on it;
  its docstring and comments say nothing about the sign-in feed being excluded and name no Ticket Center project. Its dry-run (no `--apply`) still prints the plan and calls nothing.
- **Tests.** Rewrite `scripts/tests/test_collector.py` for this contract (bytes preserved, key grammar, Eastern day by `created`, cold start vs raw cursor, already-stored, recollect leaves
  the cursor alone, parse_recollect, derive pending) and update `test_app.py` for four content types. Delete what tests the removed filter. Replace `TCKT_MTADTA` in every file you own with
  `SOC2_MSLOGS`, or drop the line when it only narrates the old project.

Hard limits: ASCII only in code and comments; no new dependency (stdlib only; `gzip`, `json`, `datetime`, `zoneinfo`); no AWS or network call in tests; a log line names counts and codes only,
never a record, an account, a file name or a key.

### AMENDMENT 2 (2026-10-16 ~22:4xZ, issuer) -- THE DERIVE-TIME REPAIR; this order is RE-OPENED and re-seated to worker ~6

The first cut of this order (worker ~1, merged at b2fef4b9b5) is the base of your worktree. Everything above stays; this section is added to it, and where it differs from the first cut it governs.


The collector Lambda (`infra/aws/lambda/m365-metadata-collector/handler.py`, over `data/m365_metadata/scripts/collector/collect.py`) was released live on 2026-10-16 and its fire at 21:31Z hit the
900-second Lambda limit (`Status: timeout`). The cause is measured: during the 7-day cold-start backlog, the fetch phase uses the whole budget (840 s, which the handler computes as the remaining time minus 60 s), derive_silver
gets only the 45-second grace after it, and a single derive call took 30 to 70 s, so the last call started at about 884 s and the Lambda was killed mid-derive. Two more faults showed: derive went OLDEST day first, so the
newest days (the ones an investigation reads) stayed on the old silver, and the cursor was written AFTER derive, so a kill in derive lost the whole fire's progress record. READ `collect.py` (the run_once
function, its fetch loop near "Fetch and store until the budget is spent", the derive block near "derive_silver: the days that received a blob", and the cursor block at the end), `tests/test_collector.py`, and the check
`org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_c1.py` (modes `derive_time` and `switch`, amended by the issuer to drive exactly these faults). Nothing here touches the live account.

### THE REPAIR (build to it exactly)

1. **Reserved derive share.** In the fetch loop, stop fetching when `elapsed >= budget_seconds - reserve` where `reserve = min(DERIVE_RESERVE_SECONDS, budget_seconds / 3)` and a new constant `DERIVE_RESERVE_SECONDS = 200`. A fetch stopped
   this way sets `complete = False` as today. `budget_seconds=None` still means unbounded (no reserve).
2. **Derive start guard.** The FIRST derive call of a fire always starts (progress is guaranteed; the reserve makes it safe). Every later derive call starts only if
   `elapsed + 1.5 * est <= budget_seconds + DERIVE_GRACE_SECONDS` where `est` is the longest single derive call so far in this run (seconds, measured with the injected `clock` around each call). The days not started stay in `derive_pending`.
3. **Newest day first.** The owed days (the cursor's `derive_pending`, the days that received a blob this fire, and the day before each) are derived in DESCENDING date order, each date once.
4. **Cursor before derive.** After coverage is written and BEFORE the first derive call, write the cursor exactly as today but with `derive_pending` = every owed day (as `yyyy-mm-dd` strings). After the derive loop, write the cursor again with `derive_pending` = the days not derived (a failed derive stays pending). A recollect run still writes NO cursor.
   The cursor's `seen`, `last_end` and `era` semantics do not change.
5. Keep everything else of TO-SM-c1's contract (raw bytes, key grammar, already-stored, cold start, coverage fields, parse_recollect). Update the module docstring for the new order and the reserve. `handler.py` needs no change.
6. Tests: extend `tests/test_collector.py` for the four rules (a slow-derive clock never passes the grace end; derive keeps a share with a backlog; descending order; the cursor is put before the first derive and again after; a small budget still fetches). ASCII only; stdlib only.

### AMENDMENT 3 (2026-10-17 ~00:5xZ, issuer) -- DERIVE MUST BE CONCURRENT AND ITS CLIENT MUST NOT RETRY; this order is RE-OPENED again and re-seated to worker ~7

Amendment 2 is merged (6cef75fd39) and its rules stand. The live fire of 00:31:22Z STILL hit the 900 s limit. The door log shows why: five `derive_silver` invocations 60 s apart (start 00:42:05, 00:43:06, 00:44:07, 00:45:10, 00:46:15), each `outcome=ok`
on the door (102 s, 77 s, 65 s, 63 s, 59 s), all for one fire. The collector built its door client with the DEFAULT boto3 `lambda` client, whose read timeout is 60 s and which makes 5 attempts: one derive of 60 to 100 s was re-invoked four times and the collector waited 300 s
for ONE day, ending past 900 s. The door itself is healthy since its memory was raised to 6144 MB (840 invocations, 0 errors). Two repairs, both in your paths:
1. **A derive client that does not retry.** In `handler.py`, build a second `boto3.client("lambda", config=botocore.config.Config(read_timeout=200, connect_timeout=10, retries={"max_attempts": 1, "mode": "standard"}))` for `derive_silver` calls only; the existing client keeps the defaults for put/get_state (short calls, retries welcome).
   `AccessClient.__init__(self, invoke, derive_invoke=None)`: `derive_silver` uses `derive_invoke` when given, else `invoke`. The handler wires `derive_invoke=lambda_invoker(derive_client, <door>, "collector")`. A `ReadTimeout` or any exception from a derive call leaves that day pending (it is never retried inside the fire).
2. **Derive the owed days concurrently.** In `collect.py`, derive newest day first in BATCHES of up to `max_workers` days, the days of a batch running at the same time in a thread pool (the handler passes `max_workers=8`; with `max_workers=1` the order and behaviour are exactly Amendment 2's). A batch's duration is its longest call. The first batch of a fire always starts;
   a later batch starts only when `elapsed + 1.5 * longest_batch_so_far <= budget_seconds + DERIVE_GRACE_SECONDS`. Cursor-before-derive and cursor-after-derive stay as Amendment 2 says. No date is derived twice in a fire.
Tests: extend `tests/test_collector.py` (concurrency with a barrier or an in-flight counter, a failing call leaves its day pending, `derive_invoke` selection, a stateless `AccessClient` under threads). ASCII only; stdlib plus the already-present boto3/botocore only inside the handler.

### ACCEPTANCE

<criterion id="SM1-c1-AC1" cell_refs="SM-c-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_c1.py raw</invocation><expect>C1-RAW-OK</expect></criterion>
`SM1-c1-AC1` -- four feeds, every account, one bronze object per blob whose gunzipped body equals the served bytes, keys in the `audit_records` grammar dated by the blob's Eastern created day, no filter or population or Ticket Center left, and the feed script starts all four.

<criterion id="SM1-c1-AC2" cell_refs="SM-c-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_c1.py switch</invocation><expect>C1-SWITCH-OK</expect></criterion>
`SM1-c1-AC2` -- an old-era cursor re-fetches the whole 7 days, the new cursor carries era raw, a second fire fetches nothing, already stored is neither a failure nor a gap, and an out-of-time derive carries `derive_pending` until it drains.

<criterion id="SM1-c1-AC3" cell_refs="SM-c-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_c1.py recollect</invocation><expect>C1-RECOLLECT-OK</expect></criterion>
`SM1-c1-AC3` -- a window run lists only its window, leaves the cursor alone, reads four stored blobs as already_stored=4 with no gap, marks coverage recollect, and the handler's window rules refuse bad windows.

<criterion id="SM1-c1-AC4" cell_refs="SM-c-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_c1.py derive_time</invocation><expect>C1-DERIVETIME-OK</expect></criterion>
`SM1-c1-AC4` -- (a fourth mechanical criterion, with this reason: the live release measured the fault after the cut, AMENDMENT 2) with 40 s and 120 s derive calls and a 1200-blob backlog the fire ends by 885 s; at least three derives run under the backlog; the days go newest first; the cursor is put before the first derive; the final cursor lists exactly the undone days; a 90 s budget still fetches. `SM1-c1-AC2` (switch) now also asserts newest-first derive order.

<criterion id="SM1-c1-AC5" cell_refs="SM-c-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_c1.py derive_par</invocation><expect>C1-DERIVEPAR-OK</expect></criterion>
`SM1-c1-AC5` -- (a fifth mechanical criterion, with this reason: AMENDMENT 3, measured live at 00:42-00:46Z) with `max_workers=4` and several owed days, derive runs more than one day at a time (never more than `max_workers`), the newest day starts first, no day twice, and an unbudgeted fire leaves nothing pending.

<criterion id="SM1-c1-AC6" cell_refs="SM-c-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_c1.py derive_client</invocation><expect>C1-DERIVECLIENT-OK</expect></criterion>
`SM1-c1-AC6` -- (a sixth mechanical criterion, same reason) the handler builds a botocore `Config` for the derive call with a read timeout between 200 and 290 s and `max_attempts` 1, so one slow derive is one door invocation.

<expected_criteria>SM1-c1-AC1,SM1-c1-AC2,SM1-c1-AC3,SM1-c1-AC4,SM1-c1-AC5,SM1-c1-AC6</expected_criteria>

Dry-run at the base 2026-10-16 ~17:0xZ: AC1 `C1-RAW-REFUSED missing ...raw_records.py`, AC2 `C1-SWITCH-REFUSED an old-era cursor must re-fetch the whole window: fetched 0 of 8; ...`, AC3
`C1-RECOLLECT-REFUSED TypeError: run_once() got an unexpected keyword argument 'window'` -- each FAIL as expected. All three were driven GREEN against a throwaway reference outside the repository.
Run each from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit. The deletions named above are inside the grant.
- **LOCAL; NOTHING is called live.** No AWS call, no Management API call, no network, no Terraform. Synthetic values only in tests. Never read a stored bronze object.
- `access.tf`, `collector.tf`, `silver_builder.py` and the door handler are other cells' files: never create or edit them.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `SOC2_MSLOGS-D1-W7-S<k>`, next free number, `surfaced_at` = `date -u +%FT%TZ` at
  filing, in the investigation file below), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_SOC2_MSLOGS~7 <0.9.0_WK_SOC2_MSLOGS~7@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
data/m365_metadata/scripts/collector/raw_records.py
data/m365_metadata/scripts/collector/collect.py
data/m365_metadata/scripts/collector/coverage_record.py
data/m365_metadata/scripts/collector/source_client.py
data/m365_metadata/scripts/collector/access_client.py
data/m365_metadata/scripts/collector/filter.py
data/m365_metadata/scripts/population.json
data/m365_metadata/scripts/app/start_subscriptions.py
data/m365_metadata/scripts/tests/test_collector.py
data/m365_metadata/scripts/tests/test_app.py
infra/aws/lambda/m365-metadata-collector/handler.py
infra/aws/lambda/m365-metadata-collector/build.sh
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP.md</decomp_doc> (round 1), cell `SM-c-1`.
<owned_cells>SM-c-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SM1-c1-AC1, SM1-c1-AC2, SM1-c1-AC3, SM1-c1-AC4, SM1-c1-AC5, SM1-c1-AC6. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.9.0_WK_SOC2_MSLOGS~7/SOC2_MSLOGS.TO-SM-c1.collector-raw.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SM1-c1-AC1,SM1-c1-AC2,SM1-c1-AC3,SM1-c1-AC4,SM1-c1-AC5,SM1-c1-AC6` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three check lines, the `pytest` summary line of your own tests (`python -m pytest data/m365_metadata/scripts/tests/test_collector.py data/m365_metadata/scripts/tests/test_app.py -q`),
the files deleted, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change in this cell (the hourly rule is unchanged; SM-r-1 reads it back).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- the CVO's already-stored arm is AC3; Andrew's raw-bytes word is AC1.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.2 C-POPULATION, C-RAW, C-COLLECT, C-SWITCH, C-COVERAGE; decomposition round 1 cell SM-c-1, rulings 2-6 and the COLLECTOR CONTRACT v3.
