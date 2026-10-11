# TO DSGN_IRPTV1.TO-IV-e-111 -- ONE candidate cut off portal PROD holding only what release 5's return needs -- the history reader, the two missing irpt-status reads, retained_ref -- with none of it in the print route's import closure; pushed by nobody

<to_id>DSGN_IRPTV1.TO-IV-e-111</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~61</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5494 (2026-10-11 ~17:47Z): "Cut ONE candidate off PROD holding only what release 5's return needs: the history reader, the two missing irpt-status reads, retained_ref. Conditions, each measured: every changed file under src/pages/InvestorReporting or src/api/endpoints/investor-reporting.ts; NONE in the print route's import closure, shown from the build's chunk graph; CI green." | **Rows:** DSGN_IRPTV1-D2-W56-S2, DSGN_IRPTV1-D2-W56-S3, DSGN_IRPTV1-D2-W59-S2 | **Decomp cell:** `IV-e-111` (decomposition v25) | **outcome_ref:** FWD-1 (the history reader on PROD; IRPT_ANLREQ release 5's return follows it) | **depends_on:** IV-e-106 (drained: its record names what the range holds).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-61` (branch `wk-dsgn-irptv1-r25-61`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~61/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-61/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` is this worktree's OWN install, made by the issuer from PROD's lockfile: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~61/`) is your base for `new_failing_ids`.

**What changed.** IV-e-106's record (`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~59/PROD_CANDIDATE.json` and `.md`; read
both first) showed that the range from portal PROD `37aa1247ee` to DEV is 127 files and 127 commits, 67 of them other projects', touching
pages partner firms can open; and that the Investor Reporting ROUTE on PROD sits behind admin, the Opal firm and user type Dev (`src/App.tsx`
line 462), while the PRINT route (line 614) admits a render claim and so stays "unsure", which the push law reads as client-facing. The
CTO ruled: the whole range is not this project's to push. ONE candidate is cut off PROD with only what release 5's return needs. You push
NOTHING. The candidate goes to the CTO.

