# TO MDPF_SECHIST.TO-SH-t7 -- round 3 SH-t-7: gold blank over gap and mmf rule

<to_id>MDPF_SECHIST.TO-SH-t7</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~6</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-7` (`decompositions/MDPF_SECHIST_DECOMP_R3.md`) | **outcome_ref:** FWD-5, FWD-9 |
**depends_on:** TO-SH-t6 (the gap record's shape: `record_address(as_of)` and its listed days)

---

## WORKER FACE

### THE CELL

`SH-t-7` (FWD-5, FWD-9). Gold, two rules in `data/etfs/scripts/gold/etf_positioning_gold.py` (`compute_returns`, `:855-921`).
(1) C-GAP: a window that contains a day the gap record lists serves BLANK (None). Today an absent interior day is compounded across;
a present null already blanks (`:913-915`). A security with no listed day is unchanged.
(2) C-MMF (PRD `:96`, analysis item 4): a money-market fund's daily return is computed from its total-return level --
(P + D) / P_prev, MDPF_DEMQUE's measured method -- not from the vendor's daily-return field; a day with neither is blank, never
estimated. SALXX and FXFXX are the money-market funds held today.
Offline tests: `data/etfs/scripts/gold/test_etf_positioning_blank_over_gap.py` (a planted absent interior day reads blank; the same
window with the day filled reads a value) and `data/etfs/scripts/gold/test_etf_positioning_mmf_rule.py`.

### ACCEPTANCE

<criterion id="SH3-t7-AC1" cell_refs="SH-t-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py BLANK data/etfs/scripts/gold/test_etf_positioning_blank_over_gap.py test_window_over_listed_gap_is_blank test_window_reads_after_gap_filled</invocation><expect>BLANK-TESTS-OK</expect></criterion>
<criterion id="SH3-t7-AC2" cell_refs="SH-t-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py MMF data/etfs/scripts/gold/test_etf_positioning_mmf_rule.py test_mmf_daily_return_from_total_return_level test_mmf_day_with_neither_is_blank</invocation><expect>MMF-TESTS-OK</expect></criterion>

<expected_criteria>SH3-t7-AC1, SH3-t7-AC2</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~13:3xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the
check under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/`.

## BOUNDS

- Write only the files in `<paths>`. No S3 write, no Bloomberg call, no run of the pull or the publisher.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row to the project's channel and keep working.

<paths>
data/etfs/scripts/gold/etf_positioning_gold.py
data/etfs/scripts/gold/test_etf_positioning_blank_over_gap.py
data/etfs/scripts/gold/test_etf_positioning_mmf_rule.py
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~6/MDPF_SECHIST.TO-SH-t7.gold-blank-over-gap-and-mmf-rule.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R3.md</decomp_doc> (round 3), cell `SH-t-7`.
<owned_cells>SH-t-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH3-t7-AC1, SH3-t7-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~6/MDPF_SECHIST.TO-SH-t7.gold-blank-over-gap-and-mmf-rule.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH3-t7-AC1 SH3-t7-AC2`
BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE code and tests only; no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE dell1 read grants used in rounds 1-2 (opal-data-etfs, opal-data-portal-v2, etf-classifications read); no new grant.
comp-adversary: RUN -- 9 of 9 round-3 criteria dry-run at the base 2026-10-09 ~13:3xZ, 9 FAIL (decomposition Battery); BLIND: live S3 and DynamoDB contents after that read, and the worker's code before it exists.
risk: SERVED -- graded on the served artifact.
direct_act: false -- a build cell.
</preflight>

Source: CTO round-2 analysis @d0230a0dac section 2 (+ ADDENDUM 1 @678d85e071 for item 6); PRD v0.2 + ADDENDUM v0.3.
