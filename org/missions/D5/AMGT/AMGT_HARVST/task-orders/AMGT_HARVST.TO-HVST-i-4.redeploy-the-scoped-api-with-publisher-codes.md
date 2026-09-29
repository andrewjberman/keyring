# AMGT_HARVST task order -- `HVST-i-4` -- ROUND 19 chain 1 of 1, cell 4 of 4: REDEPLOY THE SCOPED API -- both timeline routes serve the publisher codes

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-i-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide; no cron, alarm, monitor or cadence moves in this cell. The deploy-ledger census is re-read at the build (C2 denominator 19 at the cut).
comp-iam: RUN at L5 -- `comp-iam service opal-amgt-scoped-api`: 4 DynamoDB calls UNRESOLVED/UNGRANTED in lib/research/api/scoped_amgt.py, pre-existing and untouched. The new code reads the same chatter_daily object the deployed function already reads (gold grant landed by HVST-a-2), so NO IAM change.
comp-adversary: RUN at L5 -- the adversary is a HEAD build that ships another project's unlanded change on the shared function (one artifact serves AMGT_RESAPP's routes too), or a deploy that serves the new field against a daily part that lacks it. AC2 sweeps three RESAPP routes as controls; AC1 requires the served codes to equal the LANDED column on every day.
EGRESS CLASS, declared: (A) ONE S3 artifact write research/opal-amgt-scoped-api.zip (versioned; the prior VersionId, named on the halves, is the rollback target); (C) ONE safe-apply on infra/aws/terraform/harvest/ moving the scoped API's code only. No layer publish, no wheel download, no IAM change, no route change.
</preflight>

## 0. BEGIN ONLY WHEN ALL THREE HOLD

1. `HVST-i-2` and `HVST-i-3` are `complete` and merged on CLOUD. The spawn message names both merges.
2. BOTH never-widen halves for this act are COMMITTED, and the spawn message names both paths: the COO half
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round19/NEVER_WIDEN_HALF_COO_I4.md` and
   `1.0.0_SA_CTO~Z`'s half. **Act only inside them.** The halves name:
   - the closure diff against the deployed artifact, meaning every file the HEAD build ships that differs, by project;
   - the rollback VersionId;
   - the unzipped budget.
   If they conflict with this face, the halves win.
3. ONE NEVER-2 entry under `org/critical_paths/change_management/` is opened AND COMMITTED before the build, with its
   `.open_deploys/` sentinel, and reads back from HEAD.

## 1. THE CELL

`HVST-i-2` made the daily rule keep the covering publisher codes (`publishers_covered_codes`), and made
`lib/research/harvest/timeline_api.py` serve that column and the count on `/timeline` and `/timeline/day/{date}`.
`HVST-i-3` put a `chatter_daily` part carrying the column. **The deployed `opal-amgt-scoped-api` still runs the code
from before `i-2`,** so a user sees neither field. This cell ships that code.

**The acts, in order, under the ONE entry:**
1. Run `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only <tmp>` and print:
   - the closure diff against the deployed artifact (the VersionId the halves name);
   - the UNZIPPED total of the package and every layer, against 250 MiB.

   STOP on any difference the halves do not name.
2. Build and upload ONE artifact (record the prior VersionId), then ONE `safe-apply` on `infra/aws/terraform/harvest/`.
   Print the plan first. A plan that moves anything other than the scoped API's code is a REFUSAL: print it, stop,
   report.
3. Run AC1 and AC2. A FAIL after the apply is the ROLLBACK trigger named in the halves: re-point to the prior VersionId
   and `safe-apply` again, forward, then close the entry as ROLLED BACK.
4. Close the NEVER-2 entry in the same session.

## 2. BOUNDS

1. The acts above and nothing else: no runtime, memory or timeout change, no authorizer, no route, no IAM change, no
   layer.
2. **No S3 delete of any kind**, including a noncurrent artifact version. The prior version IS the rollback.
3. No vendor call, no portal promote, no push of a shared branch.
4. This function serves AMGT_RESAPP's page too. AC2 sweeps three of its routes as controls.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-i-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round19/checks/i-4.AC1.py</invocation><expect>AC1 RESULT: PASS (0 failure(s))</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-i-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round19/checks/i-4.AC2.py</invocation><expect>AC2 RESULT: PASS (0 failure(s))</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~A/AMGT_HARVST.TO-HVST-i-4.redeploy-the-scoped-api-with-publisher-codes.proof_of_spec.json`
with `to_id` `AMGT_HARVST.TO-HVST-i-4.redeploy-the-scoped-api-with-publisher-codes`. Report once, with:
- the closure diff and the unzipped total;
- the plan's resource list;
- both criteria's output;
- the NEVER-2 entry's open and close commits;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **A SEAT ORDER, not a worker's.** Rule 13 puts infra deploys with AE. It is issued to `0.7.0_AE_CloudOps~A`, the
   seat that ran `HVST-a-2` and AMGT_RESAPP ww-1 on this same function. The dispatch is a message to that live seat
   once section 0 holds; this seat does not spawn it.
2. **Base dry-runs, by this seat at the cut** (`round19/checks/i-4.AC{1,2}.base.txt`):
   - AC1 FAILS as expected, with 6 failures. Both fields are absent on 272 of 272 ASML_NA days and on `timeline_day`.
     Arm (2)-DENIED passes vacuously at the base (no codes anywhere) and is real only after the deploy.
   - AC2 FAILS as expected on its two build arms (code unmoved off `lg6NJ2JL...`; `61Fb7L90...` still latest). Its
     rollback-target arm and three RESAPP controls PASS.
3. **The rollback VersionId is re-read at signing.** `61Fb7L90ggUdpjcXaX4T8CcMgquyzn0U` (RESAPP ww-1, 19:15:40Z) is
   latest at the cut. A later RESAPP deploy changes it; the issuer then amends AC2's `PRIOR_VERSION` and `BASE_SHA`
   before the seat runs.
4. **The HEAD build ships whatever `lib/research/api/` and `lib/research/harvest/` carry at HEAD.** The COO half cards
   the closure diff by project, the lesson of the round-12 combined act (`HVST-a-2` AMENDMENT 2).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
**ISSUER CLOSE (`2.0.0_SA_COO~H`, 2026-09-29 ~22:1xZ):** LANDED by `0.7.0_AE_CloudOps~A` (msg 26740; entry `amgt-harvst-i4-scoped-api-publisher-codes-20260929` opened `3fc45f7c44`, CLOSED 3 of 3 at 22:01:54Z; seat work on trunk @`84548218ef`). Closure diff EXACTLY the 3 named files, 344 entries both sides; unzipped 253,470,431 of 262,144,000; plan 0/1/0, the function's code only. **Re-measured by the issuer on the served plane BEFORE the actor's report (21:58Z):** `i-4.AC1` PASS and `i-4.AC2` PASS (CodeSha256 `uv0oTSMa...`, new artifact `kABTI4Gu...` latest, rollback `61Fb7L90...` standing, RESAPP /thesis /overlay /peers 200). Instance VALID rc=0 by the issuer's own check. ONE REAL RUN `deliverables/2.0.0_SA_COO_H/round19/close_run_round19.py`: CLOSE RUN OK.
<status>complete</status>
<round>19</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
