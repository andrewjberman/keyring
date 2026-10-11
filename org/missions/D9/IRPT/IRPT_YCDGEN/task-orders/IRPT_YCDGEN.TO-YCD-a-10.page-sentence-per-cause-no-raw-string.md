# TO-YCD-a-10 -- the page prints one true sentence per not-held cause, and no raw reason string (row D2-S44)

<to_id>IRPT_YCDGEN.TO-YCD-a-10</to_id>
<project>IRPT_YCDGEN</project>
<issued_to>0.9.0_WK_IRPT_YCDGEN~13</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `YCD-a-10` (`decompositions/IRPT_YCDGEN_DECOMP_R10.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (the reason fix `YCD-a-9` is merged).

---

## WORKER FACE

### Read first

Under `infra/aws/lambda/investor-reporting/ycharts/research/`: `layout_overview.py` `_reason_line` (:945-955) and its two callers (:1035, :1043);
`held_data.py` for the constants `NO_RULE`, `FIELD_MISMATCH`, `NO_ROW`; and `_compute_opal_held` in `layout_overview.py`, which
raises a reason of the form `NOT_HELD:<CAUSE>:<sentence>`.

### THE CELL

The stored reason of an Opal-held section now tells the causes apart. The PAGE does not: for every reason that starts
`NOT_HELD:`, `_reason_line` prints
`Not available: Opal does not hold this figure for the portfolio's holdings. Reason: <the raw reason>`. That is one sentence for
different causes, and a raw code string is not page text. Fix the page.

1. For a reason that starts `NOT_HELD:`, `_reason_line` returns EXACTLY one of these three sentences, chosen by the cause that
   follows the prefix, compared with the `held_data` constants (never by matching the text of the sentence):
   - cause `NO_RULE`: `Not available: Opal does not keep this figure in this version of the report.`
   - cause `NO_ROW`: `Not available: Opal keeps this figure, but has no data for the securities this portfolio holds.`
   - cause `FIELD_MISMATCH`, or no recognisable cause: `Not available: this figure could not be worked out for this portfolio.`
2. None of the three contains `NOT_HELD`, a cause word, a colon after the first, or any part of the stored reason. Add the three
   as named module constants beside `NOT_IN_THIS_VERSION_LINE` (:204).
3. Every OTHER branch of `_reason_line` stays byte-identical: `NOT_IN_THIS_VERSION`, the outside-budget reason, and the two
   generic branches that print `Reason: %s`. You change the `NOT_HELD:` branch only.
4. The stored reason, the trace, `closed_reason` and every value, status, method and coverage are untouched. This cell changes
   page text only.
5. Tests, in `research/tests/`, offline:
   - `_reason_line` for each of the three causes and for a `NOT_HELD:` reason with no recognisable cause, asserting the exact
     sentence;
   - one rendered-page case: a page built with a NO_RULE section and a NO_ROW section contains both sentences and does not
     contain the substring `NOT_HELD`;
   - update `test_layout_overview.py` (:504), which asserts `"NOT_HELD:" in html`, to the new truth. Keep every other test in the
     folder green.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="A10-AC1" cell_refs="YCD-a-10"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/r10_checks.py a10</invocation><expect>^R10-A10-OK</expect></criterion>

<criterion id="A10-AC2" cell_refs="YCD-a-10"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/r10_checks.py a10suite</invocation><expect>^R10-A10SUITE-OK</expect></criterion>

<expected_criteria>A10-AC1,A10-AC2</expected_criteria>

- AC1 imports `layout_overview` and asks `_reason_line` directly for the three causes and an unrecognised one, and checks the
  four untouched branches still read as they do at base. At base it FAILs.
- AC2 runs the whole `ycharts/research/tests` folder: 0 failed, 0 errors, at least 247 passed (it reads 243 at base). At base
  it FAILs on the count.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS calls, no HTTP, no installs. Every `.py` edit passes
  `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_YCDGEN-D2-W13-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of the channel file
  below. Each row's `surfaced_at` is the output of `date -u +%Y-%m-%dT%H:%M:%SZ` at the moment you write it; never type a time.
  Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_YCDGEN~13" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_YCDGEN~13@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_YCDGEN~13 <0.9.0_WK_IRPT_YCDGEN~13@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools; a recursive shell grep over the repo is denied by a hook.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~13/
org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-a-10.page-sentence-per-cause-no-raw-string.md
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R10.md</decomp_doc> round 10, cell `YCD-a-10`.
<owned_cells>YCD-a-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: A10-AC1, A10-AC2. Instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~13/IRPT_YCDGEN.TO-YCD-a-10.page-sentence-per-cause-no-raw-string.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_YCDGEN.TO-YCD-a-10`.
- Validate with `python .tools/proof-of-spec-check.py <instance> A10-AC1,A10-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~11/IRPT_YCDGEN.TO-YCD-a-9.stated-reason-tells-no-rule-from-no-row.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the `_reason_line` change, with the lines;
- which existing tests you changed and why;
- whether any OTHER place in the research folder prints a stored `NOT_HELD:` string to a page or a document (name it, do not fix it);
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one function of ycharts/research/layout_overview.py, one branch; page text only. Ships only in the resident release of cell YCD-d-10, under its own pair; nothing deploys here.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission, no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read layout_overview.py :204 and :945-955 and the round-9 worker's report on the wire form. Traps: choosing the sentence by matching prose; a raw string surviving in a second print site; changing the stored reason while changing the page; the pinned assertion at test_layout_overview.py :504.
lane: ycharts/research/*.
</preflight>

Source: CTO round-10 analysis @ea78b95649 section 4 item 1 and section 3 (row D2-S44); CTO~DELL2 msg 4477.
