# TO IRPT_BCKEND.TO-IB-pr-383 -- the ONE directory release (IB-pr-380 + IB-pr-381, pin 7f31bbfa4e) applied, then the per-firm seeding run, then the after-read

<to_id>IRPT_BCKEND.TO-IB-pr-383</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~DELL2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>94</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:**
- the pair: packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~189/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-380_381.md`
  (blob d60e4a9a75); COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_380_381_DIRECTORY_RELEASE_COO_HALF.md` @8323d3fb19; CTO
  half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_380_381_DIRECTORY_RELEASE_CTO_HALF.md` @f0a2f049f7 (msg 2151, GIVEN with
  conditions);
- CTO ruling msg 1988 (one release, live before cottonwood's OVER_AGE on 2026-10-12);
- Andrew-direct: dell2 deploys go to `0.7.0_AE_CloudOps~DELL2` (msg 1756).

**Decomp cell:** `IB-pr-383` (decomposition section 87) | **outcome_ref:** FWD-7 (directory READY at all 3 firms) | **depends_on:**
IB-pr-380 and IB-pr-381 (both complete, drained @93e31749b4). **Deadline:** live by Friday 2026-10-09's close.

---

## WORKER FACE

Work in your own worktree cut from `box/dell2`. The packet is your whole procedure. Read it IN FULL, then both halves; where they add
conditions, the halves win. In order:

1. **CTO condition (S3):** show `tests/test_holdings_rearm_trigger.py::test_rearm_trigger_live` red at base `2c1f4f425d`, in a clean
   worktree, before anything else. If it is not red there, STOP.
2. **The replay arm, BEFORE the ledger.** Run the packet's "replay arm for the applier" against the artifacts actually in play: the zip
   you will upload, the bundle you will upload, and the LIVE zip `RbpsijC2...`. Use a scratch directory OUTSIDE every worktree and delete
   it after, because it holds client entries. Any stop condition in the packet ends the order.
3. **Open the ledger** (NEVER-2) in `org/critical_paths/change_management/`, with its `.open_deploys` sentinel.
4. **Land the two artifacts**, each verified live:
   - `irpt-directory-refresh` at pin `7f31bbfa4e` through Terraform. `safe-apply` targets the function in
     `infra/aws/terraform/investor-reporting/directory/`; plan, then apply from the planfile. After it, the live CodeSha256 must equal
     `6eOFTopG9nvfjpJFJxtBNAUL43pBmg0YvHv9sbErfsM=`, and a re-plan must show 0.
   - The runner bundle: `bash .tools/safe-deploy.sh data/assets/scripts/gold/investor_reporting/directory_runner.py`. After it, the ETag
     must equal md5 `b0356a757b1ae92e3a4b46a847378315` and the sha256 must equal
     `2e3e6648312f5daad1da91f0c3aaeb4736a81b16cc9bb0dd4f43e5e93886b968`.
   Record the live bundle version before and after.
5. **The seeding run** (packet Branch A step 2; CTO condition: never concurrent with a scheduled fire, so outside 13:20-14:00Z).
   Run inflection, then cottonwood, with the packet's exact `--previous-key` per firm. After each, read the landed dated key for the
   carried TERMINATED entry. Record which sub-branch ran (same-date overwrite or new-date key) and the S3 versions written.
6. **The after-read:** drive one refresh per firm, then read each `_refresh/<date>/manifest.json` at the manifest's own as_of. Record per
   firm:
   - `reason_code`, `manifest_as_of` and `terminated_count`;
   - `carried_in_served`, from the served `directory.json`;
   - for 49financial, `source_client_ids_present` read from its first landing with the new bundle (CTO condition).
7. **Close the ledger.**
8. **After-reads file** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~DELL2/IB94-2_directory_release_after_reads.json`
   holds:
   - `{replay_before_ledger: "identical"|..., ledger: "CLOSED"|..., rolled_back}`;
   - `bundle: {bundle_live_version_before, bundle_live_version_after, bundle_sha256, etag}`;
   - `seeding: {...}`;
   - `driven_refresh: {per_firm: {<firm>: {reason_code, manifest_as_of, terminated_count, carried_in_served,
     source_client_ids_present?}}}`;
   - `s71_red_at_base`.

If any step fails, apply nothing more and run Branch B per the packet (restore the seeded keys last-written-first, `latest.json` last).
File a row.

<criterion id="IB94-2-AC1" cell_refs="IB-pr-383"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r94/p94_release_cells.py" . IB94-2-AC1</invocation><expect>IB94-2-AC1 PASS</expect></criterion>
`IB94-2-AC1` -- the live refresh CodeSha256 equals the built `6eOFTopG...`, the bundle landed at the built sha, the replay ran before the
ledger, and the ledger is CLOSED. Base: FAIL (live is RbpsijC2).

<criterion id="IB94-2-AC2" cell_refs="IB-pr-383"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r94/p94_release_cells.py" . IB94-2-AC2</invocation><expect>IB94-2-AC2 PASS</expect></criterion>
`IB94-2-AC2` -- the driven refresh is READY at all 3 firms with `terminated_count` 1/1/0. The carried entry is in the served directory at
inflection and cottonwood, and 49financial's first landing is read. Base: FAIL (no file).

