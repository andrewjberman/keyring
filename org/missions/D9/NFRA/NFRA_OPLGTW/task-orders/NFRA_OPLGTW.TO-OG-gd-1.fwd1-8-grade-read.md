# NFRA_OPLGTW task order -- `OG-gd-1` -- the grade read of FWD-1..FWD-8: run each outcome's PROOF against live state and record it (R5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gd-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gd-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~66</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads only: repo files, offline test suites, the gateway's S3 audit lake and the grant store. Nothing is written outside W; nothing is deployed or scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the box's own read credentials through .tools/aws.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-36 analysis R5 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round36.md @713305ee56), direction XB-20261013T185926Z-4d72 Z3 ("GRADE FWD-1..8 instead of only ruling rows").
EGRESS CLASS, declared: NONE beyond Opal's own AWS (read-only).
</preflight>

## 1. THE CELL -- `OG-gd-1` (decomposition addendum R3-T.49, R5)

**The ask (round-36 analysis, R5, verbatim).** "For each of FWD-1 to FWD-8, run that outcome's PROOF as the PRD writes
it (`prd/NFRA_OPLGTW_PRD.md` :55-133) against live state, and record the evidence with its claim. Where a proof needs
Andrew's or a named user's act, record which act and that it is owed. This seat grades each outcome REALIZED /
NOT_REALIZED at the round-37 analysis, from that record."

1. **Split each PROOF into its arms.** For each FWD-n, read its PROOF sentence at `prd/NFRA_OPLGTW_PRD.md` (FWD-1 :63,
   FWD-2 :73, FWD-3 :83, FWD-4 :93, FWD-5 :103, FWD-6 :113, FWD-7 :123, FWD-8 :133). Every case the sentence names is one
   arm. Example: FWD-4 names an opened filtered download, a copied-link attempt by another account, an expired-link
   attempt, and a refused original-file request, so it has 4 arms.
2. **Run every arm an instrument can run, against LIVE state.** Instruments:
   - the gateway's audit lake, `s3://opal-mcp-audit/audit/dt=<day>/` (written by `app/audit.py`), for real use by real
     principals: who called which tool, outcome, refusals;
   - the grant store, `gateway-access-state-table`, read only;
   - the gateway's offline suites under `infra/aws/ec2/opal-gateway/tests/`, for refusal logic. A suite result is claim
     `inferred` for a live outcome, never `measured`;
   - the operator runbook `infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md` (FWD-8);
   - the round records under `org/missions/D9/NFRA/NFRA_OPLGTW/ledger/` and `deliverables/`. A prior measurement may be
     cited only with its date, and claim `inferred` unless you re-read it live.

   Bound every read: one UTC day or a named window per lake read, with the object denominator printed. No call through
   the live gateway is made under anyone's identity.
3. **Record the arms an instrument cannot run as OWED.** An arm that needs a person signing in, opening a link, or an
   operator walkthrough is `ran: false`. It names the owed act: `{"who": "<role or named user, e.g. 'Menachem (pilot
   user)' or 'Andrew'>", "what": "<the act, one line>"}`. If the lake shows that act already happened for real, record it
   as `ran: true` with that evidence.
4. **Write `W/GD1_GRADE_READ.json`** = `{"read_at", "outcomes": [{"fwd": "FWD-n", "proof_ref": "prd/NFRA_OPLGTW_PRD.md:<line>",
   "arms": [{"arm", "ran": bool, "claim": "measured|inferred|absent", "evidence": [{"path": "<repo path, a file under W,
   or a W file holding the command and its output>", "note"}], "owed_act": {"who", "what"} | null}]}]}`.
   - Keep every command's output you rely on as a file under W.
   - **No grade word** (REALIZED, NOT_REALIZED, HELD, PASS, FAIL) appears on an outcome. The CTO grades.
5. **Privacy.** No email address, account number, tax id, bearer or token value, and no data value from a Schwab or
   Black Diamond answer in W. Principals appear as the audit lake's own hashed principal id, or by role. Counts, dates,
   tool names and outcomes only.

## 2. BOUNDS

- Read-only everywhere. Write only under W and the investigation file. Never call a gateway tool under any identity,
  change a grant, or sign anyone in.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; print a private value (section 1 item 5).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only inputs: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`, `org/missions/D9/NFRA/NFRA_OPLGTW/ledger/`,
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/`, `infra/aws/ec2/opal-gateway/` (app, tests, runbooks),
`s3://opal-mcp-audit/audit/`, the DynamoDB table `gateway-access-state-table`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~66/`. Rows: id `NFRA_OPLGTW-Z-W66-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gd-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gd1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)fwd covered 8 of 8; extra entries 0; outcomes with no arm 0.*arms [1-9]\d*; claim-less 0; un-run without an owed act 0; grade words 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gd-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gd1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)arms run [1-9]\d*; evidence unresolved 0 \(want 0\).*private-value scan: emails 0, 8\+ digit runs 0, token-shaped 0 \(want 0 each\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: every outcome's PROOF is split, claimed and either run or owed by a named act.
- `AC2`: what ran is evidenced, and no private value is written.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gd-1.fwd1-8-grade-read.proof_of_spec.json`. Validate it after your last
commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`. Flip the ONE
`<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, R5 (round-36 analysis @713305ee56). Read only, so it runs in parallel with every other cell. No edge.
- The last grades were 0 REALIZED, 2 NOT_REALIZED and 6 HELD (`ledger/ROUND_ANALYSIS.round15.md`, round 14/15).
  Rounds 24-35 ruled rows instead of grading (direction Z3). This cell is the record the round-37 analysis grades from.
- Pre-cut:
  - gd1.AC1 and gd1.AC2 base FAIL as expected (the record is absent).
  - GREEN arms PASSED on a planted 8-outcome record.
  - RED arms FAILED as they should:
    - 7 of 8 outcomes plus one grade word;
    - one email address and one non-date 8-digit run.
  - Dates and the PRD's own master numbers are exempt from the digit scan. The fixtures were removed.

<status>pending</status>
<round>37</round>
<slot>~66</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
