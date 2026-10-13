# TO IRPT_BCKEND.TO-IB-pr-503 -- OFFLINE REPLAY: the packaged `irpt-holdings` serve path passes a node carrying `account_id` through unchanged (CTO round-173 analysis section 1 and section 2 item 2)

<to_id>IRPT_BCKEND.TO-IB-pr-503</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~354</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>173</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-173 ANALYSIS (msg 6798) section 1 (last row) and section 2 item 2 | **Decomp cell:** `IB-pr-503` (decomposition section 165) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-503` (inlined):** the 49 Financial builder is about to write an additive `account_id` member on each ACCOUNT node of the `HoldingsSnapshot` it lands in S3. Round 172 showed the live `irpt-holdings` function does not validate a snapshot at serve (`validate_slice` has no non-test caller). What is NOT yet shown is what its serve path DOES with a node member it has never seen: it could pass it through, drop it, or refuse the snapshot. **Replay the packaged serve path offline on synthetic data and record what happens.** OFFLINE: no AWS call, no function invocation, no sign-in, no deploy, no edit of product code, tests or the source map. Synthetic data only (no real account number, name or figure).

**Do:**
1. Assemble the function's packaged code in a scratch directory OUTSIDE the repository (a temp folder you create and name in the record): for each entry of `infra/aws/lambda/ci/lambda-source-map.json` `functions["irpt-holdings"]["staged_from"]` write `git show <pin>:<repo_path>` to `<scratch>/<packaged_as>` (check its sha256 equals the entry's `sha256`); for each name in the function's `files` that is not staged, take it from `source_dir` in your worktree (record it with `"pin": "WORKTREE"`). The packaged schema copy goes to `contracts/HoldingsSnapshot.schema.json` as packaged. This is the code the live function runs; the worktree's `holdings/snapshot.py` is NOT it (it differs from the staged pin).
2. Build a small SYNTHETIC `HoldingsSnapshot` that the packaged `snapshot.py` accepts at its pinned shape (read the packaged `load_snapshot` and `project`, `entry.holdings_snapshot`, and the existing holdings tests for how a snapshot is stubbed: a stub `s3_client` returning the JSON, a scope selecting the accounts). Use opaque synthetic ids such as `ACCT-SYN-1`. Three variants of ONE ACCOUNT node: (a) with `account_id` set to a synthetic string; (b) without the member; (c) with a member the packaged schema has never named (`unknown_member`).
3. Run the packaged serve path on each variant at the lowest level that is the real serve path (`snapshot.project(snapshot, scope, include=())` after `load_snapshot` through a stub S3, and, if it runs offline without AWS, `entry.holdings_snapshot`), and record for each: `passed_through` (the node in the served slice carries the member, value equal), `dropped` (the served node lacks it), `refused` (an exception or a refusal envelope), or `unchanged` (variant (b) only: the served node equals the node without the member, as before). Report what you observe, not what is hoped; a `dropped` or `refused` for (a) is a FINDING to record, not a failure of this order.
4. Write the replay as a script `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~354/replay_503.py` that is SELF-CONTAINED (it assembles the scratch tree itself from `git show` of the pins, runs offline, takes no argument, run from the repository root with `python -I`) and prints the record's JSON object to stdout and exits 0; and write the same object to `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~354/IB173-1_holdings_passthrough_replay.json`:
`{"packaged_members":[{"repo_path":"...","pin":"<40-hex or WORKTREE>","sha256":"..."}],"entry_used":"...","arms":[{"arm":"node_with_account_id","verdict":"passed_through"},{"arm":"node_without_account_id","verdict":"unchanged"},{"arm":"node_with_unknown_member","verdict":"..."}],"reading":"one sentence on what the serve path does with an unknown node member and why (cite file:line of the code that decides it)","functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"accounts_written":0,"figures_written":0,"vendor_requests_sent":0}`
List in `packaged_members` every member the replay imported.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB173-1-AC1" cell_refs="IB-pr-503"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r173/p173_cells.py" . IB173-1-AC1</invocation><expect>IB173-1-AC1 PASS</expect></criterion>
<criterion id="IB173-1-AC2" cell_refs="IB-pr-503"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r173/p173_cells.py" . IB173-1-AC2</invocation><expect>IB173-1-AC2 PASS</expect></criterion>
<criterion id="IB173-1-AC3" cell_refs="IB-pr-503"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r173/p173_cells.py" . IB173-1-AC3</invocation><expect>IB173-1-AC3 PASS</expect></criterion>

<expected_criteria>IB173-1-AC1, IB173-1-AC2, IB173-1-AC3</expected_criteria>

What the checks grade: AC1 exactly the three arms, each verdict from the closed set (`passed_through`, `dropped`, `refused`, `unchanged`), the node without the member reading `unchanged`, and `entry_used` and `reading` present; AC2 every member listed is a staged member of `irpt-holdings` at the source map's pin and sha256 (re-hashed from `git show`), or a `source_dir` file with pin `WORKTREE` whose sha256 matches your working tree; AC3 the six bound counters read 0, and the check RUNS your script and its arms equal the record's. Do not edit the checks. The issuer reads the replay against the code before relying on the verdict.

## BOUNDS

- **Grant:** the `paths` block and nothing else, plus a scratch directory outside the repository. No AWS call, no invocation, no deploy, no edit of product code, tests or the source map; synthetic data only.
- **Refusal clause:** STOP, file a row, change nothing more, if the packaged code cannot be run offline without an AWS call or a secret (say which import or call needs it), or a staged member's bytes do not hash to the source map's sha256.
- **Row ids** are `IRPT_BCKEND-D2-W354-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition with `.tools/safe-commit.sh`; ASCII only. Report once, under 150 words.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~354/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-503.irpt-holdings-passes-account-id-through-offline-replay.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 165 (round 173, workstream ~P), cell `IB-pr-503`.
<owned_cells>IB-pr-503</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB173-1-AC1, IB173-1-AC2, IB173-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~354/IRPT_BCKEND.TO-IB-pr-503.irpt-holdings-passes-account-id-through-offline-replay.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- an offline replay of repository code on synthetic data; no served artifact, no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p173_cells.py dry-run at base on dell2 2026-10-13 ~05:1xZ: IB173-1 AC1, AC2, AC3 FAIL (no record, no script). The source-map structure the AC2 check reads was printed: `functions["irpt-holdings"]["staged_from"]` is a list of 35 entries carrying repo_path, pin, packaged_as and sha256.
lane: the paths block IS the grant; worker slot ~354 of IRPT_BCKEND. Class LOCAL.
</preflight>
