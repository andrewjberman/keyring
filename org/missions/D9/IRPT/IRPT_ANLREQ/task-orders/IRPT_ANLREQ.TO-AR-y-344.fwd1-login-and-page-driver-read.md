# TO IRPT_ANLREQ.TO-AR-y-344.fwd1-login-and-page-driver-read -- the FWD-1 minted-user login read: every gate of POST /auth/login, the users row a login accepts without MFA, how a one-run password hash is produced, and what a page driver derived from the UI walker must change to file a ticket; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-y-344</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~148</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ5</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of source and a record; nothing is changed, called or deployed)
**Decomp cell:** `AR-y-344` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~148`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-148` (branch `wk-IRPT_ANLREQ-148`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~148 <0.9.0_WK_IRPT_ANLREQ~148@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W148-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`. No live call, NO PUSH, no AWS call of any kind, no edit of any source file. Scratch outside the product tree.

### THE CELL (`AR-y-344`, inlined) -- a READ. The product tree is not edited.

*Context. The FWD-1 run's DONE WHEN has a synthetic Opal staff user sign in to the portal and drive the Ticket Center PAGE (PRD lines about 28-38). The mechanics read (`AR-y-343`, merged, record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~147/r41/FWD1_RUN_MECHANICS_READ.json`, read its `q2`) found that a minted RS256 token cannot sign the PAGE in: the page's session is the HttpOnly `refresh_token` cookie that only `POST /auth/login` sets, and the page calls `/auth/refresh` on mount. The only precedent for a page sign-in by a non-person is the UI walker (`.claude/skills/ui-walk/SKILL.md`, `.claude/skills/ui-walk/ui_walker_account.py`): a dormant users-table row with a password hash, armed for one walk with a random password held in SSM. The issuer must know, from SOURCE, exactly what a minted users row needs for `/auth/login` to accept it, so the run can mint a row WITH a one-run password and sign it in through the real login. The auth handler source is under `C:/dev/wk-irpt-anlreq-148/infra/aws/opalinvest_dev/lambda/auth-handler/src/` (the order of `AR-y-343` named a different path: row W147-S7).*

Answer these four questions from SOURCE, each with `file:line` evidence read from the worktree (print the lines you cite; a line you did not read is not cited):

