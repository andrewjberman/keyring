# AMGT_RESAPP task order -- `AMGT-ee-5` -- THE WALK ON PORTAL DEV: FWD-18 ON ASML NA, AFTER ITS STORED TEXT IS THE BUSINESS SECTION

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ee-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~322</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one walk by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms its own dormant account through its own skill's mechanism.
comp-adversary: RUN at the cut -- round 79's walk read ASML NA's chart place as the share-capital refusal and its thesis figure as no control; the stored text was the 20-F's share capital (CTO~Z R1). This walk runs only after AMGT-ee-4 re-cuts ASML NA.
EGRESS CLASS, declared: NONE. Localhost dev build only.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-322`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ee-5` (round 81, decomposition s.89)

**Read the stored text FIRST** (CTO~Z round-79 R1): before walking, run
`python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81_prep/checks/r81_store.py --crit AC1` and record its
output; if it reads NO, file a BLOCKING row and stop: the walk is on a business section or not at all.

**The walker account is one identity across boxes.** On this box run it with `py -3.12`. If
`py -3.12 .claude/skills/ui-walk/ui_walker_account.py status` reads armed by anyone else when you start or between passes, file a
BLOCKING row and stop. Read `.claude/skills/ui-walk/SKILL.md` whole first. Serve the dev build on `http://localhost:5174` from YOUR
worktree's portal (`cd portal && bun run dev:live --port 5174`). Role admin. Round 80's driver is at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~317/instrument/`; copy it into your own `instrument/`.
Run no `bun install`, `bun add`, `bun update`, `npm` or `npx` in this worktree: its packages are linked.

Record in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~322/WALK_ROUND81.md`; its first line is
`PORTAL_REF: <the portal commit you served>`. Head the act `FWD-18`, quote its DONE WHEN from the PRD
(`org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md`, version and line), record what you saw, and copy the captures into
`.../0.9.0_WK_AMGT_RESAPP~322/captures/` with a positive control. Record; give no verdict.

- **FWD-18 on ASML NA** (`ASML_NA_Equity`), the Thesis tab: the company description and what the page says the company does now;
  the place where a driver chart would be (a chart, or a sentence in its place -- quote it); press ONE figure in the thesis text
  that can be pressed and record what opens (passage, filing, heading, paragraph), with captures before and after. From the
  signed-in API client record beside it: the served citations' `location` values and any refusal sentence.
- Then disarm (the disarm proves dormancy without deleting the password parameter; record what it printed).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W322-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Read-only on the product. Disarm the walker when you finish and on any failure. No deploy, no store write, no portal edit.
2. No plant by you. Nothing is fetched from the internet.
3. The dev server runs only on port 5174. Stop it when you finish and confirm 0 listeners as the last line of your report.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~322/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ee-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81/checks/r81_ee5.py"; echo "exit=$?"</invocation><expect>6 or more captures and a walk record heading FWD-18 and naming its PORTAL_REF; R81 EE5 WALK RECORD: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ee-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; py -3.12 .claude/skills/ui-walk/ui_walker_account.py status; echo "exit=$?"</invocation><expect>the account reads armed=no armedBy=none; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ee-5" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~322 <0.9.0_WK_AMGT_RESAPP~322@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~322/AMGT_RESAPP.TO-AMGT-ee-5.the-walk-of-fwd-18-on-asml-na.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the stored-text read you ran first;
- for FWD-18: what the page draws against what the server sends, and what the one press opened;
- any row;
- as the LAST line: that the dev server is stopped and the count of listeners on port 5174.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-80 analysis enrichment item 1 (the FWD-18 walk after the store half). STAGED: waits for AMGT-ee-4's ASML NA re-cut and its AC1/AC2 YES. AC3 is the CVO's L9 read. Check dry-run at the base: AC1 base: FAIL as expected (0 captures, no record).

<status>staged</status>
<round>81</round>
<slot>0.9.0_WK_AMGT_RESAPP~322</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>cancelled -- ISSUER RULING 2026-10-09T06:4xZ: its precondition (AMGT-ee-4's ASML NA re-cut, AC1/AC2 YES) cannot be met this round (ee-4 cancelled, row D1-W321-S1). Never spawned; no walk run. The FWD-18 walk on ASML NA is carried to round 82 behind the cutter repair.</status>
