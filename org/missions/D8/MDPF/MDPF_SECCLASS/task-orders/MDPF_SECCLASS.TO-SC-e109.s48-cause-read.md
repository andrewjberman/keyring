# TO MDPF_SECCLASS.TO-SC-e109.s48-cause-read -- round 28 SC-e-109: name the input that moved between the 23:00Z and 04:00Z fires, its writer, and whether the rise is right (a read; nothing is changed)

<to_id>MDPF_SECCLASS.TO-SC-e109</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~99</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-109` (`decompositions/MDPF_SECCLASS_DECOMP_R28.md`) |
**outcome_ref:** FWD-1 (the served firm mix) | **depends_on:** none | **source:** CTO round-27 analysis section 2 (msg 7425, ruling msg 7422); row MDPF_SECCLASS-D1-S48 (ARMED), D1-S49

---

## WORKER FACE

### THE CELL

`SC-e-109`. At 04:00Z on 2026-10-17 the nightly Black Diamond gold fire restated the served firm mix for 2026-10-01 to 2026-10-14 and each date's TOTAL rose by about $381k to $419k. No signed pair named a total move. You find out which INPUT moved, and which script wrote the object that moved, and whether the rise is the intended behaviour. You change nothing.

**What is already measured (do not redo it; start from it):**
- The object that moved: bucket `opal-data-bd`, key `gold/canonical/holdings/<date>.parquet`, 15 dates (2026-09-30 to 2026-10-15). Its writer is `data/black_diamond/scripts/gold/B_00.canonical_holdings.py` (it rewrites a rolling window each fire). Fifteen versions were written at 2026-10-16T23:15:29Z (the 23:00Z fire) and fifteen at 2026-10-17T04:16Z (the 04:00Z fire).
- Date 2026-10-02, key `gold/canonical/holdings/2026-10-02.parquet`: version `wtAhSnBVfcTlrV.Y6Ml3Jh.ggcyBgQkf` (written 2026-10-16T23:15:29Z) and version `aMEdNa9yQApdT4HVnPu3NLMqQ3WB1AV0` (written 2026-10-17T04:16:05Z). `sum(market_value)` goes 2,023,532,725.44 -> 2,023,940,445.76, which is +407,720.32; rows 112,417 -> 112,510. By (account_id, asset_name, source): 335 rows added ($2,935,368.64, 118 of them source `schwab_override`), 242 removed ($2,563,187.46), 153 changed in place (+$35,539.14); 55 accounts touched, 1 of them new. Columns: date, account_id, asset_name, units, price, market_value, source, bd_units, schwab_units, ticker.
- The trigger is the nightly rule, not an event: `data/black_diamond/scripts/gold/gold_dispatch.sh` line 99 runs `B_00|B_00.canonical_holdings.py|--upload --force-recent-days 14` on every fire, so B_00 re-derives the last 14 days each night and absorbs late restatements of its sources. The rise on 2026-10-01..10-14 therefore means a SOURCE B_00 reads changed for those dates between 2026-10-16T23:15:29Z and 2026-10-17T04:16:05Z. The CTO (msg 7426) suspects the Cottonwood carrier chain (a separate tree whose own B_00 also runs `--force-recent-days 14`); the object here is in the Black Diamond bucket `opal-data-bd`, so test that lead with a read (does anything of that chain write an object B_00 of the BD tree reads?) and report it either way.
- One thing to rule out (CTO msg 7429; the CRO's own Cottonwood run, msg 7431, is a different tree and was measured byte-identical for 2026-10-01, 10-02 and 10-14 on its objects): the FWD-10(b) safe-deploy also wrote `cot_bronze_ingest.py` (with a no-regress guard that rejects same-date re-pulls) to `s3://opal-data-bd/code/bronze/` at about 04:0xZ 2026-10-17 and it was rolled back to the prior bytes (sha256 prefix `c8764a43`) at 04:13:33Z. Check whether any Black Diamond (49F) bronze pull ran between 2026-10-16T23:15:29Z and 2026-10-17T04:16:05Z, and whether it landed or rejected anything for 2026-10-01..10-14. Report the answer in `why` either way.
- Not the cause (measured): no object under `opal-data-bd code/gold/` changed after 2026-10-15T18:02Z; `gold/dimensions/schwab_bd_account_mapping.parquet` has had one version since 2026-04-10T20:36:27Z.
- Not yet read: the inputs B_00 reads that DID change. `comp-pipescript io B_00 --pipeline bd-gold` lists them (the Schwab RPS silver prefix `schwab/08335338/silver/fact_rps/` is a `LOCAL-CONST` inside B_00; the bucket is in the same file). A version listing of that prefix on bucket `opal-data-assets` returned no rows at the cut and was NOT trusted without a positive control: find the real bucket in B_00 and run a positive control (a listing that returns a known object) before you accept an empty result.
- The CTO's candidates to test first, not asserted: tonight's FWD-10 Cottonwood switch (2026-10-15 only, a supervised filter) and the Cottonwood carrier re-pull (2026-10-15 only). Both are outside 2026-10-01..2026-10-14 by their own write sets, so a match there would itself be a finding.

