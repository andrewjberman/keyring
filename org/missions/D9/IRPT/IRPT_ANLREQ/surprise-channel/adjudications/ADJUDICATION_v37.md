# IRPT_ANLREQ: CVO L8 compile of the 133 undispositioned items -- 114 DISMISSED (resolved), 19 live (graduate at the slug)

<sweep_watermark>2026-10-21T18:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-21.

**Basis.** L8 channel compile by `3.0.0_SA_CVO~DELL2`, 2026-10-21T18:10Z, over the 133 items `.tools/surprise-row-gate.py` named as
undispositioned (ADJUDICATION_v36). Each row was traced by one of six read-only evidence reads that this seat directed. Each read
returned one pointer per row: an amendment line, a drain or flip commit, a later disarm row, a live release or a delete pass.

**This seat spot-read seven pointers.** Each matched its claim:
- TO-AR-y-332:64 holds AMENDMENT 3.
- ticket_center `lambda_function.py:436-439` returns 403 on a missing firm list.
- R22_DELETE_RESULT.json:18 and :26 name the run-4 and run-5 keys.
- TO-AR-y-217:37 holds the BUILD_ONLY guard check.
- The live rows read as claimed:
  - `TicketCenter.tsx:211` is `isInternal() || isDev()`;
  - the draft-store map pins `283f7e7700`;
  - `commentary/lambda_handler.py:392-402` sends after persist inside the per-item try.

**Two judgment notes:**
- W315-S1 and W315-S2 have no explicit ruling. The issuer built, signed and applied r34m from the edited guard. That is acceptance by the
  owner, and this seat dismisses on it.
- S140 is dismissed because the CTO parked D2 and D4. The cause of the step-2 refusal was never named, and that is recorded here as a
  limit.

## The 19 live items (graduate ARMED with their owners at the slug)

| row | owner | what still stands |
|---|---|---|
| D2-W90-S3 | 2.0.0_SA_COO~Y2 | releaseDom() still called in portal prospect-suggested-swaps.test.tsx |
| D2-W103-S4 | 2.0.0_SA_COO~Y2 | Predicate unchanged at portal HEAD; AUDIT_a.json:191 STANDS; a partner user with the Dev claim gets the internal view |
| D2-W107-S3 | 2.0.0_SA_COO~Y2 | KEPT shares pricing deferred to a later cell never cut; a KEPT shares row still refuses SHARES_PRICE_UNAVAILABLE |
| D2-W136-S1 | 2.0.0_SA_COO~T2 | A send that raises after persist is reported only as a hop failure with no batchItemFailures; redelivery stops at draft_exists; the I4 handoff is lost |
| D2-W143-S2 | 1.0.0_SA_CTO~DELL2 | Hashed account-id list still absent on dell2 as of 10-21; 546a502ca46 says the gate rows stay armed until the HMAC list lands |
| D2-W181-S1 | 2.0.0_SA_COO~G2 | S123 cleared this one commit by issuer read, but the gate is still blind on dell2 until the hashed list is provisioned |
| D2-W184-S1 | 2.0.0_SA_COO~G2 | S124 cleared this one commit by issuer read; the dell2 hashed list is still absent as of 10-21 |
| D2-W187-S1 | 2.0.0_SA_COO~G2 | S125 cleared this one commit by issuer read; the device-level gap is unchanged until the list lands |
| D2-W188-S1 | 2.0.0_SA_COO~G2 | S126 cleared this one commit by issuer read; the device-level gap is unchanged until the list lands |
| D2-W200-S1 | 0.0.0_AB_MSTR~DELL2 | S132 hand-checked one commit; the hashed list is still absent on dell2 (W299-S1, W385-S1 repeat the gap) |
| D2-W291-S2 | 2.0.0_SA_COO~Y2 | Draft-store map still pins the old acceptance.py; deferred to enrichment candidate 8, not fixed |
| D2-S211 | 2.0.0_SA_COO~Y2 | Application has no deleter and no lifecycle rule; leftovers removed only by one-off delete passes |
| D2-S214 | 2.0.0_SA_COO~Y2 | No delete manifest names this runs-2/3 key; the object probably stands (not checked live) |
| D2-W331-S1 | 0.0.0_AB_MSTR~DELL2 | The hashed list is still missing on dell2; every commit here goes unchecked |
| D2-W363-S1 | 2.0.0_SA_COO~Y2 | Hashed account-id list still absent; commits on this box stay unchecked |
| D2-S254 | 2.0.0_SA_COO~Y2 | Run 7K synthetic S3 residue; no delete pass past runs 7e-7j |
| D2-S255 | 2.0.0_SA_COO~Y2 | Run 7L synthetic S3 residue; newest manifest covers 7e-7j only |
| D2-S257 | 2.0.0_SA_COO~Y2 | Run 7M synthetic S3 residue; no delete pass covers 7k-7n |
| D2-S258 | 2.0.0_SA_COO~Y2 | Run 7N residue surfaced after the last delete pass (7e-7j, 193a8fe72e3) |

- **Client-data check, 8 rows:** W143-S2, W181-S1, W184-S1, W187-S1, W188-S1, W200-S1, W331-S1 and W363-S1 are one hazard. dell2 has no
  hashed account-id list, so `safe-commit.sh` cannot check client data on this box. The device owner is `0.0.0_AB_MSTR~DELL2`.
- **Synthetic S3 residue, 6 rows:** S211, S214, S254, S255, S257 and S258 are the residue and the missing application deleter. Any S3
  delete needs a human's word.
