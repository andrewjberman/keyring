# TO ETFS_GUARDRAIL.TO-EG-s-19 -- THE CATCH-UP BRANCH DRIVEN, NOT AWAITED: one served slice archived and deleted on Andrew's own word so a hole exists OLDER than the newest priced partition, then the producer's OWN scheduled-shape fire detects and refills it -- the branch that has never once run in this estate

<to_id>ETFS_GUARDRAIL.TO-EG-s-19</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~5</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: ANDREW-DIRECT ~02:5xZ at the `1.0.0_SA_CTO` terminal, verbatim: *"Call 1, yeah try it but make sure no test run hits aj's email, that is not appropriate."* -- the manufactured hole is APPROVED and the served DELETE has his word, which NEVER-AUTO-DELETE requires and which no seat may supply for him. Relayed 94909; PRD **v0.5** @`7ba9b976b0`; decomposition **v0.3** s.12, cell `EG-s-19`.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.5 | **Decomp cell:** `EG-s-19` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.3, s.12) | **outcome_ref:** FWD-1 (the recovery mechanism, DRIVEN rather than awaited -- Andrew's ~03:0xZ law that no FWD is a wait)

---

## THE CELL

`EG-s-19` -- **THE CATCH-UP BRANCH HAS NEVER RUN, AND IT IS NOT BECAUSE IT IS BROKEN.** `EG-s-17` filled the estate's only real hole (`cottonwood 2026-09-08`) and closed with `CATCHUP-BRANCH-NOT-EXERCISED` printed beside its token, honestly, because that hole was the NEWEST priced partition and `_catchup_missing_dates` skips the newest as `skip_date` (row `W2-S8`). So the recovery path FWD-1 rests on has never once been observed working. Waiting for an organic mid-window hole is exactly the wait Andrew's ~03:0xZ law forbids. **You will make one, on his word, and then make the producer find it by itself.**

⛔ **THE HOLE IS CHOSEN BY MEASUREMENT, NOT BY CONVENIENCE, AND YOU PROVE ALL FOUR PROPERTIES BEFORE YOU DELETE ANYTHING.** The date must be (1) a TRADING day -- `lib/trading_calendar.py`'s `is_trading_day` printed for it, because the estate's own calendar is the frontier (this seat measured that `2026-09-05` reads FALSE, so absence there is CORRECT and it is NOT a candidate); (2) currently PRESENT as a slice for the partner you choose (`head-object`, size and UTC printed); (3) backed by a LIVE upstream partition -- the producer's own non-writing probe (`{"date": d, "probe": true}`) answering `partition: true` and `priced` non-zero, because deleting a slice the producer CANNOT re-derive would leave a hole you cannot heal and would turn a test into damage; and (4) **NOT the newest priced partition**, or `skip_date` skips it and the branch stays unexercised exactly as before. Print all four for the date you take AND for at least one date you rejected, so the choice is visible as a choice.

⛔ **ARCHIVE FIRST. THE DELETE IS ANDREW'S WORD SPENT ONCE AND IT IS NOT REVERSIBLE BY THE BUCKET.** `opal-data-etfs` has versioning DISABLED (measured at this seat 02:0xZ; the same fact as row `W1-S12`), so a delete is final and the ONLY way back is a copy you made first. Before the delete: `copy-object` the slice to `daily/_archive/<partner>/<date>.<UTC>.json` -- a prefix OUTSIDE `daily/<partner>/` so no producer, consumer, census or month-end enumeration can ever see it as a slice -- and record BOTH sha256s, byte-equal. That copy is the rollback and it is named in the entry before the act.

⛔ **THE FIRE IS THE RULE'S OWN SHAPE, AND A `date` KEY WOULD DEFEAT THE WHOLE CELL.** Invoke the producer with the payload the RULE delivers -- EventBridge's default scheduled envelope, which `EG-s-17` measured to be the payload because `Target.Input` is ABSENT on 2 of 2 daily rules -- and **NO `date` key**: a `date` routes to the explicit-date branch at `lambda_function.py:304-308`, which never reaches the catch-up path at all, so a run with one would look like a pass and prove nothing (row `W2-S8`). The catch-up path must FIND the hole itself. That is the entire claim.

⛔ **CLEAR OF ANDREW'S ~02:5xZ CONSTRAINT BY CONSTRUCTION, AND YOU PROVE IT RATHER THAN ASSERT IT.** This cell drives `cot-etf-ownership-daily` (or the 49financial producer if you choose that partner), which writes a slice and mails nobody -- it has no SES call on any path. His standing word is that NO TEST RUN HITS aj@opalinvest.com. So: an arm reads the run window and shows ZERO SES sends of any kind, with a denominator, and the record states that this producer has no mailer at all. **You do not invoke `etfs-reports-orchestrator` under this order, in any mode, for any reason.**

## DELIVERABLE

1. The NEVER-2 entry (opened before, closed and COMMITTED after the act and BEFORE the grading reads -- spine v3.9), naming the slice, its archive copy, both sha256s and the rollback.
2. `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/test_egs19_catchup_driven.py` -- the battery, and `the-catch-up-branch-driven.result.md` -- what you measured, each criterion's invocation and its output verbatim with rc and denominator, the candidate dates you rejected and why, and any row you filed.
3. The proof-of-spec instance (below).

## BOUNDS

- **Your write surface is the `<paths>` block below**, PLUS your own `deliverables/<serial>/` folder and this face's `<status>`. A path you need that it does not name is a BLOCKING row, never an override.
- **EXACTLY ONE SLICE IS DELETED, and only after its archive copy is verified byte-equal.** No second delete for any reason, including a failed restore -- a failed restore is the rollback's job and then a row.
- **NO CODE CHANGE, NO DEPLOY.** The producers run AS DEPLOYED; a defect you find is a BLOCKING row with its measurement, never a hot fix.
- **NEVER invoke `etfs-reports-orchestrator`** (Andrew's ~02:5xZ constraint; its mailer reaches aj@ and the recipient set is the producer's, not yours). **No alarm, monitor, topic or schedule.**
- **EVERY invocation is bounded.** `timeout 120` on reads; `timeout 300` on the producer invoke; poll the restored key at most every 30 s for at most 15 minutes, and a slice still absent at 15 minutes is recorded NOT-RESTORED with the log's own lines, then the ROLLBACK runs.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W5-S<k>` (append; cite `path@commit`; never edit an existing row) -- and you KEEP WORKING.
- **NEVER `git push`.** Report push state as MEASURED (`git ls-remote origin refs/heads/CLOUD`).

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9.

<criterion id="S19-AC1" cell_refs="EG-s-19"><invocation>timeout 900 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/test_egs19_catchup_driven.py</invocation><expect>EGS19-CATCHUP-BRANCH-DRIVEN</expect></criterion>
`S19-AC1` -- a battery you write, printing the token ONLY when every arm holds: (a) THE CHOICE, with its four properties printed for the date taken AND for at least one rejected date -- trading day per `is_trading_day`, slice present with size and UTC, upstream `partition: true` with non-zero `priced` from the producer's own probe, and NOT the newest priced partition (the newest named, so the exclusion is visible); (b) THE ARCHIVE: the copy at `daily/_archive/<partner>/<date>.<UTC>.json` with the source and copy sha256 EQUAL, printed, and the entry OPEN with its opened-at preceding the delete's UTC; (c) THE HOLE EXISTS: `head-object` on the slice returns 404 after the delete, beside a 200 on a neighbouring date as the positive control in the same call sequence; (d) THE FIRE IS THE RULE'S SHAPE: the payload byte-equal to the rule's delivered envelope with NO `date` key (both printed), the request id and UTC recorded, and 1 of 1 `START RequestId` in the producer's log group read BY TIME; (e) **THE BRANCH RAN AND FOUND IT ITSELF**: the invocation's log names the recovered date on the CATCH-UP path -- `catchup_processed` carrying it, the exact line printed -- and NOT merely a main-path write, because a main-path recovery would prove the same thing `EG-s-17` already proved; (f) THE SLICE IS BACK: `head-object` 200 with size and UTC AFTER the fire, its rows counted by a second independent reader as non-zero, and its content compared to the archive with ANY difference NAMED and explained as a re-derivation rather than waved past; (g) NOTHING ELSE MOVED: the partner's slice count before and after are equal (denominator printed) and no other key under `daily/` changed in the window; (h) ZERO SES SENDS of any kind in the run window, with the denominator, and the record stating this producer has no mailer on any path (Andrew's ~02:5xZ constraint, proven not assumed). Denominators on every list; every S3 time UTC via `s3api`.

