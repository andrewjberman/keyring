# TO ETFS_GUARDRAIL.TO-EG-s-20 -- THE SEND PATH MADE CORRECT AND TEST-SAFE: the terminal send's guard reads a key the renderer never writes, at TWO sites, and the rehearsal built to catch that is blind to it for the same reason; plus a driven run must be unable to reach aj@ before anything may be driven at all

<to_id>ETFS_GUARDRAIL.TO-EG-s-20</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~4</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete -- 2026-09-10 ~04:0xZ by `0.9.0_WK_ETFS_GUARDRAIL~4`. S20-AC1 PASS by output (15 passed, round-1 floor 7; the NEW arms FAIL 7 of 7 against the pre-fix blob), S20-AC2 PASS by output (20 of 20 arms HOLD, EGS20-SEND-PATH-CORRECT-AND-TEST-SAFE), S20-AC3 RECORDED with no verdict for the CVO at L9. proof-of-spec-check rc=0 VALID. 1 row filed: ETFS_GUARDRAIL-W4-S1. NO SEND AND NO INVOCATION OF THE ORCHESTRATOR WAS FIRED. Originally: pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: PRD **v0.5** @`7ba9b976b0` (the CTO's application of Andrew's ~03:0xZ law: FWD-7 SUPERSEDED by FWD-10 because its only proof was a failure nobody controls AND row `W1-S25` measured that the send cannot fire at all); decomposition **v0.3** s.12, cell `EG-s-20`. Andrew's ~02:5xZ standing constraint binds this face: no test run reaches aj@opalinvest.com.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.5 | **Decomp cell:** `EG-s-20` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.3, s.12) | **outcome_ref:** FWD-10's PRECONDITION (the send made reachable and the driving made safe)

---

## THE CELL

`EG-s-20` -- **TWO SITES READ A KEY THAT DOES NOT EXIST, AND ONE OF THEM IS THE TEST THAT WAS SUPPOSED TO CATCH THE OTHER.** Measured on the DEPLOYED bytes (zip `lambda_function.py` sha256 `dc05ea90c94dc41e`, 28,504 B) by `0.9.0_WK_ETFS_GUARDRAIL~1` in rows `W1-S25` and `W1-S29`:

```
:435  unresolved_days = (unresolved_doc or {}).get("unresolved") or []      <- the live guard
:516  ... .get("unresolved") ...                                            <- terminal_qa, the send-free rehearsal
SERVED coverage_unresolved.json top-level keys : ['49financial', 'cottonwood']
FIXTURE test_terminal_send.py:118              : ['unresolved']
```

The renderer writes that document **keyed by partner**. So the guard evaluates falsy against real bytes and `_send_terminal_unresolved` is SKIPPED EVEN ON A GENUINE REFUSE -- FWD-7 was unreachable in production and nothing said so, which is the single instance that argued Andrew's whole law. Round-1 `EG-s-8` passed only because its fixture was built to the DOCSTRING's shape rather than the producer's output; and `:516`'s rehearsal, which exists to exercise this path without sending, makes the SAME wrong assumption -- so a QA run of the terminal path reports healthy on the day a real refusal sends nothing. **Fix both sites, and build the test from the PRODUCER'S OUTPUT rather than from either consumer's assumption.**

⛔ **THE SECOND HALF IS ANDREW'S CONSTRAINT AND IT IS A PRECONDITION, NOT A COURTESY.** His ~02:5xZ word, verbatim: *"make sure no test run hits aj's email, that is not appropriate."* The mailer's recipient set belongs to the PRODUCER (`EMAIL_RECIPIENT`, read live = `aj@opalinvest.com,andrew@opalinvest.com`), so no invoker can satisfy that word as the code stands, and `EG-s-21` may not drive anything until this order has made it impossible. Build a TEST-INVOCATION recipient path that **cannot** reach aj@ -- a recipient override honoured only on a test invocation, or no send at all on one; the shape is yours and you justify it. Two properties decide it: a test invocation CANNOT reach aj@ under any branch, and a SCHEDULED invocation is UNCHANGED (the 10-01 fire must still deliver to both, because FWD-5's real joint delivery is the product). **Proven by a read of the DEPLOYED handler, never by intent** -- that is the CTO's own condition at 94909.

⛔ **NO SEND IS FIRED BY THIS ORDER.** You change code, you deploy it, and you prove the properties by reading the deployed bytes and by unit tests. The first real driven run is `EG-s-21`'s, after this order is terminal. If you believe a criterion here requires firing the orchestrator, STOP on that arm and file a row -- it is a cut defect and mine.

⛔ **NEVER-2 AND SPINE v3.9's ORDERING.** This is a Lambda source change deployed by Terraform: open the change-management entry naming the served function, its pre-state (`CodeSha256`, `LastModified`, read live), the rollback (`git show <pre-commit>:<path>` re-applied), and BOTH never-widen halves; then plan; then `HALT_ACK=1 .tools/safe-apply.sh` on a SAVED PLAN FILE so what lands is what was reviewed; then **CLOSE AND COMMIT the entry BEFORE the grading reads**. Per row `W1-S16`, any detail the entry must CARRY is appended LAST, after its final ledger mutation. **NEVER bare `terraform apply`; NEVER `aws lambda update-function-code`.**

## DELIVERABLE

1. The two-site guard fix and the test-safe recipient path, committed BEFORE the apply.
2. A test built from the PRODUCER's output: it constructs `coverage_unresolved.json`'s shape by RUNNING the renderer's own writer (or by loading a served artifact and asserting the writer produces that shape), never by hand-typing the consumer's assumption -- and it FAILS against the pre-fix guard.
3. `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/the-send-path-correct-and-test-safe.result.md` -- what you measured, each criterion's invocation and output verbatim with rc and denominator, the recipient shape you chose and why, and any row you filed.
4. The proof-of-spec instance (below).

