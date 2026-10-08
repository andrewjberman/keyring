# TO TCKT_VNEXT.TO-F10-l2 -- household is optional for the commentary writer only, declared as type data

<to_id>TCKT_VNEXT.TO-F10-l2</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~3</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>F10</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (a Lambda handler); nothing is applied | **Decomp cell:** `F10-l-2`
(`decompositions/TCKT_VNEXT_DECOMP_F10.md`) | **outcome_ref:** FWD-6 | **depends_on:** TO-F10-l1 (drained @49c04cd4b2)

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~3`. Your worktree is `C:/tmp/tckt-f10-1`, now on the NEW branch `wk-tckt_vnext-f10-2`, cut from box/dell2
at the issuance commit (it already carries your F10-l-1 merge). Work and commit only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~3 <0.9.0_WK_TCKT_VNEXT~3@opal.agent>" -F <msgfile> -- <paths>`. Write the message
file with the Write tool. Every path is relative to the worktree root.

### THE CELL

`F10-l-2`. The IRPT analysis composition carries no household (row NFRA_TRNSPT-D2-S7; `~P2` msg 1849), so the commentary drafter
cannot supply one. The CTO ruled (msg 1875): household is optional for `svc-commentary` ONLY, declared as type data. Humans still
must answer it, and no placeholder is ever invented.

1. On the `analysis_request` definition in `TYPE_DEFINITIONS` (`infra/aws/lambda/ticket_center/lambda_function.py:86`, the
   `household` question), declare the exemption as data, e.g. `"optional_for": ["svc-commentary"]` on that question. The checks
   read the definition, so do not hardcode it in a branch.
2. Thread the principal class into answer validation (`_answer_required` `:570`, `_validate_answers` `:579`, the call at `:1044`
   in `create_ticket`):
   - a question whose `optional_for` names the caller's class is not required for that caller;
   - every other question, and every other caller, keeps today's rule exactly.
   The SUBMIT path (`submit_form`) is untouched.
3. When `svc-commentary` omits household, store NO household key in `answers`: no empty string, no "unknown", no placeholder. When
   it sends one, validate and store it as today.

**Tests:** append to `infra/aws/lambda/ticket_center/tests/test_commentary_write.py`, with EXACTLY these function names:
- `test_svc_commentary_household_optional`: a svc-commentary create with no household gets 201;
- `test_human_household_still_required`: an internal human with no household gets 400, as today;
- `test_household_optional_declared_in_type_definition`: the exemption is read from `TYPE_DEFINITIONS`;
- `test_svc_commentary_household_absent_stores_no_placeholder`: the stored `answers` has no `household` key.

### ACCEPTANCE

<criterion id="F10-l2-AC1" cell_refs="F10-l-2"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_CHECKS/f10_checks.py f10-household</invocation><expect>F10-HOUSEHOLD-OK</expect></criterion>
`F10-l2-AC1`: the four household tests named above exist and pass.

<criterion id="F10-l2-AC2" cell_refs="F10-l-2"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_CHECKS/f10_checks.py f10-regress</invocation><expect>F10-REGRESS-OK</expect></criterion>
`F10-l2-AC2`: the whole `ticket_center/tests` directory passes, with at least 104 passed and 0 failed.

<expected_criteria>F10-l2-AC1 F10-l2-AC2</expected_criteria>

Dry-run at base: AC1 `FAIL missing test(s)`; AC2 `OK passed=104`.

## BOUNDS

- **Grant.** The `<paths>` block plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~3/` and this order's file (status
  flip only).
- **WORLD by path; NOTHING is applied.** No terraform, no deploy, no AWS call.
- No non-ASCII. No new notification.
- **Refusal clause.** If a criterion cannot be met as written, stop and report it. Append a row `TCKT_VNEXT-D2-W3-S<k>` (next unused) to
  the channel below. Never weaken a test.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_commentary_write.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_F10.md</decomp_doc> (workstream F10), cell `F10-l-2`.
<owned_cells>F10-l-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: F10-l2-AC1 F10-l2-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~3/TCKT_VNEXT.TO-F10-l2.household-optional-for-svc-commentary.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> F10-l2-AC1 F10-l2-AC2` BEFORE the flip to `complete`.
</proof_of_spec>

**REPORT (your final message, once):** each check line verbatim, the commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- a narrowing-only exemption for one principal on one question; the human-still-required arm is the negative control.
lane: the <paths> block IS the grant; the deploy is a later code-only apply order to 0.7.0_AE_CloudOps~DELL2 under its own pair.
</preflight>

Source: CTO msg 1875 (ruled; recorded at `CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_12_20261008.md` ADDENDUM 1 @55491bb7ee); `~T2` msg 1864;
row NFRA_TRNSPT-D2-S7.

# pipeline-override: the code-only deploy of F10-l-2 (an issuer act cut as an apply order to 0.7.0_AE_CloudOps~DELL2 after the drain) is not a worker cell; this issuance covers the workstream's one new worker cell (F10-l-2).