<expected_criteria>IB94-2-AC1, IB94-2-AC2</expected_criteria>

## AMENDMENT 1 (2026-10-09 ~13:1xZ, issuer 2.0.0_SA_COO~P2, on the CTO's 380/381 half AMENDMENT 1 @25f78da818 (msg 2952 (2)))

The seeding legs (S1/S2/V1) are released. The CTO bound the seeding to the live runner bundle `f6d48603` (S3 version `W2Wragr`) on this
lane's re-grade (`IB94-2_live_held_read_f6d48603.json` @0b1087120f). Conditions:
- **Bundle:** re-verify by content that the live runner bundle is still `f6d48603`, immediately before the first firm. A different bundle
  is a STOP.
- **Per firm:** re-read that firm's held state immediately before its run.
- **Refusal:** a refusal stops the remaining firms and is a BLOCKING row.
- **All three firms or none:** never leave the seed partial past one firm's run; Branch B for any seeded firm otherwise.
- **TO-APPLY-27's conditions stand:** tell the laptop before any firm-bucket write, report each send, and write no 49financial data into
  another tree.
- **Ledger:** the parked entry `irpt-directory-release-20261009` (@9a461397a4) resumes. Commit each leg as it closes, then close it.
Criteria are unchanged (`p94_release_cells.py` IB94-2).

Gate limb: none graded this modification (LIMB 6 fires on newly-added orders only; placeholders NONE).

## AMENDMENT 2 (2026-10-09 ~13:2xZ, issuer 2.0.0_SA_COO~P2): the seeding WRITE SET, stated exactly (corrects AMENDMENT 1's wording)

The write set is the CTO 380/381 half's, and nothing else: ONE runner run per firm, **inflection then cottonwood**, writing **4 objects in
2 buckets** (per firm: the dated `directory.json` and `latest.json`). **49financial is NOT seeded:** step 6 READS its first landing, and no
49financial key is written. AMENDMENT 1's "all three firms or none" names the held-state gate (all three held at zero in source,
re-grade @0b1087120f) and the no-partial rule across the two seeded firms. If inflection lands and cottonwood refuses or fails,
inflection goes to Branch B. The CTO's 13:20-14:00Z scheduled-fire exclusion stands.

Gate limb: none graded this modification (LIMB 6 fires on newly-added orders only; placeholders NONE).

## BOUNDS

- **Grant:** the `<paths>` block below and nothing else.
- **The only served changes:**
  - `irpt-directory-refresh`'s code;
  - the runner bundle object;
  - the four seeded keys the halves name, per sub-branch.

  There is no IAM, route, schedule, env or other function change. Applies are targeted only.
- **No vendor call**, no call off Opal infrastructure, no monitor, alarm, SNS or SES.
- **A new-date key's rollback is an S3 delete.** It needs the human confirmation the workspace law reserves. The default rollback
  restores `latest.json` and overwrites with the prior build, with no delete.
- **Refusal clause:** STOP, file a row, and apply nothing more (Branch B if already applied) on any of these:
  - a moved start sha;
  - a census other than the packet's;
  - a built sha other than the packet's;
  - a failed replay;
  - a plan touching anything else;
  - a failed read-back.
- **Row ids** are `IRPT_BCKEND-D2-S<n>`; take the next free number from the channel at HEAD. `surfaced_at` is the real time.
- **Commit** with your own author line via `bash .tools/safe-commit.sh -F <msgfile>`. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-383.directory-release-380-381-applied-and-seeded.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~DELL2/
infra/aws/terraform/investor-reporting/directory/
infra/aws/terraform/investor-reporting/CHANGELOG.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/CHANGELOG.md
infra/aws/lambda/ci/lambda-source-map.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 87 (round 94, workstream ~P), cell `IB-pr-383`.
<owned_cells>IB-pr-383</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB94-2-AC1, IB94-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~DELL2/IRPT_BCKEND.TO-IB-pr-383.directory-release-380-381-applied-and-seeded.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give:
- the live shas before and after, and the bundle versions;
- the seeding sub-branch per firm, with the S3 versions written;
- the after-read per firm;
- the ledger entry;
- each criterion's last line;
- any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- writers of the served directory: 1 (directory_runner.land, 33/33 versions matched, IB93-1 writers file); irpt-directory-refresh live RbpsijC2 (S3 Ntv3Br2Y); bundle live JITP9ecN; seeding writes 4 keys (2 per firm), rollback versions in both halves.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; refresh writes _refresh/* only, runner role unchanged.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedules are not changed; the seeding run avoids the 09:30/09:40 ET fires (CTO condition).
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p94_release_cells.py dry-run at base f506a07c1a+ff on dell2 2026-10-09 ~02:1xZ: AC1 FAIL (live RbpsijC2 != built 6eOFTopG), AC2 FAIL (no after-reads file); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; dell2 applies by its own applier (Andrew-direct msg 1756); the bundle mint is the DS-lane act routed to the applier with the pair (CLAUDE.md 13).
</preflight>
