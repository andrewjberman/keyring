# TO MDPF_SECCLASS.TO-SC-e96 -- round 23 SC-e-96: READ: the producer's correction window, what re-deriving all of it costs, what truncating it leaves

<to_id>MDPF_SECCLASS.TO-SC-e96</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~86</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-96` (`decompositions/MDPF_SECCLASS_DECOMP_R23.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none | **source:** CTO round-22 analysis section 2 and section 3 item 1, msg 4333

---

## WORKER FACE

### THE CELL

`SC-e-96`, one read that the next order (`SC-e-97`, the same worker, after this one) takes its parameters from. The CTO ruled that C_06 re-derives,
on every fire, the dates inside the window **B_00 itself corrects**, the number read from B_00's rule at build time. This cell reads what that rule
is, where C_06 can read it, which dates it names today, what re-deriving all of them costs against a 30-minute budget, and how many dollars stay
wrong if the window is cut. Nothing is written to S3 or to a table.

Facts at HEAD you START from (read each, do not trust it): `data/black_diamond/scripts/gold/gold_dispatch.sh:99` is
`B_00|B_00.canonical_holdings.py|--upload --force-recent-days 14`; B_00's own default is 0
(`data/black_diamond/scripts/gold/B_00.canonical_holdings.py:1032`) and its cut is `anchor = newest cube date`, `cutoff = anchor - N calendar
days`, keep `d >= cutoff` (`:1119-1137`). C_06 lists its dates from `_list_positions_cube_keys` (`data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`
:393-401, `CANONICAL_HOLDINGS_PREFIX`) and builds one date through `process_date` (:587-) after `load_static_tables` (:541-). The served
per-date firm dollars are `firm[date]` in `gold/views/mix_daily_summary.json` in bucket `opal-data-bd`; each relationship's stored entries are in
`gold/entities/clients/{rid}.json` (top-level `.json`, skip `_views`).

**The record**, `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/WINDOW_READ_C06_ROLLING_20261012.json`, with these keys (the checker's header
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R23_CHECKS/r23_checks.py` lists every sub-key; read it first):

1. **`producer_rule`.** `source_file` and `source_line` where the number lives, `force_recent_days` as PARSED from that line by code (not typed),
   `anchor_rule` in a sentence, and `runtime_source`: the place C_06 can read the number at build time, which you VERIFY: (a) the S3 object
   `code/gold/gold_dispatch.sh` (head-object, then a get and a parse of the B_00 CATALOG line), and (b) whether the runner has the file beside the
   gold scripts when C_06 runs (read how the runner materializes `code/gold/`; if you cannot establish (b) from a read, say so in
   `runtime_source` and keep (a)). `readable_at_runtime` is true only if you READ the line from the source you name.
2. **`window`.** List the canonical partitions C_06 reads (paginate to exhaustion; print the key count), take their dates, and apply B_00's own
   arithmetic with the number from item 1: `anchor_date`, `cutoff_date`, `dates` (ascending; the dates inside the window today).
3. **`cost`.** Re-derive EVERY window date from the CURRENT canonical partitions through the code path the build uses (`load_static_tables` once,
   then `process_date` per date; import the module, do not copy it), read-only, in memory: `cold_wall_seconds` (first process, static load
   included), `warm_wall_seconds` (a second pass in the same process), `peak_mb` (process peak), then `relationships_rewritten` (read every stored
   relationship JSON and count those whose stored entries for the window dates DIFFER from the re-derived ones; bounded concurrency),
   `keys_written` (four keys per rewritten relationship: JSON and legacy copy, views and legacy copy) and `bytes_written` (the sizes of the payloads
   those writes would carry). `instrument` names the machine and the network path (this seat reads S3 over the internet; the runner sits in the
   region, so say that this is a measurement from here, not from the runner). `added_budget_seconds` is 1800; `fits` is whether
   `cold_wall_seconds <= 1800`; `largest_n_that_fits` is the largest number of NEWEST window dates whose cumulative cold wall stays within it
   (all of them when `fits` is true).
4. **`per_date`.** For each window date: `served_unclassified` (the stored firm figure), `rebuilt_unclassified` (the sum over relationships of
   `mix['unclassified'] * total_mv` from the re-derived entries), `delta_unclassified` (rebuilt minus served), and the two orphan counts:
   `relationships_stored_not_in_partition` (a relationship whose stored JSON carries that date and the partition no longer has it) and
   `relationships_in_partition_not_stored` (the reverse).
5. **`gap_if_truncated`.** One row per `newest_n` from 1 to the number of window dates: the sum over the window dates NOT among the newest
   `newest_n` of `|delta_unclassified|`. It is non-increasing and ends at 0.
6. Also fill `claim` (one sentence naming read-only, the time of the read and the partition versions you read) and `read_only: true`.

### ACCEPTANCE

<criterion id="SC23-e96-AC1" cell_refs="SC-e-96"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R23_CHECKS/r23_checks.py window-read org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/WINDOW_READ_C06_ROLLING_20261012.json</invocation><expect>WINDOW-READ ok=True</expect></criterion>
`SC23-e96-AC1` -- the record exists with the rule, the window, the cost, the per-date figures and the gap, its arithmetic is internally consistent, and
a copy with one field broken fails the same check first.

<expected_criteria>SC23-e96-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-12 ~11:3xZ): `WINDOW-READ ok=False error=absent`; a synthetic valid record reads `ok=True
control=ok`; one with `fits` that disagrees with the cold wall, one whose gap does not end at 0 and one with fewer than five dates each read
`ok=False`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, list_object_versions, DynamoDB get_item, ec2 describe): no write to any bucket or table, no deploy, no
  invoke. Never push. The re-derived entries live in memory and in `.scratch/` only.
- A command that needs more than `timeout 120` runs in the background (`run_in_background`) and is read when it ends; keep each date's result on
  disk under `.scratch/` so a stop loses nothing. The static-table load is the slow part: do it once per process.
- **Client data stays out.** Aggregate figures only: no relationship id, account id or client name in the record, the report or a surprise row.
- **Refusal clause.** If a figure cannot be read as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W86-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not estimate a figure and do not fill a field you did not read.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/WINDOW_READ_C06_ROLLING_20261012.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R23.md</decomp_doc> (round 23), cell `SC-e-96`.
<owned_cells>SC-e-96</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC23-e96-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~86/MDPF_SECCLASS.TO-SC-e96.c06-rolling-window-read.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC23-e96-AC1`.
</proof_of_spec>

**REPORT:** the rule and where C_06 can read it, the window dates, the cost (cold, warm, peak, relationships, keys, bytes) beside the 1,800-second
budget and `fits`, the per-date served against rebuilt Unclassified and the orphan counts, the gap table (the rows at newest_n 1, 5 and the full
window), commits, rows. Then stop: the next order is handed to you by the issuer.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE a read the seat's role already makes (the same reads as SC-e-95).
comp-adversary: RUN -- a window typed from the dispatcher line instead of parsed (the field is graded for its parse and the record carries the line); a cost taken on a warm process only (cold and warm are both required, and `fits` is graded on the cold one); a cost measured on a sample of dates (`dates_rederived` must equal the window); a gap table that does not end at zero (the checker refuses it). BLIND: the runner's own wall time, which this seat cannot measure; the record says so in `instrument`.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-22 analysis section 2 and section 3 item 1 (msg 4333); SC-e-95's record `RESIDUAL_READ_C06_FREEZE_20261012.json`; DECOMP_R23.
