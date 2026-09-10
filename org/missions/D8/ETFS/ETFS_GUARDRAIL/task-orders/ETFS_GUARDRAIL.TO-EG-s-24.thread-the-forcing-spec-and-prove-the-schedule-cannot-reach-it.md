# TO ETFS_GUARDRAIL.TO-EG-s-24 -- THREAD THE FORCING SPEC FROM THE EVENT INTO THE RENDER COMMAND, AND PROVE THE SCHEDULED PATH CANNOT REACH IT: the renderer has carried `--fixture-remove` all along and the orchestrator builds a FIXED command, so FWD-9's forced condition is unreachable by construction and no seat can drive a refusal

<to_id>ETFS_GUARDRAIL.TO-EG-s-24</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~4</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: row `ETFS_GUARDRAIL-W4-S2`, filed by `0.9.0_WK_ETFS_GUARDRAIL~4` when `EG-s-21` proved UNSATISFIABLE AS CUT -- the issuer's defect. Decomposition **v0.6** s.15, cell `EG-s-24`.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.6 | **Decomp cell:** `EG-s-24` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.6, s.15) | **outcome_ref:** FWD-9 (the enabling half; FWD-9 itself is closed by `EG-s-21` after this lands)

---

## THE CELL

**`EG-s-21` was cut on a premise the world refuses, and that is mine.** It required a forced class-C condition driven through the SAME target the schedule invokes, while binding NO CODE CHANGE and granting `<paths>` that exclude the orchestrator. `0.9.0_WK_ETFS_GUARDRAIL~4` measured why that cannot be done and **refused to fire rather than spend the order's one permitted run**:

- The deployed orchestrator builds a FIXED command -- `_render_command` at `lambda_function.py:341`, returning `python3 render_month_end.py --month {month} --pdf --gate --s3-out {out}` at `:368`, handed to SSM at `:563`. An AST census over 3,142 nodes shows the handler reads exactly **4** event keys: `mode`, `month`, `probe`, `test_recipients`. **Nothing an invoker can put in the event reaches the classifier.**
- **The forcing mechanism ALREADY EXISTS and is complete -- in the renderer.** `--fixture-remove` is declared at `render_month_end.py:1022`, parsed by `_parse_fixture_remove` at `:852`, and applied at `:1030`, `:1033`, `:1040` and `:1047`. It is EG-s-6's QA hook, it removes dates from `series` IN MEMORY, and nothing on S3 is ever touched by it. **The orchestrator simply never threads it.**
- So an unforced run would have found `verdict = "REFUSE" if any_c else "PUBLISH"` (`:963`, class C only) against a served verdict reading **class C = 0 of 3 partners** -- it would have PUBLISHED, and sent the ordinary monthly email to BOTH recipients. That is round 1's measured accident (`W1-S22`/`S23`/`S24`) and it would have **breached Andrew's standing aj@ constraint while proving nothing about FWD-9.** The assignee's refusal prevented that.

**YOUR JOB IS ONE SEAM: let the event carry a forcing spec, thread it into the render command, and prove the SCHEDULED path cannot reach it.**

⛔ **THE SAFETY PROPERTY IS THE POINT OF THIS CELL, NOT A SIDE CONDITION.** CLAUDE.md is explicit that an override letting a scheduled producer run off its own inputs **CREATES A NEW REACHABLE STATE on the manual path, and the sign-off covers that state or the override does not land**. This override is worse-shaped than a `--month` override: it makes the monthly report **drop its own input data**. A scheduled fire that could reach it would publish a report over data it silently removed. So the default must be OFF, the scheduled payload must be PROVEN not to reach it, and that proof is arm (c) -- the arm this cell exists for as much as the threading.

---

## DELIVERABLE

The changed `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py`, its tests, a battery under `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/`, and the DEPLOY of the orchestrator under its own NEVER-2 entry with a never-widen sign-off naming the new reachable state. Every `.py` edit passes `.tools/commit-gate.sh`.

---

## BOUNDS

- ⛔ **NO SEND AND NO ORCHESTRATOR INVOKE IN THIS CELL.** You change code, you test it hermetically, you deploy it, and you STOP. The driven run is `EG-s-21`'s single permitted act and it stays unspent here.
- ⛔ **DO NOT TOUCH THE RENDERER.** `data/etfs/scripts/presentation/render_month_end.py` is `EG-s-25`'s surface, live on another slot. `--fixture-remove` already works; you are threading to it, not changing it.
- ⛝ **DO NOT TOUCH `data/etfs/scripts/coverage/`** -- `0.9.0_WK_ETFS_GUARDRAIL~1` is live there on `EG-s-23`.
- ⛔ **THE SCHEDULED PATH MUST BE BIT-FOR-BIT UNCHANGED** when the event carries no forcing key. Arm (b) proves it.
- Andrew's ~02:5xZ constraint stands: **aj@opalinvest.com is not a recipient of any driven run**, and this cell fires no run at all.
- Found something off-task? Append a row to `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md` and KEEP WORKING.

---

## ACCEPTANCE

