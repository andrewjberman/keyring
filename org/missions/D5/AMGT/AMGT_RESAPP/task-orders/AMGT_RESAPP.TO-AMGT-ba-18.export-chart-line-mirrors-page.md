# AMGT_RESAPP task order -- `AMGT-ba-18` -- THE EXPORT'S CHART LINE MIRRORS THE PAGE: NO CHART LINE WHERE AN UNDRAFTED THESIS RENDERS NO CHART

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-18</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~284</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one function and its test.
comp-iam: DECLARED-NOT-APPLICABLE -- no read path is added or removed; the function reads the bundle it is handed.
comp-adversary: RUN by the issuer at the cut -- r77_ba18 AC1 FAILS at the base: `_thesis_driver_chart_markdown` (`render_pack.py:1351-1361`, called at `:1597`) prints 'The chart: ABSENT ...' on an undrafted thesis (drafting_status ABSENT, INVALID or missing) and on no bundle at all, where `ThesisDriverChart.tsx` renders no chart element. AC2 PASSES: a drafted thesis prints the one line, a served chart prints none. No test under `lib/research/print/tests/` calls the function today.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; no PDF is built by the check.
</preflight>

**Your worktree:** `C:/tmp/r77-284` (branch `wk-AMGT_RESAPP-284`, cut from the issuer's tree AFTER AMGT-ba-11 drains, with `--portal-ref 13509c52`, the portal DEV head at the cut (three print tests read the portal page source)). Work and commit only there. Start every shell call with `cd /c/tmp/r77-284`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-18` (round 77, decomposition s.85)

The CTO's ruling (`ledger/CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md` @4a89bef967, section E; row Z-W173-S4), in its words:

> The export mirrors the page. Where an undrafted thesis renders no chart, the export prints no chart line. An ABSENT line
> claims a slot the page does not have.

The row's measurement: `ThesisDriverChart.tsx` renders its absence element only when the thesis is drafted (the Thesis tab draws the panel only when `drafting_status` is `SERVED`). `render_pack._thesis_driver_chart_markdown` writes 'The chart: ABSENT' on every name. On AMD (undrafted) the page has no chart element at all and the export has the line.

**Build, in `lib/research/print/render_pack.py`, the function `_thesis_driver_chart_markdown` only (`:1351-1361`):**
- When the bundle's `drafting_status` is not `SERVED` (ABSENT, INVALID, missing, or no bundle at all), return `[]`: no chart line.
- When it is `SERVED` and the chart is not served, return the one line exactly as today. Do not reword it.
- When the chart is served, return `[]`, as today.
- **Plant test** `lib/research/print/tests/test_ba18_chart_line.py`: the four bundle states, and one `build_rich_text` arm showing an undrafted name's export carries no line starting 'The chart:'.

The row also notes that on a drafted name the page states the served reason while the export names the driver series. That is NOT ruled and is not yours: leave the drafted line's words alone, and say in your report what each side prints.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W284-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no vendor, SEC or model call, no portal write.
2. In `render_pack.py` you change `_thesis_driver_chart_markdown` and nothing else. The text re-read at `:750-757` and `build_pack` belong to AMGT-ba-11, which landed before your worktree was cut; do not touch them.
3. No other export line moves. `test_av2_export_equals_page.py` stays green.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/test_ba18_chart_line.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~284/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1200)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-18"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba18.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>C1 and C2 PASS: an undrafted thesis (ABSENT, INVALID, missing) and no bundle at all print no chart line; R77 BA18 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-18"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba18.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>C1 and C2 PASS (the control): a drafted thesis with no chart prints the one absence line in today's words, and a served chart prints none; R77 BA18 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~284 <0.9.0_WK_AMGT_RESAPP~284@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~284/AMGT_RESAPP.TO-AMGT-ba-18.export-chart-line-mirrors-page.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the print suite's last line;
- what the page and the export each print on a drafted name with no chart;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Z):** ROUND_ANALYSIS.round76.md @c8bbeeac10 section 4 item 10 (the export chart line); ruling CTO @4a89bef967 section E, row Z-W173-S4. Decomposition s.85. WRITE-SET: the chart line lives in `lib/research/print/render_pack.py`, the SAME FILE as row Z-S218's text re-read (`:750-757`, AMGT-ba-11). The two edits are 600 lines apart, but the write-set law is per file, so this order is cut one wave AFTER ba-11 (edge: ba-11 -> ba-18) and staged until ba-11 drains. Alternative the issuer may take at assembly: fold this ten-line change into ba-11 and withdraw this order. Checks dry-run at the base: ba-18 AC1 base: FAIL as expected; ba-18 AC2 base: PASS as expected. The served export changes only with the round's redeploy. A small cell: `worker-light` fits (about 10 product lines).

<status>staged</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~284</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- drained @14a36147bd; proof VALID (worktree checker); the export prints no chart line on an undrafted thesis (the page shows none); AC1 4 of 4 states, AC2 2 of 2 arms; print suite 114 passed</status>
