# TO ETFS_GUARDRAIL.TO-EG-s-31 -- THE BOX RUNS THE PACKAGE ITS RENDERER EXPECTS: a self-heal keyed on PRESENCE cannot see STALENESS, and three cells verified three files that were each current

<to_id>ETFS_GUARDRAIL.TO-EG-s-31</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~4</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>pending -- GO paired at cut (a worker order is dispatched by its spawn). Authority: BLOCKING row `ETFS_GUARDRAIL-W4-S17`, filed by this order's own assignee while REFUSING to spend the round's single permitted driven run, and owned by this seat as its `disarm_owner`. `EG-s-21` is OPEN and its `S21-AC1` is FAIL; this cell is what makes it fireable. Decomposition **v0.11** s.20, cell `EG-s-31`.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.8 | **Decomp cell:** `EG-s-31` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.11, s.20) | **outcome_ref:** FWD-9, FWD-10

---

## THE CELL

You refused to fire and you were right. This cell removes the reason.

**WHAT YOU MEASURED.** The served renderer calls `remediate._provider_for(p)` at `render_month_end.py:1162`, on the `--no-ladder` branch -- the ONLY branch that yields a driven REFUSE under `R-EG-6` shape 1. The `coverage` package the box holds does not define it: `s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/coverage/remediate.py` is **11011 B at 2026-09-05T06:53:44Z**, repo **16550 B**. Exercised, not argued: the DEPLOYED package raises `AttributeError` inside `coverage_gate` before a verdict exists; the REPO package returns `VERDICT: REFUSE holes=1 C=1`. **The issuer re-derived your provenance claim with a different instrument** -- `git log -S'_provider_for' -- data/etfs/scripts/coverage/remediate.py` returns exactly one commit, `7e544cb4d7` at `2026-09-10 12:33:05Z`, five days after the deployed artifact.

⛔ **AND THE MECHANISM IS WORSE THAN A MISSED UPLOAD, WHICH IS WHY THIS IS A CELL AND NOT A CHORE.** Read the self-heal at `render_month_end.py:118-129`:

```python
try:
    from coverage import classifier, remediate
except ImportError:
    ... aws s3 cp --recursive s3://.../coverage/ <dest>/ ...
```

**IT IS KEYED ON `ImportError` -- ON PRESENCE, NOT ON CURRENCY.** A box holding a STALE-BUT-IMPORTABLE package imports cleanly, so the bootstrap NEVER FIRES, and the failure surfaces as an `AttributeError` deep in the call path instead of as a missing module at import. **A self-heal that cannot distinguish "absent" from "old" heals exactly one of the two and is silent about the other.**

⛔ **THE SHAPE, NAMED BECAUSE IT IS THE ROUND'S LESSON.** `EG-s-29` verified the served RENDERER. `EG-s-30` verified the served ORCHESTRATOR. `EG-s-21`'s prior execution verified its own surface. **ALL THREE WERE RIGHT AND EVERY PER-MEMBER ARM PASSED.** The renderer is not self-contained -- it imports `coverage.classifier` and `coverage.remediate` from a package the box holds SEPARATELY, and no per-file check could see it. That is CLAUDE.md Rule 22's shared-dependency blindness, and this is the cleanest instance the estate has produced.

---

## THE PROPERTY THIS CELL MUST MAKE TRUE

⛔ **NAMED AS A PROPERTY, NOT AS AN ACT, BECAUSE AN ACT IS ONE WRITER OF IT:**

> **The box executes a `coverage` package whose symbols satisfy the renderer artifact it will actually run -- and that agreement is PROVEN BY EXERCISING THE CALL PATH, never by an upload receipt.**

**AN UPLOAD IS NOT THE PROPERTY.** `aws s3 cp` returning 0 proves an object moved; it proves nothing about what the box imports. **A `head-object` ETag match is not the property either** -- it compares the artifact to your local file, not the box to the artifact.

---

## THE SHAPE IS YOURS TO CHOOSE AND PRICE

