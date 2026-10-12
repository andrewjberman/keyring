# TO IRPT_BCKEND.TO-IB-pr-473 -- BUILD ONLY: the YCharts capture's probe classifies a challenge as the READ path does, the probe pair runs only when the jar holds a token, and the receipt keeps the probe's leaves per step

<to_id>IRPT_BCKEND.TO-IB-pr-473</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~328</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>165</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6476 (PRD ADDENDUM v0.49 @6bed773b76, section 2 rows D2-W302-S1/-S2/-S3 and D2-S85, section 3 item 5) | **Decomp cell:** `IB-pr-473` (decomposition section 157) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-328/` (bash `/c/dev/wk-irpt-bckend-328`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it).

**HARD BOUNDS.** BUILD ONLY. No AWS call. No request to the vendor, no sign-in, no run of the session runner against anything but the repo's own
offline replay under the netguard preload. Nothing is deployed, uploaded or installed. Every value in a test or a sample is SYNTHETIC. A vendor that locks
accounts is the reason this path is stopped: add no second submission, no retry and no wait.

**Why (read the four rows, then HEAD).** The rows are in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`:
`IRPT_BCKEND-D2-W302-S1`, `-W302-S2`, `-W302-S3`, `-S85` (search by id with the native Grep tool). In short, on the host's capture
(`infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js`, `.../run-ycharts-session.sh`, and `infra/aws/lambda/investor-reporting/ycharts/session/host_capture.py`):
1. **S1.** The capture's probe has no challenge classification. A reply the READ path would call a WAF challenge (a `waf-action` header of
   challenge, captcha or block; or a 202, 403 or 405 carrying the awswaf marker) is only status-classified as NOT_LIVE (`classifyResponse`, about lines
   584-595), so an ACCEPTED sign-in whose probe is challenged ends as `AUTH_FAILED` / `NO_AUTHENTICATED_PROBE`, the label of a rejected credential. The
   READ path's test is at `ycharts/session/controller.py` about lines 35-37 and `ycharts/generate/transport.py` about lines 188-191.
2. **S2.** The probe pair is vacuous when the cookie jar holds no `aws-waf-token`: both arms send the same token-less request (`residentClient`,
   about lines 310-319, adds the token only when it exists), so "same status in both arms" separates nothing about the token.
3. **S3.** The persisted receipt keeps the probe's WAF action class and content-type class only for the FIRST probe after the submission, not per step,
   and keeps no body marker, probe path or identity-leg record (`pairControl`, about lines 1034-1039; `host_capture.py` `_STEPS`, `_PROBE_PAIR`,
   `_derive_pair`).
4. **S85.** The full receipt was consumed in process and written nowhere. **IB-pr-434 has since landed on this branch** (it persists `login_submission`
   and `probe_pair` as closed secret-free members, keeps stderr per run, and fires the signed-out diagnosis after a submission): read HEAD FIRST and
   list, in the record, which parts of S85 and S3 that order already covers, with cites. Build ONLY the remainder; do not redo what HEAD has.

**Build (three things):**
1. **Challenge classification.** `classifyResponse` (or the probe's caller) classifies a reply by the READ path's test as a challenge, with a name
   the READ path already uses if the capture's closed failure set can carry it. A probe classified as a challenge after an ACCEPTED sign-in (identity cookie and
   document identity passed) ends the capture with a failure that is NOT `AUTH_FAILED`. If you must add a value to a closed set (a failure class or a reason
   code), give its four-postulate record (MECE over the declared domain, same grain, one intent, state coherence: which remedy moves it) and a
   word-boundary token census of the name you choose over `infra/aws/ec2/investor-reporting-ycharts/` and `infra/aws/lambda/investor-reporting/`, with the scope
   printed, in the record (`new_closed_values`); `host_capture.py` validates failure class and reason by pattern (`_FAILURE_CLASS`): make the new value pass as
   a closed token and add it wherever a reader enumerates reasons.
2. **The pair runs only with a token.** When the jar holds no `aws-waf-token`, the pair is NOT sent; the receipt records that it could not discriminate
   (a boolean member under the pair, for example `discriminating: false`) and the run prints one line saying so. When the jar holds a token, the pair runs as today.
3. **The receipt per step.** Every probe step keeps, as closed secret-free leaves: `waf_action_class`, `content_type_class`, `body_marker` (a NAME from a short
   closed list you define, such as a marker class; NEVER body text), `probe_path_name` (a NAME for the path used, such as default or overridden; NEVER the URL) and
   `identity_leg` (booleans or small integers: cookie present, document identity passed). Persist them through the existing whitelist beside the receipt
   IB-pr-434 persists (0600 file); a member not on the list is dropped, never passed through. NEVER a posted value, a cookie value, a URL, a screen-text sample or a header value.