**What you do:** (1) Read B_00's source and list every object or prefix it reads. (2) For each, list its object versions and find those written after 2026-10-16T23:15:29Z and at or before 2026-10-17T04:16:05Z (the window between the two rewrites), with a positive control on each listing. (3) Tie the changed input to the +407,720.32 on 2026-10-02 as far as the rows allow (for example the 118 added `schwab_override` rows). (4) Decide RIGHT (the changed input is its producer's normal output and B_00 computes the new rows from it by its own code) or WRONG (it is not: duplicated rows, a stray write, a restated source nobody ordered). Write `S48_CAUSE.json` at the path in `<paths>`.

`S48_CAUSE.json` has exactly these keys (the acceptance script lists them in its header; read `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R28_CHECKS/check_s48_cause.py`, do not edit it):
- `writer`: a file name under `data/black_diamond/scripts/gold/` (for example `B_00.canonical_holdings.py`).
- `moved_key`: `{bucket, key, date, before_version_id, after_version_id}` for ONE date (use 2026-10-02 and the two version ids above).
- `delta_total`: after minus before of `sum(market_value)`, which the checker recomputes (+407720.32 for 2026-10-02).
- `upstream`: a non-empty list of `{bucket, key, version_before, version_after}`, the writer's input objects that changed in the window; `version_before` must be a version written at or before 2026-10-16T23:15:29Z and `version_after` one written after it and at or before 2026-10-17T04:16:05Z (the checker reads both with `head_object`).
- `why`: at least 40 characters, in plain English, how the changed input becomes the +$407,720 and the other dates' rise.
- `verdict`: `RIGHT` or `WRONG`.

### ACCEPTANCE

<criterion id="SC28-e109-AC1" cell_refs="SC-e-109"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R28_CHECKS/check_s48_cause.py read</invocation><expect>S48-CAUSE ok=True</expect></criterion>
`SC28-e109-AC1` -- the file names a writer that exists, the two versions of the moved object bracket the two fires and reconcile to the delta, and at least one changed upstream object is read live and straddles the window.

<expected_criteria>SC28-e109-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-17 ~08:0xZ): AC1 FAILS as expected (`S48-CAUSE ok=False problems=['no file at ...S48_CAUSE.json']`). The script's own `selftest` runs a green arm and six negative arms (empty upstream, a delta that does not reconcile, an upstream that does not straddle the window, a writer that is not a gold script, a verdict of UNDETERMINED, a missing `why`) and prints `S48-CAUSE-SELFTEST ok=True`; its live readers were checked against the known 2026-10-02 numbers (+407720.32).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted (downloaded parquet files go there).
- **AWS READS ONLY** (`s3api list-object-versions`, `head-object`, `get-object` with a `VersionId`, through `.tools/aws` or boto3). No write, delete, copy, put, tag, invoke, start, stop or deploy of any kind. Nothing is changed; if a finding says something should be rolled back, you write that in `why` and stop.
- **No package install and no download** into the repo. pandas, pyarrow and boto3 are installed.
- **Never edit** anything outside the `<paths>` block; the scripts under `R28_CHECKS/` are READ-ONLY to you. Never push.
- **Refusal clause.** If you cannot name the upstream input that changed, do not guess and do not edit a check. Write what you read (with each listing's positive control) in your report, file a surprise row (id `MDPF_SECCLASS-D1-W99-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) naming the objects you could not account for, and stop; leave AC1 failing.
- Run every invocation under `timeout 120`; the check reads two parquet versions and ends well inside it. Your own reads of large objects may take longer: bound each by key, never sweep a whole bucket.

<paths>
org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~99/S48_CAUSE.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R28.md</decomp_doc> (round 28), cell `SC-e-109`.
<owned_cells>SC-e-109</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC28-e109-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~99/MDPF_SECCLASS.TO-SC-e109.s48-cause-read.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC28-e109-AC1`.
</proof_of_spec>

**REPORT:** the writer, the upstream object(s) with their before and after version ids and times, how they tie to the +407,720.32, the verdict and its reason, the criterion's output verbatim, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships.
comp-iam: DECLARED-NOT-APPLICABLE only the reads the seat's role already makes.
comp-adversary: RUN -- a file that names a writer and an upstream key it did not read (the check reads both versions live and compares their times to the window); a delta typed rather than recomputed (the check recomputes it); an upstream list with a key that did not change (the straddle test); a verdict with no reason (the 40-character floor).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-27 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_27_20261017.md`, msg 7425); DECOMP_R28.
