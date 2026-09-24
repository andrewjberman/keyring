# AMGT_RESAPP task order -- `AMGT-ro-1` -- FWD-30: THE EXPORT ADDS NOTHING THE PAGE DOES NOT SHOW, AND THE HARNESS GRADES THE EXTRAS IT COMPUTES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ro-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~152</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-39 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-ro-1` (round 40, decomposition s.48)

`FWD-30`'s DONE WHEN reads *"a field-by-field comparison against the page shows the SAME figures, the SAME cites and the
SAME absences, with NOTHING in the export that is not on the page"*. Row `AMGT_RESAPP-Z-S268` measures the rich export
(`lib/research/print/render_pack.py` `build_rich_text`, `:601` onward) publishing 17 figures the page does not show -- the
header scalars NAME, CRNCY, CNTRY_OF_DOMICILE, GICS_SECTOR_NAME, EQY_SH_OUT_REAL, EQY_FREE_FLOAT_PCT, SHORT_INT_RATIO (the
page's header shows its seven stat tiles, `portal/src/pages/SecurityAnalysis/constants.ts:109-116`, plus the identity line) and
the `IS_DIV_PER_SHR` fiscal series 2016-2025, which the page REFUSES (`REFUSED: IS_DIV_PER_SHR: unit/sign convention is
'SIGN-UNRESOLVED', not MEASURED`) while the export prints it as values. And
`portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs` computes the extra sets (`:322-324`) and never grades
them (`ok` at `:383-388`). **Build, both limbs:** (1) the export renders only what the page renders -- header figures limited to
the page's stat tiles and the identity-line fields the page shows; a mnemonic the page REFUSES appears only as its REFUSED line
(`_refused_figures_markdown`), never as a value row; the page's description ABSENT line carried verbatim when the page carries
it; with unit tests in `lib/research/print/tests/`; (2) the harness GRADES extras: `ok` also requires 0 figure extras and every
rich absence to be a page absence, and the page set it compares against includes the identity-line fields the page renders
(read them from the rendered markup the way the stat tiles are read). You are the named `POD_DE_ANY` writer for the harness.

## 2. BOUNDS

1. **No server.** You start no vite, dev build or listener (Andrew-direct: portal dev builds use port 5174 only, and that
   run is the issuer's). Your criteria are the files named below, run from the worktree root exactly as written.
2. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-152-portal` at DEV `46c0ae11`. Python from
   the repo root with `PYTHONPATH="$(pwd)"`.
3. Standing: no install, no push, no promote, no S3 write, no vendor call. REFUSE, do not rescue.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/**
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~152/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ro-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-1.AC1.sh; echo "exit=$?"</invocation><expect>harness rc=0; figures extra=0; the page absences covered N of N; EXPORT-COMPARE OK -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ro-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-1.AC2.sh; echo "exit=$?"</invocation><expect>THE DIFFERENCE CONTROL: the harness on round 38's committed body (17 extras) answers NOT OK -- harness on the stale body: rc=1 -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ro-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-1.AC3.sh; echo "exit=$?"</invocation><expect>the print package's tests pass, the cell's new ones among them (N passed, 0 failed) -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-ro-1" judgment="true"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-1.AC4.sh org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~152/judgment; echo "exit=$?"</invocation><expect>the rich export written beside the page's renders for a person to read; RECORDED, no verdict (one-line reason for a fourth criterion: the round-39 ruling requires a judgment criterion on a cell that touches served figures)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~152/AMGT_RESAPP.TO-AMGT-ro-1.the-export-adds-nothing.proof_of_spec.json`. Report once: what you changed and where, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.7 items 1 and 2. The data limb and the harness limb in one cell because the harness grades the data limb. Served only through ro-7's deploy. Disarm owner of Z-S268 stays `1.0.0_SA_CTO~Z`.

<status>pending</status>
<round>40</round>
<slot>~152</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
