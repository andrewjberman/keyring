# Deploy Completion Record
**Date opened:** 2026-09-01T16:11:32.815825+00:00
**Status:** OPEN
**Deploy:** ADVI_INSURE INS-b-1: additive s3:GetObject on the two 49F insurance silver prefixes for bd-exporter-ec2-role (the gold chain runner could not read its own input)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 36.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | apply triple is exactly 0 added / 1 changed / 0 destroyed with ONE address | the safe-apply output captured to a FILE; any other triple is a STOP with the output pasted, no retry | PASSES on the gate's exact triple. safe-apply rc=0, full output captured to a FILE and read unfiltered (the P2F-3b lesson -- never grep away an rc). 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' ADDRESS CHECK: exactly ONE address in the plan and in the apply -- aws_iam_role_policy.bd_exporter_advi_49f_chain, Modifying.../Modifications complete after 0s. The apply consumed a SAVED PLAN FILE (insurance-read.tfplan, 181205 bytes) rather than re-planning, so the applied change is byte-for-byte the reviewed plan; terraform's own warning that it 'can't guarantee to take exactly these actions' applies only to the unsaved form and was deliberately avoided. Change census over the whole plan output: 8 lines, ALL '+', ZERO '-'. HALT-GATE fired and BLOCKED the first attempt on 2 pending messages; both were READ before HALT_ACK=1 -- a CTO MEASURE REQUEST (22h) and the CTO's own STAND DOWN (20h) superseding it, neither STOP-class, neither touching ADVI_INSURE, both addressed to the BASE serial not this lane. comp-tagauthz gate PASSED (0 candidates overwrite an access-granting tag; SCPs NOT APPLICABLE -- account not in an Organization, stated not implied). tombstone-gate CLEAN. | CLOSED 20260901T162348Z |
| L2 | verify | live read-back: the new Sid present AND the 11 pre-existing statements set-identical | get-role-policy on the applied plane, both lists printed with denominators | PASSES on the live plane. get-role-policy on bd-exporter-ec2-role/advi-49f-chain-access after the apply: TWELVE statements. The ELEVEN pre-existing Sids are SET-IDENTICAL to the pre-apply read -- symmetric difference is EMPTY, computed as a set rather than eyeballed. The new AdviChainBd49fInsuranceSilverRead is present with Action ['s3:GetObject'] and exactly the two intended Resources (fact_insurance_relationshipaccountdetailsearch/* and fact_insurance_insurancerelationshiplist_export/*), and Condition NONE -- deliberately no prefix condition on GetObject, because a conditioned GetObject false-denies on a key read carrying no prefix context, which is the defect class this whole entry exists to fix. FUNCTIONAL CONFIRMATION, diagnostic not acceptance: comp-iam simulate now returns ALLOWED on the APPLIED plane for BOTH keys with the control allowed in the same invocation. NEVER-WIDEN PROVEN AT THE RESOURCE LEVEL: a SIBLING prefix under the same leaf that I deliberately did NOT grant -- fact_insurance_relationshipdetail -- still returns implicitDeny, control-proven. Had the grant been written to the 49financial/silver/ leaf that sibling would now read allowed. It does not. | CLOSED 20260901T162349Z |
| L3 | verify | post-apply targeted re-plan 0-diff | No changes. Your infrastructure matches the configuration. | PASSES. Post-apply targeted re-plan, same 1.9.8 binary, same -target: 'No changes. Your infrastructure matches the configuration.' = 0-diff. | CLOSED 20260901T162349Z |
| L4 | activation | THE ACCEPTANCE: a REAL READ by the runner on a scheduled chain fire, NEVER a simulate allowed | the chain run log showing the insurance stage reading both silver keys and emitting the gold partition; simulate is the diagnosis, not the proof |  | OPEN |
| L5 | git | CLOUD commit of the iam.tf change plus this ledger | commit hash plus push state MEASURED by ls-remote with a positive control | TWO commits, both authored via .tools/safe-commit.sh -F with the message file written by the Write tool (non-shell writer, Rule 14a). 03bcc7e3a4 = the iam.tf change plus this ledger's open, committed BEFORE the irreversible act so the record could not be stranded by it. 8295e4f8b8 = the apply record with L1/L2/L3 closed. PUSH STATE MEASURED 2026-09-01T16:28:28Z, not defaulted: git ls-remote origin refs/heads/CLOUD = 12c2996fd0df3b5356a8117c512253e3d6bc5168; 03bcc7e3a4 reads ON origin/CLOUD by merge-base --is-ancestor (an integrator ran between the two commits), 8295e4f8b8 reads LOCAL and rides the next integration window. POSITIVE CONTROL: the repo root commit reads ON with the same instrument. NEGATIVE CONTROL: HEAD is ahead of origin, so a LOCAL verdict is a real verdict rather than a broken comparison. Publication is the integrator's act -- LD-0367/LD-0368 make shared-branch push integrator-only and that gate refused this seat by name earlier today; no override was used. THE CLAIM IS PERISHABLE and ages the moment an integrator runs. | CLOSED 20260901T162906Z |

## Log

- 20260901T161132Z OPENED by 0.7.0_AE_CloudOps with 5 leg(s)
- 20260901T162348Z LEG L1 closed: PASSES on the gate's exact triple. safe-apply rc=0, full output captured to a FILE and read unfiltered (the P2F-3b lesso
- 20260901T162349Z LEG L2 closed: PASSES on the live plane. get-role-policy on bd-exporter-ec2-role/advi-49f-chain-access after the apply: TWELVE statemen
- 20260901T162349Z LEG L3 closed: PASSES. Post-apply targeted re-plan, same 1.9.8 binary, same -target: 'No changes. Your infrastructure matches the confi
- 20260901T162906Z LEG L5 closed: TWO commits, both authored via .tools/safe-commit.sh -F with the message file written by the Write tool (non-shell write
- 20260903T080000Z ANNOTATED by 0.7.0_AE_CloudOps~R -- NEVER-2 ROLLBACK TAKEN UPSTREAM; THIS ENTRY STAYS OPEN AND L4 IS STRANDED.
  Issuer: 2.0.0_SA_COO operating note 93306 (+ pointer 93324), READ-acked by this lane before the work; MSTR 93301 concurred.
  WHAT CHANGED: the ("insurance_nav_current", ...) stage tuple in data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py
  is DISARMED (commented out with a dated block) at commit 530977130b, deployed to s3://opal-data-49financial/_code/ via
  .tools/safe-deploy.sh rc=0 ("deployed and verified", comp-pipescript MATCH). INDEPENDENTLY VERIFIED against the SERVED
  artifact rather than the tool's self-report: served sha256 037541a7a771e098... == the blob at 530977130b, and DIFFERS from
  the pre-disarm blob e65edcda3c9e9a43... (negative control); served object VersionId 0hgfQygK4Dgb_MgWnMRrCvrmV5UQhJq5,
  LastModified 2026-09-03T07:59:44Z; an AST parse of the SERVED bytes shows 15 in-loop stages ending at c02_twr_daily with
  insurance_nav_current ABSENT.
  WHY: 3 of 3 post-arm scheduled fires CHAIN ABORT rc=1 at stage=insurance_nav_current (chain_20260901T214645Z,
  chain_20260902T094636Z, chain_20260902T124542Z), against a clean PRE-arm control (chain_20260901T124542Z, 18 STAGE OK,
  0 ABORT). The abort is fail-fast and also took c04_validation and perfrp_projection on every fire.
  THE FAILURE IS NOT THIS ENTRY'S GRANT. Root cause read at source in bd49f_insurance_nav_current.py:88-112 @c08c1bbe99:
  _workspace_root() raises when no org/ dir is found above the file, and _SILVER_HOME calls it at MODULE LEVEL, so the
  producer dies at IMPORT in the flat /tmp/advi_49f_code bundle -- before argparse, and before any S3 read is attempted.
  The IAM grant this entry records stays APPLIED and is NOT withdrawn; nothing was widened or narrowed by the rollback.
  L4 STATUS: STRANDED, not failed and not superseded. Its acceptance is a REAL runner read on a scheduled fire, which
  cannot occur while the stage is disarmed. THE WORLD IS NOT DONE -- do not close this entry SUPERSEDED.
  L4 RE-ARM RIDES: the runner import-safety fix (acceptance exercised in a FLAT temp dir, not the repo), then re-arm through
  ledger advi-insure-gold-chain-membership. That fix is ADVI_INSURE forward work and was explicitly NOT done under the note.
  SURFACED TO THE ISSUER, NOT SELF-ADJUDICATED: this entry is past its 36h window and is now firing RED daily as an AGED
  OPEN (last_red_at 2026-09-03T07:18:07Z), which mis-describes it -- L4 is blocked on a NAMED future event, not neglected.
  `deploy_ledger.py hold --gate-type external --gate-ref "<the runner import-safety fix + re-arm>" --reread-event "..."`
  is the state that would say so, and it re-surfaces as HELD-PAST-REREAD rather than as an aged OPEN. NOT APPLIED HERE
  because the operating note said in terms "it stays OPEN"; the status change is 2.0.0_SA_COO's call, not this lane's.
- 20260903T114500Z ANNOTATED by 0.7.0_AE_CloudOps~R -- THE ROLLBACK THAT STRANDED L4 IS NOW ACCEPTED.
  0.0.0_AB_MSTR 93554 ruled the NEVER-2 rollback ACCEPTED under /govern on the artifact, against the
  predicate fixed before the fact (93301 item 4 / 93348): s3://opal-data-49financial/gold/advi/_logs/
  chain_20260903T094640Z.log -- 18 STAGE OK, 0 CHAIN ABORT, "CHAIN OK date=2026-09-02 wall=152.9s",
  header stages=17 (was 18: the disarm visible in the RUNNING declaration), zero "insurance" tokens,
  downstream gold written inside the run window (canonical/twr_daily/date=2026-09-02 @09:49:05Z,
  dimensions/dim_asset_classification/date=2026-09-02 @09:48:54Z). A scheduled production fire on the
  deployed bytes, not a hand-run.
  THIS DOES NOT CLOSE L4 AND IS NOT A CLOSE OF THIS ENTRY. L4's proof is a REAL insurance-runner read
  on a scheduled fire; the stage is disarmed, so no such read occurred or could. The rollback being
  ACCEPTED and L4 being CLOSED are different objects and are not conflated here. gold/advi/insurance/
  insurance_nav_current/ remains its single date=2026-08-25 object -- a disarmed stage wrote nothing.
  STATUS UNCHANGED AND DELIBERATELY SO: OPEN, past window, firing RED daily -- which by the ledger's
  own guardrail (_qualifies_as_held (a): an open leg of kind != verify IS a half-landed deploy) is the
  DESIGNED signal and not noise. 2.0.0_SA_COO 93381 withdrew the 93365 hold word on exactly that
  reading and recorded the RED as expected. The tool refuses HELD here and no override was attempted.
  93554 item (1) asks for a DISPOSITIONING act recording L4's close as ROLLED-BACK with the re-arm
  riding advi-insure-gold-chain-membership under a fresh L4. THAT ACT IS NOT TAKEN HERE: the leg
  vocabulary has {closed-with-proof, open} and no member for "activation attempted, failed,
  deliberately rolled back" (the Rule 24 (i) residual already on the record as ADVI_INSURE-S12), so
  every available verb would assert something false. Surfaced to 2.0.0_SA_COO as the router; this lane
  annotates and does not invent a disposition.
  Rollback commit 530977130b; deploy served-verified 2026-09-03T07:59:44Z; acceptance ruling 93554;
  channel rows ADVI_INSURE-S12/S13/S14 @a432f0b6de, @3595675047, @15ba87a50b.
- 20260910T0055Z ANNOTATED by 0.7.0_AE_CloudOps~W -- THE GRANT IS APPLIED, RE-MEASURED ON THE LIVE
  PLANE. Routed here by 2.0.0_SA_COO's 19:20Z RED scan as item 4, whose routing line attributes to
  this entry a reading of "the iam.tf grant measured DESIRED-NOT-APPLIED" from 0.0.0_AB_MSTR's 09-07
  device-death scan. I DID NOT TAKE THAT READING ON TRUST, because it contradicts this entry's own
  L2, and a contradiction between two records is exactly where a measurement belongs.
  MEASURED 2026-09-10T00:5xZ, `iam get-role-policy` on bd-exporter-ec2-role / advi-49f-chain-access:
  TWELVE statements on the applied plane, and `AdviChainBd49fInsuranceSilverRead` is PRESENT with
  Action ["s3:GetObject"], Condition NONE, and exactly the two intended Resources --
  opal-data-assets/blackdiamond/49financial/silver/fact_insurance_relationshipaccountdetailsearch/*
  and .../fact_insurance_insurancerelationshiplist_export/*.
  So L1/L2/L3 stand as closed and the grant is APPLIED, not DESIRED. The DESIRED-NOT-APPLIED phrase
  describes a DIFFERENT grant -- MSTR's 09-07 log recorded it of the NFRA_OUTSET `outset/*` statement
  that was edited-and-uncommitted in the main tree that night, which this seat has since applied under
  its own orders. Two grants in one iam.tf, one sentence, and the sentence travelled to the wrong one.
  NEVER-WIDEN STILL HOLDS AT THE RESOURCE LEVEL, by inspection of the applied statement rather than by
  a simulate: the sibling prefix fact_insurance_relationshipdetail under the same leaf is NOT among
  the two Resources. Had the grant ever been rewritten to the 49financial/silver/ leaf it would be.
  THE ENTRY STAYS OPEN AND L4 STAYS STRANDED. Nothing here moves L4: its acceptance is a REAL runner
  read on a scheduled chain fire, which cannot occur while the insurance_nav_current stage is
  disarmed. The prior lane's judgement stands -- do NOT close this SUPERSEDED, because the world is
  not done.
  ⛔ WHAT ANDREW'S NO-WAITING WORD (~21:4xZ 09-09) DOES AND DOES NOT REACH HERE: L4 is pending a
  future SCHEDULED run, which is precisely the shape that word says must get a manual trigger. But the
  manual trigger for L4 is a chain run with the insurance stage RE-ARMED, and that needs the runner
  import-safety fix first (bd49f_insurance_nav_current.py:88-112 @c08c1bbe99 -- _SILVER_HOME calls
  _workspace_root() at MODULE level, so the producer dies at import in the flat bundle). That fix is
  ADVI_INSURE forward work and is not in this seat's hands under any order it holds. So this lane
  RECORDS the applicable trigger rather than firing one: re-arm, then a manual chain run, then L4.
  Status: the honest state is HELD on an external gate, not an aged OPEN -- `deploy_ledger.py hold
  --gate-type external`. That status change is 2.0.0_SA_COO's call, as the prior lane also found; it
  is surfaced again here and not self-adjudicated.
