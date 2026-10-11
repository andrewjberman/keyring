# TO IRPT_BCKEND.TO-IB-pr-434 -- BUILD ONLY: the YCharts session capture says what its sign-in did (receipt persisted, diagnosis un-gated, stderr kept per run)

<to_id>IRPT_BCKEND.TO-IB-pr-434</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~292</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>132</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5025 (ruling on IB-pr-431's read; row IRPT_BCKEND-D2-IB2-S1) | **Decomp cell:** `IB-pr-434` (decomposition section 124) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-292/` (bash `/c/dev/wk-irpt-bckend-292`). Work only there.

**HARD BOUNDS.** BUILD ONLY. No AWS call. No request to the vendor, no sign-in, no run of the session runner against anything but
the repo's own offline replay under the netguard preload. Nothing is deployed, uploaded or installed. Every value in a test or a
sample is synthetic.

**Why.** On 2026-10-11 the host's capture failed with `CAPTURE_FAILED:AUTH_FAILED:NO_AUTHENTICATED_PROBE`. The read
(`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB129-1_CAPTURE_FAILURE_READ.md`, read it whole) found: the
sign-in form was submitted at step 0, steps 1 to 7 each read `CH-AUTHENTICATED`, the probe never passed, `MAX_STEPS` ran out. It
could NOT say whether the vendor accepted the credentials, because the two receipt members that separate "accepted, probe broken"
from "rejected, signed-out page looks like the app" -- `login_submission` and `probe_pair` -- are persisted nowhere; and the one
explicit diagnosis of the second case, `SIGNED_OUT_APP_CHROME` (`ycharts_session.js` about lines 1041-1056), is gated on `!filled`
and so cannot fire after a submission. The vendor path is stopped for every seat until the capture can say what it did.

**Build (three things, ruled by the CTO):**
1. **The receipt's `login_submission` and `probe_pair` are PERSISTED, as CLOSED, secret-free members.** Read
   `infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js` (where each member is built: about lines 1040, 1140-1174,
   1313-1346) and `infra/aws/lambda/investor-reporting/ycharts/session/host_capture.py` (`run_capture`, about lines 93-130: it reads
   the runner's one receipt line and today propagates only a closed failure token). Persist, for EVERY capture run that reached a
   submission or a probe, a small receipt beside the stderr file (0600), holding only: booleans (for example whether the posted
   username field matched the secret's, whether the password field did), integers (the vendor's reply status, step numbers), null,
   and short NAMES (a selector name, a challenge signature, a reason code, a cookie NAME). NEVER a posted value, a cookie value, a
   URL carrying a token or query string, a screen-text sample, or a header value. Whitelist the members by name; a member not on
   the list is dropped, never passed through. The failure token the resident logs stays what it is today.
2. **The signed-out-app-chrome diagnosis fires after a submission too, under ITS OWN reason code**, so the two cases read
   differently: when a submission was made, the page then reads app chrome, and the probe says no identity cookie, the runner fails
   EXPLICITLY (not by running out of steps) with the new code and the same kind of evidence the `!filled` branch carries, minus
   anything secret. The existing `SIGNED_OUT_APP_CHROME` branch (before any submission) is unchanged. `SIGNIN_FORM_REPRESENTED` is
   unchanged. Do not add a second submission, a retry or a wait: a vendor that locks accounts is the reason this path is stopped.
   A new reason code is a new value of a closed set: state its four-postulate record (MECE over the declared domain of capture
   failure reasons, same grain, one intent, state coherence: which remedy moves it) and a word-boundary token census of the name
   you choose over the repo's two trees that read reason codes (`infra/aws/ec2/investor-reporting-ycharts/` and
   `infra/aws/lambda/investor-reporting/`), with the scope printed. `host_capture.py` validates the failure class and reason by
   pattern (`_FAILURE_CLASS`): check the new code passes through as a closed token and add it wherever a reader enumerates reasons.
3. **The capture's stderr is kept PER RUN, not truncated at every run.** Today `stderr_sink` opens `last-capture.stderr` with
   `O_TRUNC` and `keep_tail` cuts it to 64 KiB. Keep the last N runs (choose N, 8 to 32, and say why), each in its own 0600 file
   named by a rule that sorts by time, each still cut to a byte bound, the oldest removed so the directory never grows without
   bound. `last-capture.stderr` may remain as the newest run's name or be replaced; say which. A directory that cannot be written
   still costs the record, never the capture.

**Tests (the build's own):**
- `infra/aws/ec2/investor-reporting-ycharts/tests/receipt_after_submit.js`, run as
  `node --require ./tests/netguard.js tests/receipt_after_submit.js` from that folder, using the folder's existing offline fakes and
  replay (`fakes.js`, `replay_browser.js`, `replay_ycharts.js`): arms for (a) submission made, page reads app chrome, no identity
  cookie -> the NEW code, explicit, before `MAX_STEPS`; (b) no submission, same page -> the OLD code, unchanged; (c) submission made
  and the form re-presented -> `SIGNIN_FORM_REPRESENTED`, unchanged; (d) a successful sign-in is unchanged. It exits 0 only if all
  arms hold and prints one line per arm. The existing `tests/run_offline_suite.js` (rc 0 at base, under the same preload) must
  still exit 0.
- `infra/aws/lambda/investor-reporting/ycharts/session/tests/test_capture_receipt_persisted.py`: a planted run through
  `run_capture` with a fake wrapper whose receipt carries PLANTED synthetic secrets (a username, a password, a cookie value, a URL
  with a token) inside and beside the two members: the persisted receipt holds the two members' closed leaves and NONE of the
  planted strings; a non-whitelisted member is dropped; per-run stderr files rotate at N; an unwritable directory does not fail the
  capture. The folder reads `118 passed, 1 skipped` at base; after, no failure and no fewer passed.
- The planted run's persisted receipt is ALSO written, by a small script in your deliverables folder, to
  `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~292/IB132-1_persisted_receipt_sample.json`, exactly as the
  code persisted it.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~292/IB132-1_capture_receipt_record.json`:
`{files_changed:[...], persisted_members:{login_submission:[...leaf names...], probe_pair:[...]}, dropped_by_whitelist_example,
planted_secrets:[the four or more synthetic strings the sample run planted], new_reason_code:{name, four_postulates:{i_mece,
ii_same_grain, iii_one_intent, iv_state_coherence}, token_census:{scope, counts}}, stderr_per_run:{file_name_rule, runs_kept,
max_bytes_per_run, last_capture_name_kept}, hash_pins:[every place in the repo that pins a hash of a file you changed, with what
you did about it], host_reach, request_sent:false, deployed:false, suites:{offline_before, offline_after, session_before,
session_after}}`. `host_reach`: the library is pinned by hash on the host, so this change reaches it only in a resident release
under its own never-widen pair; say which package carries each changed file (read `reports/build_resident_package.py` and
`infra/aws/ec2/investor-reporting-ycharts/README.md`).
- **`hash_pins`:** if a test, a manifest or a SHA256SUMS file in the repo pins the bytes of a file you change, list it. Regenerate
  it only if it is inside your `<paths>` and is a generated record of those bytes; if it is outside, STOP on that file and file a row.

<criterion id="IB132-1-AC1" cell_refs="IB-pr-434"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r132/p132_cells.py" . IB132-1-AC1</invocation><expect>IB132-1-AC1 PASS</expect></criterion>
<criterion id="IB132-1-AC2" cell_refs="IB-pr-434"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r132/p132_cells.py" . IB132-1-AC2</invocation><expect>IB132-1-AC2 PASS</expect></criterion>
<criterion id="IB132-1-AC3" cell_refs="IB-pr-434"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r132/p132_cells.py" . IB132-1-AC3</invocation><expect>IB132-1-AC3 PASS</expect></criterion>

<expected_criteria>IB132-1-AC1, IB132-1-AC2, IB132-1-AC3</expected_criteria>

What AC2 greps, exactly: in the sample file, every leaf under a `login_submission` or a `probe_pair` member must be a boolean, an
integer, null, or a string of at most 120 characters from names' characters with no `http`, no `@` and no `%`; and none of the
record's `planted_secrets` (four or more strings, each 8 characters or longer) may appear anywhere in the sample's text.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No resident package build, no source map, no Terraform, no other handler.
- **Refusal clause:** if the two members cannot be persisted without a secret-bearing leaf, or the new branch cannot be told from
  a real authenticated page by the evidence the runner has, STOP, file a row and report; do not weaken the whitelist to pass. If a
  criterion cannot be met as written, stop, file a row and report. Never weaken a check or a test; do not edit `p132_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W292-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; append only, keeping the channel
  file's existing line endings byte for byte; check the id is free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~292" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~292@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~292 <0.9.0_WK_IRPT_BCKEND~292@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push. Use no gate override.

<paths>
infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js
infra/aws/ec2/investor-reporting-ycharts/run-ycharts-session.sh
infra/aws/ec2/investor-reporting-ycharts/README.md
infra/aws/ec2/investor-reporting-ycharts/tests/
infra/aws/lambda/investor-reporting/ycharts/session/host_capture.py
infra/aws/lambda/investor-reporting/ycharts/session/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~292/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-434.capture-receipt-persisted-and-diagnosis-ungated.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 124 (round 132, workstream ~P), cell `IB-pr-434`.
<owned_cells>IB-pr-434</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB132-1-AC1, IB132-1-AC2, IB132-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~292/IRPT_BCKEND.TO-IB-pr-434.capture-receipt-persisted-and-diagnosis-ungated.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the persisted members and where the file is written; the new reason code, its four postulates
in one line each and its census; the four offline arms; the stderr rule and N; the hash pins found and what you did; both suites'
last lines before and after; each criterion's last line; the proof checker's result; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell changes the session runner's library and its host wrapper in the repo only; the host pins the library by hash (IB-pr-431's read), so no running byte moves until a resident release under its own pair (CTO msg 5025: st32).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p132_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~13:4xZ: AC1 FAIL (the new test is absent), AC2 FAIL (no sample), AC3 FAIL (no record); commit-gate clean. Measured at base by the issuer: `node --require ./tests/netguard.js tests/run_offline_suite.js` exits 0 (it exits 2 without the preload); `pytest ycharts/session/tests` reads 118 passed, 1 skipped.
lane: the <paths> block IS the grant; the session runner under ycharts/session/ and its EC2 library are IRPT_BCKEND's (CTO msg 4916). Class WORLD by the L6 floor; nothing is deployed and no request is sent.
</preflight>
