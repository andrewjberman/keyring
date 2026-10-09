# TO IRPT_BCKEND.TO-IB-pr-390 -- release packet for IB-pr-385 + IB-pr-387 (_authz served.py hosts): census, BUILD_ONLY, replay, Branch A/B

<to_id>IRPT_BCKEND.TO-IB-pr-390</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~201</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>97</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msg 2507 (b) | **Decomp cell:** `IB-pr-390` (decomposition section 90) |
**outcome_ref:** FWD-2 / FWD-8 | **depends_on:** the drained code cells named below. Nothing here is applied; the pairs are signed after IB-pr-383 closes.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-201` (branch `wk-IRPT_BCKEND-201`, cut from `box/dell2`). Work and commit only there. Paths are
relative to the worktree. Keep scratch OUTSIDE the worktree.

**The cell: release packet for IB-pr-385 + IB-pr-387** (both edit `infra/aws/lambda/investor-reporting/_authz/served.py`;
drained @dd02e66933 and @da8abeb411). Census every function that packages `_authz/served.py` (expect irpt-export-render and
irpt-ycharts-generate among them; name them all).
- **Replay arms:**
  - `svc-custody-statement` admitted on custody-report-persist with a cottonwood claim through the built zip, and refused through the
    live zip;
  - an internal caller with a profile row `[cottonwood]` selecting inflection: refused through the built zip, admitted through the live
    zip;
  - an unrelated Opal caller with no row: identical through both;
  - a negative control.
- Also prove, from the built zip, that `lib/opal_naming.py` `lookup()` resolves cottonwood (row D2-S26).
- **The after-read:** one live `svc-custody-statement` persist refusal-or-admission read, and one internal caller's narrowed read.

BUILD_ONLY and offline replays only: nothing is uploaded or applied. The pair is signed after IB-pr-383 closes (CTO msg 2507).

1. **Census at the pin.** The pin is box/dell2 HEAD as your worktree has it. Run `python infra/aws/lambda/ci/release-census.py <function> --pin <pin>`
   for every function the code reaches, plus the bundle builder for a bundle. Every changed member must be owned by its cell's commit.
2. **BUILD_ONLY from a clean tree** (porcelain empty first; `BUILD_ONLY=1` only; clean the residue after). Build twice and confirm
   byte-identical output.
3. **Census file** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~201/IB97-3_release_census.json`:
   `{pin, artifacts: [{name, built_sha256, live_before, changed_members: [{member, owner_commit}]}], build_only: {rc, tree_clean}}`.
   `live_before` is read live: the CodeSha256, or the bundle's version id.
4. **Replay** (offline, live versus built artifacts, real or fixture inputs as named below) into
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~201/IB97-3_release_replay.json` as
   `{arms: [{name, verdict: identical|expected-diff, negative_control: bool, detail}]}`, with at least one negative control.
   Raw extracts stay in scratch OUTSIDE the worktree and are deleted after.
5. **Packet** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~201/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-390.md`, modelled on
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~189/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-380_381.md`. It must contain:
   - the pin;
   - every artifact's built sha256 and live_before;
   - the writers of each changed property;
   - Branch A and Branch B, each with rollback per artifact;
   - the replay arm for the applier;
   - the after-read.

Prove each criterion by running its invocation from the worktree root.

<criterion id="IB97-3-AC1" cell_refs="IB-pr-390"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r97/p97_release.py" . IB97-3-AC1</invocation><expect>IB97-3-AC1 PASS</expect></criterion>
<criterion id="IB97-3-AC2" cell_refs="IB-pr-390"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r97/p97_release.py" . IB97-3-AC2</invocation><expect>IB97-3-AC2 PASS</expect></criterion>

<expected_criteria>IB97-3-AC1, IB97-3-AC2</expected_criteria>

## AMENDMENT 1 (2026-10-09 ~06:2xZ, issuer 2.0.0_SA_COO~P2): ALL never admits; restage in-cell; 6 of 8 hosts released now

The rulings behind this amendment:
- Andrew-direct, relayed by ~V2 msg 2536: release 385+387 now, standalone.
- CTO msg 2539: one packet for 385+387.
- CTO msg 2569, on CVO 2565: a lone "ALL" fails closed at served.py; fix routes.json's stale denominator.

The worker's rows D2-W201-S1, S3, S4, S5 and S6 are ruled as follows.

1. **Code before the pin (rows S1 and S3).** Commit `amendment1_ALL_never_admits.patch`. A profile allowedFirmIds equal to the string
   "ALL", or a list holding "ALL", is refused FIRM_BINDING at the internal narrowing step. Add tests named `allowed_firm_ids` for both
   forms. `test_served_refuses_all` asserts FIRM_BINDING. The test
   `test_svc_custody_statement.py::test_svc_custody_statement_does_not_change_opal_or_dev_admission` gives its Opal caller an "ALL" row
   and expects any-firm access; re-point that fixture to a caller with NO profile row (unchanged behaviour), and add one assertion that an
   "ALL" row is refused. This tightens the suite only. The `_authz` suite passes whole.
2. **Restage in-cell (row S4).** Commit the restage of `infra/aws/lambda/ci/lambda-source-map.json`, so that `served.py`'s staged rows
   for the RELEASED functions pin the new code commit. A build at the real map must then carry the change; no candidate map. The
   applier does not restage.
3. **Hosts released now: 6 of 8.** irpt-49f-reporting-read-lambda, irpt-directory-search, irpt-export-render, irpt-performance-adapter,
   irpt-status and irpt-ycharts-generate.
   - **Held out:** irpt-holdings (row S5: its parity gate refuses BUILD_ONLY at the real map) and irpt-narrative (row S6: the new
     served.py raises TypeError against its staged errors.py). Their source-map rows are NOT restaged.
   - The packet lists every route each held-out host serves as NOT YET NARROWED, and names the follow-up cell.
4. **Stale denominator (row S2).** Fix it in `docs/contracts/investor-reporting/v1/routes.json`, the file that carries it: write
   declared 21, routed_elsewhere 2, total 23. Change no route.
5. **Then re-run** `replay/make_census.py`, `replay/run_replay.py` and `replay/make_packet.py` at the new pin, and flip the order to
   complete.

Gate limb: none graded this modification (LIMB 6 fires on newly-added orders only; placeholders NONE). This order's `<paths>` are widened
to the files named above.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No upload, apply or deploy; BUILD_ONLY and offline replays only. AWS reads only.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W201-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~201" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~201@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~201 <0.9.0_WK_IRPT_BCKEND~201@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool, outside the worktree.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_authz/tests/test_allowed_firm_ids.py
infra/aws/lambda/investor-reporting/_authz/tests/test_served_on_behalf_create.py
infra/aws/lambda/investor-reporting/_authz/tests/test_svc_custody_statement.py
infra/aws/lambda/ci/lambda-source-map.json
docs/contracts/investor-reporting/v1/routes.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-390.release-packet-authz-served.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~201/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 90 (round 97, workstream ~P), cell `IB-pr-390`.
<owned_cells>IB-pr-390</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB97-3-AC1, IB97-3-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~201/IRPT_BCKEND.TO-IB-pr-390.release-packet-authz-served.proof_of_spec.json`.
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
