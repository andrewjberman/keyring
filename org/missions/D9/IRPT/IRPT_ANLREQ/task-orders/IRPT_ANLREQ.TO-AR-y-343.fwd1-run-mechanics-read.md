# TO IRPT_ANLREQ.TO-AR-y-343.fwd1-run-mechanics-read -- the FWD-1 run's mechanics read: what DEV is, how a minted staff user reaches the Ticket Center page, the form's fields and the order of its calls, how the four attachments are read back, and every precondition as a checkable fact; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-y-343</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~147</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ4</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of source and a record; nothing is changed, called or deployed)
**Decomp cell:** `AR-y-343` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~147`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-147` (branch `wk-IRPT_ANLREQ-147`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~147 <0.9.0_WK_IRPT_ANLREQ~147@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W147-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`. No live call, NO PUSH, no AWS call of any kind, no edit of any source file. Scratch outside the product tree.

### THE CELL (`AR-y-343`, inlined) -- a READ. The product tree is not edited.

*Context. FWD-1's DONE WHEN (PRD `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, lines about 28-38) is one live run ON DEV: a SYNTHETIC Opal staff user (minted and removed by `0.7.0_AE_CloudOps~AQ2`, the R29 recipe: an RS256 token minted in process, the users-table row `USER#<address>` / `PROFILE`) signs in, opens the Ticket Center, CHOOSES a partner firm, fills the Analysis Request form, uploads a holdings file and submits; nobody touches anything after Submit; the still-open ticket then carries four attachments. The CTO ruled (msg 7944) that AQ2 drives the filing through the DEV page. The issuer is about to write that run order and needs, from SOURCE and the tracked records, the exact mechanics: nobody has yet written down how an automated driver reaches the DEV page as a minted user and how the four attachments are read back.*

Answer these four questions from SOURCE, each with `file:line` evidence read from the worktree (print the lines you cite; a line you did not read is not cited):

