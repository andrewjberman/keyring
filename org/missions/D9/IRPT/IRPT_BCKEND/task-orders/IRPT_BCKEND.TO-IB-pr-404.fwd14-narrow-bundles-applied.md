# TO IRPT_BCKEND.TO-IB-pr-404 -- IB-pr-402's three NARROW per-firm holdings bundles (FWD-14 publish gate) landed on lane ~IB2

<to_id>IRPT_BCKEND.TO-IB-pr-404</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>105</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the pair: packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~266/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-402.md` (blob 4f134ade55); COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_402_FWD14_NARROW_BUNDLES_COO_HALF.md` @a9d5043ef9; CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_402_FWD14_NARROW_BUNDLES_CTO_HALF.md` @c4df78131d (msg 3017) | **Decomp cell:** `IB-pr-404` (decomposition section 98) | **outcome_ref:** FWD-14

---

## WORKER FACE

**Sequence on this lane:** run this order after IB-pr-397 and BEFORE IB-pr-401. The CTO half binds the timing: all three keys land before
the 14:15Z fire on 2026-10-09, or the landed ones roll back. If steps 1-6 cannot finish before 14:00Z, start after that fire and land
all three before the next one; never straddle a fire.

Follow the packet's **landing path, steps 0-6**, exactly. It is the whole procedure; this face adds only the conditions of the two halves.
1. **Ledger:** open it and COMMIT the open before the first upload, and commit each leg as it closes (CTO condition), so no seat's drain is blocked. It names the three keys, pin `6f7ca4840e`,
   the three built sha256 and the pulling family (`irpt-holdings-refresh-lambda`, 3 firms).
2. **Precheck, per firm:** VersionId == the rollback version and ETag == the live ETag in the packet table. Anything else is a STOP.
3. **Rebuild under python 3.12** from the live version plus the committed narrow member. Read the member with
   `git show <commit>:org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~266/holdings_snapshot.narrow.py.txt`; its
   sha256 must be `dfa017b824c1aba5c1107e53ef4811edaba93b2b7903c140208e41ab8866262a`. Never use python 3.14 or a CRLF checkout (row W266-S1).
4. **Digest gate (absolute):** sha256 AND md5 of each `out.tar.gz` equal the packet table, or STOP and file a row. Never upload a
   different byte set, and never fall back to `--mint-bundle`. A refused direct put is a STOP and a row.
5. **Upload one firm at a time** with the packet's metadata. Read back ETag, metadata and the get-object sha256. Land all three before the
   next fire (`irpt-holdings-snapshot`, 10:15 America/New_York, MON-FRI), or roll the landed ones back (Branch B).
6. **Re-run the replay on the uploaded bytes** before the first fire (packet: "Rerun against the uploaded bytes"). A `real_` arm that is
   not identical, or a worse arm that does not REFUSE, is a STOP and Branch B.
7. **After the first scheduled fire after landing,** read each firm's output line and refusal record, never the SSM status. Then close the
   ledger and write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB105-1_narrow_bundles_after_reads.json`:
   `{ledger:{state,pin,sha256:[3]}, rolled_back, uploaded_version_ids:{firm:id}, replay_on_uploaded:[{name,verdict,negative_control}],
   first_fire:{firm:{outcome, output_line, refused_at, fire_after_landing}}}`.

Branch B, per firm: the packet's `copy-object` from the rollback version, then re-read ETag and metadata. **Never roll back through a
WORSE window** (a `publish_refusal.json` newer than the last index move means that firm stays).

<criterion id="IB105-1-AC1" cell_refs="IB-pr-404"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r105/p105_cells.py" . IB105-1-AC1</invocation><expect>IB105-1-AC1 PASS</expect></criterion>
<criterion id="IB105-1-AC2" cell_refs="IB-pr-404"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r105/p105_cells.py" . IB105-1-AC2</invocation><expect>IB105-1-AC2 PASS</expect></criterion>
<criterion id="IB105-1-AC3" cell_refs="IB-pr-404"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r105/p105_cells.py" . IB105-1-AC3</invocation><expect>IB105-1-AC3 PASS</expect></criterion>

<expected_criteria>IB105-1-AC1, IB105-1-AC2, IB105-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block below and nothing else. Touch only the three bundle keys (and, through the producer, its own refusal record).
  No IAM, route, schedule, env, Terraform or Lambda change. The ordered key `investor-reporting.tar.gz` is NOT touched.
- **No vendor call**, no monitor, alarm, SNS or SES.
- **Client data:** replay scratch stays OUTSIDE every worktree and is deleted file by file at the end.
- **Refusal clause:** STOP, file a row, and apply nothing more (Branch B for any landed firm) on any of these:
  - a moved live version;
  - a digest miss;
  - a refused put;
  - a failed read-back;
  - a failed replay arm.
- **Row ids** are `IRPT_BCKEND-D2-S<n>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** your own author line via `bash .tools/safe-commit.sh -F <msgfile>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-404.fwd14-narrow-bundles-applied.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 98 (round 105, workstream ~P), cell `IB-pr-404`.
<owned_cells>IB-pr-404</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB105-1-AC1, IB105-1-AC2, IB105-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-404.fwd14-narrow-bundles-applied.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** report twice. After landing: per firm, the uploaded version id, ETag and sha256, plus the replay verdicts. After the first fire:
each firm's outcome line, the ledger close, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- three S3 bundle keys, one member each (holdings_snapshot.py = live + 9af6811b61 + ce6e2a218e); served index identical on real inputs at 3 firms; ordered key untouched.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the holdings roles already allow the refusal-record put (~265's policy read).
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the existing irpt-holdings-snapshot fire runs the new bundle.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p105_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~09:4xZ: AC1 FAIL (49financial ETag 7a400c14 == live_before), AC2 and AC3 FAIL (no after-reads); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; applied by 0.7.0_AE_CloudOps~IB2 (MSTR msg 2725), IRPT_BCKEND only.
</preflight>
