# TO MDPF_SECCLASS.TO-SC-e41 -- round 9 SC-e-41: FWD-5 -- the widened reader census of the old list (the Black Diamond tree, run-time names, role grants)

<to_id>MDPF_SECCLASS.TO-SC-e41</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~31</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-41` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none. Slot ~31's first order; `TO-SC-e45` follows on the same slot.

---

## WORKER FACE

### THE CELL

`SC-e-41`: the widened reader census (row W25-S5). Round 8's trace (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_READER_TRACE_20261007.md`,
TO-SC-e38) covered 46 files OUTSIDE the Black Diamond tree and found 5 NEEDS-OLD-LIST readers with canonical producer NONE. This cell
covers what it excluded. A READ-ONLY trace: no code edit.

- FWD-5 (PRD v0.13): the old Black Diamond copy of the list (`bd-securities`, DynamoDB us-east-1) is gone, and it can be shown that
  nothing needed it. The round-8 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md`,
  section 2.10): no old-list writer stop uploads until every real reader resolves canonical-first and names a canonical producer
  with a live write count above 0; W25-S5 widens the census to `data/black_diamond` and to run-time-assembled names FIRST.
- **The census (measured at the round-9 base):** `git grep -l -E "bd-securities|BD_SECURITIES_TABLE" -- data/black_diamond/` minus
  test files = 13 files: `classification/{backfill_name_aliases,classify_bd_securities,resolve_tickers,seed_bd_securities,seed_canonical_securities}.py`,
  `gold/{B_01.holdings_lots,B_01b.classify_new_securities,E_18.detect_new_securities,build_canonical_prices_v2}.py`, `gold/gold_dispatch.sh`,
  `gold/lib/{etf_classifier,s3_layout}.py`, `silver/build_bd_assets_dim.py`.
- **Run-time names:** the IRPT fallback (`data/assets/scripts/gold/investor_reporting/bd_securities_fallback.py`) assembles its table
  name at run time, so a literal census cannot find every such reader. Find every builder of the name (`'%s-securities'` and the naming
  registry's resolution) and trace who calls it.
- **Role grants:** a role that reaches the table without code naming it (e.g. `opal-news-lambda-role` holds AmazonDynamoDBFullAccess,
  row from TO-SC-e38). Read IAM read-only (`iam list-attached-role-policies`, `get-role-policy`); name each role that can read the table
  and the function(s) that assume it.

**Build:** a census script `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/old_list_reader_census_bd.py` (read-only,
prints its denominator) and the trace `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_READER_TRACE_BD_20261007.md`:
- a `DENOMINATOR:` line (files and call sites swept, roles read);
- one `## READER: <repo path> ...` section per census file (the heading carries the path), one section whose heading names `runtime`
  (the run-time-name readers) and one whose heading names `role` (the role grants);
- in every section exactly one `READS:`, one `EVIDENCE: <path>:<line>` (a path that exists at HEAD) and one `VERDICT:` from
  NEEDS-OLD-LIST | REPOINTABLE | DEAD-READ | NOT-A-READER (a writer is NOT-A-READER for this census and says it writes);
- for every real reader (any other verdict) exactly one `MISSING-ROW:` (its own rule for a ticker with no `bd-securities` row, path:line,
  read from the code), one `SERVED-NEW:` (what its served output shows for a security first held after the writers stop: classified
  from the canonical table / unclassified / dropped / an error -- read from that rule, never predicted) and one `CANONICAL-PRODUCER:`
  (the producer that gives such a security an `etf-classifications` row before this reader runs, with its live write count from a
  read-only scan of `updated_by`, or NONE).

### ACCEPTANCE

<criterion id="SC9-e41-AC1" cell_refs="SC-e-41"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/issuer_check_sc_e41.py</invocation><expect>SC-E41-TRACE ok=True</expect></criterion>
`SC9-e41-AC1` -- the trace covers the run-time census of the Black Diamond tree (every file a section), the run-time names and the role grants, each section well formed and each real reader with its missing-row rule, served result and producer.

<expected_criteria>SC9-e41-AC1</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`no OLD_LIST_READER_TRACE_BD_*.md`). Issuer controls: a synthetic full trace read
`ok=True sections=15 census=13`; the same with one census file's section removed read `ok=False uncovered=1`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
  `R11_CHECKS/issuer_check_sc_e41.py` is READ-ONLY to you.
- **Read-only.** No code edit, no table or S3 write, no deploy, no invocation of a live function, no IAM change. Reading configuration is
  allowed. No vendor or model call.
- **NO package install and NO download of any kind** -- no pip, npm, curl or tool fetch, into any environment (row S49).
- dell1's principal is denied the three firm buckets (row W25-S1); read code, DynamoDB and IAM, not firm-bucket objects.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W31-S<k>`), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/old_list_reader_census_bd.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_READER_TRACE_BD_*.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-41`.
<owned_cells>SC-e-41</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e41-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~31/MDPF_SECCLASS.TO-SC-e41.widened-reader-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e41-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the denominator, the reader list with verdicts, every reader that NEEDS the old list that round 8's trace did not name (each
is a new switch cell for the issuer), the role grants found, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only trace arms no schedule.
comp-iam: RUN -- the cell's own role-grant read is the IAM read; R8's trace named opal-news-lambda-role (AmazonDynamoDBFullAccess) as a role-level reach.
comp-adversary: RUN -- the census is computed by the issuer's check at run time (13 files at the base), so a skipped file fails; run-time-assembled names and role grants are the two blind spots R8 named (W25-S5), each given its own section. BLIND: a caller outside the repo (an SSM document or instance cron) unless the worker's IAM read surfaces its role.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.13 @90f99888cd (FWD-5); CTO round-8 analysis @1ca9e97fc9 sections 2.10 and 4 item 1; DECOMP_R9 @5d70aab6c9.
