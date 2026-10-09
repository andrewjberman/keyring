# TO IRPT_BCKEND.TO-IB-pr-406 -- 49F-only narrow holdings bundle on the post-IB-pr-404 bytes: dell1's e56 CUSIP fallback + IB-pr-403's SmartX CUSIP ids, with its release packet

<to_id>IRPT_BCKEND.TO-IB-pr-406</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~269</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>107</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_D1_S8_49F_CUSIP_PLACEMENT_20261009.md` AMENDMENT 2 @b58f09e1b8 (msg 3107), on dell1 row MDPF_SECCLASS-D1-S8 | **Decomp cell:** `IB-pr-406` (decomposition section 100) | **outcome_ref:** FWD-2

---

## WORKER FACE

**The cell.** The scheduled 49F holdings fire runs `s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz`.
dell1's SC-e-56 CUSIP fallback (commit `01e843ce2e`, in `holdings_snapshot.py`) is live only in a key no fire runs. IB-pr-403 (code
`dfa9b72cc9`) gives 49F SmartX nodes a CUSIP. This cell builds ONE 49F bundle carrying both, on the bytes IB-pr-404 lands. The other
firms are untouched.

Read first, in `C:/dev/wk-irpt-bckend-269/org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~266/`:
`NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-402.md`, `narrow_pack.py`, `extract_bundle.py`, `compose_narrow.py` and
`holdings_snapshot.narrow.py.txt`. Also read ~265's `replay/replay_publish_gate.py` in `0.9.0_WK_IRPT_BCKEND~265/`.

1. **Base = IB-pr-402's built 49F bytes** (sha256 `3f2e738f83aa415a2b56cf506d54368f9d2f86f7ded8f19202fc373ef6a28901`).
   - Rebuild it exactly as the 402 packet's landing path does: the live rollback version `3Q_W49U7kMa_xO30Q6LQE7QLsFu7ARur` plus the
     narrow member, python 3.12, LF bytes.
   - Its sha256 must equal that base, or STOP.
   - If IB-pr-404 has already landed, the live 49F object must also hash to it.
2. **holdings_snapshot.py** = the narrow member plus the diff of `01e843ce2e` to that file ONLY. The 402 packet's control shows this
   reproduces git blob `e39636c5a8`; record the sha256.
3. **holdings_49f.py** = the base's member plus the diff of `dfa9b72cc9` to that file ONLY. It must apply cleanly; a conflict is a STOP and
   a row.
4. **Repack** with every other member byte-identical to the base and SHA256SUMS regenerated, using `narrow_pack.py` under python 3.12. Pack
   twice; the outputs must be byte-identical. Upload NOTHING.
5. **Write `IB107-1_49f_bundle_census.json`**:
   `{pin, build_only:{rc,tree_clean,method}, artifacts:[{firm:"49financial", key, base_sha256, built_sha256, built_md5_expected_etag,
   built_twice_identical, changed_members:[paths], members_sha256_metadata}]}`.
6. **Replay** on real 49F inputs (AWS reads only, scratch outside the worktree, deleted file by file). Base tree vs built tree. Write
   `IB107-1_49f_bundle_replay.json` `{arms:[{name, verdict, negative_control, detail}]}` with at least:
   - `fwd14_gate_unchanged`, `identical`: the publish gate's outcome and conditions are the same on both trees;
   - `symbol_miss_cusip_fallback`, `expected-diff`: a SmartX node whose symbol misses is classified through `CUSIP:<id>` on built and
     not on base. Give the count of nodes newly classified;
   - `real_49financial_nodes`, `expected-diff`: the same node ids on both; only `security_id` (CUSIP) and classification differ. Give
     the counts;
   - one negative control (e.g. a node with no CUSIP stays as on base).
7. **Write `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-406.md`** covering:
   - the blast radius: ONE S3 key, two members;
   - the served change: how many 49F nodes newly carry a CUSIP and how many newly classify;
   - the landing path: the same as the 402 packet (digest-gated, never a mint);
   - Branch A;
   - Branch B: copy back the version IB-pr-404 lands, read at apply time;
   - the after-read.
   Name the base sha256 and the built sha256. State that the pair is ~P2's COO half, dell1 `2.0.0_SA_COO~M1`'s COO half for the e56 member
   (via MSTR), and the CTO half.

<criterion id="IB107-1-AC1" cell_refs="IB-pr-406"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r107/p107_cells.py" . IB107-1-AC1</invocation><expect>IB107-1-AC1 PASS</expect></criterion>
<criterion id="IB107-1-AC2" cell_refs="IB-pr-406"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r107/p107_cells.py" . IB107-1-AC2</invocation><expect>IB107-1-AC2 PASS</expect></criterion>
<criterion id="IB107-1-AC3" cell_refs="IB-pr-406"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r107/p107_cells.py" . IB107-1-AC3</invocation><expect>IB107-1-AC3 PASS</expect></criterion>

<expected_criteria>IB107-1-AC1, IB107-1-AC2, IB107-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. BUILD_ONLY and offline replays only; no upload, apply or deploy. AWS reads only.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Client data:** extracted trees and node files stay OUTSIDE the worktree and are deleted at the end (file-by-file, never a recursive delete; report what remains).
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W269-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~269" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~269@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~269 <0.9.0_WK_IRPT_BCKEND~269@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~269/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-406.49f-e56-cusip-narrow-bundle.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 100 (round 107, workstream ~P), cell `IB-pr-406`.
<owned_cells>IB-pr-406</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB107-1-AC1, IB107-1-AC2, IB107-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~269/IRPT_BCKEND.TO-IB-pr-406.49f-e56-cusip-narrow-bundle.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the base and built sha256, the changed members, the replay verdicts and counts, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- ONE S3 key (49financial holdings bundle), two members (holdings_snapshot.py + 01e843ce2e; holdings_49f.py + dfa9b72cc9) on IB-pr-402's built 49F bytes; inflection and cottonwood keys untouched; nothing uploaded by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p107_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~10:3xZ: AC1-AC3 FAIL (no census, replay or packet); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO ruling D1-S8 AMENDMENT 2).
</preflight>
