# TO IRPT_BCKEND.TO-IB-pr-402 -- FWD-14 NARROW per-firm holdings bundles: each live bundle with ONLY holdings_snapshot.py moved by the FWD-14 commits, and its release packet

<to_id>IRPT_BCKEND.TO-IB-pr-402</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~266</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>103</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** row `IRPT_BCKEND-D2-W265-S1` and its disposition `IRPT_BCKEND-D2-S37` (issuer ruling inside its decomposition) | **Decomp cell:** `IB-pr-402` (decomposition section 96) | **outcome_ref:** FWD-14

---

## WORKER FACE

**The cell.** IB-pr-400 (worker ~265, drained @dda85dc8f4) found that the scheduled holdings producer `irpt-holdings-refresh-lambda`
does NOT run `investor-reporting.tar.gz`. It runs three per-firm bundles:
`s3://opal-data-<firm>/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz` for 49financial, inflection and cottonwood.
A fresh build of those bundles from HEAD moves 18 of 44 members, and 17 of them are not FWD-14. So the release is NARROW: each firm's
live bundle, unchanged, except `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`.

Read first: `C:/dev/wk-irpt-bckend-266/org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~265/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-400.md`
and its `IB102-4_release_census.json` and `IB102-4_release_replay.json` (the replay script is in `replay/`).

1. **Read each firm's live bundle** with `s3api get-object --version-id`, at these versions (a different current version is a STOP):
   49financial `3Q_W49U7kMa_xO30Q6LQE7QLsFu7ARur`, inflection `SuRm8tIYq9AKTbRD91SxTJp2Fh80CqCo`, cottonwood `NZIQjid2En9Wbe8kM8ibfsIjxjDWKEoT`.
   Extract each into its own new, empty directory OUTSIDE the worktree.
2. **Make the narrow holdings_snapshot.py per firm:** the live member's bytes plus the diffs of `9af6811b61` and `ce6e2a218e` to that
   file ONLY. The patch must apply cleanly; a conflict is a STOP and a row. Do NOT bring in `01e843ce2e` (MDPF_SECCLASS e62) or any
   other commit. Record the base: the commit whose blob equals the live member (`base_commit`), or `none-in-history` with the live
   member's sha256.
3. **Repack each bundle** with every other member byte-identical to live and SHA256SUMS regenerated. Use the packer the mint uses
   (`.tools/safe_deploy_core.py`) if it can take a member set. If not, write the minimum deterministic packer in your deliverables
   folder. Pack twice; the two outputs must be byte-identical. Upload NOTHING.
4. **Write `IB103-2_narrow_bundle_census.json`** in your deliverables folder:
   `{base_commit, pin, build_only:{rc,tree_clean,method}, artifacts:[{firm, key, live_before, built_sha256, built_md5_expected_etag, built_twice_identical, changed_members:[paths]}]}`.
5. **Replay it.** Reuse ~265's replay script against the live and narrow trees and write `IB103-2_narrow_bundle_replay.json` with
   `arms:[{name, verdict, negative_control}]`. Per firm it carries:
   - `real_<firm>_live_vs_built` on real inputs. It must be `identical` (FWD-14 only: same nodes, gate PUBLISHED; `as_of_timestamp`
     excused);
   - `fx_<firm>_worse_restored` (QA pair: REFUSED, then PUBLISHED). It reads `expected-diff`;
   - the all-UNKNOWN arm and at least one negative control.
6. **Write `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-402.md`** with these sections:
   - the blast radius: three S3 keys, one member each;
   - the landing path that ships exactly these bytes, which is NOT a mint from the tree, since that ships the 17 members;
   - Branch A;
   - Branch B: copy each `live_before` version back, and re-read the ETag;
   - the after-read: a refused fire exits 0, so read the output line and the refusal record, not the SSM status.
   Name `base_commit`, each built sha256 and each rollback version id.

<criterion id="IB103-2-AC1" cell_refs="IB-pr-402"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r103/p103_cells.py" . IB103-2-AC1</invocation><expect>IB103-2-AC1 PASS</expect></criterion>
<criterion id="IB103-2-AC2" cell_refs="IB-pr-402"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r103/p103_cells.py" . IB103-2-AC2</invocation><expect>IB103-2-AC2 PASS</expect></criterion>
<criterion id="IB103-2-AC3" cell_refs="IB-pr-402"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r103/p103_cells.py" . IB103-2-AC3</invocation><expect>IB103-2-AC3 PASS</expect></criterion>

<expected_criteria>IB103-2-AC1, IB103-2-AC2, IB103-2-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. BUILD_ONLY and offline replays only; no upload, apply or deploy. AWS reads only.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Client data:** extracted trees and node files stay OUTSIDE the worktree and are deleted at the end (file-by-file, never a recursive delete; report what remains).
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W266-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~266" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~266@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~266 <0.9.0_WK_IRPT_BCKEND~266@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~266/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-402.fwd14-narrow-per-firm-holdings-bundles.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 96 (round 103, workstream ~P), cell `IB-pr-402`.
<owned_cells>IB-pr-402</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB103-2-AC1, IB103-2-AC2, IB103-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~266/IRPT_BCKEND.TO-IB-pr-402.fwd14-narrow-per-firm-holdings-bundles.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the base commit, each firm's built sha256 and changed members, the replay verdicts, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- three per-firm S3 bundle keys, one member each (holdings_snapshot.py, FWD-14 commits only); the ordered investor-reporting.tar.gz is out of the release (no scheduled fire runs it; row W265-S1); nothing uploaded by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; ~265 read the three holdings roles' policy text: PutObject on platinum/holdings/* covers the refusal record.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p103_cells.py dry-run at base box/dell2 @79dec5414e on dell2 2026-10-09 ~08:5xZ: AC1-AC3 FAIL (no census, replay or packet); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (FWD-14 folded into ~P, PRD v0.31-v0.33).
</preflight>
