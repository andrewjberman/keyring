# TO ADVI_COTBKF.TO-CB-m-2 -- round 13 CB-m-2: the crosswalk and the account links re-run on the one signing table, diffed against the applied tables

<to_id>ADVI_COTBKF.TO-CB-m-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~29</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-m-2` (`decompositions/ADVI_COTBKF_DECOMP.round13.md`) |
**outcome_ref:** FWD-8, FWD-9 | **depends_on:** CB-m-1 (the one signing table)

---

## WORKER FACE

### THE CELL

`CB-m-2`, FWD-8 and FWD-9: two tables Opal has already APPLIED were built on the old, divergent signing rules -- the `crosswalk` (1,533
rows; MATCHED 439, NOT_MATCHED 1,094; 21 near-matches) and the `account_links` (1,450 rows; 212 LINKED). CB-m-1 (your previous order, in
this same worktree) replaced both rules with ONE table, `data/assets/scripts/silver/commonwealth_signs.py`. Measure what that changes.

Build `data/assets/scripts/analysis/commonwealth_rule_change_diff.py`, read-only, which:
1. reads the two APPLIED tables from S3 (`opal_naming.address("commonwealth", <cottonwood scope via opal_naming.lookup>, "silver",
   "crosswalk" | "account_links", "date=2026-06-23")`, the `.parquet` objects);
2. re-runs both scripts locally on the one table (`commonwealth_crosswalk.py --out <scratch>` and `commonwealth_account_links.py --out
   <scratch>`, the same inputs, no `--apply`);
3. compares row by row: crosswalk by `commonwealth_account` (status, rule, current_account, score), account links by `old_account`
   (status, new_account), and prints the class counts before and after;
4. writes `RULE_CHANGE_DIFF.md` and `rule_change_rows.csv` (every changed row: table, account, field, before, after, reason) to `--out`,
   and prints as its LAST line exactly:
   `RULE-CHANGE-DIFF crosswalk_rows=1533 crosswalk_changed=<c> crosswalk_matched_before=439 crosswalk_matched_after=<m> account_links_rows=1450 account_links_changed=<l> account_links_linked_before=212 account_links_linked_after=<k>`.

**Nothing is applied.** If either table changes, the issuer carries it to a re-apply under its own never-widen halves; DELTA=0 needs none.

**Tests** `data/assets/scripts/analysis/tests/test_commonwealth_rule_change_diff.py` (stubs, no AWS): two identical stub tables print
`crosswalk_changed=0`; one changed status prints `crosswalk_changed=1` and writes that row (the control).

### ACCEPTANCE

<criterion id="CB13m2-AC1" cell_refs="CB-m-2"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_rule_change_diff.py</invocation><expect>passed</expect></criterion>
`CB13m2-AC1` -- the diff on stubs, with the one-change control.

<criterion id="CB13m2-AC2" cell_refs="CB-m-2"><invocation>python data/assets/scripts/analysis/commonwealth_rule_change_diff.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~29</invocation><expect>RULE-CHANGE-DIFF crosswalk_rows=1533</expect></criterion>
`CB13m2-AC2` -- the real tables; the changed counts and after-counts on the same line are recorded, not presumed.

<expected_criteria>CB13m2-AC1,CB13m2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **Read-only.** No `--apply`, no S3 write, no vendor call, no download, never bun.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W29-S<k>`, `"fabric": "dell2"`), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_rule_change_diff.py
data/assets/scripts/analysis/tests/test_commonwealth_rule_change_diff.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round13.md</decomp_doc> (round 13), cell `CB-m-2`.
<owned_cells>CB-m-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB13m2-AC1, CB13m2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~29/ADVI_COTBKF.TO-CB-m-2.rule-change-diff.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB13m2-AC1,CB13m2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the RULE-CHANGE-DIFF line, the changed rows summarized by reason, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity on opal-data-assets; denominator 1 bucket; BLIND: none needed.
comp-adversary: RUN -- the applied tables, never local copies, are the before; both tables the old rules built are diffed, not only the one the analysis named; nothing applied; BLIND: none.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-12 analysis @9a9384d247, E2, widened by the issuer to the account links (decomposition round 13).