**Tests (the build's own):**
- `infra/aws/ec2/investor-reporting-ycharts/tests/probe_challenge_and_pair.js`, run as `node --require ./tests/netguard.js tests/probe_challenge_and_pair.js`
  from that folder, using the folder's offline fakes and replay (`fakes.js`, `replay_browser.js`, `replay_ycharts.js`). It prints ONE line per arm in the exact form
  `ARM <name> PASS` (or `ARM <name> FAIL`) and exits 0 only if all hold. At least five arms: (a) a reply with a challenge `waf-action` header -> challenge; (b) a 202 with the awswaf
  marker -> challenge; (c) a 403 or 405 with the awswaf marker -> challenge; (d) a plain non-challenge reply is classified exactly as before (unchanged); (e) token-less jar ->
  the pair is not sent and the receipt says it could not discriminate; (f) jar with a token -> the pair runs. The existing `tests/run_offline_suite.js` (exit 0 at base, under the same
  preload) must still exit 0.
- `infra/aws/lambda/investor-reporting/ycharts/session/tests/test_capture_receipt_per_step.py`, at least THREE tests: a planted run through `run_capture` with a fake wrapper whose
  receipt carries PLANTED synthetic secrets (a username, a password, a cookie value, a URL with a token) inside and beside the per-step members: the persisted receipt holds
  the per-step closed leaves and NONE of the planted strings; a non-whitelisted member is dropped; an unwritable directory does not fail the capture. The folder reads `127 passed, 2 skipped`
  at base; after, no failure and at least 130 passed.
- The planted run's persisted receipt is ALSO written, by a small script in your deliverables folder, to `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~328/IB165-3_persisted_receipt_sample.json`, exactly as the
  code persisted it: a top-level `steps` list of at least two steps, each carrying the five members above by those exact names.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~328/IB165-3_capture_probe_record.json`: `{base_commit, files_changed, already_covered_by_head: [{what, cite}],
new_closed_values: [{name, set, four_postulates:{i_mece, ii_same_grain, iii_one_intent, iv_state_coherence}, token_census:{scope, counts}}] (empty list if you add none), pair_rule_in_words,
planted_secrets: [4 or more synthetic strings of 8 characters or more], per_step_members: [names], hash_pins: [every place in the repo that pins a hash of a file you changed, with what you did about it],
host_reach (which resident package carries each changed file; the library is pinned by hash on the host, so this reaches it only in a resident release under its own never-widen pair), request_sent: false,
deployed: false, suites: {offline_before, offline_after, session_before, session_after}}`.

<criterion id="IB165-3-AC1" cell_refs="IB-pr-473"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-3-AC1</invocation><expect>IB165-3-AC1 PASS</expect></criterion>
<criterion id="IB165-3-AC2" cell_refs="IB-pr-473"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-3-AC2</invocation><expect>IB165-3-AC2 PASS</expect></criterion>
<criterion id="IB165-3-AC3" cell_refs="IB-pr-473"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-3-AC3</invocation><expect>IB165-3-AC3 PASS</expect></criterion>

<expected_criteria>IB165-3-AC1, IB165-3-AC2, IB165-3-AC3</expected_criteria>

What the checks grade: AC1 your node test exits 0 with at least five `ARM ... PASS` lines and none failing, and `run_offline_suite.js` still exits 0; AC2 the session folder reads no failure and at least 130 passed, and your new test file exists;
AC3 the record and the sample: at least four planted strings, none in the sample's text; a `steps` list of at least two, each with the five members by name; every leaf a boolean, an integer, null or a short string with no `http`, no `@` and no `%`.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No resident package build, no source map, no Terraform, no other handler.
- **Refusal clause:** if a probe challenge cannot be told from a real authenticated page by the evidence the runner has, or a per-step member cannot be persisted without a secret-bearing leaf, STOP, file a row and report;
  do not weaken the whitelist to pass. Never weaken a check or a test; do not edit `p165_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W328-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~328" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~328@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~328 <0.9.0_WK_IRPT_BCKEND~328@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js
infra/aws/ec2/investor-reporting-ycharts/run-ycharts-session.sh
infra/aws/ec2/investor-reporting-ycharts/README.md
infra/aws/ec2/investor-reporting-ycharts/tests/
infra/aws/lambda/investor-reporting/ycharts/session/host_capture.py
infra/aws/lambda/investor-reporting/ycharts/session/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~328/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-473.capture-probe-challenge-pair-token-and-per-step-receipt.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 157 (round 165, workstream ~P), cell `IB-pr-473`.
<owned_cells>IB-pr-473</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB165-3-AC1, IB165-3-AC2, IB165-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~328/IRPT_BCKEND.TO-IB-pr-473.capture-probe-challenge-pair-token-and-per-step-receipt.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; what HEAD already covered of S85 and S3 (cites); the challenge classification and the failure it ends in; the pair rule; the per-step members and where the file is written; any new closed value with its four postulates and census;
the node arms; both suites' last lines before and after; the hash pins found and what you did; each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell changes the session runner's library and its host wrapper in the repo only; the host pins the library by hash, so no running byte moves until a resident release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p165_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~18:0xZ: IB165-3 AC1 FAIL (the new node test is absent), AC2 FAIL (the new python test is absent), AC3 FAIL (no record); commit-gate clean. Measured by the issuer at base: `node --require ./tests/netguard.js tests/run_offline_suite.js` exits 0; `pytest ycharts/session/tests` reads 127 passed, 2 skipped. The line numbers above are the rows' (INFERRED by the issuer); the worker reads HEAD, where IB-pr-434 may have moved them.
lane: the <paths> block IS the grant; the session runner under ycharts/session/ and its EC2 library are IRPT_BCKEND's (CTO msg 4916). Class WORLD by the L6 floor; nothing is deployed and no request is sent. The vendor path stays stopped: no sign-in.
</preflight>
