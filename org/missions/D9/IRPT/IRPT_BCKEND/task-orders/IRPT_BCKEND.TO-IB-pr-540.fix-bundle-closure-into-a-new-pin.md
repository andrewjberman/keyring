# TO IRPT_BCKEND.TO-IB-pr-540 -- FIX the holdings bundle closure into a NEW pin: add the missing member, prove every closure module imports from each firm's BUILT bundle under `python -I`, and prove the closure equals the traced import set both ways (CTO round-196 analysis cell 1 @51675bfa49; row D2-W384-S1)

<to_id>IRPT_BCKEND.TO-IB-pr-540</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~385</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>196</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-196 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_P_ROUND_196_20261014.md` section 2 item 1 | **Decomp cell:** `IB-pr-540` (decomposition section 188) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-385` on a branch cut from the current branch (your deliverables go here). Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~385 <0.9.0_WK_IRPT_BCKEND~385@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read; print what a search covered before you read a zero as an absence). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected, not a finding. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, member paths and module names only in any tracked file; no account id, client id, node id, position value or holding name. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch385/`); remove what you can with `git worktree remove` and a short bounded script; a recursive delete the harness refuses is left and named in your report.

**Cell `IB-pr-540` (inlined).** The holdings producer ships to each firm only through that firm's standalone bundle, whose members are `_IRPT_HOLDINGS_CLOSURE` in `.tools/safe_deploy_core.py`. At the release pin `49467335d288d5c0012fe339c4cafcb74bd43fb5` the closure LACKS `data/assets/scripts/silver/opal_unidentified.py`, which `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py` (a member) imports at module level; the issuer built the pin's three bundle payloads with the tool's own `build_bundle_payload` (no upload), extracted them and ran each: Cottonwood raised `ModuleNotFoundError: opal_unidentified` (via `holdings_snapshot._cot_taxonomy_rules`); Inflection built. A mint from the pin would leave Cottonwood unable to publish (row D2-W384-S1). **This order makes a NEW PIN: the old pin plus exactly one closure line, and proves the class mechanically, not the one file.** It mints, uploads, applies and signs NOTHING.

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` in your worktree before your first commit is `base_commit` (state it). Read `.tools/safe_deploy_core.py` around `_IRPT_HOLDINGS_CLOSURE`, `find_bundle` and `build_bundle_payload`, and the comment above the closure (its measuring method: an `open` audit hook plus `sys.modules`).
2. **Build the new pin on a branch from the OLD pin.** `git worktree add -b pin-ib-pr-540 C:/dev/wk-ib540-pin 49467335d288d5c0012fe339c4cafcb74bd43fb5`. The worker lane admits a commit only while this order is non-terminal at that tree's HEAD, so FIRST put the order file on the branch: `git -C C:/dev/wk-IRPT_BCKEND-385 show HEAD:org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-540.fix-bundle-closure-into-a-new-pin.md > C:/dev/wk-ib540-pin/<that same path>` and commit that ONE path from `C:/dev/wk-ib540-pin` with `safe-commit.sh` (message file by the Write tool). THEN edit `.tools/safe_deploy_core.py` in `C:/dev/wk-ib540-pin`: add exactly the line `    "data/assets/scripts/silver/opal_unidentified.py",` to `_IRPT_HOLDINGS_CLOSURE` (next to `opal_strategy_matcher.py`) and, above the tuple, one comment line `# RE-MEASURED 2026-10-14 (0.9.0_WK_IRPT_BCKEND~385, IB-pr-540, row D2-W384-S1): adds silver/opal_unidentified.py (imported by build_cottonwood_mdpf_slice.py); no other change.` **No line is deleted and nothing else is added.** Commit that ONE path from `C:/dev/wk-ib540-pin` with `safe-commit.sh`. `new_pin` = that commit's hash (`git rev-parse HEAD` in the pin tree). **Leave the branch `pin-ib-pr-540` in place** (the issuer merges it); remove only the worktree at the end.
3. **Build the bundles from the new pin, no upload.** From a Python process in `C:/dev/wk-ib540-pin` (put its `.tools` first on `sys.path`, `import safe_deploy_core as core`): for `irpt_holdings_49f`, `irpt_holdings_cot`, `irpt_holdings_inf` call `core.find_bundle(name)` then `core.build_bundle_payload(b)`, untar each payload to `C:/dev/_scratch385/new/<firm>/`. Do the same at the OLD pin (a second detached worktree `git worktree add --detach C:/dev/wk-ib540-old 49467335d288d5c0012fe339c4cafcb74bd43fb5`) into `C:/dev/_scratch385/old/<firm>/`. `bundle_delta` = the member comparison old payload against new payload (by sha256 of each member's bytes): `members_added` must be exactly `["data/assets/scripts/silver/opal_unidentified.py"]`, `members_changed` and `members_removed` both `[]`.
4. **The import proof (under `python -I`, per firm).** For EVERY `.py` member of the new closure, in a clean interpreter `python -I -c "<code>"` where the code inserts into `sys.path` the extracted tree's member directories (every directory that holds a closure `.py` member, and `<tree>/lib`) and then does `import <module stem>`. (`-I` ignores `PYTHONPATH`, so the paths must be inserted by the code.) Record per firm `{"python_flags":"-I","members_imported":[every .py closure member path],"import_errors":[any module and its error],"bundle_tree_members":<files in the tree, the closure plus SHA256SUMS>}`. **An ImportError is a FAIL: record it and report; do not work around it.**
5. **The closure equals the traced import set, both ways.** For each firm, in a clean `python -I` process on the extracted new tree, put the producer's directory and `<tree>/lib` first on `sys.path`, install `sys.addaudithook` recording every file OPENED under the tree, run a real read-only build `holdings_snapshot.build_snapshot(firm, VersionedInputs(boto3 s3 client), as_of)` (custody pins: 49financial 2026-10-12, cottonwood 2026-10-12, inflection 2026-10-13; read calls only), and collect the files under the tree that appear in `sys.modules` or in the open events. `traced_files` = the union over the three firms, repo-relative with forward slashes, excluding `SHA256SUMS`. `missing` = traced not in the closure (MUST be empty). `extra` = closure members never touched by the three runs: each is listed with its `import_site` = `<closure member path>:<line number>` of an import statement in the NEW-pin source that names it (the check reads that line at the new pin and requires the module's stem on it); an extra with no such site is a closure member nothing imports: report it, do not delete it. Record `closure_vs_trace` = `{"traced_files":[..],"missing":[],"extra":[{"path":"..","import_site":".."}]}`.
6. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~385/IB196-1_closure_record.json`: `{"base_commit":"<40hex>","base_pin":"49467335d288d5c0012fe339c4cafcb74bd43fb5","new_pin":"<40hex>","import_proof":{"<firm>":{..}},"closure_vs_trace":{..},"bundle_delta":{..},"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.
7. **Run the three criteria below from your worktree root.** The check reads the new pin by hash from the shared object store, so the pin commits need not be in your branch. Record each output and exit code verbatim in `IB196-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (deliverables first, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record or build (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove the two pin worktrees and the scratch. Report once, under 150 words, naming `new_pin`.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB196-1-AC1" cell_refs="IB-pr-540"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py" . IB196-1-AC1</invocation><expect>IB196-1-AC1 PASS</expect></criterion>
<criterion id="IB196-1-AC2" cell_refs="IB-pr-540"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py" . IB196-1-AC2</invocation><expect>IB196-1-AC2 PASS</expect></criterion>
<criterion id="IB196-1-AC3" cell_refs="IB-pr-540"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py" . IB196-1-AC3</invocation><expect>IB196-1-AC3 PASS</expect></criterion>

<expected_criteria>IB196-1-AC1, IB196-1-AC2, IB196-1-AC3</expected_criteria>

What the checks grade: AC1 the new pin descends from the old pin, changes only the core file (and this order file), the parsed closure tuple gains exactly `opal_unidentified.py`, and the core file deletes no line; AC2 for each firm `python -I`, every `.py` closure member listed as imported, no import error, and the bundle tree holding the closure plus `SHA256SUMS`; AC3 the closure compared with the traced files (the check recomputes `missing` and `extra` from the closure at the new pin), each extra with a verifiable import site, a bundle delta of exactly one added member, the six bound counters 0 and no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the two pin worktrees and the scratch directory outside the repository, and the new branch `pin-ib-pr-540`. **Nothing is minted, uploaded, applied, deployed, signed, invoked or sent;** the only AWS calls are the read-only source reads of the trace builds (get/list with your identity). A denial is recorded, never worked around or widened. (AWS CLI goes through the `.tools/aws` shim; never a bare `MSYS_NO_PATHCONV=1 aws`.)
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a closure change other than the one line; an ImportError after the fix; a traced file outside the closure that you cannot explain; a call that writes to AWS; a client identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W385-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with the usual fields, including `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
.tools/safe_deploy_core.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-540.fix-bundle-closure-into-a-new-pin.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~385/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 188 (round 196, workstream ~P), cell `IB-pr-540`.
<owned_cells>IB-pr-540</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB196-1-AC1, IB196-1-AC2, IB196-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~385/IRPT_BCKEND.TO-IB-pr-540.fix-bundle-closure-into-a-new-pin.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order changes one declaration (the closure tuple in `.tools/safe_deploy_core.py`, which only names the members a standalone bundle mint packages) on a side branch from the old pin, builds the three payloads in memory and extracts them to scratch; no bundle is minted, so no served byte moves; the release that would carry the fix is a later order under packet v3's two signed halves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the trace builds read with the worker's own identity.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p196_cells.py IB196-1 dry-run at base on dell2 2026-10-14 ~17:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a throwaway git repo the run created itself (an old pin with a closure tuple, a new pin adding one member; synthetic records; removed): all three PASS; eight negatives, each failing its own arm: a traced file outside the closure, an extra with no import site, a bundle delta that changes a member, an ImportError recorded, imports not under -I, a member left unimported, a closure change beyond the one member, a stray file in the new pin.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~385` (worktree `C:/dev/wk-IRPT_BCKEND-385`). Class LOCAL (a declaration in `.tools/`, no infra path, no served byte; `.tools/` is open to any agent by `.owned-paths.yaml`). The premises are the CTO's round-196 ruling and my own reproduction of the failure (row D2-S175).
</preflight>