1. **Q1, what 'DEV' is and how a driver reaches it.** What is the portal DEV environment for a run like this: a deployed site (its URL, how DEV is built and deployed from the `DEV` trunk, `portal/CONTRIBUTING-BOXES.md`, the NFRA_DEVPLN records under `org/` that name it) or the local dev build (`bun run dev --port 5174`, the protected dev channel the `ui-walk` skill uses)? Which API does each talk to (the shared API origin the ticket service and Investor Reporting sit behind)? Name the file and line that tells the portal which API base to use. Say which one the PRD's 'on DEV' means, with the quote that decides it.
2. **Q2, how a minted staff user signs in.** The portal's sign-in is a login to the auth handler (`infra/aws/users/`, `opalinvest_dev/lambda/auth-handler/`): can a minted user row plus a token minted in process stand in for a login, and where does the portal keep the session (a cookie, `localStorage`, a header)? Read the `ui-walk` skill (`.claude/skills/ui-walk/SKILL.md`) and the R28/R29/R30 sitting scripts (`org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r2*/` and `irpt_anlreq_r30/sitting_r30.py`: a name search inside those folders only) for how earlier drivers presented a token to the API, and whether any earlier run drove the portal PAGE (a browser) as a minted user or only called the API. State plainly: is a browser drive of the Ticket Center page as a minted user DOCUMENTED anywhere in tracked source or records? If yes, name the recipe; if no, say what the smallest honest drive is (a headless browser with the token placed where the portal reads it, versus the API calls the form makes, in the order `analysisRequest.ts` makes them).
3. **Q3, what the drive must do and read back.** From `portal/src/pages/TicketCenter/analysisRequest.ts` and `AnalysisRequestParts.tsx` (on the worktree's portal at `origin/PROD`; J7 `6f4e5f671f` and the reader `a17932990a` are on other refs: read them with `git -C <portal> show <sha>:<path>`), list the form fields, their selectors or labels (`data-slot` attributes) and the ORDER of the calls on Submit (ticket create, upload door, analysis submit, and any call that records the request id on the ticket). Then list how the four attachments are read back from the ticket page: the control or `data-slot` of each of the four items ('Original file', 'Form as filled', 'Report', 'Commentary') and the route each one opens (the signed-link readers), so a check can assert each is present and openable. Name the holdings test file the run should upload: the tracked synthetic holdings CSV or XLSX of the earlier sittings (a name search for the file the R29 D1 / D6 sitting used), with its path and the firm it is valid for; do not print its contents beyond column names.
4. **Q4, what must be true before the run.** List every precondition of the run as a checkable fact with the way to check it read-only: the portal DEV build includes `AR-y-317` and J7 and the reader (the DEV head sha vs those commits), the intake Lambda accepts `commentary_requested` (IRPT_BCKEND IB-pr-456, Andrew's act f61b: how an applier reads whether it is live: the Lambda's CodeSha256 against which record), the drafter Lambda and queues are live (named in `commentary.tf`), the resident release 31, the route release (leg L), `TICKET_DL_MAP` empty (CTO msg 7944), and the minted user's removal after the run. For each: the check, and the expected value read from the tracked records (a sha or a name). End with ONE line: `RECOMMEND: BROWSER_DRIVE` or `RECOMMEND: API_DRIVE` or `RECOMMEND: NEEDS <what>`, and the one fact that decides it.


### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-147/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~147/r41/FWD1_RUN_MECHANICS_READ.json` with keys: `base` (the sha your branch started from), `q1` {`dev_is` (`deployed_site`|`local_dev_build`|`both`|`unknown`), `url` (string or null), `api_base_source` {file, line, text}, `build_deploy_path` (string), `prd_quote` (string), `evidence` (list)}, `q2` {`session_store` (string), `token_stand_in_possible` (`yes`|`no`|`unknown`), `earlier_drivers` (list of {name, drove} where `drove` is `api`|`browser`), `browser_drive_documented` (true|false), `recipe` (string), `smallest_honest_drive` (string), `evidence` (list)}, `q3` {`form_fields` (list of {label, data_slot, kind}), `submit_call_order` (list of strings), `attachment_controls` (list of {item, data_slot, route}), `holdings_file` {path, firm, columns}, `evidence` (list)}, `q4` {`preconditions` (list of {fact, check, expected, source}), `recommend` (`BROWSER_DRIVE`|`API_DRIVE`|`NEEDS`), `deciding_fact` (string), `evidence` (list)}, and `not_read` (what you did not read: the live system, the deployed bytes). Then write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~147/shape_check.py` and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~147/cite_check.py` named below. Every cited `{file, line, text}` is a path relative to the worktree root.

<criterion id="AR343-y-AC1" cell_refs="AR-y-343"><invocation>python C:/dev/wk-irpt-anlreq-147/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~147/shape_check.py</invocation><expect>^SHAPE-OK </expect></criterion>
`AR343-y-AC1`: `shape_check.py` loads `r41/FWD1_RUN_MECHANICS_READ.json` and prints `SHAPE-OK <keys>` only when every key above is present with an allowed value (`q1.dev_is`, `q2.token_stand_in_possible`, `q4.recommend` in their enums) and every answer block has at least one evidence item; otherwise `SHAPE-BAD <why>`, exit 1.

<criterion id="AR343-y-AC2" cell_refs="AR-y-343"><invocation>python C:/dev/wk-irpt-anlreq-147/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~147/cite_check.py</invocation><expect>^CITES-OK </expect></criterion>
`AR343-y-AC2`: `cite_check.py` re-opens every `{file, line, text}` of the record and prints `CITES-OK <n> of <n>` only when each cited line number exists and the cited `text` is a substring of that line (after stripping); a miss prints `CITES-BAD <file>:<line>` and exits 1. It prints the denominator n.

<criterion id="AR343-y-AC3J" cell_refs="AR-y-343" judgment="true"/>
`AR343-y-AC3J` (judgment, graded at L9, never by you): the answers follow from the cited lines, a "not found" is said plainly with what was searched, and the recommendation is the one the evidence supports.

<expected_criteria>AR343-y-AC1 AR343-y-AC2 AR343-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~147/` and this order's file (status flip only). You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-343</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~147/IRPT_ANLREQ.TO-AR-y-343.fwd1-run-mechanics-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-343`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR343-y-AC1,AR343-y-AC2,AR343-y-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the cell against the answer shape; the lens: an answer asserted without a read line, a 'not found' said without a search, a binding assumed set because a name exists, a recommendation that widens beyond the cell. The cell requires cited lines checked by script, a stated search for every absence, and a stated recommendation. NOT seen (blind): the live system and the deployed bytes; denominator: 4 questions, each answered with cited lines.
</preflight>

---

## RECORD FACE

- Cut as a dependency-free read while leg L waits on its applier and the run waits on Andrew's f61b. Workstream `ZZ4` of round 40. Risk LOCAL. Base: `AR343-y-AC1` and `AC2` FAIL as expected.
- Its output feeds the FWD-1 run order to `0.7.0_AE_CloudOps~AQ2`; nothing is changed by this cell.
