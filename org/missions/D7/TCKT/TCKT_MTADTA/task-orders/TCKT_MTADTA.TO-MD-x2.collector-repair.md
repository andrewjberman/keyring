# TO TCKT_MTADTA.TO-MD-x2 -- the collector's repair: coverage per fire, counts by each blob's own day, a cursor trimmed by age, the id-only counter, derive_silver, the collector alias, builder-equal keys

<to_id>TCKT_MTADTA.TO-MD-x2</to_id>
<project>TCKT_MTADTA</project>
<issued_to>0.9.0_WK_TCKT_MTADTA~6</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D7 | **Fabric:** dell1 | **Decomp cell:** `MD-x-2` (`decompositions/TCKT_MTADTA_DECOMP_R2.md`) |
**outcome_ref:** FWD-1, FWD-7, FWD-9 | **depends_on:** none (you build to the COLLECTOR CONTRACT v2 and the DOOR CONTRACT v2)

---

## WORKER FACE

### THE CELL

`MD-x-2`, the COLLECTOR repaired. Round 1 built the hourly collector (`data/m365_metadata/scripts/collector/`, `infra/aws/lambda/m365-metadata-collector/`,
`infra/aws/terraform/trino/collector.tf`). READ them first; you edit them. The privacy guard in `filter.py` (the eight, the whitelist, the class tokens, the
subject hash, the IP flag) is correct and STAYS; change only what is named below. Why each change (the CVO's remediation rows and the CTO's rulings):

- **D1-W3-S3.** One coverage object per DAY was overwritten by every hourly fire, so an earlier fire's GAP was erased. Write ONE coverage object PER FIRE.
- **D1-W3-S5 / D1-W3-S4.** Fire counts were attributed to the window's end day, and the cursor could not be trimmed by age, because the listing returned bare
  ids. The Management API's listing carries each blob's `contentId` and `contentCreated`: make the source return both, attribute each blob's counts to the
  Eastern day of its own `created`, and trim the cursor by `created`.
- **D1-S2.** The actor is resolved by UPN only. Count the events dropped because their only actor field is a GUID (an id-only actor) separately, so the first
  real content shows how many there are.
- **D1-W3-S2.** Keys equal `lib/opal_naming` output (a test proves it).
- **D1-S5 (PRD v0.4).** The collector calls the door through ITS OWN alias, `collector`, and the door serves that alias three operations only: `put`, `derive_silver`,
  and `get_state` on the cursor key. After it writes bronze for an Eastern day the collector calls `derive_silver` for that day, so silver exists for Andrew's read.
- **The seam found at the round-1 drain.** `collector.tf` read the door and the two secret containers as data sources, which fail at plan until they exist.
  The patch `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/2.0.0_SA_COO~S1/collector_tf_direct_references.patch` is that fix (direct references to the
  root's own resources); apply its intent to the CURRENT file, then change the invoke grant to the alias (below).

### AMENDMENT 2026-10-16 ~13:5xZ -- THE FIRST LIVE FIRE TIMED OUT (issuer, reopening this order; read this section first)

Measured live: the 13:31Z scheduled fire hit the Lambda's 300-second limit and was retried twice, each from zero. Cause: a fire with no cursor lists the whole 7-day window (the tenant's feed holds hundreds of blobs for those
days: single-window listings returned 9 to 87 blobs each, in 0.2 to 1.8 seconds) and then fetches every blob ONE AT A TIME before it writes anything. The work does not fit the limit, and nothing is saved before the limit hits, so every
retry restarts from nothing. Add a TIME BUDGET and save as you go. The contract of `run_once` gains, in addition to everything above:
- `run_once(source, access, config, now, cursor=None, clock=None, budget_seconds=None, max_workers=1) -> dict`. `clock` is a callable returning seconds (default `time.monotonic`); `budget_seconds=None` means unbounded (every
  existing test keeps passing).
- Before attempting each new blob's fetch, if `clock() - start >= budget_seconds`, STOP: no further blob is attempted this fire. What was fetched is processed as usual (bronze, `derive_silver` per Eastern day, coverage, cursor).
- The result gains `"complete": bool` (False when the fire stopped at its budget with blobs left to fetch).
- Cursor after a stopped fire: `seen` = the earlier entries (trimmed) plus the blobs ATTEMPTED this fire that did not fail; blobs not attempted are NOT in `seen`; `last_end` is NOT advanced (keep the cursor's previous `last_end`; on a cold
  start use the window start), so the next fire re-lists the same window and fetches only what is left. After a complete fire `last_end` is `now`, as before.
- The coverage document gains a top-level `"complete": bool` (`{"day", "fire", "complete", "records"}`). A blob skipped by the budget is counted in neither `listed` nor `fetched` this fire; it is counted when a later fire attempts it.
- `max_workers > 1` fetches concurrently (`concurrent.futures.ThreadPoolExecutor`), then processes the results in listing order (so the output is deterministic); the budget is checked before each batch of `max_workers` fetches. `max_workers=1` is the sequential
  path the checks drive.
