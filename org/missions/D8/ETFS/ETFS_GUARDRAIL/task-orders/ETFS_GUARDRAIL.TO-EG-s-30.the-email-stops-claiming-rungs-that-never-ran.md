# TO ETFS_GUARDRAIL.TO-EG-s-30 -- THE EMAIL STOPS CLAIMING RUNGS THAT NEVER RAN: a driven run's terminal message asserts the ladder was exhausted and never says the condition was forced

<to_id>ETFS_GUARDRAIL.TO-EG-s-30</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~4</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: row `ETFS_GUARDRAIL-W4-S9`, filed by this order's own assignee and owned by this seat; sequenced ahead of `EG-s-21` by the issuer's call after `1.0.0_SA_CTO`'s `R-EG-9` (`3d8f3d9725`) removed the only other block. Decomposition **v0.10** s.19, cell `EG-s-30`.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.8 | **Decomp cell:** `EG-s-30` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.10, s.19) | **outcome_ref:** FWD-9, FWD-10

---

## THE CELL

You filed this as `W4-S9` while refusing to fire, and you were right to file it. `R-EG-9` has now re-cut FWD-9's ACCEPT off the unobtainable 404, so **nothing stops the driven run except this.**

**WHAT YOU MEASURED:** the terminal message's opening line reads *"could not resolve N date(s) after EVERY RUNG RAN (probe, re-run the producer, re-check)"* -- **on a `--no-ladder` run where `remediate_month` was never called and ZERO rungs ran** -- and **no field of the message says the condition was FORCED.**

⛔ **TWO SEPARATE DEFECTS AND THE FACE TREATS THEM SEPARATELY, because they have different remedies and different evidence.** (1) A POSITIVE FALSE CLAIM: the message states the repair ladder was exhausted when it was never entered. (2) A MISSING DISCLOSURE: nothing tells a reader the condition was manufactured. **The first is a lie the artifact tells; the second is a truth it withholds.** Fixing only the second leaves the message still asserting rungs that did not run.

⛔ **AND THIS IS THE ISSUER'S BLIND SPOT, NAMED AS MINE.** `EG-s-26` put the disclosure requirement on the verdict DOCUMENT. **The EMAIL is the surface FWD-10 names** -- *"Andrew finds out"* -- and I wrote a requirement that stops one layer short of the only artifact a person actually reads. That is R-EG-8's and R-EG-9's shape one grain further out: **a disclosure placed on an indicator of the run rather than on every surface that speaks for it.**

**WHY THIS IS SEQUENCED AHEAD OF THE RUN, and it is my call rather than a ruling:** the driven run sends a REAL EMAIL to a REAL PERSON, and that person is Andrew. **An artifact you cannot un-send is not a place to discover a disclosure gap.** `EG-s-21`'s arm (e) does not require the disclosure, so this costs one cell and buys the only thing in the round that cannot be rolled back.

---

## DELIVERABLE

The changed `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py`, its tests, a battery under `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/`, and the DEPLOY under its own NEVER-2 entry. Every `.py` edit passes `.tools/commit-gate.sh`.

⛔ **YOUR COMMIT MACHINERY CHANGED AT `1d62717c65`:** `safe-commit.sh`, `to-pipeline-gate.py`, `surprise-row-gate.py` and `proof-of-spec-check.py` MODIFIED, new `prd-manifest-gate.py` ADDED and never run on this fabric. **READ GATE OUTPUT, NOT EXIT CODES.** ⚠ And your own row `W4-S12` says `ds-precommit-check.py` FALSE-BLOCKED your last battery on 4 findings with `ruff --target-version py39` clean on identical bytes -- if it fires again, that is the known defect, and it is `1.0.0_SA_CTO`'s. Report it, do not code around it.

---

## BOUNDS

- ⛔ **DO NOT CHANGE WHAT THE MESSAGE REPORTS, ONLY WHAT IT CLAIMS.** The per-date table, the recipients, the routing and the send path are `EG-s-20`'s and are not this cell's subject. You are fixing an assertion and adding a disclosure.
- ⛔ **THE ORGANIC PATH'S WORDING MUST STAY TRUE FOR THE ORGANIC CASE.** On a run where the ladder DID run, "after every rung ran" is correct and must survive. An arm proves it.
- ⛔ **A FIELD PRESENT ONLY ON THE FORCED RUN IS NOT A DISCLOSURE.** It carries an explicit value in BOTH cases, for the same reason `forced:false` had to exist in `EG-s-25`.
- ⛔ **NO SEND AND NO ORCHESTRATOR INVOKE UNDER THIS ORDER.** You build, test hermetically, deploy, and STOP. `EG-s-21`'s single permitted run stays UNSPENT and is not yours to fire under this face.
- ⛔ **DO NOT TOUCH THE RENDERER.** `EG-s-29` is terminal there and its equivalent-ask record is correct.
- Andrew's ~02:5xZ constraint stands: **aj@opalinvest.com is not a recipient of any driven run.**
- Found something off-task? Append a row and KEEP WORKING.

