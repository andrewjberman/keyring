# TO-AR-g-179 -- the synthetic filing instrument can tick Opal-model comparables (a Multi-Comp filing) and file real-ticker holdings, proved offline

<to_id>IRPT_ANLREQ.TO-AR-g-179</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~335</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL3</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-179` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** none. Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~335`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-335` (branch `wk-IRPT_ANLREQ-335`), provisioned by the issuer, with the nested `portal/` worktree at the PROD tip `234cddba2d837df16380f039fad1c227a472d7e5` (read only for you; nothing is committed there). First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~335 <0.9.0_WK_IRPT_ANLREQ~335@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W335-S<k>` (check the channel file for `W335` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- ASCII only. Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`. No network, no AWS, no token, no push, no deploy.
- **The checks** are the acceptance invocations below; they print closed lines only. They run the instrument OFFLINE against the portal build you make (`bun run build` in the nested portal worktree, once; the build output `portal/dist` is gitignored and is not committed). If your result and an invocation's expectation differ, re-read the cell text before you doubt the check, and if you still believe the check is wrong file a BLOCKING row quoting both and stop on that criterion.

### THE CELL (`AR-g-179`, inlined)

**What this cell is.** The synthetic filing instrument of runs 7b to 7e (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/run7_browser_leg.mjs`, a Playwright script that drives the Ticket Center's New Analysis Request form) files an Overview: it counts the form's comparable checkboxes (`[data-slot="comparables"] input[type="checkbox"]`, each with `aria-label` = the model's label) but never ticks one. FWD-10's live read needs a Multi-Comp filing (two or more Opal models ticked), on HOLDINGS THAT CAN BE PRICED: the old holdings file uses `SYNTH-*` tickers, which no price tier knows, so a comparison section built from it could only say "not available". This cell gives the instrument a `--comparables` option and a real-ticker holdings file. The instrument is proved OFFLINE only; the live filing is a later CloudOps order.

**Do exactly this.**
1. Make the folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/`. Copy into it from `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/` the files `run7_browser_leg.mjs`, `fixtures_offline.json` and `PAGE_NOTES.md` (read the notes first). Edit ONLY the copy of `run7_browser_leg.mjs`.
2. Add the flag `--comparables "<label>[,<label>...]"` (1 to 5 labels, comma separated, whitespace around a label trimmed). In phase B2, after the form is filled and BEFORE the one press of File Analysis Request, for each label find the checkbox `[data-slot="comparables"] input[type="checkbox"][aria-label="<label>"]`; there must be exactly one, else fail the leg with the leg's existing `Bad` error `comparable "<label>" not found` (phase b2; nothing is pressed); otherwise `check()` it. Then print the closed line `B2 comparables ticked=<n>`. Without the flag nothing is ticked and the behaviour is unchanged.
3. Request capture: register a listener for the filing's `POST` whose pathname ends `/investor-reporting/analysis` (the call `CALL_NAMES` names `analysis-request`), parse its JSON post data, and print the closed line `B2 request variant=<variant> comparison_keys=<n>` where `<variant>` is the body's `variant` (print the value only when it is one of auto, overview, comparison, multicomp, else `other`) and `<n>` is the length of its `comparison_keys` array (0 when absent). Print nothing else from the body. Add ` comparables=<ticked> variant=<variant> comparison_keys=<n>` to the end of the composite OK line (`B-LEG-OFFLINE-OK` / `B-LEG-OK`).
4. Print the five checkbox labels the form offers at B1 as ` model_labels=<label|label|...>` appended to the existing `B1 form ...` line (labels are catalogue text, not content), so the operator can choose labels from the closed line.
5. Create `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/holdings_fwd10.csv` with exactly these lines: `identifier,quantity,units` / `SPY,100,SHARES` / `AGG,200,SHARES` / `IWM,50,SHARES` / `EFA,80,SHARES` (public ETF tickers, no client data; the household is still the synthetic one).
6. In `PAGE_NOTES.md` of YOUR folder add a short section "Run 7f changes" (ASCII): the new flag, the two new closed lines, the new holdings file, the portal tip it was built against, and the one fact that the ETF comparable is entered through the form's Other ETFs chip input (not ticked) and is NOT exercised by this cell.
7. Build the portal once (`bun run build` in `C:/dev/wk-irpt-anlreq-335/portal`), run the three acceptance invocations, write the proof instance, commit your folder files (not `dist`, not `.scratch`), flip the order's `<status>` to complete on three PASS.

**Labels.** The invocations below use the labels `Opal Short-Term` and `Opal Long-Term`. If the B1 line's `model_labels` shows that the form's labels differ, STOP, file a BLOCKING row quoting the B1 line, and change nothing else.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR179-g-AC1" cell_refs="AR-g-179"><invocation>node org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/run7_browser_leg.mjs --offline --portal C:/dev/wk-irpt-anlreq-335/portal --dist C:/dev/wk-irpt-anlreq-335/portal/dist --fixtures org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/fixtures_offline.json --out C:/dev/wk-irpt-anlreq-335/.scratch/shots179 --holdings org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/holdings_fwd10.csv --comparables "Opal Short-Term,Opal Long-Term"</invocation><expect>B-LEG-OFFLINE-OK .*comparables=2 variant=multicomp comparison_keys=2</expect></criterion>

<criterion id="AR179-g-AC2" cell_refs="AR-g-179"><invocation>node org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/run7_browser_leg.mjs --offline --portal C:/dev/wk-irpt-anlreq-335/portal --dist C:/dev/wk-irpt-anlreq-335/portal/dist --fixtures org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/fixtures_offline.json --out C:/dev/wk-irpt-anlreq-335/.scratch/shots179 --holdings org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/holdings_fwd10.csv</invocation><expect>B-LEG-OFFLINE-OK .*comparables=0 .*comparison_keys=0</expect></criterion>

<criterion id="AR179-g-AC3" cell_refs="AR-g-179"><invocation>node org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/run7_browser_leg.mjs --offline --portal C:/dev/wk-irpt-anlreq-335/portal --dist C:/dev/wk-irpt-anlreq-335/portal/dist --fixtures org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/fixtures_offline.json --out C:/dev/wk-irpt-anlreq-335/.scratch/shots179 --holdings org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/holdings_fwd10.csv --comparables "No Such Model"</invocation><expect>B-LEG-OFFLINE-BAD .*comparable .No Such Model. not found</expect></criterion>

<expected_criteria>AR179-g-AC1,AR179-g-AC2,AR179-g-AC3</expected_criteria>

- AC1: with two Opal models ticked the offline filing succeeds and the request it sends is a multicomp with two comparison keys. At base it FAILs (the copy of the instrument does not exist yet).
- AC2: with no flag the filing is unchanged and sends no comparison key. At base it FAILs (no copy yet; the old script has no such closed line).
- AC3: an unknown comparable label is refused by name before anything is pressed. At base it FAILs (no copy yet).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-179.filing-instrument-ticks-opal-model-comparables-and-files-real-tickers.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-179`.
<owned_cells>AR-g-179</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR179-g-AC1,AR179-g-AC2,AR179-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/IRPT_ANLREQ.TO-AR-g-179.filing-instrument-ticks-opal-model-comparables-and-files-real-tickers.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-179`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR179-g-AC1,AR179-g-AC2,AR179-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- a script and a CSV in the worker folder, run offline against a local portal build; no deploy, no AWS call, no network, no token, nothing pressed on any live page.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: all three criteria FAIL at base (the copy does not exist). Traps: ticking by position instead of by the aria-label; a second press; printing request body content (only the closed variant word and the count are printed); the holdings file with a header or units the page does not accept (the old file's three columns are kept). NOT seen (blind): the live page at the PROD tip beyond the offline build, and whether the five labels read as assumed (the cell stops on a mismatch).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1, AC2 and AC3 FAIL (no copy of the instrument).