- `infra/aws/lambda/m365-metadata-collector/handler.py`: pass `max_workers=8` and `budget_seconds = context.get_remaining_time_in_millis() / 1000 - 60` (200 when `context` is None); after `run_once`, `print` ONE line with counts only
  (`fire fetched=<n> bronze_objects=<n> failed=<n> complete=<True|False>`): the function wrote nothing to its log, which is why the hang was invisible. Never print an event, key, id or value.
- `infra/aws/terraform/trino/collector.tf`: `timeout = 900` (was 300). No other change in that file.
- New check, a fourth mechanical criterion with this reason: the first live fire failed in a way criteria 1-3 could not see. `r2_check_x2.py budget` drives a fake clock (1 second per fetch) over 60 blobs across three Eastern days with a 25-second budget: fire 1 must stop with
  `complete=False` after at most 26 fetches; the backlog finishes in a few fires; every blob is fetched exactly once across them; coverage documents carry `complete`.

### THE CONTRACTS (fixed; build to them exactly)

**COLLECTOR CONTRACT v2.**
- `source.list_content(content_type, start, end) -> [{"id": str, "created": ISO-8601 UTC string}]` (the real `source_client.py` maps `contentId` and `contentCreated`);
  `source.fetch(content_type, id) -> [raw events]`.
- Cursor: `{"last_end": ISO, "seen": {content_type: {id: created_iso}}}`. After a fire, `seen[ct]` holds the ids of that fire's listing that did not fail, each with its
  `created`, plus earlier entries, all trimmed to `created >= now - 7 days`. A failed fetch is never recorded as seen. A cursor from round 1 (a LIST of ids per
  content type) is read as "nothing seen".
- `coverage_record.fire_key(day, fire_iso) -> "m365-metadata/trino/gold/collection_coverage/date=YYYY-MM-DD/coverage_YYYYMMDDTHHMMSSZ.json"` (day `YYYY-MM-DD`; the
  fire time compacted, UTC). `collect.bronze_key(day, content_type, fire_tag) -> "m365-metadata/trino/bronze/audit_events/date=YYYYMMDD/<ContentType>_<fire_tag>.json.gz"`;
  `collect.CURSOR_KEY = "m365-metadata/trino/state/subscription_cursor/current/cursor.json"`. All three equal `lib.opal_naming.address(...)` output with the bucket removed.
- Per fire, per Eastern day the window touches, ONE coverage object at `fire_key(day, fire)` holding `{"day", "fire", "records": [one record per content type]}`. A
  record's `listed` and `fetched` count the NEW blobs whose `created` falls on that Eastern day; `events` counts the kept events whose `creation_time` falls on it; `dropped` is
  the per-workload population drop count of those blobs; every record also carries `dropped_id_only` (an integer). Days older than 7 days that the cursor never covered
  are still written LOST, as before, at their own `fire_key`.
- `filter.process_batch(events, config) -> (kept, counters)` with `counters["dropped_id_only"]` = the number of dropped events whose `UserId` is a GUID
  (`8-4-4-4-12` hex) and in which none of the four actor fields resolves to one of the eight; such an event is ALSO counted in `counters["dropped"]`.
- `coverage_record.build_record(..., id_only=0)` carries `dropped_id_only`.
- `access.put(dataset, key, body)`, `access.get_state(key) -> bytes | None` (the cursor key only), `access.derive_silver(date) -> {"ok": true, "rows": n}`
  (`date` `YYYY-MM-DD`, Eastern; sends `{"op": "derive_silver", "date": date}`). `run_once` calls `access.derive_silver(day)` ONCE per Eastern day for which it wrote a
  bronze object, after all bronze puts of the fire and before the cursor is written.
- `access_client.lambda_invoker(lambda_client, function_name, qualifier=None)` passes `Qualifier=qualifier` to `invoke` when given.

**DOOR CONTRACT v2** (the far side, another cell): the collector alias serves `put` (bronze, state, gold), `derive_silver` (answers `{"ok", "rows"}`), `get_state` on the cursor key.
An unknown key shape is refused; your keys are the builder's.

### BUILD (Python 3.9+ syntax; flat modules in `collector/`, no relative imports, no `__init__.py`)

1. `collector/filter.py`, `collector/coverage_record.py`, `collector/collect.py`, `collector/source_client.py`, `collector/access_client.py` -- the changes above.
2. `data/m365_metadata/scripts/tests/test_collector.py` -- update and extend: per-fire coverage objects; a planted gap that survives the next fire; a window spanning two
   Eastern days splits its counts; the cursor trims by age and keeps the new ids; the id-only counter; `derive_silver` once per day; the keys equal builder output.
3. `infra/aws/lambda/m365-metadata-collector/handler.py` -- `lambda_handler` invokes the door with `qualifier="collector"` (a constant `ACCESS_ALIAS`); it reads the cursor
   through `get_state`; nothing else changes.
