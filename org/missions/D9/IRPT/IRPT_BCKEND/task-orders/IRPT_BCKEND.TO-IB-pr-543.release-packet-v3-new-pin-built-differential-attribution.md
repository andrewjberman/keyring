# TO IRPT_BCKEND.TO-IB-pr-543 -- WRITE packet v3 of the holdings-producer release: the new pin, the closure fix, the BUILT-bundle differential and Cottonwood's attribution by toggling; both halves UNSIGNED, READ ONLY (CTO round-196 analysis "Then packet v3" @51675bfa49)

<to_id>IRPT_BCKEND.TO-IB-pr-543</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~388</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>196</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-196 analysis (packet v3 = the new pin, the built-bundle differential and Cottonwood's attribution; both halves sign on its bytes, then the apply) | **Decomp cell:** `IB-pr-543` (decomposition section 188) | **outcome_ref:** FWD-3 | **Depends on:** `IB-pr-540`, `IB-pr-541` and `IB-pr-542` merged

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-388`, cut from the current branch AFTER the three predecessors merged. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~388 <0.9.0_WK_IRPT_BCKEND~388@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, field names, classification labels and member paths only; no account id, client id, node id, quantity or holding name.

**Cell `IB-pr-543` (inlined).** Read, in this order: packet v2 `deliverables/0.9.0_WK_IRPT_BCKEND~383/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532_V2.md` (the base text), packet v1 (`deliverables/0.9.0_WK_IRPT_BCKEND~379/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532.md`, VOID for apply), `IB196-1_closure_record.json` (`~385`), `IB196-2_built_differential.json` (`~386`) and `IB196-3_toggle_attribution.json` (`~387`), and the round-195 differential `deliverables/0.9.0_WK_IRPT_BCKEND~384/IB195-1_differential_record.json`. **Write packet v3** `deliverables/0.9.0_WK_IRPT_BCKEND~388/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532_V3.md` = v2 (copied) with its change set, moved-member, Branch A, Branch B and blast-radius sections updated, and these NEW sections (the **signed scope**):
1. **The new pin and the closure fix:** `new_pin` (full 40 hex and the old pin), the one closure line added (`data/assets/scripts/silver/opal_unidentified.py`), why (a Cottonwood bundle minted from the old pin raised `ModuleNotFoundError`, row D2-W384-S1), the `python -I` import proof and the closure-equals-trace result (missing none; the extras and their import sites), and the bundle delta (exactly +1 member).
2. **The live-against-pin differential on the BUILT bundles, at the same served state:** per firm the totals (49financial 32, Inflection 841, Cottonwood from the record), rows, account set, changed values with the largest delta, the gates on both sides against one served state (name each firm's served `latest_date`), the two digests and the mutant. State plainly that the earlier repository-tree measurements are superseded.
3. **Cottonwood's beyond-the-rule changes, attributed by toggling:** per named commit (full hash, name, subject), its revert's removed-node count, the groups it removes with counts, the largest delta; the overlap, joint and unattributed counts (unattributed must read 0). Say in one line per commit what a client sees change (classification, basis or sub-class), without client figures.
4. **Branch A** = the three mints from a worktree at `new_pin` (`bash .tools/safe-deploy.sh --mint-bundle <name>`, one session between fires) with the v2 digest gate rewritten over the BUILT bundle's member table (the changed members equal exactly the table plus the one added member plus `SHA256SUMS`; any other member or hash STOPS the release). **Branch B** as v2, with the manifest anchor rule (a manifest version newer than the packet's is admitted only as the only newer one, written by that firm's scheduled fire of the day, dated T-1). The per-firm business-date rule, the gate comparison at the same served state, and the post-fire kernel-log count while the host is Online. What the packet does not measure.
5. **The COO half and the CTO half, both UNSIGNED**, the packet's own sha256 LEFT for the signers (do not compute it).

It must be at least 3,000 characters longer than v2 and must carry the phrases (case-insensitive) "opal_unidentified", "built bundle", "toggling", "closure", "same served state", "live-against-pin", "Branch A", "Branch B", "manifest anchor", "business date", "moved member", "signed scope", the new pin's full hash, the abbreviated (first ten characters) hash and removed-node count of each of the four commits, the three firms' total changed nodes, the beyond-rule total and the word "unattributed". Write `deliverables/0.9.0_WK_IRPT_BCKEND~388/IB196-4_packet_v3_record.json`: `{"base_commit":"<40hex>","notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. **If any predecessor record shows a STOP (an unattributed node, a number that is not 32 or 841, an import error), do NOT write v3: report the STOP.**

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB196-4_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (packet, record and criteria output first, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR packet (never the check). Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB196-4-AC1" cell_refs="IB-pr-543"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py" . IB196-4-AC1</invocation><expect>IB196-4-AC1 PASS</expect></criterion>
<criterion id="IB196-4-AC2" cell_refs="IB-pr-543"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py" . IB196-4-AC2</invocation><expect>IB196-4-AC2 PASS</expect></criterion>
<criterion id="IB196-4-AC3" cell_refs="IB-pr-543"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py" . IB196-4-AC3</invocation><expect>IB196-4-AC3 PASS</expect></criterion>

<expected_criteria>IB196-4-AC1, IB196-4-AC2, IB196-4-AC3</expected_criteria>

What the checks grade: AC1 v3 at least 3,000 characters longer than v2, naming the new pin and carrying the phrases above; AC2 the removed-node count and the ten-character hash of each of the four commits, each firm's total, the beyond-rule total and the unattributed statement in the text, and both halves UNSIGNED; AC3 no long digit run (the commit ids the packet must name are excluded) and the six bound counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block. READ ONLY and WRITE ONLY in the worker's deliverables. **Nothing is minted, invoked, written to AWS, uploaded, applied, deployed, signed or sent; no AWS call is made.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a predecessor record showing a STOP; a figure you cannot source from a record; a client identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W388-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~388/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 188 (round 196, workstream ~P), cell `IB-pr-543`.
<owned_cells>IB-pr-543</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB196-4-AC1, IB196-4-AC2, IB196-4-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~388/IRPT_BCKEND.TO-IB-pr-543.release-packet-v3-new-pin-built-differential-attribution.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads four committed records and two committed packets and writes one packet and one record in the worker's deliverables; nothing is read from or written to AWS; the release v3 describes is a later order under v3's two signed halves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p196_cells.py IB196-4 dry-run at base on dell2 2026-10-14 ~18:0xZ: AC1, AC2, AC3 FAIL (no packet v3). Positive control in a throwaway git repo the run created itself (synthetic records and packets; removed): all three PASS; five negatives, each failing its own arm: a v3 that is v2 plus little, a v3 without the new pin, a v3 without a commit's count, a v3 with one half signed, a v3 with a long digit run.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~388` (worktree `C:/dev/wk-IRPT_BCKEND-388`). Class LOCAL (a document from committed records; no read of any served system). The premises are the CTO's round-196 ruling and the three predecessor records.
</preflight>
