# TO MDPF_SECCLASS.TO-SC-e93 -- round 21 SC-e-93: READ: how many served BD positions carry the literal ticker NAN or NONE

<to_id>MDPF_SECCLASS.TO-SC-e93</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~82</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-93` (`decompositions/MDPF_SECCLASS_DECOMP_R21.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none | **source:** CTO round-20 analysis section 2 (D1-W77-S1), msg 4321

---

## WORKER FACE

### THE CELL

`SC-e-93`, row MDPF_SECCLASS-D1-W77-S1. Worker ~77 found that the shared lib
`data/black_diamond/scripts/gold/lib/etf_classifier.py` treats a ticker string `NAN` or `NONE` as a BLANK ticker: it runs the blank-ticker
identity chain (CUSIP, then exact name, then the name's one CUSIP) before the `NAME::` row, so those positions are not placed by the
ticker-no-row path SC-e-87 reaches. Whether any SERVED position carries such a ticker was NOT measured. This cell measures it, read-only.

**Read (no build, no edit of any product file):**
1. Find C_06's canonical holdings partitions: `C_06.client_mix_timeseries.py` imports `CANONICAL_HOLDINGS_PREFIX` and `platinum_source` and
   lists them in `_list_positions_cube_keys()` (:324-332); `_process_partition` (:146) shows which columns it reads. Take the LATEST
   partition key (the last of the sorted list) and read it with a read-only `get_object`.
2. Count the rows whose ticker, after `str(t).strip().upper()`, equals `NAN` and the rows equal to `NONE`, separately, and the dollars of each
   (the partition's market-value column). Print the denominator beside them: total rows and total dollars in the same partition, and the
   partition's key and date.
3. Write the record as JSON at
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NAN_NONE_TICKER_COUNT_20261012.json` with exactly these keys: `claim`
   (`measured: read-only, partition <key>, <date and time of the read>`), `partition` (`key`, `date`), `positions_total`, `dollars_total`,
   `nan_none` (`NAN` and `NONE`, each `positions` and `dollars`), `nan_none_positions`, `nan_none_dollars`, `verdict`
   (`NOT_EXPOSED` when `nan_none_positions` is 0, else `EXPOSED`), `read_only` (true). Round dollars to the cent.
4. Security-level only: no relationship id, account id or client name in the record or the report.
5. If the count is non-zero, add to the report the ten largest by dollars as (ticker as read, asset name, dollars) and, for each, whether its
   name has a `NAME::` row in `etf-classifications` (`get_item` only). Do not draw a conclusion; the ruling is the CTO's.

### ACCEPTANCE

<criterion id="SC21-e93-AC1" cell_refs="SC-e-93"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R21_CHECKS/r21_read_record_check.py w77 org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NAN_NONE_TICKER_COUNT_20261012.json</invocation><expect>W77-RECORD ok=True</expect></criterion>
`SC21-e93-AC1` -- the record exists with its denominator and its totals agree (a synthetic record with one field broken fails the same check first).

<expected_criteria>SC21-e93-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-12 ~09:3xZ): SC21-e93-AC1 FAIL as expected (`W77-RECORD ok=False error=absent`).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, DynamoDB get_item): no write to any table or bucket, no deploy, no invoke. Never push.
- Read ONE partition fully; do not sweep the prefix. A read that would exceed `timeout 120` is split by column, not by sampling rows.
- **Refusal clause.** If the read cannot be done as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-W82-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not estimate a count.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NAN_NONE_TICKER_COUNT_20261012.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R21.md</decomp_doc> (round 21), cell `SC-e-93`.
<owned_cells>SC-e-93</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC21-e93-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~82/MDPF_SECCLASS.TO-SC-e93.nan-none-ticker-count.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC21-e93-AC1`.
</proof_of_spec>

**REPORT:** the partition read (key, date, rows, dollars), the NAN and NONE counts and dollars, the verdict, the top ten if non-zero, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE a read the seat's role already makes.
comp-adversary: RUN -- a count taken on a sample or on a stale partition (the latest key is read and named); a literal `nan` produced by pandas for a missing ticker counted as the string `NAN` (the worker counts the string value as read, and reports separately how many tickers were null); a case or whitespace variant missed (`strip().upper()`). BLIND: positions whose ticker is the text `N/A` or `-`, which this read does not count.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-20 analysis section 2 (D1-W77-S1 ruling: MEASURE first) and section 3 item 3 (msg 4321); row D1-W77-S1 (worker ~77); DECOMP_R21.
