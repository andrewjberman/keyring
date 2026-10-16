# TO ADVI_COTBKF.TO-CB-cy-2.disjoint-month-categories -- round 103 CB-cy-2: the UNGRADABLE months of the served month_grades as disjoint categories, the overlap of the clauses, and the exact upper bound of months a fill of every UNPRICED day could grade; read-only, counts only

<to_id>ADVI_COTBKF.TO-CB-cy-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~193</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>103</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cy-2` (`decompositions/ADVI_COTBKF_DECOMP.round103.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Round 102's census listed the 78,622 UNGRADABLE months of the served `month_grades` by several clause kinds that overlap: a month's reason text can join a blank-day clause and a reported-side clause, so the category counts summed to 82,470 over 78,622 months. The CTO asks for disjoint categories, so that the bound on how many months a vendor price history could make gradable is exact and not a range. You partition the months, show the overlap, and state the bound. **Read-only: you write nothing to S3, serve nothing, change no code, fill nothing and grade nothing.**

**Inputs (READ-ONLY).** The served objects at the pinned VersionIds, one `get_object` each: `daily_returns` at `lNzQMjfx6uX2zdFdWKsDANboShtDUz2N` and `month_grades` at `nkTE.F82uFSboXr9PEamIENCwFL9cwcC` (`s3://opal-data-assets/commonwealth/cottonwood/silver/<table>/date=2026-06-23/part-00000.parquet`).

**Read first.** (1) The issuer's script `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cy2_month_partition.py` (in your worktree; read it, do not edit it): its docstring states the six disjoint categories, the order they are assigned in and the clause texts; it prints the partition your record must equal. (2) Row `ADVI_COTBKF-D1-S18` in `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md` (the overlap, as the issuer stated it), and the round-102 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~191/BLANK_CENSUS_RECORD.json` (its `months` and `drivers`). (3) `data/assets/scripts/silver/commonwealth_monthly_grade.py` for the reason texts.

**Your items.**

