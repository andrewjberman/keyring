# TO IRPT_BCKEND.TO-IB-pr-547 -- READ why the CUSIP port blanks 45 Cottonwood sub-class values: which securities, which rule path, what the prior path did; the options for the port's own release, READ ONLY (CTO round-197 ruling 3)

<to_id>IRPT_BCKEND.TO-IB-pr-547</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~392</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>197</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-197 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_P_ROUND_197_20261014.md` | **Decomp cell:** `IB-pr-547` (decomposition section 189) | **outcome_ref:** FWD-3 | **Depends on:** none (an independent chain; the port's own release follows it, not this round)

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-392`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~392 <0.9.0_WK_IRPT_BCKEND~392@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object names, field names, classification labels and public security symbols only in any tracked file; no account id, client id, node id, quantity or holding name; the largest delta is a NUMBER with its field name and no id. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch392/`); a recursive delete the harness refuses is left and named in your report.

**Cell `IB-pr-547` (inlined).** The CTO ruled (round 197, item 3) that the CUSIP fallback port `01e843ce2e` follows as its OWN release, under its own pair, AFTER a READ: **why 45 Cottonwood sub-class values become ABSENT** under the closure-fix pin `b1d354cfc9341168a3b4c316a344876ce0049b97` (which still contains the port). Round 196's records name the groups (`deliverables/0.9.0_WK_IRPT_BCKEND~386/IB196-2_built_differential.json` and `~387/IB196-3_toggle_attribution.json`): `sub_asset_class: Investment Grade -> (absent)` 29, `Intermediate -> (absent)` 12, `Cash -> (absent)` 2, `Municipal -> (absent)` 1, `US Small Cap -> (absent)` 1 (45 nodes in all). **This order explains them: which securities, which rule path blanks the value, and what the prior (live) path did that held it. It changes and releases NOTHING.**

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`. `git worktree add --detach C:/dev/wk-ib547-pin b1d354cfc9341168a3b4c316a344876ce0049b97`. Download the live Cottonwood bundle by version id `oyIYMVdh_l2zCg5ZWvn3ISPPS6_9Q82_` (bucket `opal-data-cottonwood`, key `irpt/cottonwood/code/gold/investor-reporting-holdings.tar.gz`) and untar it to `C:/dev/_scratch392/live/`; build Cottonwood's bundle payload from the pin tree (`core.find_bundle("irpt_holdings_cot")`, `core.build_bundle_payload(b)`) and untar to `C:/dev/_scratch392/built/`. Custody pin 2026-10-12.
2. **Find the 45.** Build the Cottonwood candidate from both trees on the same pre-seeded receipts (the round-196 harness approach, `deliverables/0.9.0_WK_IRPT_BCKEND~386/built_bundle_differential.py`; one subprocess per tree, `python -I`) and list the nodes whose `sub_asset_class` is a label on the live side and absent on the built side: the count must be 45 (else STOP). For each, keep the node's public ticker-shaped symbol (never an account, node id or holding name) and its asset class.
3. **Trace the rule path.** For each of the 45, in the built tree's `holdings_snapshot.py` (and any member it calls on this path) find which statement leaves the sub-class absent: instrument or step the classification (for example call the classifier function on the node's display inputs with a tracing wrapper) and record the FIRST branch that returns no sub-class. Group the 45 into `causes`: each `{"nodes":n,"securities_public_symbols":[..],"rule":"<one or two sentences: what the branch does and why it returns no sub-class>","rule_site":"<member path>:<line number at b1d354cfc9341168a3b4c316a344876ce0049b97>","rule_identifier":"<a function or variable name that appears ON that line>","prior_path":"<what the live code did for these symbols that kept the sub-class, with its member and function>"}`. The check reads `rule_site` at the pin and requires `rule_identifier` on that line; the node counts must sum to 45.
4. **Options.** Write `options`: at least two, including `{"kind":"keep_prior_sub_class","consequence":"..","nodes_affected":n}` (the port keeps the sub-class where the prior path held it: say what code change that is, in words, without making it) and `{"kind":"documented_correction","consequence":"..","nodes_affected":n}` (the absence is a documented correction that Andrew is told of before the port ships: say what the client sees). `recommendation` = one of the option kinds, with the reason in `notes`.
5. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~392/IB197-4_cusip_sub_class_read.json`: `{"base_commit":"<40hex>","pin":"b1d354cfc9341168a3b4c316a344876ce0049b97","sub_class_blanked_nodes":45,"causes":[..],"options":[..],"recommendation":"..","notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB197-4_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove the worktrees and scratch you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB197-4-AC1" cell_refs="IB-pr-547"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py" . IB197-4-AC1</invocation><expect>IB197-4-AC1 PASS</expect></criterion>
<criterion id="IB197-4-AC2" cell_refs="IB-pr-547"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py" . IB197-4-AC2</invocation><expect>IB197-4-AC2 PASS</expect></criterion>
<criterion id="IB197-4-AC3" cell_refs="IB-pr-547"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py" . IB197-4-AC3</invocation><expect>IB197-4-AC3 PASS</expect></criterion>

<expected_criteria>IB197-4-AC1, IB197-4-AC2, IB197-4-AC3</expected_criteria>

What the checks grade: AC1 the read is at b1d354cfc9 and covers 45 nodes; each cause has a node count, public symbols, a rule sentence, a rule site `path:line` the check reads at the pin with its identifier on that line, and the prior path; the counts sum to 45; AC2 at least two options including `keep_prior_sub_class` and `documented_correction`, each with a consequence and the nodes affected, and a recommendation that names one; AC3 notes, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktrees and the scratch directory outside the repository. READ ONLY. **Nothing is minted, invoked, written to AWS, uploaded, applied, deployed, signed or sent:** the only AWS calls are `s3api get-object` on live bundle keys by version id and the harness's get/list reads with your identity. A denial is recorded, never worked around or widened. (AWS CLI goes through the `.tools/aws` shim.)
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a count other than 45 blanked values; a rule site you cannot cite at the pin; a client identifier or node id in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W392-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~392/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 189 (round 197, workstream ~P), cell `IB-pr-547`.
<owned_cells>IB-pr-547</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB197-4-AC1, IB197-4-AC2, IB197-4-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~392/IRPT_BCKEND.TO-IB-pr-547.read-why-the-cusip-port-blanks-45-sub-class-values.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order downloads one live bundle object by version id, builds one bundle payload in memory at the closure-fix pin, builds the Cottonwood candidate from both trees on versioned source reads and traces the classification path; it writes only the worker's records; nothing is changed or released
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p197_cells.py IB197-4 dry-run at base on dell2 2026-10-14 ~22:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a throwaway git repo the run created itself (a synthetic read with two causes whose rule sites hold their identifiers; removed): all three PASS; six negatives, each failing its own arm: causes covering 44 nodes, a rule site that does not hold its identifier, a cause with no prior path, one option only, a recommendation outside the options, a long digit run.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~392` (worktree `C:/dev/wk-IRPT_BCKEND-392`). Class SERVED (reads a live bundle and builds a candidate from served sources; writes only the worker's records).
</preflight>
