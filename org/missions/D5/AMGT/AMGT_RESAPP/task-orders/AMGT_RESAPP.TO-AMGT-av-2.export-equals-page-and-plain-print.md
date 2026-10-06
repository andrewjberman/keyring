# AMGT_RESAPP task order -- `AMGT-av-2` -- THE EXPORT EQUALS THE PAGE (FWD-30) AND THE PRINT READS IN PLAIN WORDS (FWD-5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-av-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~238</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- the export already reads `thesis_bundle`; no write.
comp-adversary: RUN by the issuer at the cut -- r72 c41 FAILS on deployed: the 3 prints carry 2,389 raw field-code tokens (BA 733, AMD 810, ASML 846); the repaired au-2 grader reads FWD-30 equal 0 of 3.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r72-238` (branch `wk-AMGT_RESAPP-238`, cut from the issuance commit with `--portal-ref a3ab197f --node-modules link`, so `portal/` carries the DEV page and its `node_modules`). Work and commit only there. Start every shell call with `cd /c/tmp/r72-238`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-av-2` (round 72, decomposition s.80)

PRD v0.39 DONE WHENs: FWD-30 (PRD `:838-844`), a field-by-field comparison shows the SAME figures, cites and absences, with
NOTHING in the export that is not on the page. FWD-5 (`:521-525`): the printed pack reads as a document in Opal Brand form, with no
raw code.

Both live in `lib/research/print/render_pack.py`. **Change the export, never the page** (the page is DSGN's).
1. **FWD-30, in `build_rich_text` (~`:866`):**
   - **Class 1:** the history rows are limited to the page's model-sheet rows (`portal/src/pages/SecurityAnalysis/modelSheet.ts:97-170`,
     read only), at ~`:913-921` and ~`:968`.
   - **Class 2:** add the 2026E-2028E forecast rows the page shows, from `thesis_bundle.forecast_figures`.
   - **Class 3:** the model note (`_model_sheet_notes_markdown`, ~`:804-820`) states the years actually carried, forecasts included.
   - **Class 4:** drop the cases section (~`:1005`); the page no longer renders cases.
2. **FWD-5, in the PDF pack (`build_pack`; the field-code dump is ~`:300-311`):** every line renders a plain label, with no
   `UPPER_UNDERSCORE` code. Use the page's own labels (`modelSheet.ts`) or a plain-words map in the module.
3. **Plant tests** in `lib/research/print/` for both.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W238-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. The page and the page's files are read only. No value changes in either the export or the print.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/print/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~238/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-av-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_served.py" --cell c41 --where local; echo "exit=$?"</invocation><expect>the 3 prints each read with pages above 0 and tokens 0; C1 PASS tokens 0; R72 C41 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-av-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~232/grader/sweep.py" --live --only BA_US_Equity,AMD_US_Equity,ASML_NA_Equity --cache "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~238/cache" --out "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~238/fwd30_r72.tsv" --diff; echo "exit=$?"</invocation><expect>the export is built IN PROCESS on this tree (no --served); a `FWD-30 GRADE: equal 3 of 3 identified names; values equal 3 of 3` line; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~238 <0.9.0_WK_AMGT_RESAPP~238@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~238/AMGT_RESAPP.TO-AMGT-av-2.export-equals-page-and-plain-print.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the print suite's last line;
- the plain-label map's source;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-71 analysis items 2 and 3a, ruling 3. The repaired grader is ~232's (drained @9b4e975093). Served by av-8.

<status>pending</status>
<round>72</round>
<slot>0.9.0_WK_AMGT_RESAPP~238</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-05 ~22:4xZ):** CLOSED -- drained @39e8abe250. On the shared tree, c41 local reads 0 field-code tokens over 3 prints (from 2,389), YES. Worker AC2: FWD-30 grader equal 3 of 3, 1736 compared, 0 differ. Print suite 53 passed. proof VALID. Row Z-W238-S1 INERT. Served by av-8.

<status>complete</status>