**Your portal worktree is at PROD**, `37aa1247ee` (branch `wk-dsgn-irptv1-r25-61-prodcut`), not DEV. DEV's tip is the commit
`ca23f110a25f43f952392054117c5b40942ad85f` (in this repo's object store: `git show ca23f110:<path>`, `git diff 37aa1247ee ca23f110 -- <path>`).

**The cell (`IV-e-111`).**
1. **What the candidate must carry, and nothing else:**
   - **the history reader** that reads irpt-status release 5's answer: `readOwnedHistory` in `src/pages/InvestorReporting/contracts/owned-requests.ts`
     as DEV has it (transitional: it takes the two-key answer and the contract answer; ruling (B), landed on DEV as `8ed372cb`, cell
     IV-e-99; record `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/` under the worker folder that executed IV-e-99, and the reader census
     `.../0.9.0_WK_DSGN_IRPTV1~56/READER_CENSUS.json`, which showed PROD's reader REFUSES release 5's answer);
   - **the two missing irpt-status reads** (row D2-W56-S2): the client methods and route-table rows for `analysis-request-pdf` and
     `analysis-request-original` in `src/api/endpoints/investor-reporting.ts`, and the envelope adapter for `-original`;
   - **`retained_ref`** carried by the sections reader (row D2-W56-S3; DEV's `9d3f43ef`, cell IV-e-106).
   Bring each from DEV by the smallest set of file changes that makes it work on PROD's tree: prefer `git checkout ca23f110 -- <file>`
   for a file whose whole DEV state is needed and whose DEV-only dependencies you also bring, and a hand-port of the hunks where a whole
   file would drag in an unrelated page change. Everything a carried file imports must exist on your branch (typecheck is the oracle).
   Their tests come with them. `carries`: for each of `history_reader`, `status_read_pdf`, `status_read_original`, `retained_ref`:
   {carried, where (file and line on your branch), test (the test id that holds it, passing on your branch)}.
2. **The path condition, measured.** `files` = `git diff --name-only 37aa1247ee <your HEAD>` (print the denominator): EVERY path is
   under `src/pages/InvestorReporting/` or is exactly `src/api/endpoints/investor-reporting.ts`. A change you need outside those paths is
   NOT made: it goes in `left_out` with why, and a row. `left_out`: [{what, why}] also lists what of this project's DEV work you
   deliberately did not bring (the Holdings face, the Opal wording, the Prospect opener, the labels, and so on), one line each.
3. **The print route's import closure, from the build's chunk graph.** Build your branch (`bun run build`; the portal is a vite build).
   Produce the module graph of the build (vite / rollup: a manifest with `build.manifest`, or the bundle's module ids through a
   one-off rollup plugin or `--debug`-style output; do it WITHOUT committing a config change: pass it on the command line or use an
   uncommitted temporary config you remove afterwards). From the PRINT route's entry (the component `src/App.tsx` line 614 renders),
   compute the set of source modules reachable by static and dynamic imports. `print_closure` {method (exactly what you ran), entry,
   closure_files, control {file, found}}: the control is a file you KNOW the print view imports (read the print component's own
   imports), found in the computed set; a closure that misses its control is a broken instrument, not a result.
   `changed_in_closure` = the changed files that are in that set.
   - Empty: `verdict: "CLEAR"`.
   - Not empty: do NOT hide it and do not restructure product code to dodge it beyond a clean, small separation you can justify (say
     so if you made one). If a needed file is in the closure, `verdict: "WAITS_ON_ANDREW"` with a row naming the files: the CTO ruled
     "Any file in that closure waits on Andrew."
4. `lint_errors`, `typecheck_errors`, `suite` {pass, fail} from `bun test src/pages/InvestorReporting` on your branch (PROD's own suite
   count is your base: run it before any edit and report both), `build_ok`. `candidate_commit` = your final portal HEAD; `pushed: false`.
   Record `PROD_CUT.json`, and a short `PROD_CUT.md` a principal can read: what the candidate changes, on which route, and what it leaves out.

<criterion id="IV111-AC1" cell_refs="IV-e-111"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r25/p25_round25.py" . IV111-AC1</invocation><expect>IV111-AC1 PASS</expect></criterion>
`IV111-AC1` -- the candidate is cut off PROD with every changed file under the allowed paths, and the history reader, both status reads and retained_ref carried, each with a test. Base: FAIL.

<criterion id="IV111-AC2" cell_refs="IV-e-111"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r25/p25_round25.py" . IV111-AC2</invocation><expect>IV111-AC2 PASS</expect></criterion>
`IV111-AC2` -- the print route's import closure is shown from the build's chunk graph with a control, no changed file is in it or the candidate is marked as waiting on Andrew, and lint, typecheck, the suite and the build are clean. Base: FAIL.

<expected_criteria>IV111-AC1,IV111-AC2</expected_criteria>

## AMENDMENT 1 (2.0.0_SA_COO~D2, 2026-10-11 ~18:5xZ) -- IV111-AC2's suite limb is "no new failure over PROD's base", not "0 failing"

The issuer wrote `suite.fail` 0 into IV111-AC2 without measuring PROD's own suite. The worker measured it (row DSGN_IRPTV1-D2-W61-S1):
PROD `37aa1247ee` reads 1088 pass, 27 skip, 42 fail against today's workspace contract, and the candidate reads 1101 pass, 27 skip,
the IDENTICAL 42 failing ids, none new. The worker reported the criterion FAIL as measured and did not repair files outside the cut,
which is what the order asked. The check now requires `suite.fail` equal to `suite.base_prod.fail` with `new_failing_ids` empty; every
other limb is unchanged. On the issuer's re-run at the drain (@1c99a27d31) IV111-AC1 and IV111-AC2 PASS, and the issuer flips the
order's `<status>` with this amendment, the worker having returned. Gate limb that graded this modification: none (a modification of an
issued order; LIMB 6 fires on a newly added order only).

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. The contract and the producer's fixtures (workspace files)
  are read, never edited. No file under `contracts/wire/` is hand-edited (generated; one command regenerates it:
  `bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts`).
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no
  `bun install`, no package change, no dev server on any port.
- **Every portal commit is followed by `bun run lint` and `bun run typecheck`**; a lint ERROR is fixed before you report (the count goes in
  the record as `lint_errors`, and typecheck's as `typecheck_errors`).
- **Synthetic data only** in any fixture, screenshot or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W61-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~61/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-111.prod-cut-history-reader-status-reads-retained-ref.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v25 (round 25), cell `IV-e-111`.
<owned_cells>IV-e-111</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV111-AC1,IV111-AC2. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~61/DSGN_IRPTV1.TO-IV-e-111.prod-cut-history-reader-status-reads-retained-ref.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV111-AC1,IV111-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: both criteria's last lines; the candidate commit; the changed files (count and list); for each of the four carried things where it is and its test; what was left out and why; the print closure -- the method, its size, the control, and which changed files are in it; the verdict; PROD's base suite and yours; lint, typecheck, build; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a candidate branch cut off PROD, pushed by nobody; the CTO reads it; a PROD push of a file in the print route's closure waits on Andrew.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
