# TO-AR-g-193 -- the filing instrument types a ticker into the form's Other ETFs field (for run 7M)

<to_id>IRPT_ANLREQ.TO-AR-g-193</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~383</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL13</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-193` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** AR-g-179 (merged). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~383`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-383` (branch `wk-IRPT_ANLREQ-383`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~383 <0.9.0_WK_IRPT_ANLREQ~383@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W383-S<k>` (check the channel file for `W383` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- ASCII only. Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`. No network, no AWS, no token, no push, no deploy.
- **The checks** are the acceptance invocations below; they print closed lines only. They run the instrument OFFLINE against the portal build you make (`bun run build` in the nested portal worktree `C:/dev/wk-irpt-anlreq-383/portal`, once; `portal/dist` is gitignored and is not committed). If your result and an invocation's expectation differ, re-read the cell text before you doubt the expectation, and if you still believe it is wrong file a BLOCKING row quoting both, and stop on that criterion.

### THE CELL (`AR-g-193`, inlined)

**What this cell is.** The synthetic filing instrument (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/run7_browser_leg.mjs`, cell AR-g-179, a Playwright script that drives the Ticket Center's New Analysis Request form) ticks Opal model comparables with `--comparables` but never types into the form's **Other ETFs** field (an input with `aria-label="Other ETFs"`, placeholder "Other ETFs (tickers, comma- or space-separated)", in the portal at `portal/src/pages/TicketCenter/AnalysisRequestParts.tsx`; its tickers are parsed by `portal/src/pages/TicketCenter/analysisRequest.ts`, "The 'Other ETFs' field's tickers: comma- or space-separated, blanks dropped, repeats dropped"). Run 7M (one live Multi-Comp: two Opal models plus one typed ETF) needs that. This cell gives the instrument a `--other-etfs` option. The instrument is proved OFFLINE only; the live filing is a later CloudOps order.

**Do exactly this.**
1. Make the folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/`. Copy into it from `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~335/` the files `run7_browser_leg.mjs`, `fixtures_offline.json`, `PAGE_NOTES.md` and `holdings_fwd10.csv` (read PAGE_NOTES.md first). Edit ONLY the copy of `run7_browser_leg.mjs` (and append to your copy of PAGE_NOTES.md).
2. Add the flag `--other-etfs "<ticker>[,<ticker>...]"` (1 to 5 tickers, comma separated, whitespace trimmed; each must match `[A-Z][A-Z0-9.]{0,9}` and be distinct, else fail the leg with the leg's existing `Bad` error `other-etfs needs one to five distinct tickers` in phase setup; nothing is pressed). In phase B2, after the form is filled and the comparables are ticked, and BEFORE the one press of File Analysis Request, type the tickers into the input `input[aria-label="Other ETFs"]` (separated by a comma and a space; use `fill`, then confirm the input holds the typed text) and print the closed line `B2 other_etfs=<n>` (n = the count typed). Without the flag nothing is typed and nothing new is printed.
3. Append ` other_etfs=<n>` (0 when the flag is absent) at the very END of the composite OK line (`B-LEG-OFFLINE-OK` / `B-LEG-OK`), after the existing `comparison_keys=<n>`. The existing `B2 request variant=<variant> comparison_keys=<n>` line already counts the filing body's `comparison_keys`; it must read 3 with two comparables and one typed ETF, and the variant `multicomp`.
4. Do not change anything else in the file: the earlier behavior (no flag) must print exactly what the AR-g-179 copy prints, plus the trailing ` other_etfs=0`.
5. In YOUR `PAGE_NOTES.md` add a short section "Run 7M changes" (ASCII): the new flag, the new closed line, the trailing field, and that the typed ETF is classified and priced by the resident, not by this instrument.
6. Build the portal once (`bun run build` in `C:/dev/wk-irpt-anlreq-383/portal`), run the three acceptance invocations, write the proof instance, commit your folder files (not `dist`, not `.scratch`), flip the order's `<status>` to complete on three PASS and a VALID proof.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR193-g-AC1" cell_refs="AR-g-193"><invocation>node org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/run7_browser_leg.mjs --offline --portal C:/dev/wk-irpt-anlreq-383/portal --dist C:/dev/wk-irpt-anlreq-383/portal/dist --fixtures org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/fixtures_offline.json --out C:/dev/wk-irpt-anlreq-383/.scratch/shots193 --holdings org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/holdings_fwd10.csv --comparables "Opal Short-Term,Opal Long-Term" --other-etfs "VNQ"</invocation><expect>B-LEG-OFFLINE-OK .*comparables=2 variant=multicomp comparison_keys=3 other_etfs=1$</expect></criterion>

<criterion id="AR193-g-AC2" cell_refs="AR-g-193"><invocation>node org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/run7_browser_leg.mjs --offline --portal C:/dev/wk-irpt-anlreq-383/portal --dist C:/dev/wk-irpt-anlreq-383/portal/dist --fixtures org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/fixtures_offline.json --out C:/dev/wk-irpt-anlreq-383/.scratch/shots193 --holdings org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/holdings_fwd10.csv --comparables "Opal Short-Term,Opal Long-Term"</invocation><expect>B-LEG-OFFLINE-OK .*comparables=2 variant=multicomp comparison_keys=2 other_etfs=0$</expect></criterion>

<criterion id="AR193-g-AC3" cell_refs="AR-g-193"><invocation>node org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/run7_browser_leg.mjs --offline --portal C:/dev/wk-irpt-anlreq-383/portal --dist C:/dev/wk-irpt-anlreq-383/portal/dist --fixtures org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/fixtures_offline.json --out C:/dev/wk-irpt-anlreq-383/.scratch/shots193 --holdings org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/holdings_fwd10.csv --comparables "Opal Short-Term,Opal Long-Term" --other-etfs "vnq!"</invocation><expect>B-LEG-OFFLINE-BAD .*other-etfs needs one to five distinct tickers</expect></criterion>

<expected_criteria>AR193-g-AC1,AR193-g-AC2,AR193-g-AC3</expected_criteria>

- AC1: the offline leg with two ticked models and one typed ETF files a multicomp body with 3 comparison keys and reports other_etfs=1. At base it FAILs (the flag does not exist).
- AC2: without the new flag the leg is unchanged and reports other_etfs=0. At base it FAILs (no trailing field).
- AC3: a malformed ticker fails the leg before anything is pressed. At base it FAILs (unknown flag).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-193.filing-instrument-types-an-etf-into-the-other-etfs-field.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-193`.
<owned_cells>AR-g-193</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR193-g-AC1,AR193-g-AC2,AR193-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~383/IRPT_ANLREQ.TO-AR-g-193.filing-instrument-types-an-etf-into-the-other-etfs-field.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-193`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR193-g-AC1,AR193-g-AC2,AR193-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- a copy of the synthetic filing instrument under the worker's own deliverables folder, proved offline against a local portal build; no network, no AWS, no token; nothing is deployed or run on a host.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: all three criteria FAIL at base (flag and trailing field absent); the expectations were written from the AR-g-179 order's own closed-line grammar. Traps: changing the no-flag behavior, ticking instead of typing, pressing Keep, printing the typed content beyond the count. NOT seen (blind): the live page; the resident's pricing of the typed ETF (run 7M reads it).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1, AC2 and AC3 all FAIL.
