# TO IRPT_BCKEND.TO-IB-pr-444 -- READ ONLY: the fifth run's capture receipt -- which leaves confirm or kill "accepted, then challenged", and why the new reason did not fire

<to_id>IRPT_BCKEND.TO-IB-pr-444</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~302</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>141</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5524 (on `2.0.0_SA_COO~G2`'s fifth-run host read) | **Decomp cell:** `IB-pr-444` (decomposition section 133) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-302/` (bash `/c/dev/wk-irpt-bckend-302`). Work only there.

**HARD BOUNDS.** A CODE AND RECORD READ, and nothing else. NO request to the vendor, NO sign-in, NO run of the session runner
(not even against the offline replay with a network path open; the offline suite under its netguard preload is allowed if you
want to see a branch execute), NO SSM or host command, NO AWS call of any kind, no secret read. The vendor path is stopped for
every seat by the CTO until this read is ruled on. Nothing is edited but your own deliverables.

**Why.** The resident host signs in to the vendor through `infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js`; the
wrapper `infra/aws/lambda/investor-reporting/ycharts/session/host_capture.py` persists a whitelisted, secret-free receipt of each
capture (built in IB-pr-434). A fifth run was made on the CTO's word with that build on the host (release st32). Read the
host-side record whole: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r14/FIFTH_RUN_HOST_SIDE_READ_20261011.md`.
Its receipt, by shape: ONE submission; the posted username and password MATCH the secret; the vendor's reply to the post was
302; then seven steps each read `probe_http_status` 202, `probe_state` NOT_LIVE, `probe_reason` NOT_LIVE; both arms of the
closing probe pair (with and without the token) returned 202 with the same cookies; `waf_header_sent`,
`waf_token_cookie_in_jar` and `waf_token_cookie_sent` are false in both arms; no location in either reply. The reason is the
old generic `NO_AUTHENTICATED_PROBE`; the new `SIGNED_OUT_APP_CHROME_AFTER_SUBMIT` did NOT fire.

**The hypothesis to test (the CTO's, stated as an inference):** the sign-in was ACCEPTED (a 302 answers an accepted post), the
account is not locked, and what the probe meets is a web firewall's CHALLENGE (a 202 on every probe is the status such a
challenge answers with; the journal has met `WAF_CHALLENGE` on the read path before). If so the capture is not passing a
challenge, which is a different defect from a rejected or locked credential.

**Do:**
1. **Read the probe in code.** In `ycharts_session.js`: how the session probe is made (`probeSession` and what it calls), how a
   reply's status, headers and body are classified, what `NOT_LIVE` means and every status that produces it, how a 202 is
   treated, what `waf_action_class`, `content_type_class`, `location_present`, `via`, `state`, `waf_header_sent`,
   `waf_token_cookie_in_jar`, `waf_token_cookie_sent`, `same_cookies`, `with_token_errored` are and every closed value each can
   take (with the line that writes it). Read also where the READ path classifies `WAF_CHALLENGE`
   (`infra/aws/lambda/investor-reporting/ycharts/` : search for `WAF_CHALLENGE`, `READ_BACK_PENDING`, `x-amzn-waf`, `202`) and
   say whether the read path and the capture's probe use the same test for a challenge or two different ones.
2. **Read the whitelist.** In `host_capture.py`: which of those leaves the persisted receipt keeps, under which path, and which
   it drops. The fifth run's receipt has 120 leaves; the host reader printed some as values and 33 only as a length and a hash,
   and says other "hashed leaves (the states, the `via` values, the WAF action class, the header name) are closed enums on the
   host that my check did not print".
3. **Name the leaves that decide** (`deciding_leaves`): for each, its path in the persisted receipt (as the whitelist writes it;
   say if a step index or an arm name is part of the path), the closed values the code can write there (`closed_values`, with
   `written_at` as `file:line`), which of those values CONFIRM the hypothesis (`confirms_if`), which KILL it (`kills_if`), and
   `persisted_by_the_whitelist` (true or false: a leaf that decides but is not persisted is a finding, and goes in the list with
   false). A leaf whose every value is compatible with both readings decides nothing and is not listed. Order them by how much
   one read of that leaf would settle.
4. **Why the new reason did not fire** (`why_the_after_submit_reason_did_not_fire`): the branch's exact condition in code (cite
   the lines), which part of it this run did not meet, and what probe reason it needed against what this run carried. Claim
   `measured` if the code and the record's printed leaves settle it; `inferred` otherwise. Say whether, GIVEN the hypothesis, the
   branch SHOULD have a sibling (a distinct reason for "a submission was accepted and the probe meets a challenge"): describe
   the condition in words; build nothing.
5. **The verdict from what is already read** (`hypothesis`): `SUPPORTED`, `CONTRADICTED` or `UNDECIDED`, with its claim and a
   reason that names the leaves it rests on. List `other_explanations_not_excluded` (for example: the probe endpoint answers 202
   to any client while a calculation is pending; a redirect after login to a page that sets no session; the three false WAF
   booleans meaning the capture never sent what a challenge needs) and, for each, the leaf that would exclude it.
6. **What to ask the host reader** (`reads_asked_of_the_host_reader`): the receipt paths to read out, each with what it decides,
   in the order to read them; values only as closed codes, booleans, integers and names, as the whitelist already guarantees.
   These are read from the file already on the host; no new run is asked for.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~302/`: `IB141-1_receipt_diagnosis.json` with
`{hypothesis:{stated, verdict_from_what_is_already_read, claim, reason}, deciding_leaves:[{receipt_path, closed_values, written_at,
confirms_if, kills_if, persisted_by_the_whitelist, note}], what_the_probe_result_means:{status_202_in_the_code,
not_live_in_the_code, classified_at, same_test_as_the_read_path}, why_the_after_submit_reason_did_not_fire:{in_words, code_lines,
claim, a_sibling_reason_would_need}, other_explanations_not_excluded:[{explanation, excluded_by_leaf}],
reads_asked_of_the_host_reader:[{receipt_path, what_it_decides}], vendor_requests_made:0, sign_ins_made:0, host_commands_run:0,
aws_calls_made:0}`; and a one-page `IB141-1_RECEIPT_DIAGNOSIS_READ.md`.

<criterion id="IB141-1-AC1" cell_refs="IB-pr-444"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r141/p141_cells.py" . IB141-1-AC1</invocation><expect>IB141-1-AC1 PASS</expect></criterion>
<criterion id="IB141-1-AC2" cell_refs="IB-pr-444"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r141/p141_cells.py" . IB141-1-AC2</invocation><expect>IB141-1-AC2 PASS</expect></criterion>
<criterion id="IB141-1-AC3" cell_refs="IB-pr-444"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r141/p141_cells.py" . IB141-1-AC3</invocation><expect>IB141-1-AC3 PASS</expect></criterion>

<expected_criteria>IB141-1-AC1, IB141-1-AC2, IB141-1-AC3</expected_criteria>

The checks grade the shape: each deciding leaf with its closed values, where it is written, non-overlapping confirming and
killing values drawn from those closed values, and whether it is persisted; the branch's condition cited by line; one of three
verdict words with a claim; the four zeros. Whether the hypothesis holds is UNMEASURED by the issuer: `UNDECIDED` passes as
well as the other two, and it is the right answer if the printed leaves do not settle it.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** if answering needs a value only the host holds, do not fetch it: list it in
  `reads_asked_of_the_host_reader`. If a criterion cannot be met as written, stop, file a row and report. Never weaken a check;
  do not edit `p141_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W302-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's existing line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~302" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~302@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~302 <0.9.0_WK_IRPT_BCKEND~302@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~302/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-444.fifth-run-receipt-diagnosis-which-leaves-decide.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 133 (round 141, workstream ~P), cell `IB-pr-444`.
<owned_cells>IB-pr-444</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB141-1-AC1, IB141-1-AC2, IB141-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~302/IRPT_BCKEND.TO-IB-pr-444.fifth-run-receipt-diagnosis-which-leaves-decide.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the verdict on the hypothesis with its claim and the leaves it rests on; the deciding
leaves in order, each with its confirming and killing values and whether the receipt persists it; what a 202 and NOT_LIVE are
in the code and whether the read path tests a challenge the same way; why the new reason did not fire, by line; the other
explanations not excluded; the reads to ask of the host reader; each criterion's last line; the proof checker's result;
commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a code and record read written to the worker's own deliverables folder; nothing is edited, requested or run.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change and no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p141_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~18:1xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The receipt's facts on the face are 2.0.0_SA_COO~G2's reading @77f135f74f, read by the issuer in that record's sections 1 to 4, not re-read on the host. The hypothesis is the CTO's and is stated as an inference; all three verdict words pass.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only). The vendor path stays stopped (CTO msg 5524: no request until the CTO rules on this read).
</preflight>
