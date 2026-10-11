# TO IRPT_DASHBD.TO-DB-b-125 -- the 49 Financial thresholds file: each threshold carries its claim, the file is tracked where the handler reads it, and its sha256 is recorded against the served copy

<to_id>IRPT_DASHBD.TO-DB-b-125</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~100</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-68 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_68_20261011.md` @0005d9fd9a, section 4 item 2, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v27.md` @806d057711 | **Rows:** IRPT_DASHBD-D2-W85-S1; and a NEW row the worker files for the first half (the live thresholds file carries no claims) | **Decomp cell:** `DB-b-125` (decomposition section 70) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-124 (its read of row W85-S1).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-100` (branch `wk-irpt-dashbd-68-100`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~100/`. Read first: section 2 (item 3) of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v27.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**What is wrong, in two halves.** (a) Row W85-S1: `MEASURED_THRESHOLDS_R1.json` is tracked at neither path `handler.thresholds_path()`
reads, so a kit run refuses without an untracked copy, and whether that copy equals the one the served gold is graded against is not
established. (b) The CTO's item 3: the live 49 Financial thresholds file carries NO claims; no row carried that half, so you file it
(ids `IRPT_DASHBD-D2-W100-S<k>`) before you fix it.

**The cell (`DB-b-125`).**
1. Read `thresholds_path()` and every path it tries (`handler_paths`: [{path, file, line}]).
2. Read the producer's claim vocabulary and how it consumes a thresholds input (`THRESHOLD_CLAIMS`, `threshold_claims_of` in
   `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`): a thresholds input may state a claim per value under `threshold_claims`.
3. Place the file, TRACKED, at ONE of the handler's paths (`tracked_at`), carrying the five thresholds and, for each, its claim
   (`measured` / `inferred` / `held` / `absent`) with a one-line reason drawn from where the number came from (the measurement record that
   produced it: find it; a number whose origin you cannot find is `held`, and you say so). `claims`: {key: {claim, reason}}. Change no
   threshold VALUE.
4. The served copy: its address, one read, its sha256 (`served_copy`); `tracked_sha256`; `equal_to_served` true / false /
   "NOT_ESTABLISHED" with `equal_reason`. If they differ, do NOT overwrite either: say which values differ (keys only) and file a row.
5. A test under `data/assets/scripts/gold/irpt_reporting/tests/` showing the handler resolves the tracked file and the producer reads its
   five claims. `tests` {passed, failed}; the folder's existing tests must not newly fail. `s3_writes: 0`.

<criterion id="DB68-2-AC1" cell_refs="DB-b-125"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r68/p68_round68.py" . DB68-2-AC1</invocation><expect>DB68-2-AC1 PASS</expect></criterion>
`DB68-2-AC1` -- the thresholds file is tracked at a path the handler reads, carries a claim per threshold, and is compared by hash with the served copy. Base: FAIL.

<expected_criteria>DB68-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Risk class WORLD by the issuance gate's floor** (the grant names a path under `infra/aws/lambda/`); the cell itself deploys nothing: the tracked file ships only with a later release under its own pair.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. ONE AWS read is allowed: a `head-object` / `get-object` of the ONE served thresholds object the handler reads (its address from the handler's own code or the builder, never typed); the body is saved outside the repo; a denial is recorded and the comparison reads NOT_ESTABLISHED.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~100/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W100-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~100/
infra/aws/lambda/investor-reporting/reporting-gold/
data/assets/scripts/gold/irpt_reporting/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-125.thresholds-file-claims-tracked.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 70 (round 68), cell `DB-b-125`.
<owned_cells>DB-b-125</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB68-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~100/IRPT_DASHBD.TO-DB-b-125.thresholds-file-claims-tracked.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB68-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the paths the handler reads (file:line); where the file is tracked now; the five claims with the reason for each; the served copy's address, whether it was read, both hashes and whether they are equal; the tests; and any row ids (including the new row for the missing claims).

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a tracked data file and its claims; nothing served is written, the served copy is only read and hashed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one single-object read; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