4. `infra/aws/terraform/trino/collector.tf` --
   - remove the three `data` blocks; reference `aws_secretsmanager_secret.m365_app_credential.arn` and `aws_secretsmanager_secret.m365_subject_key.arn` (declared in
     `identity.tf`) and `aws_lambda_alias.collector.arn` (declared in `access.tf`, another cell's file in the same root: reference it, never declare it);
   - the policy statement `InvokeTheAccessDoorOnly` has `Resource = aws_lambda_alias.collector.arn` (the alias ARN, not the function ARN);
   - `terraform fmt` clean; the collector role still holds NO S3 and NO KMS action; no alarm or notification resource.

### ACCEPTANCE

<criterion id="MD2-x2-AC1" cell_refs="MD-x-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_x2.py coverage</invocation><expect>X2-COVERAGE-OK</expect></criterion>
`MD2-x2-AC1` -- one coverage object per fire; a planted gap in fire 1 is still there after a clean fire 2; `derive_silver` is called once per Eastern day with bronze.

<criterion id="MD2-x2-AC2" cell_refs="MD-x-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_x2.py attribution</invocation><expect>X2-ATTRIBUTION-OK</expect></criterion>
`MD2-x2-AC2` -- a two-day window splits its listed and fetched counts by each blob's own day; the cursor trims by age; the id-only actor counter reads 1 on a planted GUID-only event.

<criterion id="MD2-x2-AC3" cell_refs="MD-x-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_x2.py invoker</invocation><expect>X2-INVOKER-OK</expect></criterion>
`MD2-x2-AC3` -- the keys equal builder output; the client invokes the collector alias; `collector.tf` has no data source and grants invoke on the alias ARN with no S3 or KMS action.

<criterion id="MD2-x2-AC4" cell_refs="MD-x-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_x2.py budget</invocation><expect>X2-BUDGET-OK</expect></criterion>
`MD2-x2-AC4` -- (the fourth mechanical criterion, with its reason in the amendment above) a fire stops at its time budget, saves what it did without advancing past the unprocessed, and the next fires finish the backlog with every blob fetched exactly once. Two invariants the CTO named (msg 6726) are inside it: every partial save still passes the population filter and the C-FIELDS levers BEFORE the write (the check plants an outsider's event, a subject, an internal and an external recipient in every blob and searches all stored bytes), and the cursor advances only past blobs whose writes landed (a bronze put that fails mid-fire must leave the cursor unwritten: a timeout loses nothing and duplicates nothing).

<expected_criteria>MD2-x2-AC1,MD2-x2-AC2,MD2-x2-AC3,MD2-x2-AC4</expected_criteria>

Dry-run at the base 2026-10-16 ~08:3xZ: each `X2-*-REFUSED AttributeError/TypeError ...` (no `fire_key`, no `bronze_key`, the listing returns bare ids) -- FAIL as expected. AC1 and AC2
were driven GREEN against a throwaway reference outside the repository. Run each from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **WORLD by the gate's path floor; NOTHING is run live.** No Microsoft or Management API call, no AWS call, no S3 access, no `terraform apply`/`init`.
  SYNTHETIC events only; no real event, address, subject, IP or file name enters the repository, in tests, fixtures, deliverables or your report.
- `access.tf`, `identity.tf`, `main.tf`, `population.json` and the door's `handler.py` are other cells' files or fixed: never edit them.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `TCKT_MTADTA-D1-W6-S<k>`), and do not
  weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_TCKT_MTADTA~6 <0.9.0_WK_TCKT_MTADTA~6@opal.agent>"`, `-F` a message file you write with the
  Write tool, and `-- <paths>`.

<paths>
data/m365_metadata/scripts/collector/filter.py
data/m365_metadata/scripts/collector/coverage_record.py
data/m365_metadata/scripts/collector/collect.py
data/m365_metadata/scripts/collector/source_client.py
data/m365_metadata/scripts/collector/access_client.py
data/m365_metadata/scripts/tests/test_collector.py
infra/aws/lambda/m365-metadata-collector/handler.py
infra/aws/terraform/trino/collector.tf
org/missions/D7/TCKT/TCKT_MTADTA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP_R2.md</decomp_doc> (round 2), cell `MD-x-2`.
<owned_cells>MD-x-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: MD2-x2-AC1, MD2-x2-AC2, MD2-x2-AC3, MD2-x2-AC4. Instance at `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.9.0_WK_TCKT_MTADTA~6/TCKT_MTADTA.TO-MD-x2.collector-repair.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> MD2-x2-AC1,MD2-x2-AC2,MD2-x2-AC3,MD2-x2-AC4` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three check lines, the `pytest` summary line, the `collector.tf` diff nature (resources touched), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the hourly rule is unchanged.
comp-iam: RUN at the apply (MD-r-1); the collector role stays free of S3 and KMS actions.
comp-adversary: DECLARED-NOT-APPLICABLE -- findings inlined: the CVO's remediation rows D1-W3-S2, D1-W3-S3, D1-W3-S5, D1-S2 (REMEDIATION_v1).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.4 C-POPULATION, C-COVERAGE, C-ACCESS; CTO rulings msgs 6585, 6590, 6591; decomposition round 2 cell MD-x-2 and the COLLECTOR and DOOR contracts.
