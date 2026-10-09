# AMGT_RESAPP task order -- `AMGT-hh-3` -- THE 20-F CUTTER CUTS PBR'S BUSINESS AND MD&A FROM THE SECTIONS ITS CROSS-REFERENCE TABLE NAMES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-hh-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~331</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; the cutter and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- the checks read cached filing texts in-process; no store read or write.
comp-adversary: RUN at the cut (round83_prep/GROUP_PBR_NOTES.md) -- the round-82 cutter takes PBR's business from 'About us' and its MD&A from a liquidity sub-heading: plausible lengths, wrong scope; r82_cut graded length only.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-331`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-hh-3` (round 83, decomposition s.91)

Row AMGT_RESAPP-D1-W323-S1. Read `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/GROUP_PBR_NOTES.md`
WHOLE first (the cross-reference table's rows for 4.B, 3.D and 5, the true body headings and offsets, why the cutter picked
'About us' and the liquidity sub-heading), then `lib/research/filings/document.py` whole. Repair the cutter so PBR's three cuts
start at the sections its own cross-reference table names, without moving any other cached 20-F cut or any 10-K or fixture cut.
Add one test per rule you change, each with the decoy the notes name that must NOT be cut.

**Before the checks:** copy the cached filing texts from the base checkout into your worktree (gitignored, never committed):
`cp -r /c/Dev/ajb_workspace/.scratch/r82_20f <your worktree>/.scratch/`. Run `lib/research/filings/tests/` before your commit
(an empty `fitz.py` on PYTHONPATH) and report its last line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W331-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `document.py` and its test file only. Never fetch a filing (the cache is the input).

## 3. SURFACES

<paths>
lib/research/filings/document.py
lib/research/filings/tests/test_document.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~331/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-hh-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/checks/r83_pbr.py" --crit AC1; echo "exit=$?"</invocation><expect>PBR's business, risk and mdna each start at the section its cross-reference table names for 4.B, 3.D and 5, and the other four names' twelve cells are unchanged; R83 PBR AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-hh-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/checks/r82_cut.py" --crit AC2; echo "exit=$?"</invocation><expect>the 10-K fixture and dd-1's 20-F fixture sections hash as at the base; R82 CUT AC2: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~331 <0.9.0_WK_AMGT_RESAPP~331@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~331/AMGT_RESAPP.TO-AMGT-hh-3.pbr-cut-from-its-real-sections.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the filings folder's last line;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-82 analysis enrichment item 2 (row D1-W323-S1). Grounded round83_prep/GROUP_PBR_NOTES.md. document.py is a site-Z producer path: the MERGE is a site-Z deploy under 1.0.0_SA_CTO~Z's half. Checks dry-run at the base: AC1 base: FAIL as expected; AC2 base: PASS as expected.

<status>pending</status>
<round>83</round>
<slot>0.9.0_WK_AMGT_RESAPP~331</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
