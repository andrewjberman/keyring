# TO ETFS_GUARDRAIL.TO-EG-s-29 -- THE LADDER-SKIPPED BRANCH IS A FIFTH WRITER: it builds unresolved records inline with no provider and no egress ask, so the one path that can produce a driven REFUSE is the one path `EG-s-28`'s fix cannot reach

<to_id>ETFS_GUARDRAIL.TO-EG-s-29</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~5</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: `1.0.0_SA_CTO`'s ruling **R-EG-8** at msg 95151, adopting SHAPE (b) -- FIX THE ARTIFACT, DO NOT WEAKEN THE ACCEPT -- on row `ETFS_GUARDRAIL-W1-S33`, which `EG-s-28`'s assignee raised by applying that cell's own law one level above where the issuer placed it. Decomposition **v0.9** s.18, cell `EG-s-29`. RULED ORDERING, not issuer discretion: this cell lands and is PROVEN before `EG-s-21`'s single permitted driven run is spent.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.8 | **Decomp cell:** `EG-s-29` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.9, s.18) | **outcome_ref:** FWD-9, FWD-10

---

## THE CELL

You wrote the disclosure field in `EG-s-25` and the skip record in `EG-s-26`, both in this function. This cell is the third thing that branch must carry, and it is the one that makes the whole shape work.

**THE FINDING IS `W1-S33`, MEASURED BY `EG-s-28`'S ASSIGNEE, NOT ARGUED.** That cell fixed `provider` at 4 of 4 `unresolved.append` sites in `data/etfs/scripts/coverage/remediate.py`. It then asked whether four was the POPULATION rather than merely the list it was handed. It is not. **`render_month_end.py:1000-1008` is a FIFTH WRITER**: on `--no-ladder` the `else:` branch never calls `remediate_month` at all and builds the unresolved records INLINE:

```python
        else:
            ladder_result = {
                "resolved": [], "expected_empty": [],
                "unresolved": [
                    {"date": d, "class": e["class"], "reason": "ladder skipped (--no-ladder)"}
```

Measured hermetically with `boto3` stubbed to raise, so 0 AWS calls occurred: **0 of 2 records carry `provider`**, both rendering `2026-08-04 | cottonwood | (not stated) | C | ladder skipped (--no-ladder)`.

⛔ **SO THE ADOPTED SHAPE DOES NOT GO THROUGH THE PRODUCER `EG-s-28` FIXED.** Shape 1 -- drive the refusal with the ladder skipped -- is the ONLY path that yields a driven REFUSE, and it is exactly the path that bypasses `remediate.py`. **THIS PROJECT HAS NOW PAID FOUR TIMES FOR A FENCE COVERING ONE WRITER OF A PROPERTY** (`W4-S4`, `W4-S5`, `EG-s-24`, and this), and the fourth was found BY THE CELL CUT TO FIX THE THIRD.

**IT BLOCKS `EG-s-21` ON TWO INDEPENDENT ARMS AT ONCE**, which is why this cell exists and why it is sequenced first. Arm (d) needs the ladder's outputs on the refusal branch WITH the egress ask present, and rung 3 -- the SOLE writer of `coverage_egress_ask.json` (`remediate.py:189`, the only `put_object` in that module) -- never fires under `--no-ladder`. Arm (e) fires the terminal send, which is FWD-10, whose ACCEPT (ii) requires each missing day listed *"with its partner AND THE PROVIDER"*. Both fail on the same run for the same structural reason.

⛔ **THE RULING, AND ITS REASON, BECAUSE THE REASON BOUNDS WHAT YOU MAY BUILD.** R-EG-8 refused the cheaper shape -- amending the arm to accept a message naming NO provider -- and its reason is that FWD-10's accept (ii) encodes a real operational property: **an operator reading the terminal alert can tell WHICH PROVIDER FAILED.** Weakening the arm would let FWD-10 grade REALIZED while the property it exists to guarantee is FALSE. That is this project's own row `S16`, cited in CLAUDE.md Rule 24 as a GRADE reading REALIZED on the violation. **An accept that cannot be met by the artifact is evidence about the ARTIFACT.**

**SO: THE ASK MUST BE PRESENT, NOT DISCLOSED-AS-ABSENT.** `EG-s-26` already records that the ladder was skipped and that the ask is absent by construction, and that record STAYS -- it is the honesty half and it is correct. This cell makes the absence stop being true: the skipped branch writes a **rung-3-EQUIVALENT** record. **Same property, different writer.**

