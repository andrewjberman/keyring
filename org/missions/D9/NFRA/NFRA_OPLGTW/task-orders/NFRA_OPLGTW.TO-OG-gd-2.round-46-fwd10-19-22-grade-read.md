# NFRA_OPLGTW task order -- `OG-gd-2` -- READ-ONLY: the grade read of FWD-10 to FWD-19 and FWD-22: run each outcome's PROOF against live state and record it, in the shape of GD1 (round 46; round-45 analysis A1 item 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gd-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gd-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~162</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads only: repo files, offline test suites, the gateway's S3 audit lake, the grant store and the silver and backfill-status objects. Nothing is written outside W; nothing is deployed or scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the box's own read credentials through .tools/aws.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-45 analysis amendment A1, list item 2 (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round45.md` @6018fc83fd): "a read-only grade read for FWD-10 to 19 and 22, in GD1's shape, no grade word".
EGRESS CLASS, declared: NONE beyond Opal's own AWS (read-only).
</preflight>

## 1. THE CELL -- `OG-gd-2` (decomposition addendum R3-T.123, amendment A1, round 46, workstream ENRICH-R46-B)

**The ask (round-45 analysis A1, item 2, verbatim).** "Per FWD and per proof arm: `ran`, `claim` (`measured` / `inferred` / `absent`), evidence paths, and the owed act with its operator. No grade word: the grade is this seat's, at the round-46 analysis."

