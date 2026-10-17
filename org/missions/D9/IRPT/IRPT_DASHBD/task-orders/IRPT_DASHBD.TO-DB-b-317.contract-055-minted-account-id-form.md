# TO IRPT_DASHBD.TO-DB-b-317 -- CONTRACT 0.5.5 for the minted account id, in ONE drain with the reader and the validator that produce and check it: `account_id` is the minted opaque id, a new field `account_id_form` = `minted` on every account entry, the accounts ascending by the minted id (CTO ruling, packet-5 analysis @ee3383bf1e, ruling 2) (round 149)

<to_id>IRPT_DASHBD.TO-DB-b-317</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~252</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>CONTRACT055</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** CONTRACT055, round 150 enrichment list item 1 | **Ordered by:** the CTO's round analysis for packet 5, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_149_PACKET_5_20261017.md` @`ee3383bf1e` (ruling 2: minting is the policy; the contract catches up in ONE drain with the producer; the portal mirror follows in the same round, AFTER Andrew's smoke) and the CVO's adjudication v148/v149 (finding b: the minted ids contradicted contract 0.5.4:157 and the :126 order rule) | **Decomp cell:** `DB-b-317` (decomposition section 177).

**Risk class WORLD** is the floor of the path (`infra/`): the contract file, one handler block, one publisher block and tests in a branch. No Terraform command, no AWS call, no push. Nothing is deployed by this cell: the deploy of the reader and validator is a later signed pair, and the portal mirror waits for Andrew's smoke of the Performance tab branch.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-252` (branch `wk-IRPT_DASHBD-252`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~252/`. Never push; never commit the workspace `portal` gitlink. Counts, dates, hashes and words only in the repo, a row, a commit message or your report; use synthetic ids in tests. **Before every commit, scan what you stage for a client figure and for long identifier runs; the commit gate's client-data list is absent on this box, so that scan is yours.** **Commit order: the artifact first, then the proof instance, then the status flip to complete as the LAST commit.** Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them.

**What is wrong.** The reader (`DB-b-310`) mints the composed ids, but contract 0.5.4 still says `account_id` is the account_activity_daily custodian form (line 157), the accounts are "in account_id order" (line 126, and the custodian order is not the minted order), and no field says which form an id is. The CTO ruled: contract 0.5.5 makes the minted id the contract's form, adds the field `account_id_form` = `minted` on every account entry so a consumer rejects a raw id BY FIELD, and states the order as ascending by the minted `account_id`.

**The cell (`DB-b-317`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p183_contract_055_minted_form.py` (your three criteria) and the issuer's REFERENCE DIFF `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/DB317_REFERENCE.patch` (the five files of this cell, already green against the checker). The contract's `change_rule` and `lineage` (follow the rule for a version bump; `lineage` and `open_changes` may change).
2. **Apply the reference diff** (`git apply` from your worktree root, then read every hunk): the contract at the agreed paths only (version `0.5.5`, `account_entry_fields` gains `account_id_form` after `account_id`, the new `account_id_form_rule`, the ascending order in `document.shape` and `row_dimensions.account.order`, the source note of `account_id`, one clause in `per_row_member_form`); `handler.py` `_filled_mint` sets `account_id_form` = `"minted"` on every entry and sorts the accounts ascending by the minted id; `publisher.py` `validate_filled_report` requires the five fields (the constant gains `account_id_form`), the form `minted`, a minted-shaped id (`acc_` plus 24 lowercase hex, no regex, no new import), and ascending order; the two test files: the helpers `_minted` and the publish fixture carry the form and the order, and FOUR NEW tests whose names contain `form` or `ascending` are added (a missing or other form is refused; a raw-looking id and an out-of-order list are refused; every entry carries `minted`; the accounts are ascending). If the contract's `change_rule` asks for more (a `lineage` line, an `open_changes` entry), add exactly that and nothing else. Nothing outside the five files, the `<paths>` below and your folder changes.
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p183_contract_055_minted_form.py" . DB183-1-AC1`, then AC2, then AC3.
4. **Record** `RD_CONTRACT_055_FACTS_R149.json` in your folder with EXACTLY these fields: `contract_version` ("0.5.5"); `changed_contract_paths` (sorted dotted paths of the leaves that differ from the base); `reader` (one sentence: what `_filled_mint` now does); `validator` (one sentence: the four new refusals); `tests_added` (the names of the new tests); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: nothing was deployed, the portal mirror and the first filled pass are later, and whether the function's own run of the new validator over every real household is unknown).

<criterion id="DB183-1-AC1" cell_refs="DB-b-317"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p183_contract_055_minted_form.py" . DB183-1-AC1</invocation><expect>DB183-1-AC1 PASS</expect></criterion>
`DB183-1-AC1` -- the contract reads 0.5.5 and changed only at the agreed dotted paths; `handler.py` changed only in `_filled_mint` and new functions of its first `FILLED-REPORT-A` block; `publisher.py` only in `validate_filled_report` and nothing outside its second block; `locals.tf` is byte-identical. Base: FAIL.
<criterion id="DB183-1-AC2" cell_refs="DB-b-317"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p183_contract_055_minted_form.py" . DB183-1-AC2</invocation><expect>DB183-1-AC2 PASS</expect></criterion>
`DB183-1-AC2` -- behaviour over a fake S3: the composed document carries `account_id_form` minted on every entry, the accounts ascending by the minted id with each entry keeping its own `last4`; the validator refuses a missing form, another form, a raw-looking id, an out-of-order list and an extra account field; the pass writes one object that carries the form and no raw id. Base: FAIL.
<criterion id="DB183-1-AC3" cell_refs="DB-b-317"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p183_contract_055_minted_form.py" . DB183-1-AC3</invocation><expect>DB183-1-AC3 PASS</expect></criterion>
`DB183-1-AC3` -- at least four NEW tests carry `form` or `ascending` in their name, and both filled-report test files pass under pytest. Base: FAIL.

<expected_criteria>DB183-1-AC1,DB183-1-AC2,DB183-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no Terraform command, no push. Writes: the contract, the one handler, the one publisher, the two test files and your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the reference diff does not apply, or a checker clause is wrong rather than your edit, file a BLOCKING row naming it and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W252-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json
infra/aws/lambda/investor-reporting/reporting-publish/handler.py
infra/aws/lambda/investor-reporting/reporting-publish/publisher.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_reader.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_publish.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~252/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-317.contract-055-minted-account-id-form.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 177 (round 150, workstream CONTRACT055), cell `DB-b-317`.
<owned_cells>DB-b-317</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB183-1-AC1, DB183-1-AC2, DB183-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~252/IRPT_DASHBD.TO-DB-b-317.contract-055-minted-account-id-form.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB183-1-AC1,DB183-1-AC2,DB183-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the changed contract paths in one line; the reader and the validator in one line each; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a contract file, one handler block, one publisher block and tests in a branch; no plan, no apply, nothing deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the issuer ran them on a reference tree (green, the reference diff is committed beside the checker) and on six single-fault mutants and one diff mutant (all red).
lane: the <paths> block IS the grant.
</preflight>