Three shapes, with what each costs. **Take another if you can state why.**

- **(i) UPLOAD + FORCE THE RE-PULL BY REMOVING THE BOX-SIDE DIRECTORY.** Makes the existing `ImportError` branch fire as designed. ⛔ **Needs the box RUNNING and an SSM command, and it is a DELETE on a box** -- name what you remove and prove it is the vendored copy and not something else.
- **(ii) UPLOAD + MAKE THE SELF-HEAL CURRENCY-AWARE** so a stale package refreshes itself. **This is the only shape that fixes the CLASS rather than this instance.** ⛔ **AND IT TOUCHES `render_month_end.py`, WHICH IS `EG-s-29`'s TERMINAL SURFACE.** That is not forbidden, but it is a re-cut of a closed cell's file and it needs THIS SEAT'S WORD IN WRITING before you edit -- file a row naming the change you want and STOP on that limb; do not take it on your own reading.
- **(iii) UPLOAD ONLY, and prove the box picks it up by some path you can name.** ⚠ **The issuer's read is that this SHAPE DOES NOT WORK** given `:118-129`, and offering it is deliberate: if you can show it does, that finding is worth more than the cell.

**THE ISSUER'S PREFERENCE IS (i) FOR THIS ROUND AND (ii) AS A SEPARATE FUTURE CELL** -- fix the instance now under an open blocking row, and fix the class where it can be graded on its own evidence rather than as a rider.

---

## BOUNDS

- ⛔ **NO DRIVEN RUN UNDER THIS ORDER.** `EG-s-21`'s single permitted run stays UNSPENT and is not yours to fire here. You prove the CALL PATH resolves; you do not exercise the refusal.
- ⛔ **STOPPING AN EC2 IS A HUMAN-CONFIRMATION ACT (CLAUDE.md).** Starting the box is ordinary; **stopping it afterwards is NOT yours.** If your shape starts the box, LEAVE IT RUNNING and say so loudly in the report with the instance id -- do not stop it, and do not treat leaving it running as a defect you must fix.
- ⛔ **NEVER-AUTO-DELETE remains absolute for S3.** No S3 delete under this order. A box-side filesystem removal under shape (i) is NOT an S3 delete, and the distinction is yours to state explicitly in the entry.
- ⛔ **NO EDIT TO `render_month_end.py` WITHOUT THIS SEAT'S WRITTEN WORD** (shape (ii) above). A row and a stop, not an edit.
- **NEVER-2:** a deploy opens an entry naming the act's BLAST RADIUS on EITHER branch before the act, closed and COMMITTED before the grading reads.
- Andrew's constraint stands: **aj@opalinvest.com is not a recipient of any run.**
- Found something off-task? Append a row and KEEP WORKING.

---

## DELIVERABLE

The deploy, its NEVER-2 entry, a battery and a result document under `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/`, and the proof-of-spec instance. Every `.py` edit passes `.tools/commit-gate.sh`.

⚠ **YOUR OWN DIFFERENCE CONTROL FROM `EG-s-21` IS THE ACCEPTANCE INSTRUMENT AND IT ALREADY DISCRIMINATES** -- `.scratch/exercise_provider_for.py`. Re-establish it in this order's deliverables rather than reaching into a torn-down worktree.

---

## ACCEPTANCE

<criterion id="S31-AC1" cell_refs="EG-s-31"><invocation>timeout 900 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/test_egs31_box_package_matches_renderer.py</invocation><expect>EGS31-THE-BOX-RUNS-THE-PACKAGE-THE-RENDERER-EXPECTS</expect></criterion>
**`S31-AC1` -- PASSES BY OUTPUT.** One battery, every number beside its denominator, token only when all five arms hold.

