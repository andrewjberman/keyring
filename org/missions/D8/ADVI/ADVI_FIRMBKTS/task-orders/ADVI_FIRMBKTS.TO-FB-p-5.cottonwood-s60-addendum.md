# ADVI_FIRMBKTS task order -- `FB-p-5` -- S60 (THE COTTONWOOD BLACK DIAMOND SECRET) ENTERED INTO THE COTTONWOOD PLAN AS A RETIRE CANDIDATE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1 passes.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R9.md</decomp_doc>
<owned_cells>FB-p-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~88</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads only.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only; no grant is added.
comp-adversary: RUN by the issuer (`compose` on this order, read-vintage 2026-10-16 ~17:5xZ): any cited commit verified; the only absent cited paths are the record and the proof instance the executor creates. At base the record is absent (AC1 FAIL as expected). The grader rejects a row other than D1-S60, a retire entry that does not name the secret, a delete that is not marked Andrew's or is marked performed, a census with no roles scanned, and any call carrying a write verb or `get-secret-value`. Blindness: it proves shape, not that the secret is unused.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-p-5` (round 9, item 3 of the CTO's enrichment list)

The surprise row `ADVI_FIRMBKTS-D1-S60` (in `org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md`; read it) records: the secret `opal/bd/cottonwood/credentials` is live in AWS Secrets Manager, declared by no Terraform, readable by 0 of 304 roles, unaccessed since 2026-05-26; a retire candidate for the Cottonwood move plan. The CTO's ruling: **it enters the Cottonwood plan as a retire candidate. Deleting a secret is irreversible and is Andrew's act: the plan names it, and the delete waits on his confirmation.** You write the addendum; you do NOT delete, rotate or read the secret.

The Cottonwood plan is `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~82/PLAN_COTTONWOOD.json`; its `retire` list has six entries `R1` to `R6`, each `{"id", "operation", "consumers", "decision"}`. Do NOT edit that file (it is another worker's committed deliverable); write the new entry as an addendum record. The issuer adds the pointer to the plan index at the merge.

### Steps (read-only)

1. Read the row `D1-S60`, its grounding, and the CRO census it cites.
2. Re-read the secret's **metadata only**: `.tools/aws secretsmanager describe-secret --secret-id opal/bd/cottonwood/credentials` (its LastAccessedDate, LastChangedDate, whether rotation is on, its tags, its resource policy through `get-resource-policy`). NEVER call `get-secret-value`, and print no value.
3. Re-measure what you can of "readable by 0 of 304 roles": at least a read of the resource policy and a search of the live AWS plane (`comp-find --corpus aws 'cottonwood/credentials'`, which prints its denominator) for any policy or Lambda environment naming the secret or its ARN. If you re-run a role-by-role simulation, say so; if you carry the CRO's figure of 304 roles and 0 readers, name its source in `not_read` as carried, not re-measured.
4. Write the retire entry in the plan's shape: `id` `R7`, `operation` naming the secret and what it is, `consumers` the count you read, `decision` recommending retire with the delete marked as Andrew's act after his confirmation.

### The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~88/COTTONWOOD_PLAN_ADDENDUM_S60.json`

```json
{"order": "FB-p-5", "read_at": "<ISO UTC>", "calls": ["<every call as run>"],
 "row": {"id": "D1-S60"},
 "retire_entry": {"id": "R7", "operation": "secret opal/bd/cottonwood/credentials: <what it is>", "consumers": 0,
                  "decision": "Recommend retire. The delete is irreversible and is Andrew's act: it waits on his confirmation.", "delete_by": "andrew", "delete_performed": false},
 "census": {"roles_scanned": 304, "roles_with_read": 0, "last_accessed": "2026-05-26", "source": "<re-measured here, or carried from the CRO census and named>"},
 "not_read": ["<what you did not read, and why>"], "claim": "measured"}
```
`delete_by` is exactly `andrew` and `delete_performed` exactly `false`.

## 2. BOUNDS

1. READ ONLY, and for the secret METADATA ONLY: never `get-secret-value`, never `delete-secret`, `rotate-secret`, `put-` or `update-` of anything. AWS from bash is `.tools/aws`.
2. Print no secret value, credential, client name or relationship id.
3. You edit no file but your own record and proof instance. Anything surprising and off-task is ONE row in the project's surprise channel, then keep working.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~88/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~88/ADVI_FIRMBKTS.TO-FB-p-5.cottonwood-s60-addendum.proof_of_spec.json` (named by this file's whole stem).
  <criterion id="AC1" cell_refs="FB-p-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 60 python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/checks/r9_checks.py addendum --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~88/COTTONWOOD_PLAN_ADDENDUM_S60.json</invocation><expect>^ADDENDUM: OK consumers=[0-9]+ delete=andrew$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Commit the record FIRST, your rows and the proof instance second. Report once: the consumers you read, whether the 304-role figure was re-measured or carried, and the secret's last access.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round 9 item 3 (CTO analysis @bc6444b8e2, section 3 on S60). The delete of the secret is Andrew's act and appears in the round-9 packet's list of acts only he can perform. S59 (Cottonwood silver `account_attributes`) is routed to `2.0.0_SA_COO~C1` by the CTO and is not in this order.

<status>complete</status>
<round>9</round>
<workstream>S60</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-p-5</to_id>
<slot>~88</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
