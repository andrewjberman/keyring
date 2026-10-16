# ADVI_FIRMBKTS task order -- `FB-p-4` -- THE INFLECTION PLAN'S NO-MOVE NOTES (ENTRIES 16 TO 30) CONFIRMED, CONTRADICTED OR CARRIED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1 passes.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R9.md</decomp_doc>
<owned_cells>FB-p-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~87</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads only.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only.
comp-adversary: RUN by the issuer (`compose` on this order, read-vintage 2026-10-16 ~17:5xZ): any cited commit verified; the only absent cited paths are the record and the proof instance the executor creates. At base the record is absent (AC1 FAIL as expected). The grader rejects an entry range other than 16 to 30, a verdict outside CONFIRMED, CONTRADICTED and CARRIED, a CONFIRMED or CONTRADICTED entry with no evidence, a CARRIED entry with no owner or next move, a write-verb call and zero denominators. Blindness: it proves shape, not that a confirmation is true.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-p-4` (round 9, item 2 of the CTO's enrichment list, entries 16 to 30)

The Inflection move plan is `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json`. Its `open_questions` list has 30 entries. **Entries 16 to 30 (list positions 15 to 29) are NO-MOVE notes**, each saying that a named resource is retained and not moved (`NO-MOVE L02 mdpf-gold-lambda ...`, `NO-MOVE R07 ...`, `NO-MOVE INF-FN-37 and INF-FN-38 ...`), a few saying an item "is now a move". Entries 1 to 15 are real questions and belong to another order. For each of your 15 entries, check by a live read (or a tree read) whether the note is still true, and record it.

### The rule for each entry

- **CONFIRMED:** the named resource exists as the note says (state, schedule, trigger, target) and nothing you read touches the bucket `opal-data-inf` in a way that would force a move. `evidence` names the call or file.
- **CONTRADICTED:** the live state differs from the note (the resource is gone, disabled, newly reading the bucket, or "now a move" is not reflected in the plan's moves). `answer` says how; `evidence` names the read; `next_move` names the plan row to correct.
- **CARRIED:** you cannot determine it from reads you can make (a resource you may not read, an owner outside this project). `owner` names who can, `next_move` what follows.
- For an entry naming several items (`L28 and L29`, `INF-FN-37 and INF-FN-38`), check each item and say in `answer` which.
- `id` is the identifier the note starts with (`L02`, `L28/L29`, `R07`, `INF-FN-37/38` and so on).

### The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~87/PLAN_INFLECTION_NOMOVE_16_30.json`

```json
{"order": "FB-p-4", "read_at": "<ISO UTC>", "calls": ["<every call as run>"],
 "denominators": {"notes_in_plan": 15, "notes_checked": 15, "aws_lists_counted": 0},
 "entries": [{"n": 16, "id": "L02", "verdict": "CONFIRMED", "answer": "<one or two sentences>", "evidence": "<call or file:line>", "owner": "", "next_move": ""}],
 "not_read": ["<what you did not read, and why>"], "claim": "measured"}
```
`entries` has exactly 15 objects, `n` = 16 to 30, once each. At least one denominator above zero.

## 2. BOUNDS

1. READ ONLY. No `put-`, `delete-`, `create-`, `update-`, `enable-`, `disable-`, `start-` or `invoke` call. AWS from bash is `.tools/aws`.
2. Print no secret, client name, advisor name, account id or relationship id; counts and resource names only.
3. You edit no file but your own record and proof instance. Anything surprising and off-task is ONE row in the project's surprise channel (the file in `<paths>`), then keep working.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~87/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~87/ADVI_FIRMBKTS.TO-FB-p-4.inflection-plan-nomove-notes.proof_of_spec.json` (named by this file's whole stem).
  <criterion id="AC1" cell_refs="FB-p-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 60 python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/checks/r9_checks.py planq --first 16 --last 30 --kind NOMOVE --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~87/PLAN_INFLECTION_NOMOVE_16_30.json</invocation><expect>^PLANQ: OK entries=15 carried=[0-9]+$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Commit the record FIRST, your rows and the proof instance second. Report once: counts of CONFIRMED, CONTRADICTED and CARRIED, and each contradiction.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round 9 item 2 (CTO analysis @bc6444b8e2), the second half of the plan's 30 entries (`FB-p-3` holds the first 15). A CONTRADICTED note is a correction to the plan, ruled by the issuer in the round-9 packet.

<status>pending</status>
<round>9</round>
<workstream>PLANQ</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-p-4</to_id>
<slot>~87</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
