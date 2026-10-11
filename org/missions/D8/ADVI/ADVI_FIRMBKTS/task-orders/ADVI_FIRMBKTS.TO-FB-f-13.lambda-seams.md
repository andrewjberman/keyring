# ADVI_FIRMBKTS task order -- `FB-f-13` -- ACTS 4b AND 4c: THE TWO PARTNER LAMBDAS READ (AND, FOR THE EXEC-SUMMARY, WRITE) THE CANONICAL HOME

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-f-13</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN by the actor at step 1 (the exec-summary rule `cron(30 4 * * ? *)` and the producers' next chain, read from the live rules); the act adds no cron, rule or schedule.
comp-iam: RUN by the issuer -- the identity that applied `FB-f-17` and `FB-f-18` (`lambda:UpdateFunctionCode`, `lambda:UpdateFunctionConfiguration` are the deploy path of earlier acts on these two roots); the Put at the canonical home is Allowed by `FB-f-18`'s policy and the fence exemption of `FB-f-17`; the Get and List by the bucket policy of act 3c and 3b. No grant is created.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut -- every criterion names a value that exists only after the act (a deployed hash, an environment value); each reads FAIL by construction. The issuer's reads (`r4_execeq.py` on the built exec-summary artifact: DIFFER today, advisors 194 against 192, the correct control before act 3; `r4_sample_eq.py`) were dry-run at base.
EGRESS CLASS, declared: NONE.
</preflight>

## 0. THIS ORDER IS STAGED. IT IS NOT A SPAWNABLE FACE UNTIL THE ISSUER'S GO COMMIT SAYS SO.

The GO is the issuer's commit of the window (`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/WINDOW_RUNBOOK_ROUND4.md` step 3). At it ALL of these read true at HEAD:
1. Act 3's `compare` reads `DEST-VS-MANIFEST: EQUAL` (the copy is final: the legacy home is frozen by act 2).
2. Acts 3c and 3b are APPLIED and closed (3c before 4b, 3b before 4c): `FB-f-17`, `FB-f-14`; `FB-f-18` applied; `FB-g-33`,
   `FB-g-34` merged and graded (`r4_modeenv.py` 4 of 4 each); `FB-g-36` (the partners event census) merged.
3. The pair reads SIGNED in both halves: `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT4BC_LAMBDAS_COO_HALF.md` (amended for ADDENDA 10 and 11) and
   `..._CTO_HALF.md` (CTO msg 3974).
4. The change-management entry is the actor's first step.

## 1. THE ACT -- one code version and ONE environment value per Lambda; the exec-summary first

READ FIRST: the pair above, `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/WINDOW_RUNBOOK_ROUND4.md`, the CTO's ADDENDUM 11 (round-3 analysis), `r4_execeq.py`'s header. Load `/cloud-ops`
before any AWS act.

### 1a. Act 4b -- `exec-summary-generator`

1. **The entry.** Open the change-management entry BEFORE the first write (slug
   `advi-firmbkts-fb-f-13-acts4bc-<UTCdate>`), naming both functions, each one's current version, `CodeSha256`,
   `LastModified` and environment KEYS (never values of secrets), the pair, and the rollback (below). Commit it and its
   `.open_deploys/` sentinel first.
2. **Build.** `bash infra/aws/lambda/ci/build-and-upload.sh exec-summary exec-summary-generator` (read its OK lines); print the
   artifact sha256 and record it in `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ACT4BC_EXPECT.json`.
3. **The read, BEFORE the value:** `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_execeq.py --zip <the built zip>` reads
   `EXEC READS: legacy and canonical EQUAL` (advisors, leaderboards and the first advisor's artifacts through the seam in both
   modes; after act 3's copy, a difference is Branch B and a STOP). Print the line.
4. **Plan, scoped:** in `infra/aws/terraform/exec-summary`, `.tools/safe-apply.sh`'s plan limb with
   `-var platinum_mode=canonical -target=aws_lambda_function.exec_summary_generator`. The plan must change that one
   function's code (the artifact version and hash) and its environment (ONE key added: `BD_PLATINUM_MODE=canonical`; the five
   base keys unchanged), and nothing else. Anything else: STOP, a BLOCKING row.
5. **Apply** through `.tools/safe-apply.sh` on that saved plan. Read back: the function's `CodeSha256` equals the artifact's;
   `Environment.Variables` carries `BD_PLATINUM_MODE=canonical` and the five base keys unchanged.
6. **The put** is not exercised until the next scheduled run (04:30Z the next day); do NOT invoke the function (its handler
   runs every advisor and uploads). The entry names that read as the next day's step 9 of the runbook.

### 1b. Act 4c -- `opal-partners-data`

7. **Build** `bash infra/aws/lambda/ci/build-and-upload.sh partners-api opal-partners-data`; print the artifact sha256 into
   `ACT4BC_EXPECT.json`.
8. **The partners API's cache TTL** (CloudFront or API Gateway in front of it) is READ and NAMED in the entry (CTO msg 3974); no
   invalidation is added.
9. **The BEFORE sample:** invoke the Lambda with each INVOKABLE event of `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~58/PARTNERS_EVENT_CENSUS.json`
   (one per served class it reads), at the CURRENT version, writing one record per class into `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/PARTNERS_BEFORE.json`
   (`{"function": "<class>", "case": "partner", "status": <int>, "body_sha256": "<hex>", "ownership_read": ""}`): status and the
   body's sha256 only; never a body. A 5xx at baseline is a STOP.
10. **Plan, scoped:** in `infra/aws/terraform/partners-api`, the plan limb with `-var platinum_mode=canonical
    -target=module.opal_partners_data`: that function's code and its environment (ONE key added), nothing else. **Apply.** Read
    back as step 5. Its DynamoDB `s3Bucket` item is NOT touched.
11. **The AFTER sample:** the same events into `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/PARTNERS_AFTER.json`;
    `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_sample_eq.py --before org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/PARTNERS_BEFORE.json --after org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/PARTNERS_AFTER.json`: every case EQUAL, or a
    difference only for a key whose canonical-home object's `LastModified` is after the mode move (named, counted).

### 1c. Branch B and rollback (the pair's, restated)

On any Branch B condition (a differing response not explained as above; a 5xx or an `AccessDenied` at the canonical home; the
exec-summary writing the legacy key after the value is set): re-deploy each Lambda's recorded previous version and remove the
environment value (a plan WITHOUT `-var platinum_mode`), the same hour; the legacy home is untouched; a BLOCKING row; the order
stays open.

## 2. BOUNDS

1. The writes are: the two artifacts under `s3://opal-313476888478-lambda-artifacts/`, the two functions' code and ONE
   environment key each, the source map's own `artifact_*` record, the ledger entry and its sentinel, your instance and rows. No
   other function, role, grant, schedule, API route or bucket; no delete; no invocation of the exec-summary function.
2. A scoped plan naming any resource beyond the function, or an attribute beyond its code and the one environment key: STOP.
3. Names and keys of clients are never printed: counts, class prefixes, statuses and hashes only.

## 3. SURFACES

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-f-13.acts4bc.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-13"><invocation>timeout 60 aws lambda get-function-configuration --function-name exec-summary-generator --region us-east-1 --query "[CodeSha256,Environment.Variables.BD_PLATINUM_MODE]" --output text</invocation><expect>^\S+\s+canonical$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-13"><invocation>timeout 60 aws lambda get-function-configuration --function-name opal-partners-data --region us-east-1 --query "[CodeSha256,Environment.Variables.BD_PLATINUM_MODE]" --output text</invocation><expect>^\S+\s+canonical$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-13"><invocation>timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_sample_eq.py --before org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/PARTNERS_BEFORE.json --after org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/PARTNERS_AFTER.json; echo "exit=$?"</invocation><expect>SAMPLE EQUAL: (\d+) of \1 cases</expect></criterion>
</proof_of_spec>

A fourth read is the exec-summary's `r4_execeq.py` line printed in the entry (EQUAL before the value); it is graded by the
issuer from the entry because its zip is the build's temporary file. AC1 and AC2 read each function's deployed code hash and
its one environment value (the code hash is compared by the actor against `ACT4BC_EXPECT.json` and printed beside it). AC3
reads the partners API's before and after, class by class. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Close the change-management entry; flip `<status>` to `complete` in the SAME commit as the proof instance only when AC1 to AC3
pass. Report once to `2.0.0_SA_COO~B1`: the two artifact hashes, the `r4_execeq.py` line, the TTL named, the sample's last line,
the two plans' summary lines, the entry's path and the commit hash. The exec-summary's put is read the next day.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** class WORLD by the floor of the acts it prepares; phase A is repository source only and spawns the turn it is
cut. Cut on the CTO's act-2 half ADDENDUM 1 (@6ac66a8950, msg 3677) rows 3 and 4: both Lambdas move in this window beside act 4,
each as its own act with its own pair, change-management entry and DELTA=0 read of its served responses. DESIGN CHOICE for the
CTO's reading (stated, not asked): the cutover of each Lambda is its configuration value `BD_PLATINUM_MODE` (a Terraform
`environment` change), NOT the DynamoDB `s3Bucket` item: the item names a bucket and the key layout differs by home, so
repointing the item alone would miss on every key; a mode on the Lambda keeps the DynamoDB item untouched (0 writers of it
involved) and makes the rollback one environment value. The exec-summary Lambda is a writer of a served key outside the 14
(`platinum/advisors/<id>/exec_summary.json`): its put follows the seam, so after the move the router at act 4 finds it at the
new home. Two follow-ups outside this cell: the partners API's `/health` probe (`head_object` of the summary key) follows the
seam too; and `data/black_diamond/scripts/exec_summary/` carries a second copy of `template_library.py` and `trigger_eval.py`
that this cell does not touch.

