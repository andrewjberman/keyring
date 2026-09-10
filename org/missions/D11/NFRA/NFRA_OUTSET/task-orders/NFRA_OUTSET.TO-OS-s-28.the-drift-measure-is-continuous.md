# TO NFRA_OUTSET.TO-OS-s-28 -- THE DRIFT MEASURE IS CONTINUOUS AND NEVER HAND-TRIGGERED: Andrew took none of the three shapes because all three kept a once-daily timer

<to_id>NFRA_OUTSET.TO-OS-s-28</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: ANDREW-DIRECT 2026-09-10 ~15:3xZ at the `2.0.0_SA_COO` terminal, recorded verbatim at `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260910_153xZ_DRIFT_IS_CONTINUOUS_NEVER_HAND_TRIGGERED.md` @`c64cc4f345`, and `1.0.0_SA_CTO`'s routing ruling at msg 95321 (CUT IT; the endpoint does NOT move). Decomposition **v0.10** s.33, cell `OS-s-28`.</status>

**Directive:** D11 | **Fabric:** laptop | **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.11 | **Decomp cell:** `OS-s-28` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.10, s.33) | **outcome_ref:** FWD-5

---

## THE CELL

You raised `S38` and `S39`: `OpalOutsetDriftLaptop` was due 11:30Z and DID NOT RUN, its principal is `Interactive`, and the console logon came NINETEEN MINUTES after the due instant -- so the trigger was SKIPPED rather than deferred. You offered three shapes and recommended S4U with its cost exercised. **ANDREW TOOK NONE OF THEM.**

**HIS WORDS, VERBATIM AND ENTIRE, TWO MESSAGES IN ORDER:**

> no this should be a continuously stitched function, maybe every 15 min.

> no hand-drawn anything, no manual trigger anything for something like this

⛔ **THE QUESTION WAS THE WRONG ONE AND THAT IS THE ISSUER'S DEFECT, NOT YOURS.** All three shapes preserve a ONCE-DAILY timer and argue about how to make that single firing land. His answer changes the shape of the thing.

**WHAT IS DEAD.** Moving the trigger to an hour a session reliably exists dies by name -- it makes the cadence depend on a human habit. Accept-and-disclose dies. ⛔ **AND THE CURRENT ARTIFACT'S PROVENANCE DIES**: the reading the estate report serves for this device right now was produced by a HAND-STARTED run, and under his word **a hand-made value that happens to be FRESH still violates the instruction.** S4U is **not adopted either** -- it answered "how does a daily firing survive nobody being logged on", which is not "make this continuous". A logged-out principal may still be an implementation consequence of his design; that is yours to price, not the cut's to impose.

⛔ **TWO THINGS THIS FACE DELIBERATELY DOES NOT RESOLVE, AND NEITHER IS HIS INSTRUCTION.**

**"STITCHED"** is ambiguous between this estate's EXISTING stitch mechanism (the post-commit hook republishing a shared marker from every clone) and plain English for "continuously woven in". `1.0.0_SA_CTO` declined to infer it and so does this seat; it is with Andrew as a question. **Build to the PROPERTY, not to either reading.**

**"MAYBE EVERY 15 MIN" CARRIES HIS OWN HEDGE.** The number is a TARGET. ⛔ **NO ARM OF THIS FACE GRADES ON THE NUMBER**, and none may be added that does until he fixes it.

---

## DELIVERABLE

The changed producer and/or scheduling surface under `infra/aws/ec2/outset-drift-device/`, coverage in its own suite, and a battery plus result document under `org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/`. Every `.py` edit passes `.tools/commit-gate.sh`.

⛔ **YOUR COMMIT MACHINERY CHANGED AT `1d62717c65`**, minutes before this cut: `safe-commit.sh`, `to-pipeline-gate.py`, `surprise-row-gate.py` and `proof-of-spec-check.py` were MODIFIED and a new `prd-manifest-gate.py` was ADDED that has never run on this fabric. **READ GATE OUTPUT, NOT EXIT CODES.** A refusal from the new gate may be the gate working on a fabric that has never exercised it -- file a row and report it, do NOT override it.

