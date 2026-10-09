# TO IRPT_BCKEND.TO-IB-pr-400 -- FWD-14 release packet: the runner bundle carrying the holdings publish gate (IB-pr-393 + IB-pr-396)

<to_id>IRPT_BCKEND.TO-IB-pr-400</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~265</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>102</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msgs 2655, 2738 and 2748 (cut the release pair once v0.33 is admitted; CVO msg 2744) | **Decomp cell:** `IB-pr-400` (decomposition section 95) | **outcome_ref:** FWD-14 (S392 retires after the deploy and its first scheduled fire)

---

## WORKER FACE

**The release:** FWD-14's gate in `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (IB-pr-393 @42793c81fc + IB-pr-396 v0.33 @5eeef73870)
ships in the runner bundle `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`. Its
live version is W2Wragr (sha256 f6d48603), from IB-pr-389's ratified runner. Model the packet on
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~200/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-389.md`.
1. **Census of the bundle at your pin:** members changed versus live, each owned (expect holdings_snapshot.py), plus any
   other member that moved since W2Wragr. Name each and its owner, and flag any non-FWD-14 change.
2. **BUILD_ONLY** with the mint's deterministic builder, twice, from a clean tree.
3. **Replay arms:**
   - the real holdings inputs at all 3 firms through live versus built: identical publication when nothing is WORSE;
   - the QA worse/restored pair: REFUSED, then PUBLISHED;
   - an all-UNKNOWN firm losing an account: PUBLISHED and listed;
   - a negative control.
4. **IAM read:** does the holdings writer's role already cover `put_object` on the refusal record path
   (`.../platinum/holdings/current/publish_refusal.json`)? Read it, never assume. A missing grant is a row and part of the
   packet's step list.
5. **Packet** with Branch A/B. Rollback copies W2Wragr back over the key; never roll back through a WORSE window. The
   after-read is the first scheduled fire per firm: PUBLISHED or REFUSED, with the record. Note that S392 retires then.
Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~265/IB102-4_release_census.json`, `IB102-4_release_replay.json` and
`NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-400.md`.

<criterion id="IB102-4-AC1" cell_refs="IB-pr-400"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r102/p102_cells.py" . IB102-4-AC1</invocation><expect>IB102-4-AC1 PASS</expect></criterion>

<expected_criteria>IB102-4-AC1</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code, tests, source-map restage, BUILD_ONLY and offline replays only; no upload, apply or
  deploy. AWS reads only.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W265-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~265" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~265@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~265 <0.9.0_WK_IRPT_BCKEND~265@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~265/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-400.fwd14-publish-gate-release-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 95 (round 102, workstream ~P), cell `IB-pr-400`.
<owned_cells>IB-pr-400</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB102-4-AC1. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~265/IRPT_BCKEND.TO-IB-pr-400.fwd14-publish-gate-release-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the pin, the bundle built sha256 and live_before, changed members with owners, the IAM finding, the replay verdicts, the commit hashes, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the runner bundle only; holdings_snapshot.py's publish step changes (FWD-14 gate); live W2Wragr (ratified).
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes no permission; it READS one role (the holdings writer's) for put_object on the refusal-record path and reports a missing grant as a row and a packet step.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p102_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~07:2xZ: AC1 FAIL (no census); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (FWD-14 folded into ~P, PRD v0.31-v0.33).
</preflight>