---

## DELIVERABLE

The changed `data/etfs/scripts/presentation/render_month_end.py`, coverage in its own suite, and a battery under `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/`. Every `.py` edit passes `.tools/commit-gate.sh`.

⛔ **THE DEPLOY IS IN THIS CELL** -- an `aws s3 cp` to the artifact prefix, because the box pulls this file by key at run time -- under its own NEVER-2 entry opened BEFORE the copy and closed BEFORE the grading reads, naming the exact key and the byte-for-byte rollback. You did this twice already (`EG-s-25`, `EG-s-26`); the same discipline applies, and `EG-s-26`'s entry is the model because it closed SUPERSEDED against a world-done act.

---

## BOUNDS

- ⛔ **DO NOT CHANGE THE VERDICT LOGIC, THE CLASS RULE, OR THE LADDER'S BEHAVIOUR.** You are making the SKIPPED branch carry what the LADDER branch already carries. The `ladder=True` path is not this cell's subject and must not move -- arm (e) proves it did not.
- ⛔ **DO NOT "FIX" THE RE-CLASSIFY AT `:999`.** That is SHAPE 2 and it was REFUSED at R-EG-6 because it rewrites a served daily slice to demonstrate a guard.
- ⛔ **DO NOT INVENT A PROVIDER.** A partner absent from the mapping renders the honest absence marker, never a guess and never `None`. `remediate.py:130`'s `.get(partner, "<no provider mapped>")` is the established shape -- **import or mirror it, do not re-implement a second default**, because a second default is a second writer of the same property and that is the defect this cell exists to close.
- ⛔ **DO NOT TOUCH `data/etfs/scripts/coverage/remediate.py`.** `EG-s-28` is terminal there and its 4 of 4 fix is correct; you READ it to take the mapping and the record shape, and you write nothing to it.
- ⛔ **NO SEND, NO ORCHESTRATOR INVOKE, NO BOX RUN, NO WRITE UNDER `platinum/reports/`.** `EG-s-21`'s single permitted run stays UNSPENT and is not yours to fire.
- Andrew's ~02:5xZ constraint stands: **aj@opalinvest.com is not a recipient of any driven run**, and this cell fires none.
- Found something off-task? Append a row to `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md` and KEEP WORKING.

---

## ACCEPTANCE

<criterion id="S29-AC1" cell_refs="EG-s-29"><invocation>timeout 600 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/test_egs29_skipped_branch_carries_the_property.py</invocation><expect>EGS29-SKIPPED-BRANCH-CARRIES-THE-PROPERTY</expect></criterion>
**`S29-AC1` -- PASSES BY OUTPUT.** One battery, every number beside its denominator, ending with the token only when all seven arms hold. Each arm is one clause.

**(a) THE DEFECT REPRODUCES FIRST, AND THE WRITER POPULATION IS ENUMERATED FROM SOURCE.** Against the renderer as it stands, print the DENOMINATOR of sites that construct an unresolved record ACROSS BOTH FILES -- the renderer's inline branch and `remediate.py`'s four -- found by reading the source, and show which carry `provider` and which do not. **Do not work from this face's list; it is the issuer's and may be stale, and that is exactly how the fifth writer went uncounted.** Then run the skipped branch and show every record lacking the field. **If any already carries it, the premise is wrong: file a row, print it, and STOP.**

**(b) EVERY RECORD ON THE SKIPPED BRANCH NAMES ITS PROVIDER.** After the change, a `--no-ladder` run over a case reaching every record-producing path shows N of N carrying `provider`, denominator printed, with the value equal to what `remediate.py`'s mapping yields for the same partner -- **compared against that module rather than asserted**.

**(c) AN UNMAPPED PARTNER STILL READS AS UNKNOWN -- the arm that stops this becoming a fabrication.** A partner absent from the mapping yields the honest absence marker on the skipped branch, byte-identical to what the ladder branch yields for the same partner. **This is a POSITIVE control in the strict sense: it proves the honest-absence path can still fire.**

**(d) THE EGRESS ASK IS RECORDED FOR THE RUN -- the arm that unblocks `EG-s-21`.** A `--no-ladder` run produces a rung-3-EQUIVALENT ask record, printed whole, carrying per-date partner and provider and the same `authorization` PER-USE semantics rung 3 writes. **Print it beside a real rung-3 ask from an unforced ladder run over the same input and state every field that differs.** ⛔ The record must ALSO say it was written by the skipped branch rather than by rung 3 -- a reader must not mistake an equivalent for the original, which is `EG-s-26`'s own principle applied to this artifact.