---

## THE SHAPE IS YOURS TO CHOOSE AND PRICE

⛔ **THE ISSUER CANNOT RESOLVE HIS "STITCHED" FORK AND WILL NOT PRETEND TO**, so the mechanism is yours the way `EG-s-27`'s coupled-versus-independent choice was its assignee's. Three shapes, each with what it costs:

- **(i) A RECURRING TIMER at roughly quarter-hour.** Simplest. ⛔ **IT INHERITS THE EXACT PROBLEM THAT KILLED THE DAILY FIRING** -- a task principal that only runs while someone is logged on -- so it is not free, and choosing it means solving that too.
- **(ii) PUBLISH ON COMMIT, via the existing hook.** Genuinely continuous while work happens, needs no scheduler and no session, and goes quiet when nobody works. ⛔ **ITS BLIND SPOT IS STRUCTURAL: it measures at the moment uncommitted work is SMALLEST**, so a long stretch nobody commits -- the exact case worth catching -- is the case it cannot see.
- **(iii) BOTH.** On commit, plus a floor at roughly quarter-hour. **THE ISSUER'S PREFERENCE, and the reason is (ii)'s blind spot rather than belt-and-braces.**

**Take another shape if you can state why**, and pay for it with arm (c)'s census and arm (d)'s adversarial arm the same way `EG-s-24` paid.

---

## BOUNDS

- ⛔ **NO HUMAN ACT IN THE STEADY-STATE PATH.** Not a logon, not a hand run, not a "someone kicks it if it looks stale". That is the whole instruction.
- ⛔ **DO NOT HAND-PUBLISH TO MAKE THE CURRENT ARTIFACT FRESH**, not even once, not even to keep the report green while you build. That is the act he forbade, and it would **erase the evidence that the automatic path does not work.** If the reading ages past the consumer's 26 h ceiling before this lands, **THE REPORT SHOULD SAY THIS DEVICE IS SILENT** -- that is the instrument working, not a gap to paper over.
- ⛔ **DO NOT CHANGE WHAT `comp-heat drift` MEASURES.** The question -- *"What has been written in this workspace that is not in any commit?"* -- and its denominators are not this cell's subject. You are changing WHEN and BY WHAT it runs.
- ⛔ **DO NOT WIDEN THE PUBLISHER'S REACH.** The scoped-role assume with a hard exit on failure (`OS-s-21` shape (d), CTO ruling @`054353ac5e`) stands unchanged. Nothing new is stored on the device.
- **A PRINCIPAL CHANGE MAY NEED AN ELEVATED LINE ONLY ANDREW CAN RUN** (`S39`). If your shape needs it, that is a call to surface with the exact line and its one-line rollback -- not a blocker to work around, and not something to route around by choosing a weaker shape silently.
- Found something off-task? Append a row to this project's investigation channel and KEEP WORKING.

---

## ACCEPTANCE

<criterion id="O28-AC1" cell_refs="OS-s-28"><invocation>timeout 600 python org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/test_os28_drift_is_continuous.py</invocation><expect>OS28-DRIFT-PUBLISHES-WITHOUT-A-HUMAN</expect></criterion>
**`O28-AC1` -- PASSES BY OUTPUT.** One battery, every number beside its denominator, ending with the token only when all six arms hold.

**(a) THE DEFECT REPRODUCES FIRST, ON THE LIVE PLANE.** Print the task's principal and its trigger as they stand, the last published artifact's LastModified and its producing trigger, and the interval since. Show the 11:30Z firing did not produce an artifact. **If the world has already changed under you, say so and STOP** -- do not grade against a state that has moved.

**(b) THE PUBLISH HAPPENS WITH NO HUMAN ACT -- the arm that carries the outcome.** Exercise your chosen mechanism and show a NEW artifact version appearing whose production involved no logon, no hand invocation and no interactive session. **Name the instrument that proves the absence of a human act** rather than asserting it -- a VersionId and timestamp alone cannot tell a hand run from an automatic one, which is exactly the defect this cell exists to close.