## BOUNDS

- **Your write surface is the `<paths>` block below**, PLUS your own `deliverables/<serial>/` folder and this face's `<status>`.
- **THE RUNG-3 ASK IS NOT YOURS.** Row `W1-S27` (the egress ask names 1 of 2 unresolved dates) is a SEPARATE cell on this same file and is deliberately NOT bundled here -- a fix cell that quietly grows a second subject stops being reviewable. Do not touch it; if you must read it to understand the document's shape, say so.
- **EVERY invocation is bounded.** `timeout 120` on reads; `timeout 600` on plan/apply; a targeted plan only.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W4-S<k>`; append, cite `path@commit`, never edit an existing row, keep working.
- **NEVER `git push`.** Report push state as MEASURED.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9.

<criterion id="S20-AC1" cell_refs="EG-s-20"><invocation>python -m pytest infra/aws/lambda/etfs-reports-orchestrator/test_terminal_send.py -q</invocation><expect>passed</expect></criterion>
`S20-AC1` -- the existing battery plus your new arms is green, and the count is RECORDED (>= the 7 that passed at `30be6b2757`). At least one NEW arm is built from the PRODUCER's output shape and FAILS against the pre-fix guard -- prove that by running it against the pre-fix blob and printing the failure, because a test that passes both before and after is not a test of this change.

<criterion id="S20-AC2" cell_refs="EG-s-20"><invocation>timeout 600 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/test_egs20_send_path.py</invocation><expect>EGS20-SEND-PATH-CORRECT-AND-TEST-SAFE</expect></criterion>
`S20-AC2` -- a battery you write, printing the token ONLY when every arm holds, ALL READ FROM THE DEPLOYED BYTES (fetch the function's own code zip and hash it; never the worktree, Rule 22a): (a) BOTH sites are fixed -- `:435`'s guard and `:516`'s rehearsal each quoted post-fix with their line numbers, and a census over the deployed source showing ZERO remaining reads of the absent key (denominator: occurrences scanned); (b) the guard now evaluates TRUTHY against a real served `coverage_unresolved.json` fetched from S3, printed, and the same expression evaluated against the pre-fix blob printed beside it as the discriminating pair; (c) THE RECIPIENT PROPERTY, both directions: a TEST invocation's resolved recipient list CANNOT contain aj@opalinvest.com (the resolution shown from the deployed bytes with the test marker set), and a SCHEDULED invocation's list is UNCHANGED and still contains BOTH -- print both lists; a fix that makes the scheduled path stop delivering to aj@ is WRONG and fails this arm; (d) DEPLOYED == BUILT: the zip's `lambda_function.py` sha256 equal to the committed blob's, both printed; (e) the entry OPEN before the apply (its opened-at preceding the apply's UTC), CLOSED AND COMMITTED before these reads (both commit hashes printed), with the rollback and both halves named; (f) the targeted plan read exactly one resource pre-apply (quoted verbatim from the transcript, which you PRESERVE in your deliverables because it is unreproducible afterwards) and the post-apply re-plan reads `No changes` at `-detailed-exitcode` rc 0. Denominators on every list.

<criterion id="S20-AC3" cell_refs="EG-s-20" judgment="true"/>
`S20-AC3` -- graded by the CVO at L9: the recipient shape chosen and why, what a future reader must do to keep the scheduled path's joint delivery intact, whether the new test would have caught the original defect had it existed in round 1, and what remains untested about the terminal path after this order (the send itself is `EG-s-21`'s). Evidence with vintage. NO VERDICT.

<expected_criteria>S20-AC1, S20-AC2, S20-AC3</expected_criteria>

<paths>
infra/aws/lambda/etfs-reports-orchestrator/
infra/aws/terraform/etfs-reports/
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.3, cell `EG-s-20`.
<owned_cells>EG-s-20</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-09 ~22:2xZ, its VINTAGE STATED rather than re-run at this issuance -- WITHIN BUDGET, 5 of 5 carriers, GATES ARMED 25, REACHED-DENOMINATORS C1=23 C2=6 C3=12 C4=20 C5=335, ZERO of the 25 naming ETFS_GUARDRAIL, `etfs-reports-orchestrator` or `opal-data-etfs`. THE VINTAGE HOLDS BECAUSE no schedule or rule in this surface has changed since; the monthly schedule was read LIVE at 02:0xZ under `EG-s-18` (ENABLED, `cron(0 10 1 * ? *)`, RoleArn `etfs-reports-scheduler-role`) and is untouched by this cell. BLIND SPOT, stated: the gate ledger cannot see a source change to a Lambda -- the NEVER-2 entry, the saved-plan apply and the DEPLOYED-vs-BUILT arm ARE those controls.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is created, widened or read on the APPLIED plane by this cell; the function's role is untouched.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants. `test_terminal_send.py` lives inside the granted Lambda directory and is this cell's own subject.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S20-AC1`, `S20-AC2`, `S20-AC3`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/ETFS_GUARDRAIL.TO-EG-s-20.the-send-path-correct-and-test-safe.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), validated with `python .tools/proof-of-spec-check.py <instance> S20-AC1,S20-AC2,S20-AC3` BEFORE the complete flip, which you commit yourself. Flip only when the mechanical criteria PASS by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row. `ETFS_GUARDRAIL.TO-EG-s-21` follows on that report from the same issuer, and it CANNOT start until this order is terminal.
