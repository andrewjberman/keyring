# TO IRPT_BCKEND.TO-IB-pr-546 -- WRITE packet v3 of the holdings-producer release ON PIN 2: the closure fix, the CUSIP port reverted and its own release, the built-bundle differential at the same served state; both halves UNSIGNED, READ ONLY (CTO round-197 ruling 2)

<to_id>IRPT_BCKEND.TO-IB-pr-546</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~391</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>cancelled</status>
<status_reason>NOT RUN over a STOP: packet v3 reads IB-pr-545's record, which stopped (49financial 119 against the signed 32 at pin 2); a packet written over an unattributed change would sign a scope the measurement does not hold; the CTO's round-198 analysis rules the per-firm pin question first</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>197</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-197 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_P_ROUND_197_20261014.md` | **Decomp cell:** `IB-pr-546` (decomposition section 189) | **outcome_ref:** FWD-3 | **Depends on:** `IB-pr-544` and `IB-pr-545` merged

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-391`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~391 <0.9.0_WK_IRPT_BCKEND~391@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object names, field names, classification labels and public security symbols only in any tracked file; no account id, client id, node id, quantity or holding name; the largest delta is a NUMBER with its field name and no id. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch391/`); a recursive delete the harness refuses is left and named in your report.

**Cell `IB-pr-546` (inlined).** Read, in this order: packet v2 `deliverables/0.9.0_WK_IRPT_BCKEND~383/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532_V2.md` (the base text), packet v1 (`deliverables/0.9.0_WK_IRPT_BCKEND~379/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532.md`, VOID for apply), the round-196 records (`~385/IB196-1_closure_record.json`, `~386/IB196-2_built_differential.json`, `~387/IB196-3_toggle_attribution.json`), and this round's records (`~389/IB197-1_pin2_record.json`, `~390/IB197-2_built_differential.json`). **Write packet v3** `deliverables/0.9.0_WK_IRPT_BCKEND~391/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532_V3.md` = v2 (copied) with its change set, moved-member, Branch A, Branch B and blast-radius sections updated, and these NEW sections (the **signed scope**):
1. **Pin 2 and what it is:** `5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f` (full 40 hex), a single commit on the closure-fix pin `b1d354cfc9341168a3b4c316a344876ce0049b97` that reverts the CUSIP port `01e843ce2e` in `holdings_snapshot.py`; the closure fix (`opal_unidentified`); the `python -I` import proof and closure-equals-trace result; the bundle delta against the closure-fix pin (exactly `holdings_snapshot.py`). State plainly why the port is out (the CTO's round-197 ruling: this release exists to fix `account_lost`; the port carries a client-visible loss of 45 Cottonwood sub-class values nobody has explained) and that **the CUSIP port is its OWN release** under its own pair after a read.
2. **The signed scope on the BUILT bundle at pin 2, at the same served state:** per firm the totals (49financial 32, Inflection 841, Cottonwood from the record), rows, account set, changed values with the largest delta, the gates on both sides against one served state (name each firm's served `latest_date`), the two digests and the mutant; **every change is the signed cash rule** (Cottonwood's count is the identity-patch count at pin 2, which includes the 4 nodes the round-196 toggle found overdetermined). The signed counts of the earlier packets are superseded for Cottonwood by this count. Earlier repository-tree and CUSIP-included measurements are superseded.
3. **Branch A** = the three mints from a worktree at pin 2 (`bash .tools/safe-deploy.sh --mint-bundle <name>`, one session between fires) with the digest gate over the BUILT bundle's member table (the changed members equal exactly `holdings_snapshot.py` against the closure-fix pin and the one closure addition against the old pin, plus `SHA256SUMS`; any other member or hash STOPS the release). **Branch B** as v2, with the manifest anchor rule (a manifest version newer than the packet's is admitted only as the only newer one, written by that firm's scheduled fire of the day, dated T-1). The per-firm business-date rule, the gate comparison at the same served state, the post-fire kernel-log count while the host is Online. What the packet does not measure.
4. **The COO half and the CTO half, both UNSIGNED**, the packet's own sha256 LEFT for the signers (do not compute it).

It must be at least 3,000 characters longer than v2 and carry these phrases (case-insensitive): "opal_unidentified", "built bundle", "closure", "own release", "cash rule", "same served state", "Branch A", "Branch B", "manifest anchor", "business date", "moved member", "signed scope", pin 2's full hash, the reverted port's short id `01e843ce2e`, and each firm's total changed nodes from `IB197-2_built_differential.json`. Write `deliverables/0.9.0_WK_IRPT_BCKEND~391/IB197-3_packet_v3_record.json`: `{"base_commit":"<40hex>","notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. **If any predecessor record shows a STOP (a number that is not 32 or 841, an unattributed group, an import error), do NOT write v3: report the STOP.**

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB197-3_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove the worktrees and scratch you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB197-3-AC1" cell_refs="IB-pr-546"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py" . IB197-3-AC1</invocation><expect>IB197-3-AC1 PASS</expect></criterion>
<criterion id="IB197-3-AC2" cell_refs="IB-pr-546"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py" . IB197-3-AC2</invocation><expect>IB197-3-AC2 PASS</expect></criterion>
<criterion id="IB197-3-AC3" cell_refs="IB-pr-546"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py" . IB197-3-AC3</invocation><expect>IB197-3-AC3 PASS</expect></criterion>

<expected_criteria>IB197-3-AC1, IB197-3-AC2, IB197-3-AC3</expected_criteria>

What the checks grade: AC1 v3 at least 3,000 characters longer than v2, naming pin 2 and the reverted port and carrying the phrases above; AC2 each firm's total changed nodes in the text and both halves UNSIGNED; AC3 no long digit run (the commit ids the packet must name are excluded) and the six bound counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktrees and the scratch directory outside the repository. READ ONLY. **Nothing is minted, invoked, written to AWS, uploaded, applied, deployed, signed or sent:** the only AWS calls are `s3api get-object` on live bundle keys by version id and the harness's get/list reads with your identity. A denial is recorded, never worked around or widened. (AWS CLI goes through the `.tools/aws` shim.)
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a predecessor record showing a STOP; a figure you cannot source from a record; a client identifier or node id in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W391-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~391/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 189 (round 197, workstream ~P), cell `IB-pr-546`.
<owned_cells>IB-pr-546</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB197-3-AC1, IB197-3-AC2, IB197-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~391/IRPT_BCKEND.TO-IB-pr-546.release-packet-v3-on-pin-2-cash-rule-only.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads committed records and packets and writes one packet and one record in the worker's deliverables; nothing is read from or written to AWS; the release v3 describes is a later order under v3's two signed halves
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p197_cells.py IB197-3 dry-run at base on dell2 2026-10-14 ~22:5xZ: AC1, AC2, AC3 FAIL (no packet v3). Positive control in a throwaway git repo the run created itself (synthetic records and packets; removed): all three PASS; six negatives, each failing its own arm: a v3 that is v2 plus little, a v3 without pin 2, a v3 without the reverted port, a v3 without a firm total, one half signed, a long digit run.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~391` (worktree `C:/dev/wk-IRPT_BCKEND-391`). Class LOCAL (a document from committed records; no read of any served system).
</preflight>
