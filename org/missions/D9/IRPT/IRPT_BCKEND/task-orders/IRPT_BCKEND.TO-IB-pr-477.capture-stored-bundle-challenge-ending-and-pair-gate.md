# TO IRPT_BCKEND.TO-IB-pr-477 -- BUILD ONLY: a challenged stored-bundle probe ends the capture without a fresh sign-in, and the probe pair runs on the first probe that holds a token

<to_id>IRPT_BCKEND.TO-IB-pr-477</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~332</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>166</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6503 (CTO ROUND-166 ANALYSIS section 2 rows D2-W328-S1 and D2-W328-S2, section 3 item 3); issuer row IRPT_BCKEND-D2-S109 | **Decomp cell:** `IB-pr-477` (decomposition section 158) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-332/` (bash `/c/dev/wk-irpt-bckend-332`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it).

**HARD BOUNDS.** BUILD ONLY. No AWS call. No request to the vendor, no sign-in, no run of the session runner against anything but the repo's own offline replay under the netguard preload. Nothing is deployed, uploaded or installed. Every value in a test is SYNTHETIC. A vendor that locks accounts is the reason this path is stopped: add NO second submission, no retry and no wait.

**Why (read the rows by id in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`: `IRPT_BCKEND-D2-W328-S1`, `-W328-S2`, `-S109`).** IB-pr-473 (merged) made the capture's probe name a challenged reply `WAF_CHALLENGE` and end the run as `UNEXPECTED_CHALLENGE:WAF_CHALLENGE` after an accepted sign-in. It covered `acquireSession`'s own probe only:
1. **W328-S1 (the hazard).** In `infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js`, `withAuthenticatedPage` (the path `mainCli` runs) probes a STORED bundle first and, for any probe that is not authenticated, whatever its reason, calls `refreshSession` (a fresh sign-in submission). At the older base this was line 1525, `if (!bundle) bundle = await refreshSession(stored.present ? 'stored bundle failed the probe' : stored.reason)`. So a stored bundle whose probe is now classified `WAF_CHALLENGE` still signs in again. That is the base code's behaviour and is NOT released anywhere, but the ruling is that it is repaired before any resident release carries `ycharts_session.js`.
2. **W328-S2 (the pair gate).** The pair is requested once per run, so a token-less first probe forecloses a later paired probe. The CTO's ruling: the gate is `discriminating !== true`: the pair runs on the first probe that holds a token; once per run stays (after ONE discriminating pair, no further pair).

**Build (two things).**
1. A stored-bundle probe whose reason is `WAF_CHALLENGE` ENDS the run with the same challenge ending `acquireSession` uses (read how IB-pr-473 ends it: `ChallengeFailure`, forwarded as `CAPTURE_FAILED:UNEXPECTED_CHALLENGE:WAF_CHALLENGE`), and does NOT call `refreshSession`: no sign-in, no retry. Every other unauthenticated reason on a stored bundle (for example no identity cookie) still refreshes EXACTLY as today.
2. The pair gate as ruled. The receipt's `probe_pair.discriminating` keeps its meaning (true only for a pair that ran with a token).

