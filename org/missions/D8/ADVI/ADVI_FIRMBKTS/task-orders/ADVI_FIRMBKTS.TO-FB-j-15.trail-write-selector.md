# ADVI_FIRMBKTS task order -- `FB-j-15` -- THE ORGANIZATION TRAIL RECORDS OBJECT WRITES ON THE THREE LEGACY BUCKETS (DEC-12, FWD-6's WRITE INSTRUMENT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-15</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FBL</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed; one CloudTrail event selector is added.
comp-iam: RUN by the actor at step 0 -- the laptop identity's `cloudtrail:PutEventSelectors` and the trail's bucket-side permissions by simulate, one resource per call, a positive control in its own call. The Dell users cannot make this change (CloudTrail write is a kept deny); that is why the order goes to the laptop.
comp-adversary: RUN by the issuer -- at base (the live trail, read from dell1 at 2026-10-13 ~20:3xZ: two selectors, the management one and a ReadOnly one on four buckets) AC1 reads FAIL ("write selector missing"); a hand-built three-selector document reads OK, and one whose write selector lists a fourth bucket reads FAIL. Blindness: the check reads the selectors, not that events arrive.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- add the write-event selector to the organization trail (the laptop CTO's infra-lane ruling, bus 671c3981, relayed by the dell1 manager as msg 5135)

Why: FWD-6 asks that nothing wrote to a legacy home during the quiet window. Reads on the legacy buckets are recorded; object WRITES are not
(the PRD's DEC-12). Andrew ruled DEC-12 YES (~20:0xZ, the CTO's record `ANDREW_DIRECT_20261013_200xZ_NINE_OPEN_CALLS_ANSWERED_FIRMBKTS_DEMQUE_BRIEF_HARVEST.md`).

In `infra/aws/terraform/shared-infra/cloudtrail-organization-trail.tf` (the resource `aws_cloudtrail.organization`, the untagged provider alias) add a THIRD basic `event_selector`:

```
read_write_type           = "WriteOnly"
include_management_events = false
data_resource { type = "AWS::S3::Object"   values = the ARNs "arn:aws:s3:::opal-data-bd/", "arn:aws:s3:::opal-data-inf/", "arn:aws:s3:::opal-data-cot/" }
```

Basic selectors are kept (never convert to advanced); no wildcard and no prefix over `opal-data-*`; `opal-data-49financial` is NOT on the write list (its served-key writes
have their own trail). The two existing selectors stay byte-unchanged. Declare the three buckets in a new local beside `org_trail_read_logged_buckets`, with a comment naming DEC-12.

Steps:
0. **Before:** `aws cloudtrail get-event-selectors --trail-name opal-organization-trail --region us-east-1` saved in your folder as `TRAIL_SELECTORS_BEFORE.json` (the rollback: it is the prior state); the step-0 simulate pairs named above.
1. **Ledger** (NEVER-2) with its `.open_deploys/` sentinel BEFORE the apply: the trail, the prior selectors, the rollback (remove the third selector block and apply, or `put-event-selectors` with the saved prior document), the cost note (write data events are billed; Andrew ruled DEC-12 YES on that basis).
2. **Plan:** `bash .tools/safe-apply.sh` plan limb in `infra/aws/terraform/shared-infra` with `-target=aws_cloudtrail.organization`: `0 to add, 1 to change, 0 to destroy`, the one change the new selector. Anything else (a diff on the other selectors, a tag diff, a replace): STOP, a BLOCKING row. Apply on that saved plan.
3. **Read back:** `get-event-selectors` saved as `TRAIL_SELECTORS_AFTER.json`; the trail still `IsLogging` true.
4. **Stamp:** print the apply's UTC time. It is FWD-6's observed-live stamp for the write instrument; do not edit any other file with it.
5. **Close** the ledger entry.

## 2. BOUNDS

1. One resource (`aws_cloudtrail.organization`) changes; no bucket, key, KMS key or bucket policy of the trail's log bucket is touched.
2. No Terraform apply outside `safe-apply`; `MSYS_NO_PATHCONV` only where the tooling needs it.
3. Do not touch `opal-data-inf` contents: this order reads and writes no object there.

## 3. SURFACES

<paths>
infra/aws/terraform/shared-infra/cloudtrail-organization-trail.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ADVI_FIRMBKTS.TO-FB-j-15.trail-write-selector.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-15"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 100 .tools/aws cloudtrail get-event-selectors --trail-name opal-organization-trail --region us-east-1 --output json | timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py trailsel</invocation><expect>^TRAILSEL: OK selectors=3 write_buckets=3$</expect></criterion>
</proof_of_spec>

AC1 reads the live trail's selectors: the management selector and the read selector unchanged, the third WriteOnly on exactly the three buckets.

## 5. WHEN YOU ARE DONE

Close the ledger entry; flip `<status>` to `complete` in the SAME commit as the proof instance only when AC1 passes. Row ids `ADVI_FIRMBKTS-D1-S<k>`. Report once to
`2.0.0_SA_COO~B1` through the laptop manager: the apply UTC, the plan line, the after-read, the entry's path and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a cell added to round 7 by the laptop CTO's infra-lane ruling (bus 671c3981; dell1 msg 5135) on Andrew's DEC-12 YES (the CTO's msg 5128). It is a
cross-box order to a laptop seat, an exception to the pivot's "no CloudOps order from a Dell-placed project to a laptop seat" that the laptop CTO's ruling names
(the Dell users cannot do the write). Round 7's spec is otherwise frozen; this cell serves FWD-6's instrument only and is independent of FB-j-3/-4/-7. WORLD by the
change to a shared audit trail; the ruling and the Andrew word are the authority; no served output moves.

<status>complete</status>
<round>7</round>
<workstream>TRAILWRITE</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-15</to_id>
<slot>~FBL</slot>
<fabric>laptop</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
