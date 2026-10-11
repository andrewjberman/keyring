# TO IRPT_DASHBD.TO-DB-b-131 -- account-number-shaped values in served manifests, sized: the thresholds file inside the LIVE function's package read by content, and ONE recent 49 Financial daily returns manifest -- key names and counts only, no value printed or kept

<to_id>IRPT_DASHBD.TO-DB-b-131</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~105</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-69 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_69_20261011.md` @90cb3e774b, section 4 item 1, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v28.md` @595332678c | **Rows:** IRPT_DASHBD-D2-W100-S3, IRPT_DASHBD-D2-W100-S2 | **Decomp cell:** `DB-b-131` (decomposition section 72) | **outcome_ref:** FWD-11 | **depends_on:** none; it runs FIRST.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-105` (branch `wk-irpt-dashbd-70-105`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~105/`. Read first: section 2 (item 1) of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v28.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**Why this is first.** The reviewer read 49 Financial's served method row 2 manifest: a thresholds object of 24 keys, two named
`per_account`, and 12 digit runs of 8 or more. The code copies the WHOLE thresholds object into every daily returns manifest too, so whether
one served object carries those or thousands depends on the thresholds file inside the LIVE function's package, which nobody has read by
content (row W100-S2). The CTO: "A read first, counts and key names only, no value printed or kept."

**The cell (`DB-b-131`).** Read-only. You change no code. Record `PACKAGE_AND_MANIFEST_READ.json` in your folder.
1. **The live package.** `get-function`; record `live` {code_sha256, last_modified}. Download the package to
   `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~105/`, open it (python `zipfile`), find the thresholds file the handler reads
   (`thresholds_path()` in `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` names the bundled path). `package`: {read,
   file_in_package, sha256, key_names (TOP-LEVEL key names only), key_count, digit_runs_8plus (count, over the whole file's text, of runs
   of 8 or more digits), five_values_equal_to_tracked}. The last member compares ONLY the five threshold values
   (tolerance, large_flow_share, plausibility_band_low, plausibility_band_high, comparability_max_excluded_weight) with the tracked file
   `data/assets/scripts/gold/irpt_reporting/MEASURED_THRESHOLDS_R1.json`: true, false (then `differing_keys`, names only) or
   "NOT_ESTABLISHED".
2. **ONE daily returns manifest.** The most recent trading day's `manifest.json` for 49 Financial. `returns_manifest`: {read, day,
   key_names (the top-level key names of its `thresholds` object), key_count, digit_runs_8plus (over that object's text)}.
3. **Nothing kept.** If a top-level key NAME itself holds a run of 8 or more digits, write it as `<digits>` and count it. No value of any
   key is printed, logged, reported or written into the repo; the downloaded files stay outside the repo. `values_kept: 0`,
   `s3_writes: 0`. The check refuses a record that holds any run of 8 or more digits (members named `*sha256` excepted).

<criterion id="DB70-1-AC1" cell_refs="DB-b-131"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r70/p70_round70.py" . DB70-1-AC1</invocation><expect>DB70-1-AC1 PASS</expect></criterion>
`DB70-1-AC1` -- the live package's thresholds file and one recent daily returns manifest are each read for their top-level key names and their count of long digit runs, with no value kept. Base: FAIL.

<expected_criteria>DB70-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim, and nothing else: `lambda get-function` of the ONE function `irpt-49f-reporting-gold-lambda` (its `Code.Location` is a short-lived link to the package: download it with curl to the folder outside the repo); and, for ONE recent trading day, a `head-object` / `get-object` of the ONE `manifest.json` of 49 Financial's `account_return_daily` partition for that day (its address from the producer's own builder, never typed; no `data.parquet` and no other key). A denial is recorded verbatim, not retried by another route, and that part reads `read: false` with its `reason`.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~105/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W105-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~105/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-131.package-thresholds-and-one-manifest-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 72 (round 70), cell `DB-b-131`.
<owned_cells>DB-b-131</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB70-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~105/IRPT_DASHBD.TO-DB-b-131.package-thresholds-and-one-manifest-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB70-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; for the package and for the manifest: whether it was read, the top-level key NAMES of the thresholds object, the key count and the count of digit runs of 8 or more (never a value); whether the package's five threshold values equal the tracked file's; what is live (CodeSha256); everything not read and why; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; two reads; nothing served is written.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one function read and one object read; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
