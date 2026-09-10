# TO ETFS_GUARDRAIL.TO-EG-s-27 -- THE LADDER SKIP RIDES THE FORCING AND IS NOT INDEPENDENTLY REACHABLE: a driven refusal needs the ladder off, and a second independently-settable switch on a served producer is a new reachable state nobody asked for

<to_id>ETFS_GUARDRAIL.TO-EG-s-27</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~4</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete -- S27-AC1 PASS-by-output (arms: 7 of 7 HOLD -> EGS27-SKIP-RIDES-FORCING-SCHEDULE-CLEAN, rc=0, on SERVED bytes); S27-AC2 RECORDED for 3.0.0_SA_CVO at L9, not self-graded. proof-of-spec-check rc=0. DEPLOYED-VERIFIED: served CodeSha256 5qPTUpaxx+NUvTN6hmXdNfe2pT2xwkHF9Y3Q3fFJVSw= at 2026-09-10T12:16:53Z, three reads equal, NEVER-2 entry 20260910T1215Z CLOSED with 5 of 5 legs proven. GO paired at cut (a seat order is dispatched by its issuance). Authority: `1.0.0_SA_CTO`'s ruling R-EG-6 at 95061 (PRD **v0.7**, commit `9f548bfbc9`) adopting SHAPE 1 on row `ETFS_GUARDRAIL-W4-S6`. Decomposition **v0.7** s.16, cell `EG-s-27`.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.7 | **Decomp cell:** `EG-s-27` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.7, s.16) | **outcome_ref:** FWD-9 (the enabling half of the adopted shape)

---

## THE CELL

You measured why `EG-s-21` cannot fire: the forcing dies at `render_month_end.py:999`, where the ladder re-classifies from real S3 and the fixture never touched S3. The CTO adopted SHAPE 1 -- **drive the refusal with the ladder SKIPPED** -- and refused SHAPE 2 at its own seat rather than sending a served-data rewrite to Andrew.

The renderer already has `--no-ladder` (`:1000-1008`). **The orchestrator does not thread it.** That is your cell.

⛔ **THE SHAPE MATTERS MORE THAN THE THREADING, AND THIS IS THE PART TO WEIGH BEFORE YOU WRITE ANYTHING.** The obvious implementation is a second event key. **The issuer's preference, offered with its reasoning and NOT as a prescription, is that the ladder skip RIDE THE FORCING rather than be independently settable:** when a forcing spec is present, the command carries `--no-ladder`; when it is absent, it does not, and no event key can set it alone.

The reason is the one your own `W4-S5` taught this project four hours ago. A second independently-writable switch on a served producer is a NEW REACHABLE STATE, and NEVER-1 requires the sign-off to cover it. **A skip that rides the forcing cannot be reached without also forcing** -- and forcing already discloses itself on the artifact, so the dangerous combination is self-announcing. An independent switch would let a caller disable the repair ladder on a real month with nothing forced and nothing disclosed, which is strictly worse than the hole you just fenced.

**If you judge the coupled shape wrong for a reason you can state, take the independent one and pay for it:** a full writer census by subtraction on the NEW property with N printed, an adversarial arm that the scheduled path cannot reach it, and the new reachable state named in the sign-off in its own words. That is the same bill `EG-s-24` paid, and it is a real bill rather than a discouragement.

---

## DELIVERABLE

The changed `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py`, its tests, a battery under `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/`, and the DEPLOY under its own NEVER-2 entry with a never-widen sign-off. Every `.py` edit passes `.tools/commit-gate.sh`.

---

## BOUNDS

- ⛔ **BLOCKING ORDERING -- `EG-s-26` LANDS BEFORE, OR IN THE SAME DEPLOY AS, THIS CELL. NEVER AFTER.** `EG-s-26` (live on `0.9.0_WK_ETFS_GUARDRAIL~5`) is what makes a ladder-skipped run RECORD that it skipped and that rung 3's egress ask is absent by construction. **If the skip becomes reachable while the disclosure does not yet exist, a run in that window produces a REFUSE nobody can later tell from an organic one** -- the identical unrepairable window the ordering condition on `EG-s-24` existed to prevent, and you satisfied that one by a proof obligation rather than a sequence. Do the same here: verify `EG-s-26`'s renderer on the served key **by your own sha256**, printed in the entry BEFORE the apply. If it is not there, STOP and report; do not wait in a loop.
- ⛔ **DO NOT TOUCH THE RENDERER** -- `data/etfs/scripts/presentation/` is `EG-s-26`'s surface, live in parallel.
- ⛔ **THE SCHEDULED PATH MUST BE BIT-FOR-BIT UNCHANGED** when no forcing is present. Arm (b) proves it.
- ⛔ **NO SEND, NO ORCHESTRATOR INVOKE.** You change code, test it hermetically, deploy, and STOP. `EG-s-21`'s single permitted run stays unspent.
- Andrew's ~02:5xZ constraint stands: **aj@opalinvest.com is not a recipient of any driven run.**
- Found something off-task? Append a row to `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md` and KEEP WORKING.

---

## ACCEPTANCE

<criterion id="S27-AC1" cell_refs="EG-s-27"><invocation>timeout 600 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/test_egs27_skip_rides_the_forcing.py</invocation><expect>EGS27-SKIP-RIDES-FORCING-SCHEDULE-CLEAN</expect></criterion>
**`S27-AC1` -- PASSES BY OUTPUT.** One battery, every number beside its denominator, ending with the token only when all seven arms hold. Each arm is one clause.

**(a) THE ABSENCE REPRODUCES FIRST.** Against the code as it stands, show no event shape produces a command containing `--no-ladder`, with the event-key denominator printed. **If one already does, the premise is wrong: file a row, print it, and STOP.**

