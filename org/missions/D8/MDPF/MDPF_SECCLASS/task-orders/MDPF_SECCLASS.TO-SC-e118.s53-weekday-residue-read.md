# TO MDPF_SECCLASS.TO-SC-e118.s53-weekday-residue-read -- round 30 SC-e-118: name the step and the class behind the $32k Monday-to-Thursday gap between the served TOTAL and the canonical holdings (a read)

<to_id>MDPF_SECCLASS.TO-SC-e118</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~106</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-118` (`decompositions/MDPF_SECCLASS_DECOMP_R30.md`) |
**outcome_ref:** FWD-1 (the served firm mix) | **depends_on:** none | **source:** CTO round-29 analysis section 4 item 2 (msg 8326); row MDPF_SECCLASS-D1-S53

---

## WORKER FACE

### THE CELL

`SC-e-118`. The served firm TOTAL (`mix_daily_summary.json`) ran about $31.6k to $32.2k BELOW the canonical holdings' total on every Monday-to-Thursday date of 2026-10-01 to 2026-10-14, and exactly equal on Friday, Saturday and Sunday dates (a 14-date reconciliation, worker `~103`, file `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~103/S48_RANGE_RECON.json`: read it first; its `rows` give the residue per date and its `served` and `canonical` blocks pin the S3 versions you read). Nobody has read WHY a weekday gap exists. You find out, and you change nothing.

**What you do:**
1. For at least 3 Monday-to-Thursday dates (for example 2026-10-05, 2026-10-06, 2026-10-07) and at least 2 dates with a zero residue (for example 2026-10-09 and 2026-10-10), split the residue by class: the served class totals of that date (the pinned `post_version_id` of `mix_daily_summary.json`, `firm[<date>]`) against the canonical holdings of that date (the pinned `after_version_id` of `gold/canonical/holdings/<date>.parquet`, summed by its own class column, or by the served class names if you map them; say how in the `summary`). Find which class carries the gap and by how much.
2. Within that class, find the holdings (by ticker or name) that make up the gap on a Monday-to-Thursday date and are present in the canonical holdings but absent from the served total, and say whether the same holdings exist on the zero-residue dates.
3. Read the producer's own rule for the TOTAL (the gold script that builds `mix_daily_summary.json`: find it with `Glob data/black_diamond/scripts/gold/C_06*` and read what it keeps and drops; also `A_03.positions_cube.py` and `B_00` if the rule is upstream) and name the ONE step and line whose rule leaves out those holdings on Monday-to-Thursday dates. Read `lib/trading_calendar.py` and name the function the step's weekday or trading-day logic is read against (a function name that `def <name>` finds in that file).
4. If you cannot name the step from what you read, say so: set `cause_named` to false, list what you did not read in `not_read`, and stop. A named cause you did not read is the one wrong answer.

`S53_CAUSE.json` has exactly these keys (the checker `R30_CHECKS/check_r30_reads.py` lists them in its header; read it, do not edit it):
- `dates`: one object per date you split, `{"date": "YYYY-MM-DD", "residue": <number copied from the recon row>, "classes": {"<class>": <number>, ...}}`; the class numbers sum to the residue within 1.00. At least 3 Monday-to-Thursday dates with a non-zero residue and at least 2 dates with a zero residue.
- `step`: `{"file": "<repo path from the repo root, forward slashes>", "line": <int>, "quote": "<12 or more characters copied from that line or within 2 lines of it>"}`.
- `calendar`: `{"file": "lib/trading_calendar.py", "function": "<name>"}` (or the real path of the calendar module if it lives elsewhere; the checker looks for `def <name>` in it).
- `cause_named`: `true`, or `false` with a non-empty `not_read` list.
- `summary`: 80 or more characters: the class that carries the gap, the holdings, the step, and whether a weekday rule explains Monday-to-Thursday but not Friday to Sunday.

### ACCEPTANCE

<criterion id="SC30-e118-AC1" cell_refs="SC-e-118"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R30_CHECKS/check_r30_reads.py s53-cause</invocation><expect>R30-s53-cause ok=True</expect></criterion>
`SC30-e118-AC1` -- the residues equal the reconciliation file's, each date's class numbers sum to its residue, the weekday split holds, the quoted step is in the repo file and the calendar function is defined.

<expected_criteria>SC30-e118-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-19 ~15:0xZ): AC1 FAILS as expected (`R30-s53-cause ok=False problems=['no file at ...S53_CAUSE.json']`). The script's `selftest` runs a green arm and negative arms and prints `R30-SELFTEST ok=True`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **AWS READS ONLY** (S3 `list-object-versions`, `head-object`, `get-object`, `list-objects-v2`; through `.tools/aws` or boto3). No write, delete, copy, put, tag, invoke, start, stop or deploy of any kind. Nothing is changed.
- **No package install and no download** into the repo. pandas, pyarrow and boto3 are installed.
- **Never edit** anything outside the `<paths>` block; the script under `R30_CHECKS/` is READ-ONLY to you. Never push.
- **Append to the surprise channel in BYTE MODE** (`open(path, 'ab')`), one new row only if you file one: never read and rewrite that file (it mixes CRLF and LF blocks and a round trip changes the old bytes).
- **Refusal clause.** If you cannot do what the cell asks, do not guess and do not edit a check. Write what you read in your report, file a surprise row (id `MDPF_SECCLASS-D1-W106-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) naming what you could not account for, and stop; leave AC1 failing or set `cause_named` false with `not_read`.
- Run every invocation under `timeout 120`; bound each of your own reads by key or version, never sweep a whole bucket.

<paths>
org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~106/S53_CAUSE.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R30.md</decomp_doc> (round 30), cell `SC-e-118`.
<owned_cells>SC-e-118</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC30-e118-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~106/MDPF_SECCLASS.TO-SC-e118.s53-weekday-residue-read.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC30-e118-AC1`.
</proof_of_spec>

**REPORT:** what you found and where (paths, version ids, times), the criterion's output verbatim, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships.
comp-iam: DECLARED-NOT-APPLICABLE only the reads the seat's role already makes.
comp-adversary: RUN -- a step quoted from a file that does not hold it (the check reads the file); class numbers that do not add up to the residue; a weekday pattern asserted from three dates of one weekday (the check wants 3 weekday dates and 2 zero dates, weekday computed from the date); a calendar function that does not exist. NOT CHECKED: the class numbers are not recomputed from S3 by the script; the issuer recomputes one Monday date at the drain.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-29 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_29_20261019.md`, msg 8326); DECOMP_R30; rows MDPF_SECCLASS-D1-S53 and D1-S54.