<criterion id="S19-AC2" cell_refs="EG-s-19" judgment="true"/>
`S19-AC2` -- graded by the CVO at L9: whether the catch-up branch actually recovered a hole it discovered itself (the log's own lines quoted), what the restored slice differs in from the archived original if anything and whether that difference is a faithful re-derivation or a drift, what the branch would have done had the upstream partition been absent, and what this exercise still does not prove about a multi-day or multi-partner gap. Evidence with vintage. NO VERDICT.

<expected_criteria>S19-AC1, S19-AC2</expected_criteria>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.3, cell `EG-s-19`.
<owned_cells>EG-s-19</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-09 ~22:2xZ, its VINTAGE STATED rather than re-run at this issuance -- WITHIN BUDGET, 5 of 5 carriers, 56.25 s of a 90 s default, GATES ARMED 25, REACHED-DENOMINATORS C1=23 C2=6 C3=12 C4=20 C5=335, and ZERO of the 25 armed gates names ETFS_GUARDRAIL, the daily producers or `opal-data-etfs`. THE VINTAGE HOLDS BECAUSE no schedule, rule or gate in this project's surface has been created or changed since that read; the two daily rules were read LIVE at 02:0xZ under `EG-s-18` and are unchanged. BLIND SPOT, stated: the gate ledger cannot see a served DELETE -- Andrew's own word and the archive-first clause ARE that control, and they are named in the accept.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied; the producer runs under its existing role and this order changes no policy.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants. The served objects under `daily/` are not a repo path and are reached only through the acts this face names.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S19-AC1`, `S19-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/ETFS_GUARDRAIL.TO-EG-s-19.the-catch-up-branch-driven.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), validated with `python .tools/proof-of-spec-check.py <instance> S19-AC1,S19-AC2` BEFORE the complete flip, which you commit yourself. Flip only when `S19-AC1` PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
