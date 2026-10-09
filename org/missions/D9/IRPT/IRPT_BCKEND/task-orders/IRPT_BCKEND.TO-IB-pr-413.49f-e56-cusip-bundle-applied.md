# TO IRPT_BCKEND.TO-IB-pr-413 -- IB-pr-410's 49F-only narrow holdings bundle (dell1's e56 + IB-pr-403 with ticker kept) landed on lane ~IB2

<to_id>IRPT_BCKEND.TO-IB-pr-413</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>114</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the pair: packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~273/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-410.md` (blob 92994b0980); COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_410_49F_E56_CUSIP_BUNDLE_COO_HALF.md` @ec2d6b6f68; CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_410_49F_E56_CUSIP_BUNDLE_CTO_HALF.md` @56bc28957c; dell1 `2.0.0_SA_COO~M1`'s half on the e56 member (asked via MSTR~DELL2) | **Decomp cell:** `IB-pr-413` (decomposition section 107) | **outcome_ref:** FWD-2

---

## WORKER FACE

**Two start gates, both measured, never assumed:**
1. dell1 `2.0.0_SA_COO~M1`'s half on the e56 member is filed. The issuer sends its path by amendment; until then, STOP before any upload.
2. IB-pr-404's ledger `irpt-fwd14-narrow-holdings-bundles-20261009` is CLOSED after its L6 fire read, so the 49F key is not changed
   inside 404's window.

Then follow the packet's **landing path, steps 0-6**, for ONE key: `s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz`.
- **Ledger:** open it and COMMIT the open before the upload. Commit each leg as it closes. It states pin `9b7256a99f`, built sha256
  `47be54d6479fdb849477a41b7cffa089319f2f18d38069b3384393fec192dda5`, and the pulling family (`irpt-holdings-refresh-lambda`, 49financial).
- **Precheck:** the ETag reads `01387cef54b9e15e10023f05029e357d`, the IB-pr-404 bytes. Record the VersionId as the rollback version.
  Anything else is a STOP.
- **Rebuild under python 3.12 and LF:** base = the live version; members as the packet states. The digest gate is absolute: sha256
  `47be54d6...dda5` and md5 `1e8ff3096af151f91b96c4e8a3712e4a`. Never upload other bytes, and never fall back to `--mint-bundle`.
- **Upload** with metadata `members-sha256=96925f389381e64beeeb31ebf61eecdd5335fddf30cce0335300b455979bfd62,member-count=44`. Read back
  ETag, metadata and the get-object sha256.
- **Re-run the replay on the uploaded bytes** before the next fire. `fwd14_gate_unchanged` and `smartx_class_parity` must read identical,
  or STOP and Branch B.
- **After the first scheduled fire after landing:**
  - read the output line and the refusal record, never the SSM status;
  - record its wall time and the prior fire's (row W269-S2). A timed-out fire is a STOP and Branch B.
  - Then close the ledger and write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB114-1_49f_bundle_after_reads.json`:
    `{ledger:{state,pin,sha256}, rolled_back, uploaded_version_id, replay_on_uploaded:[{name,verdict}], first_fire:{outcome, output_line,
    refused_at, fire_after_landing, wall_time_s, prior_wall_time_s}}`.

Branch B: `copy-object` from the recorded rollback version, then re-read ETag and metadata. Never roll back through a WORSE window.

<criterion id="IB114-1-AC1" cell_refs="IB-pr-413"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r114/p114_cells.py" . IB114-1-AC1</invocation><expect>IB114-1-AC1 PASS</expect></criterion>
<criterion id="IB114-1-AC2" cell_refs="IB-pr-413"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r114/p114_cells.py" . IB114-1-AC2</invocation><expect>IB114-1-AC2 PASS</expect></criterion>
<criterion id="IB114-1-AC3" cell_refs="IB-pr-413"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r114/p114_cells.py" . IB114-1-AC3</invocation><expect>IB114-1-AC3 PASS</expect></criterion>

<expected_criteria>IB114-1-AC1, IB114-1-AC2, IB114-1-AC3</expected_criteria>

## AMENDMENT 1 (2026-10-09 ~14:1xZ, issuer 2.0.0_SA_COO~P2): start gate 1 MET -- dell1 ~M1's half is signed

