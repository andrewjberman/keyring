# TO IRPT_DASHBD.TO-DB-b-95 -- E1: apply the R44 release -- DB-b-90 + DB-b-91 as ONE gold Lambda release over live yIAQjspL, under the signed pair (COO half @723a5e7d62, CTO half @fa8d2c2961)

<to_id>IRPT_DASHBD.TO-DB-b-95</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~70</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>47</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's R44 CTO half @fa8d2c2961 and ADDENDUM 13.1 (msg 3413), enrichment item E1 | **Decomp cell:** `DB-b-95` (decomposition section 49) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-94 (drained), both halves SIGNED.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-70`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~70/`.

**The cell (`DB-b-95`).** Both halves of the R44 pair are SIGNED against the packet blob `2d373de0a0` (sha256 `28e224f0...`). Read all three files
in `C:/dev/wk-irpt-dashbd-70` before acting:
- the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~69/NEVER_WIDEN_PACKET_R44_RELEASE.md` and its census `R44_RELEASE_CENSUS.json`;
- the COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_R44_RELEASE_COO_HALF.md`;
- the CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R44_RELEASE_CTO_HALF.md`.

The procedure and its traps are the R37 delta's: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~63/R37_DELTA_RECORD.json` and its packet.

1. **Ledger first.** Open it with `python .tools/deploy_ledger.py`, pinned to the packet sha256 `28e224f0...`. Add a first-fire sizing leg that stays
   OPEN for the issuer. Commit after each leg, and record `ledger_entry`.
2. **Before reads.** Read live `irpt-49f-reporting-gold-lambda` CodeSha256 again: it must be `yIAQjspL...`, else STOP. Record it as
   `base_codesha256_before`. Read the `_status/` prefix under the activity table for every firm the function serves, expect 0 objects, print
   the read, and record `status_prefix_objects_before`. Re-read the rollback anchor (S3 version `a.YllA9SmwwfY34NlajqOaNsex2bBZAy`).
3. **Build at this worktree's base,** whose `handler.py` blob is `7c9bb9dcdc5b`. Do NOT merge box/dell2 into this worktree before the build: a later
   handler edit (DB-b-97) must not ride this release.
   - Re-pin `account_activity_lots.py` in the source map to `d18ddf000d`. `reporting_policies.json` stays at its pin `0c35aeeaa8`.
   - Re-read every staged pin with `git show <pin>:<path> | sha256sum`.
   - Build with `infra/aws/lambda/ci/build-and-upload.sh`, BEFORE upload, and compare the built zip's members against the live zip (download it
     by its S3 version).
   - `upload_member_diff` must be EXACTLY the two member paths, and `reporting_policies.json` must equal live's bytes. Any third difference: STOP
     before upload.
   - Record `build_commit` and `built_codesha256`.
4. **Plan and apply.** The targeted plan (`-target=module.irpt_reporting_gold.aws_lambda_function.this`) must read `0 to add, 1 to change, 0 to
   destroy`; record `plan` {add, change, destroy}. Anything else is a STOP. Then ONE `.tools/safe-apply.sh` from the saved plan.
   - Read back `live_codesha256_after`; it must equal the built value. Stamp it with `record-deploy-scope.py`.
   - A post-apply plan must read `No changes`; record `replan_no_changes`.
5. **No invoke.** The next scheduled fire is the sizing read (85% of the timeout and of the memory). The issuer reads it and closes that leg.

Record `R44_APPLY_RECORD.json`. Report the deploy to `0.0.0_AB_MSTR~DELL2` through the issuer.

<criterion id="DB47-1-AC1" cell_refs="DB-b-95"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r47/p47_round47.py" . DB47-1-AC1</invocation><expect>DB47-1-AC1 PASS</expect></criterion>
`DB47-1-AC1` -- the R44 release is live over yIAQjspL with exactly the two members, plan 0/1/0, and live equal to the build. Base: FAIL.

<expected_criteria>DB47-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** under the signed pair, you build, upload and run ONE targeted safe-apply of the gold Lambda function, and you edit the source map in `infra/aws/lambda/investor-reporting/reporting-gold/`. No invoke. Deletes are Andrew's.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~70/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~70/
org/critical_paths/
infra/aws/lambda/investor-reporting/reporting-gold/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-95.r44-release-apply.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 49 (round 47), cell `DB-b-95`.
<owned_cells>DB-b-95</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB47-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~70/IRPT_DASHBD.TO-DB-b-95.r44-release-apply.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB47-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the before reads, the build commit, the member diff, the plan, the readback, the ledger entry, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one function, irpt-49f-reporting-gold-lambda; the pair's census names exactly two changed members.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the pair's radius reads no new grant, action or role statement.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the R37 schedule is unchanged; the next scheduled fire is the sizing read.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB47-1-AC1 FAIL at base (no record). R44 pair: COO @723a5e7d62, CTO @fa8d2c2961.
lane: the <paths> block IS the grant.
</preflight>
