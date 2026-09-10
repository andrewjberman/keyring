# TO ETFS_GUARDRAIL.TO-EG-s-26 -- THE ARTIFACT MUST RECORD WHAT WAS *SKIPPED*, NOT ONLY WHAT WAS FORCED: a run that bypasses the remediation ladder and does not say so produces a REFUSE indistinguishable from one the ladder tried and failed to fix

<to_id>ETFS_GUARDRAIL.TO-EG-s-26</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~5</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: `1.0.0_SA_CTO`'s ruling R-EG-6 at 95061 (PRD **v0.7**, commit `9f548bfbc9`) adopting SHAPE 1 on row `ETFS_GUARDRAIL-W4-S6`, with condition (i): *the ladder's absence DISCLOSED ON THE ARTIFACT, in the SAME field family as `forced:true`, so ONE read tells a reader both what was forced and what was SKIPPED.* Decomposition **v0.7** s.16, cell `EG-s-26`.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.7 | **Decomp cell:** `EG-s-26` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.7, s.16) | **outcome_ref:** FWD-9 (the honesty half of the adopted shape)

---

## THE CELL

`EG-s-21` has now been refused THREE times by its assignee, each time correctly, and the third refusal found the reason the first two did not: **the forcing cannot survive the ladder.** `coverage_gate` classifies once from the fixture-mutated in-memory series (`render_month_end.py:991`), and with `ladder=True` -- the only path the orchestrator's fixed `--gate` command takes -- **re-classifies from real S3 at `:999` with no `series=` argument**, its own comment reading *"never the in-memory series the ladder itself bypassed"*. Measured hermetically with the arm's own positive control, identical fixture and month and probe, the only difference being the flag:

```
ladder=False -> VERDICT REFUSE   C=1  holes ['2026-08-04']
ladder=True  -> VERDICT PUBLISH  C=0  holes []
```

**The CTO adopted SHAPE 1: drive the refusal with the ladder SKIPPED.** It refused SHAPE 2 -- fixing the re-classify so the ladder runs for real -- at its own seat and did not send it to Andrew, because that shape rewrites a SERVED daily slice to demonstrate a guard, which is the `W1-S24` harm by design and a bad trade when a sufficient non-destructive proof exists.

⛔ **YOUR CELL IS THE HONESTY HALF, AND IT IS WHAT MAKES SHAPE 1 LEGITIMATE RATHER THAN A SHORTCUT.** A run that skips the ladder and does not say so produces a `REFUSE` **indistinguishable from one where the ladder ran, tried every rung, and could not close the hole.** Those are different facts about the world and a reader must be able to tell them apart from the artifact alone. This is the same principle your own `EG-s-25` established for forcing, applied to the second thing a driven run conceals.


⛔⛔ **AND THE SKIP IS WIDER THAN "THE LADDER", WHICH `0.9.0_WK_ETFS_GUARDRAIL~4` FOUND BY CHECKING A BOUNDARY THE
ISSUER DREW TOO NARROWLY.** `--no-ladder` does not merely bypass the repair attempt: the `else:` branch at
`:1000-1008` **never calls `remediate_month` at all** and builds `ladder_result` inline with every rung zero. So
**RUNG 3 NEVER FIRES** -- and rung 3 is not a repair. `remediate.py:24` calls it *"STOP AND ASK A PERSON ... A
DIFFERENT ACTOR"* and `:38` says it *"writes an ASK, never a value, and is a STOP by construction"*. It has exactly
ONE call site, `remediate.py:284`, inside the function the flag skips, and it is the **SOLE WRITER** of
`coverage_egress_ask.json` (`:189`, the only `put_object` in a module whose docstring says rungs 1-2 never write to
S3).

**SO A `--no-ladder` RUN SILENTLY PRODUCES ONE FEWER ARTIFACT THAN THE ORGANIC RUN IT STANDS FOR**, and it reaches
FWD-10's own content: `_build_terminal_email` emits the *"Egress ask (per-use only...)"* block and the
*"Authorization:"* line only `if ask and ask.get('asks')`. The send still fires, so FWD-10 stays provable -- but the
message a person receives is materially thinner than the organic one, **with nothing on the artifact saying that
absence was structural.** That is precisely the indistinguishability this cell exists to close, one level deeper
than the issuer specified.