dell1 `2.0.0_SA_COO~M1`'s COO half on the e56 member is SIGNED: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_COO_HALF_SECCLASS_E56_49F_IB410_20261009.md`
@0d1b55e332 (origin box/dell1 eed6b7b743; relayed by MSTR~DELL2 msg 3436). ~M1 verified the e56 diff and member blob `e39636c5a8`
against the packet. Its conditions add to the order's:
- the digest gate;
- the after-read counts the custody e56 arm, expected 32 newly classified and 0 lost; record `e56_arm:{newly_classified, lost}` in
  `first_fire`;
- SECCLASS e56 acceptance 1 closes on that read.
Start gate 2 (IB-pr-404's ledger CLOSED after its L6 fire read) still applies.

Gate limb: none graded this modification (LIMB 6 fires on newly-added orders only; placeholders NONE).

## AMENDMENT 2 (2026-10-09 ~14:4xZ, issuer 2.0.0_SA_COO~P2, on CTO ADDENDUM 19.1): HELD

The 49financial producer was SIGKILLed on IB-pr-404's first fire (row D2-S56). This order lands more work on the same firm (the e56 lookups,
row W269-S2), so it is HELD until IB-pr-414's memory fix is signed. Its bundle is then rebuilt with the fixed `holdings_snapshot.py`
member under a new packet and pair, and this order is re-pointed by amendment.

Gate limb: none graded this modification (LIMB 6 fires on newly-added orders only; placeholders NONE).

## AMENDMENT 3 (2026-10-09 ~18:0xZ, issuer 2.0.0_SA_COO~P2, on CTO ADDENDUM 20): RE-POINTED to IB-pr-417's bundle; still HELD for its pair

IB-pr-414's memory fix is graded and IB-pr-417 has built the bundle it carries. This order now applies **IB-pr-417's artifact, not
IB-pr-410's**:
- **Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~279/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-417.md`, blob `36621e44cb`.
- **Built:** sha256 `fe4000cbd31aaee971793854ad6cf26bc7b2d9a37a484e953896a09084f02f2e`, md5 `8b482c8db26c2e913aeee72023bacc7e`.
  Follow the packet's landing path steps 0-5 exactly; the digest gate is absolute.
- **Start gate:** all three halves signed at blob `36621e44cb`: ~P2's COO half
  (`deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_417_49F_BUNDLE_MEMORY_FIX_COO_HALF.md`), dell1 `2.0.0_SA_COO~M1`'s COO half, and the
  CTO half. The ~M1 half on IB-pr-410 does NOT carry over.
- **Window:** apply before Monday 2026-10-12 13:00Z, so the 14:15Z fire runs these bytes. Not landed by then: IB-pr-404 AMENDMENT 2's
  Branch B runs on the 49F key instead.
- **Branch B (the COO half's condition):** on a REFUSED, SIGKILLed or timed-out first fire, copy back the PRE-404 version
  `3Q_W49U7kMa_xO30Q6LQE7QLsFu7ARur`, never the 404 version.
- **After-read:** the output line, the refusal record, the wall time and the absence of rc 137 on that fire.

Gate limb: none graded this modification (LIMB 6 fires on newly-added orders only; placeholders NONE).

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Touch only the 49financial bundle key (and, through the producer, its own refusal
  record). The inflection and cottonwood keys and the ordered key are NOT touched. No IAM, route, schedule, env, Terraform or Lambda change.
- **No vendor call**, no monitor, alarm, SNS or SES.
- **Client data:** replay scratch stays OUTSIDE every worktree and is deleted file by file.
- **Refusal clause:** STOP, file a row, and apply nothing more (Branch B if landed) on any of these:
  - a gate not met;
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
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-413.49f-e56-cusip-bundle-applied.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 107 (round 114, workstream ~P), cell `IB-pr-413`.
<owned_cells>IB-pr-413</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB114-1-AC1, IB114-1-AC2, IB114-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-413.49f-e56-cusip-bundle-applied.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** report twice. After landing: the uploaded version id, ETag and sha256, and the replay verdicts. After the first fire: the
outcome line, the wall times, the ledger close, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- ONE S3 key (49financial holdings bundle), two members (holdings_snapshot.py + 01e843ce2e; holdings_49f.py + IB-pr-403 + IB-pr-410), on IB-pr-404's landed bytes; FWD-14 gate PUBLISHES on both trees; 0 SmartX class lost.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the existing holdings fire runs the new bundle.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p114_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~14:1xZ: AC1 FAIL (49F ETag == 404 bytes), AC2 + AC3 FAIL (no after-reads); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; applied by 0.7.0_AE_CloudOps~IB2 (MSTR msg 2725), IRPT_BCKEND only.
</preflight>
