# TO IRPT_BCKEND.TO-IB-pr-542 -- ATTRIBUTE Cottonwood's beyond-the-cash-rule changes by TOGGLING one named commit at a time on the new pin's BUILT bundle: four reverts, each change lands on the commit whose revert removes it or is UNATTRIBUTED (a STOP), READ ONLY (CTO round-196 analysis cell 3 @51675bfa49; rows D2-W384-S3, D2-S174, D2-S175)

<to_id>IRPT_BCKEND.TO-IB-pr-542</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~387</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>196</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-196 analysis section 2 item 3 ("by TOGGLING, not by bisect... member-level attribution is NOT enough") | **Decomp cell:** `IB-pr-542` (decomposition section 188) | **outcome_ref:** FWD-3 | **Depends on:** `IB-pr-540` and `IB-pr-541` merged

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-387`, cut from the current branch AFTER `IB-pr-540` and `IB-pr-541` merged (so `deliverables/0.9.0_WK_IRPT_BCKEND~385/IB196-1_closure_record.json` and `deliverables/0.9.0_WK_IRPT_BCKEND~386/IB196-2_built_differential.json` are in it). Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~387 <0.9.0_WK_IRPT_BCKEND~387@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, field names, classification labels and public symbols only in any tracked file; no account id, client id, node id, quantity or holding name. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch387/`); a recursive delete the harness refuses is left and named in your report.

**Cell `IB-pr-542` (inlined).** Round 195 measured Cottonwood's live-against-pin differential at 485 changed SECURITY nodes: 249 are the signed cash rule and **236 are not** (`asset_class` 4 more fixed_income to cash, `asset_class_basis` NAME_ALIAS or NAME_PATTERN to TABLE, `sub_asset_class` 51 changes, 45 of them to absent). They reproduce with the pin's `holdings_snapshot.py` swapped alone (member-level), but the commit that causes each is not proven; round 195's keyword match of five commit subjects proved nothing (and one of them, `f3a42b2ab8`, is the signed exemption repair). `IB-pr-541` re-measured on the BUILT bundles and records `beyond_rule_nodes` (READ `IB196-2_built_differential.json`). **This order attributes each beyond-rule change to the commit whose REVERT removes it, on the new pin's built Cottonwood bundle. It mints, uploads, applies and signs NOTHING.**

