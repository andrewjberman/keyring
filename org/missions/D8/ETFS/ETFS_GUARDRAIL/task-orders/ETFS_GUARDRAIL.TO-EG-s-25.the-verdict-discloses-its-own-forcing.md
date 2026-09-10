# TO ETFS_GUARDRAIL.TO-EG-s-25 -- THE VERDICT ARTIFACT MUST DISCLOSE ITS OWN FORCING: the deployed renderer carries ZERO disclosure tokens against five non-zero positive controls, so a driven refusal would be indistinguishable from an organic one forever after

<to_id>ETFS_GUARDRAIL.TO-EG-s-25</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~5</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete -- S25-AC1 PASSES BY OUTPUT (rc 0, 6 of 6 arms, token EGS25-VERDICT-DISCLOSES-FORCING) and S25-AC2 is RECORDED with its evidence and NO verdict for 3.0.0_SA_CVO at L9; proof-of-spec-check rc 0 VALID with 4 of 4 surprise ids resolving to channel rows. coverage_verdict.json now records HOW THE RUN WAS CONFIGURED on BOTH branches -- forced {forced:true, mechanism:"--fixture-remove", the spec, the count, a run id} and unforced {forced:false, mechanism:"none"} -- and the unforced case is enforced by the DEFAULT PATH, so a caller cannot omit it by forgetting. The absence it closes was re-measured on the deployed bytes: 10 of 10 disclosure tokens ZERO against 5 of 5 positive controls NON-ZERO. THE VERDICT DID NOT MOVE: old deployed bytes vs new, 5 of 5 pre-existing keys and 10 of 10 class counts identical across a PUBLISH and a REFUSE scenario, exactly one key added. DEPLOYED and byte-verified to s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py under its own closed NEVER-2 entry (opened 05:18:38Z before the 05:19:33Z copy, closed 05:24:13Z before the grading reads), rollback exact from two independently verified sources. No send, no invoke, no box run, and platinum/reports/ unchanged 36 of 36. THE FLIP ITSELF was blocked until now and is recorded as row W5-S7: this branch predated the issuance that created this face, so committing it was an ADD the L6 gate rightly refuses; the issuer directed the merge of CLOUD into the branch (b831616961, under safe-merge with every guard run and the channel conflict resolved as a proven 71-row UNION), which put the face at HEAD and made this flip a MODIFICATION. The audited pipeline-override escape was NOT taken. Original status line follows -- pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: row `ETFS_GUARDRAIL-W4-S2`, filed by `0.9.0_WK_ETFS_GUARDRAIL~4` when `EG-s-21` proved UNSATISFIABLE AS CUT -- the issuer's defect. Decomposition **v0.6** s.15, cell `EG-s-25`.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.6 | **Decomp cell:** `EG-s-25` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.6, s.15) | **outcome_ref:** FWD-9 (the honesty half; FWD-9 itself is closed by `EG-s-21` after this lands)

---

## THE CELL

`EG-s-21` requires that a driven refusal be **DISCLOSED ON THE ARTIFACT with its run id, so no later reader mistakes a forced refusal for an organic one**. `0.9.0_WK_ETFS_GUARDRAIL~4` measured that the artifact cannot carry that, on the renderer **the box actually pulls**:

- `s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py`, 62,880 B, sha256 `55701125e86740f3...`, **byte-equal to the repo build input**.
- **10 of 10 disclosure tokens read ZERO**, against **5 positive controls all non-zero** on the same file (`generated_at` 1, `fixture_remove` 22, `verdict` 23, `unresolved` 13, `per_partner` 6). The zeros are an ABSENCE, not a dead read -- which is exactly the control that makes a zero worth quoting.

**So the honesty requirement in `EG-s-21` was unsatisfiable as I cut it, and that is my defect.** A forced refusal written today would land in `coverage_verdict.json` looking precisely like a real one, and the forcing would live only in a worker's report -- which is the shape this project exists to prevent.

**YOUR JOB: make the verdict artifact record that it was forced, what the forcing was, and which run did it.**

The mechanism it must record already exists and you are not building it: `--fixture-remove` is declared at `render_month_end.py:1022`, parsed by `_parse_fixture_remove` at `:852`, and applied at `:1030`/`:1033`/`:1040`/`:1047`. The verdict is decided at `:963` (`verdict = "REFUSE" if any_c else "PUBLISH"`). **When a run removes data from its own input, the object it writes must say so.**

⛔ **AN ABSENT FORCING MUST BE DISTINGUISHABLE FROM AN UNRECORDED ONE.** A field that is missing when nothing was forced and missing when something was forced is not a disclosure. An ordinary run must write the field with an explicit not-forced value, so a later reader can tell "this run forced nothing" from "this run did not say". That is arm (c), and it is the arm that carries the outcome.

---

## DELIVERABLE

The changed `data/etfs/scripts/presentation/render_month_end.py`, coverage in its own suite, and a battery under `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/`. Every `.py` edit passes `.tools/commit-gate.sh`.

⛔ **THE DEPLOY IS IN THIS CELL and it is an `aws s3 cp` to the artifact prefix, NOT Terraform** -- the box pulls this file by key at run time (`lambda_function.py:348`). It lands under its own NEVER-2 entry with a never-widen sign-off, opened BEFORE the copy and closed BEFORE the grading reads, naming the exact key and the byte-for-byte rollback.

