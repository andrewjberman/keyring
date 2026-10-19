# TO IRPT_ANLREQ.TO-AR-y-400.upload-door-not-authorized-versus-the-mint-code-read -- READ ONLY: trace the upload door's NOT_AUTHORIZED predicate (the route, the user-row fields and token claims it reads) against what the synthetic mint writes, by key name and type, and name what the minted row lacks that a real staff row carries

<to_id>IRPT_ANLREQ.TO-AR-y-400</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~294</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ61</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (read-only; one record file and optional surprise rows)
**Decomp cell:** `AR-y-400` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none (CTO ruling addendum 2, msg 10662)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~294`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-294` (branch `wk-IRPT_ANLREQ-294`), provisioned by the issuer from the current branch (sparse). First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~294 <0.9.0_WK_IRPT_ANLREQ~294@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. A row id has the form `IRPT_ANLREQ-D2-W294-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions). No non-ASCII in what you add.
- **READ ONLY.** You change no source file, run no AWS call, no network call, no deploy. You write ONE record file and, if you find something odd off the task, rows. Read code with the Read, Grep and Glob tools (a named folder or file, never a blind search of the whole repository) and `git show HEAD:<path>`; cite every answer as `<path>:<line>` read from the file at HEAD of your worktree (print the line, do not recall it).

### THE CELL (AR-y-400, inlined)

*Context.* A fresh synthetic run (IB2, order `org/tier2_senior/0.7.0_AE_CloudOps~IB2/task_orders/IRPT_ANLREQ.TO-RUN-COMMENTARY-E2E.fresh-synthetic-commentary-end-to-end-ib2.md`, receipt `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e/A_E2E.txt`) minted one synthetic staff user (`A mint ok`), logged in (`L login ok`) and was REFUSED at the upload (`U upload REFUSED NOT_AUTHORIZED`). Window 4 (2026-10-16) was refused at the same door with the same code (surprise investigation lines 22817-22823 of `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`). The door is `POST /api/scoped/investor-reporting/analysis/inputs` (`infra/aws/lambda/investor-reporting/intake/upload_entry.py:21`, logic in `intake/uploads.py`); the authorization code that builds the caller's principal from the users row and token is under `infra/aws/lambda/investor-reporting/_authz/` (`served.py` is the main file) and `_scope/` (`interactive_access.py`, `ordinary_viewer.py`); `NOT_AUTHORIZED` appears in `_authz/served.py`, `intake/uploads.py`, `_scope/interactive_access.py`, `_scope/ordinary_viewer.py`, `_scope/maintained_sources.py`, `holdings/errors.py` and `ops/entry.py` among others. The synthetic mint is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_mint.py` (`item_for` at about line 57 writes the users row: PK, SK, email, passwordHash, status, firmId, allowedFirmIds, role, userType, name, exp). The cell that last changed the mint is `TO-AR-y-373` (worker 167, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~167/`). The login code that builds a session token is in the ticket/auth service (find the module by name in `infra/aws/lambda/`, a named folder at a time).

*Questions. Answer each in ONE line of the record, labelled `V1` to `V6`, each line holding at least one `<file>.<ext>:<line>` citation (py, ts, tsx, mjs or md):*
- `V1` THE DOOR'S PATH: from `POST /api/scoped/investor-reporting/analysis/inputs` to the first authorization decision, the functions in order with file:line, and EVERY predicate on that path that can return or raise `NOT_AUTHORIZED` (one clause each: the condition and its line).
- `V2` THE PRINCIPAL: how the door builds the caller's principal from the users row and the token: the users-row attribute names and types it reads, the token claims it reads, and how each of `userType`, `role`, `firmId`, `allowedFirmIds` and `status` maps to `principal_class`, a firm placement or a permission (cite the mapping lines). Names and types only; no value of any secret.
- `V3` THE MINT: the attribute NAMES and DynamoDB TYPES `fwd1_mint.py` writes (read `item_for`), and the fixed non-secret values it writes for `status`, `role` and `userType` and the NAME of the firm constants it uses (do not print a password or hash).
- `V4` THE FIRST FAILURE: walking V1 with V3's row, the FIRST predicate the minted principal fails and the closed code branch it takes, or `NOT READ <what is missing>` if the code does not decide it from the row alone (for example a token claim the login adds that the mint cannot supply).
- `V5` THE REAL ROW: what a real staff user row (and the token claims the login issues for it) carries that the minted row lacks, from the login code and the users-table shape the code reads (cite the lines); the list of differences by NAME and TYPE, and the fixed values where the door compares one (for example a `userType` the door recognizes).
- `V6` THE CLASS: one of `MINT-GAP` (the door is right and the mint lacks a field or value), `DOOR` (the door refuses a principal it should admit), `UNDETERMINED`, with the one-clause reason and the citation. If `MINT-GAP`, name the exact edit to `fwd1_mint.py` `item_for` by attribute name and value (a LOCAL change the issuer would order), but make NO edit.

Anything you cannot answer from the code is written `V<k> NOT READ <what is missing>`; a guess is a defect. Write no secret, password, hash or token, and no client data.

---

## ACCEPTANCE

Record file: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~294/r53/DOOR_VERSUS_MINT.md` (create the folder). It holds a first line `# door versus mint` and then exactly the six lines `V1` to `V6`, each starting at column 0 with its label and a space, each answer on that single line.

<criterion id="AR400-y-AC1" cell_refs="AR-y-400"><invocation>grep -c -E "^V[1-6] " org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~294/r53/DOOR_VERSUS_MINT.md</invocation><expect>^6$</expect></criterion>
<criterion id="AR400-y-AC2" cell_refs="AR-y-400"><invocation>grep -c -E "^V[1-6] .*[A-Za-z_0-9]+\.(py|ts|tsx|mjs|md):[0-9]+" org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~294/r53/DOOR_VERSUS_MINT.md</invocation><expect>^[5-6]$</expect></criterion>

`AR400-y-AC1`: the six labelled answers exist; at base the record is absent and it FAILS. `AR400-y-AC2`: at least five of the six lines carry a `file:line` citation; at base it FAILS.

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~294/IRPT_ANLREQ.TO-AR-y-400.upload-door-not-authorized-versus-the-mint-code-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-400`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR400-y-AC1,AR400-y-AC2"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-400</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, the deliverables folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~294/`, this order's file (status line only) and the surprise investigation file are the only places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~294/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-400.upload-door-not-authorized-versus-the-mint-code-read.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of code and one record file; nothing is built, uploaded, planned, applied, invoked or called.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- a predicate recalled instead of read (each line is printed from the file), a guess written as a finding (NOT READ is the honest answer), a secret or hash copied (forbidden), a test's mock read as the production predicate (cite the production module), a mint edit made (forbidden: read only). NOT seen (blind): the live users row and the token the login actually issued; denominator: six questions, two criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (`RULING_COMMENTARY_GAP_TWO_CAUSES_20261017.md` ADDENDUM 2, msg 10662) after the synthetic run stopped at the upload door with `NOT_AUTHORIZED` after a good mint and login. If the class is `MINT-GAP`, the fix is a LOCAL edit of `fwd1_mint.py` and a re-run under the same pair by addendum; if `DOOR`, its own WORLD cell and pair. The same door gates window 5 (held). Base: the record is absent, so `AR400-y-AC1` and `AR400-y-AC2` FAIL as expected.