**Tests (the build's own):** `infra/aws/ec2/investor-reporting-ycharts/tests/stored_bundle_challenge_and_pair_gate.js`, run as `node --require ./tests/netguard.js tests/stored_bundle_challenge_and_pair_gate.js` from that folder, using the folder's offline fakes and replay (`fakes.js`, `replay_browser.js`, `replay_ycharts.js`). It prints ONE line per arm in the exact form `ARM <name> PASS` (or `ARM <name> FAIL`) and exits 0 only if all hold. At least FOUR arms:
(a) a stored bundle whose probe is challenged -> the run ends with the challenge ending, and a spy on `refreshSession` (or on the sign-in submission) reads 0 calls; (b) a stored bundle that is unauthenticated for another reason -> it refreshes as today (spy reads 1 call); (c) the first probe holds no token (no pair sent) and a LATER probe holds a token -> the pair runs on that later probe; (d) after one discriminating pair, a later probe sends no second pair.
Difference control: run arm (a) against the base `ycharts_session.js` (`git show <base_commit>:...` into a temp file) and show it FAILS there (record it). The round-165 test `tests/probe_challenge_and_pair.js` (9 arms PASS at base) must still print 9 arms PASS, `tests/run_offline_suite.js` must still exit 0, and the session folder `infra/aws/lambda/investor-reporting/ycharts/session/tests` (149 passed, 2 skipped at base) must read no failure.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~332/IB166-2_stored_bundle_record.json`: `{base_commit, files_changed, refresh_calls_on_challenge: 0 (the spy reading of arm a), challenge_ending_in_words, pair_gate_rule_in_words, difference_control:{arm_a_on_base:"FAIL"},
hash_pins:[every place in the repo that pins a hash of a file you changed, with what you did about it], host_reach (which resident package carries each changed file; the library is pinned by hash on the host, so this reaches it only in a resident release under its own never-widen pair), request_sent:false, deployed:false,
suites:{offline_before, offline_after, session_before, session_after}}`.

<criterion id="IB166-2-AC1" cell_refs="IB-pr-477"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-2-AC1</invocation><expect>IB166-2-AC1 PASS</expect></criterion>
<criterion id="IB166-2-AC2" cell_refs="IB-pr-477"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-2-AC2</invocation><expect>IB166-2-AC2 PASS</expect></criterion>
<criterion id="IB166-2-AC3" cell_refs="IB-pr-477"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-2-AC3</invocation><expect>IB166-2-AC3 PASS</expect></criterion>

<expected_criteria>IB166-2-AC1, IB166-2-AC2, IB166-2-AC3</expected_criteria>

What the checks grade: AC1 your new node test exits 0 with at least four `ARM ... PASS` lines and none failing (AC2 PASSes at base BY DESIGN: it is the regression guard, the round-165 probe test still printing 9 arms PASS); AC3 the record's form, `refresh_calls_on_challenge` 0, `request_sent` and `deployed` false, and that nothing outside the host folder, `ycharts/session/`, your deliverables, rows and order changed.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No resident package build, no source map, no Terraform, no other handler.
- **Refusal clause:** if a challenged stored-bundle probe cannot be ended without a sign-in on the evidence the runner has, STOP, file a row and report; do not weaken the whitelist or a test. Never weaken a check; do not edit `p166_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W332-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~332" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~332@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~332 <0.9.0_WK_IRPT_BCKEND~332@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js
infra/aws/ec2/investor-reporting-ycharts/run-ycharts-session.sh
infra/aws/ec2/investor-reporting-ycharts/README.md
infra/aws/ec2/investor-reporting-ycharts/tests/
infra/aws/lambda/investor-reporting/ycharts/session/host_capture.py
infra/aws/lambda/investor-reporting/ycharts/session/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~332/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-477.capture-stored-bundle-challenge-ending-and-pair-gate.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 158 (round 166, workstream ~P), cell `IB-pr-477`.
<owned_cells>IB-pr-477</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB166-2-AC1, IB166-2-AC2, IB166-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~332/IRPT_BCKEND.TO-IB-pr-477.capture-stored-bundle-challenge-ending-and-pair-gate.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the challenge ending for a stored bundle in a sentence and the spy reading; the pair gate rule; the four arms and the difference control on the base file; the offline, probe-test and session suites' last lines before and after; the hash pins found and what you did;
each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell changes the session runner's library in the repo only; the host pins the library by hash, so no running byte moves until a resident release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p166_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~19:3xZ: IB166-2 AC1 FAIL (the new node test is absent), AC2 PASS (the regression guard: probe_challenge_and_pair.js prints 9 arms PASS), AC3 FAIL (no record); commit-gate clean. Measured by the issuer at base: run_offline_suite.js exits 0; the session tests read 149 passed, 2 skipped (after IB-pr-473). The issuer read ycharts_session.js at 2d923d0564 line 1525 for the stored-bundle refresh (row S109).
lane: the <paths> block IS the grant; the session runner under ycharts/session/ and its EC2 library are IRPT_BCKEND's (CTO msg 4916). Class WORLD by the L6 floor; nothing is deployed and no request is sent. The vendor path stays stopped: no sign-in.
</preflight>
