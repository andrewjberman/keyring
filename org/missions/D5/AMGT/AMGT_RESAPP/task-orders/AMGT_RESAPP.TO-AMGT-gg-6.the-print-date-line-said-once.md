# AMGT_RESAPP task order -- `AMGT-gg-6` -- THE PRINT PDF SAYS 'DATE NOT STORED WITH THIS FIGURE' ONCE, NOT ON EVERY UNDATED HEADER LINE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gg-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~328</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one helper and one test.
comp-iam: DECLARED-NOT-APPLICABLE -- no read or write path changes.
comp-adversary: RUN at the cut (round82_prep/GROUP_PRINT_NOTES.md) -- the PDF header repeats the phrase on 10-11 of ~21 lines for AMD, BA, ASML, NU and UNVGY; the rich-text export says it 0 times. AC1 and AC2 FAIL at the base (the helper does not exist).
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-328`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-gg-6` (round 82, decomposition s.90)

Read `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/GROUP_PRINT_NOTES.md` whole first.

1. In `lib/research/print/render_pack.py` add `_header_print_lines(header_figs, trading_currency, reporting_currency) -> list[str]`:
   each header figure's line as `_plain_figure_line` makes it today, with ` - date not stored with this figure` removed, plus ONE
   line at the END of the header block saying `Figures marked without a date: date not stored with this figure.` -- only when at
   least one header figure has a number and no date of its own. `build_pack` prints those lines for the Header block.
2. Nothing else in the pack changes; the rich-text export is untouched.
3. New test `lib/research/api/tests/test_header_date_once.py` (the three cases: some undated, all dated, text only).

`pypdf` is absent on this box, so tests that read the rendered PDF fail at import: name them, file no row.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W328-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `render_pack.py` and add the one test file only.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/api/tests/test_header_date_once.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~328/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gg-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/checks/r82_print.py" --crit AC1; echo "exit=$?"</invocation><expect>the phrase appears exactly once across AMD's header lines, 0 times when every numeric figure is dated and 0 times for a text-only header; P1-P4 PASS; R82 PRINT AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gg-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/checks/r82_print.py" --crit AC2; echo "exit=$?"</invocation><expect>every header figure line equals today's line minus the phrase; B1 PASS; R82 PRINT AC2: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~328 <0.9.0_WK_AMGT_RESAPP~328@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~328/AMGT_RESAPP.TO-AMGT-gg-6.the-print-date-line-said-once.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line (api folder on this box: 2 failed at the base, both `No module named 'pypdf'` -- name them, file no row);
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-81 analysis enrichment item 4c (msg 1880). Checks dry-run at the base: AC1 base FAIL as expected; AC2 base FAIL as expected (a build equivalence check that needs the new helper; relabelled at the cut). Served only through AMGT-gg-7.

<status>pending</status>
<round>82</round>
<slot>0.9.0_WK_AMGT_RESAPP~328</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- drained @23da81a54e (build 0c685343ea, proof 96f65f006a VALID rc=0). Re-run by the issuer on the branch: R82 PRINT AC1: YES (AMD 22 header lines, the phrase once, at the end of the Header block), AC2: YES (21 of 21 figure lines equal today's minus the phrase); api folder 2 failed (pypdf absent on dell1), 878 passed. Served only through AMGT-gg-7.</status>
