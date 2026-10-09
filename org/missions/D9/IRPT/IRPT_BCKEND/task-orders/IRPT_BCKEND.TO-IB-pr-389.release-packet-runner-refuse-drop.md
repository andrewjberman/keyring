# TO IRPT_BCKEND.TO-IB-pr-389 -- release packet for IB-pr-384 (runner bundle): census, BUILD_ONLY, replay, Branch A/B

<to_id>IRPT_BCKEND.TO-IB-pr-389</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~200</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>97</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msg 2507 (b) | **Decomp cell:** `IB-pr-389` (decomposition section 90) |
**outcome_ref:** FWD-7 | **depends_on:** the drained code cells named below. Nothing here is applied; the pairs are signed after IB-pr-383 closes.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-200` (branch `wk-IRPT_BCKEND-200`, cut from `box/dell2`). Work and commit only there. Paths are
relative to the worktree. Keep scratch OUTSIDE the worktree.

**The cell: release packet for IB-pr-384** (the runner refuses a build that drops a source entry; drained @1895f16a0b). The artifact
is the runner bundle `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz` (live today: version
OxaIJns0, from IB-pr-383). Build it with the mint's deterministic builder, as in the IB-pr-381 packet.
- **Replay arms:**
  - the real inflection and cottonwood inputs through the live and built bundles: identical landings while nothing is dropped;
  - a fixture that drops an entry the source still holds: the built bundle refuses with 0 puts; the live bundle lands it;
  - a negative control.
- **The after-read** is the next scheduled landing at all 3 firms, read as landed.

BUILD_ONLY and offline replays only: nothing is uploaded or applied. The pair is signed after IB-pr-383 closes (CTO msg 2507).

1. **Census at the pin.** The pin is box/dell2 HEAD as your worktree has it. Run `python infra/aws/lambda/ci/release-census.py <function> --pin <pin>`
   for every function the code reaches, plus the bundle builder for a bundle. Every changed member must be owned by its cell's commit.
2. **BUILD_ONLY from a clean tree** (porcelain empty first; `BUILD_ONLY=1` only; clean the residue after). Build twice and confirm
   byte-identical output.
3. **Census file** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~200/IB97-2_release_census.json`:
   `{pin, artifacts: [{name, built_sha256, live_before, changed_members: [{member, owner_commit}]}], build_only: {rc, tree_clean}}`.
   `live_before` is read live: the CodeSha256, or the bundle's version id.
4. **Replay** (offline, live versus built artifacts, real or fixture inputs as named below) into
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~200/IB97-2_release_replay.json` as
   `{arms: [{name, verdict: identical|expected-diff, negative_control: bool, detail}]}`, with at least one negative control.
   Raw extracts stay in scratch OUTSIDE the worktree and are deleted after.
5. **Packet** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~200/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-389.md`, modelled on
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~189/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-380_381.md`. It must contain:
   - the pin;
   - every artifact's built sha256 and live_before;
   - the writers of each changed property;
   - Branch A and Branch B, each with rollback per artifact;
   - the replay arm for the applier;
   - the after-read.

Prove each criterion by running its invocation from the worktree root.

<criterion id="IB97-2-AC1" cell_refs="IB-pr-389"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r97/p97_release.py" . IB97-2-AC1</invocation><expect>IB97-2-AC1 PASS</expect></criterion>
<criterion id="IB97-2-AC2" cell_refs="IB-pr-389"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r97/p97_release.py" . IB97-2-AC2</invocation><expect>IB97-2-AC2 PASS</expect></criterion>

<expected_criteria>IB97-2-AC1, IB97-2-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No upload, apply or deploy; BUILD_ONLY and offline replays only. AWS reads only.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W200-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~200" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~200@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~200 <0.9.0_WK_IRPT_BCKEND~200@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool, outside the worktree.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-389.release-packet-runner-refuse-drop.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~200/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 90 (round 97, workstream ~P), cell `IB-pr-389`.
<owned_cells>IB-pr-389</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB97-2-AC1, IB97-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~200/IRPT_BCKEND.TO-IB-pr-389.release-packet-runner-refuse-drop.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give what you built and where, the commit hashes, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- CTO msg 2507 (b); code + tests only in this cell; its release follows IB-pr-383 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; any IAM is DESIRED code for the release pair.
comp-routes: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; a route, if needed, is DESIRED code for the release pair.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p97_release.py dry-run at base 6dea768ce8 on dell2 2026-10-09 ~05:0xZ: new-test criteria FAIL (0 selected), suite criteria PASS as control; 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO msg 2507); release pairs signed after IB-pr-383 closes.
</preflight>