- **Product or build defects, 5 rows:**
  - W90-S3: a portal test releases the DOM.
  - W103-S4: the Ticket Center's Dev-claim predicate.
  - W107-S3: KEPT shares pricing was never cut.
  - W136-S1: a commentary send after persist is lost on a raise.
  - W291-S2: the draft-store map pins the old acceptance.py.

## All 133 items

| row | class/hazard | verdict | evidence | reason |
|---|---|---|---|---|
| D2-W62-S6 | OBSERVATION/ARMED | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-217.irpt-status-with-status-py.md:37 (also TO-AR-y-228:32; row D2-S69) | Later orders require a BUILD_ONLY guard check at the base before any build |
| D2-W62-S9 | BLOCKING/INERT | RESOLVED | 9405a1f2852 flip(TO-AR-y-212 and TO-AR-y-213, suites repaired by AR-y-216) | AR-y-216 moved the suites to the status rule; AC1 re-graded; order complete |
| D2-W76-S2 | BLOCKING/INERT | RESOLVED | ae22b5c99db status(TO-AR-y-244, row W76-S2 fixed) | Issuer fixed the checker path; record passes y244-read; order complete |
| D2-W74-S1 | BLOCKING/INERT | RESOLVED | 27204d9ebdc status(TO-AR-y-242, trunk checker passes) | Trunk checker passes on the amended record; order complete with an issuer note |
| D2-W78-S3 | BLOCKING/INERT | RESOLVED | 7ff2ede6ac5 record(TO-AR-y-242 amendment 1, row W78-S3) | Issuer committed the amended record and pinned the proof (95cd92861d2); order complete |
| D2-W80-S1 | BLOCKING/INERT | RESOLVED | c53686ba6dc (re-cut with grants); 5d3ed81c12a revert(AR-y-277) | Re-cut as AR-y-251; the swap feature was later withdrawn by the CTO (msg 7176) and reverted |
| D2-W79-S1 | BLOCKING/INERT | RESOLVED | 6cae7c8cc97 drain(TO-AR-y-250); 81333acb8dc | Harness re-cut with a grant and built; the whole line later withdrawn and reverted |
| D2-W79-S2 | BLOCKING/INERT | RESOLVED | 81333acb8dc stop(AR-y-266, CTO withdrew rulings B, (a), (a') msg 7176) | Premise went to the CTO; swap design withdrawn under PRD C-SWAP |
| D2-W84-S1 | BLOCKING/INERT | RESOLVED | 5d3ed81c12a revert(AR-y-277) | The second advisory construction was reverted; the split is gone |
| D2-S83 | BLOCKING/INERT | RESOLVED | dbe928a6261 drain(TO-AR-y-265) | Portal fix 923f7d69 is an ancestor of portal HEAD; analysis-submit-silence test present |
| D2-W90-S3 | OBSERVATION/ARMED | LIVE | deliverables/0.9.0_WK_IRPT_ANLREQ~287/r47/AUDIT_a.json:130 (verdict STANDS) | releaseDom() still called in portal prospect-suggested-swaps.test.tsx |
| D2-W93-S1 | BLOCKING/INERT | RESOLVED | 84352a18894 status(TO-AR-y-280 and TO-AR-y-272 flipped complete with issuer notes) | Issuer accepted the void premise and closed AR-y-272 with a note |
| D2-W92-S1 | BLOCKING/INERT | RESOLVED | ecdc6cac82e drain(TO-AR-y-271) | Read-only cell; the J2 finding led to ruling (A) and later builds |
| D2-W97-S2 | BLOCKING/INERT | RESOLVED | 96b1a95596f drain(TO-AR-y-280) | After CTO ruling (A), SUBMIT-FORM accepts answers and an attachment |
| D2-W101-S1 | BLOCKING/INERT | RESOLVED | 4f6d6acb879 status(TO-AR-y-285 Y285-PKG-SENDER-OK) | AR-y-284 and AR-y-285 added request_id/request_revision to PACKAGE; both complete |
| D2-W101-S3 | OBSERVATION/ARMED | RESOLVED | d592d28527e record(TO-APPLY-R30a release 29b closed); INVESTIGATION_v1.md:13669 (S101) | Owner check on input_id live; KMS gap fixed by 8220c590a0f and disarmed by S101 |
| D2-W103-S1 | BLOCKING/INERT | RESOLVED | a79aa40ffdf (CTO: Ticket Center DEV class settled by the build mode) | CTO ruled the DEV discriminator is the build mode; App.tsx gates on isPartnerDevReach |
| D2-W103-S4 | OBSERVATION/ARMED | LIVE | portal/src/pages/TicketCenter/TicketCenter.tsx:211 (const internal = auth.isInternal() or auth.isDev()) | Predicate unchanged at portal HEAD; AUDIT_a.json:191 STANDS; a partner user with the Dev claim gets the internal view |
| D2-W107-S1 | BLOCKING/INERT | RESOLVED | 4abb3fe9e01 amend(TO-AR-y-293 AMENDMENT 1, rows W107-S1, S3) | Grant widened to ops/status.py; AR-y-293 complete with Y293-KEPT-OK |
| D2-W107-S3 | BLOCKING/INERT | LIVE | infra/aws/lambda/investor-reporting/intake/tests/test_unresolved_keep.py:100; decompositions/IRPT_ANLREQ_DECOMP_R28A_Y.md:13 | KEPT shares pricing deferred to a later cell never cut; a KEPT shares row still refuses SHARES_PRICE_UNAVAILABLE |
| D2-W109-S1 | BLOCKING/INERT | RESOLVED | c7a0d3a3dae test(AR-y-285 AMENDMENT 2) | AMENDMENT 2 granted the two pinned test edits; AC1 passes; order complete |
| D2-W112-S4 | BLOCKING/INERT | RESOLVED | 67af307441c amend(TO-AR-y-281 AMENDMENT 4, row W112-S4) | AC1 re-pointed; order complete with Y281-LIST-OK |
| D2-W111-S4 | BLOCKING/INERT | RESOLVED | bd4f8ddea5b amend(TO-AR-y-294 checker) | Checker grades only the last row; AC1 PASS; order complete |
| D2-W118-S2 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-300.release-build-resident.md:61 (AMENDMENT 1), :98 | Issuer agreed the packager is a REPLACE, fixed the expected delta; order complete with Y300-BUILD-OK |
| D2-S93 | BLOCKING/INERT | RESOLVED | task-orders/TO-AR-y-306.ordinary-viewer-authorizer.md:35; 5c4b50864d1 (TO-EXERCISE-R29, partner advisor NORMALIZED live) | ordinary_authorizer built under AR-y-306, shipped in release 29; partner upload admitted live |
| D2-S94 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-308.shares-not-composed-words.md:35 (CTO msg 7546) | CTO ruled the Shares refusal stays (enrichment); missing correction words added and shipped in release 29 |
| D2-W120-S1 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-306.ordinary-viewer-authorizer.md:54 (AMENDMENT 1) | Test file added to the grant; two absent-producer pins moved to the composed state |
| D2-W120-S2 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-306.ordinary-viewer-authorizer.md:56 (AMENDMENT 2, CTO msg 7529) | CTO accepted one authorizer for the upload door and owned-input route; owner-only tests added |
| D2-W121-S2 | BLOCKING/INERT | RESOLVED | deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_ANLREQ_RELEASE29_ORDINARY_VIEWER_AND_SHARES_WORDS_CTO_HALF.md:18 | CTO half accepts the retained-repository reach as named in the release-29 pair |
| D2-W122-S1 | BLOCKING/INERT | RESOLVED | 322c4fed4eb drain(slot 122 TO-AR-y-308) row W122-S1 accepted | Issuer accepted the shipped words; the loose wording was the issuer's; no reader change |
| D2-W123-S1 | OBSERVATION/ARMED | RESOLVED | 04ac01333bf merge(TO-APPLY-R29a) source-map record for irpt-status after release 29 leg L2 | Applier re-pinned irpt-status in the map, as v23 held it should |
| D2-S96 | BLOCKING/INERT | RESOLVED | 260141f23b2 (TO-EXERCISE-R30 run 2: owner check refuses K1-K3 HTTP 400); db961a401a1 | Owner check on input_id (AR-y-316) live in release 29b; other-firm inputs refused live |
| D2-W126-S1 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-316.submit-input-owner-check.md:44 (AMENDMENT 1 (i)) | Invocation gained --color=no; drain 49f70cd0783 records the row dispositioned |
| D2-W126-S2 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-316.submit-input-owner-check.md:44 (AMENDMENT 1 (ii)), :39 | Ruling limits the check to CLIENT-class callers; INTERNAL submit never reaches the grant |
| D2-S97 | BLOCKING/INERT | RESOLVED | dd4279282a1 (W128-S3 disarmed: the pop at interactive_access.py:138 is in the closed r33 release) | Cause named by AR-y-318, fixed by AR-y-319, live in r33 |
| D2-W136-S1 | OBSERVATION/ARMED | LIVE | data/transcripts/scripts/commentary/lambda_handler.py:392-402,426-429 | A send that raises after persist is reported only as a hop failure with no batchItemFailures; redelivery stops at draft_exists; the I4 handoff is lost |
| D2-W139-S1 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-331.commentary-pdf-backend-route.md:66 (AMENDMENT 1) | Ruling uses a local _commentary_logical_id helper; source map and producer import untouched |
| D2-W140-S1 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-332.ticket-page-commentary-pdf-reader.md:71 (AMENDMENT 1) | Grant gained envelope.ts |
| D2-W140-S2 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-332.ticket-page-commentary-pdf-reader.md:71 (AMENDMENT 1) | Seven pinned tests brought into an amended grant |
| D2-W139-S2 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-331.commentary-pdf-backend-route.md:63 (AMENDMENT 2) | Grant widened to routes.json; AC1 and AC3 amended |
| D2-W139-S3 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-331.commentary-pdf-backend-route.md:63, :51 | AMENDMENT 2 added ops/pdf_link.py to the grant |
| D2-W140-S3 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-332.ticket-page-commentary-pdf-reader.md:68 (AMENDMENT 2) | Issuer corrected its grant path to envelope.ts |
| D2-W140-S4 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-332.ticket-page-commentary-pdf-reader.md:68 (AMENDMENT 2) | AR-y-331 merged first, then generators and pins run against it |
| D2-W140-S5 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-332.ticket-page-commentary-pdf-reader.md:68 (AMENDMENT 2) | AMENDMENT 2 answers the out-of-grant fake clients; order complete |
| D2-W140-S6 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-332.ticket-page-commentary-pdf-reader.md:68, :64 | Re-pin follows AR-y-331 routes row; AMENDMENT 3 re-pins in-grant counts |
| D2-W139-S7 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-331.commentary-pdf-backend-route.md:60 (AMENDMENT 3) | Grant gained the response schema and denominator counts; AC3 amended |
| D2-W143-S2 | OBSERVATION/ARMED | LIVE | d461cdb47fe "IRPT_ANLREQ-D2-W362-S1 -- client-data-check ABSENT on dell2" (2026-10-21) | Hashed account-id list still absent on dell2 as of 10-21; 546a502ca46 says the gate rows stay armed until the HMAC list lands |
| D2-W140-S8 | BLOCKING/INERT | RESOLVED | org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-332.ticket-page-commentary-pdf-reader.md:64 | AMENDMENT 3 widened the grant to cover the fixtures smoke map; order went complete (58e951da550) |
| D2-W140-S9 | BLOCKING/INERT | RESOLVED | IRPT_ANLREQ.TO-AR-y-332.ticket-page-commentary-pdf-reader.md:64 | AMENDMENT 3 widened the grant to cover the published-map excused list; order complete (58e951da550) |
| D2-W140-S10 | BLOCKING/INERT | RESOLVED | IRPT_ANLREQ.TO-AR-y-332.ticket-page-commentary-pdf-reader.md:64 | AMENDMENT 3 widened the grant to cover the responses.ts envelope and the no-status-reason test; order complete |
| D2-W140-S11 | BLOCKING/INERT | RESOLVED | IRPT_ANLREQ.TO-AR-y-332.ticket-page-commentary-pdf-reader.md:64 | AMENDMENT 3 widened the grant to cover the carry unprojected-grant list; order complete |
| D2-W145-S2 | BLOCKING/INERT | RESOLVED | org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~145/IRPT_ANLREQ.TO-AR-y-339.irpt-status-release-31-build.proof_of_spec.json:136 | AMENDMENT 1 dropped the stale pins and amendment 3 re-pinned status_installed.py; TO-AR-y-339 complete |
| D2-W144-S6 | BLOCKING/INERT | RESOLVED | org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~145/r41/IRPT_STATUS_R31_BUILD.json:92 | The deleted live-read/ was ~145's download; ~145 re-staged it in its own folder and TO-AR-y-339 completed |
| D2-S115 | BLOCKING/INERT | RESOLVED | org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md:16907 | Row S116 disarms it: addendum 1 leg A added the gateway route, applied and read back (route 0bxt97o) |
| D2-W172-S1 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:17478 | Closing row W172-S3: issuer widened the sparse checkout and the AR-g-53 record answered Q1-Q4 from source |
| D2-W173-S1 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:17533 | Closing row W173-S2: issuer widened the sparse checkout; the AR-g-54 record was committed at 80be7fd041 |
| D2-S120 | BLOCKING/INERT | RESOLVED | org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-352.fwd1-driver-post-allowlist-trace-and-amend.md:85 | TO-AR-y-352 (complete) amended the driver's POST allow-list; window 2 then filed the ticket (faf23f293f8) |
| D2-W190-S1 | BLOCKING/INERT | RESOLVED | org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~190/IRPT_ANLREQ.TO-AR-t-31.commentary-drafter-figure-block.proof_of_spec.json:91 | AMENDMENT 1 (36a56617cb) widened the cone; AC1 ran on the real tree; TO-AR-t-31 complete |
| D2-W178-S1 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:18181 | Closing row W178-S2: issuer widened the worktree; AC2 passes 108 |
| D2-W179-S1 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:18318 | Row W179-S5: issuer widened the cone to infra/ and docs/; AC2 passes 65 of 65 |
| D2-S121 | BLOCKING/INERT | RESOLVED | f3a43e0f3b9 "TO-RUN-COMMENTARY-E2E-7D: RUN-DONE PASS, both report PDFs open" | Window-2 attach failure superseded: cause read (TO-AR-y-357), later runs pass with the packager ATTACHED (b114d427283) |
| D2-S122 | BLOCKING/INERT | RESOLVED | org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/fwd1run/NEVER_WIDEN_PAIR_ANLREQ_FWD1_RUN_ADDENDUM3_THIRD_WINDOW_COO_HALF.md:11 | ReportRefused traced to a resident registry gap (AR-y-357); later resident releases run the packager and the E2E runs pass |
| D2-W181-S1 | OBSERVATION/ARMED | LIVE | d461cdb47fe "client-data-check ABSENT on dell2" (2026-10-21) | S123 cleared this one commit by issuer read, but the gate is still blind on dell2 until the hashed list is provisioned |
| D2-W184-S1 | OBSERVATION/ARMED | LIVE | d461cdb47fe "client-data-check ABSENT on dell2" | S124 cleared this one commit by issuer read; the dell2 hashed list is still absent as of 10-21 |
| D2-W182-S1 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:18648 | Row W182-S3: issuer amendment a294ca574a added opal_naming to NESTED_OK; AC2 passes; TO-AR-g-82 complete |
| D2-W191-S1 | BLOCKING/INERT | RESOLVED | org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~T2/R42_T_CLOSE.md:15 | Sparse-cone fact only: the test passes on the main tree (69 passed); TO-AR-t-32 complete |
| D2-W187-S1 | OBSERVATION/ARMED | LIVE | d461cdb47fe "client-data-check ABSENT on dell2" | S125 cleared this one commit by issuer read; the device-level gap is unchanged until the list lands |
| D2-W188-S1 | OBSERVATION/ARMED | LIVE | d461cdb47fe "client-data-check ABSENT on dell2" | S126 cleared this one commit by issuer read; the device-level gap is unchanged until the list lands |
| D2-W157-S1 | BLOCKING/INERT | RESOLVED | 3c26947b3ed "row(IRPT_ANLREQ D2-S128 ...): DISARMS W157-S1" | Issuer re-graded AR360-y-AC1: the folder failures are the same set on origin/PROD; the new file passes 6 of 6 |
| D2-W197-S1 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:19454 (S129) | Verifier's expected list stale; the build's 15 changed / 284 identical is correct; AR92-g-AC1 passes |
| D2-W200-S1 | OBSERVATION/ARMED | LIVE | 3e5ecaad1bd "client-data check did not run (hashed account-id list absent on this box)" (row W385-S1) | S132 hand-checked one commit; the hashed list is still absent on dell2 (W299-S1, W385-S1 repeat the gap) |
| D2-W215-S1 | BLOCKING/INERT | RESOLVED | 951b98adac4 "drain(TO-AR-ty-52 ...) row D2-W215-S1 resolved by the cone change" | Cone changed; AR52-ty-AC1 R46-TESTS-OK (18); merged complete |
| D2-W163-S1 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:20494 (S135) | AR-y-367 (b6500a74b9) moved driver decisions after Submit; premise no longer matters |
| D2-W163-S2 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:20494 (S135) | Driver answers prompts after Submit; rule amended for run 3 |
| D2-W163-S3 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:20494 (S135) | Labels checker rule reworded in AR-y-367; order superseded by complete AR-y-367 |
| D2-W218-S1 | BLOCKING/INERT | RESOLVED | 2b8f087c823 "drain(TO-AR-ty-55 ...) row D2-W218-S1 resolved by the cone change" | Cone changed; AR55-ty-AC1 R46-TESTS-OK (5); complete |
| D2-W214-S1 | BLOCKING/INERT | RESOLVED | 91b2d28ec5f "drain(TO-AR-ty-51 ...) row D2-W214-S1 resolved by the cone change" | Cone changed; AR51-ty-AC1 R46-TESTS-OK (10); merged complete |
| D2-W219-S1 | BLOCKING/INERT | RESOLVED | 4f984bacc98 "drain(TO-AR-ty-56 ...) rows D2-W219-S1 resolved by the cone change" | Worker re-seated; R46-TESTS-OK 15 (feae6f4be88); complete |
| D2-W220-S1 | BLOCKING/INERT | RESOLVED | 4e33ac844f7 "drain(TO-AR-ty-57 ...) row D2-W220-S1 resolved by the cone change" | Cone changed; AR57-ty-AC1 R45-REC-OK over 23 rows; complete |
| D2-W224-S1 | OBSERVATION/ARMED | RESOLVED | INVESTIGATION_v1.md:21682 (S144) | Gate scans every OPAL_GLOBAL site under infra/aws/lambda (40 sites, 21 files), merged with AR-tz-66; register rows ruled |
| D2-W224-S2 | OBSERVATION/ARMED | RESOLVED | infra/aws/lambda/ticket_center/lambda_function.py:436-439; 028ee030b9f "PROFILE firm scope fails closed" | PROFILE row with no list gets 403 unless scope_all_firms; shipped in opal-ticket-api (d12b0d3579e) |
| D2-W252-S1 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:21168 (S142) | Missing record folder was the issuer's omission; order names it; TO-AR-g-112 complete |
| D2-S140 | BLOCKING/INERT | RESOLVED | cc972fcd73d "R33 D2/D4 stay parked"; 7174cd8a214 (TO-EXERCISE-R33 superseded) | CTO parked D2 and D4; R33 order superseded; step-2 refusal cause never named |
| D2-S141 | BLOCKING/INERT | RESOLVED | cc972fcd73d "priceDate arms accepted on the log count" | CTO ruled P1/P1M arms accepted on the log count; order superseded |
| D2-W228-S3 | OBSERVATION/ARMED | RESOLVED | b16fc01db2b (ADJUDICATION_v35, W225-S1 DISMISSED) | Stood only while W225-S1 was ARMED; W225-S1 dismissed on the deployed bytes |
| D2-S143 | BLOCKING/INERT | RESOLVED | 636d00c7a61 "yfinance 1.2.0 closure installed in the resident pydeps ... ledger CLOSED" | TO-APPLY-YFDEPS installed yfinance on the resident; r34k imports the checker (S168) |
| D2-W230-S4 | BLOCKING/INERT | RESOLVED | e536fc070a4 "AR66-tz-AC1 PASS -- R46-TESTS-OK passed=14" | G4-G11 register rows placed; acceptance passed; merged complete at 303d5fb79a2 |
| D2-W231-S1 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:21708 (S145) | Meeting POST is an EXCLUDED row outside the DONE WHEN; driver exits 0 (AR-tz-68, e2a160b783) |
| D2-W231-S2 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:21708 (S145) | --firm-b, --request-id, --job-id now required inputs (AR-tz-68) |
| D2-W258-S1 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:22072 (S146) | Sparse-cone omission was the issuer's; fixed, re-graded; TO-AR-g-121 complete |
| D2-W262-S1 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:22150 (S148) | Cone omitted docs/; worker re-seated on full checkout; TO-AR-g-129 complete |
| D2-W169-S1 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-377.ticket-form-names-the-advisor-email.md:90 | AR-y-377 superseded by AR-y-378 (typed Advisor login email, CTO ruling B, msg 9909) |
| D2-S155 | OBSERVATION/ARMED | RESOLVED | INVESTIGATION_v1.md:22926; 74622065961 correction(TO-RUN-FWD5) | IB2 withdrew the row: the four 200 answers were CONTRACT_VERSION refusal envelopes; sitting 2 read 7 of 7 refused (S159) |
| D2-W170-S4 | OBSERVATION/ARMED | RESOLVED | INVESTIGATION_v1.md:23090 (S160 DISARMS W170-S4, CTO msg 9975) | CTO disarmed it: the field may show to every staff filer who picks a firm; the server is the guard |
| D2-W285-S2 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-385.prod-based-recut-of-the-dell2-portal-set.md:36 (AMENDMENT 1); 8c0a8f2825c | The 0-failed gate became a diff against origin/PROD; order complete |
| D2-W290-S1 | BLOCKING/INERT | RESOLVED | b195f459183 cut(TO-AR-y-392 superseding TO-AR-y-391); TO-AR-y-391.md:8 superseded | The crashing order was replaced by TO-AR-y-392, which is complete |
| D2-W290-S2 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:25555 (S208); TO-AR-y-392.md:87 | AR-y-392 moved the acceptance.py pin; r36 ships get_commentary_ref, live CodeSha256 read back |
| D2-W291-S2 | OBSERVATION/ARMED | LIVE | infra/aws/lambda/ci/function-map/irpt-commentary-draft-store-lambda.json:25 (pin 283f7e7700, sha 06425d47); 239c07e50d5 enrich candidate 8 | Draft-store map still pins the old acceptance.py; deferred to enrichment candidate 8, not fixed |
| D2-S207 | OBSERVATION/ARMED | RESOLVED | f3a43e0f3b9 TO-RUN-COMMENTARY-E2E-7D RUN-DONE PASS (commentary route answered a 2-page PDF) | AR-y-470 route binding and later releases: run 7D's commentary route served a retained PDF |
| D2-W294-S2 | BLOCKING/INERT | RESOLVED | 71d88918bf0 (worker 294 read, second run authorized); d09a236b6c0 ADDENDUM 2 | The second run named an advisor and the door authorized it |
| D2-W295-S2 | BLOCKING/INERT | RESOLVED | 794f7bfb81c surprise(D2-S211, ARMED) | The block was carried forward as S211; run 3 went ahead |
| D2-S211 | OBSERVATION/ARMED | LIVE | infra/aws/terraform/investor-reporting/core/reporting_storage.tf:2 (No lifecycle disposal); no delete_object in investor-reporting/reports | Application has no deleter and no lifecycle rule; leftovers removed only by one-off delete passes |
| D2-S214 | OBSERVATION/ARMED | LIVE | org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e2/LEFTOVER.txt:2 | No delete manifest names this runs-2/3 key; the object probably stands (not checked live) |
| D2-S215 | OBSERVATION/ARMED | RESOLVED | ad01c07f934 report(1.0.0_SA_CTO~DELL2): the 425-cards fix live; fresh report 3 sections, 0 builder-only | Fix live; fresh report clean; run 5D passed the cards check |
| D2-W303-S1 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-g-166.price-pages-per-holding-price-table.md:31-33 (AMENDMENT 1); 622955a8a71 | Vendor-word rule stands; Source column prints neutral labels; AC3 passed; complete |
| D2-W303-S2 | BLOCKING/INERT | RESOLVED | TO-AR-g-166.md:32 (AMENDMENT 1); 622955a8a71 | Test file added to the grant; proof passed AC1-AC3 |
| D2-W308-S1 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.md:33 (AMENDMENT 1); c13b33d9407 | Issuer widened the sparse set; order complete |
| D2-W308-S2 | BLOCKING/INERT | RESOLVED | TO-AR-g-170.md:31 (AMENDMENT 2); a44ac16b1ba | Issuer corrected its wording and dropped the delattr from arm 1; complete |
| D2-W311-S1 | BLOCKING/INERT | RESOLVED | 478017db45b proof(TO-AR-y-417) after the sparse-set fix; flip 51e552c6046 | data/ added to the sparse set; invocations passed; complete |
| D2-W312-S1 | BLOCKING/INERT | RESOLVED | 95497d5c477 cut(AR-y-422 RetainedSections); AR-y-418 flip 326110816f6 | Follow-up AR-y-422 targets the component the Ticket Center mounts; AR-y-418 complete |
| D2-W309-S1 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-y-415.o1-staff-owner-fallback-in-create-owner-and-advisor-owner.md:40 | Issuer added data/ and terraform to the sparse set; baseline ran; complete |
| D2-S217 | OBSERVATION/ARMED | RESOLVED | 0ec21d47c5c TCKT_VNEXT TO-R22-DL1 RUN-OK (42 irpt synthetic versions deleted); TV2 r22_delete/R22_DELETE_RESULT.json:18 | Run-4 leftover key deleted by exact VersionId in the R22 pass |
| D2-W315-S1 | BLOCKING/INERT | RESOLVED | 7937889912a flip AR-y-430; c63a24c76fb r34m packet; 555d123bfcd r34m applied | No explicit ruling; the issuer built, signed and applied r34m from the edited guard |
| D2-W315-S2 | BLOCKING/INERT | RESOLVED | 7937889912a, c63a24c76fb, 555d123bfcd | No explicit ruling; text/constant edits; r34m signed and applied |
| D2-S218 | OBSERVATION/ARMED | RESOLVED | 0ec21d47c5c R22 delete; R22_DELETE_RESULT.json:26 (key ART-5c5ed7...) | Third leftover deleted in the R22 pass; fixture fixed in runs 5B-5D, 5D passed |
| D2-S219 | OBSERVATION/ARMED | RESOLVED | INVESTIGATION_v1.md:31743 | Run 5B keys in V2 R22_DELETE_MANIFEST.json; 42 of 42 versions ABSENT after TV2 delete pass |
| D2-W316-S1 | BLOCKING/INERT | RESOLVED | deliverables/2.0.0_SA_COO~G2/S220_S222_DISPOSITION_READS_20261021.md:20 | Refusal traced to the S245 packaging defect, fixed in r34q; runs 7L/7N with the unknown ticker passed |
| D2-W319-S1 | BLOCKING/INERT | RESOLVED | INVESTIGATION_v1.md:28083 (W319-S3); 2fa1a0957e4 | Issuer fixed the AC3 expectation typo; map check prints the matching line |
| D2-W331-S1 | OBSERVATION/ARMED | LIVE | 3e5ecaad1bd (W385-S1, hashed account-id list absent on this box) | The hashed list is still missing on dell2; every commit here goes unchecked |
| D2-W330-S10 | BLOCKING/INERT | RESOLVED | 527a2031207 AC3 regress PASS (OWN[175]) | Issuer added the file to the checker OWN[175]; regress passed |
| D2-W330-S11 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-g-175.producer-comparison-stage-and-resident-ports.md:37 | AMENDMENT 4 replaced the sys.path restore with a module-scoped fixture; order complete |
| D2-W343-S9 | BLOCKING/INERT | RESOLVED | task-orders/IRPT_ANLREQ.TO-AR-g-175.producer-comparison-stage-and-resident-ports.md:35 | AMENDMENT 3 added model_bytes to the expected key set; order complete |
| D2-W333-S1 | BLOCKING/INERT | RESOLVED | 19e5ae70525 (TO-AR-g-177 AR177-g-AC1 PASS after re-seat) | AC1 3 passed after re-seat; order complete (5de15b03540) |
| D2-W333-S2 | BLOCKING/INERT | RESOLVED | 19e5ae70525 (AR177-g-AC2 PASS, 9 passed) | AC2 file present after re-seat and passed; order complete |
| D2-W355-S1 | OBSERVATION/ARMED | RESOLVED | deliverables/2.0.0_SA_COO~G2/AR183_AC2_ISSUER_REGRADE_20261021.md:16 | Issuer rule adds data/ to the cone for registry-reading cells; AR-g-182 complete |
| D2-W356-S1 | BLOCKING/INERT | RESOLVED | deliverables/2.0.0_SA_COO~G2/AR183_AC2_ISSUER_REGRADE_20261021.md:16 | Full-tree re-grade passed=51 |
| D2-W356-S2 | BLOCKING/INERT | RESOLVED | deliverables/2.0.0_SA_COO~G2/AR183_AC2_ISSUER_REGRADE_20261021.md:16 | Same full-tree re-grade passed=51; ycharts folder now in later cones |
| D2-W359-S1 | BLOCKING/INERT | RESOLVED | deliverables/2.0.0_SA_COO~G2/AR186_AC3_ISSUER_REGRADE_20261021.md:19 | Full-tree re-grade passed=85; order complete |
| D2-W363-S1 | OBSERVATION/ARMED | LIVE | 3e5ecaad1bd (W385-S1) | Hashed account-id list still absent; commits on this box stay unchecked |
| D2-S254 | OBSERVATION/ARMED | LIVE | ADJUDICATION_v31.md:59 | Run 7K synthetic S3 residue; no delete pass past runs 7e-7j |
| D2-S255 | OBSERVATION/ARMED | LIVE | ADJUDICATION_v31.md:59 | Run 7L synthetic S3 residue; newest manifest covers 7e-7j only |
| D2-S257 | OBSERVATION/ARMED | LIVE | ADJUDICATION_v31.md:59 | Run 7M synthetic S3 residue; no delete pass covers 7k-7n |
| D2-S258 | OBSERVATION/ARMED | LIVE | deliverables/2.0.0_SA_COO~Y2/synthetic_residue_delete_list_supplement_runs7e_7j_20261021.json | Run 7N residue surfaced after the last delete pass (7e-7j, 193a8fe72e3) |

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S19",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-21T18:10:00Z",
  "one_line": "L8 compile of the 133 undispositioned IRPT_ANLREQ items (2026-10-13 to 10-21): 114 DISMISSED as resolved, each with its pointer in this file's table; 19 still live, graduating ARMED with their owners at the slug.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_ANLREQ-D2-S115",
   "IRPT_ANLREQ-D2-S120",
   "IRPT_ANLREQ-D2-S121",
   "IRPT_ANLREQ-D2-S122",
   "IRPT_ANLREQ-D2-S140",
   "IRPT_ANLREQ-D2-S141",
   "IRPT_ANLREQ-D2-S143",
   "IRPT_ANLREQ-D2-S155",
   "IRPT_ANLREQ-D2-S207",
   "IRPT_ANLREQ-D2-S215",
   "IRPT_ANLREQ-D2-S217",
   "IRPT_ANLREQ-D2-S218",
   "IRPT_ANLREQ-D2-S219",
   "IRPT_ANLREQ-D2-S83",
   "IRPT_ANLREQ-D2-S93",
   "IRPT_ANLREQ-D2-S94",
   "IRPT_ANLREQ-D2-S96",
   "IRPT_ANLREQ-D2-S97",
   "IRPT_ANLREQ-D2-W101-S1",
   "IRPT_ANLREQ-D2-W101-S3",
   "IRPT_ANLREQ-D2-W103-S1",
   "IRPT_ANLREQ-D2-W107-S1",
   "IRPT_ANLREQ-D2-W109-S1",
   "IRPT_ANLREQ-D2-W111-S4",
   "IRPT_ANLREQ-D2-W112-S4",
   "IRPT_ANLREQ-D2-W118-S2",
   "IRPT_ANLREQ-D2-W120-S1",
   "IRPT_ANLREQ-D2-W120-S2",
   "IRPT_ANLREQ-D2-W121-S2",
   "IRPT_ANLREQ-D2-W122-S1",
   "IRPT_ANLREQ-D2-W123-S1",
   "IRPT_ANLREQ-D2-W126-S1",
   "IRPT_ANLREQ-D2-W126-S2",
   "IRPT_ANLREQ-D2-W139-S1",
   "IRPT_ANLREQ-D2-W139-S2",
   "IRPT_ANLREQ-D2-W139-S3",
   "IRPT_ANLREQ-D2-W139-S7",
   "IRPT_ANLREQ-D2-W140-S1",
   "IRPT_ANLREQ-D2-W140-S10",
   "IRPT_ANLREQ-D2-W140-S11",
   "IRPT_ANLREQ-D2-W140-S2",
   "IRPT_ANLREQ-D2-W140-S3",
   "IRPT_ANLREQ-D2-W140-S4",
   "IRPT_ANLREQ-D2-W140-S5",
   "IRPT_ANLREQ-D2-W140-S6",
   "IRPT_ANLREQ-D2-W140-S8",
   "IRPT_ANLREQ-D2-W140-S9",
   "IRPT_ANLREQ-D2-W144-S6",
   "IRPT_ANLREQ-D2-W145-S2",
   "IRPT_ANLREQ-D2-W157-S1",
   "IRPT_ANLREQ-D2-W163-S1",
   "IRPT_ANLREQ-D2-W163-S2",
   "IRPT_ANLREQ-D2-W163-S3",
   "IRPT_ANLREQ-D2-W169-S1",
   "IRPT_ANLREQ-D2-W170-S4",
   "IRPT_ANLREQ-D2-W172-S1",
   "IRPT_ANLREQ-D2-W173-S1",
   "IRPT_ANLREQ-D2-W178-S1",
   "IRPT_ANLREQ-D2-W179-S1",
   "IRPT_ANLREQ-D2-W182-S1",
   "IRPT_ANLREQ-D2-W190-S1",
   "IRPT_ANLREQ-D2-W191-S1",
   "IRPT_ANLREQ-D2-W197-S1",
   "IRPT_ANLREQ-D2-W214-S1",
   "IRPT_ANLREQ-D2-W215-S1",
   "IRPT_ANLREQ-D2-W218-S1",
   "IRPT_ANLREQ-D2-W219-S1",
   "IRPT_ANLREQ-D2-W220-S1",
   "IRPT_ANLREQ-D2-W224-S1",
   "IRPT_ANLREQ-D2-W224-S2",
   "IRPT_ANLREQ-D2-W228-S3",
   "IRPT_ANLREQ-D2-W230-S4",
   "IRPT_ANLREQ-D2-W231-S1",
   "IRPT_ANLREQ-D2-W231-S2",
   "IRPT_ANLREQ-D2-W252-S1",
   "IRPT_ANLREQ-D2-W258-S1",
   "IRPT_ANLREQ-D2-W262-S1",
   "IRPT_ANLREQ-D2-W285-S2",
   "IRPT_ANLREQ-D2-W290-S1",
   "IRPT_ANLREQ-D2-W290-S2",
   "IRPT_ANLREQ-D2-W294-S2",
   "IRPT_ANLREQ-D2-W295-S2",
   "IRPT_ANLREQ-D2-W303-S1",
   "IRPT_ANLREQ-D2-W303-S2",
   "IRPT_ANLREQ-D2-W308-S1",
   "IRPT_ANLREQ-D2-W308-S2",
   "IRPT_ANLREQ-D2-W309-S1",
   "IRPT_ANLREQ-D2-W311-S1",
   "IRPT_ANLREQ-D2-W312-S1",
   "IRPT_ANLREQ-D2-W315-S1",
   "IRPT_ANLREQ-D2-W315-S2",
   "IRPT_ANLREQ-D2-W316-S1",
   "IRPT_ANLREQ-D2-W319-S1",
   "IRPT_ANLREQ-D2-W330-S10",
   "IRPT_ANLREQ-D2-W330-S11",
   "IRPT_ANLREQ-D2-W333-S1",
   "IRPT_ANLREQ-D2-W333-S2",
   "IRPT_ANLREQ-D2-W343-S9",
   "IRPT_ANLREQ-D2-W355-S1",
   "IRPT_ANLREQ-D2-W356-S1",
   "IRPT_ANLREQ-D2-W356-S2",
   "IRPT_ANLREQ-D2-W359-S1",
   "IRPT_ANLREQ-D2-W62-S6",
   "IRPT_ANLREQ-D2-W62-S9",
   "IRPT_ANLREQ-D2-W74-S1",
   "IRPT_ANLREQ-D2-W76-S2",
   "IRPT_ANLREQ-D2-W78-S3",
   "IRPT_ANLREQ-D2-W79-S1",
   "IRPT_ANLREQ-D2-W79-S2",
   "IRPT_ANLREQ-D2-W80-S1",
   "IRPT_ANLREQ-D2-W84-S1",
   "IRPT_ANLREQ-D2-W92-S1",
   "IRPT_ANLREQ-D2-W93-S1",
   "IRPT_ANLREQ-D2-W97-S2"
  ],
  "spec_asserts": "Spine L8/L10: every investigation item is dispositioned by a new row naming it in adjudicates before the slug; a BLOCKING row is resolved when the order that raised it is amended, superseded or completed on a fix.",
  "world_is": "Of 133 items: 114 resolved (task-order amendments, drain/flip commits, later disarm rows, live releases, the R22 delete pass); 19 live: 8 rows on the absent dell2 hashed account-id list, 6 synthetic S3 residue rows, 5 product or build defects (W90-S3, W103-S4, W107-S3, W136-S1, W291-S2).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "per-row pointers in the table of org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/adjudications/ADJUDICATION_v37.md, gathered by six read-only reads directed by this seat",
    "this seat's spot reads: TO-AR-y-332:64, ticket_center/lambda_function.py:436-439, TV2 r22_delete/R22_DELETE_RESULT.json:18,26, TO-AR-y-217:37, portal TicketCenter.tsx:211, function-map/irpt-commentary-draft-store-lambda.json:25, commentary/lambda_handler.py:392-402"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Each resolved item is closed by the amendment, later cell, ruling, release or delete pass its table row names; the live items are not adjudicated here and graduate with their owners."
 }
]
```

-- `3.0.0_SA_CVO~DELL2`