---

## BOUNDS

- ⛔ **NO SEND, NO ORCHESTRATOR INVOKE, NO BOX RUN.** You change code, exercise it hermetically, deploy the file, and STOP. The driven run is `EG-s-21`'s single permitted act.
- ⛔ **DO NOT TOUCH THE ORCHESTRATOR.** `infra/aws/lambda/etfs-reports-orchestrator/` is `EG-s-24`'s surface, live on another slot right now.
- ⛝ **DO NOT TOUCH `data/etfs/scripts/coverage/`** -- `0.9.0_WK_ETFS_GUARDRAIL~1` is live there on `EG-s-23`.
- ⛔ **DO NOT CHANGE THE VERDICT LOGIC.** `:963`'s class-C rule is `EG-s-4`'s and is not this cell's subject. You are adding a record of HOW the run was configured, never changing WHAT it decides.
- ⛔ **NO SERVED REPORT KEY IS WRITTEN OR DELETED.** The artifact prefix is a code location, not served output; `platinum/reports/` is untouched by this cell.
- Andrew's ~02:5xZ constraint stands: **aj@opalinvest.com is not a recipient of any driven run**, and this cell fires no run at all.
- Found something off-task? Append a row to `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md` and KEEP WORKING.

---

## ACCEPTANCE

<criterion id="S25-AC1" cell_refs="EG-s-25"><invocation>timeout 600 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/test_egs25_verdict_discloses_forcing.py</invocation><expect>EGS25-VERDICT-DISCLOSES-FORCING</expect></criterion>
**`S25-AC1` -- PASSES BY OUTPUT.** One battery, printing every number beside its denominator, ending with the token only when all six arms hold. Each arm is one clause.

**(a) THE ABSENCE REPRODUCES FIRST, ON THE DEPLOYED BYTES.** Against the renderer as deployed, re-take the token census: the disclosure tokens read ZERO and the positive controls read NON-ZERO, both printed with the file's sha256 and its byte count. **If a disclosure field already exists, the premise is wrong: file a row, print it, and STOP.**

**(b) A FORCED RUN DISCLOSES.** With a fixture-remove spec supplied, the written `coverage_verdict.json` carries the forcing spec and a run id, printed whole.

**(c) AN UNFORCED RUN SAYS SO EXPLICITLY.** With no spec supplied, the object carries the SAME field with an explicit not-forced value -- printed beside the forced case and textually different. **A missing field is not a disclosure and does not pass this arm.**

**(d) THE VERDICT ITSELF DID NOT MOVE.** Re-compute a verdict over the same inputs before and after your change and show every class count and the `verdict` value identical, denominator printed. The forced case is excluded from this comparison and you say so.

**(e) THE DEPLOY IS REAL AND REVERSIBLE.** The served object at the artifact key is byte-equal to your committed bytes (sha256 both sides, printed), the prior object archived and its sha256 recorded in the entry BEFORE the copy, and the rollback stated as an exact key-and-bytes restore. Entry OPENED before the copy, CLOSED before the grading reads.

**(f) NO SEND, NO INVOKE, NO SERVED-REPORT WRITE.** Print the evidence from your own run, with the denominator of what you checked, that no SES call, no Lambda invoke and no write under `platinum/reports/` occurred.

<criterion id="S25-AC2" cell_refs="EG-s-25" judgment="true"/>
**`S25-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: the field's shape and why a reader can trust it; whether any consumer parses `coverage_verdict.json` and could be broken by a new key, censused with a denominator rather than recalled; whether the run id you record is the one a reader could join to a run log, and if not, what it is; and what this disclosure does NOT prove. No verdict.

<expected_criteria>S25-AC1, S25-AC2</expected_criteria>

<paths>
data/etfs/scripts/presentation/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/
org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-25.the-verdict-discloses-its-own-forcing.md
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.6, cell `EG-s-25`.
<owned_cells>EG-s-25</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-09 ~22:2xZ, its VINTAGE STATED rather than re-run -- WITHIN BUDGET, 5 of 5 carriers, GATES ARMED 25, and ZERO of the 25 armed gates names ETFS_GUARDRAIL, the daily producers or `opal-data-etfs`. THE VINTAGE HOLDS BECAUSE no schedule, rule or gate in this project's surface has been created or changed since. BLIND SPOT, stated: this cell replaces a file the MONTHLY schedule's box pulls at run time, which no schedule census can see -- the NEVER-2 entry, the archived prior object and arm (d)'s no-movement proof ARE that control.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied; the copy runs under the seat's existing credentials to an existing key.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants. `data/etfs/scripts/presentation/` is NOT a `{gold,silver,bronze}` path, so CLAUDE.md rule 13's DS commit lane does not gate it; rule 14's `.tools/commit-gate.sh` binds on every `.py` edit.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S25-AC1`, `S25-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/ETFS_GUARDRAIL.TO-EG-s-25.the-verdict-discloses-its-own-forcing.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), validated with `python .tools/proof-of-spec-check.py <instance> S25-AC1,S25-AC2` BEFORE the complete flip, which you commit yourself.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
