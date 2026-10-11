# ADVI_FIRMBKTS -- round 3 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-11T11:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T11:45:00Z. L8 packet: 2.0.0_SA_COO~B1 msgs 3790 and 3806, `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/R3_CLOSE.md` @4199237975 (blob 84e3c1f153, 16,039 bytes; first read @5c50521a0c, blob bf91b649ae).
13 orders: 9 complete (TO-FB-f-12 completed after the close), 4 parked. round-close-check --round 3: proof_ok 9, MAY-CLOSE.

**L9:** every recorded criterion of the orders complete at the close re-run at HEAD 7664786060: all PASS. FWD-1 PARTIAL on this
seat's count (all four 184 of 209, both right 182 of 207, contents agree, independence NOT MET). Act 1 read live: router v27 and
guard v6 as recorded, the distribution unchanged since 08:22Z, the ACL's LockToken unchanged, a no-session request 401 (D1-C-S16).
TO-FB-f-12 read live: the role's trust is sns.amazonaws.com only, retention 14 on both log groups; the account's SMS attributes are
NOT readable by this seat (D1-C-S25).

**L10: precondition met; the slug is sent.** The four parked orders sit outside the round by the CTO's ruling (D1-C-S17, residual
stated).

**Rows:** 110 undispositioned since v3's watermark. 74 dismissed, 36 graduated to `remediations/REMEDIATION_v4.md` (17 to
2.0.0_SA_COO~B1, 15 to 1.0.0_SA_CTO~DELL1, 3 to 0.0.0_AB_MSTR~DELL1, 1 to 0.7.0_AE_CloudOps; D1-S17 and D1-S19 stay ARMED with their
disarm owners), plus the new D1-C-S21 (to 2.0.0_SA_COO~B1). REMEDIATION_v3: 8 rows REMEDIATED (D1-C-S24).

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-C-S14",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:45:00Z",
    "one_line": "ROUND 3 L9 (packet org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/R3_CLOSE.md @4199237975 (blob 84e3c1f153, 16,039 bytes; first read @5c50521a0c, blob bf91b649ae)): every recorded criterion of the 8 orders complete at the close re-run by this seat at the merged HEAD 7664786060 (main checkout, 11:11Z), all PASS: FB-f-1 LIVE 3 of 3 and MUTANT 2 of 2; FB-f-2 structure 5 of 5 and repair 5 of 5; FB-f-3 and FB-f-4 3 of 3 each (each reader directory holds exactly LOCATIONS.json and its answers file); FB-f-5 OWNFIRM 4 of 4 and POSITIVE 3 of 3 (live); FB-f-6 3 of 3; FB-f-7 router 51 pass, guard 46 pass, F6 DIFF 193 of 193 twice, record 3 of 3, DORMANCY router 88 of 88 and guard 396 of 396. Parked cells' merged phases also re-run: FB-f-9 producers static 4 of 4 (14 of 14 writers reach the seam, 0 literal bucket names), rotation 3 of 3, read census 127 sites UNROUTED 0, dispatch export and gate all cases PASS; FB-f-9 AC1 deployed-equal reads 0 of 20 (phase B not shipped: production still runs the pre-round code, as parked); FB-f-13 AC1-AC3 PASS (census, 6 parity tests OK, targets exit 0). FWD-1 on this seat's own count over ANSWERS_A/B.json, READING_KEY.json and mapping_v3.json: PARTIAL. Canonical n=209: system 208, firm 209, tier 209, table 185, all four 184 (equal to the issuer's); both readers right on all four 182 of 207 truth-joined. The 25 disagreements: 19 a table-grain choice, 5 an unknown table, 1 an unknown system. Contents: 0 date conflicts (the one apparent conflict names a period's end beside the whole period) and 12 of 12 sampled pairs describe the same object. Legacy contrast: all four 1 of 209, firm 3 of 209. Agreement fell from round 2 (195 to 184). Independence NOT MET: readers 0.9.0_WK_ADVI_FIRMBKTS~13 and ~14 are subagents of the issuing session; project-free directories make the read blind, not two people who never worked together (D1-S3 stays OPEN).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "ADVI_FIRMBKTS PRD FWD-1 ACCEPT (two people who have never worked together ... agree); spine L9: graded by a seat that did none of the work.",
    "world_is": "ROUND 3 L9 (packet org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/R3_CLOSE.md @4199237975 (blob 84e3c1f153, 16,039 bytes; first read @5c50521a0c, blob bf91b649ae)): every recorded criterion of the 8 orders complete at the close re-run by this seat at the merged HEAD 7664786060 (main checkout, 11:11Z), all PASS: FB-f-1 LIVE 3 of 3 and MUTANT 2 of 2; FB-f-2 structure 5 of 5 and repair 5 of 5; FB-f-3 and FB-f-4 3 of 3 each (each reader directory holds exactly LOCATIONS.json and its answers file); FB-f-5 OWNFIRM 4 of 4 and POSITIVE 3 of 3 (live); FB-f-6 3 of 3; FB-f-7 router 51 pass, guard 46 pass, F6 DIFF 193 of 193 twice, record 3 of 3, DORMANCY router 88 of 88 and guard 396 of 396. Parked cells' merged phases also re-run: FB-f-9 producers static 4 of 4 (14 of 14 writers reach the seam, 0 literal bucket names), rotation 3 of 3, read census 127 sites UNROUTED 0, dispatch export and gate all cases PASS; FB-f-9 AC1 deployed-equal reads 0 of 20 (phase B not shipped: production still runs the pre-round code, as parked); FB-f-13 AC1-AC3 PASS (census, 6 parity tests OK, targets exit 0). FWD-1 on this seat's own count over ANSWERS_A/B.json, READING_KEY.json and mapping_v3.json: PARTIAL. Canonical n=209: system 208, firm 209, tier 209, table 185, all four 184 (equal to the issuer's); both readers right on all four 182 of 207 truth-joined. The 25 disagreements: 19 a table-grain choice, 5 an unknown table, 1 an unknown system. Contents: 0 date conflicts (the one apparent conflict names a period's end beside the whole period) and 12 of 12 sampled pairs describe the same object. Legacy contrast: all four 1 of 209, firm 3 of 209. Agreement fell from round 2 (195 to 184). Independence NOT MET: readers 0.9.0_WK_ADVI_FIRMBKTS~13 and ~14 are subagents of the issuing session; project-free directories make the read blind, not two people who never worked together (D1-S3 stays OPEN).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO re-ran every <invocation> of TO-FB-f-1..7 (and FB-f-13 AC1-AC3, FB-f-9 AC1) with the worktree roots replaced by the main checkout, HEAD 7664786060, 2026-10-11T11:11Z",
        "3.0.0_SA_CVO ran round3/checks/r3_producers.py --arms static, r3_rotation.py, r3_reads.py, r3_dispatch.py --arm export / --arm gate",
        "3.0.0_SA_CVO own script over C:/dev/wk-firmbkts-reader-{a,b}/ANSWERS_{A,B}.json, round3/READING_KEY.json and deliverables/mapping_v3.json (truth joined by bucket+class, 414 of 418)",
        "L8 packet org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/R3_CLOSE.md @5c50521a0c (blob bf91b649ae, equal to the working tree)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record. The unmet independence clause is carried by D1-S3 (REMEDIATION_v2, OPEN)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S15",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:45:00Z",
    "one_line": "D1-C-S7 re-read: the instrument limb is DONE. r3_f7_ctl.py --arms live (this seat, 11:11Z) prints DEST-VS-MANIFEST: EQUAL and, on its own line, SOURCE-VS-MANIFEST: DRIFTED changed=49110 gone=0, verdict COPY-COMPLETE exit 0, over the round-2 manifest (52,910 keys); --arms mutant reads DEST-VS-MANIFEST: DIFFERENT and COPY-NOT-COMPLETE on a planted mismatch. The copy is a snapshot: 49,110 of 52,910 sources changed since the manifest (D1-S4 stays OPEN). D1-C-S7's own close condition names the round-3 DELTA copy's compare, and that act (TO-FB-f-10) is parked, so the row stays OPEN in REMEDIATION_v3; it closes at act 3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-C-S7 re-read: the instrument limb is DONE. r3_f7_ctl.py --arms live (this seat, 11:11Z) prints DEST-VS-MANIFEST: EQUAL and, on its own line, SOURCE-VS-MANIFEST: DRIFTED changed=49110 gone=0, verdict COPY-COMPLETE exit 0, over the round-2 manifest (52,910 keys); --arms mutant reads DEST-VS-MANIFEST: DIFFERENT and COPY-NOT-COMPLETE on a planted mismatch. The copy is a snapshot: 49,110 of 52,910 sources changed since the manifest (D1-S4 stays OPEN). D1-C-S7's own close condition names the round-3 DELTA copy's compare, and that act (TO-FB-f-10) is parked, so the row stays OPEN in REMEDIATION_v3; it closes at act 3.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO r3_f7_ctl.py --arms live / --arms mutant --root C:/dev/ajb_workspace, 2026-10-11T11:11Z",
        "remediations/REMEDIATION_v3.md row ADVI_FIRMBKTS-D1-C-S7 (close condition: the round-3 delta copy's compare)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A re-read record; D1-C-S7 stays OPEN in REMEDIATION_v3 until act 3."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S16",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:45:00Z",
    "one_line": "ACT 1 (TO-FB-f-8, APPLIED on the laptop 08:21Z-08:23Z) read live by this seat at 11:14Z-11:20Z, read-only as cloudops-dell1-agent-user: shared-advisor-router:27 CodeSha256 cOG/BuFhy9xc.. and shared-advisor-router-response:6 YIgGtFjZ.., both Active, LastModified 08:22:18Z, equal to the change-management entry's L4 values; the downloaded zips hash to the same values and each is one bundled index.mjs with 0 bytes above 127. Distribution EVTSA9VEHNZVH ETag ELAAK8OWYOWV1, Deployed, LastModified 08:22:18Z (no change since the apply); associations 5 x router:27 and 5 x guard:6 among 40 (auth-validator-edge:22 x26, cache-control-injector:2 x2, public-data-router:7 x2). WAF ACL opal-cloudfront-protection: 6 rules, 3 in Count, LockToken 848a6d0b.. equal to the pre-act value. A no-session GET of /api/scoped/advisor-intelligence/summary.json returns 401 on d2n2nzpeqf34ge.cloudfront.net and on opalinvest.dev. Build input: the edge source is unchanged since the deploy commit 3a96b7d81f; this seat's rebuild with dell1's bun 1.4.2 matches the deployed bundles in length (7,509 and 3,538 bytes) but not byte for byte -- the difference is minifier output (identifier names; one destructuring form), so byte identity to the build input rests on the laptop's recorded artifact hash, not on this seat's rebuild. TO-FB-f-8's criteria still carry <ROUTER_VERSION>, <ROUTER_SHA256>, <GUARD_VERSION>, <GUARD_SHA256>, <WAF_ACL_NAME> and <WAF_ACL_ID> placeholders at complete; the values live in the change-management entry (row D1-C-S20).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "ACT 1 (TO-FB-f-8, APPLIED on the laptop 08:21Z-08:23Z) read live by this seat at 11:14Z-11:20Z, read-only as cloudops-dell1-agent-user: shared-advisor-router:27 CodeSha256 cOG/BuFhy9xc.. and shared-advisor-router-response:6 YIgGtFjZ.., both Active, LastModified 08:22:18Z, equal to the change-management entry's L4 values; the downloaded zips hash to the same values and each is one bundled index.mjs with 0 bytes above 127. Distribution EVTSA9VEHNZVH ETag ELAAK8OWYOWV1, Deployed, LastModified 08:22:18Z (no change since the apply); associations 5 x router:27 and 5 x guard:6 among 40 (auth-validator-edge:22 x26, cache-control-injector:2 x2, public-data-router:7 x2). WAF ACL opal-cloudfront-protection: 6 rules, 3 in Count, LockToken 848a6d0b.. equal to the pre-act value. A no-session GET of /api/scoped/advisor-intelligence/summary.json returns 401 on d2n2nzpeqf34ge.cloudfront.net and on opalinvest.dev. Build input: the edge source is unchanged since the deploy commit 3a96b7d81f; this seat's rebuild with dell1's bun 1.4.2 matches the deployed bundles in length (7,509 and 3,538 bytes) but not byte for byte -- the difference is minifier output (identifier names; one destructuring form), so byte identity to the build input rests on the laptop's recorded artifact hash, not on this seat's rebuild. TO-FB-f-8's criteria still carry <ROUTER_VERSION>, <ROUTER_SHA256>, <GUARD_VERSION>, <GUARD_SHA256>, <WAF_ACL_NAME> and <WAF_ACL_ID> placeholders at complete; the values live in the change-management entry (row D1-C-S20).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO .tools/aws lambda get-function-configuration / get-function (zip downloaded, hashed, scanned) for shared-advisor-router:27 and shared-advisor-router-response:6, 2026-10-11T11:14Z",
        "3.0.0_SA_CVO .tools/aws cloudfront get-distribution / get-distribution-config EVTSA9VEHNZVH; wafv2 get-web-acl opal-cloudfront-protection a09833c0-4043-49fc-a92c-0dcdeaff9abd",
        "3.0.0_SA_CVO curl https://d2n2nzpeqf34ge.cloudfront.net and https://opalinvest.dev /api/scoped/advisor-intelligence/summary.json -> 401, 401",
        "org/critical_paths/change_management/20261011T0814Z_advi-firmbkts-fb-f-8-advtenant-act1-laptop-20261011_deploy_completion.md (L1, L4, CLOSED)",
        "git diff 3a96b7d81f HEAD -- the edge source: empty; bun build with dell1 bun 1.4.2: lengths equal, minifier naming differs"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A WORLD read record: act 1's live state equals its record."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S17",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:45:00Z",
    "one_line": "L10 PRECONDITION MET -- THE SLUG IS SENT. At HEAD the round holds 13 orders: 9 complete, each with a VALID proof-of-spec instance (round-close-check --round 3: proof_ok 9 of 9, judgment 0, MAY-CLOSE), and 4 parked (FB-f-9 phase B, FB-f-10, FB-f-11, FB-f-13's acts), each carrying its owner and un-park conditions in its record face. A parked order sits outside the round by the CTO's ruling (org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND4_5_ANALYSIS_MDPF_SECCLASS_20260930.md:20-21: 'a parked order sits outside the round by ruling and re-enters on a status flip'; carried by surprise-row-gate.py TERMINAL_TO_WORDS and round-close-check.py OTHER_TERMINAL_WORDS), so it does not hold the slug. TO-FB-f-12, pending at this seat's first read (un-parked at edf6430bbc), is complete (62f7598435), its proof VALID on this seat's proof-of-spec-check, its change-management entry closed 4 of 4 (5cbdf9bf06). Every BLOCKING and ARMED row is dispositioned in this file. Residual, stated: the spine's L10 text (CANONICAL_FABRIC_WORKFLOW_20260901.md:524) asks every order of the round be terminal and 'finished with a valid proof-of-spec instance'; FB-f-10 and FB-f-11 carry no instance, and only the ruling admits the parked four. The round-4 issuance re-enters them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L10 PRECONDITION MET -- THE SLUG IS SENT. At HEAD the round holds 13 orders: 9 complete, each with a VALID proof-of-spec instance (round-close-check --round 3: proof_ok 9 of 9, judgment 0, MAY-CLOSE), and 4 parked (FB-f-9 phase B, FB-f-10, FB-f-11, FB-f-13's acts), each carrying its owner and un-park conditions in its record face. A parked order sits outside the round by the CTO's ruling (org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND4_5_ANALYSIS_MDPF_SECCLASS_20260930.md:20-21: 'a parked order sits outside the round by ruling and re-enters on a status flip'; carried by surprise-row-gate.py TERMINAL_TO_WORDS and round-close-check.py OTHER_TERMINAL_WORDS), so it does not hold the slug. TO-FB-f-12, pending at this seat's first read (un-parked at edf6430bbc), is complete (62f7598435), its proof VALID on this seat's proof-of-spec-check, its change-management entry closed 4 of 4 (5cbdf9bf06). Every BLOCKING and ARMED row is dispositioned in this file. Residual, stated: the spine's L10 text (CANONICAL_FABRIC_WORKFLOW_20260901.md:524) asks every order of the round be terminal and 'finished with a valid proof-of-spec instance'; FB-f-10 and FB-f-11 carry no instance, and only the ruling admits the parked four. The round-4 issuance re-enters them.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task-orders FB-f-9 :255, FB-f-10 :103, FB-f-11 :97, FB-f-13 :175 (PARKED, owner and un-park conditions); <status>parked</status> each",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND4_5_ANALYSIS_MDPF_SECCLASS_20260930.md:20-21",
        "org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:524 (the L10 precondition)",
        "commits 62f7598435 (FB-f-12 complete) and 5cbdf9bf06 (its ledger closed 4 of 4); proof-of-spec-check on its instance: VALID (rc=0)",
        "python .tools/round-close-check.py --project ADVI_FIRMBKTS --round 3 (this seat, after FB-f-12 complete): orders=13, 9 complete, proof_ok 9, MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The L10 precondition record: met; the slug is sent."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S25",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:45:00Z",
    "one_line": "TO-FB-f-12 (WORLD, applied on the laptop 11:2xZ after the gate fix 59f114b6d9) read by this seat, read-only as cloudops-dell1-agent-user, 11:29Z: role arn:aws:iam::313476888478:role/opal-sms-delivery-status-role created 2026-10-11T11:15:15Z, trust policy exactly one statement Allow sns.amazonaws.com sts:AssumeRole, one inline policy (opal-sms-delivery-status-policy), no attached policy; log groups sns/us-east-1/313476888478/DirectPublishToPhoneNumber and .../Failure, retentionInDays 14 on both, storedBytes 0 on both (no delivery record yet). NOT READ by this seat: the account's SMS attributes (AC2 DeliveryStatusIAMRole, AC3 DeliveryStatusSuccessSamplingRate): sns get-sms-attributes is refused to the dell1 identity (AuthorizationError, sms-voice:DescribeSpendLimits, 11:21Z and 11:29Z). For AC2 and AC3 the only evidence is the laptop lane's own read-back (deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/read_backs.txt), one source, not corroborated. The proof instance reads VALID (rc 0). The lane's first run hit a 403 iam:PassRole and the same plan passed three minutes later; the cause is unproven (the packet's addendum says so). The first reason line was read by the CTO at 11:30Z (row D1-S20: 'No origination identity available to send to destination number').",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "TO-FB-f-12 (WORLD, applied on the laptop 11:2xZ after the gate fix 59f114b6d9) read by this seat, read-only as cloudops-dell1-agent-user, 11:29Z: role arn:aws:iam::313476888478:role/opal-sms-delivery-status-role created 2026-10-11T11:15:15Z, trust policy exactly one statement Allow sns.amazonaws.com sts:AssumeRole, one inline policy (opal-sms-delivery-status-policy), no attached policy; log groups sns/us-east-1/313476888478/DirectPublishToPhoneNumber and .../Failure, retentionInDays 14 on both, storedBytes 0 on both (no delivery record yet). NOT READ by this seat: the account's SMS attributes (AC2 DeliveryStatusIAMRole, AC3 DeliveryStatusSuccessSamplingRate): sns get-sms-attributes is refused to the dell1 identity (AuthorizationError, sms-voice:DescribeSpendLimits, 11:21Z and 11:29Z). For AC2 and AC3 the only evidence is the laptop lane's own read-back (deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/read_backs.txt), one source, not corroborated. The proof instance reads VALID (rc 0). The lane's first run hit a 403 iam:PassRole and the same plan passed three minutes later; the cause is unproven (the packet's addendum says so). The first reason line was read by the CTO at 11:30Z (row D1-S20: 'No origination identity available to send to destination number').",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO .tools/aws iam get-role / list-role-policies / list-attached-role-policies opal-sms-delivery-status-role, 2026-10-11T11:29Z",
        "3.0.0_SA_CVO .tools/aws logs describe-log-groups --log-group-name-prefix sns/us-east-1/313476888478/DirectPublishToPhoneNumber: 14, 14",
        "3.0.0_SA_CVO .tools/aws sns get-sms-attributes: AuthorizationError at 11:21Z and 11:29Z (NOT READ)",
        "python .tools/proof-of-spec-check.py deliverables/0.7.0_AE_CloudOps~FBL/ADVI_FIRMBKTS.TO-FB-f-12.sms-delivery-status-logging.proof_of_spec.json: VALID (rc=0)",
        "packet ADDENDUM 1 @4199237975"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A WORLD read record of TO-FB-f-12; AC2 and AC3 stand on the lane's read-back alone."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S18",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:45:00Z",
    "one_line": "DISMISSED, act 1 and its build, and the SMS lane's ruled stops: D1-S11, D1-S12, D1-S13 (BLOCKING: act 1's non-ASCII, ACL-rider and explicit-deny stops) each ruled in an amendment of TO-FB-f-8 and closed by its Branch A; this seat's live read (D1-C-S16) finds the deployed bundles at 0 bytes above 127 (tier_policy.mjs keeps 10 non-ASCII comment characters, 29 bytes, which the minifier strips) and the ACL at 6 rules, 3 Count, LockToken unchanged. D1-W17-S1 and D1-W17-S5 (ARMED; S5 BLOCKING): the alias directory is one equivalence class by ruling and AC5 reads router 88 of 88 and guard 396 of 396 identical to base on this seat's run. D1-W17-S7: the deployed guard is all ASCII. S13 (BLOCKING): ruled a scoped apply (amendment 1); the secret orion/eclipse_jwt/current shows no version created at the 11:15Z apply (AWSCURRENT 09:51:35Z, AWSPREVIOUS 2026-10-10 21:01Z). S14 and S16 (BLOCKING): the two none_owed rows landed @5165905870. S15: the same standing hazard as D1-S19, carried there. S17 and S18 (BLOCKING): the plan limb's refusal of the two RULED log groups and an override that did not exist -- the gate fix landed at 59f114b6d9 (LGIC_ENFORCE-D1-S6) and the act applied through the gate's own plan limb with no override (TO-FB-f-12 complete, D1-C-S25).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-S11",
      "ADVI_FIRMBKTS-D1-S12",
      "ADVI_FIRMBKTS-D1-S13",
      "ADVI_FIRMBKTS-D1-W17-S1",
      "ADVI_FIRMBKTS-D1-W17-S5",
      "ADVI_FIRMBKTS-D1-W17-S7",
      "ADVI_FIRMBKTS-S13",
      "ADVI_FIRMBKTS-S14",
      "ADVI_FIRMBKTS-S15",
      "ADVI_FIRMBKTS-S16",
      "ADVI_FIRMBKTS-S17",
      "ADVI_FIRMBKTS-S18"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "DISMISSED, act 1 and its build, and the SMS lane's ruled stops: D1-S11, D1-S12, D1-S13 (BLOCKING: act 1's non-ASCII, ACL-rider and explicit-deny stops) each ruled in an amendment of TO-FB-f-8 and closed by its Branch A; this seat's live read (D1-C-S16) finds the deployed bundles at 0 bytes above 127 (tier_policy.mjs keeps 10 non-ASCII comment characters, 29 bytes, which the minifier strips) and the ACL at 6 rules, 3 Count, LockToken unchanged. D1-W17-S1 and D1-W17-S5 (ARMED; S5 BLOCKING): the alias directory is one equivalence class by ruling and AC5 reads router 88 of 88 and guard 396 of 396 identical to base on this seat's run. D1-W17-S7: the deployed guard is all ASCII. S13 (BLOCKING): ruled a scoped apply (amendment 1); the secret orion/eclipse_jwt/current shows no version created at the 11:15Z apply (AWSCURRENT 09:51:35Z, AWSPREVIOUS 2026-10-10 21:01Z). S14 and S16 (BLOCKING): the two none_owed rows landed @5165905870. S15: the same standing hazard as D1-S19, carried there. S17 and S18 (BLOCKING): the plan limb's refusal of the two RULED log groups and an override that did not exist -- the gate fix landed at 59f114b6d9 (LGIC_ENFORCE-D1-S6) and the act applied through the gate's own plan limb with no override (TO-FB-f-12 complete, D1-C-S25).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row ADVI_FIRMBKTS-D1-C-S16 (this seat's live read)",
        "3.0.0_SA_CVO byte scan of infra/aws/lambda-edge/shared-advisor-router/tier_policy.mjs at HEAD: 29 bytes above 127 on 10 comment lines",
        "3.0.0_SA_CVO dormancy_grid.mjs at HEAD: ROUTER 88 of 88, GUARD 396 of 396, differing 0",
        "3.0.0_SA_CVO .tools/aws secretsmanager list-secret-version-ids orion/eclipse_jwt/current",
        "task-orders TO-FB-f-8 amendments; TO-FB-f-12 amendments 1, 2, 5; commit 5165905870"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "DISMISSED, act 1 and its build, and the SMS lane's ruled stops: D1-S11, D1-S12, D1-S13 (BLOCKING: act 1's non-ASCII, ACL-rider and explicit-deny stops) each ruled in an amendment of TO-FB-f-8 and closed by its Branch A; this seat's live read (D1-C-S16) finds the deployed bundles at 0 bytes above 127 (tier_policy.mjs keeps 10 non-ASCII comment characters, 29 bytes, which the minifier strips) and the ACL at 6 rules, 3 Count, LockToken unchanged. D1-W17-S1 and D1-W17-S5 (ARMED; S5 BLOCKING): the alias directory is one equivalence class by ruling and AC5 reads router 88 of 88 and guard 396 of 396 identical to base on this seat's run. D1-W17-S7: the deployed guard is all ASCII. S13 (BLOCKING): ruled a scoped apply (amendment 1); the secret orion/eclipse_jwt/current shows no version created at the 11:15Z apply (AWSCURRENT 09:51:35Z, AWSPREVIOUS 2026-10-10 21:01Z). S14 and S16 (BLOCKING): the two none_owed rows landed @5165905870. S15: the same standing hazard as D1-S19, carried there. S17 and S18 (BLOCKING): the plan limb's refusal of the two RULED log groups and an override that did not exist -- the gate fix landed at 59f114b6d9 (LGIC_ENFORCE-D1-S6) and the act applied through the gate's own plan limb with no override (TO-FB-f-12 complete, D1-C-S25)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S19",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:45:00Z",
    "one_line": "DISMISSED, the round's build and process rows, each resolved at HEAD on this seat's run: W11-S1 and W15-S2 (BLOCKING: status flips outside the write grant) -- FB-f-1 and FB-f-5 read complete; W11-S2 -- the compare prints gone= apart from changed=; W15-S1 -- the face's class description, AC1 4 of 4; W12-S1 and W12-S4 (BLOCKING) -- the CTO's ADDENDUM 1 to the grain ruling, and repair arms T2 and T3 PASS; W16-S2 (ARMED) -- producers static D3 reads 0 literal bucket names in the 14 writers (D_00f's two 'opal-data-bd' mentions are docstring lines 37 and 51); W16-S7 and S8 -- rotation and sentinel 3 of 3; W16-S9 -- records the seam; W16-S10 (BLOCKING) -- the phase-A build merged, static 4 of 4; W16-S13 -- targets exit 0; W16-S14 -- census AC1 3 of 3; W16-S16 (BLOCKING) -- lib/platinum_dest_view.json is absent and untracked at HEAD; W20-S3 -- the invocation runs under env -u FORCE_COLOR and reads OK; W20-S5 -- resolved and merged; W21-S1, W23-S1..S5 (BLOCKING) and W23-S7 -- amendment 9, gold_dispatch.sh reads 0 bytes above 127; W22-S1 -- 6 parity tests OK; W22-S4 (BLOCKING, ARMED) -- the probe is routed by the _ServedS3 wrapper (census EXEMPT 1, UNROUTED 0); W22-S5 -- a WARN on an existing constant; W22-S6 -- records the ruling.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-W11-S1",
      "ADVI_FIRMBKTS-D1-W11-S2",
      "ADVI_FIRMBKTS-D1-W15-S1",
      "ADVI_FIRMBKTS-D1-W15-S2",
      "ADVI_FIRMBKTS-D1-W12-S1",
      "ADVI_FIRMBKTS-D1-W12-S4",
      "ADVI_FIRMBKTS-D1-W16-S2",
      "ADVI_FIRMBKTS-D1-W16-S7",
      "ADVI_FIRMBKTS-D1-W16-S8",
      "ADVI_FIRMBKTS-D1-W16-S9",
      "ADVI_FIRMBKTS-D1-W16-S10",
      "ADVI_FIRMBKTS-D1-W16-S13",
      "ADVI_FIRMBKTS-D1-W16-S14",
      "ADVI_FIRMBKTS-D1-W16-S16",
      "ADVI_FIRMBKTS-D1-W20-S3",
      "ADVI_FIRMBKTS-D1-W20-S5",
      "ADVI_FIRMBKTS-D1-W21-S1",
      "ADVI_FIRMBKTS-D1-W23-S1",
      "ADVI_FIRMBKTS-D1-W23-S2",
      "ADVI_FIRMBKTS-D1-W23-S3",
      "ADVI_FIRMBKTS-D1-W23-S4",
      "ADVI_FIRMBKTS-D1-W23-S5",
      "ADVI_FIRMBKTS-D1-W23-S7",
      "ADVI_FIRMBKTS-D1-W22-S1",
      "ADVI_FIRMBKTS-D1-W22-S4",
      "ADVI_FIRMBKTS-D1-W22-S5",
      "ADVI_FIRMBKTS-D1-W22-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "DISMISSED, the round's build and process rows, each resolved at HEAD on this seat's run: W11-S1 and W15-S2 (BLOCKING: status flips outside the write grant) -- FB-f-1 and FB-f-5 read complete; W11-S2 -- the compare prints gone= apart from changed=; W15-S1 -- the face's class description, AC1 4 of 4; W12-S1 and W12-S4 (BLOCKING) -- the CTO's ADDENDUM 1 to the grain ruling, and repair arms T2 and T3 PASS; W16-S2 (ARMED) -- producers static D3 reads 0 literal bucket names in the 14 writers (D_00f's two 'opal-data-bd' mentions are docstring lines 37 and 51); W16-S7 and S8 -- rotation and sentinel 3 of 3; W16-S9 -- records the seam; W16-S10 (BLOCKING) -- the phase-A build merged, static 4 of 4; W16-S13 -- targets exit 0; W16-S14 -- census AC1 3 of 3; W16-S16 (BLOCKING) -- lib/platinum_dest_view.json is absent and untracked at HEAD; W20-S3 -- the invocation runs under env -u FORCE_COLOR and reads OK; W20-S5 -- resolved and merged; W21-S1, W23-S1..S5 (BLOCKING) and W23-S7 -- amendment 9, gold_dispatch.sh reads 0 bytes above 127; W22-S1 -- 6 parity tests OK; W22-S4 (BLOCKING, ARMED) -- the probe is routed by the _ServedS3 wrapper (census EXEMPT 1, UNROUTED 0); W22-S5 -- a WARN on an existing constant; W22-S6 -- records the ruling.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row ADVI_FIRMBKTS-D1-C-S14 (this seat's re-runs at HEAD 7664786060)",
        "3.0.0_SA_CVO git ls-files data/black_diamond/scripts/gold/lib/platinum_dest_view.json -> 0; test -e -> no",
        "3.0.0_SA_CVO byte scan data/black_diamond/scripts/gold/gold_dispatch.sh -> 0 above 127",
        "3.0.0_SA_CVO grep -n opal-data-bd data/black_diamond/scripts/gold/D_00f.advisor_nna_canonical.py -> lines 37, 51 (docstring)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "DISMISSED, the round's build and process rows, each resolved at HEAD on this seat's run: W11-S1 and W15-S2 (BLOCKING: status flips outside the write grant) -- FB-f-1 and FB-f-5 read complete; W11-S2 -- the compare prints gone= apart from changed=; W15-S1 -- the face's class description, AC1 4 of 4; W12-S1 and W12-S4 (BLOCKING) -- the CTO's ADDENDUM 1 to the grain ruling, and repair arms T2 and T3 PASS; W16-S2 (ARMED) -- producers static D3 reads 0 literal bucket names in the 14 writers (D_00f's two 'opal-data-bd' mentions are docstring lines 37 and 51); W16-S7 and S8 -- rotation and sentinel 3 of 3; W16-S9 -- records the seam; W16-S10 (BLOCKING) -- the phase-A build merged, static 4 of 4; W16-S13 -- targets exit 0; W16-S14 -- census AC1 3 of 3; W16-S16 (BLOCKING) -- lib/platinum_dest_view.json is absent and untracked at HEAD; W20-S3 -- the invocation runs under env -u FORCE_COLOR and reads OK; W20-S5 -- resolved and merged; W21-S1, W23-S1..S5 (BLOCKING) and W23-S7 -- amendment 9, gold_dispatch.sh reads 0 bytes above 127; W22-S1 -- 6 parity tests OK; W22-S4 (BLOCKING, ARMED) -- the probe is routed by the _ServedS3 wrapper (census EXEMPT 1, UNROUTED 0); W22-S5 -- a WARN on an existing constant; W22-S6 -- records the ruling."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S20",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:45:00Z",
    "one_line": "DISMISSED: D1-W19-S1..S35, the 35 read-back and stale-cleanup sites that read BUCKET while their writer writes through the seam. Phase A3 routed the reads (merged); this seat's r3_reads.py over the 14 scripts reads 127 S3 data call sites, ROUTED 88, NOT-SERVED 36, EXEMPT 3, UNROUTED 0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-W19-S1",
      "ADVI_FIRMBKTS-D1-W19-S2",
      "ADVI_FIRMBKTS-D1-W19-S3",
      "ADVI_FIRMBKTS-D1-W19-S4",
      "ADVI_FIRMBKTS-D1-W19-S5",
      "ADVI_FIRMBKTS-D1-W19-S6",
      "ADVI_FIRMBKTS-D1-W19-S7",
      "ADVI_FIRMBKTS-D1-W19-S8",
      "ADVI_FIRMBKTS-D1-W19-S9",
      "ADVI_FIRMBKTS-D1-W19-S10",
      "ADVI_FIRMBKTS-D1-W19-S11",
      "ADVI_FIRMBKTS-D1-W19-S12",
      "ADVI_FIRMBKTS-D1-W19-S13",
      "ADVI_FIRMBKTS-D1-W19-S14",
      "ADVI_FIRMBKTS-D1-W19-S15",
      "ADVI_FIRMBKTS-D1-W19-S16",
      "ADVI_FIRMBKTS-D1-W19-S17",
      "ADVI_FIRMBKTS-D1-W19-S18",
      "ADVI_FIRMBKTS-D1-W19-S19",
      "ADVI_FIRMBKTS-D1-W19-S20",
      "ADVI_FIRMBKTS-D1-W19-S21",
      "ADVI_FIRMBKTS-D1-W19-S22",
      "ADVI_FIRMBKTS-D1-W19-S23",
      "ADVI_FIRMBKTS-D1-W19-S24",
      "ADVI_FIRMBKTS-D1-W19-S25",
      "ADVI_FIRMBKTS-D1-W19-S26",
      "ADVI_FIRMBKTS-D1-W19-S27",
      "ADVI_FIRMBKTS-D1-W19-S28",
      "ADVI_FIRMBKTS-D1-W19-S29",
      "ADVI_FIRMBKTS-D1-W19-S30",
      "ADVI_FIRMBKTS-D1-W19-S31",
      "ADVI_FIRMBKTS-D1-W19-S32",
      "ADVI_FIRMBKTS-D1-W19-S33",
      "ADVI_FIRMBKTS-D1-W19-S34",
      "ADVI_FIRMBKTS-D1-W19-S35"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "DISMISSED: D1-W19-S1..S35, the 35 read-back and stale-cleanup sites that read BUCKET while their writer writes through the seam. Phase A3 routed the reads (merged); this seat's r3_reads.py over the 14 scripts reads 127 S3 data call sites, ROUTED 88, NOT-SERVED 36, EXEMPT 3, UNROUTED 0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO python round3/checks/r3_reads.py at HEAD 7664786060: S3 data call sites=127 ROUTED=88 NOT-SERVED=36 EXEMPT=3 UNROUTED=0"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "DISMISSED: D1-W19-S1..S35, the 35 read-back and stale-cleanup sites that read BUCKET while their writer writes through the seam. Phase A3 routed the reads (merged); this seat's r3_reads.py over the 14 scripts reads 127 S3 data call sites, ROUTED 88, NOT-SERVED 36, EXEMPT 3, UNROUTED 0."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S21",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:45:00Z",
    "one_line": "NEW: TO-FB-f-8 reached complete with its four criteria still typed as placeholders (<ROUTER_VERSION>, <ROUTER_SHA256>, <GUARD_VERSION>, <GUARD_SHA256>, <WAF_ACL_NAME>, <WAF_ACL_ID>). The values exist only in the change-management entry and the proof, so the order text cannot be re-run as written; this seat re-ran it from the entry's values (D1-C-S16).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CLAUDE.md rule 27 L7: the worker face carries one clause per criterion with its invocation and expectation; .tools/to-pipeline-gate.py GATE (viii) grades <placeholders>.",
    "world_is": "NEW: TO-FB-f-8 reached complete with its four criteria still typed as placeholders (<ROUTER_VERSION>, <ROUTER_SHA256>, <GUARD_VERSION>, <GUARD_SHA256>, <WAF_ACL_NAME>, <WAF_ACL_ID>). The values exist only in the change-management entry and the proof, so the order text cannot be re-run as written; this seat re-ran it from the entry's values (D1-C-S16).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task-orders/ADVI_FIRMBKTS.TO-FB-f-8.act1-deploy-advtenant.md criteria AC1-AC4",
        "org/critical_paths/change_management/20261011T0814Z_advi-firmbkts-fb-f-8-advtenant-act1-laptop-20261011_deploy_completion.md L4"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S22",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:45:00Z",
    "one_line": "GRADUATED to 2.0.0_SA_COO~B1 (17): the face template (W16-S4, W17-S4: a status flip ordered outside the write grant; W16-S15: the pin rule against one commit); the census's missed writes (W16-S5, S6, S11, S12) and the awswrangler reads the read census cannot see (W22-S2), to be accounted before act 2; FB-f-7's spec and header text (W17-S2, S3, S6); act 2's canonical-mode behaviors (W20-S1, S2, S4); W21-S2 and W23-S6 (ARMED until now; INERT while BD_PLATINUM_MODE cannot be set -- FB-f-9 deployed-equal reads 0 of 20, so production runs the pre-round dispatcher); D1-S18 (BLOCKING: the producers' role holds no grant on the new prefix, carried to round 4 as its own act). Plus the new D1-C-S21.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-W16-S4",
      "ADVI_FIRMBKTS-D1-W17-S4",
      "ADVI_FIRMBKTS-D1-W16-S15",
      "ADVI_FIRMBKTS-D1-W16-S5",
      "ADVI_FIRMBKTS-D1-W16-S6",
      "ADVI_FIRMBKTS-D1-W16-S11",
      "ADVI_FIRMBKTS-D1-W16-S12",
      "ADVI_FIRMBKTS-D1-W17-S2",
      "ADVI_FIRMBKTS-D1-W17-S3",
      "ADVI_FIRMBKTS-D1-W17-S6",
      "ADVI_FIRMBKTS-D1-W20-S1",
      "ADVI_FIRMBKTS-D1-W20-S2",
      "ADVI_FIRMBKTS-D1-W20-S4",
      "ADVI_FIRMBKTS-D1-W21-S2",
      "ADVI_FIRMBKTS-D1-W23-S6",
      "ADVI_FIRMBKTS-D1-W22-S2",
      "ADVI_FIRMBKTS-D1-S18"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "GRADUATED to 2.0.0_SA_COO~B1 (17): the face template (W16-S4, W17-S4: a status flip ordered outside the write grant; W16-S15: the pin rule against one commit); the census's missed writes (W16-S5, S6, S11, S12) and the awswrangler reads the read census cannot see (W22-S2), to be accounted before act 2; FB-f-7's spec and header text (W17-S2, S3, S6); act 2's canonical-mode behaviors (W20-S1, S2, S4); W21-S2 and W23-S6 (ARMED until now; INERT while BD_PLATINUM_MODE cannot be set -- FB-f-9 deployed-equal reads 0 of 20, so production runs the pre-round dispatcher); D1-S18 (BLOCKING: the producers' role holds no grant on the new prefix, carried to round 4 as its own act). Plus the new D1-C-S21.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows as listed",
        "row ADVI_FIRMBKTS-D1-C-S14 (FB-f-9 AC1: DEPLOY EQUAL 0 of 20)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S23",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:45:00Z",
    "one_line": "GRADUATED to 1.0.0_SA_CTO~DELL1 (15): the grain ruling's edges behind the FAULT 84 (W12-S2, S3, S5..S11); the instruments that are not this project's (W16-S1, W16-S3: comp-pipescript io; W22-S3: opal_naming targets' Lambda classification); D1-S14 (ADDENDUM 4 condition 1 on E_01 and E_24); S12 (portal-auth's plan keeps a WAF ACL diff that ADDENDUM 3 waived for act 1 only); D1-S17 (ARMED, the CTO's own tripwire: the stale ownership map at the new home, disarmed at act 4). GRADUATED to 0.0.0_AB_MSTR~DELL1, their disarm owner: D1-S15, D1-S16 and D1-S20 (the SEV1 SMS path delivered 0 of 28 in 14 days; the reason, read by the CTO at 11:30Z, is 'No origination identity available to send to destination number'). GRADUATED to 0.7.0_AE_CloudOps, stays ARMED: D1-S19 (the inf-pipeline root's pending secret version; any unscoped apply mints a new current version).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-W12-S2",
      "ADVI_FIRMBKTS-D1-W12-S3",
      "ADVI_FIRMBKTS-D1-W12-S5",
      "ADVI_FIRMBKTS-D1-W12-S6",
      "ADVI_FIRMBKTS-D1-W12-S7",
      "ADVI_FIRMBKTS-D1-W12-S8",
      "ADVI_FIRMBKTS-D1-W12-S9",
      "ADVI_FIRMBKTS-D1-W12-S10",
      "ADVI_FIRMBKTS-D1-W12-S11",
      "ADVI_FIRMBKTS-D1-W16-S1",
      "ADVI_FIRMBKTS-D1-W16-S3",
      "ADVI_FIRMBKTS-D1-W22-S3",
      "ADVI_FIRMBKTS-D1-S14",
      "ADVI_FIRMBKTS-S12",
      "ADVI_FIRMBKTS-D1-S17",
      "ADVI_FIRMBKTS-D1-S15",
      "ADVI_FIRMBKTS-D1-S16",
      "ADVI_FIRMBKTS-D1-S20",
      "ADVI_FIRMBKTS-D1-S19"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "GRADUATED to 1.0.0_SA_CTO~DELL1 (15): the grain ruling's edges behind the FAULT 84 (W12-S2, S3, S5..S11); the instruments that are not this project's (W16-S1, W16-S3: comp-pipescript io; W22-S3: opal_naming targets' Lambda classification); D1-S14 (ADDENDUM 4 condition 1 on E_01 and E_24); S12 (portal-auth's plan keeps a WAF ACL diff that ADDENDUM 3 waived for act 1 only); D1-S17 (ARMED, the CTO's own tripwire: the stale ownership map at the new home, disarmed at act 4). GRADUATED to 0.0.0_AB_MSTR~DELL1, their disarm owner: D1-S15, D1-S16 and D1-S20 (the SEV1 SMS path delivered 0 of 28 in 14 days; the reason, read by the CTO at 11:30Z, is 'No origination identity available to send to destination number'). GRADUATED to 0.7.0_AE_CloudOps, stays ARMED: D1-S19 (the inf-pipeline root's pending secret version; any unscoped apply mints a new current version).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows as listed",
        "deliverables/mapping_v3.json: FAULT 84, owner 1.0.0_SA_CTO~DELL1 on all 84"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S24",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T11:45:00Z",
    "one_line": "REMEDIATION_v3 re-read against its close conditions. REMEDIATED by the in-place clock: D1-S9 (ROUND_ANALYSIS.round2.md:32-35 names the list entry AND the map value in step 4); D1-W4-S2..S6 (the grain ruling, ROUND_ANALYSIS.round2.md:46-51 and ADDENDUM 1, applied by TO-FB-f-2: repair T1-T5 PASS on this seat's run); D1-W7-S1 (the own-firm admit read EXERCISED: FB-f-5 O3, a GetObject of the own-grant key SUCCEEDED); D1-W9-S1 (the deployed router reads 0 bytes above 127). STAY OPEN: D1-S4 and D1-S7 (acts 3 and 4), D1-S10 (the CTO routed it to the gate owner; round-close-check has not adopted the gate's resolver), D1-W9-S2, D1-W9-S5 and D1-W4-S7 (12 of 13 round-3 orders state an absolute root or none is needed; TO-FB-f-9 AC1 runs a repo-relative path with no root), D1-C-S7 (C-S15). REMEDIATION_v2: D1-S1 (prd_version v1.3, the addendum not landed), D1-S2 and D1-S3 stay OPEN.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-S9",
      "ADVI_FIRMBKTS-D1-W4-S2",
      "ADVI_FIRMBKTS-D1-W4-S3",
      "ADVI_FIRMBKTS-D1-W4-S4",
      "ADVI_FIRMBKTS-D1-W4-S5",
      "ADVI_FIRMBKTS-D1-W4-S6",
      "ADVI_FIRMBKTS-D1-W7-S1",
      "ADVI_FIRMBKTS-D1-W9-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "REMEDIATION_v3 re-read against its close conditions. REMEDIATED by the in-place clock: D1-S9 (ROUND_ANALYSIS.round2.md:32-35 names the list entry AND the map value in step 4); D1-W4-S2..S6 (the grain ruling, ROUND_ANALYSIS.round2.md:46-51 and ADDENDUM 1, applied by TO-FB-f-2: repair T1-T5 PASS on this seat's run); D1-W7-S1 (the own-firm admit read EXERCISED: FB-f-5 O3, a GetObject of the own-grant key SUCCEEDED); D1-W9-S1 (the deployed router reads 0 bytes above 127). STAY OPEN: D1-S4 and D1-S7 (acts 3 and 4), D1-S10 (the CTO routed it to the gate owner; round-close-check has not adopted the gate's resolver), D1-W9-S2, D1-W9-S5 and D1-W4-S7 (12 of 13 round-3 orders state an absolute root or none is needed; TO-FB-f-9 AC1 runs a repo-relative path with no root), D1-C-S7 (C-S15). REMEDIATION_v2: D1-S1 (prd_version v1.3, the addendum not landed), D1-S2 and D1-S3 stay OPEN.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round2.md:32-35, :46-51, :94",
        "3.0.0_SA_CVO r3_mapping.py --arms repair: T1-T5 PASS; r3_f4.py --arms ownfirm: O3 PASS; edge zip scan: 0 bytes above 127",
        "task-orders/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.md:87 (AC1 invocation, no root)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Close conditions met as stated; the eight rows advance in REMEDIATION_v3 by remediation.state OPEN to REMEDIATED and closed false to true only."
  }
]
```
