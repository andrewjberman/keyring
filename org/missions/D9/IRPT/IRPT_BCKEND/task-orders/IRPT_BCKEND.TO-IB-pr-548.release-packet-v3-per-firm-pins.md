# TO IRPT_BCKEND.TO-IB-pr-548 -- WRITE packet v3 of the holdings-producer release on PER-FIRM PINS: 49financial on the closure-fix pin, Cottonwood and Inflection on pin 2, each moved by the signed cash rule alone; both halves UNSIGNED, READ ONLY (CTO round-198 ruling, msg 7910)

<to_id>IRPT_BCKEND.TO-IB-pr-548</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~393</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>198</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-198 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_P_ROUND_198_20261015.md` | **Decomp cell:** `IB-pr-548` (decomposition section 190) | **outcome_ref:** FWD-3 | **Depends on:** none (every record it reads is committed)

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-393`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~393 <0.9.0_WK_IRPT_BCKEND~393@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object names, field names and classification labels only in any tracked file; no account id, client id, node id, quantity, security identifier or holding name. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch393/`).

**Cell `IB-pr-548` (inlined).** The CTO ruled (round 198) that the holdings-producer release ships on PER-FIRM PINS because the live bytes differ by firm: the live 49financial producer already carries the CUSIP port (its `holdings_snapshot.py` is the closure-fix pin minus the 40 signed lines), Cottonwood's and Inflection's do not. The principle is round 197's: each firm moves by the signed cash rule ONLY, each firm's bundle is ONE commit's bytes.

| firm | pin | changed nodes | record |
|---|---|---|---|
| 49financial | closure-fix pin `b1d354cfc9341168a3b4c316a344876ce0049b97` (port kept: already live there) | 32 | `deliverables/0.9.0_WK_IRPT_BCKEND~386/IB196-2_built_differential.json` |
| cottonwood | pin 2 `5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f` (port reverted: not live there) | 255 | `deliverables/0.9.0_WK_IRPT_BCKEND~390/IB197-2_built_differential.json` |
| inflection | pin 2 `5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f` | 841 | same record (841 at the closure-fix pin too) |

**Read, in this order:** packet v2 `deliverables/0.9.0_WK_IRPT_BCKEND~383/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532_V2.md` (the base text), the CTO's analysis above, the closure record `~385/IB196-1_closure_record.json`, `~386/IB196-2_built_differential.json`, `~389/IB197-1_pin2_record.json`, `~390/IB197-2_built_differential.json` (read its 49financial 119 and its notes), `~392/IB197-4_cusip_sub_class_read.json`, and the channel rows `IRPT_BCKEND-D2-S177` and `D2-S178` in `surprise-channel/investigations/INVESTIGATION_v1.md`.

**Write packet v3** `deliverables/0.9.0_WK_IRPT_BCKEND~393/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532_V3.md` = v2 (copied) with its change set, moved-member, Branch A, Branch B and blast-radius sections updated, and these NEW sections (the **signed scope**):
1. **The per-firm pin table** (a markdown table, one row per firm, each row naming its firm, its pin by the first 10 hex characters, "the cash rule" and its changed nodes), then the full 40-hex hashes of BOTH pins in the text. A row for 49financial must NOT name pin 2; rows for cottonwood and inflection must NOT name the closure-fix pin.
2. **The two pins:** the closure-fix pin (adds `opal_unidentified`; `python -I` import proof of every closure member from each firm's built bundle and closure equals the traced set both ways, from `~385`) and pin 2 (one commit on it reversing the CUSIP port `01e843ce2e` in `holdings_snapshot.py`; bundle delta exactly `holdings_snapshot.py`, from `~389`).
3. **Why 49financial is not on pin 2:** at pin 2 its differential measured 119 changed nodes (34 the cash rule, 87 outside it; the built gate REFUSED on `classified_security_lost` against live PUBLISHED at the same served state), because the live 49financial producer already carries the CUSIP port (row D2-S178). State it plainly, with the 119.
4. **The temporary fork:** a per-firm pin is a named, temporary fork, not a standing one ("identical naming structure and operations per firm"). It is closed by the CUSIP port's OWN release, which brings Cottonwood and Inflection to the port after the read of the 45 absent Cottonwood sub-class values (`~392`: one rule site, three options); that release's pair names the reconvergence as its goal. The 45 values do not ship in this release (pin 2 carries no port).
5. **The signed scope at the same served state:** per firm the total changed nodes (the table's), rows, account set, changed values (largest delta), the gates on both sides against one served state (name each firm's served `latest_date`), the digests and mutant; **every change is the signed cash rule**. Cottonwood's 255 includes the 4 nodes round 196 found overdetermined. These counts supersede the earlier packets' (249 and 485 for Cottonwood).
6. **Branch A (per firm):** each mint is run from a worktree AT THAT FIRM'S PIN (`bash .tools/safe-deploy.sh --mint-bundle <name>`: `irpt_holdings_49f` at the closure-fix pin, `irpt_holdings_cot` and `irpt_holdings_inf` at pin 2), one session between fires, with the digest gate over the BUILT bundle's member table (any member or hash other than the recorded delta STOPS the release). **Branch B** as v2, with the manifest anchor rule (a manifest version newer than the packet's is admitted only as the only newer one, written by that firm's scheduled fire of the day, dated T-1), the per-firm business date rule, the gate comparison at the same served state, the post-fire kernel-log count while the host is Online. What the packet does not measure.
7. **The COO half and the CTO half, both UNSIGNED**, the packet's own sha256 LEFT for the signers (do not compute it).

It must be at least 3,000 characters longer than v2 and carry these phrases (case-insensitive): "opal_unidentified", "built bundle", "closure", "own release", "cash rule", "same served state", "Branch A", "Branch B", "manifest anchor", "business date", "moved member", "signed scope", "per-firm pin", "temporary fork", "reconverg", both pins' full hashes, the reverted port's short id `01e843ce2e`, "119", and "COO half" and "CTO half" each beside the word UNSIGNED. Write `deliverables/0.9.0_WK_IRPT_BCKEND~393/IB198-1_packet_v3_record.json`: `{"base_commit":"<40hex>","notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` before your first commit. **If a record contradicts the table (a total other than 32, 255 or 841), do NOT write v3: report it.**

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB198-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR packet or record (never the check); a check no packet can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB198-1-AC1" cell_refs="IB-pr-548"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r198/p198_cells.py" . IB198-1-AC1</invocation><expect>IB198-1-AC1 PASS</expect></criterion>
<criterion id="IB198-1-AC2" cell_refs="IB-pr-548"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r198/p198_cells.py" . IB198-1-AC2</invocation><expect>IB198-1-AC2 PASS</expect></criterion>
<criterion id="IB198-1-AC3" cell_refs="IB-pr-548"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r198/p198_cells.py" . IB198-1-AC3</invocation><expect>IB198-1-AC3 PASS</expect></criterion>

<expected_criteria>IB198-1-AC1, IB198-1-AC2, IB198-1-AC3</expected_criteria>

What the checks grade: AC1 v3 at least 3,000 characters longer than v2, naming both pins in full and the reverted port and carrying the phrases above; AC2 the per-firm pin table (49financial on the closure-fix pin with the record's 32, cottonwood and inflection on pin 2 with the records' totals, never the other pin), the 119, and both halves UNSIGNED; AC3 no long digit run (the two pins excepted) and the six bound counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and the scratch directory outside the repository. READ ONLY. **Nothing is minted, invoked, written to AWS, uploaded, applied, deployed, signed or sent;** no AWS call is needed (a document from committed records).
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a record contradicting the table; a client identifier, node id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W393-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~393/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 190 (round 198, workstream ~P), cell `IB-pr-548`.
<owned_cells>IB-pr-548</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB198-1-AC1, IB198-1-AC2, IB198-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~393/IRPT_BCKEND.TO-IB-pr-548.release-packet-v3-per-firm-pins.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads committed records and packets and writes one packet and one record in the worker's deliverables; nothing is read from or written to AWS; the release v3 describes is a later order under v3's two signed halves
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; no AWS call is made.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p198_cells.py IB198-1 dry-run at base on dell2 2026-10-15 ~02:2xZ: AC1, AC2, AC3 FAIL (no packet v3). Positive control in a temporary root the run created itself (synthetic records and packets; removed): all three PASS; fourteen negatives, each failing its own arm: a v3 that is v2 plus little, a v3 without the closure-fix pin, without pin 2, without the reverted port, without the temporary fork, 49financial on pin 2, cottonwood on the closure-fix pin, inflection without its total, no 119, one half signed, a record reading 49financial 31, a record reading cottonwood 485, a long digit run, a counter above 0.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~393` (worktree `C:/dev/wk-IRPT_BCKEND-393`). Class LOCAL (a document from committed records; no read of any served system).
</preflight>
