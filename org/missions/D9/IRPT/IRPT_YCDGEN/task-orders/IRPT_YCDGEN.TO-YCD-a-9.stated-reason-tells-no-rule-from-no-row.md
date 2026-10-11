# TO-YCD-a-9 -- the reason a section states tells "Opal does not keep this figure" from "no row for this security"

<to_id>IRPT_YCDGEN.TO-YCD-a-9</to_id>
<project>IRPT_YCDGEN</project>
<issued_to>0.9.0_WK_IRPT_YCDGEN~11</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `YCD-a-9` (`decompositions/IRPT_YCDGEN_DECOMP_R9.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none.

---

## WORKER FACE

### Read first

`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r8/HELD_STORE_READ_YCD-e-8_PART1_20261011.md`, sections 1 and 2. Then, under `infra/aws/lambda/investor-reporting/ycharts/research/`:
`opal_producer.py` `closed_reason` (:102-116), `held_data.py` `value_of` (:271-288) and `_not_held_reason` (:176-186), and
`layout_overview.py` `_compute_opal_held` (:613-641).

### THE CELL

Today every reason that starts `NOT_HELD:` becomes `INPUT_MISSING:held_<group>` on the page. `value_of` returns NotHeld for
three different causes, and the page states one reason for all of them. In the run of record that put the same words on 155
sections: 70 where Opal keeps no such figure by design, and 85 where the figure is kept but no security of the portfolio has a
row. Make the stated reason say which.

1. **A typed cause, not a sentence.** `held_data.NotHeld` gains a `cause` that is exactly one of `NO_RULE`, `FIELD_MISMATCH`,
   `NO_ROW`. `value_of` sets it at each of its three NotHeld returns. Do not decide the cause anywhere by matching the text of
   a reason.
2. **The cause travels.** `layout_overview._compute_opal_held` carries the cause into the reason it raises, in a form
   `closed_reason` can read without parsing prose (for example `NOT_HELD:<CAUSE>:<the existing text>`). The layout's own
   sentence stays in the trace, as today.
3. **The closed reason, in `opal_producer.closed_reason`:**
   - cause `NO_RULE` -> `NOT_IN_THIS_VERSION` (already a member of `CLOSED_REASONS`);
   - cause `NO_ROW` -> `INPUT_MISSING:security_not_covered`;
   - cause `FIELD_MISMATCH` -> `INPUT_MISSING:held_<group>`, as today (it is a map defect, and the word fits it);
   - a `NOT_HELD:` reason with no recognisable cause -> `INPUT_MISSING:held_<group>`, as today. Never guess a cause.
4. **The contract.** Read the `reason` property of the Opal branch in `infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.v2.schema.json`
   (`$defs.opal_engine`, the `sections` item). If it admits `INPUT_MISSING:security_not_covered`, say so in your report with
   the line. If its pattern or enum REFUSES that string, do NOT edit the schema (it is generated from a PRD): stop, file a row
   and report.
5. **Tests**, in `research/tests/`, offline:
   - `closed_reason` for each of the four arms of step 3;
   - `value_of` sets the right cause on a group with no rule, on a field mismatch, and on a rule-fed group whose rows are empty;
   - one end-to-end case through the producer's own entry: a portfolio whose securities have no store row yields a section
     whose stated reason is `INPUT_MISSING:security_not_covered`, and a no-rule section in the same run reads
     `NOT_IN_THIS_VERSION`;
   - update `test_opal_producer.py` `test_closed_reason_maps_every_layout_word_into_the_closed_set` (:348), which pins the old
     fold, to the new arms. Keep every other test in the folder green.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="A9-AC1" cell_refs="YCD-a-9"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r8/r8_checks.py f8</invocation><expect>^R8-F8-OK</expect></criterion>

<criterion id="A9-AC2" cell_refs="YCD-a-9"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r8/r8_checks.py f8fold</invocation><expect>^R8-F8FOLD-OK</expect></criterion>

<expected_criteria>A9-AC1,A9-AC2</expected_criteria>

- AC1 runs the whole `ycharts/research/tests` folder: 0 failed, 0 errors, and at least 240 passed (it reads 235 at base). At
  base it FAILs on the count.
- AC2 imports the two modules and asks them directly: `closed_reason` of a NO_RULE reason is `NOT_IN_THIS_VERSION`, of a NO_ROW
  reason is `INPUT_MISSING:security_not_covered`, and the NotHeld of a no-rule group carries cause `NO_RULE`. At base it FAILs.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS calls, no HTTP, no installs. Every `.py` edit passes
  `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_YCDGEN-D2-W11-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of the channel file
  below. Each row's `surfaced_at` is the output of `date -u +%Y-%m-%dT%H:%M:%SZ` at the moment you write it; never type a time.
  Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_YCDGEN~11" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_YCDGEN~11@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_YCDGEN~11 <0.9.0_WK_IRPT_YCDGEN~11@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools; a recursive shell grep over the repo is denied by a hook.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/held_data.py
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~11/
org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-a-9.stated-reason-tells-no-rule-from-no-row.md
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R9.md</decomp_doc> round 9, cell `YCD-a-9`.
<owned_cells>YCD-a-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: A9-AC1, A9-AC2. Instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~11/IRPT_YCDGEN.TO-YCD-a-9.stated-reason-tells-no-rule-from-no-row.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_YCDGEN.TO-YCD-a-9`.
- Validate with `python .tools/proof-of-spec-check.py <instance> A9-AC1,A9-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~66/IRPT_ANLREQ.TO-AR-g-31.packager-live-ticket-ports.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- how the cause travels from `value_of` to `closed_reason`, with the lines;
- what the v2 schema's `reason` admits (step 4), with the line;
- which existing tests you changed and why;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- three modules of ycharts/research; the stated reason of an Opal-held NOT_AVAILABLE section changes for two of three causes; no value, status, method or coverage changes. Ships only in a resident release under its own pair; nothing deploys here.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission, no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route; the served reader passes `reason` through.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read opal_producer.py :54-55 and :102-116, held_data.py :176-186 and :271-288, layout_overview.py :613-641, and the census @ab43002cf5. Traps: deciding the cause by matching a sentence; a reason the v2 schema refuses (the contract is generated, not edited here); changing a value while changing a word; the pinned old fold in test_opal_producer.py :353.
lane: ycharts/research/*.
</preflight>

Source: CTO round-9 analysis @eeb799ce72 section 3 item 1 (first written under ADDENDUM 8.3 @7f3b2e983a, msg 4403); the held-store read @2931dbfa0e and @bcc8b703e7.
