# TO MDPF_SECCLASS.TO-SC-e114.s48-range-reconcile-read -- round 29 SC-e-114: reconcile the S48 14-date ranges, served against the canonical-holdings input, per date (a read)

<to_id>MDPF_SECCLASS.TO-SC-e114</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~103</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-18</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-114` (`decompositions/MDPF_SECCLASS_DECOMP_R29.md`) |
**outcome_ref:** FWD-1 (the served firm mix) | **depends_on:** none | **source:** CTO round-28 analysis section 3 item 6 (msg 7829); CTO msg 7442

---

## WORKER FACE

### THE CELL

`SC-e-114`. The 04:00Z restatement of 2026-10-17 raised the served firm TOTAL for 2026-10-01 to 2026-10-14. Two measures of the rise exist and have never been put side by side per date: the CVO's on the served object (about +381k to +419k), and the worker `~99`'s on the canonical-holdings input (+382,473 to +450,743). You compute both for each of the 14 dates and their residue (served minus canonical). You change nothing, and you explain nothing you cannot read: a non-zero residue is reported as a number, and the cell is satisfied by a correct table plus a `summary`, not by a zero.

**The two measures, pinned to versions (so a later fire cannot move them):**
- **Served:** bucket `opal-data-49financial`, key `advi/49financial/platinum/views/mix_daily_summary.json`; `pre_version_id` `87CvfcFpbyM7ZRAb0P6AztqK1X74W6cQ` (2026-10-17T00:22:27Z), `post_version_id` `l2Wqoi6iUJwQwwmTCu3lXWozfW4.Ak_.` (2026-10-17T05:24:08Z). For a date `d`, the served delta is `post.firm[d].total - pre.firm[d].total`. (Known: for 2026-10-02 it is +407,720.32.)
- **Canonical:** bucket `opal-data-bd`, one object per date, `sum(market_value)` of the version written 2026-10-16T23:15Z (before) and the version written 2026-10-17T04:16Z (after):

| date | key `gold/canonical/holdings/<date>.parquet` before_version_id | after_version_id |
|---|---|---|
| 2026-10-01 | `gK6wE3FNua_E2yZfPOUsBVLTGWe5UCkw` | `QQXsJBKzu44JaRVdabbU7D4sXxGfDJEO` |
| 2026-10-02 | `wtAhSnBVfcTlrV.Y6Ml3Jh.ggcyBgQkf` | `aMEdNa9yQApdT4HVnPu3NLMqQ3WB1AV0` |
| 2026-10-03 | `2ul.EMCChf744o_3Yqth9PHLHEFtN13m` | `nM1S0ZnWmxCsWwvNGyHyXhISMRFgJZiA` |
| 2026-10-04 | `6cqBjVGgzk6NEDmoe0AjbEK1aw4BIZoD` | `vVPXZjcpmCs2pmrK8wrLUgs84c5o_JcB` |
| 2026-10-05 | `6cZGJKLgszB25HS87bGTpmqnYSPL91U0` | `MPkQQMxbD1hHT_qMhRxfhO.y59.1y5q3` |
| 2026-10-06 | `X1JNjNynuzFLRB91MErRPUfy9M2bpmrO` | `81a9N4jBUShVFQsgy.nWB5.sJkECsrLC` |
| 2026-10-07 | `sgAy8VVVuyIDyTv7wDpBFn.pk5Fpk3YM` | `_7eexKPV8AdyezyKVS24JQCHr7cxW1HA` |
| 2026-10-08 | `KkC1BdGWoyB3DRDOq2tXKxbNlGmbVoML` | `pMHzxQin1MyoGgy6aAoDklexI.NN5EiL` |
| 2026-10-09 | `1n7BcIHi6kF5oTl2x3L_0FJTnPtqIH2Z` | `6ifYA5sO0sFgmBP1TnaGleGvrn3th8zW` |
| 2026-10-10 | `q.6aWD43IViX935xhWvW9yk_2kv8v8Le` | `tzYOEeMkW95XnYwfs0J_a3NU5Hxkjx02` |
| 2026-10-11 | `2UvhThWL4BFonU__JLIy_yuBdsHaPqIl` | `rY_z584ryb33R845uoZ0zf9NK1cNsJ.L` |
| 2026-10-12 | `OiJptpAgjssTZp4YByiBE5N3Apc0NZiB` | `RkleuntTHLvtwWEhbpE2_COFD_0wL1XG` |
| 2026-10-13 | `LIAkXkK8Xbcn4WtuNyMX7FHq9D4piAx3` | `i4EgmgFe8AtbxHQYsLwNYNiUksUrcNz9` |
| 2026-10-14 | `lKA0CR43plBVgDAH7nYNFP1UKBI3.x_v` | `SVGAmTUoMW9ivopsINhed89h3oNCqnkE` |

(every key is `gold/canonical/holdings/<date>.parquet` in bucket `opal-data-bd`; for 2026-10-02 the delta is +407,720.32.)

**What you do:** (1) For the 14 dates compute the served delta, the canonical delta and the residue. (2) Look at the pattern in the residue (by date, by sign, against the count of added or removed rows if that helps) and say in the `summary` what it is or that you cannot tell. (3) If a residue is not near zero on some date, say whether it is the same size on every date; do not name a cause you did not read. (4) Write `S48_RANGE_RECON.json` at the path in `<paths>`.

`S48_RANGE_RECON.json` has exactly these keys (the script lists them in its header; read `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R29_CHECKS/check_r29_reads.py`, do not edit it):
- `served`: `{"bucket": "opal-data-49financial", "key": "advi/49financial/platinum/views/mix_daily_summary.json", "pre_version_id": ..., "post_version_id": ...}` as above.
- `canonical`: `{"bucket": "opal-data-bd", "dates": {"2026-10-01": {"key": ..., "before_version_id": ..., "after_version_id": ...}, ...}}` for the 14 dates.
- `rows`: 14 objects `{"date", "served_delta", "canonical_delta", "residue"}`; the checker recomputes all three within 0.01.
- `summary`: at least 40 characters.

### ACCEPTANCE

<criterion id="SC29-e114-AC1" cell_refs="SC-e-114"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R29_CHECKS/check_r29_reads.py s48-range</invocation><expect>R29-s48-range ok=True</expect></criterion>
`SC29-e114-AC1` -- all 14 dates have a row, and each served delta, canonical delta and residue equals the checker's recomputation from the pinned versions.

<expected_criteria>SC29-e114-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-18 ~02:0xZ): AC1 FAILS as expected (`R29-s48-range ok=False problems=['no file at ...S48_RANGE_RECON.json']`). The script's `selftest` runs a green arm and negative arms for every mode and prints `R29-SELFTEST ok=True`; its live readers were checked against known numbers (the served 2026-10-02 delta +407,720.32; the live CodeSha256 of opal-partners-data).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **AWS READS ONLY** (S3 `list-object-versions`, `head-object`, `get-object`, `list-objects-v2`; CloudWatch Logs `filter-log-events`, `describe-log-groups`, `describe-log-streams`; Lambda `get-function`, `get-function-configuration`; SSM `get-command-invocation`, `list-command-invocations`; through `.tools/aws` or boto3). No write, delete, copy, put, tag, invoke, start, stop or deploy of any kind. Nothing is changed.
- **No package install and no download** into the repo. pandas, pyarrow and boto3 are installed.
- **Never edit** anything outside the `<paths>` block; the script under `R29_CHECKS/` is READ-ONLY to you. Never push.
- **Append to the surprise channel in BYTE MODE** (`open(path, 'ab')`), one new row only if you file one: never read and rewrite that file (it mixes CRLF and LF blocks and a round trip changes the old bytes).
- **Refusal clause.** If you cannot do what the cell asks, do not guess and do not edit a check. Write what you read (with each listing's positive control) in your report, file a surprise row (id `MDPF_SECCLASS-D1-W103-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) naming what you could not account for, and stop; leave AC1 failing.
- Run every invocation under `timeout 120`; bound each of your own reads by key or prefix, never sweep a whole bucket.

<paths>
org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~103/S48_RANGE_RECON.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R29.md</decomp_doc> (round 29), cell `SC-e-114`.
<owned_cells>SC-e-114</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC29-e114-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~103/MDPF_SECCLASS.TO-SC-e114.s48-range-reconcile-read.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC29-e114-AC1`.
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
