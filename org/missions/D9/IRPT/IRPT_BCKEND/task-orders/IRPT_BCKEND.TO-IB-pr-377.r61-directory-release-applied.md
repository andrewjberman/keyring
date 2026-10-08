# TO IRPT_BCKEND.TO-IB-pr-377 -- the r61 directory release applied on dell2: irpt-directory-refresh (refresh.py only) then irpt-directory-search (the over-age branch), at release pin 4710b8007b

<to_id>IRPT_BCKEND.TO-IB-pr-377</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~DELL2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>89</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** both halves of the r61 directory release (packet + COO half
`deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_R61_DIRECTORY_RELEASE_PACKET_20261007.md` @0c3d443030; CTO half
`deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R61_DIRECTORY_RELEASE_CTO_HALF.md` @74e91285b4); the applier's ask (msg 1832); Andrew-direct
dell2 deploys go to `0.7.0_AE_CloudOps~DELL2` (msg 1756) | **Decomp cell:** `IB-pr-377` (decomposition section 82) | **outcome_ref:** FWD-7
| **depends_on:** row S364 cleared by row D2-S11 (terraform on dell2 verified).

---

## WORKER FACE

**Who:** `0.7.0_AE_CloudOps~DELL2`. Work in a clean worktree cut from `box/dell2` at or after `4710b8007b`. Never build in the dell2
shared tree.

**What is signed.** Two functions, in this order:
1. `irpt-directory-refresh`: `refresh.py` ONLY. `handler.py` stays at its running blob `48313e9c0e` (the CTO half's P2 rider ruling;
   the staged row pins it).
2. `irpt-directory-search`: `entry.py` changed; `expiry.py` and `trading_calendar.py` added. This is the over-age branch, which answers
   `{_data, _status}` with `DIRECTORY_OVER_AGE`/`STALE` or `CALENDAR_UNAVAILABLE`/`UNCERTAIN`.

Both gates were met on 10-07 (row S364): P1, the consumer read 6/6 (IB-pr-341 @55dce54d28), and P2, the rider pinned back (IB-pr-337).

**Release pin 4710b8007b; the issuer measured it on 2026-10-08 ~22:5xZ.**
- `release-census.py irpt-directory-refresh --pin 4710b8007b` reads `changed refresh.py`, `changed_members=1`.
- `--pin 4710b8007b` for `irpt-directory-search` reads `changed entry.py`, `added expiry.py`, `added trading_calendar.py`,
  `changed_members=3`. These equal the signed member lists.
- `entry.py`'s bytes differ from the packet's pin `b9411881a0` by ONE commit, `4850c85632` (IB-pr-341: the over-age `_status`
  carries only public members). That is the fix the CTO half's P1 gate required. `expiry.py` and `trading_calendar.py` are
  byte-identical to the signed pin.
- The root `infra/aws/terraform/investor-reporting/directory` IS initialized and applied. Its state object
  `investor-reporting/directory/tfstate` is 195,705 bytes, last modified 2026-10-06T01:40:04Z. **The "SKELETON ONLY, NOT INITIALISED"
  header in its main.tf is stale** (written by IB-s-18 on 2026-09-10). Initialize against the existing backend; do not re-create it.

**Steps.**
0. **Start reads.**
   - Live `irpt-directory-refresh` CodeSha256 must be `DXuzx9jpOPKOq+CjWwL36SumE5tRBZA/kfi3y5jKBgk=`.
   - Live `irpt-directory-search` must be `cmNmYm1jeyjoaUUeOCEV6AZS+Wdg3zfySn1DxC8Ftx0=`.
   - Either different: STOP.
   - Both censuses at `4710b8007b` must read as above. Anything else: STOP.
1. **Ledger** (NEVER-2), opened first with its sentinel committed. Rollback sources: refresh S3 version
   `M8O8zFhaS8YGlWPgya0PtiCIXfLSaTmR`; search S3 version `S5vL.tP9KPBcoAnJVlD2z6mBLX5Ai6CR`.
2. **Build both** with `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting <fn>` from your clean tree at the pin.
3. **Targeted `safe-apply` of the directory root, refresh first, then search.** Read back each CodeSha256 = the built sha. Re-plan each
   target: 0. Census each at the pin: `changed_members=0`.
