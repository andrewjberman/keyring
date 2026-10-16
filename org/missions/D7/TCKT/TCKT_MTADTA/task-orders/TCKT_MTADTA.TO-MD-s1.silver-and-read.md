# TO TCKT_MTADTA.TO-MD-s1 -- silver (bronze events to sorted parquet) and the one-day read through the door

<to_id>TCKT_MTADTA.TO-MD-s1</to_id>
<project>TCKT_MTADTA</project>
<issued_to>0.9.0_WK_TCKT_MTADTA~4</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D7 | **Fabric:** dell1 | **Decomp cell:** `MD-s-1` (`decompositions/TCKT_MTADTA_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (you build to the BRONZE CONTRACT and the SILVER CONTRACT below)

---

## WORKER FACE

### THE CELL

`MD-s-1`, SILVER and the READ: the last two hops of FWD-1. "Andrew picks one of the eight operations team members and a trading day, and
reads that person's Microsoft 365 day in order, from collection that is actually running; nothing on the page was typed in by hand." Two
files, both pure and testable without a network:

1. `silver_builder.py` -- the function the access Lambda calls inside the door to turn one Eastern date's bronze events into a sorted
   parquet partition (bronze is read only inside the door; this is why it lives beside the Lambda).
2. `read_day.py` -- what Andrew runs: it asks the door for one person's day and prints it in time order, in Eastern time.

### THE CONTRACTS (fixed by the decomposition; build to them exactly)

**BRONZE CONTRACT (your input).** `build` receives a list of dicts, each with exactly the keys: `event_id, creation_time (ISO UTC, trailing Z),
workload, operation, record_type, result_status, actor (a lower-cased member UPN), subject_hash (64 hex or null), participants (list of
strings: a member UPN | "internal-other" | "external"), site, file_id, file_name, extension, folder, client_ip_class ("office" | "remote" |
"unknown")`.

**SILVER CONTRACT (your output).** `build(events: list[dict]) -> bytes` is a parquet file (pyarrow), one row per event, SORTED by
`creation_time`, columns in EXACTLY this order: `event_id, creation_time, date, actor, workload, operation, record_type, result_status,
subject_hash, participants, site, file_id, file_name, extension, folder, client_ip_class`. `participants` is the list comma-joined into one
string. `date` is the America/New_York calendar date of `creation_time` (so `2026-10-16T02:30:00Z` is `2026-10-15`; the partition boundary
is Eastern midnight). `partition_date(iso: str) -> "YYYY-MM-DD"` returns that Eastern date; use `zoneinfo.ZoneInfo("America/New_York")`.

**THE DOOR (what `read_day.py` calls).** The Lambda `globgrph-trino-access-lambda` answers `{"op": "get_day", "person": <UPN>, "date":
"YYYY-MM-DD"}` with `{"ok": true, "rows": [<silver row dicts, time-ordered>]}` or `{"ok": false, "error": ...}`. Rows carry the silver
columns above (`participants` as a comma-joined string, or a list: accept both).

### BUILD (Python 3.9+ syntax; `pyarrow` is imported only inside `silver_builder.py`)

1. **`infra/aws/lambda/globgrph-trino-access/silver_builder.py`** -- `build`, `partition_date`, exactly as above.
2. **`infra/aws/lambda/globgrph-trino-access/tests/test_silver_builder.py`** -- pytest: column order, sort order, the Eastern boundary on both
   sides (`2026-10-16T03:59:59Z` -> `2026-10-15`; `2026-10-16T04:00:00Z` -> `2026-10-16`), an empty input gives a valid empty table with the
   same columns, a round trip through `pyarrow.parquet.read_table`.
3. **`data/m365_metadata/scripts/silver/read_day.py`** --
   - `EIGHT`: the eight UPNs (`andrew`, `alyssa`, `bobby`, `manav`, `yang`, `menachem`, `jim`, `jeanette`, each `@opalinvest.com`).
   - `fetch(invoker, person, date) -> list[dict]`: raises `ValueError` for a person outside `EIGHT` BEFORE any call; otherwise calls
     `invoker({"op": "get_day", "person": person, "date": date})` ONCE and returns `rows`; raises `RuntimeError` carrying the door's `error`
     when `ok` is false.
   - `render(rows) -> str`: one line per row, ascending by `creation_time`, `HH:MM:SS` in America/New_York, then the operation, the
     workload and the file name (blank when absent); a day with no rows renders the single line `no activity collected for this day` (never
     an empty string).
   - `main(argv)`: `--person`, `--date`; builds the real invoker with `boto3.client("lambda")` inside `main` only, invoking the function named
     by `lib.opal_naming.name('globgrph', None, 'trino-access', 'lambda')`; prints `render(fetch(...))`. Not exercised in round 1.
4. **`data/m365_metadata/scripts/tests/test_read_day.py`** -- pytest: order, Eastern times, the non-member refusal makes no call, the empty-day line.

### ACCEPTANCE

<criterion id="MD1-s1-AC1" cell_refs="MD-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_s1.py silver</invocation><expect>S1-SILVER-OK</expect></criterion>
`MD1-s1-AC1` -- bronze events become a sorted parquet table with the ruled columns and Eastern-date partition.

<criterion id="MD1-s1-AC2" cell_refs="MD-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_s1.py readday</invocation><expect>S1-READDAY-OK</expect></criterion>
`MD1-s1-AC2` -- one person's day is fetched through an injected invoker, rendered in time order in Eastern time, and a non-member never reaches the door.

<expected_criteria>MD1-s1-AC1,MD1-s1-AC2</expected_criteria>

Dry-run at the base 2026-10-16 ~06:5xZ: AC1 `SILVER-REFUSED missing ...silver_builder.py`, AC2 `READDAY-REFUSED missing ...read_day.py` -- each
FAIL as expected; both were also driven GREEN against a throwaway reference outside the repository. Run from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **WORLD by the gate's path floor (`infra/`); NOTHING is run live.** No AWS call, no S3 access, no Lambda invoke. SYNTHETIC events only; no
  real address, subject, IP or file name enters the repository.
- `handler.py`, `build.sh` and `tests/test_handler.py` in the Lambda's folder belong to the `MD-a-1` cell: never create or edit them.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `TCKT_MTADTA-D1-W4-S<k>`), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_TCKT_MTADTA~4 <0.9.0_WK_TCKT_MTADTA~4@opal.agent>"`, `-F` a message
  file you write with the Write tool, and `-- <paths>`.

<paths>
infra/aws/lambda/globgrph-trino-access/silver_builder.py
infra/aws/lambda/globgrph-trino-access/tests/test_silver_builder.py
data/m365_metadata/scripts/silver/read_day.py
data/m365_metadata/scripts/tests/test_read_day.py
org/missions/D7/TCKT/TCKT_MTADTA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP.md</decomp_doc> (round 1), cell `MD-s-1`.
<owned_cells>MD-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: MD1-s1-AC1, MD1-s1-AC2. Instance at `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.9.0_WK_TCKT_MTADTA~4/TCKT_MTADTA.TO-MD-s1.silver-and-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> MD1-s1-AC1,MD1-s1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two check lines, the `pytest` summary lines of your own tests, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: DECLARED-NOT-APPLICABLE for this cell -- no principal; `read_day.py` is invoked by a member of the access group.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round. The FWD-1 ACCEPT line (nothing typed by hand) is the real run at release act 4.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.2 FWD-1, C-ACCESS, SURFACE MANIFEST R1 C5; decomposition cell MD-s-1, the BRONZE and SILVER CONTRACTS.