<criterion id="S24-AC1" cell_refs="EG-s-24"><invocation>timeout 600 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/test_egs24_forcing_seam.py</invocation><expect>EGS24-FORCING-THREADED-SCHEDULE-CLEAN</expect></criterion>
**`S24-AC1` -- PASSES BY OUTPUT.** One battery, printing every number beside its denominator, ending with the token only when all six arms hold. Each arm is one clause.

**(a) THE SEAM REPRODUCES ITS OWN ABSENCE FIRST.** Against the code BEFORE your change, show `_render_command` produces a command containing NO `--fixture-remove` for every event shape you can construct, with the event-key denominator printed. **If a forcing key already reaches the classifier, the premise is wrong: file a row, print it, and STOP.**

**(b) THE SCHEDULED PATH IS BIT-FOR-BIT UNCHANGED.** For every marker-free payload shape the schedule can deliver, the command string your code builds is IDENTICAL to the pre-change command string -- printed, compared, with the shape denominator.

**(c) THE SCHEDULED PATH CANNOT REACH THE FORCING, ADVERSARIALLY.** Enumerate payloads that attempt to smuggle the forcing key through the scheduled shape -- absent, null, empty, wrong case, nested, string-encoded, a key the default EventBridge envelope actually carries -- and show 0 of N reach the flag, N printed. **This is the arm the cell exists for.**

**(d) THE FORCING WORKS WHEN EXPLICITLY ASKED.** An event carrying the forcing spec produces a command whose `--fixture-remove` argument is exactly the spec, printed, and parses under the renderer's own `_parse_fixture_remove` (import it; do not re-implement it).

**(e) THE DEPLOY IS REAL AND MATCHES WHAT WAS REVIEWED.** Served `CodeSha256` equals the built zip equals the value the pre-apply plan predicted, on three reads; the zip member byte-equal to `git show HEAD:<path>`; the pre-fix blob as a negative control that does NOT match. Entry OPENED before the apply and CLOSED before the grading reads, with the never-widen sign-off naming the NEW REACHABLE STATE in its own words.

**(f) NO SEND, NO INVOKE.** Print the evidence from your own run that no SES call and no orchestrator invocation occurred, with the denominator of what you checked.

<criterion id="S24-AC2" cell_refs="EG-s-24" judgment="true"/>
**`S24-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: the shape of the forcing key and why it cannot be confused with a scheduled field; what a caller could still do wrong with it; whether any OTHER caller of `_render_command` exists, censused with a denominator rather than recalled; and what this seam does NOT make reachable. No verdict.

<expected_criteria>S24-AC1, S24-AC2</expected_criteria>

<paths>
infra/aws/lambda/etfs-reports-orchestrator/
infra/aws/terraform/etfs-reports/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/
org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-24.thread-the-forcing-spec-and-prove-the-schedule-cannot-reach-it.md
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.6, cell `EG-s-24`.
<owned_cells>EG-s-24</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-09 ~22:2xZ, its VINTAGE STATED rather than re-run -- WITHIN BUDGET, 5 of 5 carriers, 56.25 s of a 90 s default, GATES ARMED 25, and ZERO of the 25 armed gates names ETFS_GUARDRAIL, the daily producers or `opal-data-etfs`. THE VINTAGE HOLDS BECAUSE no schedule, rule or gate in this project's surface has been created or changed since; the monthly rule was read LIVE under `EG-s-18` and again under `EG-s-20`'s deploy at 03:54:09Z and is unchanged. BLIND SPOT, stated: this cell CHANGES what a manual invoke of that rule's target can do, which no schedule census can see -- arm (c) and the never-widen sign-off ARE that control.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied; the function runs under its existing role and this order changes no policy.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable, and arm (c) is adversarial by construction.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants. `infra/aws/lambda/` is not a `{gold,silver,bronze}` path so rule 13's DS lane does not gate it; rule 14's `.tools/commit-gate.sh` binds on every `.py` edit, and NEVER-9 binds the apply to `safe-apply`.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S24-AC1`, `S24-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/ETFS_GUARDRAIL.TO-EG-s-24.thread-the-forcing-spec-and-prove-the-schedule-cannot-reach-it.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), validated with `python .tools/proof-of-spec-check.py <instance> S24-AC1,S24-AC2` BEFORE the complete flip, which you commit yourself.

⛔ **THE IDENTITY GATE, CORRECTED -- MY EARLIER FACE WAS WRONG AND YOU MEASURED IT (`W4-S1`).** There are TWO gates and the ORDER is the mechanism. `safe-apply.sh:11,50` runs `halt-gate-check.sh` FIRST, and that file resolves identity ONLY from `org/mcp/sessions/$CLAUDE_CODE_SESSION_ID.serial` (`:56-57`) or a `.orphan-cleaned` marker (`:76-80`) -- `OPAL_AGENT_SERIAL` appears in it ZERO times, which is why exporting it still returned rc=3. `safe-apply.sh:152-154` THEN calls `resolve_actor`, which DOES honour the variable (so your report's first clause was also wrong; the source settled both). **The gate's OWN PRINTED REMEDY at `halt-gate-check.sh:118` is legitimate and expected, not a workaround:** write your serial to that gitignored session path. Nothing tracked moves.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
