# TO IRPT_ANLREQ.TO-AR-y-345.fwd1-driver-and-mint-helper-build -- BUILD the FWD-1 page driver (derived from the UI walker, with a four-POST allow-list and an order-token gate), its mint helper (a one-run bcrypt password held in memory only) and the synthetic holdings file; offline self-test only, nothing run against AWS or the portal

<to_id>IRPT_ANLREQ.TO-AR-y-345</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~149</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ6</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; source and tests only, the worker deploys NOTHING)
**Decomp cell:** `AR-y-345` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-343` (merged `833cacb2b7`), `AR-y-344` (merged `99599a99ed`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~149`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-149` (branch `wk-IRPT_ANLREQ-149`), provisioned by the issuer. Commit WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~149 <0.9.0_WK_IRPT_ANLREQ~149@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W149-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH, no deploy, no upload, no apply, no invoke, no AWS call. Scratch outside the product tree.

### THE CELL (`AR-y-345`, inlined)

*The FWD-1 run (PRD `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` lines about 28-38; CTO msg 7944: `0.7.0_AE_CloudOps~AQ2` mints the synthetic staff user and files through the DEV page) needs a DRIVER. Two reads settle its design (read both records first): `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~147/r41/FWD1_RUN_MECHANICS_READ.json` (`AR-y-343`: DEV is the local dev build at `http://localhost:5174`; a minted token cannot sign the page in; the four calls of the filing and the four attachment controls) and `.../0.9.0_WK_IRPT_ANLREQ~148/r41/FWD1_LOGIN_DRIVER_READ.json` (`AR-y-344`: a users row with a bcrypt `passwordHash` (cost 12), `status` active, a lower-case `email`, no `mfaEnabled`/`mfaChannel`, `firmId` `opal-capital` logs in through `POST /auth/login` on the password alone; the tracked hash helper is `hashPassword` in `infra/aws/opalinvest_dev/lambda/auth-handler/src/password.ts`; the walker `.claude/skills/ui-walk/walk.mjs` is read-only by construction, so the driver is a NEW script derived from it). This cell BUILDS the driver and its mint helper. NOTHING IS RUN against AWS or the portal by you: the run is AQ2's, under a never-widen pair that does not exist yet. You write, self-test offline and record.*

**What to build, all inside your deliverable folder `C:/dev/wk-irpt-anlreq-149/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/` (never edit `.claude/skills/ui-walk/` or any source file; copy the parts you need):**

