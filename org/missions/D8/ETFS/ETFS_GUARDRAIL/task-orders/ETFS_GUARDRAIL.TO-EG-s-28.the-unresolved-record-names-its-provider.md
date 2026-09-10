# TO ETFS_GUARDRAIL.TO-EG-s-28 -- THE UNRESOLVED RECORD MUST NAME ITS PROVIDER: the terminal alert renders "(not stated)" for EVERY row in EVERY run, organic or driven, because the field the message needs is never written into the artifact it reads

<to_id>ETFS_GUARDRAIL.TO-EG-s-28</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete -- S28-AC1 PASSES BY OUTPUT (rc=0, 6 of 6 arms, 0 failed assertions, token EGS28-EVERY-UNRESOLVED-NAMES-ITS-PROVIDER); S28-AC2 RECORDED for L9 and not self-graded; proof-of-spec instance VALID (rc=0, 6 of 6 artifact rows CONTENT-resolved at 7e544cb4d7, surprises limb resolves W1-S33). Flipped by 0.9.0_WK_ETFS_GUARDRAIL~1. Was: pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: `1.0.0_SA_CTO`'s ruling **R-EG-7** at 95077 (PRD **v0.8**, commit `f89616279c`), which found the collision by reading `_build_terminal_email` after this seat's boundary correction sent it to the builder. Decomposition **v0.8** s.17, cell `EG-s-28`.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.8 | **Decomp cell:** `EG-s-28` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.8, s.17) | **outcome_ref:** FWD-10

---

## THE CELL

FWD-10's ACCEPT (ii) requires the terminal message to list each missing day *"with its partner AND THE PROVIDER the data should have come from"*. **It cannot, and it never could -- in ANY run, organic or driven.** `_build_terminal_email`'s own comment at `lambda_function.py:348` is the finding:

```
# `provider` is NOT written by the producer into coverage_unresolved.json
# (only coverage_egress_ask.json carries it) -- render the absence as text
# rather than the literal "None" a bare .get() puts into an urgent email.
```

So the per-date table's provider column renders **`(not stated)` in every case**, and the ONLY place a provider is ever named is the rung-3 ask block, gated on `if ask and ask.get("asks")` -- which the adopted shape-1 driven run removes by construction. **Under shape 1 the terminal message names NO PROVIDER ANYWHERE.**

⛔ **THE CTO RULED THAT THE ACCEPT IS RIGHT AND DOES NOT MOVE: FIX THE ARTIFACT.** A person receiving an URGENT alert about unrecoverable data should be told which provider it should have come from -- that is the point of telling them at all. This is deliberately NOT an accept amendment and NOT a reason to reconsider the shape the CTO refused.

**WHERE IT BELONGS, MEASURED AT THE ISSUER'S SEAT RATHER THAN INFERRED FROM THE RULING'S WORDING.** The renderer does not build these records -- it copies them: `render_month_end.py:1017` assigns `any_unresolved[p] = ladder_result["unresolved"]` and `:1138` uploads the result. The records are built in **`data/etfs/scripts/coverage/remediate.py`, inside `remediate_month`, at FOUR SEPARATE `unresolved.append(...)` SITES: `:240`, `:248`, `:261`, `:272`.** None carries `provider`. The mapping already exists at `:60` (`_PROVIDER_BY_PARTNER`) and is read at `:130` -- **but only inside `rung3_stop_and_ask`**, which is why the ask has it and the unresolved record does not.

⛔ **FOUR SITES IS THE POINT OF THIS CELL, NOT A DETAIL.** A fix that reaches three of them produces an artifact where SOME dates name a provider and some render the absence, which is worse than the uniform absence today -- a reader cannot tell "this provider is unknown" from "this code path forgot". **This project has now paid three times for a fence that covered one writer of a property** (`W4-S4`, `W4-S5`, and my own `EG-s-24`), and the assignee's own sentence is the standing law: **a fence on ONE WRITER of a property is not a fence on the PROPERTY.** Enumerate the sites from the source with a printed denominator; do not work from this face's list, which is the issuer's and could be stale.

---

## DELIVERABLE

The changed `data/etfs/scripts/coverage/remediate.py`, permanent coverage in `data/etfs/scripts/coverage/tests/test_remediate.py`, and a battery under `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/`. Every `.py` edit passes `.tools/commit-gate.sh`.

---

## BOUNDS

- ⛔ **DO NOT INVENT A PROVIDER.** A partner with no mapping must still render an honest absence. The existing `.get(partner, "<no provider mapped>")` default at `:130` is the shape; arm (c) is its control and it is the arm that keeps this fix from becoming a fabrication.
- ⛔ **DO NOT TOUCH THE RENDERER OR THE ORCHESTRATOR.** `data/etfs/scripts/presentation/` is `EG-s-26`'s LIVE surface on `~5` and `infra/aws/lambda/etfs-reports-orchestrator/` is `EG-s-27`'s LIVE surface on `~4`. You change one file in a package whose last order is terminal, and you read the other two without writing to them.
- ⛔ **DO NOT CHANGE THE LADDER'S BEHAVIOUR OR THE ASK.** Rungs 1-2 still never write to S3; rung 3's own record is already correct and is not this cell's subject. You are adding a field to records that already exist.
- ⛔ **THIS CELL DEPLOYS NOTHING** and writes NO served key. Arm (e) measures the deployed-vs-built gap rather than closing it -- and note `S33`/`S34`: an upload to the artifact prefix does not reach the box, so a deploy claim here would be false twice over.
- ⛔ **NO SEND, NO INVOKE, NO EGRESS.** Andrew's ~02:5xZ constraint stands and this cell cannot violate it; arm (f) proves that from your run.
- Found something off-task? Append a row to `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md` and KEEP WORKING.

