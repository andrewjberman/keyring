# AMGT_RESAPP task order -- `AMGT-gg-3` -- THE WALK ON PORTAL DEV: FWD-18 ON ASML NA, AFTER ITS STORED TEXT IS READ FIRST AND IS THE BUSINESS SECTION

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gg-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~325</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one walk by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account through its own skill's mechanism.
comp-adversary: RUN at the cut -- round 79's walk read ASML NA's chart place as the share-capital refusal; round 81's walk was cancelled with its store half. This walk runs only after AMGT-gg-2 re-cuts ASML NA.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-325`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-gg-3` (round 82, decomposition s.90)

The same walk as round 81's AMGT-ee-5 (`task-orders/AMGT_RESAPP.TO-AMGT-ee-5.the-walk-of-fwd-18-on-asml-na.md` -- read its face
whole: the stored-text read first, the walker rules, the FWD-18 act, the disarm), recorded in
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~325/WALK_ROUND82.md` (first line `PORTAL_REF: <commit>`), the act
headed `FWD-18`, captures copied into `.../0.9.0_WK_AMGT_RESAPP~325/captures/`. The GO names the portal ref.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W325-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Read-only on the product. Disarm the walker when you finish and on any failure. No deploy, no store write, no portal edit.
2. No plant. Nothing is fetched from the internet.
3. The dev server runs only on port 5174; stop it and confirm 0 listeners as the last line of your report.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~325/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gg-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/checks/r82_gg3.py"; echo "exit=$?"</invocation><expect>6 or more captures and a walk record heading FWD-18 and naming its PORTAL_REF; R82 GG3 WALK RECORD: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gg-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; py -3.12 .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads armed=no armedBy=none; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-gg-3" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~325 <0.9.0_WK_AMGT_RESAPP~325@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~325/AMGT_RESAPP.TO-AMGT-gg-3.the-walk-of-fwd-18-on-asml-na.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the stored-text read you ran first;
- for FWD-18: what the page draws against what the server sends, and what the one press opened;
- any row;
- as the LAST line: the dev server stopped and the count of listeners on port 5174.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-81 analysis enrichment item 2 (the FWD-18 walk after the store half). STAGED: waits for AMGT-gg-2's ASML NA AC1/AC2 YES. AC3 is the CVO's L9 read. Check dry-run at the base: AC1 base FAIL (no record).

<status>staged</status>
<round>82</round>
<slot>0.9.0_WK_AMGT_RESAPP~325</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>cancelled -- ISSUER RULING 2026-10-09T08:4xZ: its precondition (AMGT-gg-2's ASML NA re-cut, AC1/AC2 YES) cannot be met this round (gg-2 cancelled, row D1-W324-S1). Never spawned; no walk run; worktree C:/tmp/r82-325 removed unused.</status>
