# TO IRPT_BCKEND.TO-IB-pr-541 -- RE-RUN the live-against-pin differential on the BUILT bundles (live bundle bytes against the new pin's bundle bytes) with a same-state gate comparison; 32 and 841 must reproduce, READ ONLY (CTO round-196 analysis cell 2 @51675bfa49; rows D2-W384-S1, D2-W384-S2, D2-S175)

<to_id>IRPT_BCKEND.TO-IB-pr-541</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~386</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>196</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-196 analysis section 2 item 2 | **Decomp cell:** `IB-pr-541` (decomposition section 188) | **outcome_ref:** FWD-3 | **Depends on:** `IB-pr-540` merged (its record names `new_pin`)

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-386`, cut from the current branch AFTER `IB-pr-540` merged (so `deliverables/0.9.0_WK_IRPT_BCKEND~385/IB196-1_closure_record.json` is in it and `new_pin` resolves). Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~386 <0.9.0_WK_IRPT_BCKEND~386@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, object names, field names, classification labels and public symbols only in any tracked file; no account id, client id, node id, quantity or holding name; the largest delta is a NUMBER with its field name and no id. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch386/`); a recursive delete the harness refuses is left and named in your report.

**Cell `IB-pr-541` (inlined).** Round 195's differential (`deliverables/0.9.0_WK_IRPT_BCKEND~384/`, harness `live_pin_differential.py` and record `IB195-1_differential_record.json`, READ THEM FIRST) ran the pin's code from the full repository tree, which hid that the pin's bundle closure lacked a member (`IB-pr-540` fixed it into `new_pin`). **For a release, the bundle is the build input (CLAUDE.md 22a). This order repeats the differential with BOTH sides as BUNDLES: the live bundle bytes as downloaded, against the bundle `core.build_bundle_payload` makes at `new_pin`, extracted.** It mints, uploads, applies and signs nothing.

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`. Read the `IB196-1_closure_record.json` `new_pin`. Create the new-pin tree `git worktree add --detach C:/dev/wk-ib541-pin <new_pin>` (outside the repository). Download the three live bundles by version id (49financial `UHOCIkWj3QiIzNucG1VjNnk_AufIg6oD`, cottonwood `oyIYMVdh_l2zCg5ZWvn3ISPPS6_9Q82_`, inflection `PzhCs97qVBXkZcIjaOklHmzWiFsOFafM`; bucket `opal-data-<firm>`, key `irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz`) with `s3api get-object --version-id` and untar each into `C:/dev/_scratch386/live/<firm>/`. Build each firm's bundle payload from the new-pin tree with `core.find_bundle(...)` and `core.build_bundle_payload(b)` (put `C:/dev/wk-ib541-pin/.tools` first on `sys.path`), untar into `C:/dev/_scratch386/built/<firm>/`. `built_bundle_members` = the files in the built tree (the closure plus `SHA256SUMS`).
2. **The harness** `deliverables/0.9.0_WK_IRPT_BCKEND~386/built_bundle_differential.py` (committed; read only): start from round 195's `live_pin_differential.py` and change its two code sides to the live tree and the BUILT tree above (one subprocess per tree per firm, `python -I`, assert the imported file lies under its tree, the built tree FIRST then the live tree on the same pre-seeded source receipts, per-node signatures, rows, account set, numeric leaves with absolute tolerance 0.01 and the largest delta, the four classification fields, the identity-patch build for the signed cash rule). The S3 client wrapper refuses every operation not named `get_`, `list_` or `head_`. Custody pins: 49financial 2026-10-12, cottonwood 2026-10-12, inflection 2026-10-13.
3. **The same-state gate.** Read the firm's served publication ONCE (`HoldingsPublication(...).begin()` and `served_publication`, read calls only) and evaluate each code's `evaluate_publish_gate` against THAT one served state; record `gate.served_state` = `{"latest_date":"<the served frontier>","manifest_version":"<its version id>"}` and `gate.live` / `gate.built` = `{"outcome","conditions":[names]}`. `gate.attribution` is `same` when equal, `signed_exemption_repair` when they differ on Cottonwood only, and anything else is a STOP. (A candidate dated before the served frontier reads REFUSED on `source_frontier_older` on BOTH sides; that is the clock, not the code, and is recorded as measured.)
4. **Counts.** Per firm `total_changed_nodes`, and the `differences` list (one entry per field group, `group` = `<field>: <from> -> <to>`, `nodes`). The signed cash rule (`attribution` `signed_cash_rule`, `attributed_by` `identity-patch`) must equal 32 / 249 / 841. **49financial must total EXACTLY 32 and Inflection EXACTLY 841 with no other group; any other number is a STOP: record it, report it, and write the rest up to it.** On Cottonwood every group that is not the signed rule is `attribution` `TO_IB-pr-542` (that order attributes them) and `beyond_rule_nodes` counts their distinct nodes.
5. **Determinism and the mutant (per firm).** Run the comparison TWICE (two fresh pairs of builds on the same receipts): `run1_digest` and `run2_digest` = sha256 over the canonical JSON (sorted keys, compact) of the comparison result, equal. Plant a MUTANT (one `asset_class` value changed in the built side's signature) and re-run the comparison step only: `mutant` = `{"flagged":true,"changed_nodes_with_mutant":<total_changed_nodes + 1>}` as MEASURED.
6. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~386/IB196-2_built_differential.json`: `{"base_commit":"<40hex>","new_pin":"<40hex>","custody_pins":{..},"live_versions":{..},"firms":{"<firm>":{"rows":{"live":{"<kind>":n},"built":{..}},"account_set":{"only_live":n,"only_built":n,"both":n},"changed_values":{"tolerance":0.01,"nodes_with_changed_numeric_value":n,"largest_abs_delta":x,"largest_delta_field":".."},"gate":{"served_state":{..},"live":{..},"built":{..},"attribution":".."},"total_changed_nodes":n,"differences":[..],"beyond_rule_nodes":n (cottonwood only),"built_from":"core.build_bundle_payload at the new pin","built_bundle_members":n,"run1_digest":"..","run2_digest":"..","mutant":{..}}},"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.
7. **Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB196-2_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (harness, record and criteria output first, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove the pin worktree and scratch. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB196-2-AC1" cell_refs="IB-pr-541"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py" . IB196-2-AC1</invocation><expect>IB196-2-AC1 PASS</expect></criterion>
<criterion id="IB196-2-AC2" cell_refs="IB-pr-541"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py" . IB196-2-AC2</invocation><expect>IB196-2-AC2 PASS</expect></criterion>
<criterion id="IB196-2-AC3" cell_refs="IB-pr-541"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py" . IB196-2-AC3</invocation><expect>IB196-2-AC3 PASS</expect></criterion>

<expected_criteria>IB196-2-AC1, IB196-2-AC2, IB196-2-AC3</expected_criteria>

What the checks grade: AC1 per firm the rows, account set, changed values, the gate on both sides against ONE served state (a difference only as the signed exemption repair on Cottonwood), the signed cash rule at 32 / 249 / 841, 49financial and Inflection totalling exactly those numbers with no other group, Cottonwood's other groups named for IB-pr-542; AC2 `new_pin` equal to IB-pr-540's, the signed custody pins and live version ids, the build input named as the built bundle (at least 46 members), ONE digest from two runs and a mutant flagged as exactly one more changed node; AC3 notes, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the new-pin tree and the scratch outside the repository. READ ONLY. **Nothing is minted, invoked, written to AWS, uploaded, applied, deployed, signed or sent:** the only AWS calls are `s3api get-object` on the three live bundle keys by version id and the harness's get/list reads with your identity. A denial is recorded, never worked around or widened. (AWS CLI goes through the `.tools/aws` shim.)
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; 49financial not exactly 32 or Inflection not exactly 841; a gate difference that is not the signed exemption repair on Cottonwood; two runs that disagree after you ruled out a harness defect; a client identifier or node id in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W386-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~386/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 188 (round 196, workstream ~P), cell `IB-pr-541`.
<owned_cells>IB-pr-541</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB196-2-AC1, IB196-2-AC2, IB196-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~386/IRPT_BCKEND.TO-IB-pr-541.built-bundle-differential-same-state-gate.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order downloads the three live bundle objects by version id, builds three bundle payloads in memory at the new pin, builds candidates in memory from versioned source reads under both code sides (twice per firm), reads each firm's served publication once; it writes only the worker's records; the release it measures is a later order under packet v3's two signed halves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity (round 195's worker read the same sources).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p196_cells.py IB196-2 dry-run at base on dell2 2026-10-14 ~17:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a throwaway git repo the run created itself (synthetic records in the shapes above; removed): all three PASS; nine negatives, each failing its own arm: 49financial not reproducing 32, an extra group on Inflection, a gate difference called nothing, no served state, a new pin that is not IB-pr-540's, a build input that is not the built bundle, two digests, a mutant not flagged, a counter above 0.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~386` (worktree `C:/dev/wk-IRPT_BCKEND-386`). Class SERVED (reads the live bundles and builds candidates from served sources; writes only the worker's records). The premises are the CTO's round-196 ruling, round 195's differential (32 / 485 / 841 on the repository tree) and the closure fix of IB-pr-540.
</preflight>