---

## ACCEPTANCE

<criterion id="S28-AC1" cell_refs="EG-s-28"><invocation>timeout 300 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/test_egs28_unresolved_names_its_provider.py</invocation><expect>EGS28-EVERY-UNRESOLVED-NAMES-ITS-PROVIDER</expect></criterion>
**`S28-AC1` -- PASSES BY OUTPUT.** One battery, every number beside its denominator, ending with the token only when all six arms hold. Each arm is one clause.

**(a) THE DEFECT REPRODUCES FIRST, AND THE SITE COUNT IS ENUMERATED FROM SOURCE.** Against `remediate.py` as it stands, print the DENOMINATOR of `unresolved.append` sites found by reading the file, and show that 0 of them carry `provider`. Then run the ladder to produce an `unresolved` list and show every entry lacks the field. **If any already carries it, the premise is wrong: file a row, print it, and STOP.**

**(b) EVERY SITE IS FIXED, NOT SOME.** After the change, the same enumerated denominator reads N of N carrying `provider`, and a ladder run over a case that reaches EVERY branch shows every entry carrying it. **Name which branch each site serves so a reader can see the coverage rather than trust the count.**

**(c) AN UNKNOWN PROVIDER STILL READS AS UNKNOWN -- THE ARM THAT STOPS THIS BECOMING A FABRICATION.** A partner absent from `_PROVIDER_BY_PARTNER` yields the honest absence marker, not a guess and not `None`, printed. This is a POSITIVE control in the strict sense: it proves the honest-absence path can still fire.

**(d) THE TERMINAL MESSAGE NOW NAMES A REAL PROVIDER -- THE DIFFERENCE CONTROL, AND THE ARM THAT CARRIES THE OUTCOME.** Build the terminal message from a `coverage_unresolved.json` produced BEFORE your change and one produced AFTER, same dates and same partners, and print both provider columns: the first renders `(not stated)` for every row, the second renders the real provider. ⛔ **Engaged against the SAME input disengaged** -- spine v3.12/v3.13: a positive control bounds under-firing only and would not show this.

**(e) NOTHING ELSE MOVED, AND THE DEPLOY GAP IS MEASURED NOT CLOSED.** Re-run `data/etfs/scripts/coverage/tests/test_remediate.py` by its own path printing rc and counts BEFORE and AFTER; show the ask's own record unchanged; and print `DEPLOYED != BUILT` as a measured sha256 pair with the sentence that an artifact-prefix upload does not reach the box (`S33`/`S34`).

**(f) NO SEND, NO INVOKE, NO EGRESS.** Print the evidence from your own run with the denominator of what you checked.

<criterion id="S28-AC2" cell_refs="EG-s-28" judgment="true"/>
**`S28-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO` at L9: whether any consumer parses `coverage_unresolved.json` and could be broken by a new key, censused with a denominator rather than recalled; whether the provider a record now names is the one the data would ACTUALLY have come from or merely the one the mapping asserts, and how a reader could tell; and what a reader still cannot learn from the message after this change. No verdict.

⛔ **THE ISSUER'S OWN v3.12/v3.13 CONFORMANCE COUNT, STATED RATHER THAN IMPLIED:** of `S28-AC1`'s six arms, exactly **ONE** carries a DIFFERENCE control -- arm (d), and it is the arm that carries the outcome. Arm (c) is a POSITIVE control in the strict sense (it bounds under-firing of the honest-absence path) and is NOT a difference control. Arms (a) and (b) are CENSUSES with printed denominators, arm (e) is an INVARIANCE proof plus a census, and arm (f) is a census -- all non-applications under v3.13 qualifier 2 rather than gaps.

<expected_criteria>S28-AC1, S28-AC2</expected_criteria>

<paths>
data/etfs/scripts/coverage/remediate.py
data/etfs/scripts/coverage/tests/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/
org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-28.the-unresolved-record-names-its-provider.md
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.8, cell `EG-s-28`.
<owned_cells>EG-s-28</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger; it edits one library module and runs a local battery. BLIND SPOT, stated: the changed module is pulled by the reporter box, but this cell deploys nothing and arm (e) MEASURES that gap rather than closing it.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied; no policy, role or trust document is read or written.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants. `data/etfs/scripts/coverage/` is NOT a `{gold,silver,bronze}` path, so CLAUDE.md rule 13's DS commit lane does not gate it; rule 14's `.tools/commit-gate.sh` binds on every `.py` edit.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S28-AC1`, `S28-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-28.the-unresolved-record-names-its-provider.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), validated with `python .tools/proof-of-spec-check.py <instance> S28-AC1,S28-AC2` BEFORE the complete flip, which you commit yourself.

**MERGE CLOUD INTO YOUR BRANCH BEFORE THE FLIP.** Your branch is `wk-etfs_guardrail-2-1` and was cut before this face existed, so the grant cannot resolve from HEAD until the issuance commit is in your ancestry and the flip would be an ADD the L6 gate refuses. That is the issuer's banked hand-off defect; it cost two sibling seats a blocked flip tonight and it is named here so it costs you none.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
