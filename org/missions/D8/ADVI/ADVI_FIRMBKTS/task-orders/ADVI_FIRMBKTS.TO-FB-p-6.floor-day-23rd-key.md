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

The first floor day of the moved publisher trigger was 2026-10-16. The publisher `inf-portal-publisher` has 23 NAMED output keys (listed in `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ACT3_BASELINE_VERSIONS.json`, with their VersionIds before the switch). In the PUBLISHER'S RUN WINDOW on that day, 13:30:00Z to 13:35:00Z, 22 of the 23 drew a new version (3 snapshots at 13:30:48Z and 19 advisor files 13:31:10Z to 13:31:13Z). The 23rd drew none in that window. The first-day record (`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/MOVE_RECORD.json`, field `exercised.evidence`) says it is `inflection_wealth_management/top_holdings.json` and "is written by the gold chain, not the publisher". **Name the key, name who writes it, and say why the publisher's run did not give it a new version. Check; do not copy.** The CTO's wording: "named rather than assumed."

**AMENDED by the issuer (amendment 1, 2026-10-16 ~18:5xZ), after the first worker read the original and filed a BLOCKING row.** The original said "on the floor day" and "drew no new version that day". That was false as written: the daily gold step `data/inf/scripts/gold/INF_D_02b.top_holdings.py` writes this key earlier the same day (about 12:52Z), so the key DOES have a version dated 2026-10-16. The quantity the CTO asks about is the publisher's own run window above. The reads you already made stand; use them. What was NOT yet read is why the publisher did not write the key in its 13:30Z run: the advisor publisher's write of this key is conditional (`infra/aws/lambda/inf-portal-advisor-publisher/lambda_function.py` near lines 1200-1201).

### Steps (read-only)

1. Read the 23 keys from `ACT3_BASELINE_VERSIONS.json`. For each, read its version history in the bucket `opal-data-inf` (`.tools/aws s3api list-object-versions --bucket opal-data-inf --prefix <key>`; count client-side; the keys under the advisor prefix carry advisor names: print COUNTS for those, key names only for the three snapshot keys and the 23rd). Identify the one key with NO version dated inside the publisher's run window, 2026-10-16T13:30:00Z to 2026-10-16T13:35:00Z. Record how many versions it has on 2026-10-16 in total (the daily gold step may have written one earlier) and the time of its newest version.
2. **Its writer:** read the publisher source `infra/aws/lambda/inf-portal-publisher/lambda_function.py` for how the 23 names are derived and whether the publisher writes this key; read the gold chain for the step that writes it (`comp-find` on the key name over `infra/`, `lib/`, `integrations/`; name the file and line). Then read the condition under which the PUBLISHER writes this key (the advisor publisher, near lines 1200-1201) and name the file and line.
3. **Why the publisher's run gave it no new version:** from the condition you read in step 2 and the inputs the publisher tested on 2026-10-16 (its log lines at about 13:31Z, or a live read of what it looked at), say why the publisher did not write this key in its 13:30Z run, and whether that is expected. The daily gold write at about 12:52Z is a different writer and does not count as the publisher's.
4. If your reads show the premise false (the key you identify DID draw a version inside the 13:30Z to 13:35Z window, or two keys drew none inside it), do not force the record: file ONE BLOCKING row naming what you read, and stop.

### The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~89/KEY23.json`

```json
{"order": "FB-p-6", "read_at": "<ISO UTC>", "floor_day": "2026-10-16", "key": "<the 23rd key>", "writer": "<the daily gold step: file:line>",
 "publisher_condition": "<the condition under which the publisher writes this key: file:line, and how it evaluated on 2026-10-16>",
 "why": "<why the publisher's run gave it no new version, and whether that is expected>", "last_version_at": "<ISO UTC of its newest version>",
 "publisher_window": {"from": "2026-10-16T13:30:00Z", "to": "2026-10-16T13:35:00Z"}, "versions_in_publisher_window": 0, "versions_on_floor_day_total": 1,
 "calls": ["<every call as run>"], "claim": "measured"}
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

**ISSUER NOTES:** Round 9 item 4 (CTO analysis @bc6444b8e2, section 1). The CTO accepted C4 and sent this to round 9 "to be named rather than assumed". **AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-16 ~18:5xZ):** the first worker (`~89`) measured that the key drew a version at 12:52:32Z the same day, from the daily gold step, and stopped on a BLOCKING row (D1-W89-S1) as the face told it to. The defect was the issuer's wording ("floor day" for "the publisher's run window"), not the worker's. The face, the record shape and the grader's `key23` mode are amended to the publisher's window; the AC1 invocation is unchanged. The same worker continues on this face; its rows stand and the issuer dispositions S1 as answered by this amendment.

<status>complete</status>
<round>9</round>
<workstream>KEY23</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-p-6</to_id>
<slot>~89</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
