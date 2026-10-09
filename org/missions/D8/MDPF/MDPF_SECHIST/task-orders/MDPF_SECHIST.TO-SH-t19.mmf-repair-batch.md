# TO MDPF_SECHIST.TO-SH-t19 -- round 5 SH-t-19: mmf repair batch

<to_id>MDPF_SECHIST.TO-SH-t19</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~18</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-19` (`decompositions/MDPF_SECHIST_DECOMP_R5.md`) | **outcome_ref:** FWD-9, FWD-1 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`SH-t-19` (FWD-9, FWD-1). The round's ONE batched repair cell (round-4 analysis section 3 items 1 and 4; PRD v0.3 C-MMF). Four repairs:
(1) `integrations/bloomberg/pipeline/etf_daily_pull.py:64-69`: drop `TOT_RETURN_INDEX_GROSS_DVDS` from `HISTORY_FIELDS` (back to
`["PX_LAST", "DAY_TO_DAY_TOT_RETURN_GROSS_DVDS"]`) and remove `TOTAL_RETURN_LEVEL_FIELD`; the SH-t-8 gap re-request windows stay.
(2) `data/etfs/scripts/gold/etf_positioning_gold.py` (C-MMF block near :917-1040): the SALXX / FXFXX daily return reads
`DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`; a null day serves BLANK -- never estimated, never computed from a level; remove `TOT_RETURN_LEVEL_COL`
and the level path. Re-point the seam test in `test_etf_positioning_mmf_rule.py` (`test_level_column_matches_the_pulls_total_return_field`)
so it pins gold's money-market field to one of the pull's `HISTORY_FIELDS`. Negative arm, as a test: a money-market fund whose first day is
null reads blank; after the gap re-request adds that day's value, the same day reads filled.
(3) Depth re-plan bound (rows S1 / W1-S1): `history_backfill_plan` (`etf_daily_pull.py:248`) re-plans every run a ticker whose real history
is shorter than a year (2602335D, PFDE, PFOE live), costing a request and a cap slot for zero rows. A ticker whose last backfill returned no
row older than its earliest stored date is NOT planned again; the run records those tickers in its manifest (a field the next run reads) so
the bound persists. Pure-function test with fakes.
(4) Rows S2 / W2-S1: the three gold suites below fail when run from the worktree root (ModuleNotFoundError `etf_classifications_dynamodb`,
tracked under `infra/aws/lambda/v2_portal/_shared/`; and a SystemExit in the industry-group suite). Make each runnable from the worktree
root with no environment set-up (a path insert at the top of the test files is enough); do not copy the module.

### ACCEPTANCE

<criterion id="SH5-t19-AC1" cell_refs="SH-t-19"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py MMFR data/etfs/scripts/gold/test_etf_positioning_mmf_rule.py test_mmf_daily_return_from_day_to_day_field test_null_first_day_reads_blank_then_filled_after_rerequest test_mmf_rule_never_reads_level</invocation><expect>MMFR-TESTS-OK</expect></criterion>
<criterion id="SH5-t19-AC2" cell_refs="SH-t-19"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py PULLR integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py test_history_fields_drop_total_return_level test_depth_plan_skips_exhausted_ticker test_exhausted_list_printed_with_entry_date</invocation><expect>PULLR-TESTS-OK</expect></criterion>
<criterion id="SH5-t19-AC3" cell_refs="SH-t-19"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R5_CHECKS/r5_suites_clean.py GOLD data/etfs/scripts/gold/test_etf_positioning_upgrade_forward.py data/etfs/scripts/gold/test_etf_positioning_per_fund_asof.py data/etfs/scripts/gold/test_etf_positioning_industry_group.py</invocation><expect>GOLD-SUITES-OK</expect></criterion>

<expected_criteria>SH5-t19-AC1, SH5-t19-AC2, SH5-t19-AC3</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~16:4xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the checks under
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/` or `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R5_CHECKS/`.

### AMENDMENT 1 (issuer 2.0.0_SA_COO~H1, 2026-10-09 ~16:5xZ) -- the exhausted list carries entry dates and is printed

Condition 1 of the CTO half on SH-t-8's take (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_SECHIST_SH_T8_SITEZ_TAKE_20261009.md`,
msg 2848): the manifest field `history_backfill_exhausted` becomes a mapping ticker -> the as-of date the ticker ENTERED the list (an entry
carried from the previous manifest keeps its original date; a prior manifest holding the old sorted-list form is read with entry date
unknown, written as null), and every run logs one line per entry, `history backfill exhausted: <ticker> since <date>`, plus a count line
(0 entries prints the count line). Proven by the added named test `test_exhausted_list_printed_with_entry_date` in criterion SH5-t19-AC2
(dry-run at @13b5880f53: BAD on that name only). Same paths; the proof instance is rewritten with the amended AC2 output.

## BOUNDS

- Write only the files in `<paths>`. No S3 write, no Bloomberg call, no run of the pull or the publisher; tests use fakes.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row (dell1 id form `<CODE>-D1-W<n>-S<k>`) and keep working.
- Client-data bounds (0.0.0_AB_MSTR~DELL1, standing): never read, search, copy or `git show` any `org/**/W73_S*_EVIDENCE.json`, commits
  1ba8eafcda / f5645bb6e9, the ADVI_COTBKF ~74 / ~66 / ~70 cottonwood manifests, the IRPT_DASHBD tie-out files, or anything under
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/`. Search only inside the paths named here.

<paths>
integrations/bloomberg/pipeline/etf_daily_pull.py
integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py
data/etfs/scripts/gold/etf_positioning_gold.py
data/etfs/scripts/gold/test_etf_positioning_mmf_rule.py
data/etfs/scripts/gold/test_etf_positioning_upgrade_forward.py
data/etfs/scripts/gold/test_etf_positioning_per_fund_asof.py
data/etfs/scripts/gold/test_etf_positioning_industry_group.py
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~18/MDPF_SECHIST.TO-SH-t19.mmf-repair-batch.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R5.md</decomp_doc> (round 5), cell `SH-t-19`.
<owned_cells>SH-t-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH5-t19-AC1, SH5-t19-AC2, SH5-t19-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~18/MDPF_SECHIST.TO-SH-t19.mmf-repair-batch.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH5-t19-AC1 SH5-t19-AC2 SH5-t19-AC3`
BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE code and tests only; the schedule is unchanged.
comp-iam: DECLARED-NOT-APPLICABLE fakes only; the gold write grant is the deploy pair R1 statement, not this cell.
comp-adversary: RUN -- 7 of 7 round-5 criteria dry-run at the base 2026-10-09 ~16:4xZ, 7 FAIL (decomposition Battery); BLIND: live S3 contents after that read, and the worker's code before it exists.
risk: SERVED.
direct_act: false -- a build cell.
</preflight>

Source: CTO round-4 analysis `ledger/ROUND_ANALYSIS.round4.md` (msg 2828) section 3; PRD v0.3 (CVO sign @cc57bafcdb).
