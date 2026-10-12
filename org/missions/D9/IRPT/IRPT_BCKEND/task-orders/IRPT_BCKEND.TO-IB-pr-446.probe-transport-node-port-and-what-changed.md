# TO IRPT_BCKEND.TO-IB-pr-446 -- READ ONLY, CODE ONLY: the probe's transport (`node-port`), the job's calls after a capture, and what changed since 2026-10-05

<to_id>IRPT_BCKEND.TO-IB-pr-446</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~304</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>143</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5579 (on `2.0.0_SA_COO~G2`'s read-out @07f11659ea) | **Decomp cell:** `IB-pr-446` (decomposition section 135) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-304/` (bash `/c/dev/wk-irpt-bckend-304`). Work only there.

**HARD BOUNDS.** A CODE AND RECORD READ, and `git log` / `git show` on this repository. NO request to the vendor, NO sign-in, NO
run of the session runner (the offline suite under its netguard preload is the only execution allowed, and only to watch a
branch execute), NO SSM or host command, NO AWS call of any kind, no secret read. **You propose NO change to how the vendor is
reached**: the CTO has ruled that whether Opal adapts its automation to a vendor's challenge is not an engineering call alone
and is put to Andrew. Describe what the code does; recommend nothing about getting past the challenge.

**What is known** (read these two records whole first):
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~302/IB141-1_RECEIPT_DIAGNOSIS_READ.md` (the diagnosis from
code) and `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r14/FIFTH_RUN_HOST_SIDE_READ_20261011.md` with its
ADDENDUM 1 (the receipt's values, read out on the host). In short: on the fifth run the host submitted one sign-in; the posted
credentials matched the secret; the vendor answered 302; the page then read `CH-AUTHENTICATED` on seven steps and the session
cookie's name was present; and the PROBE was answered 202 with the firewall action class `challenge` on both arms, with and
without the token. Every probe went `via node-port`. So the credentials are right, the browser is signed in, the account is not
locked; what is refused is the probe. The session bundle on the host was last written 2026-10-05T10:04Z: captures worked until
then. The host's library hash equals this tree's (`ycharts_session.js` sha256 a1c28801...).

**Read and state, each from cited lines:**
1. **What `node-port` is.** In `infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js` (about lines 300-345 and wherever
   the port is built): what makes the request (which client, from which process), what it sends (which cookies, which headers,
   which user agent; whether it carries the browser's cookie jar, and the firewall's token cookie if the jar holds one), and
   every OTHER transport the library can use (`browser-context`, `api-request-context`, `page-document`, `bundle-identity`, and
   any other), each with where it is chosen and when the library falls back from one to another (`transports`).
2. **Why the probe uses it and not the page** (`why_the_probe_uses_it`): the reason AS THE CODE OR ITS COMMENTS STATE IT (quote
   the comment's line), or, if no comment states it, say so and give the inference separately marked. Include what the probe is
   FOR (the face of `infra/aws/lambda/investor-reporting/ycharts/session/` : the session is USABLE only after the intended
   identity and a report-capable response are verified "from the transport that will use it"): read whether the probe's transport
   is deliberately the transport the later Lambda replay uses. PRD context: FWD-4's CONSTRAINT lines in
   `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` (about lines 50-52).
3. **The vendor calls a job makes AFTER a capture** (`job_calls_after_a_capture`): in
   `infra/aws/lambda/investor-reporting/ycharts/generate/` (the resident worker, `transport.py`, `recipe.py`, `job.py`) and
   `ycharts/session/` (`controller.py`, `broker.py`, `resident_session.py`, `deadline_transport.py`): every call to the vendor a
   generation makes once it holds a session (upload, portfolio, generation, read-back, PDF, and the session's own checks), each
   with the transport that makes it (the same Node/HTTP client kind as the probe, a Python HTTP client, the browser) and the
   code line; counted by transport. Then: would those calls meet the same refusal the probe met? Answer true, false or null with
   its claim; `measured` only if a record already on the trunk shows it (the journal lines quoted in
   `deliverables/0.7.0_AE_CloudOps~IB2/IB129-1_CAPTURE_FAILURE_READ.md` name `READ_BACK_PENDING:WAF_CHALLENGE` on the read path
   on several days: say what that shows and what it does not).
4. **What changed on our side since 2026-10-05, or that nothing did** (`changes_since_2026_10_05`): `git log --since=2026-10-04`
   on `infra/aws/ec2/investor-reporting-ycharts/` and `infra/aws/lambda/investor-reporting/ycharts/` (state the paths searched
   and the command): per changed file, its commits and one sentence on whether the change bears on the probe, its transport, the
   request's headers or cookies, or the classification of a reply. And what the HOST runs (`what_the_host_runs`): from the
   records on the trunk only (the resident releases st29 to st32 and their packets under
   `org/missions/D9/IRPT/IRPT_YCDGEN/` and `org/tier2_senior/0.7.0_AE_CloudOps~YC2/deliverables/`; search with the native Grep
   tool for `st30`, `st31`, `st32`, `library_sha256`, `CAPTURE_SOURCE_PIN`): which releases reached the host since 2026-10-05,
   on which dates, and whether any moved the library or the wrapper BEFORE the first failed capture in the journal read
   (IB-pr-431: failures from late September, the last three with `NO_AUTHENTICATED_PROBE`). The question behind this: did
   something of OURS change between the last good bundle and the first challenged probe, or did the vendor's side change while
   ours stood still? If the records cannot say, say so (`claim: absent`) and list what would.
5. **Not established** (`not_established`): everything above you could not settle from code and records.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~304/`: `IB143-1_probe_transport_read.json` with
`{node_port:{what_it_is, sends, code_lines, claim}, transports:[{name, chosen_at, carries_the_browsers_cookies, falls_back_to}],
why_the_probe_uses_it:{in_words, stated_in_code_or_inferred, code_lines, claim}, job_calls_after_a_capture:{calls:[{call,
transport, code_line}], by_transport:{...}, would_meet_the_same_refusal, claim, reason},
changes_since_2026_10_05:{paths_searched, command, nothing_changed_in_the_repo, files:[{path, commits:[...],
bears_on_the_probe_or_its_transport_in_words}], what_the_host_runs:{releases_since:[{release, date, moved}], read_from, claim},
ours_or_the_vendors:{answer, claim}}, not_established:[...], vendor_requests_made:0, sign_ins_made:0, host_commands_run:0,
aws_calls_made:0, changes_proposed_to_how_the_vendor_is_reached:0}`; and a one-page `IB143-1_PROBE_TRANSPORT_READ.md` written for
a reader who will put the question to Andrew: plain statements, each with its claim.

<criterion id="IB143-1-AC1" cell_refs="IB-pr-446"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r143/p143_cells.py" . IB143-1-AC1</invocation><expect>IB143-1-AC1 PASS</expect></criterion>
<criterion id="IB143-1-AC2" cell_refs="IB-pr-446"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r143/p143_cells.py" . IB143-1-AC2</invocation><expect>IB143-1-AC2 PASS</expect></criterion>
<criterion id="IB143-1-AC3" cell_refs="IB-pr-446"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r143/p143_cells.py" . IB143-1-AC3</invocation><expect>IB143-1-AC3 PASS</expect></criterion>

<expected_criteria>IB143-1-AC1, IB143-1-AC2, IB143-1-AC3</expected_criteria>

The checks grade the shape: cited lines, claims, every call counted by transport, the changes listed per file or stated as
none with what was searched, the five zeros. The answers are UNMEASURED by the issuer; "it cannot be told from code and
records" passes wherever it is the truth.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** if answering needs a value only the host or the vendor holds, do not fetch it: list it under
  `not_established`. If a criterion cannot be met as written, stop, file a row and report. Never weaken a check; do not edit
  `p143_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W304-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's existing line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~304" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~304@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~304 <0.9.0_WK_IRPT_BCKEND~304@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~304/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-446.probe-transport-node-port-and-what-changed.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 135 (round 143, workstream ~P), cell `IB-pr-446`.
<owned_cells>IB-pr-446</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB143-1-AC1, IB143-1-AC2, IB143-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~304/IRPT_BCKEND.TO-IB-pr-446.probe-transport-node-port-and-what-changed.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: what `node-port` is and what it sends; the other transports; why the probe uses it, and
whether the code states that or you infer it; the job's vendor calls after a capture by transport, and whether they would meet
the same refusal, with the claim; what changed in the repo since 2026-10-05 and what reached the host, and whether the records
say the change was ours or the vendor's; what is not established; each criterion's last line; the proof checker's result;
commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a code and record read written to the worker's own deliverables folder; nothing is edited, requested or run.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change and no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p143_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~18:5xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The facts on the face are 2.0.0_SA_COO~G2's read-out @07f11659ea (its message 5577, read by the issuer) and IB-pr-444's merged record; the issuer read the `via` values at ycharts_session.js:322-341 before the cut. The face forbids any proposal on how the vendor is reached (CTO msg 5579).
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only). The vendor path stays stopped.
</preflight>
