# TO IRPT_BCKEND.TO-IB-pr-490 -- the live read: the deployed adapter's claim and counts on one Inflection account, against the offline prediction (closes row D2-S114)

<to_id>IRPT_BCKEND.TO-IB-pr-490</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>169</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ROUND-169 ANALYSIS section 3 item 2 (msg 6660); the release it reads: `IRPT_BCKEND.TO-IB-pr-487` (live `irpt-performance-adapter` `abep4h7RngMS9JomQUdkcOT3EZ+W953OdxeK0HkdzFo=` since 2026-10-12T22:35:06Z) | **Decomp cell:** `IB-pr-490` (decomposition section 161) | **outcome_ref:** FWD-3

---

## WORKER FACE

**HOLD (issuer, 2026-10-13T00:4xZ, on the CTO's msgs 6701 and 6703):** the cause is known and is not ours: ADVI_FIRMBKTS act 4 (dell1, ledger `org/critical_paths/change_management/20261012T1340Z_advi-firmbkts-fb-f-11-act4-irpt-leg-20261012_deploy_completion.md`) moved the adapter's Inflection reads onto `opal-data-inflection`'s bucket-policy fence at 14:03Z to 14:13Z on 10-12; our `IB-pr-482` release sits on top of it and is not the cause. **HOLD the Inflection live read** (the invokes and the three criteria) **until dell1's fix is live**; do NOT retry the invokes, do NOT change a role, a bucket policy or an exemption list, do NOT roll anything back. The read-only CloudTrail read below is now OPTIONAL: stop it where it stands, report what you already have in one line, and read no further unless the issuer asks.

**AMENDMENT 1 (issuer, 2026-10-13T00:3xZ, on the CTO's ruling msg 6698 and your row S116, which was right): DO THIS NEXT, READ-ONLY, BEFORE ANY RETRY OF THE INVOKES AND BEFORE ANY FIX.** Find what changed around the retained-index `AccessDenied`. Window: **2026-10-11T09:45Z to now** (the last computed Inflection answer was 10-11 09:45Z). With `aws cloudtrail lookup-events` (management events; auto-paginate and print the denominator of events scanned per lookup) read, with WHO (the principal's type and its role or user NAME, never an account id or ARN prefix) and WHEN (event time) for each hit: (1) iam `PutRolePolicy`, `DeleteRolePolicy`, `AttachRolePolicy`, `DetachRolePolicy`, `UpdateAssumeRolePolicy` on the role `irpt-performance-adapter-role`; (2) kms `PutKeyPolicy`, `CreateGrant`, `RevokeGrant`, `RetireGrant`, `DisableKey` on the key that encrypts `irpt-requests` (the key id appears in the role's own policy statement `RequestEncryptionViaDynamoOnly`); (3) dynamodb `UpdateTable` and `PutResourcePolicy` on `irpt-requests`; (4) the DENIED call's own CloudTrail error line: events whose errorCode is `AccessDenied` or `AccessDeniedException` for the function's role session from 2026-10-13T00:04Z onward (kms `Decrypt` is a management event and may show it; a DynamoDB `GetItem` is a data event: say whether any trail in the account records data events for `irpt-requests` (`describe-trails`, `get-event-selectors`), and if one does read ONLY its log object for the 00:26Z window, read-only). **ADDED by the CTO's finding (msg 6701; issuer commit of 2026-10-13T00:4xZ):** the denied call is NOT DynamoDB. The function's own log since 00:00Z reads `not authorized to perform: s3:ListBucket on resource opal-data-inflection with an explicit deny in a resource-based policy`; the bucket policy's `DenyForeignFirmPrincipals` admits only `role/*-inf-*` plus a named list, and `irpt-performance-adapter-role` is not in it. So ADD to the read: (5) s3 `PutBucketPolicy` and `DeleteBucketPolicy` on `opal-data-inflection` (who, when); (6) who changed the function `irpt-performance-adapter` at **2026-10-12T14:11Z** (its LastModified): the lambda events (`UpdateFunctionCode*`, `UpdateFunctionConfiguration*`, `PublishVersion`) in 14:00Z to 14:20Z with the principal's kind and NAME; and (7) read, with `aws s3api get-bucket-policy --bucket opal-data-inflection`, whether the policy text today names `irpt-performance-adapter-role` in its deny exemptions, and record only YES or NO (never the policy text). No fix, no exemption-list edit, no bucket-policy edit.

Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB169-3_accessdenied_cloudtrail_read.json` with, per lookup, `{lookup, events_scanned, hits:[{event_name, event_time_utc, principal_kind, principal_name}], error_lines:[{event_name, event_time_utc, error_code}], data_events_for_table: true|false|unknown}`: counts, names and times only. Report to `2.0.0_SA_COO~P2` in one message under 150 words: the hits that fall in the window (who, when, which statement), or none, and whether the denied call's error line was found. **READ ONLY: no IAM, key, table, grant or function change, no retry of the invokes, no fix; report before any fix.** This amendment adds no criterion; the order's three criteria stay as they are and stay open until the live read can run.

**START ONLY ON THE ISSUER'S MESSAGE** naming this order and saying `IB-pr-489` is drained (the reference file exists). Until then do nothing on this order. This is a chain dependency, not a wait on the world: the walk is an act the issuer's worker takes now.

**Cell `IB-pr-490` (inlined):** the changed path of the `IB-pr-487` release (the claim follows the excluded day's status; two counts appear beside `days_linked`) has run on no live answer: your nine kept references refused before any compute. `IB-pr-489` keeps the Inflection selection references its walk produced, ONE OR TWO lines `sel_` + 64 hex (the performance paths of one client's tab carried two distinct references; only a single-account selection computes, a relationship or multi-account selection answers a refusal that persists nothing), in `C:\Users\Test\AppData\Local\Temp\claude\C--dev-ajb-workspace\f0005e69-69e0-455c-b522-7be87d97fcdc\scratchpad\inflection_sel_ref.txt` (outside any git tree). Read that answer once per window and compare it with the offline prediction.

**Steps:**
1. Read the reference file (one or two lines). Do not copy any line into a record, message or commit.
2. **Invoke the deployed function directly** as in your `IB-pr-487` session (the Opal internal principal, the function's own role, the same API-shaped event, `selected_tenant` = `inflection`), with the first reference and the window **2026-01-01 to 2026-10-09** (YTD to the latest served day). If that answer is `ok:false`, record its code (counts only) and try the SECOND reference the same way; if both are `ok:false`, STOP: do not probe other firms. On the first `ok` answer you may make ONE more invoke, for the window **2025-10-09 to 2026-10-09** (1Y), on the same reference. **At most 4 invokes in all; each ok answer persists a retained revision (a new record; nothing is overwritten): at most 2 persisted.**
3. From each answer take the claim on the headline figure, `days_without_base` and `days_with_return_left_out`, and the sha256 of the figure (not the figure).
4. **The prediction, offline, at the build's pin:** the answer names the account it was computed for (the answer's own scope; read it from the answer, keep it in YOUR scratch outside the repo, delete the scratch at the end). With the round-166 driver `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~331/ib166_measure.py` (read it first for its inputs and its use of the served gold) compute the claim the reader's rule gives that account over that window at the built pin `05219b844491b6c3c9309b6b3747e54edb823299`. A `measured` or `inferred` prediction is both valid.
5. Read the function's log group `/aws/lambda/irpt-performance-adapter` from 22:35:06Z: the `irpt_retained_phases` line of your invoke names a computed path (not `refused:*`), and 0 `TypeError` lines.
6. Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB169-3_inflection_live_read.json`: `{ref_count: <1 or 2>, invokes: <1 to 4>, path_class: "computed", persisted_retained_revisions: <int 0..2>, windows: [{window: "YTD"|"1Y", claim_observed, claim_predicted, days_without_base: <int>, days_with_return_left_out: <int>, figure_sha256}], not_established: [...]}`. No account id, client name, reference or figure in it: counts, sha256 and class words only.

**Criteria (run each under `timeout 120`, record the output and exit code verbatim):**

<criterion id="IB169-3-AC1" cell_refs="IB-pr-490"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-3-AC1</invocation><expect>IB169-3-AC1 PASS</expect></criterion>
<criterion id="IB169-3-AC2" cell_refs="IB-pr-490"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-3-AC2</invocation><expect>IB169-3-AC2 PASS</expect></criterion>
<criterion id="IB169-3-AC3" cell_refs="IB-pr-490"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-3-AC3</invocation><expect>IB169-3-AC3 PASS</expect></criterion>

<expected_criteria>IB169-3-AC1, IB169-3-AC2, IB169-3-AC3</expected_criteria>

What the checks grade: AC1 the record: 1 to 4 invokes on one or two references, every window's observed claim equals its predicted claim, both counts present as integers, a figure sha256, `path_class` computed; AC2 a live AWS read of the function's log since the apply: at least one `irpt_retained_phases` line that is not `refused:*`, and 0 `TypeError`; AC3 `persisted_retained_revisions` an integer 0 to 2, no long digit run, no reference, no client key.

**If the observed claim differs from the prediction, or a count is absent:** that is Branch B's trigger for the `IB-pr-487` release (signed in both halves): do NOT redeploy; file a BLOCKING row with both values and STOP, and the issuer rules. Never weaken a check.

## BOUNDS

- **Grant:** the `paths` block and nothing else. Four direct invokes at most, at most two of them persisting a retained revision (the ok answers) in the function's own store by the function's own role. No deploy, no Terraform, no source-map edit, no selection write, no read of `irpt-requests`, no other function, no vendor call.
- **Refusal clause:** STOP and file a row on any of: the reference file missing or not one line; an `ok:false` first answer; a 5xx or `TypeError`; a claim differing from its prediction; a count absent.
- **Row ids** are `IRPT_BCKEND-D2-S<n>` (the next free number: check the id is free just before you commit); `surfaced_at` is `date -u +%FT%TZ` at filing.
- **Commit with** your own author line via `bash .tools/safe-commit.sh -F <msgfile>` (message file via the Write tool, outside the worktree; do NOT pre-`git add`); ASCII only. Report to `2.0.0_SA_COO~P2` in one message under 150 words: each criterion's last line, the invoke count, the persisted count, observed against predicted claim in words.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-490.inflection-live-read-claim-and-counts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 161 (round 169, workstream ~P), cell `IB-pr-490`.
<owned_cells>IB-pr-490</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB169-3-AC1, IB169-3-AC2, IB169-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-490.inflection-live-read-claim-and-counts.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- the order changes no resource: two direct invokes of a function that is already live, each persisting a retained report (a new record) in the function's own store; the persists are named in the face and bounded at 2. The CTO half's AMENDMENT 2 (Amendment 1's 18-revision ceiling) is the standing sign-off for retained-revision writes by this function.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the invokes use the path IB-pr-487 used (the function's own role, CTO ADDENDUM 3 path 1), no new grant.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p169_cells.py dry-run at base on dell2 2026-10-12 ~23:2xZ: IB169-3 AC1 FAIL (no record), AC2 FAIL (a live AWS read: 9 `irpt_retained_phases` lines since 22:35:06Z, all `refused:*`, so no computed line), AC3 FAIL (no record). The cut has no positive control for AC1 and AC3 beyond the shape rules; AC2 is graded on the live log.
lane: the <paths> block IS the grant; applied by 0.7.0_AE_CloudOps~IB2, IRPT_BCKEND only, on the issuer's go-message after IB-pr-489 drains. Class SERVED.
</preflight>
