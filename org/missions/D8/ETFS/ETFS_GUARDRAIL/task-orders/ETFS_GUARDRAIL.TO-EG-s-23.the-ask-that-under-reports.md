# TO ETFS_GUARDRAIL.TO-EG-s-23 -- THE STOP WORKED AND THE ASK UNDER-REPORTS: rung 3 writes one PARTNER-LESS key and is called ONCE PER PARTNER, so every partner's ask silently overwrites the one before it and a person authorising egress approves less than what is outstanding while believing they have seen all of it

<to_id>ETFS_GUARDRAIL.TO-EG-s-23</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: the ROUND-2 ANALYSIS at 94988 (`ledger/ROUND_ANALYSIS.round2.md`, grades `ledger/COMPLETION_GRADES.round2.json`, commit `f5074019a1`), which graded **FWD-8 NOT_REALIZED** and named this the round's honest half: "a stop-and-ask whose ask under-reports fails the outcome even though the stop worked." One of three cells that analysis listed as still to place; the other two are `EG-s-20` (TERMINAL, drained @`5d292ff11f`) and `EG-s-21` (running). Round 3 is mid-execution and this cell enters BY AMENDMENT under Andrew's 2026-09-03 scope-change word. Decomposition **v0.5** s.14, cell `EG-s-23`.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.6 | **Decomp cell:** `EG-s-23` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.5, s.14) | **outcome_ref:** FWD-8

---

## THE CELL

FWD-8 is *"going outside Opal to ask a provider for missing data stays a decision a person makes"*, and its accept is that the system **stops, NAMES THE DAYS IT WANTS, and waits for a person to say yes**. `EG-s-15`'s real September run proved the STOP is real: `coverage_egress_ask.json` was written, naming date, partner and provider, with zero vendor egress on two instruments with printed denominators. **The stop is not what fails. The NAMING is.**

Read the mechanism yourself before you change anything, because it is worse than a miscount.

```
rung3_stop_and_ask(partner, month, unresolved, ...)          # remediate.py:89
    key = "platinum/reports/%s/coverage_egress_ask.json" % month     # :118  <- NO PARTNER
    s3.put_object(Bucket=ETFS_BUCKET, Key=key, ...)                  # :119-124
```

`rung3_stop_and_ask` builds its `asks` list from EVERY day in the `unresolved` it is handed (`:100-109`), so **the function is not wrong about the partner it is given** -- it is faithful. But the KEY it writes carries the MONTH and NOT THE PARTNER, and `remediate_month` (`:129`) is a PER-PARTNER function. Run the ladder across the estate's partners and each partner's ask **overwrites the one before it at the same key**. The served artifact is the LAST partner's ask wearing the name of the month's ask.

**So the failure is not that a number is low. It is that an entire partner's outstanding days are ABSENT from an artifact whose whole purpose is to be complete**, and absent in a way that reads as complete: the file exists, it is well-formed, its `authorization` line is correct, and nothing in it says "there was another partner." A person authorising egress on it approves less than what is outstanding while believing they have seen all of it. That is the exact failure FWD-8 exists to prevent, arriving through the artifact rather than through the stop.

**THE BAR IS COMPLETENESS, AND THE SHAPE IS YOURS.** A person reading the month's ask must be able to reach EVERY outstanding unresolved day across EVERY partner -- or the artifact must say IN ITS OWN CONTENT which partners it does not cover, so a reader can tell a complete ask from a partial one without knowing the code. Per-partner keys, one merged document, or a manifest are all legitimate; what is not legitimate is a shape where a missing partner is invisible to its reader.

⛔ **DO NOT ENUMERATE THE PARTNERS BY RECALL.** CLAUDE.md rule 24 (i) as sharpened tonight: the set is THE PRINTED DENOMINATOR MINUS WHAT YOU EXCLUDE, never a forward list. This project has been bitten by a hand-typed partner list **twice in one night** -- an accept naming two of three, and an arm of mine naming two of three -- and both passed while the third partner carried the violation. Take the partner list from an artifact that owns it and print it as your denominator.

---

## DELIVERABLE

The changed `data/etfs/scripts/coverage/remediate.py`, permanent regression coverage in the estate's own suite at `data/etfs/scripts/coverage/tests/test_remediate.py`, and a battery under `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/` proving the arms below by output. Every `.py` edit passes `.tools/commit-gate.sh`. You commit the `complete` flip yourself after the proof instance validates.

---

## BOUNDS

- ⛔ **NO EGRESS, AND THIS IS THE OUTCOME'S OWN SUBJECT.** You make no provider call, open no HTTP client, use no credential and invoke nothing outward. Ruling card 4's PER-USE authorization stands for nobody and this cell does not touch it.
- ⛔ **NO SEND AND NO LAMBDA INVOKE.** Clear of Andrew's standing constraint (*"make sure no test run hits aj's email"*, ~02:5xZ 2026-09-10) BY CONSTRUCTION; arm (f) proves it from your run rather than asserting it.
- ⛔ **THIS CELL DEPLOYS NOTHING** and writes NO served key. You may READ the served `coverage_egress_ask.json`; you may not overwrite it. Arm (e) measures the deployed-vs-built gap rather than closing it.
- ⛔ **DO NOT TOUCH `0.9.0_WK_ETFS_GUARDRAIL~4`'S SURFACE.** That seat is live on `EG-s-21` inside `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py`. Your file is `data/etfs/scripts/coverage/remediate.py`. They do not overlap and must not.
- The rung-1/rung-2 ladder's behaviour is NOT this cell's subject: no fabrication, only a READ decides "resolved", and class B still stops without a re-run. If your change moves any of that, it has gone too far.
- Found something off-task? Append a row to `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md` and KEEP WORKING.

