# TO IRPT_ANLREQ.TO-AR-y-328.resident-release-bindings-read -- the resident release's bindings read: every variable, config key and file the resident reads for the analysis_ready, commentary_ready and packager wirings, where release 29 leaves them, which targets are declared in tracked source, and the producer-list edit sites; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-y-328</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~136</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of source and a record; nothing is changed, called or deployed)
**Decomp cell:** `AR-y-328` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~136`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-136` (branch `wk-IRPT_ANLREQ-136`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~136 <0.9.0_WK_IRPT_ANLREQ~136@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W136-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`. No live call, NO PUSH, no AWS call of any kind, no edit of any source file. Scratch outside the product tree.

### THE CELL (`AR-y-328`, inlined) -- a READ. The product tree is not edited.

*Context. The next resident release (root `0485393f3a-r30` over the running r29) is ONE release that binds the three queues and the packager (the CTO's ruling, msg 7767, and round-41 path msg 7723 item 4), carries the intake members (`AR-y-318`, `AR-y-319`), the standalone-commentary members (`AR-y-327`), and adds ONE address to `OPAL_PRODUCER_PRINCIPALS` in `C:/dev/wk-irpt-anlreq-136/infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py` (about line 165). In release 29 the analysis_ready, commentary_ready and packager bindings are all unset (null). To build that release the issuer must know, from source, EVERYTHING the resident reads to wire them. Your record is that list.*

Answer these four questions from SOURCE, each with `file:line` evidence read from the worktree (print the lines you cite; a line you did not read is not cited):

1. **Q1, the bindings.** For each of these five wirings, list every environment variable, config key or file the resident reads, in `ycharts/generate/resident_worker.py` and the modules it imports (`reports/resident_installed.py`, `ycharts/research/opal_packager.py`, the commentary drafter module, `_keys`): (a) the `analysis_ready` send (`IRPT_ANALYSIS_READY_QUEUE_URL`, `send_ready`, about line 207); (b) the commentary drafter's CONSUMER of `analysis_ready`; (c) the `commentary_ready` send; (d) the packager's CONSUMER of `commentary_ready` (`test_package_poll.py` names the poll); (e) the packager's ticket ports (`live_ticket_ports` config keys `api_base`, `secret_name`) and its principal (`svc-irpt-packager`, `PACKAGER_PRINCIPAL_UNSET`, `live_attach`). For each: the NAME, where it is read (file:line), the value CLASS (queue URL, queue name, secret name, base URL, flag), and what the code does when it is UNSET (silent skip, WARN, raise, refuse), with the line.
2. **Q2, where release 29 sets or leaves them.** In the release-29 host scripts under `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~125/r39/` (`install_r29.sh`, `pre_read_r29.sh`, `rollback_r29.sh`, the unit or env file the install writes): for each name in Q1, is it SET (to what class of value), UNSET, or not mentioned, with file:line? Name the file on the HOST that holds the resident's environment (the unit file or env file path the install writes) and the exact mechanism by which an install adds or changes a variable (so a build cell can derive `install_r30.sh` from it).
3. **Q3, the declared targets.** For each target the bindings point at (the `analysis_ready` queue, the `commentary_ready` queue, any dead-letter queue, the packager's secret, the `svc-irpt-packager` principal row in the ticket service's users table): is it DECLARED in tracked source (Terraform under `infra/`, a seed or registry file, a script), with file:line? If NOT declared in tracked source say so after a search of `infra/` and `org/missions/D9/IRPT/` (name the search terms). Do not call AWS. Note which of these a worker could build from the repository and which need an applier's live read or an Andrew act.
4. **Q4, the producer-list edit.** The exact edit site for adding ONE address to `OPAL_PRODUCER_PRINCIPALS` (resident_worker.py about line 165) and every OTHER place that must agree for the address to take effect (the installer's second check `reports/resident_installed.py` about line 274; any test or constant that pins the list; the producer choice at `resident_worker.py` about line 748). List each with file:line and say what the list's comment (lines about 159-164) requires to change in the same edit.


### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-136/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~136/r41/RESIDENT_BINDINGS_READ.json` with keys: `base` (the sha your branch started from), `q1` (a list of rows `{wiring` (one of `analysis_ready_send`, `drafter_consumer`, `commentary_ready_send`, `packager_consumer`, `packager_ports`), `name`, `read_at` {file, line, text}, `value_class` (`queue_url`|`queue_name`|`secret_name`|`base_url`|`flag`|`other`), `when_unset` (`skip`|`warn`|`raise`|`refuse`|`other`), `when_unset_evidence` {file, line, text}}), `q2` (a list of rows `{name, r29_state` (`set`|`unset`|`absent`), `evidence` (a list of {file, line, text})`}` plus `host_env_file`, `install_mechanism` (a short string) and `mechanism_evidence`), `q3` (a list of rows `{target` (`analysis_ready_queue`|`commentary_ready_queue`|`dead_letter_queue`|`packager_secret`|`packager_principal_row`), `declared` (true|false), `evidence` (list), `searched` (the terms, when declared is false), `needs` (`worker_buildable`|`applier_live_read`|`andrew_act`)}), `q4` {`edit_site` {file, line, text}, `must_agree` (a list of {file, line, text, why}), `comment_change` (string)}, and `not_read` (what you did not read: the live system, the deployed bytes). Then write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~136/shape_check.py` and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~136/cite_check.py` named below. Every cited `{file, line, text}` is a path relative to the worktree root.

