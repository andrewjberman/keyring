# AMGT_RESAPP task order -- `AMGT-ii-2` -- THE 20-F CUTTER STRIPS THE FILING'S RUNNING PAGE HEADER FROM EVERY CUT SECTION

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ii-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~335</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; the cutter and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- the checks read cached filing texts in-process; no store read or write.
comp-adversary: RUN at the cut (round84_prep/GROUP_HEADER_NOTES.md) -- 612 running-header lines sit inside the 15 cut sections of the five stored 20-F names (ASML 235, BABA 100, NU 128, PBR 69, SAP 80). No passage a served ASML or NU sentence cites carries one (0 of 22, 0 of 34), so no store re-run is owed for them.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-335`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ii-2` (round 84, decomposition s.92)

CTO~DELL1 round-83 analysis R1 item 3: cited passages carry the filing's running page header. Read
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/GROUP_HEADER_NOTES.md` WHOLE first (each filing's header
shape, the strip point in `cut()`, and the rule that keeps repeated table cells), then `lib/research/filings/document.py` whole.
Strip running page headers from 20-F cut sections only; a body line that merely resembles a header stays. 10-K cuts and every
existing fixture cut stay byte-identical, and the round-83 PBR cut keeps its section starts. Add tests in
`lib/research/filings/tests/test_document.py`: one plant per header shape the notes name, each with a look-alike body line that
must be kept.

**Before the checks:** copy the cached filing texts from the base checkout into your worktree (gitignored, never committed):
`mkdir -p <your worktree>/.scratch && cp -r /c/Dev/ajb_workspace/.scratch/r82_20f <your worktree>/.scratch/`. PyMuPDF does not
load on this box; put an empty `fitz.py` on PYTHONPATH for the filings test folder.
Run `lib/research/filings/tests/` before your commit and report its last line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W335-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `document.py` and its test file only. Never fetch a filing (the cache is the input).

## 3. SURFACES

<paths>
lib/research/filings/document.py
lib/research/filings/tests/test_document.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~335/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ii-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_header.py" --crit AC1; echo "exit=$?"</invocation><expect>0 running-header lines remain in the 15 cut sections of the five cached 20-F filings and every planted look-alike body line is kept; H1-H2 PASS; R84 HEADER AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ii-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/checks/r82_cut.py" --crit AC2; echo "exit=$?"</invocation><expect>the 10-K fixture and dd-1's 20-F fixture sections hash as at the base; R82 CUT AC2: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ii-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/checks/r83_pbr.py" --crit AC1 --starts-only; echo "exit=$?"</invocation><expect>PBR's three sections still start at the sections its cross-reference table names and the other four names' 12 section START offsets are unchanged (chars and sha256 move by the strip, by design); R83 PBR AC1: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~335 <0.9.0_WK_AMGT_RESAPP~335@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~335/AMGT_RESAPP.TO-AMGT-ii-2.the-cutter-strips-running-page-headers.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines (AC1's per-name counts in full);
- the filings folder's last line;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-83 analysis R1 item 3 / enrichment item 1. document.py is a site-Z producer path: the MERGE is a site-Z deploy under 1.0.0_SA_CTO~Z's half. Checks dry-run at the base: AC1 base: FAIL as expected (612 lines; H2 3 of 3 kept); AC2, AC3 base: PASS as expected (bounds).

<status>pending</status>
<round>84</round>
<slot>0.9.0_WK_AMGT_RESAPP~335</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending -- AMENDMENT 1 (issuer, 2026-10-09T11:0xZ) on row AMGT_RESAPP-D1-W335-S1: AC3 as cut (r83_pbr P4 comparing start, chars and sha256 of the other four names' cells) contradicts AC1 -- stripping header lines inside a section must change chars and sha. AC3 now runs `r83_pbr.py --crit AC1 --starts-only` (P4 compares start offsets only; the strict default stays for other callers), @this commit. Re-graded on the worker's branch b18d3670ff: --starts-only YES (P1-P3 PASS, P4 12 of 12 starts); strict NO as expected. Graded by no gate limb (a modification; <placeholders>NONE).</status>
