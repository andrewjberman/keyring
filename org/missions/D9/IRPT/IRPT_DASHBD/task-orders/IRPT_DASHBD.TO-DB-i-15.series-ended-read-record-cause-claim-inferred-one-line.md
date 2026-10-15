# TO IRPT_DASHBD.TO-DB-i-15 -- the series-ended read record carries its claim: ONE key, cause_claim "inferred", added to the round-126 record (direct act)

<to_id>IRPT_DASHBD.TO-DB-i-15</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~315</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>128</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_126_20261015.md` (msg 8730): "add one line to the read record, cause_claim: inferred (absent from a complete partition; account status not read)".

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-315`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~315/`. Never touch a path outside the `<paths>` block below.

**Why.** Round 126's cause read says an early-ending Orion series belongs to an account Opal's positions silver no longer holds. That verdict rests on the account being ABSENT from complete positions partitions; the account's own status (closed, transferred, re-registered) was not read. A value must carry its claim in a field a consumer can reject on, so the record gets one key saying so.

**The cell (`DB-i-15`).** Text of the owned cell: *"Add the key cause_claim with the string value inferred to the round-126 series-ended read record, and touch nothing else."*

**What you do (one file, one key).** Edit `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~313/SERIES_ENDED_CAUSE_R126.json`: add the single top-level key `"cause_claim"` with the value `"inferred"`. Load the file with `json`, add the key, and write it back with `indent=2` and `sort_keys=True` as ASCII, so that the diff is exactly one added line and no other byte moves (check with `git diff`). Do not touch the script, the private extract, the checker or any other key. Then run the criterion below.

<criterion id="DBI128-1-AC1" cell_refs="DB-i-15"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r126/p126_cause.py" . DBI126-1-AC1</invocation><expect>DBI126-1-AC1 PASS</expect></criterion>
`DBI128-1-AC1` -- the round-126 read record passes the round-126 check, which now also requires `cause_claim` to read `inferred`; and `git diff` of the record against its parent shows exactly one added line. Base: FAIL (the record carries no `cause_claim`).

<expected_criteria>DBI128-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the check, the script and the private folder.
- **No read, no call.** No S3 read, no vendor call, no write outside the grant, no push.
- **Client data.** None enters the repo; the record already carries counts, words and digests only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or widened. Rows (if any) go to the investigation file, ids `IRPT_DASHBD-D2-W315-S<k>`, `surfaced_at` from `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh`. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~313/SERIES_ENDED_CAUSE_R126.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~315/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-15.series-ended-read-record-cause-claim-inferred-one-line.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 14, cell `DB-i-15`.
<owned_cells>DB-i-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI128-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~315/IRPT_DASHBD.TO-DB-i-15.series-ended-read-record-cause-claim-inferred-one-line.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI128-1-AC1` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line, the `git diff --stat` of the record, and the commit ids. No client value, no account or household id, no date.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one key added to one data record; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call, no secret, no grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI128-1-AC1 FAILS at base (no cause_claim), PASSES on the record with the key (checked in the issuer's worktree), and FAILS on the record with the key set to measured.
</preflight>