---

## ACCEPTANCE

<criterion id="S23-AC1" cell_refs="EG-s-23"><invocation>timeout 300 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/test_egs23_ask_completeness.py</invocation><expect>EGS23-ASK-NAMES-EVERY-PARTNER</expect></criterion>
**`S23-AC1` -- PASSES BY OUTPUT.** One battery, run by the invocation in the tag above, printing every number beside its denominator and ending with the literal token `EGS23-ASK-NAMES-EVERY-PARTNER` only when all seven arms hold. Each arm is one clause.

**(a) THE DEFECT REPRODUCES FIRST, ON THE CODE AS IT STANDS.** Against `remediate.py` BEFORE your change, run the ladder for TWO partners that each have at least one unresolved day, with a fake `s3` that records every `put_object`, and show that both calls target the SAME key and that the final stored body contains only the SECOND partner's dates. Print both bodies and the key. **If this does not reproduce, the premise of this cell is wrong: file a surprise row, print what you found, and STOP** -- do not change code on a premise the world just refused.

**(b) EVERY PARTNER IS REACHABLE AFTER THE CHANGE.** With the partner list taken from an artifact that owns it and PRINTED AS THE DENOMINATOR, run the ladder for every partner that has an unresolved day and show that each partner's dates are reachable by a reader of the month's ask. State the shape you chose in one sentence.

**(c) A PARTIAL ASK CANNOT READ AS COMPLETE.** Construct the case where one partner's ask is missing and show the artifact a reader gets is TEXTUALLY DIFFERENT from the complete case -- print both. This is the arm that carries the outcome: FWD-8 fails when a reader cannot tell the two apart.

**(d) THE LADDER'S OTHER PROPERTIES ARE UNDISTURBED.** Re-run `data/etfs/scripts/coverage/tests/test_remediate.py` by its own path, printing rc and pass/fail counts BEFORE and AFTER; and show `authorization` still reads PER-USE verbatim, that a `dry_run` still fires no rung 3, and that class B still stops without a re-run.

**(e) DEPLOYED-vs-BUILT, MEASURED.** Print the sha256 of the `remediate.py` bytes deployed at the box's artifact prefix beside your committed bytes and state `DEPLOYED == BUILT` or `DEPLOYED != BUILT` in those literal words. **This cell does not deploy and `DEPLOYED != BUILT` is the expected answer** -- the arm exists so the gap is a number somebody carries rather than an assumption nobody wrote down.

**(f) NO EGRESS, NO SEND, NO INVOKE.** Print the evidence from your own run that no provider call, HTTP client, credential, SES client or Lambda invoke occurred over the whole battery, with the denominator of what you checked.

**(g) THE REGRESSION ARMS ARE CONTROLS, NOT CONSTANTS.** The arms you add to the estate's own suite must FAIL against the pre-change code. Print them failing against it and passing against yours -- an arm that passes both ways proves nothing.

<criterion id="S23-AC2" cell_refs="EG-s-23" judgment="true"/>
**`S23-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** Your record states, for `3.0.0_SA_CVO` at L9: the shape you chose and why; what the SERVED 2026-09 `coverage_egress_ask.json` currently omits, with both counts and its vintage, since that is the artifact a person would have authorised on; whether any consumer reads that key and would be broken by a shape change, censused with a denominator rather than recalled; and what this change does NOT repair. Do not grade yourself PASS -- it is graded at L9.

<expected_criteria>S23-AC1, S23-AC2</expected_criteria>

<paths>
data/etfs/scripts/coverage/remediate.py
data/etfs/scripts/coverage/tests/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/
org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-23.the-ask-that-under-reports.md
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.5, cell `EG-s-23`.
<owned_cells>EG-s-23</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger; it edits one library module and runs a local battery. The round-3 schedule read at `EG-s-19`'s cut (2026-09-09 ~22:2xZ, 5 of 5 carriers, 25 gates armed, zero naming ETFS_GUARDRAIL or `opal-data-etfs`) is unchanged and is stated as context, not as this cell's disposition.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied; no policy, role or trust document is read or written.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants. `data/etfs/scripts/coverage/` is NOT a `{gold,silver,bronze}` path, so CLAUDE.md rule 13's DS commit lane does not gate it; rule 14's `.tools/commit-gate.sh` does, on every `.py` edit, and binds here.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S23-AC1`, `S23-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-23.the-ask-that-under-reports.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), validated with `python .tools/proof-of-spec-check.py <instance> S23-AC1,S23-AC2` BEFORE the complete flip, which you commit yourself. Flip only when `S23-AC1` PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