---

## ACCEPTANCE

<criterion id="S30-AC1" cell_refs="EG-s-30"><invocation>timeout 600 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/test_egs30_email_stops_claiming_rungs.py</invocation><expect>EGS30-EMAIL-TELLS-THE-TRUTH-ON-BOTH-BRANCHES</expect></criterion>
**`S30-AC1` -- PASSES BY OUTPUT.** One battery, every number beside its denominator, ending with the token only when all six arms hold.

**(a) BOTH DEFECTS REPRODUCE FIRST, SEPARATELY.** Against the deployed bytes, build the terminal message for a ladder-SKIPPED run and print it whole: show the "after every rung ran" assertion PRESENT, and show a forcing-disclosure token census reading ZERO with a NON-ZERO positive control on a field that does exist. **Two findings, two measurements -- do not fold them into one.** If either is already absent, the premise is wrong: file a row, print it, STOP.

**(b) THE FALSE CLAIM IS GONE ON THE SKIPPED BRANCH -- and the arm says what replaced it.** The message no longer asserts rungs that did not run. Print the new wording verbatim. **It must state what actually happened rather than merely deleting the claim** -- a message that silently omits the ladder is less wrong and still not informative.

**(c) THE ORGANIC BRANCH IS UNCHANGED -- the INVARIANCE arm.** On a run where the ladder DID run, the message is byte-identical to what the deployed bytes produce today, compared as bytes and not as a description. ⛔ **This is the arm that stops the fix breaking the real case.**

**(d) THE DISCLOSURE IS PRESENT ON BOTH BRANCHES WITH AN EXPLICIT VALUE -- the DIFFERENCE control, and the arm that carries the outcome.** Build the message from the SAME inputs forced and unforced; print both; the forced one names the forcing and its run id, the unforced one carries the same field with its not-forced value. Engaged against the same run disengaged.

**(e) A PERSON CAN TELL, AND THE ARM SAYS HOW.** State in one sentence what a reader sees that distinguishes a driven run from a real emergency, quoting the line they would read. ⛔ **A disclosure buried below the per-date table is not one** -- FWD-10's subject is a person finding out, and where it sits is part of whether it works.

**(f) THE DEPLOY IS REAL AND NOTHING ELSE FIRED.** Served `CodeSha256` equal to the built zip on three reads, zip member byte-equal to `git show HEAD:<path>`, pre-fix blob as a negative control that does NOT match, entry OPENED before the apply and CLOSED before the grading reads. ⛔ **Check whether your bytes are ALREADY served before you apply** -- if a prior act landed them the entry closes SUPERSEDED and you do not re-apply (NEVER-2). Print evidence of 0 SES sends, 0 orchestrator invokes, with the denominator of what you checked.

<criterion id="S30-AC2" cell_refs="EG-s-30" judgment="true"/>
**`S30-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO` at L9: whether a person reading the forced message could still mistake it for an organic one and what would remain of that risk; whether any OTHER sentence in the message asserts something a shape-1 run did not do, censused rather than recalled; and whether the disclosure's PLACEMENT survives the way mail clients truncate. No verdict.

⛔ **THE ISSUER'S v3.12/v3.13 CONFORMANCE COUNT, STATED RATHER THAN IMPLIED:** of `S30-AC1`'s six arms, exactly **ONE** carries a DIFFERENCE control -- arm (d), and it is the arm that carries the outcome. Arm (c) is an INVARIANCE proof, arm (a) is a paired census with a positive control, arms (b), (e) and (f) are single-state reads and censuses -- non-applications under v3.13 qualifier 2 rather than gaps.

<expected_criteria>S30-AC1, S30-AC2</expected_criteria>

<paths>
infra/aws/lambda/etfs-reports-orchestrator/
infra/aws/terraform/etfs-reports/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/
org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-30.the-email-stops-claiming-rungs-that-never-ran.md
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.10, cell `EG-s-30`.
<owned_cells>EG-s-30</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: it changes what the MONTHLY rule's target sends, which no schedule census sees; arm (c)'s byte-identical organic branch and the NEVER-2 entry ARE that control.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied; the function runs under its existing role and this order changes no policy.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants. `infra/aws/lambda/` is not a `{gold,silver,bronze}` path so rule 13's DS lane does not gate it; rule 14's `.tools/commit-gate.sh` binds on every `.py` edit and NEVER-9 binds any apply to `safe-apply`.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S30-AC1`, `S30-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/ETFS_GUARDRAIL.TO-EG-s-30.the-email-stops-claiming-rungs-that-never-ran.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), validated with `python .tools/proof-of-spec-check.py <instance> S30-AC1,S30-AC2` BEFORE the complete flip, which you commit yourself.

**MERGE CLOUD INTO YOUR BRANCH BEFORE THE FLIP** if CLOUD advances under you.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
