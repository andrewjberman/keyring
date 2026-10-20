# TO IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form -- PROVE OFFLINE: re-prove the run 7 browser-leg script against a local build of branch cand/dell2/anlreq-andrew-walk-v2 (the Advisor pre-filled and required), with the Advisor left as the page fills it; nothing is called on the network, nothing is filed, nothing is deployed

<to_id>IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~325</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ118</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a script copy and fixtures in the worker deliverables; a build in the worker's own portal worktree) | **Decomp cell:** `AR-y-459` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-2, FWD-1 and FWD-8 read through the page on PROD (run 7b, ADDENDUM 9 terms) | **depends_on:** CTO msgs 11385 and 11403 (the Advisor is always sent; run 7b leaves the pre-filled Advisor as it is), the tested script of order AR-y-454

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~325`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-325` (branch `wk-IRPT_ANLREQ-325`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~325 <0.9.0_WK_IRPT_ANLREQ~325@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W325-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>`.
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~323/IRPT_ANLREQ.TO-AR-y-454.run7-browser-leg-script-proved-offline-against-a-build-of-the-prod-tip.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (the blank-Advisor control below) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR459-y-AC1,AR459-y-AC2,AR459-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-459`, inlined)

*Context.* Run 7 STOPPED at B2: the PROD page dropped a blank Advisor and the ticket service requires it (400). The page on branch `cand/dell2/anlreq-andrew-walk-v2` always sends the Advisor, pre-fills it with the signed-in filer's name (editable), labels it required and holds a blank one with the words "Advisor is required. Add the advisor presenting this report to submit it." Run 7b files through that form on PROD as an unseeded synthetic Opal staff user and leaves the pre-filled Advisor as it is. The live run is one-shot, so the script must be re-proved BEFORE it is used. Your cell is that re-proof, offline.

*The build.* In `C:/dev/wk-irpt-anlreq-325/portal` (read-only for you: commit nothing there) run `git fetch origin`, `git checkout --detach d5d2fdeab3af8fcbc1f74ef2d5f2eefd7a89c3d3`, print `git diff --numstat 4546cee0528c1b2e21726666f8a97bf2f1f5f5bc HEAD` (it must list 12 files, all under `src/pages/TicketCenter/`; else STOP with a BLOCKING row), then `bun run build` (no network is needed; if it needs more than the linked node_modules, STOP with a BLOCKING row naming what).

*The script.* Create `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/` and copy into it from `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~323/`: `run7_browser_leg.mjs`, `fixtures_offline.json`, `holdings_sample.csv` (do not edit the originals). Read the new form at that tree (`portal/src/pages/TicketCenter/AnalysisRequestParts.tsx`, `TicketCenter.tsx`, `analysisRequest.ts`) and change YOUR copies so that: (a) the script does NOT type into or clear the Advisor in the normal path; it only reads the field's value and placeholder; (b) the B1 line prints `advisor=<optional|required|absent>` from the placeholder words, `advisor_prefilled=<yes|no>` (the field holds a non-empty value at first paint) and keeps every other B1 field; (c) the Needed-by control is no longer looked for (it is gone) and Other ETFs are not typed (the run files no extra ETF); (d) the fixtures give the stub session a non-empty user name so the Advisor is pre-filled (read how `ui-smoke` and the script build the stub session and what name the page reads: `auth.user?.name`), and answer every call the form makes; (e) a new option `--blank-advisor` clears the Advisor field before the one submit; with it the script prints the page's held words on the B2 line as `B2 filed REFUSED <the words>` and `CALLS` lists NO tickets create. Keep the single-submit rule, the closed-output rule, no Keep press, no token, URL or file content in any output. The composite `--offline` prints ONE final line `B-LEG-OFFLINE-OK b1_labels=<n> advisor=required advisor_prefilled=yes report_type=absent commentary=absent firms=3 models=5 b2_calls=<the call names in order, as the page makes them> b3_face=yes`, else `B-LEG-OFFLINE-BAD <why>`.

*Notes.* Record in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/PAGE_NOTES.md` the accessible names, the call sequence and every place the new form differs from what the copied script and ADDENDUM 9 assumed (read `PAGE_NOTES.md` of ~323 first). The issuer reads it before the GO.

---

## ACCEPTANCE

<criterion id="AR459-y-AC1" cell_refs="AR-y-459"><invocation>node org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/run7_browser_leg.mjs --offline --portal C:/dev/wk-irpt-anlreq-325/portal --dist C:/dev/wk-irpt-anlreq-325/portal/dist --fixtures org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/fixtures_offline.json --holdings org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/holdings_sample.csv --out org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/shots_offline</invocation><expect>^B-LEG-OFFLINE-OK b1_labels=[0-9]+ advisor=required advisor_prefilled=yes report_type=absent commentary=absent firms=3 models=5 b2_calls=\S+ b3_face=yes$</expect></criterion>
<criterion id="AR459-y-AC2" cell_refs="AR-y-459"><invocation>node org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/run7_browser_leg.mjs --offline --blank-advisor --portal C:/dev/wk-irpt-anlreq-325/portal --dist C:/dev/wk-irpt-anlreq-325/portal/dist --fixtures org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/fixtures_offline.json --holdings org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/holdings_sample.csv --out org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/shots_blank_advisor</invocation><expect>^B-LEG-OFFLINE-BAD b2 .*Advisor is required</expect></criterion>
<criterion id="AR459-y-AC3" cell_refs="AR-y-459"><invocation>cat org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/PAGE_NOTES.md org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/OFFLINE_STDOUT.txt | grep -c -E 'eyJ[A-Za-z0-9_-]{10,}|https?://|Bearer '</invocation><expect>^0$</expect></criterion>

(Save the stdout of the AC1 command as `OFFLINE_STDOUT.txt` in the same folder before AC3 is run.)

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR459-y-AC1,AR459-y-AC2,AR459-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-459</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a Node script copy, fixtures and notes in the worker deliverables, and a vite build in the worker's own portal worktree; no network call, no deploy, no filing, no token; nothing runs against PROD.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the CTO's rulings (msgs 11385, 11403) and the approval record of row 4664 against this cell; the lens: a script that passes offline because the fixtures answer more than the page asks (record every call in CALLS and compare with analysisRequest.ts), a pre-filled Advisor that only the fixture's stub name makes non-empty (the live filer's name is the real session's), a control the script cannot find reported as success, a second submit, a Keep press, a printed token or URL, a screenshot of a real name or figure (fixtures are synthetic), the blank-Advisor control that cannot fire. NOT seen (blind): the live PROD page for a real staff user (firm list, catalogue, the real user name), the live ticket view; denominator: three criteria.
</preflight>
