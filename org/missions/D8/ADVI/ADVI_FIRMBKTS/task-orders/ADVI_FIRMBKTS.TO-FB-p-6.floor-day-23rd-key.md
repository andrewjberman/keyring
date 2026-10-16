# ADVI_FIRMBKTS task order -- `FB-p-6` -- THE 23RD NAMED KEY THAT DREW NO NEW VERSION ON THE 2026-10-16 FLOOR DAY, NAMED WITH WHY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1 passes.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R9.md</decomp_doc>
<owned_cells>FB-p-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~89</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads only.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only.
comp-adversary: RUN by the issuer (`compose` on this order, read-vintage 2026-10-16 ~17:5xZ): any cited commit verified; the only absent cited paths are the record and the proof instance the executor creates. At base the record is absent (AC1 FAIL as expected). The grader rejects a floor day other than 2026-10-16, a count of versions on the floor day other than zero, an empty key, writer, reason or last-version time, and a write-verb call. Blindness: it proves shape, not that the reason is true.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-p-6` (round 9, item 4 of the CTO's enrichment list)

The first floor day of the moved publisher trigger was 2026-10-16. The publisher `inf-portal-publisher` has 23 NAMED output keys (listed in `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ACT3_BASELINE_VERSIONS.json`, with their VersionIds before the switch). On the floor day, 22 of the 23 drew a new version (3 snapshots at 13:30:48Z and 19 advisor files 13:31:10Z to 13:31:13Z). The 23rd drew none. The first-day record (`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/MOVE_RECORD.json`, field `exercised.evidence`) says it is `inflection_wealth_management/top_holdings.json` and "is written by the gold chain, not the publisher". **Name the key, name its writer, and say why it drew no new version that day. Check; do not copy.** The CTO's wording: "named rather than assumed."

### Steps (read-only)

1. Read the 23 keys from `ACT3_BASELINE_VERSIONS.json`. For each, read its version history in the bucket `opal-data-inf` (`.tools/aws s3api list-object-versions --bucket opal-data-inf --prefix <key>`; count client-side; the keys under the advisor prefix carry advisor names: print COUNTS for those, key names only for the three snapshot keys and the 23rd). Identify the one key with NO version dated 2026-10-16.
2. **Its writer:** read the publisher source `infra/aws/lambda/inf-portal-publisher/lambda_function.py` for how the 23 names are derived and whether the publisher writes this key; read the gold chain for the step that writes it (`comp-find` on the key name over `infra/`, `lib/`, `integrations/`; name the file and line).
3. **Why no new version on the floor day:** from its version history (its last version time, its cadence over the previous days) and its writer (does it write daily, only when an input changed, or weekly), say why a floor-day publisher run would not produce a new version, and whether that is expected.
4. If your reads show the premise false (the key you identify DID draw a version on 2026-10-16, or two keys drew none), do not force the record: file ONE BLOCKING row naming what you read, and stop.

### The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~89/KEY23.json`

```json
{"order": "FB-p-6", "read_at": "<ISO UTC>", "floor_day": "2026-10-16", "key": "<the 23rd key>", "writer": "<file:line or role that writes it>",
 "why": "<why it drew no new version on the floor day, and whether that is expected>", "last_version_at": "<ISO UTC of its newest version>",
 "versions_on_floor_day": 0, "calls": ["<every call as run>"], "claim": "measured"}
```

## 2. BOUNDS

1. READ ONLY. No `put-`, `delete-`, `copy-`, `restore-` or `invoke` call. AWS from bash is `.tools/aws`.
2. Print no secret, client name, advisor name, account id or relationship id: counts for any advisor key.
3. You edit no file but your own record and proof instance. Anything surprising and off-task is ONE row in the project's surprise channel, then keep working.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~89/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~89/ADVI_FIRMBKTS.TO-FB-p-6.floor-day-23rd-key.proof_of_spec.json` (named by this file's whole stem).
  <criterion id="AC1" cell_refs="FB-p-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 60 python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/checks/r9_checks.py key23 --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~89/KEY23.json</invocation><expect>^KEY23: OK key=.+$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Commit the record FIRST, your rows and the proof instance second. Report once: the key, its writer, the reason, and whether the first-day record's claim held.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round 9 item 4 (CTO analysis @bc6444b8e2, section 1). The CTO accepted C4 and sent this to round 9 "to be named rather than assumed".

<status>pending</status>
<round>9</round>
<workstream>KEY23</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-p-6</to_id>
<slot>~89</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