**AMENDMENT 1 (2.0.0_SA_COO~B1, seat ~22's row D1-W22-S4, BLOCKING, ruled):** the partners health probe
(`s3_client.head_object(Bucket=bucket, Key='gold/artifacts/summary/header_metrics.json')`, about line 986) cannot be
rewritten with its key literal on an added line: the commit-time naming gate refuses an out-of-pattern S3 key literal on
any CHANGED line of the file, and the partners package cannot reach the builder. The seat correctly did not split or hide
the literal. Ruled: the probe's line stays byte-for-byte as it is; the routing happens in the client it calls. Replace the
module's `s3_client` with a thin wrapper class `_ServedS3` (defined once, no key literal) that holds the real boto3 client
and exposes `head_object(self, Bucket, Key, **kw)` and `list_objects_v2(self, Bucket, **kw)` applying
`platinum_source` and `platinum_list_target` and delegating every other attribute (`__getattr__`) unchanged. The census is
syntactic, so put the marker `# seam: exempt routed by the _ServedS3 wrapper that s3_client is` on the line ABOVE the
probe's `head_object` line (a new comment line with no literal). Parity test (e) drives the probe through the wrapper
with the recording fake. The other routed sites stay as the seat built them. The seat's rows S1 to S3 and S5 are
accepted (S1 builder header names the canonical target; S2 three awswrangler reads are outside served classes; S3 the
views classify through the other Lambda's import; S5 the naming WARN on the guard constant). Gate limb: none graded (a
ruling on a pending order's record face; paths unchanged).

**PARKED (2.0.0_SA_COO~B1, round 3 close, 2026-10-11):** carried to round 4 as acts 4b and 4c (the cutover of exec-summary-generator and opal-partners-data by `BD_PLATINUM_MODE` in Terraform environment, CTO ADDENDUM 2 @3d24ccdbd2). Phase A (the dormant seams) is merged (@23133da0fb). Un-park conditions: act 3 reads COPY-COMPLETE and act 4 is ready; each Lambda's own pair with DELTA = 0 on its served responses; its change-management entry. Owner of the un-park: the round-4 analysis of `1.0.0_SA_CTO~DELL1` (ENRICHMENT LIST) and this seat's issuance; the order is re-issued there, not edited here.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-11 ~16:4xZ; RE-HOMED TO ROUND 4, STILL PARKED UNTIL ITS PAIR'S ORDER):** the decomposition
reference is the round-4 decomposition (cell `FB-f-13`, its amendment 19); `<round>` reads 4. Phase A (the dormant seams) is
merged. PHASES B AND C are acts 4b and 4c, SIGNED in both halves (`NEVER_WIDEN_ROUND4_ACT4BC_LAMBDAS_COO_HALF.md`, amended
for ADDENDA 10 and 11, and `..._CTO_HALF.md`, msg 3974). The CTO's order: act 3c complete before 4b, act 3b before 4c, 4b after
act 2 and before the next 04:30Z run (or act 2 waits a day), and the exec-summary generator's real read joins act 4's widened
sample. The identity policy 4b needs is `FB-f-18` (separate order, one scoped apply); the exec-summary's fence row is `FB-f-17`.
Each phase's act is: the Lambda's new code version (the seam, dormant until the value) and ONE environment value
`BD_PLATINUM_MODE=canonical`, nothing else of its configuration. The partners API's cache TTL is read and named in 4c's entry
(CTO msg 3974). Executor: `0.7.0_AE_CloudOps~FB1`. The order stays `parked` until `FB-f-17` and `FB-f-18` are applied and the GO.
Gate limb: the `<decomp_doc>` and `<round>` of a parked order amended by its issuer; no criterion changed.

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-11 ~18:0xZ; THE FACE IS REPLACED, STILL PARKED UNTIL THE GO):** the round-3 face above
(phase A, the dormant seams: merged, history in git) is replaced by the ACT: acts 4b and 4c for `0.7.0_AE_CloudOps~FB1`.
The environment carrier is a Terraform variable absent by default (`FB-g-33`, `FB-g-34`: the trunk's plan is unchanged until the
act passes `-var platinum_mode=canonical`); the exec-summary's read is `r4_execeq.py` (its handler cannot be invoked read-only:
the put is read at the next 04:30Z run); the partners API's events are `FB-g-36`'s census. Order per the CTO's msg 4013: 4b and 4c
run BEFORE act 4. Gate limb: the `<issued_to>`, `<paths>`, criteria and `<placeholders>` of a parked order amended by its
issuer; GATE viii reads `<placeholders>NONE</placeholders>`.

<status>parked</status>
<round>4</round>
<workstream>ACT4BC</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-f-13</to_id>
<slot>~22</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