**(b) THE SCHEDULED PATH IS BIT-FOR-BIT UNCHANGED.** For every marker-free payload shape the schedule can deliver, the command string your code builds is IDENTICAL to the pre-change string -- printed, compared, denominator stated.

**(c) THE SKIP IS NOT INDEPENDENTLY REACHABLE.** With the coupled shape: no event can produce `--no-ladder` without a forcing spec also present. Enumerate adversarial payloads that attempt it -- absent, null, empty, wrong case, nested, string-encoded, and **through `month`, which `W4-S5` proved is a writer** -- and show 0 of N succeed, N printed. **If you took the independent shape, this arm becomes the full writer census by subtraction with N printed instead, and the sign-off carries N.**

**(d) THE FORCING NOW REACHES THE VERDICT, WHICH IS THE WHOLE POINT AND THE THING `EG-s-24` DID NOT PROVE.** Against the SERVED renderer, show that a forcing spec delivered through your command yields `REFUSE` with class C non-zero -- and print the SAME run with the forcing absent yielding `PUBLISH`. **That pair is the arm's own DIFFERENCE CONTROL -- engaged against the SAME run disengaged.** ⛔ It is NOT a positive control and the issuer first wrote it as one: spine v3.13 qualifier 1, landed minutes after this face was cut, is that a POSITIVE control bounds UNDER-FIRING only and never shows what CHANGES when the control is engaged, so it does not discharge v3.12. Corrected here rather than left to read as conformance it would not have earned. ⛔ Spine v3.12: a seam proved to deliver its input is not a seam proved to have an effect, and this arm exists because my `EG-s-24` proved only the first half.

**(e) THE DISCLOSURE IS PRESENT ON THAT RUN.** The `coverage_verdict.json` your forced run produces carries `EG-s-26`'s skip record AND the forcing record. Print the object whole. **This is the arm that proves the ordering held.**

**(f) THE DEPLOY IS REAL AND MATCHES WHAT WAS REVIEWED.** Served `CodeSha256` equals the built zip equals the value the pre-apply plan predicted, on three reads; the zip member byte-equal to `git show HEAD:<path>`; the pre-fix blob as a negative control that does NOT match. Entry OPENED before the apply, CLOSED before the grading reads, with the never-widen sign-off naming the new reachable state in its own words.

**(g) NO SEND, NO INVOKE.** Print the evidence from your own run, with the denominator of what you checked.

⛔ **THE ISSUER'S OWN v3.12/v3.13 CONFORMANCE COUNT FOR THIS FACE, STATED RATHER THAN IMPLIED (qualifier 1 requires naming WHICH arms carry the shape): of `S27-AC1`'s seven arms, exactly ONE -- arm (d) -- carries a DIFFERENCE control.** Arm (b) is an INVARIANCE proof (the scheduled string must NOT move) and arms (c), (f) and (g) are CENSUSES with printed denominators, both of which qualifier 2 makes non-applications rather than gaps. Arm (a) is a premise check and arm (e) reads a single state. **One of seven, and the one is the arm that carries the outcome.** A looser count would have said four and would have been wrong in the direction that flatters the cut.

<criterion id="S27-AC2" cell_refs="EG-s-27" judgment="true"/>
**`S27-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO` at L9: which shape you took and why; what a caller could still do wrong; whether any OTHER caller of `_render_command` exists, censused with a denominator; and **what a driven run under this shape still does NOT exercise**, naming rung 3 and the egress ask explicitly. No verdict.

<expected_criteria>S27-AC1, S27-AC2</expected_criteria>

<paths>
infra/aws/lambda/etfs-reports-orchestrator/
infra/aws/terraform/etfs-reports/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/
org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-27.the-skip-rides-the-forcing.md
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.7, cell `EG-s-27`.
<owned_cells>EG-s-27</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-09 ~22:2xZ, VINTAGE STATED rather than re-run -- WITHIN BUDGET, 5 of 5 carriers, 25 gates armed, ZERO naming ETFS_GUARDRAIL, the daily producers or `opal-data-etfs`. THE VINTAGE HOLDS BECAUSE no schedule or rule in this surface has been created or changed since; the monthly rule's own `Input` was read LIVE under `EG-s-24` at 06:0xZ as `{"mode":"run"}`. BLIND SPOT, stated: this cell changes what a MANUAL invoke of that rule's target can do, which no schedule census can see -- arm (c) and the never-widen sign-off ARE that control.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied; the function runs under its existing role and this order changes no policy.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; arm (c) is adversarial by construction and the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants. `infra/aws/lambda/` is not a `{gold,silver,bronze}` path so rule 13's DS lane does not gate it; rule 14's `.tools/commit-gate.sh` binds on every `.py` edit and NEVER-9 binds the apply to `safe-apply`.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S27-AC1`, `S27-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/ETFS_GUARDRAIL.TO-EG-s-27.the-skip-rides-the-forcing.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), validated with `python .tools/proof-of-spec-check.py <instance> S27-AC1,S27-AC2` BEFORE the complete flip, which you commit yourself.

**MERGE CLOUD INTO YOUR BRANCH BEFORE THE FLIP** -- the issuance commit must be in your ancestry or the grant cannot resolve from HEAD and the flip is an ADD the L6 gate refuses. You hit this on `EG-s-24` and diagnosed it with the untracked-face discriminator; it is named here so it costs you nothing twice. The identity gate is unchanged: `safe-apply` runs `halt-gate-check.sh` FIRST and that file reads only `org/mcp/sessions/$CLAUDE_CODE_SESSION_ID.serial`, so its own printed remedy at `:118` is legitimate.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