**THE MECHANISMS ARE NOT UNPROVEN AND THE RECORD SHOULD SAY SO RATHER THAN IMPLY A HOLE:** rung 1's producer invoke
was driven against a REAL hole by `EG-s-19` under Andrew's explicit approval, and **rung 3's stop-and-ask was
exercised on the REAL September run** -- `platinum/reports/2026-09/coverage_egress_ask.json`, 1,017 B, LastModified
`2026-09-10T01:20:20Z`, written beside `coverage_unresolved.json` and `coverage_verdict.json` at the same second
(measured at the issuer's seat). **What shape 1 removes from the DRIVEN run is the CO-PRESENCE of the three
artifacts in ONE run -- not any mechanism.** Your disclosure is what makes that difference legible.

**PUT IT IN THE SAME FIELD FAMILY AS `forced`.** The CTO's condition is that ONE read tells a reader both what was forced and what was skipped -- not two fields in two places a reader must know to join.

---

## DELIVERABLE

The changed `data/etfs/scripts/presentation/render_month_end.py`, coverage in its own suite, and a battery under `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/`. Every `.py` edit passes `.tools/commit-gate.sh`.

⛔ **THE DEPLOY IS IN THIS CELL** -- an `aws s3 cp` to the artifact prefix, because the box pulls this file by key at run time (`lambda_function.py:348`) -- under its own NEVER-2 entry opened BEFORE the copy and closed BEFORE the grading reads, naming the exact key and the byte-for-byte rollback. You did exactly this on `EG-s-25`; the same discipline applies.

---

## BOUNDS

- ⛔ **DO NOT CHANGE THE VERDICT LOGIC OR THE LADDER'S BEHAVIOUR.** `:963`'s class-C rule and the `ladder` branch at `:993-:999` are not this cell's subject. You are adding a RECORD of what the run did, never changing what it does. **In particular: do NOT "fix" the re-classify at `:999` -- that is SHAPE 2 and it is REFUSED.**
- ⛔ **DO NOT TOUCH `infra/aws/lambda/etfs-reports-orchestrator/`** -- that is `EG-s-27`'s surface, live on `0.9.0_WK_ETFS_GUARDRAIL~4` in parallel.
- ⛔ **NO SEND, NO ORCHESTRATOR INVOKE, NO BOX RUN, NO WRITE UNDER `platinum/reports/`.** The one driven run belongs to `EG-s-21` and stays unspent.
- Andrew's ~02:5xZ constraint stands: **aj@opalinvest.com is not a recipient of any driven run**, and this cell fires none.
- Found something off-task? Append a row to `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md` and KEEP WORKING.

---

## ACCEPTANCE

<criterion id="S26-AC1" cell_refs="EG-s-26"><invocation>timeout 600 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/test_egs26_artifact_records_the_skip.py</invocation><expect>EGS26-SKIP-DISCLOSED-IN-ONE-READ</expect></criterion>
**`S26-AC1` -- PASSES BY OUTPUT.** One battery, every number beside its denominator, ending with the token only when all six arms hold. Each arm is one clause.

**(a) THE ABSENCE REPRODUCES FIRST, ON THE DEPLOYED BYTES.** Against the renderer as currently served, show the object carries NO record of whether the ladder ran -- a token census with its denominator, beside NON-ZERO positive controls on the fields that DO exist (`forced`, `mechanism`, `verdict`). **If a skip record already exists, the premise is wrong: file a row, print it, and STOP.**

**(b) A LADDER-SKIPPED RUN SAYS SO, AND NAMES WHAT THE SKIP COST.** With the ladder disabled, the written `coverage_verdict.json` records that it was skipped, why, **and that RUNG 3 DID NOT RUN so `coverage_egress_ask.json` IS ABSENT BY CONSTRUCTION** -- printed whole. A reader must not have to know that the flag implies the missing artifact.

**(c) A LADDER-RAN RUN SAYS SO TOO, AND THE TWO ARE TEXTUALLY DIFFERENT.** Print both objects side by side. ⛔ **A field present only in the skipped case is NOT a disclosure** -- it must carry an explicit ran-value, for the same reason `forced:false` had to exist.

**(d) ONE READ, NOT TWO.** Show the skip record and the `forced` record are in the SAME field family, and state in one sentence how a reader gets both without knowing to join two places. This is the CTO's condition (i) and it is the arm that carries it.

**(e) THE VERDICT DID NOT MOVE.** Re-compute a verdict over the same inputs before and after your change and show every class count and the `verdict` value identical, denominator printed, on BOTH ladder branches.

**(f) THE DEPLOY IS REAL AND REVERSIBLE, AND NOTHING ELSE FIRED.** The served object at the artifact key byte-equal to your committed bytes (sha256 both sides), the prior object's sha256 and VersionId recorded in the entry BEFORE the copy, rollback stated as an exact restore. Print the evidence that no SES call, no Lambda invoke and no write under `platinum/reports/` occurred, with the denominator of what you checked.

<criterion id="S26-AC2" cell_refs="EG-s-26" judgment="true"/>
**`S26-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO` at L9: the field's shape and why a reader can trust it; whether any consumer parses `coverage_verdict.json` and could be broken by another new key, censused with a denominator rather than recalled; and **what a reader still cannot tell from the artifact after this change** -- name the residual rather than implying there is none. No verdict.

<expected_criteria>S26-AC1, S26-AC2</expected_criteria>

<paths>
data/etfs/scripts/presentation/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/
org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-26.the-artifact-records-what-was-skipped.md
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.7, cell `EG-s-26`.
<owned_cells>EG-s-26</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: it replaces a file the MONTHLY schedule's box pulls at run time, which no schedule census can see; the NEVER-2 entry, the archived prior object and arm (e)'s no-movement proof on BOTH ladder branches ARE that control.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied; the copy runs under the seat's existing credentials to an existing key.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants. `data/etfs/scripts/presentation/` is NOT a `{gold,silver,bronze}` path, so CLAUDE.md rule 13's DS commit lane does not gate it; rule 14's `.tools/commit-gate.sh` binds on every `.py` edit.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S26-AC1`, `S26-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/ETFS_GUARDRAIL.TO-EG-s-26.the-artifact-records-what-was-skipped.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), validated with `python .tools/proof-of-spec-check.py <instance> S26-AC1,S26-AC2` BEFORE the complete flip, which you commit yourself.

**YOUR BRANCH ALREADY CARRIES THIS FACE'S ANCESTRY REQUIREMENT AND YOU KNOW WHY:** the issuance commit must be IN your branch before the flip, or the grant cannot resolve from HEAD and the flip is an ADD the L6 gate refuses. Merge CLOUD as you did for `EG-s-25` -- that is the issuer's hand-off defect, banked, and it is named here so you do not hit it a second time.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
