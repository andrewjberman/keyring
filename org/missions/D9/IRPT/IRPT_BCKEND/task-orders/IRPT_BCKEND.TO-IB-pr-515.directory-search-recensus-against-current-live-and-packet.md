# TO IRPT_BCKEND.TO-IB-pr-515 -- `irpt-directory-search` RE-CENSUSED and rebuilt against its CURRENT live bytes, BUILD ONLY, with step 0 and the refreshed never-widen packet (CTO RE 7037, round 181; supersedes the live side of IB-pr-499's packet)

<to_id>IRPT_BCKEND.TO-IB-pr-515</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~365</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>181</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's RE 7037 ("round 181 = the directory-search apply, step 0 reads which home it reads; no home moves") and the round-180 analysis item 2 | **Decomp cell:** `IB-pr-515` (decomposition section 173) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-515` (inlined):** round 171's order `IB-pr-499` built the `irpt-directory-search` candidate (handler.py: a tail query returns the ACCOUNT's own entry) and wrote the never-widen packet `deliverables/0.9.0_WK_IRPT_BCKEND~349/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-499.md`, with the LIVE zip at CodeSha256 `TefVhmGStCRorgQFrQFCS0lVUC+pXrWJYfdUCEExqe4=` (hex `4de7d586...`, 2026-10-12T14:06:08Z). **That live zip is gone:** IRPT_ANLREQ's status-rule release (ledger `irpt-status-rule-all-eight-20261013`) redeployed `irpt-directory-search` at 2026-10-13T12:34:28Z; the live CodeSha256 is now `tvrsQ+w820jp1pxiUoYrhiKCZGVnViUTbBsDUbJEG3w=` (194476 bytes; the source map's `irpt-directory-search` row records it as `artifact_sha256`, `last_deployed_commit` `1b88b22dea`). Another deploy ledger, `irpt-status-rule-exercise-20261013` (0.7.0_AE_CloudOps~AQ2, opened 2026-10-13, 6 legs), names `irpt-directory-search` too. So the packet's digest gate would STOP. **Rebuild the candidate against the CURRENT live, re-run the census, the replay and the reach, and write a REFRESHED packet.** BUILD ONLY: nothing is uploaded, applied, deployed or invoked; no Terraform; no write to the source map.

**Root:** your worktree (`git rev-parse --show-toplevel`); `git rev-parse HEAD` before your first commit is `base_commit` (state it). **Client data rule:** counts, sha256 and reason codes only in any tracked file; extracted zips and scratch stay OUTSIDE the worktree (`C:/dev/_scratch365/`), deleted file by file at the end with a short bounded script.

**Read first (prior art, copy what you need into YOUR folder, edit none of theirs):** `deliverables/0.9.0_WK_IRPT_BCKEND~349/` (the packet, `ib171_4_member_diff.py`, `ib171_4_replay_reach.py`, `IB171-4_release_census.json`, `IB171-4_reach_and_arms.json`) and `deliverables/0.9.0_WK_IRPT_BCKEND~278/signature_closure_attr.py`.

**Do:**
1. **Step 0 (CTO RE 7037; READ ONLY).** Which directory home does `irpt-directory-search` READ? Read the function's environment `IRPT_DIRECTORY_BUCKET_MAP` (`lambda get-function-configuration`; record ONLY the firm names and the bucket/key of the directory, no other variable) and its IAM role's S3 grants, and the builder's home: the bucket and key the 49F builder wrote its directory read from at the 7639-of-7640 `account_id` snapshot (`holdings_snapshot._directory_account_ids` via `hs.firm_bucket_map()`: `opal-data-bd`, `investor-reporting/directory/latest.json`, per row `IRPT_BCKEND-D2-W364-S1`). Record `directory_home`: `{"function_reads":"<bucket/key per firm>","builder_reads":"<bucket/key>","match":true|false,"source":"<file:line or call>"}`. **If they DIFFER (`match` false): this is a finding, not a failure: file ONE surprise row naming BOTH homes (the CTO's ruling: no home moves in this release; the canonical `opal-data-49financial` address is NOT adopted here, its migration is its own project, rule 30 / R19), say in the packet that the APPLY must STOP at its own step 0 until the CTO rules, and carry on with the rest of this order.**
2. **The open ledgers.** List every deploy ledger under `org/critical_paths/change_management/` (and open ones on any worktree: `git worktree list --porcelain`, then `ls-tree` per tree) that names `irpt-directory-search`, with its status (`OPEN`/`CLOSED`/`SUPERSEDED`/`HELD`): `open_ledgers_naming_the_function`. The repository's rule (`docs/deployment/MDPF_RUNNER_CODE_SYNC.md` SEQUENCING and the NEVER-2 law): an act that names a file another open deploy order names waits for that ledger to read CLOSED; state in the packet which ledger(s) the apply waits on.
3. **Rebuild.** `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-directory-search` at your HEAD (the real source map; `handler.py` is a `files[]` member read from the source dir; show the real `lambda-source-map.json` sha256 identical before and after); pack TWICE to byte-identical output; upload nothing. Fetch the CURRENT live zip (`aws lambda get-function`, `Code.Location`) to scratch; its sha256 must equal the source map's `artifact_sha256` (base64 `tvrsQ+w8...`), else STOP and say what differs.
4. **The changed members** against the CURRENT live: **must be exactly `handler.py`** (its built sha256 equals the repo blob at the pin). Any other differing member (for example one the status-rule release changed) is a STOP: file a row naming it and report; do not widen.
5. **Signature instrument** (`signature_closure_attr.py`) on the built AND the live zip: 0 signature mismatches on both; attribute mismatches: built not above live and every built line a live line (the latent `served.py`/`enforce.py` `load_report_owner` line, row W349-S1, is expected on both).
6. **Replay arms and reach** (offline, SYNTHETIC; the four arms of the prior packet on the built `handler.py` against the CURRENT live's: tail of a non-head account, shared tail, name query, entry without masks) and the REACH counts per firm over the landed directories (counts only, read the way the builder reads them).
7. **The refreshed packet** `deliverables/0.9.0_WK_IRPT_BCKEND~365/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-515.md` in the prior packet's form (it supersedes `IB-pr-499`'s: say so by that id, and say its live digest is stale and why): the served change in words; the CURRENT live and built sha256; the one changed member; **Branch A** (land digest-gated, never a mint; via the function's Terraform path `s3_object_version` and `source_code_hash`, a plan to a planfile showing 1 change and 0 to destroy, `bash .tools/safe-apply.sh`; its step 0 reads `directory_home` and the ledgers and STOPS on a mismatch or an OPEN ledger) and **Branch B** (restore the live version, named and re-read at apply, rollback per key); the red list (`deliverables/0.9.0_WK_IRPT_BCKEND~278/IB117-1_red_list.json`); the replay arms with the live contrast; the consumers (one read-through each, as before); the order condition (this release after the status-rule exercise's ledger reads CLOSED); the direct proof to run AFTER the apply; the pair: `2.0.0_SA_COO~P2`'s COO half and the CTO half, both UNSIGNED. State the apply as gated by (a) both halves signed at this packet's bytes, (b) the ledger(s) of step 2 CLOSED, (c) step 0 matching.
8. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~365/IB181-1_release_census.json` (shape of `IB171-4_release_census.json`: `{base_commit, pin_commit, uploaded:false, functions:[{function:"irpt-directory-search", built_sha256, live_sha256, built_twice_identical, built_signature_mismatched, live_signature_mismatched, built_attribute_mismatched, live_attribute_mismatched, attribute_mismatch_lines_built, attribute_mismatch_lines_live, changed_members:[{name, built_member_sha256, repo_blob_sha256_at_pin}]}]}`) and `IB181-1_step0_and_replay.json`: `{"directory_home":{...},"open_ledgers_naming_the_function":[{"ledger":"...","status":"..."}],"arms":[{"arm":"tail_of_non_head_account","verdict":"account_entry"},{"arm":"shared_tail","verdict":"two_account_entries"},{"arm":"name_query","verdict":"relationship_entry"},{"arm":"entry_without_masks","verdict":"unchanged"}],"live_contrast":[...],"reach":{"<firm>":{"entries":N,"entries_with_masks":N,"accounts":N,"accounts_tail_addressable_after":N}},"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"accounts_written":0,"figures_written":0,"vendor_requests_sent":0}`.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB181-1-AC1" cell_refs="IB-pr-515"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r181/p181_cells.py" . IB181-1-AC1</invocation><expect>IB181-1-AC1 PASS</expect></criterion>
<criterion id="IB181-1-AC2" cell_refs="IB-pr-515"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r181/p181_cells.py" . IB181-1-AC2</invocation><expect>IB181-1-AC2 PASS</expect></criterion>
<criterion id="IB181-1-AC3" cell_refs="IB-pr-515"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r181/p181_cells.py" . IB181-1-AC3</invocation><expect>IB181-1-AC3 PASS</expect></criterion>

<expected_criteria>IB181-1-AC1, IB181-1-AC2, IB181-1-AC3</expected_criteria>

What the checks grade: AC1 the census (built twice identical, 0 signature mismatches, attribute mismatches not above live's and a subset of its lines, the live sha256 equals the source map's last deployed CodeSha256, `handler.py` the ONLY changed member and equal to the repo blob at the pin, `uploaded` false); AC2 the packet exists with Branch A, Branch B, the red list, the live and built sha256, both halves, the rollback, the open-ledger sequencing, the superseded `IB-pr-499`, and the CURRENT live CodeSha256 (`tvrsQ+w820jp...`); AC3 `directory_home` recorded with a boolean `match`, the ledger list, the four replay arms exactly as above, the reach for three firms, no long digit run, the six bound counters 0. A `match` of false does NOT fail AC3 (it is the finding); it is a row and a STOP for the apply. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and the scratch directory. BUILD ONLY. **Nothing is uploaded, applied or deployed**: no `aws lambda update-function-code`, no `aws s3 cp` to a bucket, no `terraform`, no write to `infra/aws/lambda/ci/lambda-source-map.json`, no change-management entry, no Lambda invoke, no sign-in, no vendor call. Allowed AWS calls (READ): `lambda get-function`, `lambda get-function-configuration`, `iam get-role-policy`/`list-attached-role-policies`/`get-policy-version`, and the in-memory landed-directory reads of the prior order.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a changed member beyond `handler.py`; a signature mismatch, or an attribute mismatch the live zip does not carry; a build not byte-identical twice; a live zip whose sha256 differs from the source map's `artifact_sha256`; a live zip you cannot fetch. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W365-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition; ASCII only. Report once, under 150 words.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~365/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-515.directory-search-recensus-against-current-live-and-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 173 (round 181, workstream ~P), cell `IB-pr-515`.
<owned_cells>IB-pr-515</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB181-1-AC1, IB181-1-AC2, IB181-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~365/IRPT_BCKEND.TO-IB-pr-515.directory-search-recensus-against-current-live-and-packet.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- BUILD ONLY: the order builds a candidate of one Lambda in scratch and reads the live function; nothing is uploaded or applied; the consumers of the search results are read in the packet (the portal's client search and the function's other readers).
comp-iam: RUN -- no permission change; step 0 READS the function's role grants to say which directory home it may read.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p181_cells.py dry-run at base on dell2 2026-10-13 ~16:1xZ: IB181-1 AC1, AC2, AC3 FAIL (no record). Positive control: synthetic records in a path the run created itself (live sha256 taken from the source map, handler.py the only changed member, a packet carrying the current live prefix, four arms, three firms) pass all three, and the path was removed.
lane: the paths block IS the grant; worker slot ~365 of IRPT_BCKEND. Class SERVED.
</preflight>