<criterion id="AR328-y-AC1" cell_refs="AR-y-328"><invocation>python C:/dev/wk-irpt-anlreq-136/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~136/shape_check.py</invocation><expect>^SHAPE-OK </expect></criterion>
`AR328-y-AC1`: `shape_check.py` loads `r41/RESIDENT_BINDINGS_READ.json` and prints `SHAPE-OK <keys>` only when every key above is present with an allowed value (`q1` rows, `q2` rows, `q3` rows and `q4` with their enums) and every answer block has at least one evidence item; otherwise `SHAPE-BAD <why>`, exit 1.

<criterion id="AR328-y-AC2" cell_refs="AR-y-328"><invocation>python C:/dev/wk-irpt-anlreq-136/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~136/cite_check.py</invocation><expect>^CITES-OK </expect></criterion>
`AR328-y-AC2`: `cite_check.py` re-opens every `{file, line, text}` of the record and prints `CITES-OK <n> of <n>` only when each cited line number exists and the cited `text` is a substring of that line (after stripping); a miss prints `CITES-BAD <file>:<line>` and exits 1. It prints the denominator n.

<criterion id="AR328-y-AC3J" cell_refs="AR-y-328" judgment="true"/>
`AR328-y-AC3J` (judgment, graded at L9, never by you): the answers follow from the cited lines, a "not found" is said plainly with what was searched, and the recommendation is the one the evidence supports.

<expected_criteria>AR328-y-AC1 AR328-y-AC2 AR328-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~136/` and this order's file (status flip only). You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-328</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~136/IRPT_ANLREQ.TO-AR-y-328.resident-release-bindings-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-328`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR328-y-AC1,AR328-y-AC2,AR328-y-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the cell against the answer shape; the lens: an answer asserted without a read line, a 'not found' said without a search, a binding assumed set because a name exists, a recommendation that widens beyond the cell. The cell requires cited lines checked by script, a stated search for every absence, and a stated recommendation. NOT seen (blind): the live system and the deployed bytes; denominator: 4 questions, each answered with cited lines.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (msg 7767, C-SWITCH A') and round-41 path (msg 7723 item 4). Workstream `ZN` of round 40. Risk LOCAL: the cell reads source and writes a record in its deliverable folder. Base: `AR328-y-AC1` and `AC2` FAIL as expected (no record, no checker files).
- Its output feeds the build cell of the single resident release and the applier's live-read order; nothing is changed by this cell.
