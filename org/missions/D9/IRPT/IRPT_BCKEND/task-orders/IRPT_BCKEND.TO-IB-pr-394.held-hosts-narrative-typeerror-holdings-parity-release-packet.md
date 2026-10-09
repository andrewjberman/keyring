# TO IRPT_BCKEND.TO-IB-pr-394 -- the two hosts IB-pr-390 held out: irpt-narrative TypeError and irpt-holdings parity gate fixed, restaged, released as a packet (every route ONE)

<to_id>IRPT_BCKEND.TO-IB-pr-394</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~262</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>99</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msg 2690 via ~V2 msg 2691; rows D2-W201-S5, D2-W201-S6 | **Decomp cell:** `IB-pr-394` (decomposition section 92) |
**outcome_ref:** FWD-2 (IRPT_ANLREQ FWD-1 seat run: every route reads ONE) | **depends_on:** none for the code. The release follows IB-pr-383's after-read, under its own pair.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-262` (branch `wk-IRPT_BCKEND-262`, cut from `box/dell2`). Work and commit only there. Paths are
relative to the worktree. Keep scratch OUTSIDE the worktree.

**The cell (CTO msg 2690, relayed by ~V2 msg 2691).** IB-pr-390 released 6 of the 8 functions that package `infra/aws/lambda/investor-reporting/_authz/served.py`
and held two out. You fix both, restage them and package their release. IRPT_ANLREQ FWD-1's seat run starts only when every route in the SA
route census (`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.json`) reads ONE. Your worktree already
carries IB-pr-390's new `served.py` (code @74a62fb46c) and its restage of the 6 released hosts (@c2bb612234).

1. **irpt-narrative (row IRPT_BCKEND-D2-W201-S6).** The new `served.py` raises TypeError on irpt-narrative's error path against that
   function's STAGED `errors.py`, and its staged boundary is 27 `served.py` commits behind.
   - Fix at the root: restage the narrative function's members to a consistent current set, or make the error path compatible. Pick the
     smaller change that keeps every other host unchanged, and say why.
   - Add tests in `infra/aws/lambda/investor-reporting/narrative/tests/`, names containing `served_error_path`, at least 2: an internal caller and a service caller each
     get the staged `errors.py` shape, with no TypeError.
2. **irpt-holdings (row D2-W201-S5).** Its BUILD_ONLY refuses on the ADHC_DRIFTD.002 parity gate because `holdings_publication_port.py` is
   not in its `files[]`. Fix that in `infra/aws/lambda/ci/lambda-source-map.json`: add the member, owned.
3. **Restage `served.py`** in both hosts' staged rows to the IB-pr-390 code commit. A build at the REAL map must carry the change.
4. **Release packet** (BUILD_ONLY and offline replays only; nothing uploaded or applied):
   - census at your pin of both functions: built sha256, live_before, changed members with their owners;
   - BUILD_ONLY from a clean tree, built twice;
   - replay arms: each host's routes admit the right firm and refuse another, and an unrelated Opal caller is identical through the live
     and built zips; include a negative control;
   - the packet itself, modelled on IB-pr-390's: Branch A/B with rollback per function, and a per-route admitted/refused table for both
     hosts;
   - write it to `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~262/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-394.md`, with the census at
     `.../IB99-1_release_census.json` (`{pin, artifacts: [{name, built_sha256, live_before, changed_members}], build_only: {rc, tree_clean}}`).
     Keep scratch outside the worktree.

Prove each criterion by running its invocation from the worktree root.

<criterion id="IB99-1-AC1" cell_refs="IB-pr-394"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r99/p99_held_hosts.py" . IB99-1-AC1</invocation><expect>IB99-1-AC1 PASS</expect></criterion>
<criterion id="IB99-1-AC2" cell_refs="IB-pr-394"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r99/p99_held_hosts.py" . IB99-1-AC2</invocation><expect>IB99-1-AC2 PASS</expect></criterion>

<expected_criteria>IB99-1-AC1, IB99-1-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code, tests, source-map restage, BUILD_ONLY and offline replays only; no upload, apply or deploy. AWS reads only.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W262-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~262" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~262@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~262 <0.9.0_WK_IRPT_BCKEND~262@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool, outside the worktree.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/investor-reporting/narrative/
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/holdings/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-394.held-hosts-narrative-typeerror-holdings-parity-release-packet.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~262/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 92 (round 99, workstream ~P), cell `IB-pr-394`.
<owned_cells>IB-pr-394</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB99-1-AC1, IB99-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~262/IRPT_BCKEND.TO-IB-pr-394.held-hosts-narrative-typeerror-holdings-parity-release-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give what you built and where, the commit hashes, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- CTO msg 2690 via ~V2 msg 2691; rows D2-W201-S5, D2-W201-S6; code + tests only in this cell; its release follows IB-pr-383 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; any IAM is DESIRED code for the release pair.
comp-routes: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; a route, if needed, is DESIRED code for the release pair.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p99_held_hosts.py dry-run at base de49d4f7a2 on dell2 2026-10-09 ~06:4xZ: new-test criteria FAIL (0 selected), suite criteria PASS as control; 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO msg 2690); its pair is signed after the packet lands.
</preflight>