**(e) THE LADDER BRANCH DID NOT MOVE -- the INVARIANCE arm.** Re-run a `ladder=True` verdict over the same inputs before and after your change: every class count, the `verdict` value, and the unresolved records byte-identical, denominator printed. **`EG-s-26`'s skip record and `EG-s-25`'s forcing record both still present and unchanged on their respective branches.**

**(f) THE DEPLOY IS REAL AND REVERSIBLE, AND NOTHING ELSE FIRED.** The served object at the artifact key byte-equal to your committed bytes (sha256 both sides, the served copy RE-DOWNLOADED by its new VersionId rather than trusted from the PUT response), the prior object's sha256 and VersionId recorded in the entry BEFORE the copy, rollback stated as an exact restore. ⛔ **Check whether your bytes are ALREADY SERVED BEFORE YOU COPY** -- if a prior act landed them, the entry closes SUPERSEDED and you do NOT re-copy (NEVER-2; a re-execute of an overtaken promote is a REWIND). Print the evidence that no SES call, no Lambda invoke and no write under `platinum/reports/` occurred, with the denominator of what you checked.

**(g) THE TREE YOU MEASURED IN.** Any census in this battery states the tree it ran in, with a POSITIVE CONTROL proving the tool read YOUR worktree -- a file present only on your branch appearing in the hits. ⛔ The comp-rail resolved its corpus from the tool's INSTALL LOCATION until `838b963638` landed on CLOUD, so a worktree-run census silently scanned the MAIN tree and returned a well-formed zero with a real denominator. Your branch should carry the fix; **prove it rather than assuming it** (row `S35`).

<criterion id="S29-AC2" cell_refs="EG-s-29" judgment="true"/>
**`S29-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO` at L9: **whether the rung-3-equivalent record is a FAITHFUL ANALOGUE of what rung 3 itself would have written or merely a record with the same shape**, naming every difference you found in arm (d) rather than implying there are none; whether a person could authorise egress on it as safely as on a real ask; whether any consumer parses either artifact and could be broken by the new field, censused with a denominator rather than recalled; and what a reader still cannot tell from a shape-1 run after this change. No verdict.

⛔ **THE ISSUER'S OWN v3.12/v3.13 CONFORMANCE COUNT, STATED RATHER THAN IMPLIED:** of `S29-AC1`'s seven arms, exactly **TWO** carry a DIFFERENCE control -- arm (b) (skipped branch before and after, the same run engaged and disengaged) and arm (d) (the equivalent record against a real rung-3 ask over the same input), and arm (d) is the one that carries the outcome. Arm (c) is a POSITIVE control in the strict sense and is NOT a difference control. Arm (e) is an INVARIANCE proof, arms (a), (f) and (g) are CENSUSES with printed denominators -- all non-applications under v3.13 qualifier 2 rather than gaps.

<expected_criteria>S29-AC1, S29-AC2</expected_criteria>

<paths>
data/etfs/scripts/presentation/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/
org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-29.the-skipped-branch-carries-the-property.md
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.9, cell `EG-s-29`.
<owned_cells>EG-s-29</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: it replaces a file the MONTHLY schedule's box pulls at run time, which no schedule census can see; the NEVER-2 entry, the archived prior object and arm (e)'s no-movement proof on the LADDER branch ARE that control.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied; the copy runs under the seat's existing credentials to an existing key.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants. `data/etfs/scripts/presentation/` is NOT a `{gold,silver,bronze}` path, so CLAUDE.md rule 13's DS commit lane does not gate it; rule 14's `.tools/commit-gate.sh` binds on every `.py` edit.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S29-AC1`, `S29-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/ETFS_GUARDRAIL.TO-EG-s-29.the-skipped-branch-carries-the-property.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), validated with `python .tools/proof-of-spec-check.py <instance> S29-AC1,S29-AC2` BEFORE the complete flip, which you commit yourself.

**MERGE CLOUD INTO YOUR BRANCH BEFORE THE FLIP** -- the issuance commit must be in your ancestry or the grant cannot resolve from HEAD and the flip is an ADD the L6 gate refuses. This is the issuer's banked hand-off defect and it has now cost this project three separate slots; it is named here so it costs you nothing a third time.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