**The four named commits** (CTO round 195, W383-S2): `account_id` (the 49F `account_id` member, `7ace854890` is the candidate), the keyed gate summary (the FWD-14 publish gate holding the served publication as keyed sets, `3f2bdda578` is the candidate), the SC-e-56 CUSIP fallback (`01e843ce2e` ports e62 + e56, the original is `39043b3f90`), and `multi_asset` (`4cc72587d6` readers; `9efbec3c2f` removes the DEPLOY-SERVE-HELD lines). **You identify, for each name, the ONE commit whose revert undoes that change in `holdings_snapshot.py` at the new pin (read `git show`, `git log -S` on the identifying string; print what you searched), and record its 40-hex id.** The check requires the commit's subject to name it: `account_id`, `keyed`, (`SC-e-56` or `CUSIP` or `e56`), `multi_asset`.

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`. `new_pin` from `IB196-1_closure_record.json`. Download the live Cottonwood bundle by version id `oyIYMVdh_l2zCg5ZWvn3ISPPS6_9Q82_` (bucket `opal-data-cottonwood`, key `irpt/cottonwood/code/gold/investor-reporting-holdings.tar.gz`) and untar it to `C:/dev/_scratch387/live/`. Custody pin 2026-10-12.
2. **The base run.** `git worktree add --detach C:/dev/wk-ib542-base <new_pin>`; build Cottonwood's bundle payload there (`core.find_bundle("irpt_holdings_cot")`, `core.build_bundle_payload(b)`, tool from that tree's `.tools`), untar to `C:/dev/_scratch387/base/`. Build the Cottonwood candidate from the LIVE tree and from the BASE tree on the same pre-seeded receipts with the round-195 harness approach (`deliverables/0.9.0_WK_IRPT_BCKEND~384/live_pin_differential.py`, one subprocess per tree, `python -I`, per-node signatures with the four classification fields); the beyond-rule set = the changed (node, field) pairs of base against live minus the signed cash-rule movers (identity-patch). Its distinct-node count MUST equal `beyond_rule_nodes` of `IB196-2_built_differential.json` (else STOP and report).
3. **Four toggles.** For each named commit `c`: `git worktree add --detach C:/dev/wk-ib542-r-<name> <new_pin>`; `git revert --no-commit <c>` there (a conflict is recorded as `revert_applied` false and reported: do not hand-resolve it into something else); build Cottonwood's bundle payload from that tree, untar, and build the candidate on the same receipts. A beyond-rule change is REMOVED by `c` when, in the reverted run, that node's field equals the LIVE value. Record per commit `{"name","commit","revert_applied":true,"removed_nodes":<nodes whose beyond-rule changes ALL vanish with this one revert>,"largest_abs_delta":<largest numeric value delta among its nodes, 0.0 if classification only>,"groups":[{"group":"<field>: <from> -> <to>","nodes":n}]}`.
4. **The arithmetic.** `beyond_rule_total` = the distinct nodes of step 2. `overlap_nodes` = the sum over commits of `removed_nodes` minus the number of distinct nodes removed by at least one commit. `joint_nodes` = nodes no single revert removes entirely but whose every change is removed by SOME single revert. `unattributed_nodes` = nodes with at least one change no single revert removes. The check requires `sum(removed_nodes) - overlap_nodes + joint_nodes + unattributed_nodes == beyond_rule_total`. **Any unattributed node is a STOP (the check fails): record it, report it, and write the rest up to it.**
5. **Determinism and the mutant.** Run the whole toggling TWICE (fresh builds on the same receipts): `run1_digest` and `run2_digest` = sha256 over the canonical JSON (sorted keys, compact) of the per-commit result; equal. Plant a MUTANT: change ONE field value of ONE Cottonwood node in the BASE run's signature to a value that is neither the live nor the base value, and re-run the comparison step only; record `mutant` = `{"flagged":true,"unattributed_nodes_with_mutant":<unattributed_nodes + 1>}` as MEASURED.
6. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~387/IB196-3_toggle_attribution.json`: `{"base_commit":"<40hex>","new_pin":"<40hex>","beyond_rule_total":n,"per_commit":[{..} x4],"overlap_nodes":n,"joint_nodes":n,"unattributed_nodes":n,"run1_digest":"..","run2_digest":"..","mutant":{..},"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.
7. **Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB196-3_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove the worktrees and scratch. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB196-3-AC1" cell_refs="IB-pr-542"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py" . IB196-3-AC1</invocation><expect>IB196-3-AC1 PASS</expect></criterion>
<criterion id="IB196-3-AC2" cell_refs="IB-pr-542"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py" . IB196-3-AC2</invocation><expect>IB196-3-AC2 PASS</expect></criterion>
<criterion id="IB196-3-AC3" cell_refs="IB-pr-542"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py" . IB196-3-AC3</invocation><expect>IB196-3-AC3 PASS</expect></criterion>

<expected_criteria>IB196-3-AC1, IB196-3-AC2, IB196-3-AC3</expected_criteria>

What the checks grade: AC1 `beyond_rule_total` equal to IB-pr-541's `beyond_rule_nodes`, exactly the four named commits each existing with a subject that names it, each revert applied, a removed-node count and a largest delta per commit, the arithmetic above, and `unattributed_nodes` equal to 0; AC2 ONE digest from two runs and a mutant flagged as exactly one more unattributed node; AC3 notes, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktrees and the scratch directory outside the repository. READ ONLY. **Nothing is minted, invoked, written to AWS, uploaded, applied, deployed, signed or sent:** the only AWS calls are `s3api get-object` on the live Cottonwood bundle key by version id and the harness's get/list reads with your identity. A denial is recorded, never worked around or widened. (AWS CLI goes through the `.tools/aws` shim.)
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; an UNATTRIBUTED node; a beyond-rule node count that differs from IB-pr-541's; a revert that does not apply cleanly; two runs that disagree after you ruled out a harness defect; a client identifier or node id in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W387-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~387/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 188 (round 196, workstream ~P), cell `IB-pr-542`.
<owned_cells>IB-pr-542</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB196-3-AC1, IB196-3-AC2, IB196-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~387/IRPT_BCKEND.TO-IB-pr-542.cottonwood-beyond-rule-attribution-by-toggling.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order downloads one live bundle object by version id, builds Cottonwood bundle payloads in memory at the new pin and at four reverted trees (scratch worktrees, nothing committed), and builds candidates from versioned source reads (twice); it writes only the worker's records; the release it informs is a later order under packet v3's two signed halves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p196_cells.py IB196-3 dry-run at base on dell2 2026-10-14 ~18:0xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a throwaway git repo the run created itself (four named commits and an unrelated one; synthetic records; removed): all three PASS; eight negatives, each failing its own arm: an UNATTRIBUTED node, a revert not applied, a commit whose subject does not name it, a joint node not counted, only three commits, a beyond-rule total that is not 541's, two digests, a mutant not flagged, plus a long digit run.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~387` (worktree `C:/dev/wk-IRPT_BCKEND-387`). Class SERVED (reads a live bundle and builds candidates from served sources; writes only the worker's records). The premises are the CTO's round-196 ruling, round 195's measured 485 / 249 / 236 and the closure fix of IB-pr-540.
</preflight>
