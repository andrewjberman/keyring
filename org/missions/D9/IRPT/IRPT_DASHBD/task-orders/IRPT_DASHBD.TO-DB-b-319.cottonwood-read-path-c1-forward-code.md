# TO IRPT_DASHBD.TO-DB-b-319 -- C1 of the Cottonwood Performance read path: the CODE. The 49F read function FORWARDS a Cottonwood request to the Cottonwood read function through a literal one-entry map, after its own guard; the target runs its own full guard (CTO ruling A, msg 10134, conditions 1 and 2) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-319</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~253</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>COTFWD</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/RULING_COTTONWOOD_READ_PATH_OPTION_A_20261017.md` @6bfcbcf2cc (A ruled; condition 1: the Cottonwood function runs the full served guard on the forwarded event and trusts no forwarder field, with a forged-forward refusal test; condition 2: the forward is a literal one-entry map, admitted by the 49F guard first, and never logs the body; tests cover the 49F path unchanged, cottonwood forwarded, and others refused) and C0's record (`COT_READ_C0_RECORD.json`: the live function refuses cottonwood at the directory bucket map with FIRM_BINDING) | **Decomp cell:** `DB-b-319` (decomposition section 179).

**Risk class WORLD** is the floor of the path (`infra/`): one source file and a new test file in a branch. No Terraform command, no AWS call, no push. Nothing is deployed: the apply is the pair (C4).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-253` (branch `wk-IRPT_DASHBD-253`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~253/`. Never push; never commit the workspace `portal` gitlink. Counts, dates, hashes and words only in the repo, a row, a commit message or your report; use synthetic ids and the marker strings of the tests only. **Before every commit, scan what you stage for a client figure and for long identifier runs; the commit gate's client-data list is absent on this box, so that scan is yours.** **Commit order: the artifact first, then the proof instance, then the status flip to complete as the LAST commit.** Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them.

**The cell (`DB-b-319`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p185_cot_read_forward.py` (your three criteria) and the issuer's REFERENCE DIFF `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/DB319_REFERENCE.patch` (served.py and one new test file, already green against the checker); `infra/aws/lambda/investor-reporting/_authz/served.py` `handle` (the internal-caller test, `bucket_for`, the allowed-firm narrowing) and `_authz/tests/test_allowed_firm_ids.py` (the harness the new tests copy).
2. **Apply the reference diff** (`git apply` from your worktree root, then read every hunk): `served.py` gains (a) the module-level LITERAL map `FORWARD_FUNCTION_ENV = {"cottonwood": "IRPT_FORWARD_COTTONWOOD_FUNCTION"}` (exactly one entry; only the 49F function will ever have the variable set, so only it forwards; the Cottonwood function's own environment never sets it), (b) the `forward_invoke` port on `Entry.__init__` (a callable or None), (c) the method `Entry._forward(event, function_name, operation)` (the original event handed to a synchronous Lambda invoke, the proxy response returned untouched, ANY failure answered NOT_READY with no class, message or body, nothing printed or logged, the event never edited), (d) one change in `handle`: where `bucket_for(selected)` raises, forward ONLY if the literal map names the firm AND the environment names the target (else FIRM_BINDING as today), and call `_forward` only AFTER the existing allowed-firm narrowing (`verified = selected`). The caller was admitted as INTERNAL and narrowed by its profile row before the forward, as for any firm. The new test file `_authz/tests/test_forward_cottonwood.py` (11 tests; at least six carry `forward` in the name) is part of the diff. If a hunk does not apply, or you think the reference is wrong, file a BLOCKING row and stop on it.
3. **Nothing else changes:** no other source file, no other test, no Terraform, no registry row (the Cottonwood ownership-map location is the next cell's, after the pair's real probe).
4. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p185_cot_read_forward.py" . DB185-1-AC1`, then AC2, then AC3 (AC3 runs the whole `_authz/tests` directory, about 25 seconds).
5. **Record** `RD_COT_READ_FORWARD_FACTS_R149.json` in your folder with EXACTLY these fields: `forward_map` (the literal, as a string); `guard_order` (one sentence: where in `handle` the forward sits relative to the internal test and the narrowing); `failure` (one sentence: what a failed forward answers); `logging` (one sentence: what is logged); `tests_added` (the names of the new tests); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: nothing was deployed, the Cottonwood function does not exist yet, the real proxy event across a real Lambda invoke was not exercised, and whether a staff read of a Cottonwood account is served without a Cottonwood ownership map is unknown until the pair's probe).

<criterion id="DB185-1-AC1" cell_refs="DB-b-319"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p185_cot_read_forward.py" . DB185-1-AC1</invocation><expect>DB185-1-AC1 PASS</expect></criterion>
`DB185-1-AC1` -- only `served.py` and the new `test_forward_cottonwood*` file changed; `served.py` only at the agreed places (at most 8 lines removed and 70 added); `FORWARD_FUNCTION_ENV` is exactly the one-entry literal; `_forward` logs and prints nothing and edits no event. Base: FAIL.
<criterion id="DB185-1-AC2" cell_refs="DB-b-319"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p185_cot_read_forward.py" . DB185-1-AC2</invocation><expect>DB185-1-AC2 PASS</expect></criterion>
`DB185-1-AC2` -- behaviour on the real `Entry.handle`: cottonwood forwarded once with the original event and the reply untouched; the 49F path unchanged; inflection, a non-internal caller, a missing environment and an unlisted caller refused; a failure is NOT_READY and leaks nothing; nothing printed; a forged forwarder field admits nothing at the target. Base: FAIL.
<criterion id="DB185-1-AC3" cell_refs="DB-b-319"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p185_cot_read_forward.py" . DB185-1-AC3</invocation><expect>DB185-1-AC3 PASS</expect></criterion>
`DB185-1-AC3` -- at least six NEW tests carry `forward` in their name and the whole `_authz/tests` directory passes. Base: FAIL.

<expected_criteria>DB185-1-AC1,DB185-1-AC2,DB185-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no Terraform command, no push. Writes: `served.py`, the new test file and your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W253-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_authz/tests/test_forward_cottonwood.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~253/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-319.cottonwood-read-path-c1-forward-code.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 179 (round 150, workstream COTFWD), cell `DB-b-319`.
<owned_cells>DB-b-319</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB185-1-AC1, DB185-1-AC2, DB185-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~253/IRPT_DASHBD.TO-DB-b-319.cottonwood-read-path-c1-forward-code.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB185-1-AC1,DB185-1-AC2,DB185-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the guard order and the failure answer in one line each; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one source file and a new test file in a branch; no plan, no apply, nothing deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; no grant changes (the forward's InvokeFunction grant is cell C2's).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the issuer ran them on a reference tree (green, the reference diff is committed beside the checker) and on five single-fault mutants (all red).
lane: the <paths> block IS the grant.
</preflight>
