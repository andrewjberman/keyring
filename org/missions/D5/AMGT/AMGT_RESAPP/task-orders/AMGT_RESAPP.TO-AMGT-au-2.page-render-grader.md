# AMGT_RESAPP task order -- `AMGT-au-2` -- THE PAGE-RENDER GRADER REPAIRED (Z-W230-S1), THEN FWD-30's PAGE-AGAINST-EXPORT READ ON DEPLOYED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-au-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~232</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a tool repair and one read.
comp-iam: DECLARED-NOT-APPLICABLE -- invokes the deployed function read-only; no write.
comp-adversary: RUN by the issuer at the cut -- the round-45 grader fails at the base: `Cannot find module '@/ui/components/graphic/GraphicCard'` (row Z-W230-S1).
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/tmp/r71-232` (branch `wk-AMGT_RESAPP-232`, cut from the issuance commit with `--portal-ref e6ab82ad --node-modules link`, so `portal/` carries the DEV page and its `node_modules`). Work and commit only there. Start every shell call with `cd /c/tmp/r71-232`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-au-2` (round 71, decomposition s.79)

PRD v0.38 FWD-30 DONE WHEN (PRD `:824-831`): the export is a <=2-page Opal Brand presentation or machine-readable rich text, and "a
field-by-field comparison against the page shows the SAME figures, the SAME cites and the SAME absences, with NOTHING in the export that
is not on the page".

The grader is two files, `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/sweep.py` and `page_render.cjs` beside it. Run from `portal/`,
`page_render.cjs` transpiles `SecurityAnalysis.tsx` with TypeScript, swaps imports for stubs (`STUBS` / `SOURCE_STUBS`, ~`:41-112`) and
renders with `renderToStaticMarkup`; `sweep.py` reads the page's data attributes and compares them with the deployed rich export. It is
stale since the DSGN_AMGTV1 page changes.

1. **Copy both files into `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~232/grader/`** and repair the copies only (the originals are the issuer's record):
   - stub `@/ui/components/graphic/GraphicCard` and `@/ui/components/graphic/HeroGraphic` (with `PanelEyebrow` and `ICON_GLOW`), as
     `portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs:90-100` does (read it; do not edit it). The imports are in
     `LeadPanel.tsx:98-99`, `HeaderCards.tsx:14-15`, `SecurityOverlay.tsx:40`, `ThesisCards.tsx:29`;
   - add a `useCollectedChatter` stub to the hooks stub;
   - in `sweep.py`'s `_PageReader`, reset `self.years` at each header `<tr>`: the model sheet's "Consensus (Bloomberg)" group-header row
     shifts every year by one column;
   - point `sweep.py`'s render call at the copied `page_render.cjs`.
   A ratio shown with an `x` suffix (`117.6x`) is a number the reader must parse; repair that too.
2. **Run the FWD-30 read on DEPLOYED** for `BA_US_Equity`, `AMD_US_Equity` and `ASML_NA_Equity` (AC1).
3. **Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~232/FWD30_READ_ROUND71.md`:** per name, every remaining difference class (page-only figures, export-only figures,
   cases, value differences) with counts and five examples each, and for each class whether it is a PRODUCT difference (the page and the
   export really differ) or a GRADER fault. The issuer measured, on a scratch repair: about 539-629 export-only fiscal figures per name
   (including `ARD_*` rows), 3 export-only case lines per name (the page no longer renders cases, `ModelTab.tsx:7-8`), 17-18 page-only
   2026E-2028E figures per name, and 19 value differences, all `x`-suffixed ratios.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W232-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`. The grade of FWD-30 is the CVO's at L9; you read and classify, you do not grade.

## 2. BOUNDS

1. Write only the paths below. Read `portal/` only; never edit it. No deploy, no store write, no vendor or model call.
2. The grader's comparison rules stay as written except the repairs named in section 1.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~232/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-au-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~232/grader/sweep.py" --live --served --only BA_US_Equity,AMD_US_Equity,ASML_NA_Equity --cache "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~232/cache" --out "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~232/fwd30_r71.tsv" --diff; echo "exit=$?"</invocation><expect>a line `served over 3 of N folders: OK a, NOT_OK b, CAPTURE_FAILED 0` with a+b = 3; a `value facts over 3 compared names` line with compared above 0; a `FWD-30 GRADE:` line; exit printed (0 or 1: the grade is not this criterion)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-au-2" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~232 <0.9.0_WK_AMGT_RESAPP~232@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~232/AMGT_RESAPP.TO-AMGT-au-2.page-render-grader.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the repaired lines in each copy;
- the FWD-30 GRADE line and the classification table;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-70 analysis item 2, ruling 4; CTO msg 29615 (the ~600 differences are round-72 product work). AC2 is the CVO's L9 read of FWD30_READ_ROUND71.md: is each class correctly called product or grader. The issuer measured the repair on a scratch copy (scratchpad sweep_patched.py / page_render_patched.cjs: 416 of 459 -> 19 of 494 value differences).

<status>pending</status>
<round>71</round>
<slot>0.9.0_WK_AMGT_RESAPP~232</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-05 ~18:0xZ):** CLOSED -- drained @9b4e975093. AC1: renders 3 of 3, CAPTURE_FAILED 0; values equal 3 of 3 (1674 compared, 0 differ). AC2 (judgment) goes to CVO L9 via FWD30_READ_ROUND71.md. proof VALID. Rows Z-W232-S1/S2 INERT; disarms Z-W230-S1. The product differences (export-only fiscal figures 195-200 per name, page-only E-years, cases) are round-72 product work (CTO msg 29615).

<status>complete</status>