1. **Q1, the login gates.** Trace `POST /auth/login` in `index.ts` and `auth.ts`: every check between the request and the `Set-Cookie` of the refresh token, in order: the origin check (`originVerify.ts`: which `Origin` or header is required, and does a request from `http://localhost:5174` pass), throttling (`throttle.ts`: per what key, how many tries, what lockout), the user lookup (which table, which key or GSI, which attributes), `status`, the password check (`password.ts`: the hash scheme and its parameters, a pepper or secret if any, the exact stored attribute name and format), the breached-password check (`breached-passwords.ts`: does it apply at login or only at set-password), MFA (`mfa.ts`: when is a second factor required, what flags or `userType` values skip it), and device trust (`deviceTrust.ts`). For each gate say `applies`, `skipped for userType Dev` (or whichever condition), or `not at login`, with the lines.
2. **Q2, the row a login accepts.** From Q1 list the exact attributes of a users-table row for which login succeeds WITHOUT mfa and without a person: key shape (`USER#<id>`/`PROFILE` or the email form), `email` and the GSI, `status`, the password attribute, `userType`, `role`, `firmId`, anything MFA/device related, and the claims the issued access token carries (`jwt.ts`: `tier`, `firmId`, `userType`, `allowedFirms`: what computes them for a staff row, and whether a `firmId` of `opal-capital` with `userType` `test-filer` (the R29 recipe) gets `tier internal`). Then read `ui_walker_account.py` and state how the walker row differs (it is `Dev`, role admin) and which of those differences matter for login.
3. **Q3, minting a password hash.** How would a minting script produce the stored password attribute for a random one-run password (the hashing library and parameters in `password.ts`; the same library the walker's `ui_walker_account.py` uses, if any)? Is there a tracked helper that does it? Does anything validate password strength or history at the point of a direct row write (no: only at the handlers; confirm)? Where does the walker keep its password (SSM `/opal/ui-walker/password`) and could a minted row hold a password that only the driving process knows (held in memory, never written)? State plainly whether that is possible without any change to the auth handler.
4. **Q4, the page driver.** Read how the walker drives a browser (`.claude/skills/ui-walk/`): the engine file, the library (Playwright?), how it signs in through the login form, how it restricts requests (the network guard) and what it must change to ALLOW the four POSTs of the filing (`/api/scoped/investor-reporting/analysis/inputs`, `/api/scoped/tickets`, `/api/scoped/investor-reporting/analysis`, `/api/scoped/tickets/<id>/report`) and a file upload, and to click Submit. Does any tracked page-driver already file a ticket (a name search in `portal/e2e/`, `portal/tests/`, `.claude/skills/`)? State plainly whether the smallest honest FWD-1 driver is a NEW script derived from the walker (name its parts) or an existing one. End with ONE line: `RECOMMEND: MINT_WITH_PASSWORD` or `RECOMMEND: API_DRIVE_ONLY` or `RECOMMEND: NEEDS <what>`, and the one fact that decides it (MFA, a throttle or the origin check are the likely deciders).


### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-148/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~148/r41/FWD1_LOGIN_DRIVER_READ.json` with keys: `base` (the sha your branch started from), `q1` {`gates` (a list of {`gate`, `applies` (`applies`|`skipped`|`not_at_login`), `condition` (string), `evidence` {file, line, text}}), `origin_localhost_passes` (`yes`|`no`|`unknown`)}, `q2` {`row_attributes` (a list of {name, value_or_form}), `token_claims` (a list of strings), `test_filer_gets_tier_internal` (`yes`|`no`|`unknown`), `walker_differences` (a list of strings), `evidence` (list)}, `q3` {`hash_scheme` (string), `helper_exists` (true|false), `helper` (string or null), `strength_checked_on_direct_write` (`yes`|`no`|`unknown`), `password_in_memory_only_possible` (`yes`|`no`|`unknown`), `evidence` (list)}, `q4` {`driver_library` (string), `signin_method` (string), `guard_changes_needed` (a list of strings), `existing_filing_driver` (true|false), `smallest_honest_driver` (string), `recommend` (`MINT_WITH_PASSWORD`|`API_DRIVE_ONLY`|`NEEDS`), `deciding_fact` (string), `evidence` (list)}, and `not_read` (what you did not read: the live system, the deployed bytes). Then write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~148/shape_check.py` and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~148/cite_check.py` named below. Every cited `{file, line, text}` is a path relative to the worktree root.

<criterion id="AR344-y-AC1" cell_refs="AR-y-344"><invocation>python C:/dev/wk-irpt-anlreq-148/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~148/shape_check.py</invocation><expect>^SHAPE-OK </expect></criterion>
`AR344-y-AC1`: `shape_check.py` loads `r41/FWD1_LOGIN_DRIVER_READ.json` and prints `SHAPE-OK <keys>` only when every key above is present with an allowed value (`q1.origin_localhost_passes`, `q2.test_filer_gets_tier_internal`, `q3.password_in_memory_only_possible`, `q4.recommend` in their enums) and every answer block has at least one evidence item; otherwise `SHAPE-BAD <why>`, exit 1.

<criterion id="AR344-y-AC2" cell_refs="AR-y-344"><invocation>python C:/dev/wk-irpt-anlreq-148/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~148/cite_check.py</invocation><expect>^CITES-OK </expect></criterion>
`AR344-y-AC2`: `cite_check.py` re-opens every `{file, line, text}` of the record and prints `CITES-OK <n> of <n>` only when each cited line number exists and the cited `text` is a substring of that line (after stripping); a miss prints `CITES-BAD <file>:<line>` and exits 1. It prints the denominator n.

<criterion id="AR344-y-AC3J" cell_refs="AR-y-344" judgment="true"/>
`AR344-y-AC3J` (judgment, graded at L9, never by you): the answers follow from the cited lines, a "not found" is said plainly with what was searched, and the recommendation is the one the evidence supports.

<expected_criteria>AR344-y-AC1 AR344-y-AC2 AR344-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~148/` and this order's file (status flip only). You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-344</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~148/IRPT_ANLREQ.TO-AR-y-344.fwd1-login-and-page-driver-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-344`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR344-y-AC1,AR344-y-AC2,AR344-y-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the cell against the answer shape; the lens: an answer asserted without a read line, a 'not found' said without a search, a binding assumed set because a name exists, a recommendation that widens beyond the cell. The cell requires cited lines checked by script, a stated search for every absence, and a stated recommendation. NOT seen (blind): the live system and the deployed bytes; denominator: 4 questions, each answered with cited lines.
</preflight>

---

## RECORD FACE

- Cut while leg L waits on its applier and the run waits on Andrew's f61b. Workstream `ZZ5` of round 40. Risk LOCAL. Base: `AR344-y-AC1` and `AC2` FAIL as expected.
- Its output decides whether the FWD-1 run drives the page (a minted user with a one-run password, signed in through the real login, a driver derived from the UI walker) or only the API; nothing is changed by this cell.
