# TO MDPF_SECCLASS.TO-SC-e113.d1016-absence-read -- round 29 SC-e-113: why 2026-10-16 is absent from the 00:24Z served mix version (a read; nothing is changed)

<to_id>MDPF_SECCLASS.TO-SC-e113</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~102</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-18</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-113` (`decompositions/MDPF_SECCLASS_DECOMP_R29.md`) |
**outcome_ref:** FWD-1 (the served firm mix) | **depends_on:** none | **source:** CTO round-28 analysis section 2 and 3 item 1b (msg 7829)

---

## WORKER FACE

### THE CELL

`SC-e-113`. The served object is bucket `opal-data-49financial`, key `advi/49financial/platinum/views/mix_daily_summary.json`; JSON `firm[<date>]` holds one entry per firm date. Version `0IrqqSvyNAbXY34LxfRcAx0DtjM9PODv` was written 2026-10-18T00:24:42Z, after the 23:00Z fire of Saturday 2026-10-17. Its last date is 2026-10-15; there is NO 2026-10-16 entry. By `lib/trading_calendar.py` (`expected_last_trading_day`) the frontier for a run at that time is 2026-10-16 (a Friday), so the date should exist. You name the producer step that dropped or never wrote 2026-10-16, and why.

**What is already known (start from it):**
- The previous version `l2Wqoi6iUJwQwwmTCu3lXWozfW4.Ak_.` (2026-10-17T05:24:08Z) has its own last date; compare. The nightly chain is `gold_dispatch.sh` (catalog lines near line 99; `B_00` runs `--force-recent-days 14`); the served file is written by `C_06.client_mix_timeseries.py` (rolling window, `restated_through`); its inputs include `gold/canonical/holdings/<date>.parquet`, `gold/timeseries/positions_cube/<date>.parquet` and `gold/holdings_lots/<date>.parquet` in bucket `opal-data-bd`.
- The 23:00Z fire was a Saturday-night fallback fire; the nightly 04:00Z fire runs Monday to Saturday. Weekend and holiday handling lives in `lib/trading_calendar.py` and in whatever anchors each producer's date window (a producer anchored on "the latest date present in its input" will stop at the input's last date, not at the calendar frontier).

**What you do:** (1) Read the last dates of the two served versions. (2) For each producer step in the chain (B_00 canonical holdings, A_03 positions cube, the lots writer B_01, C_06), find whether an object for 2026-10-16 exists in its output and when it was written (`list-object-versions` of `gold/canonical/holdings/2026-10-16.parquet`, `gold/timeseries/positions_cube/2026-10-16.parquet`, `gold/holdings_lots/2026-10-16.parquet`; positive control each listing with a date that exists). (3) Name the FIRST step in the chain whose output lacks 2026-10-16, and read that step's code to say why (an input missing for that date, a window anchored on its input's latest date, or a calendar rule). (4) Write `D1016_ABSENCE.json` at the path in `<paths>`.

`D1016_ABSENCE.json` has exactly these keys (the script lists them in its header; read `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R29_CHECKS/check_r29_reads.py`, do not edit it):
- `served`: `{"bucket": "opal-data-49financial", "key": "advi/49financial/platinum/views/mix_daily_summary.json", "version_id": "0IrqqSvyNAbXY34LxfRcAx0DtjM9PODv"}`.
- `tail_date`: the last `firm` date of that version (the checker recomputes it).
- `missing_date`: `"2026-10-16"`.
- `frontier_date`: the date `lib/trading_calendar.expected_last_trading_day` returns for the version's write time (the checker recomputes it).
- `producer_step`: a file name under `data/black_diamond/scripts/gold/` (for example `C_06.client_mix_timeseries.py`).
- `reason`: at least 40 characters, in plain English.

### ACCEPTANCE

<criterion id="SC29-e113-AC1" cell_refs="SC-e-113"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R29_CHECKS/check_r29_reads.py calendar</invocation><expect>R29-calendar ok=True</expect></criterion>
`SC29-e113-AC1` -- the tail date, the absence of 2026-10-16 and the calendar frontier are recomputed from the served version and the repo, and the producer step is a real gold script with a reason.

<expected_criteria>SC29-e113-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-18 ~02:0xZ): AC1 FAILS as expected (`R29-calendar ok=False problems=['no file at ...D1016_ABSENCE.json']`). The script's `selftest` runs a green arm and negative arms for every mode and prints `R29-SELFTEST ok=True`; its live readers were checked against known numbers (the served 2026-10-02 delta +407,720.32; the live CodeSha256 of opal-partners-data).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **AWS READS ONLY** (S3 `list-object-versions`, `head-object`, `get-object`, `list-objects-v2`; CloudWatch Logs `filter-log-events`, `describe-log-groups`, `describe-log-streams`; Lambda `get-function`, `get-function-configuration`; SSM `get-command-invocation`, `list-command-invocations`; through `.tools/aws` or boto3). No write, delete, copy, put, tag, invoke, start, stop or deploy of any kind. Nothing is changed.
- **No package install and no download** into the repo. pandas, pyarrow and boto3 are installed.
- **Never edit** anything outside the `<paths>` block; the script under `R29_CHECKS/` is READ-ONLY to you. Never push.
- **Append to the surprise channel in BYTE MODE** (`open(path, 'ab')`), one new row only if you file one: never read and rewrite that file (it mixes CRLF and LF blocks and a round trip changes the old bytes).
- **Refusal clause.** If you cannot do what the cell asks, do not guess and do not edit a check. Write what you read (with each listing's positive control) in your report, file a surprise row (id `MDPF_SECCLASS-D1-W102-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) naming what you could not account for, and stop; leave AC1 failing.
- Run every invocation under `timeout 120`; bound each of your own reads by key or prefix, never sweep a whole bucket.

<paths>
org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~102/D1016_ABSENCE.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R29.md</decomp_doc> (round 29), cell `SC-e-113`.
<owned_cells>SC-e-113</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC29-e113-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~102/MDPF_SECCLASS.TO-SC-e113.d1016-absence-read.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC29-e113-AC1`.
</proof_of_spec>

**REPORT:** what you found and where (paths, version ids, times), the criterion's output verbatim, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships.
comp-iam: DECLARED-NOT-APPLICABLE only the reads the seat's role already makes.
comp-adversary: RUN -- a file that quotes text the check does not find in the source; a number typed rather than recomputed (the check recomputes it from S3, the repo or the live Lambda); a path that does not exist; a reason under its length floor.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-28 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_28_20261018.md`, msg 7829); DECOMP_R29.
