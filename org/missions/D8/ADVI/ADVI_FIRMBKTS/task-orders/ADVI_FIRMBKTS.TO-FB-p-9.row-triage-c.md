# ADVI_FIRMBKTS task order -- `FB-p-9` -- TRIAGE OF THE 21 OPEN REMEDIATION ROWS OF `REMEDIATION_v1`, `v2`, `v3` AND `v6` (GROUP C): A VERDICT AND ITS EVIDENCE FOR EACH

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1 passes.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R9.md</decomp_doc>
<owned_cells>FB-p-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~92</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads only.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only.
comp-adversary: RUN by the issuer (`compose` on this order, read-vintage 2026-10-16 ~17:5xZ): any cited commit verified; the only absent cited paths are the record and the proof instance the executor creates. At base the record is absent (AC1 FAIL as expected). The grader rejects a row list that is not exactly the 21 listed ids once each, a verdict outside MET, RE_OWN, DISMISS and CARRY, a verdict missing its required field (MET evidence, RE_OWN new_owner, DISMISS reason, CARRY carrier), any non-MET verdict without the evidence read, a write-verb call and zero denominators. Blindness: it proves coverage and shape, not that a verdict is right; the CVO reads the proposals and writes the clocks.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-p-9` (round 9, item 5 of the CTO's enrichment list, group C)

The project's surprise channel keeps remediation rows: a hazard row was filed, and a remedy was named with an owner. **84 of them are still OPEN and have not moved for two or more rounds.** The CTO's rule: "each one met, re-owned or dismissed with a reason." You hold group C: the **21 OPEN rows of `REMEDIATION_v1`, `REMEDIATION_v2`, `REMEDIATION_v3` and `REMEDIATION_v6`**, listed one per line (id, tab, file version) in `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/triage_ids_C.txt`. Give each a verdict and the evidence you read. **You propose; you do not close.** The remediation clock is the CVO's to write, so you edit no channel row.

### For each id in your list

1. Read its remediation row in the file named on the id's line of your list: `org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/remediations/REMEDIATION_v1.md`, `.../REMEDIATION_v2.md`, `.../REMEDIATION_v3.md` or `.../REMEDIATION_v6.md` (a fenced JSON block whose `id` is the id): the hazard, the remedy asked, the owner, the class. Read the investigation row of the same id in `org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md` for what the world was.
2. Check the world NOW with the cheapest read that settles it: a live AWS `get-`, `list-` or `describe-` call through `.tools/aws`, or a read of the file at HEAD (`comp-read`, `Read`; `comp-find` for a search, never a blind recursive grep), or `git log`/`git show` for the commit that did the remedy.
3. Give ONE verdict:
   - **MET**: the world now matches what the row asked. `evidence` names the read or the commit.
   - **DISMISS**: nothing remains to do. `reason` starts with `NOT_A_DEFECT:` (the spec was wrong, a ruling amended it, or the row only records a fact), `IRREMEDIABLE:` (no act can restore the world) or `ACCEPTED_BY_RULING:` (a ruling keeps the spec and accepts the gap; name the ruling), then why. `evidence` is still required.
   - **RE_OWN**: the remedy is still owed but its owner cannot do it (the serial is gone, retired, or the project moved). `new_owner` is the serial that now holds the work; `evidence` says why the old owner cannot.
   - **CARRY**: the remedy is still owed and lives with another carrier. `carrier` names the successor row id, order or seat; `evidence` names the read that shows it is still owed. If you could not settle a row within about three reads, CARRY it with `carrier` beginning `UNDETERMINED:` and say what you read.
4. Never guess a verdict from the row's text alone: every verdict carries a read.

### The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~92/TRIAGE_C.json`

```json
{"order": "FB-p-9", "read_at": "<ISO UTC>", "group": "C", "calls": ["<every read as run, file reads included>"],
 "denominators": {"rows_listed": 21, "rows_read": 21},
 "rows": [{"id": "ADVI_FIRMBKTS-D1-S1", "verdict": "MET", "evidence": "<the read or commit>", "reason": "", "new_owner": "", "carrier": ""}],
 "not_read": ["<what you did not read, and why>"], "claim": "measured"}
```
`rows` has exactly the 21 ids of your list, once each. Each row fills the field its verdict requires (`MET` evidence; `RE_OWN` new_owner; `DISMISS` reason; `CARRY` carrier) and `evidence` for every verdict.

## 2. BOUNDS

1. READ ONLY. No `put-`, `delete-`, `create-`, `update-`, `enable-`, `disable-`, `start-`, `invoke` or other write call. AWS from bash is `.tools/aws`.
2. You edit no channel row and no file but your own record and proof instance. Anything surprising and off-task is ONE new row in the project's investigation channel (the file in `<paths>`), then keep working.
3. Print no secret, client name, advisor name, account id or relationship id: counts and resource names only.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~92/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~92/ADVI_FIRMBKTS.TO-FB-p-9.row-triage-c.proof_of_spec.json` (named by this file's whole stem).
  <criterion id="AC1" cell_refs="FB-p-9"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 60 python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/checks/r9_checks.py triage --ids org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/triage_ids_C.txt --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~92/TRIAGE_C.json</invocation><expect>^TRIAGE: OK rows=21 met=[0-9]+ re_own=[0-9]+ dismiss=[0-9]+ carry=[0-9]+$</expect></criterion>
</proof_of_spec>

AC1 grades coverage and shape, not that a verdict is right.

## 5. WHEN YOU ARE DONE

Commit the record FIRST, your rows and the proof instance second. Report once: the counts by verdict and every RE_OWN and every UNDETERMINED carry.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round 9 item 5 (CTO analysis @bc6444b8e2). The "84 OPEN rows not moved for 2 or more rounds" are, by the instrument, the OPEN remediation rows of `REMEDIATION_v1..v6` (4 + 2 + 5 + 33 + 30 + 10); group C is `v4`, B is `v5`, C is `v1`, `v2`, `v3` and `v6`. The issuer reads the three proposals, rules RE_OWN and CARRY inside its own decomposition, and sends the MET and DISMISS proposals to `3.0.0_SA_CVO`, who writes the clocks.

<status>complete</status>
<round>9</round>
<workstream>TRIAGE</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-p-9</to_id>
<slot>~92</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
