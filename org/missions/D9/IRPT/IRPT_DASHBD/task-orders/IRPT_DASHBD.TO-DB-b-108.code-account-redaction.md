# TO IRPT_DASHBD.TO-DB-b-108 -- E1: the 14 IRPT_DASHBD code files carrying real 49F client account numbers are repaired -- every literal replaced by its acct#<sha8> token, and any code needing the real id reads it at run time from IRPT_PRIVATE_EVIDENCE_DIR (outside the repo), never a typed id

<to_id>IRPT_DASHBD.TO-DB-b-108</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~83</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>54</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's containment ruling @0e8209c33c (msgs 3643, 3696 AMENDMENT 2), enrichment item E1 | **Decomp cell:** `DB-b-108` (decomposition section 56) | **outcome_ref:** FWD-8 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-83`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~83/`.

**The cell (`DB-b-108`).** The CTO's containment ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_CLIENT_ACCOUNT_DATA_IN_REPO_CONTAINMENT_20261009.md`,
@0e8209c33c, AMENDMENT 2) says client account numbers do not live in tracked files. Evidence was moved out; documents were redacted to tokens; code is
ONE cell per project. These 14 files under `C:/dev/wk-irpt-dashbd-83/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/` carry the numbers:
- `0.9.0_WK_IRPT_DASHBD~1/bd_likeday_pull_r4.py`
- `0.9.0_WK_IRPT_DASHBD~1/decompose_three_pairs_r6.py`
- `0.9.0_WK_IRPT_DASHBD~1/remeasure_three_pairs_r6.py`
- `0.9.0_WK_IRPT_DASHBD~2/build_tieout_r8.py`
- `0.9.0_WK_IRPT_DASHBD~2/remeasure_fourteen_pairs_r8.py`
- `0.9.0_WK_IRPT_DASHBD~21/gap_diagnosis_e1.py`
- `2.0.0_SA_COO~P/checks/r1/p1_1_ac1_gold_under_contract.py`
- `2.0.0_SA_COO~P/checks/r1/p1_2_ac1_series_manifest.py`
- `2.0.0_SA_COO~P/checks/r1/p1_4_ac1_read_route_local.py`
- `2.0.0_SA_COO~P/checks/r2/p2_6_ac1_flow_residual_record.py`
- `2.0.0_SA_COO~P/checks/r4/p4_1_ac1_one_pull_in_scope.py`
- `2.0.0_SA_COO~P/checks/r6/p6_1_ac2_three_pairs_dispositioned.py`
- `2.0.0_SA_COO~P/checks/r8/p8_1_ac2_fourteen_pairs_population_guard.py`
- `2.0.0_SA_COO~P/p2_window/p2_backfill_driver.py`

**THE CLIENT-DATA RULE (binding on this cell):** evidence carrying account numbers or client figures is written OUTSIDE the repo. The repo carries
counts, sha256 and reason codes only. Never print an account number in a commit message, a record or a row.

1. In each file, replace every literal 49F account number with its token: `acct#` + the first 8 hex of `sha256("49financial:<account>")`.
   - Where the code must use the real id at run time (an S3 key, a filter), read it from a JSON map
     `<IRPT_PRIVATE_EVIDENCE_DIR>/account_map_49financial.json` (`{token: account}`). The environment variable names the directory: no typed
     id, no device path (CLAUDE.md: derive, do not hardcode).
   - If the variable or the file is absent, the code refuses by name. These are historical round scripts; they need not run here.
2. Every file must still `py_compile`, and pass `.tools/commit-gate.sh`.
3. Record `CODE_REDACTION.json` {files: [the 14 repo paths], tokens_replaced, runtime_lookups (count of call sites that now read the map)}. It holds NO
   account number.

**Lane:** these files sit in other serials' folders. Commit with `GIT_COMMIT_AUTHOR_OVERRIDE=TREE_DELIVERABLES` (audited), citing @0e8209c33c in the
message, exactly as the CTO and the issuer did for the removals. Edit only these 14 files and your own folder.

<criterion id="DB54-1-AC1" cell_refs="DB-b-108"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r54/p54_round54.py" . DB54-1-AC1</invocation><expect>DB54-1-AC1 PASS</expect></criterion>
`DB54-1-AC1` -- the 14 code files carry no account number, compile, and the record names exactly them. Base: FAIL.

<expected_criteria>DB54-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit the 14 named files in other serials' folders under the audited TREE_DELIVERABLES override, on the containment ruling. No AWS call.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~83/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/bd_likeday_pull_r4.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/decompose_three_pairs_r6.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/remeasure_three_pairs_r6.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2/build_tieout_r8.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2/remeasure_fourteen_pairs_r8.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/gap_diagnosis_e1.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_1_ac1_gold_under_contract.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_2_ac1_series_manifest.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_4_ac1_read_route_local.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r2/p2_6_ac1_flow_residual_record.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r4/p4_1_ac1_one_pull_in_scope.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r6/p6_1_ac2_three_pairs_dispositioned.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r8/p8_1_ac2_fourteen_pairs_population_guard.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/p2_window/p2_backfill_driver.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~83/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-108.code-account-redaction.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 56 (round 54), cell `DB-b-108`.
<owned_cells>DB-b-108</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB54-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~83/IRPT_DASHBD.TO-DB-b-108.code-account-redaction.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB54-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the tokens replaced, the run-time lookups, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: historical round scripts and checks; no served code; nothing deploys.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB54-1-AC1 FAIL at base (no record; the files carry account numbers). Containment ruling @0e8209c33c.
lane: the <paths> block IS the grant.
</preflight>