**(a) THE DEFECT REPRODUCES FIRST, ON THE DEPLOYED ARTIFACT, BEFORE ANY ACT.** The served renderer over the CURRENTLY deployed `coverage` package raises `AttributeError: ... has no attribute '_provider_for'`, printed verbatim, beside the REPO package returning `VERDICT: REFUSE holes=1`. ⛔ **If it does NOT reproduce, the premise moved: file a row, print it, STOP** -- do not proceed to fix a thing that is already fixed (NEVER-2's supersede limb).

**(b) THE ARTIFACT PREFIX CARRIES THE CURRENT PACKAGE -- and the arm prints the DENOMINATOR of what it uploaded.** Every `.py` under the prefix listed with size and UTC before and after, and each compared to its repo counterpart BY CONTENT (sha256), never by filename. **State how many files the package has and how many you moved; if those numbers differ, say why.**

**(c) THE BOX IMPORTS THE NEW SYMBOL -- the arm that carries the outcome, and it is an EXERCISE not a receipt.** On the box, through the same entry point a run uses, resolve `remediate._provider_for` and show it PRESENT. ⛔ **A successful `s3 cp`, an ETag match, or a directory listing DO NOT SATISFY THIS ARM.** Print what you ran ON THE BOX and its raw output.

**(d) THE CALL PATH NOW RETURNS A VERDICT INSTEAD OF RAISING -- the DIFFERENCE control.** The same `--no-ladder` code path that raised in arm (a), re-run against the box's package after the act, returns `VERDICT: REFUSE holes=1` for spec `cottonwood:2026-08-14`. **Same code, same spec, before and after, printed both times.**

**(e) NOTHING ELSE MOVED, AND THE BOX'S POWER STATE IS REPORTED AS A MEASURED VALUE.** Enumerate every key written with size and UTC; zero S3 deletes; zero SES sends; zero orchestrator invokes. **Print the instance id and its state at the end of your run** -- if you started it, say so and say it is still running and that stopping it is Andrew's act, not a defect.

<criterion id="S31-AC2" cell_refs="EG-s-31" judgment="true"/>
**`S31-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO` at L9: which shape you took and what you rejected; **whether any OTHER shared dependency of the renderer is in the same condition, censused rather than recalled** -- the package has more than one module and this cell was found through one symbol; and whether a currency-aware self-heal (shape (ii)) would have prevented this class, with what it would cost. No verdict.

⛔ **THE ISSUER'S CONFORMANCE COUNT, STATED:** of `S31-AC1`'s five arms, **ONE** carries a DIFFERENCE control -- arm (d), and it is the arm that carries the outcome. Arm (a) is a paired reproduction with both sides printed, arm (c) is a single-state EXERCISE (deliberately, because the property is what the box does), arms (b) and (e) are censuses. Non-applications under v3.13 qualifier 2, not gaps.

<expected_criteria>S31-AC1, S31-AC2</expected_criteria>

<paths>
data/etfs/scripts/coverage/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/
org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-31.the-box-runs-the-package-its-renderer-expects.md
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.11, cell `EG-s-31`.
<owned_cells>EG-s-31</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: it changes what the MONTHLY rule's renderer will import on its next fire, which no schedule census sees; arm (d)'s difference control on the real call path IS that control.
comp-iam: DECLARED-NOT-APPLICABLE at the cut -- nothing granted and nothing applied; the upload uses the existing artifact-bucket path and the box its existing role. If the chosen shape needs a grant, that surfaces as a row with the exact line, not as an act.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants. `data/etfs/scripts/coverage/` is NOT a `{gold,silver,bronze}` path so rule 13's DS lane does not gate it; rule 14's `.tools/commit-gate.sh` binds on every `.py` edit; NEVER-9 binds any apply to `safe-apply`.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S31-AC1`, `S31-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~4/ETFS_GUARDRAIL.TO-EG-s-31.the-box-runs-the-package-its-renderer-expects.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), validated with `python .tools/proof-of-spec-check.py <instance> S31-AC1,S31-AC2` BEFORE the complete flip, which you commit yourself.

**MERGE CLOUD INTO YOUR BRANCH BEFORE THE FLIP** if CLOUD advances under you.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
