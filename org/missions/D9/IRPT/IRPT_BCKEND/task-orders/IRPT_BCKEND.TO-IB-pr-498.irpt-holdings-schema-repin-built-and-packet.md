# TO IRPT_BCKEND.TO-IB-pr-498 -- `irpt-holdings` rebuilt with the HoldingsSnapshot schema that admits `account_id`, and its never-widen packet (the CVO's v0.52 order condition, part 1)

<to_id>IRPT_BCKEND.TO-IB-pr-498</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~348</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>171</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-171 ANALYSIS (msg 6764) section 1 row D2-W344-S1 ("BOTH packaged copies re-pin and deploy BEFORE the builder first writes `account_id`") and section 2 item 2; the CVO's v0.52 review | **Decomp cell:** `IB-pr-498` (decomposition section 163) | **outcome_ref:** FWD-3

---

## WORKER FACE

**AMENDMENT 1 (issuer, 2026-10-13T03:3xZ; your row S1 was right).** The signature instrument reads ONE attribute mismatch on the BUILT zip and the SAME one on the LIVE zip: the staged `_authz/served.py` (pin `74a62fb46c`) passes `load_report_owner` to `enforce.Enforcer`, whose staged pin lacks that keyword. It predates this order, it is identical in the live bundle, and the path is dead in this function: `served.py` reaches it only when `render_ports` is not None, and this function's entry never passes `render_ports` (the issuer read the entry and grepped the function's folder: no match). So do NOT stop on it. Instead: record in the census `built_signature_mismatched` 0 and `live_signature_mismatched` 0, `built_attribute_mismatched` and `live_attribute_mismatched` (integers; built not above live), and `attribute_mismatch_lines_built` and `attribute_mismatch_lines_live` (the instrument's ATTR_MISMATCH lines, as lists; every built line must be a live line). STOP only on a signature mismatch or an attribute mismatch the LIVE zip does not carry. In the packet state this latent mismatch, why it is unreachable here, and that the pin pair's repair is a SEPARATE later cell (the issuer's): never repaired inside this release, because that would widen it. Your inherited commit is your build; continue from it (do not rebuild unless a hash disagrees).

Root: your worktree (`git rev-parse --show-toplevel`); work only there; `git rev-parse HEAD` before your first commit is `base_commit` (state it).

**Client data rule.** No account id, balance or figure goes in any tracked file: counts, sha256 and reason codes only. Extracted zips and any scratch stay OUTSIDE the worktree (`C:/dev/_scratch348/`) and are deleted file by file at the end with a short bounded script.

**HARD BOUNDS.** BUILD ONLY. **Nothing is uploaded, applied or deployed**: no `aws lambda update-function-code`, no `aws s3 cp` to a bucket, no `terraform`, no write to `infra/aws/lambda/ci/lambda-source-map.json`, no change-management entry. Allowed AWS calls: `aws lambda get-function` (to fetch the LIVE zip's code location and download it to scratch). No Lambda is invoked, nobody signs in, no vendor call, no S3 read of client data. Applying comes later, by an order to `0.7.0_AE_CloudOps~IB2`, once the pair is signed.

**Why.** PRD v0.52 (`prd/IRPT_BCKEND_PRD.md` ADDENDUM v0.52) names an optional `account_id` on `HoldingsSnapshot` ACCOUNT nodes; the schema copies carry it (merged: `IB-pr-493`; the docs copy is `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`). The node schema has `additionalProperties: false` and the Lambda validates the snapshot at serve against its PACKAGED copy, so a snapshot carrying `account_id` is REFUSED by a function whose packaged copy is the old one. The function `irpt-holdings` (`infra/aws/lambda/ci/lambda-source-map.json`, entry `irpt-holdings`) stages that file as `contracts/HoldingsSnapshot.schema.json` from a `staged_from` row pinned to an OLD commit (read the row: `repo_path` `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`, its `pin`, `packaged_as`, `sha256`). So the pin is stale by design: the pair's apply order re-pins it, and this order builds that artifact and writes the packet. Order condition (the CVO): this deploy lands BEFORE the builder first writes `account_id`. The function `irpt-ycharts-generate` stages the same file and is NOT this order's (it waits for IRPT_ANLREQ's reader release).

**Read first (the prior art, same shape):** `deliverables/0.9.0_WK_IRPT_BCKEND~337/` (`NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-482.md`, `make_candidate_map*.py` or the candidate map it wrote, the build and census scripts), `deliverables/0.9.0_WK_IRPT_BCKEND~278/` (`signature_closure_attr.py`, `IB117-1_red_list.json`, `make_candidate_map.py`, `make_packet_416.py`) and `deliverables/0.9.0_WK_IRPT_BCKEND~272/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-409.md`. Copy what you need into YOUR folder; edit none of theirs.

**Build:**
1. **The pin and the candidate map.** `pin_commit` is `base_commit`. Make a CANDIDATE copy of `lambda-source-map.json` in your folder in which ONLY the `irpt-holdings` `staged_from` row for `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` is moved to `pin_commit` and its `sha256` set to the sha256 of the blob `git show <pin_commit>:docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`; every other row keeps its pin. Build with `BUILD_ONLY=1 BAU_SOURCE_MAP_OVERRIDE=<your candidate map> bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-holdings` (read `infra/aws/lambda/ci/tests/test_build_only.sh` for the exact use; the real source map must stay byte-identical: show it by hash before and after). Pack TWICE to byte-identical output; upload nothing.
2. **The zip carries the merged bytes, and ONLY the intended change.** Unzip the built zip to scratch; the changed members hash, as built, EQUAL to `git show <pin_commit>:<path>` (list each as `{name, built_member_sha256, repo_blob_sha256_at_pin}`). Fetch the LIVE zip (`aws lambda get-function`, `Code.Location`) to scratch; record its sha256 as `live_sha256` and list which members differ from the built zip. **`changed_members` must be exactly the packaged schema (`contracts/HoldingsSnapshot.schema.json`).** A member that differs and is not intended (another unreleased change in `files[]` or a staged row) is a STOP: file a row naming the member, change nothing more, and report; do not widen the release and do not edit a pin other than the one named.
3. **Both limbs of the signature instrument** read 0 SIGNATURE mismatches on the built zip and no attribute mismatch beyond the live zip's (see AMENDMENT 1) (`deliverables/0.9.0_WK_IRPT_BCKEND~278/signature_closure_attr.py`); run it on the LIVE zip too and record both readings.
4. **The replay arms on the BUILT bytes.** With `jsonschema` (Draft 2020-12), validate against the built zip's packaged `contracts/HoldingsSnapshot.schema.json`: (a) the instance of `infra/aws/lambda/investor-reporting/_contracts/fixtures/HoldingsSnapshot.valid.json` (it carries `account_id` on its ACCOUNT node): `valid`; (b) the same instance with `account_id` removed from the node: `valid`; (c) the same instance with a node member `unknown_member` added: `refused`. Run the same three against the LIVE zip's packaged copy as the contrast (expected: (a) refused, (b) valid, (c) refused). Record them in `IB171-3_replay_arms.json`: `{arms:[{arm:"node_with_account_id", verdict:"valid"}, {arm:"node_without_account_id", verdict:"valid"}, {arm:"node_with_unknown_member", verdict:"refused"}], live_contrast:[...same arms with the live verdicts...], served_figures_changed: 0, functions_invoked:0, sign_ins_made:0, aws_writes_made:0, accounts_written:0, figures_written:0, vendor_requests_sent:0}`.
5. **The census** `IB171-3_release_census.json`: `{base_commit, pin_commit, uploaded:false, functions:[{function:"irpt-holdings", built_sha256, live_sha256, built_twice_identical:true, built_signature_mismatched:0, live_signature_mismatched:0, built_attribute_mismatched:<int>, live_attribute_mismatched:<int>, attribute_mismatch_lines_built:[...], attribute_mismatch_lines_live:[...], changed_members:[{name, built_member_sha256, repo_blob_sha256_at_pin}]}]}`. (`built_sha256` and `live_sha256` are 64-hex sha256 of the zip files, as the round-167 census recorded them.)
6. **The packet** `deliverables/0.9.0_WK_IRPT_BCKEND~348/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-498.md`, in IB-pr-482's form, with: the served change in words (a serve-time validator that admits one more OPTIONAL member; nothing is served differently until the builder first writes `account_id`; no figure moves); the live and built sha256 and the changed member; **Branch A** (land it, digest-gated, never a mint) and **Branch B** (restore the live version, named and re-read at apply, with the rollback per key); the ADDENDUM 18 red list (`IB117-1_red_list.json`) showing your member touches none of its targets; the replay arms with the live contrast; the CONSUMERS of `contracts/HoldingsSnapshot.schema.json` inside this function (cite file:line of each reader, one read-through each); the order condition (this deploy BEFORE the builder writes `account_id`); the direct proof to run AFTER the apply (the function validates the valid fixture with and without `account_id`, by the function's own validator, no live data); the pair: `2.0.0_SA_COO~P2`'s COO half and the CTO half.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB171-3-AC1" cell_refs="IB-pr-498"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-3-AC1</invocation><expect>IB171-3-AC1 PASS</expect></criterion>
<criterion id="IB171-3-AC2" cell_refs="IB-pr-498"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-3-AC2</invocation><expect>IB171-3-AC2 PASS</expect></criterion>
<criterion id="IB171-3-AC3" cell_refs="IB-pr-498"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-3-AC3</invocation><expect>IB171-3-AC3 PASS</expect></criterion>

<expected_criteria>IB171-3-AC1, IB171-3-AC2, IB171-3-AC3</expected_criteria>

What the checks grade: AC1 the census (the function `irpt-holdings`, built twice identical, 0 signature mismatches, attribute mismatches no more than the live zip's and a subset of its lines, the built member hashes equal the repo blobs at the pin, the schema copy among the changed members, `uploaded` false); AC2 the packet exists with Branch A, Branch B, the red list, the live and built sha256, the COO half and the rollback; AC3 the replay arms read exactly valid / valid / refused, `served_figures_changed` 0, the six bound counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and nothing else. No upload, apply, deploy, source-map write, invoke or vendor call.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a changed member beyond the schema copy; a signature or attribute mismatch on the built zip; a build that is not byte-identical twice; a live zip you cannot fetch; the schema copies not byte-identical at the pin. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W348-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition; ASCII only. Report once, under 150 words.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~348/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-498.irpt-holdings-schema-repin-built-and-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 163 (round 171, workstream ~P), cell `IB-pr-498`.
<owned_cells>IB-pr-498</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB171-3-AC1, IB171-3-AC2, IB171-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~348/IRPT_BCKEND.TO-IB-pr-498.irpt-holdings-schema-repin-built-and-packet.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- BUILD ONLY: builds a candidate zip locally from a candidate source map in the worker's folder; the real source map, S3, Lambda and Terraform are untouched; one read-only `get-function` to fetch the live zip. The APPLY is a later order under a never-widen pair (a serve-time validator change).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p171_cells.py dry-run at base on dell2 2026-10-13 ~04:0xZ: IB171-3 AC1, AC2 and AC3 FAIL (no census, no packet, no replay record). Not run: the build itself; whether other members of `irpt-holdings` differ from the live zip (unmeasured: the order makes that a STOP).
lane: the paths block IS the grant; worker slot ~348 of IRPT_BCKEND. Class WORLD (the `infra/` floor; build only).
</preflight>
