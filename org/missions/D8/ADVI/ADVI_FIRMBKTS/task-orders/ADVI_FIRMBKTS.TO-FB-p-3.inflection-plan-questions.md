# ADVI_FIRMBKTS task order -- `FB-p-3` -- THE INFLECTION PLAN'S QUESTIONS Q1 TO Q15, EACH ANSWERED BY A LIVE READ OR CARRIED WITH AN OWNER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1 passes.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R9.md</decomp_doc>
<owned_cells>FB-p-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~86</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads only.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only.
comp-adversary: RUN by the issuer (`compose` on this order, read-vintage 2026-10-16 ~17:5xZ): any cited commit verified; the only absent cited paths are the record and the proof instance the executor creates. At base the record is absent (AC1 FAIL as expected). The grader rejects an entry range other than 1 to 15, a verdict outside ANSWERED and CARRIED, an ANSWERED entry with no evidence, a CARRIED entry with no owner or no next move, a call with a write verb, and zero denominators. Blindness: it proves shape, not that an answer is true.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-p-3` (round 9, item 2 of the CTO's enrichment list, entries 1 to 15)

The Inflection move plan is `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json`. Its `open_questions` list has 30 entries. **Entries 1 to 15 (list positions 0 to 14) are real questions, written `Q1 (before M03): ...` to `Q15 (M42): ...`.** Entries 16 to 30 are retained-as-is notes and belong to another order. For each of your 15 entries, give an answer with its evidence, or carry it with an owner and the next move. The CTO's wording: "each answered by a live read or carried with its owner, with the next move ordered."

### The rule for each entry

- A **factual** question (what does X read, does Y exist, who writes Z) is **ANSWERED** by a live read: AWS `get-`, `list-` or `describe-` calls through `.tools/aws`, or a read of the repository tree (`comp-find`, `comp-read`, `Read`). `evidence` names the call or the file and line. Count lists client-side and print the denominator.
- A **decision** question (the text says the CTO decides, Andrew decides, or an owner outside this project must confirm) is **CARRIED**: `owner` is the named decider, and `next_move` names the plan move (for example `M02`) and what happens once they answer. You do not decide it, and you do not guess it.
- Q7 (who writes `gold/meta/pipeline-complete.json`), Q8 and Q9 overlap the Door 6 census (`FB-p-1`, another worker, same round). Answer them from your own reads; do not wait for it.
- If a live read contradicts the plan, say so in `answer` and carry the entry with the plan row to correct as the `next_move`.

### The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~86/PLAN_INFLECTION_Q01_15.json`

```json
{"order": "FB-p-3", "read_at": "<ISO UTC>", "calls": ["<every call as run>"],
 "denominators": {"questions_in_plan": 30, "questions_answered_here": 15, "aws_lists_counted": 0},
 "entries": [{"n": 1, "id": "Q1", "verdict": "ANSWERED", "answer": "<one or two sentences>", "evidence": "<call or file:line>", "owner": "", "next_move": ""},
             {"n": 4, "id": "Q4", "verdict": "CARRIED", "answer": "<what is known>", "evidence": "<what was read>", "owner": "<the decider>", "next_move": "<M-id and the action after the answer>"}],
 "not_read": ["<what you did not read, and why>"], "claim": "measured"}
```
`entries` has exactly 15 objects, `n` = 1 to 15, once each. At least one denominator above zero.

## 2. BOUNDS

1. READ ONLY. No `put-`, `delete-`, `create-`, `update-`, `enable-`, `disable-`, `start-` or `invoke` call. AWS from bash is `.tools/aws`.
2. Print no secret, client name, advisor name, account id or relationship id; counts and resource names only.
3. You edit no file but your own record and proof instance. Anything surprising and off-task is ONE row in the project's surprise channel (the file in `<paths>`), then keep working.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~86/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~86/ADVI_FIRMBKTS.TO-FB-p-3.inflection-plan-questions.proof_of_spec.json` (named by this file's whole stem).
  <criterion id="AC1" cell_refs="FB-p-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 60 python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/checks/r9_checks.py planq --first 1 --last 15 --kind Q --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~86/PLAN_INFLECTION_Q01_15.json</invocation><expect>^PLANQ: OK entries=15 carried=[0-9]+$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Commit the record FIRST, your rows and the proof instance second. Report once: how many entries are ANSWERED and how many CARRIED, and each carried entry's owner.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round 9 item 2 (CTO analysis @bc6444b8e2). The plan's "30 open questions" are 15 real questions and 15 NO-MOVE notes (`FB-p-4`). A carried decision goes to its decider through the issuer's round-9 packet, not by the worker.

<status>complete</status>
<round>9</round>
<workstream>PLANQ</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-p-3</to_id>
<slot>~86</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
