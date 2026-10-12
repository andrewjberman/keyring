# TO IRPT_BCKEND.TO-IB-pr-482 -- BUILD ONLY: `irpt-performance-adapter` rebuilt from one pin so it carries the reader's claim-by-status change (C-CHAINCLAIM), and the never-widen packet that prints the MOVES with the reach beside them

<to_id>IRPT_BCKEND.TO-IB-pr-482</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~337</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>167</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6517 (PRD ADDENDUM v0.51 section 2 item 2; contract C-CHAINCLAIM, ADDENDUM v0.48, as amended by v0.49 section 1) | **Decomp cell:** `IB-pr-482` (decomposition section 159) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-337/` (bash `/c/dev/wk-irpt-bckend-337`). Work only there; `git rev-parse HEAD` before your first commit is `base_commit` (state it).

**Client data rule (CTO ruling @0e8209c33c item 6).** No account id, balance, fee or flow goes in any tracked file. The repo carries counts, sha256 and reason codes only. Extracted zips, cached partitions and any client data stay OUTSIDE the worktree (use `C:/dev/_scratch337/`) and are deleted file by file at the end with a short bounded script.

**HARD BOUNDS.** BUILD ONLY. **Nothing is uploaded, applied or deployed**: no `aws lambda update-function-code`, no `aws s3 cp` to a bucket, no `terraform`, no write to `lambda-source-map.json`, no change-management entry opened. Allowed AWS calls: `aws lambda get-function` (to fetch the LIVE zip's code location and download it to scratch), and S3 list/get of the served holdings gold up to the cap day 2026-10-08. No Lambda is invoked, nobody signs in, no vendor call.
Applying comes later, by an order to `0.7.0_AE_CloudOps~IB2`, once the pair is signed.

**Why.** Round 166 merged the reader's claim change and left it unbuilt: `infra/aws/lambda/investor-reporting/performance/holdings_gold.py` now sets `value_facts.claim` by the excluded day's STATUS (C-CHAINCLAIM) and carries two new integers beside `days_linked`. The reader's record is
`deliverables/0.9.0_WK_IRPT_BCKEND~331/IB166-1_reader_record.json` (read it whole, and its READ file), merged at `6a875f0dfd`. The function that carries `holdings_gold.py` is `irpt-performance-adapter` (`infra/aws/lambda/ci/lambda-source-map.json`, entry `irpt-performance-adapter`, `staged_from` members; no other function lists it). This MOVES a served value (the claim on some answers goes `measured` to `inferred`; the figures do not move), so it ships under ONE never-widen pair. This order builds the artifact and writes the packet; it does not apply.

**Read first (the prior art, same shape):** `deliverables/0.9.0_WK_IRPT_BCKEND~278/` (`NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-416.md`, `make_candidate_map.py`, `candidate_source_map.json`, `make_census_416.py`, `make_packet_416.py`, `signature_closure_attr.py`, `IB117-1_red_list.json`, `replay/`) and `deliverables/0.9.0_WK_IRPT_BCKEND~272/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-409.md`. Copy what you need into YOUR folder; edit none of theirs.

**Build:**
1. **The pin and the candidate map.** `pin_commit` is `base_commit` (the tree you stand in, which carries `6a875f0dfd`). Make a CANDIDATE copy of `lambda-source-map.json` in your folder (as `make_candidate_map.py` does) in which the `irpt-performance-adapter` `staged_from` pin of `holdings_gold.py` is moved to `pin_commit`; every other member keeps the pin it has. Build with `BUILD_ONLY=1 BAU_SOURCE_MAP_OVERRIDE=<your candidate map> bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-performance-adapter`
   (read `infra/aws/lambda/ci/tests/test_build_only.sh` for the exact use; the real source map must stay byte-identical, show it by hash before and after). Pack TWICE to byte-identical output; upload nothing.
2. **The zip carries the merged bytes.** Unzip the built zip to scratch; the changed members (at least `holdings_gold.py`) hash, as built, EQUAL to `git show <pin_commit>:<path>`. List each as `{name, built_member_sha256, repo_blob_sha256_at_pin}`. Fetch the LIVE zip (`aws lambda get-function`, `Code.Location`) to scratch; record its sha256 as `live_sha256` and list which members differ from the built zip (`changed_members` are exactly those you intend; a member that differs and is not intended is a STOP and a row).
3. **Both limbs of the signature instrument** read 0 mismatches on the built zip: `deliverables/0.9.0_WK_IRPT_BCKEND~278/signature_closure_attr.py` (its two limbs: signature and attribute-call). Run it on the LIVE zip too as the negative-control context and record both readings.
4. **The four arms on the built bytes.** Run the BUILT zip's `holdings_gold.py` (imported from scratch) over the same four synthetic frames as the round-166 test `performance/tests/test_chain_claim.py` (no-base days -> `measured`; `ALL-HOLDINGS-EXCLUDED` -> `inferred`; `NON-POSITIVE-BASE` with a prior-day position row -> `inferred`; an unnamed status -> `inferred`) and show the same four verdicts. Record them as the replay arms in `IB167-2_release_census.json`, each `identical` or `expected-diff` against the LIVE zip's reader (the claim arms are `expected-diff`; a figure arm is `identical`).
5. **The counts, at the build's pin.** Re-take the claim counts with the reader AS BUILT AT THE PIN over the served gold at the cap day 2026-10-08, both entries, windows SI, YTD, QTD, 1Y: reuse `deliverables/0.9.0_WK_IRPT_BCKEND~331/ib166_measure.py` and `ib166_assemble.py` (read them; cache partitions in scratch; bound every step; print the denominator of partitions read). Write `IB167-2_release_counts.json`:
   `{base_commit, pin_commit, counts_taken_at_pin: <pin_commit>, latest_landed_day: "2026-10-08", rule_reach:{"49F":{"SI":..,"YTD":..,"QTD":..,"1Y":..},"orion":{...}}, claim_moves:{...same shape...}, already_inferred_at_base:{...}, consumers_read_through:[{cite, reads, read_through}], functions_invoked:0, sign_ins_made:0, aws_writes_made:0, accounts_written:0, figures_written:0, vendor_requests_sent:0}`.
   The CTO's numbers, which your run must reproduce: REACH 49F SI 23, YTD 19, QTD 2, 1Y 20; orion SI 894, YTD 200, QTD 7, 1Y 240. MOVES (the accounts whose claim actually goes `measured` to `inferred`) 49F 23, 19, 2, 20; orion SI 750, YTD 76, QTD 7, 1Y 106. If a number differs, STOP on it: file a row naming the cell and both numbers and report; do not edit a threshold.
   `consumers_read_through`: every consumer of the claim and the state, with ONE read through each: take the 11 backend consumers of `IB166-1_reader_record.json` and the portal readers of `deliverables/0.9.0_WK_IRPT_BCKEND~334/IB166-4_value_facts_readers.json`, and add any you find; each `{cite, reads, read_through}`.
6. **The packet** `deliverables/0.9.0_WK_IRPT_BCKEND~337/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-482.md`, in IB-pr-409's and IB-pr-416's form, with these sections: the served change in words (the claim, the two integers, and that PARTIAL stays); live and built sha256 and the changed members; **the MOVES with the REACH beside them, per firm and window, as a table**, and the line that the pair is signed against the moves; **Branch A** (land it, digest-gated, never a mint) and **Branch B** (restore the live version, named and re-read at apply, with the rollback per key);
   the ADDENDUM 18 red list (`IB117-1_red_list.json` in the prior art) showing your members touch none of its targets; the replay arms; the consumers with their read-throughs; the direct-invoke proof to run AFTER the apply (the same four arms by direct invoke under the instrument already signed for this function family, with the figure of each unchanged from before); the pair: `2.0.0_SA_COO~P2`'s COO half and the CTO half.

<criterion id="IB167-2-AC1" cell_refs="IB-pr-482"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-2-AC1</invocation><expect>IB167-2-AC1 PASS</expect></criterion>
<criterion id="IB167-2-AC2" cell_refs="IB-pr-482"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-2-AC2</invocation><expect>IB167-2-AC2 PASS</expect></criterion>
<criterion id="IB167-2-AC3" cell_refs="IB-pr-482"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-2-AC3</invocation><expect>IB167-2-AC3 PASS</expect></criterion>

<expected_criteria>IB167-2-AC1, IB167-2-AC2, IB167-2-AC3</expected_criteria>

What the checks grade: AC1 `IB167-2_release_census.json` (shape `{base_commit, pin_commit, uploaded:false, functions:[{function:"irpt-performance-adapter", built_sha256, live_sha256, built_twice_identical:true, built_signature_mismatched:0, built_attribute_mismatched:0, changed_members:[{name, built_member_sha256, repo_blob_sha256_at_pin}], replay_arms:[...]}]}`): the built member hashes equal the repo blobs at the pin, `holdings_gold.py` among them;
AC2 the packet exists with Branch A, Branch B, the red list, the live and built sha256, the moves beside the reach, the COO half and the rollback; AC3 the counts record: reach equal to the CTO's reach, moves equal to the CTO's moves, counts taken at the pin, at least one consumer read-through with a resolving cite, the six bound counters 0.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. NO product file is edited: this order builds and writes; it does not change `holdings_gold.py` or any source. NO edit of `lambda-source-map.json`, `build-and-upload.sh` or any other file under `infra/`.
- **Refusal clause:** a changed member that is not intended, a count that differs, a signature mismatch on the built zip, an AWS read refused: file a row and report. Never weaken a check; do not edit `p167_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W337-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~337" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~337@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~337 <0.9.0_WK_IRPT_BCKEND~337@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~337/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-482.claim-and-partial-release-built-and-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 159 (round 167, workstream ~P), cell `IB-pr-482`.
<owned_cells>IB-pr-482</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB167-2-AC1, IB167-2-AC2, IB167-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~337/IRPT_BCKEND.TO-IB-pr-482.claim-and-partial-release-built-and-packet.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base and the pin; the built and live sha256 and the changed members with their hashes; both limbs' readings on the built and the live zip; the four arms on the built bytes; the eight reach and eight moves counts against the CTO's; the consumers and read-throughs; the real source map byte-identical before and after; the packet path; whether the scratch was cleaned;
each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell builds a zip into scratch and writes records under the worker's folder; nothing is uploaded, applied or deployed. The blast radius of the later apply is the packet's subject, graded by the pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; get-function and S3 list/get by the box's own identity, the reads earlier cells made.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; no route is called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p167_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~20:4xZ: IB167-2 AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The issuer read the prior art's file list (deliverables ~278 and ~272) and the source-map entry for irpt-performance-adapter (staged_from members; holdings_gold.py pinned at 361c44fa9d); it has not run the build.
lane: the <paths> block IS the grant. Class WORLD (the artifact is for a Lambda release; the L6 floor reads the order's <paths>, which name no infra path, so the class is DECLARED WORLD by the issuer for the reach of the later apply). Nothing is deployed here.
</preflight>
