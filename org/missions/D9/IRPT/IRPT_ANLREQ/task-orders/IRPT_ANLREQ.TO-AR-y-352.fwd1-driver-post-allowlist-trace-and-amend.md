# TO IRPT_ANLREQ.TO-AR-y-352.fwd1-driver-post-allowlist-trace-and-amend -- the FWD-1 run died because the driver's POST allow-list lacked the page's own directory/resolve call: trace every non-GET request the DEV Ticket Center page makes up to the Submit click, then amend the allow-list by the read-shaped ones ONLY; offline, no run

<to_id>IRPT_ANLREQ.TO-AR-y-352</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~153</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ13</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (source and a driver script in a deliverable folder; the browser is never launched, nothing is called, minted or filed)
**Decomp cell:** `AR-y-352` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~153`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-153` (branch `wk-IRPT_ANLREQ-153`), with a portal worktree `C:/dev/wk-irpt-anlreq-153/portal` (branch `wk-IRPT_ANLREQ-153-portal`) at `origin/DEV` provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~153 <0.9.0_WK_IRPT_ANLREQ~153@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W153-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call, NO network act, NO AWS call, NO push, you never launch a browser and never run the driver except with `--selftest` (offline). Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py` from inside it. Scratch outside the product tree.

### THE CELL (`AR-y-352`, inlined)

*Context. The FWD-1 run `r41` (applier `0.7.0_AE_CloudOps~AQ2`, record `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r31/A_RUN_FWD1.txt`, row `IRPT_ANLREQ-D2-S120`) signed a synthetic Opal staff user into the DEV portal build, then FAILED at step 4: the driver's route guard refused `POST /api/scoped/investor-reporting/directory/resolve`, so the Ticket Center's firm chooser never rendered. The guard (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs`, `POST_ALLOWED` lines about 34-42, the guard about lines 166-172, the self-test `--selftest` about lines 266-322) admits GET/HEAD/OPTIONS and exactly seven POST shapes: `/auth/login`, `/auth/refresh`, `/auth/logout`, `analysis/inputs`, `tickets`, `analysis`, `tickets/<id>/report`. An earlier read of the issuer (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~150/r41/STAFF_FIRMS_CATALOGUE_READ.json`, q1) found that the DEV chooser reads the Global firms through `loadAllowedFirms` in `portal/src/pages/TicketCenter/TicketCenter.tsx` (about lines 97-125 and the effect about 303-316) by `resolveDirectoryContext` in `portal/src/api/endpoints/investor-reporting.ts`, a POST to the directory route that WRITES NOTHING (a read-shaped call that happens to be a POST). The guard exists so that a synthetic run can WRITE only what the signed pair names (a ticket, an upload, an analysis, a report attachment); a read-shaped POST is not such a write, but nothing else may be added without the issuer and the CTO. The run is not retried until the allow-list is amended and the pair is re-signed: your cell is OFFLINE (source and the driver script only).*

1. **Q1, the full list.** From the sign-in landing (`/market` after `POST /auth/login`) through the Ticket Center page (`portal/src/pages/TicketCenter/`), New Ticket, type Analysis Request, the firm choice, choosing the holdings file, and the Submit click (`File Analysis Request`), list EVERY request the page can make whose method is not GET, HEAD or OPTIONS (a search over `portal/src/api/` and the pages' own calls; `fetchJson`, `postJson`, `apiClient`, `fetch(` and the endpoint clients `src/api/endpoints/*.ts` used by `TicketCenter.tsx`, `AnalysisRequestParts.tsx`, `analysisRequest.ts`, the shell around the page, and the auth refresh on mount). For each: method, path (templated), the caller `file:line`, WHEN it fires (on mount, when the form opens, when the type is chosen, when the firm is chosen, when the file is chosen, on Submit), whether it WRITES server state (`writes`) or is a read-shaped call (`read_shaped`), and whether the driver's `POST_ALLOWED` already admits it. Also list the portal telemetry call the driver already answers locally (`/analytics/ingest`) and say if any OTHER telemetry or logging POST exists.
2. **Q2, what the chooser waits on.** State, with `file:line`, the chain from opening the form to the firm selector being rendered (the label `Choose the firm this request is filed under`), and whether it depends on `directory/resolve` and on anything else that the guard could refuse. If a second blocking call exists, name it.
3. **Q3, the amendment.** Amend `fwd1_driver.mjs` (in `deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/`, the file the run order names) so that `POST_ALLOWED` gains ONLY the POST shapes that Q1 shows are `read_shaped` AND needed before or during the filing (the expected one: `^\/api\/scoped\/investor-reporting\/directory\/resolve$`, anchored exactly, no wildcard, no near-miss). A POST that WRITES and is not already among the seven is NEVER added: it goes in your record as a `needs_issuer` row and you stop on it. Keep the order-token gate, the localhost-only base and every other rule exactly as they are. Add self-test cases: the new shape is admitted; near-misses are REFUSED (`/directory/resolve/x`, `/directory/resolved`, `/api/scoped/investor-reporting/directory`, a path with a query suffix is admitted or refused exactly as the existing guard treats queries on the seven: say which); every existing refused shape stays refused; the seven are still admitted. Run `node fwd1_driver.mjs --selftest` (offline) and print the output.
4. **Q4, the record.** Write `r41/ALLOWLIST_AMEND.json` in your deliverable folder (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~153/`) with keys: `base` (your branch's base sha), `q1` {`requests` (a list of {`method`, `path`, `caller` {file, line, text}, `fires` (string), `class` (`writes`|`read_shaped`), `admitted_before` (true|false)}), `telemetry` (string), `evidence`}, `q2` {`chain` (a list of {step, file, line, text}), `blocking_calls` (a list of strings), `evidence`}, `q3` {`added` (a list of the exact regex source strings added to `POST_ALLOWED`), `needs_issuer` (a list of {method, path, why}), `driver_sha256_before`, `driver_sha256_after`, `selftest_cases_before` (29), `selftest_cases_after`, `selftest_output` (the printed lines), `near_misses_refused` (a list of strings)}, and `not_read` (the live portal bundle, the live run, whether the page makes a request the source does not show). Then write the three checker scripts named in ACCEPTANCE into your deliverable folder.

### ACCEPTANCE

<criterion id="AR352-y-AC1" cell_refs="AR-y-352"><invocation>node C:/dev/wk-irpt-anlreq-153/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs --selftest</invocation><expect>^SELFTEST-OK ([3-9][0-9]|[1-9][0-9][0-9]) cases$</expect></criterion>
`AR352-y-AC1`: the amended driver's offline self-test passes with at least 30 cases (29 before plus the new ones).

<criterion id="AR352-y-AC2" cell_refs="AR-y-352"><invocation>python C:/dev/wk-irpt-anlreq-153/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~153/allowlist_check.py</invocation><expect>^ALLOWLIST-OK </expect></criterion>
`AR352-y-AC2`: you write `allowlist_check.py`: it reads `POST_ALLOWED` from the committed base `fwd1_driver.mjs` (`git show <base>:<path>`) and from the amended file, and prints `ALLOWLIST-OK <n> added, seven kept` only when the seven base entries are all still present and unchanged, the added entries equal the record's `q3.added`, every added entry is an anchored exact path (starts `^` ends `$`, no `.*`, no `+`, no `|`), and each is in the record's `q1.requests` with class `read_shaped`; otherwise `ALLOWLIST-BAD <why>`, exit 1. It prints the denominator.

<criterion id="AR352-y-AC3" cell_refs="AR-y-352"><invocation>python C:/dev/wk-irpt-anlreq-153/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~153/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR352-y-AC3` (the one mutant that fails): you write `mutant_check.py`: it copies the amended driver to a scratch folder OUTSIDE the product tree with the new entry loosened to `/^\/api\/scoped\/investor-reporting\/directory\/.*$/`, runs `node <copy> --selftest`, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR352-y-AC4J" cell_refs="AR-y-352" judgment="true"/>
`AR352-y-AC4J` (judgment, graded at L9, never by you): Q1 lists the page's non-GET requests from source with callers, nothing that writes was added, the added shape is exact, and the record says plainly what it did not read.

<expected_criteria>AR352-y-AC1 AR352-y-AC2 AR352-y-AC3 AR352-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~153/` and this order's file (status flip only). The driver file `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs` is the ONE other file you edit (its `POST_ALLOWED` and the self-test cases only). Edit no other file of that folder, not the mint helper, the holdings file, `driver_check.py` or the earlier record.
- READ only: everything else, the portal above all. NO run of the driver except `--selftest`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-352</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~153/IRPT_ANLREQ.TO-AR-y-352.fwd1-driver-post-allowlist-trace-and-amend.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-352`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR352-y-AC1,AR352-y-AC2,AR352-y-AC3,AR352-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source reads and one driver script edited in a deliverable folder; the browser is never launched and nothing is called, minted or filed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the failed run's record (row S120), the driver's guard and the staff-firms read against the cell; the lens: a wildcard that admits more than the one read, a write-shaped POST added to make the page work, a second blocking call missed because the trace stopped at the first refusal, a self-test that never exercises the near-miss. The cell requires exact anchored shapes only, a stop on any write, a full trace from source, and a mutant that fails. NOT seen (blind): the live portal bundle and any request the source does not show; denominator: 4 questions, 1 driver file, 3 checker scripts, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on AQ2's run report (msg 8446, row `IRPT_ANLREQ-D2-S120`) after the FWD-1 run `r41` failed safely at step 4 (the synthetic user removed, ABSENT twice; nothing filed). Workstream `ZZ13` of round 40. Base: `AR352-y-AC1` reads SELFTEST-OK 29 cases (below the 30 the criterion needs), `AC2` and `AC3` FAIL as expected (no checker files).
- A second run is a NEW act the signed pair does not cover (the CTO's condition 3); the issuer writes a pair addendum from this record, the CTO signs it, and a new order goes to the applier. The driver's sha256 changes; the run order's pins are restated by that addendum.
