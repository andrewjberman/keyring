# TO MDPF_SECCLASS.TO-SC-e112.e18-fire-line-read -- round 29 SC-e-112: read E_18's own stdout line for the 23:00Z fire (a read; nothing is changed)

<to_id>MDPF_SECCLASS.TO-SC-e112</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~101</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-18</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-112` (`decompositions/MDPF_SECCLASS_DECOMP_R29.md`) |
**outcome_ref:** S42 disarm (row MDPF_SECCLASS-D1-S42, ARMED) | **depends_on:** none | **source:** CTO round-28 analysis section 3 item 1a (msg 7829)

---

## WORKER FACE

### THE CELL

`SC-e-112`. The nightly Black Diamond gold chain fired at 2026-10-17T23:00:11Z (the runner instance `i-01003b035d2988dfb` launched then). Its E_18 step (`data/black_diamond/scripts/gold/E_18.detect_new_securities.py`) ran at 2026-10-18T00:05:04Z to 00:05:07Z and wrote `gold/.checkpoints/2026-10-17/E_18.done` in bucket `opal-data-bd` at 00:05:09Z. E_18 prints a summary block; one line reads `Scheduled-classification candidates:      <n>` (see the print at about line 255 of the script). The telemetry object for that run (`logs/gold-layer/telemetry/bd-gold-layer-runner/E_18/f98551718369.jsonl`) holds only CPU and memory rows, NOT that line. You find the SERVED artifact that holds E_18's stdout for that fire and quote the summary line from it.

**What is already known (start from it):**
- The earlier ship test run of E_18 (2026-10-17 08:40Z, by `0.7.0_AE_CloudOps~DELL1`) printed `Scheduled-classification candidates: 0`, `Already resolved (in resolution table): 9`, `Truly unresolved: 72`; that was a single run, not the fire. The CTO's disarm of S42 needs the FIRE's own line.
- Where such a stdout may live (not asserted, look): `s3://opal-data-bd/logs/gold-layer/` under a date or run folder other than `telemetry/`; `gold/perf_report.json` and `gold/perf_history/`; the gold runner's CloudWatch log group (find it with `describe-log-groups`, names containing `gold` or `bd-gold-layer-runner`); the SSM command output of the boot chain for that instance start. Run a positive control on every listing (a listing that returns a known object) before you accept an empty result.

**What you do:** (1) Find the artifact. (2) Quote the line verbatim, with the neighbouring `Already resolved`, `Scheduled rows written / refused` lines. (3) Write `E18_FIRE_LINE.json` at the path in `<paths>`.

`E18_FIRE_LINE.json` has exactly these keys (the script lists them in its header; read `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R29_CHECKS/check_r29_reads.py`, do not edit it):
- `source`: either `{"type": "s3", "bucket": ..., "key": ..., "version_id": optional}` or `{"type": "cloudwatch", "log_group": ..., "log_stream": optional, "start_ms": ..., "end_ms": ...}` (epoch milliseconds around 2026-10-18T00:05Z). The checker re-reads it live; the source must be timestamped between 2026-10-18T00:04Z and 03:00Z.
- `line`: the exact `Scheduled-classification candidates: ...` line as it appears in the source (the checker requires it to be a substring of the source text).
- `candidates`, `already_resolved`, `written`, `refused`: integers from the neighbouring lines.

### ACCEPTANCE

<criterion id="SC29-e112-AC1" cell_refs="SC-e-112"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R29_CHECKS/check_r29_reads.py e18-line</invocation><expect>R29-e18-line ok=True</expect></criterion>
`SC29-e112-AC1` -- the quoted line is found in a served source written in the fire's window and its figure equals the `candidates` field.

<expected_criteria>SC29-e112-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-18 ~02:0xZ): AC1 FAILS as expected (`R29-e18-line ok=False problems=['no file at ...E18_FIRE_LINE.json']`). The script's `selftest` runs a green arm and negative arms for every mode and prints `R29-SELFTEST ok=True`; its live readers were checked against known numbers (the served 2026-10-02 delta +407,720.32; the live CodeSha256 of opal-partners-data).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **AWS READS ONLY** (S3 `list-object-versions`, `head-object`, `get-object`, `list-objects-v2`; CloudWatch Logs `filter-log-events`, `describe-log-groups`, `describe-log-streams`; Lambda `get-function`, `get-function-configuration`; SSM `get-command-invocation`, `list-command-invocations`; through `.tools/aws` or boto3). No write, delete, copy, put, tag, invoke, start, stop or deploy of any kind. Nothing is changed.
- **No package install and no download** into the repo. pandas, pyarrow and boto3 are installed.
- **Never edit** anything outside the `<paths>` block; the script under `R29_CHECKS/` is READ-ONLY to you. Never push.
- **Append to the surprise channel in BYTE MODE** (`open(path, 'ab')`), one new row only if you file one: never read and rewrite that file (it mixes CRLF and LF blocks and a round trip changes the old bytes).
- **Refusal clause.** If you cannot do what the cell asks, do not guess and do not edit a check. Write what you read (with each listing's positive control) in your report, file a surprise row (id `MDPF_SECCLASS-D1-W101-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) naming what you could not account for, and stop; leave AC1 failing.
- Run every invocation under `timeout 120`; bound each of your own reads by key or prefix, never sweep a whole bucket.

<paths>
org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~101/E18_FIRE_LINE.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R29.md</decomp_doc> (round 29), cell `SC-e-112`.
<owned_cells>SC-e-112</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC29-e112-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~101/MDPF_SECCLASS.TO-SC-e112.e18-fire-line-read.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC29-e112-AC1`.
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
