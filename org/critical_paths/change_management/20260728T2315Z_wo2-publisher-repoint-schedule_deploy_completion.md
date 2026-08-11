# Deploy Completion Record
**Date opened:** 2026-07-28T23:15:00+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260811T143521Z
**Deploy:** WO-2 publisher functional+scheduled+run: re-point both legs (read portal/gold/mdpf/* derived, write opal-data-portal-v2/platinum/mdpf/{scope}/{type}.json), swap to egress role (old fenced role attached to nothing), flip mdpf_egress_live_serve_write_cosigned=true (Andrew 2157Z + CTO + COO 221211Z scoped platinum/mdpf/* ONLY), own 16:15Z daily ScheduleExpression, PIN-4 event log + R7 provenance stamp from birth.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: publisher rewrite + TF re-point/schedule/var-flip committed | hash pushed | 94952ba865 (rewrite + TF + var flip + ledger) + 5579fc381c (artifact hash), pushed | CLOSED 20260728T2316Z |
| L2 | activation | build-and-upload + targeted safe-apply (module.mdpf_publisher + schedule rule/target/permission + live-serve policy count 0->1) + 0-diff + tag | apply changed-set + 0-diff + live get-function-configuration (role=egress, env legs) + get-rule ScheduleExpression | apply 4add/1change/0destroy; 0-diff clean; live: role=opal-assets-mdpf-egress-publisher-role, CodeSha256 WSwmCWplyR1l8JiXTVijQsmynKldh297SJklzyWEL9M= @23:17:04Z, env GOLD/SERVE legs correct; rule cron(15 16 * * ? *) ENABLED; tag opal-assets-v0.35.0 | CLOSED 20260728T2318Z |
| L3 | verify-iam | applied battery on live primitives: live-serve policy reaches EXACTLY platinum/mdpf/* (any json/* reach = UNSIGNED = STOP); simulate one-resource-per-call + isolated positive control + context-entries; D-controls: both json/* explicitDenys on mdpf-daily-runner-ec2-role UNMOVED | get-role-policy JSON + simulate outputs + D-control get-role-policy | role carries exactly 2 inline policies; live-serve statements reach ONLY opal-data-portal-v2/platinum/mdpf/* (+conditioned ListBucket) -- zero json/* reach, COO scope holds. sim1 platinum PutObject=allowed; sim2 ISOLATED json/mdpf PutObject=implicitDeny; sim3 ISOLATED staging positive=allowed (one --resource-arns per call). D-controls: P0DenyJsonMdpfClobber20260728 + P0DenyLegacyPortfoliosClobber20260728 + R14 fence UNMOVED on live get-role-policy AND behaviorally exercised by both chain runs' AccessDenied WARNs tonight. | CLOSED 20260728T2319Z |
| L4 | exercise | PIN-1 pre-invoke report to CTO, then INVOKE ONCE; verify written set == pinned set d6c9562318 BOTH directions, ETag/size/vintage per object | invoke result + platinum listing + both-direction set diff | pre-invoke report sent 231944Z; invoked once 23:20Z: 11/11 published, all_present=true, 0 unrecognized. INDEPENDENT live-listing verify: tonight's 11 written keys == the pinned d6c9562318 set BOTH DIRECTIONS (pinned-not-written=[], written-not-pinned=[]); ETags match self-report; vintages match the pinned table (49f 07-27/28, inf 07-27, cot 07-27/24, global 07-27/28). _provenance stamp verified on served object (written_by/written_at/source_keys/source_vintages). Legacy underscore serve keys untouched by the publisher (global/aggregate_aua_timeseries.json LM 22:53:57Z = the legacy chain's own write). | CLOSED 20260728T2322Z |

## Log

- 20260811T143500Z SCHEMA-MIGRATE by 0.7.0_AE_CloudOps: log field added (pre-log-vintage sentinel crashed deploy_ledger.py close with KeyError) so the TOOL can perform the close
- 20260811T143521Z CLOSED -- all 4 legs proven