4. **Real runs** (packet section 4.3):
   - (b) The five-arm controlled-clock drive (`deliverables/0.9.0_WK_IRPT_BCKEND~2/ib_s_4_controlled_clock.py`) against the DEPLOYED
     modules: unzip the live zip and import from it.
   - (a) The driven refresh fire READY manifest and (c) the over-age search read touch firm buckets, which deny the dell2 identity
     (S347). Write each as a request FILE for the laptop under the standing rule (msg 215). Leave those two ledger legs OPEN until the
     file lands. The activation legs close on the CodeSha read-backs.
5. **Record** the deploy with the recorder, and correct the refresh record per row S357 (packet step 4).
6. **Branch B.** If a read-back or re-plan fails, roll that function back to its S3 version the same turn, write `rolled_back: true`,
   and file a BLOCKING row.

**After-reads file:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~DELL2/IB89-1_r61_release_after_reads.json`, holding:
- `pin`;
- `functions: {<fn>: {census_changed_members, built_sha, post_census_changed_members, replan_changes, rollback_source_version}}`;
- `five_arm_drive: {rc, arms_passed, arms_total, against: "deployed"}`;
- `laptop_file_requests` (the paths for (a) and (c)), `ledger_entry`, `ledger_activation_legs_closed`, `rolled_back`, `limits`.

<criterion id="IB89-1-AC1" cell_refs="IB-pr-377"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r89/p89_cells.py" . IB89-1-AC1</invocation><expect>IB89-1-AC1 PASS</expect></criterion>
`IB89-1-AC1` -- pin 4710b8007b; refresh {refresh.py} and search {entry.py, expiry.py, trading_calendar.py}; live == built for both
(re-read live); census 0 and re-plan 0; activation legs closed; not rolled back. Base: FAIL (no file).

<criterion id="IB89-1-AC2" cell_refs="IB-pr-377"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r89/p89_cells.py" . IB89-1-AC2</invocation><expect>IB89-1-AC2 PASS</expect></criterion>
`IB89-1-AC2` -- the five-arm controlled-clock drive passes 5 of 5 against the deployed modules. Base: FAIL (no file).

<expected_criteria>IB89-1-AC1, IB89-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and nothing else.
- **The only served changes** are these two functions' code. No IAM, route, schedule, table or bucket change. Targeted applies only.
- **No read of `opal-data-*` firm buckets from dell2.** Those reads go to the laptop as files.
- **No vendor call.** No call off Opal infrastructure. No monitor, alarm, SNS or SES send.
- **Refusal clause.** A moved start sha, a census other than the signed lists, a plan touching anything else, or a failed read-back:
  STOP, file a row, apply nothing more (Branch B if already applied).
- **Row ids** are `IRPT_BCKEND-D2-S<n>` (seat rows on dell2); `surfaced_at` is the real time.
- **Commit** with your own author line via `bash .tools/safe-commit.sh`, `-F` with a message file. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-377.r61-directory-release-applied.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~DELL2/
infra/aws/terraform/investor-reporting/directory/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/CHANGELOG.md
infra/aws/lambda/ci/lambda-source-map.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 82 (round 89, workstream ~P), cell `IB-pr-377`.
<owned_cells>IB-pr-377</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB89-1-AC1, IB89-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~DELL2/IRPT_BCKEND.TO-IB-pr-377.r61-directory-release-applied.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P2`: commit hashes, built and live CodeSha256 per function, AC1 and AC2 last lines, the ledger
entry, the two laptop file paths, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- release-census at 4710b8007b (issuer, 2026-10-08 ~22:5xZ): refresh 1 member (refresh.py), search 3 members (entry.py, expiry.py, trading_calendar.py), equal to the signed lists; live CodeSha256 of both still equals the packet's "live" (cmNmYm1j.., DXuzx9jp..), so r61 is unapplied.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched (the refresh schedule is unchanged; one driven fire only).
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p89_cells.py dry-run at base 4710b8007b on dell2 2026-10-08 ~22:5xZ: IB89-1-AC1 FAIL, IB89-1-AC2 FAIL (no file); 0 control bytes.
lane: the <paths> block IS the grant; dell2 applies by its own applier (Andrew-direct msg 1756); terraform on dell2 verified (row D2-S11).
</preflight>