**(c) THE ARTIFACT SAYS WHICH TRIGGER PRODUCED IT.** A reader of the published artifact can tell an automatic publish from a hand one, from the artifact alone. If the existing `argv` / publisher-ARN fields already carry it, print them and say so; if they do not, add what is needed. ⛔ **A field present only in the automatic case is NOT a disclosure** -- it must carry an explicit value in both, for the same reason `forced:false` had to exist in `ETFS_GUARDRAIL`.

**(d) THE HUMAN PATH CANNOT BE THE STEADY STATE -- the adversarial arm.** Enumerate the ways the publish could still end up depending on a person -- an interactive-only principal, a session-scoped credential, a logon trigger, a device-off window -- and show which your shape closes and which it does not. **Print the denominator.** Any that remain open are named in the result document, not omitted.

**(e) NOTHING ELSE MOVED -- the INVARIANCE arm.** The drift question, its denominators and the scoped-role assume are byte-identical before and after, proven as a comparison rather than asserted. No new credential is stored on the device. The consumer's 26 h ceiling is untouched.

**(f) THE TREE YOU MEASURED IN, AND NO NUMBER-GRADING.** Any census states the tree it ran in with a positive control proving the tool read your own checkout. ⛔ **AND STATE EXPLICITLY THAT NO ARM OF THIS BATTERY GRADES ON THE FIFTEEN-MINUTE NUMBER** -- his word carries "maybe", so the cadence is a target and an arm that fails on 14 or 16 minutes would be grading a constant he never fixed.

<criterion id="O28-AC2" cell_refs="OS-s-28" judgment="true"/>
**`O28-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO` at L9: which shape you took and why, including what you rejected; **whether a reader of the published artifact can distinguish an automatic publish from a hand one, measured on a REAL artifact rather than argued**; what human dependency remains, if any, and what would remove it; and whether your mechanism has a blind spot analogous to the commit-trigger one named in this face. No verdict.

⛔ **THE ISSUER'S v3.12/v3.13 CONFORMANCE COUNT, STATED RATHER THAN IMPLIED:** of `O28-AC1`'s six arms, exactly **ONE** carries a DIFFERENCE control -- arm (b), the publish occurring with and without the human act, and it is the arm that carries the outcome. Arm (c) proves a disclosure in both branches and is closer to a positive control than a difference one. Arm (e) is an INVARIANCE proof; arms (a), (d) and (f) are CENSUSES with printed denominators -- non-applications under v3.13 qualifier 2 rather than gaps.

<expected_criteria>O28-AC1, O28-AC2</expected_criteria>

<paths>
infra/aws/ec2/outset-drift-device/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/
org/missions/D11/NFRA/NFRA_OUTSET/task-orders/NFRA_OUTSET.TO-OS-s-28.the-drift-measure-is-continuous.md
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> v0.10, cell `OS-s-28`.
<owned_cells>OS-s-28</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE at the cut -- but read this qualifier before relying on it: this cell's whole subject IS a schedule, and a schedule census taken at the cut describes the state the cell exists to change. The assignee's arm (a) is the live read that matters, and arm (d) is the control on what it leaves open.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied by this cut; the scoped-role assume is unchanged and a bound forbids widening it. If the chosen shape needs a principal change, that surfaces as a call rather than an act.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; arm (d) is adversarial by construction and the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants. `infra/aws/ec2/` is not a `{gold,silver,bronze}` path so rule 13's DS lane does not gate it; rule 14's `.tools/commit-gate.sh` binds on every `.py` edit.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `O28-AC1`, `O28-AC2`. Instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-28.the-drift-measure-is-continuous.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), validated with `python .tools/proof-of-spec-check.py <instance> O28-AC1,O28-AC2` BEFORE the complete flip, which you commit yourself.
</proof_of_spec>

**REPORT:** to your issuer, once, when the order is terminal.
