# TO IRPT_BCKEND.TO-IB-pr-499 -- `irpt-directory-search` rebuilt with the tail-to-ACCOUNT search, its reach, and its never-widen packet (row D2-S28)

<to_id>IRPT_BCKEND.TO-IB-pr-499</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~349</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>171</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-171 ANALYSIS (msg 6764) section 2 item 2 ("the last-four ACCOUNT entry") and the DSGN_IRPTV1 ROUND-31 ANALYSIS section 2a (row D2-S28) | **Decomp cell:** `IB-pr-499` (decomposition section 163) | **outcome_ref:** FWD-3

---

## WORKER FACE

**AMENDMENT 1 (issuer, 2026-10-13T03:3xZ; your row S1 was right).** The signature instrument reads ONE attribute mismatch on the BUILT zip and the SAME one on the LIVE zip: the staged `_authz/served.py` (pin `74a62fb46c`) passes `load_report_owner` to `enforce.Enforcer`, whose staged pin lacks that keyword. It predates this order, it is identical in the live bundle, and the path is dead in this function: `served.py` reaches it only when `render_ports` is not None, and this function's entry never passes `render_ports` (the issuer read the entry and grepped the function's folder: no match). So do NOT stop on it. Instead: record in the census `built_signature_mismatched` 0 and `live_signature_mismatched` 0, `built_attribute_mismatched` and `live_attribute_mismatched` (integers; built not above live), and `attribute_mismatch_lines_built` and `attribute_mismatch_lines_live` (the instrument's ATTR_MISMATCH lines, as lists; every built line must be a live line). STOP only on a signature mismatch or an attribute mismatch the LIVE zip does not carry. In the packet state this latent mismatch, why it is unreachable here, and that the pin pair's repair is a SEPARATE later cell (the issuer's): never repaired inside this release, because that would widen it. Your inherited commit is your build; continue from it (do not rebuild unless a hash disagrees).

Root: your worktree (`git rev-parse --show-toplevel`); work only there; `git rev-parse HEAD` before your first commit is `base_commit` (state it).

**Client data rule.** No account id, name, balance or number longer than 8 digits goes in any tracked file: counts, sha256 and reason codes only. Extracted zips and any landed-directory object stay in memory or OUTSIDE the worktree (`C:/dev/_scratch349/`), deleted file by file at the end.

**HARD BOUNDS.** BUILD ONLY. **Nothing is uploaded, applied or deployed**: no `aws lambda update-function-code`, no `aws s3 cp` to a bucket, no `terraform`, no write to `infra/aws/lambda/ci/lambda-source-map.json`, no change-management entry. Allowed AWS calls: `aws lambda get-function` (to fetch the LIVE zip), and S3 GET/LIST of the landed DIRECTORY object per firm (read-only, counts only). No Lambda is invoked, nobody signs in, no vendor call. Applying comes later, by an order to `0.7.0_AE_CloudOps~IB2`, once the pair is signed.

**Why.** `IB-pr-492` (merged) made `infra/aws/lambda/investor-reporting/directory/handler.py` return an ACCOUNT entry when a search query matches an account's tail (the head's or any other's), two accounts sharing a tail give two entries, and `resolve` accepts the synthesized entry id. This MOVES a served behaviour (what a last-four search returns and how a pick resolves; no figure moves), so it ships under ONE never-widen pair. The function is `irpt-directory-search` (`infra/aws/lambda/ci/lambda-source-map.json`, entry `irpt-directory-search`; its `source_dir` `infra/aws/lambda/investor-reporting/directory` is shared with `irpt-directory-refresh`, which this order does NOT touch). This order builds the artifact and writes the packet; it does not apply.

**Read first (the prior art, same shape):** `deliverables/0.9.0_WK_IRPT_BCKEND~337/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-482.md` and the scripts it was built with, `deliverables/0.9.0_WK_IRPT_BCKEND~278/` (`signature_closure_attr.py`, `IB117-1_red_list.json`, `make_candidate_map.py`), `deliverables/0.9.0_WK_IRPT_BCKEND~272/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-409.md`. Copy what you need into YOUR folder; edit none of theirs.

**Build:**
1. **The pin and the candidate map.** `pin_commit` is `base_commit`. Read the `irpt-directory-search` entry: `handler.py` is either a `files[]` member read from `source_dir` at the workspace HEAD, or a `staged_from` row with a pin. If it is a staged row, make a CANDIDATE copy of the map in your folder in which ONLY that row's pin moves to `pin_commit` (and its `sha256` is the blob's at the pin); if it comes from `source_dir`, no map change is needed (say which). Build with `BUILD_ONLY=1 [BAU_SOURCE_MAP_OVERRIDE=<your candidate map>] bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-directory-search` (read `infra/aws/lambda/ci/tests/test_build_only.sh`; the real source map must stay byte-identical, show it by hash before and after). Pack TWICE to byte-identical output; upload nothing.
2. **The zip carries the merged bytes, and ONLY the intended change.** Unzip to scratch; the changed members hash, as built, EQUAL to `git show <pin_commit>:<path>`. Fetch the LIVE zip (`aws lambda get-function`, `Code.Location`) to scratch; `live_sha256` is its sha256; list which members differ from the built zip. **`changed_members` must be exactly `handler.py`.** Any other differing member (another unreleased change) is a STOP: file a row naming it, change nothing more, report; do not widen the release.
3. **Both limbs of the signature instrument** read 0 SIGNATURE mismatches on the built zip and no attribute mismatch beyond the live zip's (see AMENDMENT 1) (`deliverables/0.9.0_WK_IRPT_BCKEND~278/signature_closure_attr.py`); run it on the LIVE zip too.
4. **The replay arms on the BUILT bytes.** Import the BUILT zip's `handler.py` from scratch and run it over a SYNTHETIC directory (opaque ids made up, no real data; see `directory/tests/test_tail_account_entry.py` for the shapes): (a) a query equal to the tail of a NON-head account: `account_entry`; (b) a tail shared by two accounts of two entries: `two_account_entries`; (c) a name query: `relationship_entry`; (d) an entry with no `account_masks`: `unchanged`. Run the same four against the LIVE zip's `handler.py` as the contrast. Record in `IB171-4_reach_and_arms.json`: `{arms:[{arm:"tail_of_non_head_account", verdict:"account_entry"}, {arm:"shared_tail", verdict:"two_account_entries"}, {arm:"name_query", verdict:"relationship_entry"}, {arm:"entry_without_masks", verdict:"unchanged"}], live_contrast:[...], reach:{...}, functions_invoked:0, sign_ins_made:0, aws_writes_made:0, accounts_written:0, figures_written:0, vendor_requests_sent:0}`.
5. **The REACH, read-only, per firm** (`49financial`, `cottonwood`, `inflection`): read each firm's landed directory object the way `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` `_directory_account_ids` does (the firm bucket from `hs.firm_bucket_map()`, `<prefix>/latest.json`, then `pointer["key"]`; read it in memory only; `sys.path` to that folder; if a firm has no landed directory, record its numbers as 0 and say so in `not_established`). For each firm count, as integers: `entries`, `entries_with_masks` (entries carrying a non-empty `account_masks`), `accounts` (unique account ids), `accounts_tail_addressable_after` (unique accounts in entries with masks, each of which a tail query now reaches as its own ACCOUNT entry, plus the accounts of entries without masks, which stay head-addressable only through their entry). Put them under `reach` as `{"49financial": {...}, "cottonwood": {...}, "inflection": {...}}`. Counts only; no id, name or example.
6. **The census** `IB171-4_release_census.json`: `{base_commit, pin_commit, uploaded:false, functions:[{function:"irpt-directory-search", built_sha256, live_sha256, built_twice_identical:true, built_signature_mismatched:0, live_signature_mismatched:0, built_attribute_mismatched:<int>, live_attribute_mismatched:<int>, attribute_mismatch_lines_built:[...], attribute_mismatch_lines_live:[...], changed_members:[{name, built_member_sha256, repo_blob_sha256_at_pin}]}]}`.
7. **The packet** `deliverables/0.9.0_WK_IRPT_BCKEND~349/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-499.md`, in IB-pr-482's form: the served change in words (a tail query returns ACCOUNT entries; a pick of one resolves to that one account; the relationship entry still returns on a name match and still resolves to all its accounts; permission is unchanged: the synthesized entries carry only accounts the viewer is already permitted, so nothing is widened); the live and built sha256 and the changed member; **the reach per firm** as a table; **Branch A** (land it, digest-gated, never a mint) and **Branch B** (restore the live version, named and re-read at apply, with the rollback per key); the ADDENDUM 18 red list (`IB117-1_red_list.json`) showing `handler.py` touches none of its targets; the replay arms with the live contrast; the consumers of the search results (the portal's client search reads `scope_kind` and `entry_id`: cite the portal reader file:line, one read-through each); the direct proof to run AFTER the apply (one search by an account tail through the function's own handler on a synthetic directory, no live data); the pair: `2.0.0_SA_COO~P2`'s COO half and the CTO half.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB171-4-AC1" cell_refs="IB-pr-499"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-4-AC1</invocation><expect>IB171-4-AC1 PASS</expect></criterion>
<criterion id="IB171-4-AC2" cell_refs="IB-pr-499"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-4-AC2</invocation><expect>IB171-4-AC2 PASS</expect></criterion>
<criterion id="IB171-4-AC3" cell_refs="IB-pr-499"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-4-AC3</invocation><expect>IB171-4-AC3 PASS</expect></criterion>

<expected_criteria>IB171-4-AC1, IB171-4-AC2, IB171-4-AC3</expected_criteria>

What the checks grade: AC1 the census (the function `irpt-directory-search`, built twice identical, 0 signature mismatches, attribute mismatches no more than the live zip's and a subset of its lines, the built member hashes equal the repo blobs at the pin, `handler.py` among the changed members, `uploaded` false); AC2 the packet exists with Branch A, Branch B, the red list, the live and built sha256, the COO half and the rollback; AC3 the four replay arms read exactly as stated, `reach` is present per firm with integer counts and no long digit run, and the six bound counters read 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and nothing else. No upload, apply, deploy, source-map write, invoke or vendor call; S3 access is GET/LIST of the landed directory objects only, in memory.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a changed member beyond `handler.py`; a signature or attribute mismatch; a build that is not byte-identical twice; a live zip you cannot fetch; an AWS read refused (say the error code, never a key). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W349-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition; ASCII only. Report once, under 150 words, counts only.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~349/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-499.directory-search-built-and-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 163 (round 171, workstream ~P), cell `IB-pr-499`.
<owned_cells>IB-pr-499</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB171-4-AC1, IB171-4-AC2, IB171-4-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~349/IRPT_BCKEND.TO-IB-pr-499.directory-search-built-and-packet.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- BUILD ONLY: builds a candidate zip locally from a candidate source map in the worker's folder; the real source map, S3 artifacts, Lambda and Terraform are untouched; reads: one `get-function` and the landed directory object of each of three firm buckets, in memory, counts only (SERVED class: it reads served client-directory data). The APPLY is a later order under a never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; an AccessDenied is a STOP, never a request for a grant.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched (`directory/search` and `directory/resolve` keep their shapes).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p171_cells.py dry-run at base on dell2 2026-10-13 ~04:0xZ: IB171-4 AC1, AC2 and AC3 FAIL (no census, no packet, no record). Not run: the build itself; whether other members of `irpt-directory-search` differ from the live zip (unmeasured: the order makes that a STOP).
lane: the paths block IS the grant; worker slot ~349 of IRPT_BCKEND. Class SERVED.
</preflight>