1. **Run the issuer's script** with no argument: `python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cy2_month_partition.py` (about 7 seconds). Its `MONTH-PARTITION` line is the partition: `no_daily`, `blank_only_unpriced`, `blank_only_other`, `blank_and_reported`, `reported_only`, `other`, which sum to the UNGRADABLE months (`sum_equals=True`) with `text_blank_mismatch=0`.
2. **Reproduce it yourself** from the two served objects with your own read (a small script of yours, committed in your deliverables folder as evidence), using the definitions in the issuer script's docstring, and confirm the six counts. A difference between yours and the issuer's is a finding to report, not to adjust.
3. **The overlap matrix.** For the UNGRADABLE months, the cross-tabulation of three flags: has at least one blank day (from `daily_returns`, a null `return`); has a reported-side clause (the reason texts `no reported monthly return`, `reported span`, `reported rows disagree`, `not finite`); has no `daily_returns` row at all. Eight cells (some will be 0), counts only, summing to the UNGRADABLE months. Also, within the blank-day months: the months by the set of blank reasons they hold, grouped as: only UNPRICED; UNPRICED with at least one other reason; only other reasons (counts).
4. **The exact bound.** `fill_upper_bound` = the months of the category `blank_only_unpriced`: the most months that could grade if every UNPRICED blank day received a price and nothing else changed, because every other category keeps a blocking reason. State what the bound is not: not a promise that any of those months would match, and not conditional on whether a vendor covers the securities (round 103's other cell measures that).
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~193/MONTH_PARTITION_RECORD.json` with exactly these top-level keys: `measured`, `reason` (when not measured), `served` (`{"daily_returns_version","month_grades_version"}`), `ungradable`, `partition` (`{"no_daily","blank_only_unpriced","blank_only_other","blank_and_reported","reported_only","other"}`), `overlap_matrix` (eight objects `{"has_blank_day","has_reported_clause","has_no_daily","months"}`), `blank_reason_sets` (`{"only_unpriced","unpriced_and_other","only_other"}` as counts of the months with a blank day), `fill_upper_bound`, `earlier_range` (`{"low":70943,"high":74791,"note":"row D1-S18 estimate"}`), `what_this_shows` (two sentences in counts), `not_established`; and a short `.md` beside it. The keys `ungradable`, `partition` and `fill_upper_bound` must equal the issuer's script. No account id, name or dollar value in either file.

### ACCEPTANCE

<criterion id="CB103cy2-AC1" cell_refs="CB-cy-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~193/MONTH_PARTITION_RECORD.json',encoding='utf-8'));m=d['measured'];p=d.get('partition') or {};print('MONTH-PARTITION-RECORD measured=%s' % m + ((' ungradable=%d categories=%d sum=%d bound=%d' % (d['ungradable'],len(p),sum(p.values()),d['fill_upper_bound'])) if m else ' reason=%s' % d['reason']))"</invocation><expect>^MONTH-PARTITION-RECORD measured=(True ungradable=\d+ categories=6 sum=\d+ bound=\d+|False reason=.+)$</expect></criterion>
`CB103cy2-AC1` -- the record states the UNGRADABLE months, the six disjoint categories with their sum, and the exact bound, or states plainly why nothing could be measured.

<criterion id="CB103cy2-AC2" cell_refs="CB-cy-2"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cy2_month_partition.py org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~193/MONTH_PARTITION_RECORD.json</invocation><expect>^MONTH-CROSS partition_equal=True fill_bound_equal=True$</expect></criterion>
`CB103cy2-AC2` -- the issuer's script recomputes the partition from the served objects and the record equals it, category by category, and its bound equals the `blank_only_unpriced` category.

<criterion id="CB103cy2-AC3" cell_refs="CB-cy-2"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cu1_ac3_served_unchanged_check.py</invocation><expect>^SERVED-UNCHANGED versions_equal=3 of 3$</expect></criterion>
`CB103cy2-AC3` -- the cell wrote nothing: the three served keys still carry the VersionIds the round-98 apply left.

<expected_criteria>CB103cy2-AC1,CB103cy2-AC2,CB103cy2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your deliverables folder, your own NEW channel row, and this order's own file (for the one `<status>` flip). You change no code, test or other committed file. Scratch, if any, stays under `C:/Dev/ajb_workspace/.scratch/cotbkf_r103b/` (gitignored, never committed). Your instance rows for artifacts that already exist in a commit are pinned to that commit's FULL hash (never `PENDING-THIS-COMMIT` for a file an earlier commit carried).
- **AWS: READ-ONLY** (`get_object` of the two served objects at the pinned VersionIds, `head_object` for AC3); no write, no vendor call, no Bloomberg, no Yahoo. You do not contact Cottonwood or Commonwealth.
- **No account id, name or dollar value** in the record, the report or any message.
- **NEVER** serve, apply, overwrite, push, override a gate or `--force`; never edit any module; never fill, estimate or repair a blank or a month; never grade FWD-3 yourself.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W193-S<k>` (`date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'ab')` writing LF bytes only (the file holds CRLF lines from earlier rows: never read and rewrite it); `git diff --numstat` must show added lines only. A difference between your counts and the issuer's script is a finding to report, not to adjust: AC2 then reads False and you stop.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-cy-2.disjoint-month-categories.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row; the one write to this order is the `<status>` flip.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round103.md</decomp_doc> (round 103), cell `CB-cy-2`.
<owned_cells>CB-cy-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB103cy2-AC1, CB103cy2-AC2, CB103cy2-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~193/ADVI_COTBKF.TO-CB-cy-2.disjoint-month-categories.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB103cy2-AC1,CB103cy2-AC2,CB103cy2-AC3` BEFORE the flip. The `output_evidence` of each criterion must equal its `expect` pattern exactly (no suffix); put any note in `denominator`. All three criteria are mechanical. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when all three PASS** (the order file is in your `<paths>` for this flip).
</proof_of_spec>

**REPORT:** FIRST the `MONTH-PARTITION-RECORD` line. Then: the six categories and their sum; the overlap matrix; the blank-reason sets; the bound and what it is not; whether your own reproduction equals the issuer's script; any step you could not run and why; the three criterion lines; commits; every gate refusal and hook denial, verbatim. No account id or value.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of two served objects and a count; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE get_object of two objects at pinned versions under the existing role; no new permission.
comp-adversary: RUN -- the partition is recomputed by an issuer script from the same served objects and the record must equal it (AC2); BLIND: both read the same objects, so a defect in the served tables is not tested; the category definitions, in particular what counts as a reported-side clause (four reason-text fragments), are the issuer's and read from the module's reason texts, so a clause text the module does not emit today is not covered (the script's `other` category would show it as non-zero).
lane: the <paths> block IS the grant (worker RULING 1), and names the order file for the status flip.
</preflight>

**ISSUER NOTES:** Source: `1.0.0_SA_CTO~DELL1` msg 6633 (item 2, row D1-S18). Issuer's pre-count: ungradable 78,622 = no_daily 116 + blank_only_unpriced 72,184 + blank_only_other 1,563 + blank_and_reported 3,818 + reported_only 941 + other 0; `text_blank_mismatch=0`. Mechanical checks dry-run at the base (the record file is absent): AC1 and AC2 FAIL as expected; AC3 PASSES (served versions unchanged).
