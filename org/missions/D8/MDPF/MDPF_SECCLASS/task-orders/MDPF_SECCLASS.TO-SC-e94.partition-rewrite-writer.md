# TO MDPF_SECCLASS.TO-SC-e94 -- round 21 SC-e-94: READ: what rewrote the 2026-10-06 and 2026-10-07 holdings partitions at 2026-10-10T23:15Z

<to_id>MDPF_SECCLASS.TO-SC-e94</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~83</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-94` (`decompositions/MDPF_SECCLASS_DECOMP_R21.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none | **source:** CTO round-20 analysis section 2 (D1-W78-S1), msg 4321

---

## WORKER FACE

### THE CELL

`SC-e-94`, row MDPF_SECCLASS-D1-W78-S1. Worker ~78 recomputed C_06's firm totals for 2026-10-06, 07 and 08 from the current canonical holdings
partitions and found only 2026-10-08 reproduces to the cent: the recomputed 10-06 and 10-07 totals exceed the served ones by $584,886.01 and
$442,485.38. All three partitions were last written 2026-10-10T23:15Z, AFTER the served snapshot (2026-10-10T05:26Z). The cause of the
partition change was not traced. This cell traces it, read-only, and answers one more question the leg G comparator rests on.

**Read (no build, no edit of any product file):**
1. The three partitions: C_06 lists them in `_list_positions_cube_keys()` (`C_06.client_mix_timeseries.py` :324-332) under
   `CANONICAL_HOLDINGS_PREFIX` in the bucket named by `platinum_source`. For 2026-10-06 and 2026-10-07 (and 2026-10-08 as the comparison),
   record each key, its `LastModified` and the version list of the key (`list_object_versions`, with the `LastModified` of every version).
2. **Name the writer** of the 2026-10-10T23:15Z versions. Use, in this order, whatever resolves it: the object's own metadata; the BD gold runner's
   telemetry and logs for the window (`opal-data-bd`, `logs/gold-layer/`, runs launched 2026-10-10 about 23:00Z by `bd-gold-trigger`; the
   script that wrote that prefix is named by `comp-pipescript io <script> --pipeline <tree>` or by grepping `data/black_diamond/scripts/` for the
   prefix); CloudTrail management events for the instance and the Lambda. State which source named it and how confident it is
   (`identified_by`).
3. **Count the writers** of the canonical holdings prefix inside the window 2026-10-10T23:00Z to 23:30Z: distinct scripts or principals that
   put an object under it, from the same sources (an integer, at least 1).
4. State whether the NEXT C_06 fire re-serves those dates: C_06 runs incremental (`build()` :659-692) and builds only partitions dated after
   the watermark `gold/client_timeseries/_watermark.json`. Read the watermark's value now, name the dates C_06 would build next, and answer
   yes or no with the line numbers that decide it (`c06_reserves_dates_next_fire`, with `c06_reason`).
5. Write the record as JSON at
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/W78_PARTITION_REWRITE_WRITER_20261012.json` with exactly these keys: `claim`
   (`measured: read-only, <date and time of the read>`), `partitions` (a list of `date`, `key`, `last_modified`, `version_count`),
   `rewrite_window` (`from`, `to`), `writer` (`principal`, `identified_by`, `script_or_lambda`), `writer_count`,
   `c06_reserves_dates_next_fire` (true or false), `c06_reason`, and `ruling_on_correction_or_drift` set to `null` (the ruling follows the read).
6. Security-level only: no relationship id, account id or client name in the record or the report.

### ACCEPTANCE

<criterion id="SC21-e94-AC1" cell_refs="SC-e-94"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R21_CHECKS/r21_read_record_check.py w78 org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/W78_PARTITION_REWRITE_WRITER_20261012.json</invocation><expect>W78-RECORD ok=True</expect></criterion>
`SC21-e94-AC1` -- the record exists, names the writer and the partitions, counts the writers and answers the re-serve question (a synthetic record with one field broken fails the same check first).

<expected_criteria>SC21-e94-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-12 ~09:3xZ): SC21-e94-AC1 FAIL as expected (`W78-RECORD ok=False error=absent`).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, list_object_versions, DynamoDB get_item, CloudTrail lookup): no write, no deploy, no invoke. Never push.
- A source that cannot name the writer is reported as such (`identified_by` says what was tried); do not guess a writer from timing alone
  unless you state that it is timing alone and set the writer's `principal` to `UNRESOLVED-BY-TIMING-ONLY`.
- **Refusal clause.** If the read cannot be done as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-W83-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not fill a field you did not read.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/W78_PARTITION_REWRITE_WRITER_20261012.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R21.md</decomp_doc> (round 21), cell `SC-e-94`.
<owned_cells>SC-e-94</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC21-e94-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~83/MDPF_SECCLASS.TO-SC-e94.partition-rewrite-writer.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC21-e94-AC1`.
</proof_of_spec>

**REPORT:** the three partitions with their versions, the writer and the source that named it, the writer count, the watermark and the re-serve answer, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE a read the seat's role already makes.
comp-adversary: RUN -- a writer named from timing alone (the order says so when it is); the 23:00Z fallback fire's own scripts conflated with a manual run (the sources are listed with the answer); a paginated version list counted as a total (list_object_versions is paginated to exhaustion and its page count printed). BLIND: S3 object-level data events are not in CloudTrail lookup, so the writer may rest on runner telemetry and the script's own write target.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-20 analysis section 2 (D1-W78-S1 ruling) and section 3 item 4 (msg 4321); row D1-W78-S1 (worker ~78); DECOMP_R21.
