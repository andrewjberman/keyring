# TO IRPT_BCKEND.TO-IB-pr-545 -- RE-RUN the live-against-pin differential on the BUILT bundles at release pin 2: 32 and 841 unchanged, every Cottonwood change the signed cash rule alone, same-state gate, READ ONLY (CTO round-197 ruling 2)

<to_id>IRPT_BCKEND.TO-IB-pr-545</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~390</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>197</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-197 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_P_ROUND_197_20261014.md` | **Decomp cell:** `IB-pr-545` (decomposition section 189) | **outcome_ref:** FWD-3 | **Depends on:** `IB-pr-544` merged

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-390`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~390 <0.9.0_WK_IRPT_BCKEND~390@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object names, field names, classification labels and public security symbols only in any tracked file; no account id, client id, node id, quantity or holding name; the largest delta is a NUMBER with its field name and no id. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch390/`); a recursive delete the harness refuses is left and named in your report.

**Cell `IB-pr-545` (inlined).** Round 196's built-bundle differential (`deliverables/0.9.0_WK_IRPT_BCKEND~386/`, harness `built_bundle_differential.py` and record `IB196-2_built_differential.json`, READ BOTH FIRST) measured 32 / 485 / 841 with the CUSIP port in. The CTO ruled the release ships WITHOUT the port: pin 2 = `5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f`. **Repeat that differential with the BUILT side = the bundle `core.build_bundle_payload` makes at pin 2** (the live side = the live bundle bytes as downloaded, as before). Expected: 49financial EXACTLY 32 and Inflection EXACTLY 841, and Cottonwood 485 less the 232 the port explained: about 253 nodes, ALL of them the signed cash rule (the 4 nodes the round-196 toggle left overdetermined are cash-rule movers again once the port is out). **Every remaining change must attribute to the cash rule alone; any other group is UNATTRIBUTED, a STOP.** It mints, uploads, applies and signs NOTHING.

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`. `git worktree add --detach C:/dev/wk-ib545-pin 5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f`. Download the three live bundles by version id (49financial `UHOCIkWj3QiIzNucG1VjNnk_AufIg6oD`, cottonwood `oyIYMVdh_l2zCg5ZWvn3ISPPS6_9Q82_`, inflection `PzhCs97qVBXkZcIjaOklHmzWiFsOFafM`; bucket `opal-data-<firm>`, key `irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz`) with `s3api get-object --version-id`, untar into `C:/dev/_scratch390/live/<firm>/`; build each firm's bundle payload from the pin-2 tree (`core.find_bundle(...)`, `core.build_bundle_payload(b)`, its own `.tools` first on `sys.path`) and untar into `C:/dev/_scratch390/built/<firm>/`.
2. **The harness** `deliverables/0.9.0_WK_IRPT_BCKEND~390/built_bundle_differential_pin2.py` (committed; read only): start from round 196's `built_bundle_differential.py` with the built side = the pin-2 trees (one subprocess per tree per firm, `python -I`, assert the imported file lies under its tree, the built tree first then the live tree on the same pre-seeded receipts, per-node signatures, rows, account set, numeric leaves with absolute tolerance 0.01 and the largest delta, the four classification fields, the identity-patch build for the signed cash rule). Custody pins: 49financial 2026-10-12, cottonwood 2026-10-12, inflection 2026-10-13.
3. **The same-state gate.** As in round 196: read each firm's served publication ONCE (`HoldingsPublication(...).begin()` and `served_publication`, read calls only) and evaluate each code's `evaluate_publish_gate` against THAT one state; `gate.served_state` = `{"latest_date":..,"manifest_version":..}`; `gate.attribution` is `same`, or `signed_exemption_repair` on Cottonwood only; anything else is a STOP.
4. **Counts.** Per firm `total_changed_nodes` and the `differences` list (`group` = `<field>: <from> -> <to>`, `nodes`, `attribution` `signed_cash_rule`, `attributed_by` `identity-patch`). **49financial must total EXACTLY 32 and Inflection EXACTLY 841 with no other group; Cottonwood's total must equal its signed-cash-rule nodes (the identity-patch count at pin 2, expected about 253) with NO other group.** Any other number or group is a STOP: record it, report it, and write the rest up to it.
5. **Determinism and the mutant (per firm).** Run the comparison TWICE (fresh pairs of builds on the same receipts): `run1_digest` and `run2_digest` = sha256 over the canonical JSON (sorted keys, compact) of the comparison result, equal. Plant a MUTANT (one `asset_class` value changed in the built side's signature) and re-run the comparison step only: `mutant` = `{"flagged":true,"changed_nodes_with_mutant":<total_changed_nodes + 1>}` as MEASURED.
6. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~390/IB197-2_built_differential.json`: `{"base_commit":"<40hex>","new_pin":"5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f","custody_pins":{"49financial":"2026-10-12","cottonwood":"2026-10-12","inflection":"2026-10-13"},"live_versions":{"49financial":"..","cottonwood":"..","inflection":".."},"firms":{"<firm>":{"rows":{"live":{"<kind>":n},"built":{..}},"account_set":{"only_live":n,"only_built":n,"both":n},"changed_values":{"tolerance":0.01,"nodes_with_changed_numeric_value":n,"largest_abs_delta":x,"largest_delta_field":".."},"gate":{"served_state":{..},"live":{..},"built":{..},"attribution":".."},"total_changed_nodes":n,"differences":[..],"built_from":"core.build_bundle_payload at pin 2","built_bundle_members":n,"run1_digest":"..","run2_digest":"..","mutant":{..}}},"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB197-2_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove the worktrees and scratch you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB197-2-AC1" cell_refs="IB-pr-545"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py" . IB197-2-AC1</invocation><expect>IB197-2-AC1 PASS</expect></criterion>
<criterion id="IB197-2-AC2" cell_refs="IB-pr-545"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py" . IB197-2-AC2</invocation><expect>IB197-2-AC2 PASS</expect></criterion>
<criterion id="IB197-2-AC3" cell_refs="IB-pr-545"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py" . IB197-2-AC3</invocation><expect>IB197-2-AC3 PASS</expect></criterion>

<expected_criteria>IB197-2-AC1, IB197-2-AC2, IB197-2-AC3</expected_criteria>

What the checks grade: AC1 per firm the rows, account set, changed values, the gate on both sides against ONE served state (a difference only as the signed exemption repair on Cottonwood), every difference group the signed cash rule, 49financial EXACTLY 32 and Inflection EXACTLY 841, Cottonwood's groups covering its total with that total between 249 and 260; AC2 `new_pin` equal to IB-pr-544's, the signed custody pins and live version ids, the build input named as the built bundle at pin 2 (at least 46 members), ONE digest from two runs and a mutant flagged as exactly one more changed node; AC3 notes, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktrees and the scratch directory outside the repository. READ ONLY. **Nothing is minted, invoked, written to AWS, uploaded, applied, deployed, signed or sent:** the only AWS calls are `s3api get-object` on live bundle keys by version id and the harness's get/list reads with your identity. A denial is recorded, never worked around or widened. (AWS CLI goes through the `.tools/aws` shim.)
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; 49financial not exactly 32 or Inflection not exactly 841; any Cottonwood group that is not the signed cash rule; a gate difference that is not the signed exemption repair on Cottonwood; two runs that disagree after you ruled out a harness defect; a client identifier or node id in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W390-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~390/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 189 (round 197, workstream ~P), cell `IB-pr-545`.
<owned_cells>IB-pr-545</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB197-2-AC1, IB197-2-AC2, IB197-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~390/IRPT_BCKEND.TO-IB-pr-545.built-bundle-differential-at-pin-2-cash-rule-only.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order downloads the three live bundle objects by version id, builds three bundle payloads in memory at pin 2, builds candidates in memory from versioned source reads under both code sides (twice per firm) and reads each firm's served publication once; it writes only the worker's records; the release it measures is a later order under packet v3's two signed halves
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p197_cells.py IB197-2 dry-run at base on dell2 2026-10-14 ~22:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a throwaway git repo the run created itself (synthetic records in the shapes above; removed): all three PASS; eight negatives across IB197-2, each failing its own arm: a beyond-rule Cottonwood group, 49financial not reproducing 32, Cottonwood still at 485, a gate difference called nothing, a pin that is not IB-pr-544's, a build input that is not the built bundle, two digests, a counter above 0.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~390` (worktree `C:/dev/wk-IRPT_BCKEND-390`). Class SERVED (reads the live bundles and builds candidates from served sources; writes only the worker's records).
</preflight>