1. **`fwd1_mint.py`** (Python 3.9 syntax; `bash .tools/commit-gate.sh <file>` passes): subcommands `mint` and `remove`, modelled on the release-29/30 sittings (read `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r30/sitting_r30.py` and `.../irpt_anlreq_r29/sitting_r29.py` for the table, key shapes, the conditional write, the removal and the ABSENT polling; reuse their approach and constants by reading, never by importing). `mint` reads ONE JSON object `{"password": "..."}` from STDIN (the driver's in-memory password; it never reads it from an argument, a file or the environment), hashes it with bcrypt at cost 12 (`bcrypt.hashpw(pw, bcrypt.gensalt(12))`, stored as `passwordHash`), and writes the row `PK USER#fwd1-staff-r41a@opal.invalid`, `SK PROFILE` with attributes: `email` `fwd1-staff-r41a@opal.invalid`, `passwordHash`, `status` `active`, `firmId` `opal-capital`, `role` `user`, `userType` `test-filer`, `name` `IRPT_ANLREQ FWD-1 synthetic staff`, and an `exp` TTL attribute 3 hours ahead, with `ConditionExpression attribute_not_exists(PK)`; NO `mfaEnabled`, NO `mfaChannel`, NO `allowedFirmIds`. `remove` deletes that row (`attribute_exists(PK)`), then polls a ConsistentRead get_item AND the `email-index` GSI query for up to 300 s and prints `ABSENT GSI <address>` and `ABSENT CONSISTENT <address>`; it exits non-zero if either is still present. Neither subcommand ever prints, logs or returns the password or the hash; stdout carries only the fixed status words above. The boto3 import and every AWS call sit inside the subcommand functions (a `--plan` of the driver, and the self-test, must never import boto3).
2. **`fwd1_driver.mjs`** (Node ESM, Playwright via the portal's `node_modules` the way `walk.mjs` lines 24-25 load it; Microsoft Edge with the bundled-Chromium fallback as `walk.mjs` lines 1603-1605): arguments `--base http://localhost:5174` (REFUSED unless the host is exactly `localhost`), `--firm 49financial`, `--holdings <path>`, `--out <dir>`, `--poll-minutes 20`, `--plan`, `--selftest`, and `--go <ORDER-ID>` (the run proceeds only with `--go IRPT_ANLREQ.TO-RUN-FWD1.<anything>` matching `^IRPT_ANLREQ\.TO-RUN-FWD1\.`; without it the driver prints the plan and exits 0). Steps, each logged with a UTC time and a screenshot: (1) generate the password in memory (`crypto.randomBytes`, at least 24 characters, never written); (2) call `python fwd1_mint.py mint` with the password on stdin; (3) launch the browser with the route guard and sign in through the real form exactly as `walk.mjs` lines 1645-1659 do (`#email`, `#password`, `button[type=submit]`, wait to leave `/login`); (4) open `/ticket-center`, start a new Analysis Request, CHOOSE the firm in the control labelled 'Choose the firm this request is filed under' (J7), fill the form for the variant Overview (read `AnalysisRequestParts.tsx` in `C:/dev/wk-irpt-anlreq-149/portal` and the selectors of the record), attach the holdings file with `setInputFiles` on the Holdings input (about `AnalysisRequestParts.tsx:213`), and click Submit (locate the Submit control's exact label and `data-slot` from the source and record them: the previous read could not); capture the ticket id from the response of `POST /api/scoped/tickets`; (4b) from then on the driver TOUCHES NOTHING: it only reads; (5) poll the ticket page (reload every 60 s, up to `--poll-minutes`) and record at each poll which of the four attachment items are present and openable (`open-package-original`, `form-as-filled`, `open-package-report`, `open-package-commentary`), stopping when all four are present or the time is up; (6) in a `finally` block ALWAYS call `python fwd1_mint.py remove` and record its two ABSENT lines; (7) write `run_report.json` (times, ticket id, per-poll presence, the guard's refusals, the ABSENT lines, the screenshot names; NEVER the password, hash, token or cookie).
   **The route guard** is a function `admit(method, url, base)` that returns true only for: GET, HEAD and OPTIONS to the base host or its API origin; and POST to exactly `/auth/login`, `/auth/refresh`, `/auth/logout`, `/api/scoped/investor-reporting/analysis/inputs`, `/api/scoped/tickets`, `/api/scoped/investor-reporting/analysis`, and `/api/scoped/tickets/<id>/report` (the path form `/api/scoped/tickets/[A-Za-z0-9_-]+/report`); everything else (any other POST, any PUT, PATCH or DELETE, any request to another host) is aborted and logged. Playwright's `page.route` uses it; the walker's telemetry-answer behaviour (`walk.mjs`: the portal's own telemetry is answered locally, never sent) is kept.
   **`--selftest`** (offline: no browser, no network, no AWS, no boto3 import) runs at least these cases and prints `SELFTEST-OK <n> cases` or `SELFTEST-BAD <which>` and exits 1: the guard admits each of the seven POST shapes and GETs; refuses a POST to `/api/scoped/tickets/abc/claim`, `/api/scoped/tickets/abc/complete`, a PUT, a DELETE and a POST to another host; the base check refuses `http://example.com`, `https://localhost.evil.com` and `http://localhost:5174.evil` and admits `http://localhost:5174`; two generated passwords differ and each is at least 24 characters; a redactor removes a known password and a known `refresh_token` value from a sample log line; `--plan` output lists the steps in order and, run as a subprocess with `PYTHONPATH` poisoned so that importing `boto3` would raise, exits 0 (proving plan mode never reaches AWS); without `--go` the run phase is refused.
3. **`fwd1_holdings_49financial.csv`**: the synthetic holdings file the R29 D1 sitting used (find `FILE_D1` in `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r29/sitting_r29.py`; copy its bytes to this CSV; columns `Ticker`, `Dollars`, `Acct Market Value`; it is a synthetic input of that sitting, not client data: say so in the record and confirm no real account number or client name appears).
4. **`FWD1_DRIVER_RECORD.json`** in `r41/`: `base`, `commit`, `files` (name, bytes, sha256), `selectors` (every selector and `data-slot` the driver uses, each with the source `file:line` where you read it), `submit_control` {label, data_slot, file, line}, `guard_admits` (the seven POST shapes), `selftest` {cases, output}, `hash_check` (see below), `run_requirements` (what the run needs on the box: node, Playwright from `portal/node_modules`, Edge, python bcrypt and boto3, the AWS profile of the applier), `claim`, `not_read` (the live portal, the live auth handler, any AWS state).

**Never:** run `fwd1_mint.py mint` or `remove`, call AWS, sign in anywhere, start the dev server, or print a password, hash, token or cookie. The selftest is offline.


### ACCEPTANCE

<criterion id="AR345-y-AC1" cell_refs="AR-y-345"><invocation>python C:/dev/wk-irpt-anlreq-149/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/driver_check.py</invocation><expect>^DRIVER-OK </expect></criterion>
`AR345-y-AC1`: you write `driver_check.py` in your deliverable folder: it runs `node --check fwd1_driver.mjs`, `python -m py_compile fwd1_mint.py`, then `node fwd1_driver.mjs --selftest`, and prints `DRIVER-OK <n> selftest cases` only when all three succeed and the selftest printed `SELFTEST-OK <n> cases` with n at least 12; otherwise `DRIVER-BAD <why>` and exit 1.

<criterion id="AR345-y-AC2" cell_refs="AR-y-345"><invocation>python C:/dev/wk-irpt-anlreq-149/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR345-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `fwd1_driver.mjs` to a scratch folder OUTSIDE the product tree with the guard changed to admit EVERY POST, runs that copy's `--selftest`, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR345-y-AC3" cell_refs="AR-y-345"><invocation>python C:/dev/wk-irpt-anlreq-149/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/hash_check.py</invocation><expect>^HASH-OK </expect></criterion>
`AR345-y-AC3`: you write `hash_check.py`: it imports the hashing function of `fwd1_mint.py` (import-safe: no AWS at import), hashes a random password, and prints `HASH-OK scheme=2b cost=12 python=ok bcryptjs=<ok|ABSENT>` only when the hash starts with `$2b$12$` (or `$2a$12$`), verifies with python bcrypt, and, when a `bcryptjs` package exists in any `node_modules` of this worktree (the portal's or the auth handler's; search those two folders only), also verifies with it through `node -e`; `bcryptjs=ABSENT` is printed (not a failure) when none is found; it never prints the password or the hash; otherwise `HASH-BAD <why>` and exit 1.

<criterion id="AR345-y-AC4J" cell_refs="AR-y-345" judgment="true"/>
`AR345-y-AC4J` (judgment, graded at L9, never by you): the driver files nothing without the order token, admits only the seven named POSTs, signs in through the real form, touches nothing after Submit, removes the minted user in a finally block, and never prints or writes the password, hash, token or cookie; the selectors and the Submit control are read from source.

<expected_criteria>AR345-y-AC1 AR345-y-AC2 AR345-y-AC3 AR345-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>

org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-345</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/IRPT_ANLREQ.TO-AR-y-345.fwd1-driver-and-mint-helper-build.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-345`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR345-y-AC1,AR345-y-AC2,AR345-y-AC3,AR345-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a script and a CSV in the worker's deliverable folder; nothing is run against AWS or the portal. The run is a later applier order under a never-widen pair.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed by the worker; any route this cell adds is source only and is served only after a later signed release. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the two records (AR-y-343, AR-y-344) and the walker's guard against the cell; the lens: a driver that mints or files without the order token, a guard that admits a POST it should refuse, a password in a log or an argument, a removal skipped on failure, a non-localhost base, a Submit selector guessed. The cell requires the token gate, the exact admit list, stdin-only password, a finally-block removal and selectors read from source. NOT seen (blind): the live system and the deployed bytes; denominator: 3 checkers, 12 or more selftest cases, 7 admitted POST shapes.
</preflight>


---

## RECORD FACE

- Cut on the findings of `AR-y-343` (merged 833cacb2b7) and `AR-y-344` (merged 99599a99ed). Workstream `ZZ6` of round 40. Base: `AR345-y-AC1`, `AC2`, `AC3` FAIL as expected (no checker files).
- The run itself is a later applier order to `0.7.0_AE_CloudOps~AQ2` under a never-widen pair (a minted internal user with a password, the filing, the producer-list address in use); nothing in this cell touches AWS or the portal.
