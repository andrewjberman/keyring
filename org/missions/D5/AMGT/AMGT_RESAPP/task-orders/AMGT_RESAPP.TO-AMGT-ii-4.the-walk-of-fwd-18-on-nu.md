# AMGT_RESAPP task order -- `AMGT-ii-4` -- THE WALK ON PORTAL DEV: FWD-18 ON A SECOND 20-F NAME, NU_US_EQUITY, AFTER ITS STORED TEXT IS READ FIRST

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ii-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~337</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one walk by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account through its own skill's mechanism.
comp-adversary: RUN at the cut -- FWD-18 holds on DEV for ASML NA only (round 83 hh-5); NU was re-served in round 83 (38 of 38 draft sentences on span; live /thesis 39 locations, 4 from its business item, 98% English sentences).
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-337`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ii-4` (round 84, decomposition s.92)

The same walk as round 83's AMGT-hh-5 (`task-orders/AMGT_RESAPP.TO-AMGT-hh-5.the-walk-of-fwd-18-on-asml-na.md` -- read its face
whole, and round 81's ee-5 face it cites: the stored-text read first, the walker rules, the FWD-18 act, the disarm), on
NU_US_Equity instead of ASML NA, recorded in
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~337/WALK_ROUND84.md` (first line `PORTAL_REF: <commit>`), the act
headed `FWD-18`, captures copied into `.../0.9.0_WK_AMGT_RESAPP~337/captures/`. The stored-text read first is
`python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_store.py --key NU_US_Equity --crit AC2`. The GO names the portal ref. If another seat holds the walker lease or
port 5174, wait for it to clear; never touch another seat's lease.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W337-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Read-only on the product. Disarm the walker when you finish and on any failure. No deploy, no store write, no portal edit.
2. No plant. Nothing is fetched from the internet.
3. The dev server runs only on port 5174; stop it and confirm 0 listeners as the last line of your report.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~337/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ii-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_ii4.py"; echo "exit=$?"</invocation><expect>6 or more captures and a walk record heading FWD-18 and naming its PORTAL_REF; R84 II4 WALK RECORD: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ii-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; py -3.12 .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads armed=no armedBy=none; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ii-4" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~337 <0.9.0_WK_AMGT_RESAPP~337@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~337/AMGT_RESAPP.TO-AMGT-ii-4.the-walk-of-fwd-18-on-nu.proof_of_spec.json`.
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

**ISSUER NOTES:** CTO~DELL1 round-83 analysis enrichment item 3 (one walked name besides ASML). No dependency: NU was re-served in round 83. AC3 is the CVO's L9 read. Check dry-run at the base: AC1 base FAIL (no record).

<status>pending</status>
<round>84</round>
<slot>0.9.0_WK_AMGT_RESAPP~337</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- issuer close 2026-10-09T11:0xZ: merged @ab5d2a1a6c (wk-AMGT_RESAPP-337 @1806621f4d, proof VALID). AC1 YES (8 captures, PORTAL_REF 9b06f6edcb), AC2 YES (armed=no; post-disarm login refused), AC3 RECORDED for the CVO's L9: NU's 39 served locations (Item 5 x23, 3.D x13, 4.B x3) are all drawn (20 + 9 + 10 passage blocks); share-capital refusal 0; driver chart place a sentence (ABSENT, 0 points); the page's 'No company description is on file yet.' matches the server here (company_description absent); the one press on a figure opened nothing (no pressable figure). Row D1-W337-S1 (r84_store's business regex also matches a 3.D heading containing 'our business'; T2 holds on the 3 true 4.B locations) is INERT and carried: tighten the regex.</status>