**The model is the GD1 record** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~66/GD1_GRADE_READ.json` and its order `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-gd-1.fwd1-8-grade-read.md`. Read both first: the shape, the evidence rules and the privacy rules below are theirs. This order states only what differs.

1. **The outcomes** are exactly these eleven, with the PRD line of each PROOF sentence in `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`: FWD-10 :144, FWD-11 :154, FWD-12 :164, FWD-13 :174, FWD-14 :184, FWD-15 :194, FWD-16 :204, FWD-17 :214, FWD-18 :224, FWD-19 :234, FWD-22 :291 (its DONE WHEN, :278-282, names six census groups G1 to G6 plus a client-data refusal; each negative arm in the PROOF is its own arm; treat each group's driven call as an arm). FWD-20 and FWD-21 are NOT in this order. Split each PROOF into its arms: every case the sentence names is one arm.
2. **Run every arm an instrument can run, against LIVE state.** Instruments (as GD1, plus):
   - the audit lake `s3://opal-mcp-audit/audit/dt=<day>/` for real use by real principals (who called which tool, outcome, refusals); bound each read to one UTC day or a named window and print the object denominator;
   - the grant store `gateway-access-state-table`, read only;
   - the offline suites under `infra/aws/ec2/opal-gateway/tests/` (claim `inferred` for a live outcome, never `measured`);
   - the silver and `meta/backfill-status.json` objects in `s3://opal-data-assets` for a master's files (FWD-12, FWD-13, FWD-19): a LIST or a `get-object` of a status file, never a data row;
   - the round records under `org/missions/D9/NFRA/NFRA_OPLGTW/ledger/` and `deliverables/`, and the live tool index (`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, the deployed tool names) for FWD-22. A prior measurement may be cited only with its date, claim `inferred`, unless you re-read it live.
   No call through the live gateway is made under anyone's identity.
3. **Record the arms an instrument cannot run as OWED.** An arm that needs a person's sign-in, a person's reading against a statement, or an operator's act is `ran: false`, and `owed_act` is `{"who": "<role or named user>", "what": "<the act, one line>", "operator": "<the seat or person who would run it>"}`. If the lake shows that act already happened for real, record `ran: true` with that evidence.
4. **Write `W/GD2_GRADE_READ.json`** = `{"read_at", "outcomes": [{"fwd": "FWD-n", "proof_ref": "prd/NFRA_OPLGTW_PRD.md:<line>", "arms": [{"arm", "ran": bool, "claim": "measured|inferred|absent", "evidence": [{"path": "<repo path, a file under W, or a W file holding the command and its output>", "note"}], "owed_act": {"who", "what", "operator"} | null}]}]}` with exactly the eleven outcomes above, one entry each.
   - Keep every command's output you rely on as a file under W.
   - **No grade word** (REALIZED, NOT_REALIZED, HELD, PASS, FAIL) appears on an outcome. The CTO grades.
5. **Privacy** as GD1: no email address, account number, tax id, bearer or token value, and no data value from a Schwab or Black Diamond answer in W. Principals appear as the audit lake's hashed principal id, or by role. Counts, dates, tool names and outcomes only. A last-4 never appears as a number (use `****`).

6. **The one protocol edit that rides this cell** (the CTO's round-45 analysis A2, msg 35928: "G-C was retired by `1.0.0_SA_CTO~O` ruling 28152 (Andrew-direct 2026-09-30); see the OG-g-1 status. WALKTHROUGH_PROTOCOL.md section 1 still names G-C as a precondition. Dropping it is a protocol edit, yours to cut, and it can ride OG-gd-2."). In `infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md`, by the smallest edit that works, and nothing else in the file:
   - the first row of the section-1 table (the controlled-identity walkthrough): replace the path of the G-C record in its "presupposes (input record)" cell with the words `retired: G-C was retired by 1.0.0_SA_CTO~O ruling 28152 (Andrew-direct 2026-09-30); no input record is required`;
   - the sentence under the table that begins `Neither input record exists at this cell's base`: rewrite it so it says the pilot input record (G-E) does not exist at the base, that G-C is retired so the controlled walkthrough has no input record to wait for, and that a walkthrough with an input record does not start until that record names the principal class, the approved grant revision and the operator;
   - the `Input:` line of the controlled walkthrough record template (the line in section 8 or later that names `G-C_CONTROLLED_IDENTITY_AND_GRANT.md @<commit>`): replace it with `Input: none (G-C was retired by ruling 28152)`.
   Every other line, including the pilot row and the G-E path, stays byte-equal. Do not decide what replaces the controlled walkthrough: that is the CTO's.

## 2. BOUNDS

- Read-only everywhere except the one protocol file of item 6. Write only under W, that file and the investigation file. Never call a gateway tool under any identity, change a grant, or sign anyone in.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; print a private value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only inputs: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`, `org/missions/D9/NFRA/NFRA_OPLGTW/ledger/`, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/`, `infra/aws/ec2/opal-gateway/` (app, tests, runbooks), `s3://opal-mcp-audit/audit/`, `s3://opal-data-assets` (status objects and listings only), the DynamoDB table `gateway-access-state-table`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~162/`. Rows: id `NFRA_OPLGTW-Z-W162-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gd-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/gd2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)fwd covered 11 of 11; extra entries 0; outcomes with no arm 0.*arms [1-9]\d*; claim-less 0; un-run without an owed act 0; grade words 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gd-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/gd2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)arms run [1-9]\d*; evidence unresolved 0 \(want 0\).*private-value scan: emails 0, 8\+ digit runs 0, token-shaped 0 \(want 0 each\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-gd-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/gd2.AC3.sh; echo "exit=$?"</invocation><expect>(?s)G-C record path named as an input 0 time\(s\) \(want 0\); says G-C was retired by ruling 28152 yes; pilot record G-E still named yes.*added lines [0-8], removed lines [0-8] \(want each 8 or fewer\); changed lines from section 2 on [01] \(want 0 or 1.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: every outcome's PROOF is split, claimed and either run or owed by a named act. `AC2`: what ran is evidenced, and no private value is written. `AC3`: the walkthrough protocol no longer presupposes the retired G-C record, by a narrow edit (base blob `d649cb3e4987de8b88062bdc93ca5cb4720b5f98`).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gd-2.round-46-fwd10-19-22-grade-read.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` (`python3`, not `python`: only `python3 -I` sees `jsonschema`, ruling msg 35901). Flip the ONE `<status>` tag to `complete` only if all three PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 46, workstream ENRICH-R46-B. Source: the CTO's round-45 analysis amendment A1 (msg 35923). Read only; no edge, runs in parallel with every other cell.
- READING DISCLOSED TO THE CTO: (1) FWD-22 is read as its six census groups plus the negative arms (non-Opal refused; no-firm and two-firm refused; ambiguous last-4 returns candidates); each is an arm. (2) `owed_act` carries a third field, `operator`, because the analysis asks for "the owed act with its operator"; GD1's shape has two fields. (3) FWD-20 and FWD-21 are not in this order (FWD-20 is `OG-cd-2` to `OG-ap-50`; FWD-21 is Andrew's act).
- The protocol edit (item 6, `AC3`) rides this cell on the CTO's word (A2, msg 35928). A1's item 4 (G-C written by the CTO) is withdrawn by A2. `AC3` base FAIL as expected (the G-C path is named twice); a narrow edit passes; an edit that leaves the template's G-C `Input:` line, one that omits the ruling number, and one that changes the Evidence rules section each fail.
- Pre-cut: `gd2.AC1` and `gd2.AC2` base FAIL as expected (the record is absent); a planted 11-outcome record passed both; 10 of 11 outcomes, a grade word, an unresolved evidence path, an email and a 12-digit run each failed as they should. The fixture was removed.

<status>complete</status>
<round>46</round>
<workstream>ENRICH-R46-B</workstream>
<slot>~162</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
