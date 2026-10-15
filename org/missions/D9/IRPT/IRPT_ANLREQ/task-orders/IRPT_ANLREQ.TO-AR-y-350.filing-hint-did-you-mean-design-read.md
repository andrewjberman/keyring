# TO IRPT_ANLREQ.TO-AR-y-350.filing-hint-did-you-mean-design-read -- the C-FILING-HINT design read: what the filing form holds about a holding, what the served catalogue carries (a CUSIP or ISIN or not), where a per-holding suggestion would show and how an accepted one reaches the backend, and the smallest change set; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-y-350</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~151</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ11</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of source and a record; nothing is changed, called or deployed)
**Decomp cell:** `AR-y-350` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~151`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-151` (branch `wk-IRPT_ANLREQ-151`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~151 <0.9.0_WK_IRPT_ANLREQ~151@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W151-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`. No live call, NO PUSH, no AWS call of any kind, no network act at all, no edit of any source file. Scratch outside the product tree.

### THE CELL (`AR-y-350`, inlined) -- a READ. The product tree is not edited.

*Context. PRD ADDENDUM v0.12 (read it: `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, the section 'ADDENDUM v0.12', about lines 364-381) adds the contract C-FILING-HINT, on Andrew's word that a 'Did you mean' is needed at the filing point: on the Ticket Center filing form, a holding whose symbol is not in the SERVED CATALOGUE shows ONE suggestion, 'Did you mean <symbol> (<name>)?', the closest catalogue entry by exact CUSIP or ISIN match first, then the ticker edit distance, then the name; the filer accepts it (the row takes the suggested symbol) or keeps their own, and nothing is replaced without the filer's click; a kept unknown symbol files as typed; swaps are never offered at the form (the backend does them after filing); the suggestion reads only the served catalogue the form already loads (no new vendor call at filing) and must work for the staff filer once a firm is chosen. The issuer must know, from SOURCE, what the form already holds about a holding and what the catalogue carries, before the build cell is cut. The portal is the nested repository at `C:/dev/wk-irpt-anlreq-151/portal` (your own portal worktree, at DEV); the backend source is under `infra/aws/lambda/investor-reporting/` of your worktree (it may be skip-worktree: read blobs with `git show HEAD:<path>`, as an earlier reader did). The Ticket Center form is `portal/src/pages/TicketCenter/` (`TicketCenter.tsx`, `AnalysisRequestParts.tsx`, `analysisRequest.ts`); the catalogue client is `portal/src/pages/InvestorReporting/tabs/analysis/comparisonCatalogue.ts`; the upload client is in `portal/src/api/endpoints/investor-reporting.ts`.*

Answer these four questions from SOURCE, each with `file:line` evidence read from the worktree (print the lines you cite; a line you did not read is not cited):

1. **Q1, what the form holds about a holding.** Trace the holdings file from the chooser (`analysisFile`, `chooseFile`, `stageFile`) through the upload call (`POST /api/scoped/investor-reporting/analysis/inputs`) and what the response carries back: does the PAGE ever hold the parsed holdings rows (symbol, CUSIP, ISIN, name, quantity), or only a stored-input reference and findings? List the response members (the wire type and its schema under `docs/contracts/investor-reporting/v1/`), and every finding code about an unrecognised or unresolved security (a name search for `UNRESOLVED`, `UNKNOWN`, `NOT_FOUND`, `SECURITY` in the upload door `infra/aws/lambda/investor-reporting/intake/uploads.py` and the findings the portal renders).
2. **Q2, what the served catalogue carries.** The entry type `CatalogueEntry` and the handler of `GET .../analysis/comparisons` (`comparison-catalogue` in `irpt-ycharts-generate`): the members of an entry (key, label, ticker, name, `name_source`, any CUSIP or ISIN), how many entries and which universe (models, funds, ETFs, or the holdings universe), and whether an entry carries a CUSIP or an ISIN. State plainly whether an exact CUSIP or ISIN match is possible from the catalogue alone.
3. **Q3, where a per-holding suggestion would show and what 'the row takes the suggested symbol' means.** Does the form have any per-holding row UI today (a table or list of holdings the filer can edit)? If the holdings stay in the uploaded file, how would an accepted suggestion reach the backend: is there a submit member that carries per-holding overrides (read `AnalysisSubmissionRequest` in `docs/contracts/investor-reporting/v1/` and the submit call), or would the file have to be rewritten in the page, or is a new wire member needed (a CONTRACT change)? Cite the lines.
4. **Q4, the smallest change set.** In one paragraph: the SMALLEST set of changes that delivers C-FILING-HINT as the addendum words it, with the file and function of each, whether it is PORTAL_ONLY or needs a backend or wire member, the tests to add (names under `src/pages/TicketCenter/__tests__/`), and which of the four points of the addendum cannot be met from what exists (say which and why). End with ONE line: `RECOMMEND: PORTAL_ONLY` or `RECOMMEND: BACKEND_AND_PORTAL` or `RECOMMEND: CONTRACT_NEEDED <what>`, and the one fact that decides it. You recommend; the issuer and the CTO rule.


### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-151/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~151/r41/FILING_HINT_DESIGN_READ.json` with keys: `base` (the sha your branch started from), `q1` {`page_holds_rows` (`yes`|`no`|`unknown`), `response_members` (a list of strings), `unresolved_finding_codes` (a list of {code, evidence}), `evidence` (list of {file, line, text})}, `q2` {`entry_members` (a list of strings), `universe` (string), `entry_has_cusip_or_isin` (`yes`|`no`|`unknown`), `exact_id_match_possible` (`yes`|`no`|`unknown`), `evidence`}, `q3` {`per_holding_ui_exists` (`yes`|`no`|`unknown`), `override_member_exists` (`yes`|`no`|`unknown`), `how_acceptance_reaches_backend` (string), `evidence`}, `q4` {`change_set` (a list of {file, function, change}), `tests_to_add` (a list of strings), `points_not_met` (a list of {point, why}), `recommend` (`PORTAL_ONLY`|`BACKEND_AND_PORTAL`|`CONTRACT_NEEDED`), `deciding_fact` (string), `evidence`}, and `not_read` (what you did not read: the live system, the deployed bytes). Then write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~151/shape_check.py` and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~151/cite_check.py` named below. Every cited `{file, line, text}` is a path relative to the worktree root.

<criterion id="AR350-y-AC1" cell_refs="AR-y-350"><invocation>python C:/dev/wk-irpt-anlreq-151/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~151/shape_check.py</invocation><expect>^SHAPE-OK </expect></criterion>
`AR350-y-AC1`: `shape_check.py` loads `r41/FILING_HINT_DESIGN_READ.json` and prints `SHAPE-OK <keys>` only when every key above is present with an allowed value (`q1.page_holds_rows`, `q2.exact_id_match_possible`, `q3.override_member_exists`, `q4.recommend` in their enums) and every answer block has at least one evidence item; otherwise `SHAPE-BAD <why>`, exit 1.

<criterion id="AR350-y-AC2" cell_refs="AR-y-350"><invocation>python C:/dev/wk-irpt-anlreq-151/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~151/cite_check.py</invocation><expect>^CITES-OK </expect></criterion>
`AR350-y-AC2`: `cite_check.py` re-opens every `{file, line, text}` of the record and prints `CITES-OK <n> of <n>` only when each cited line number exists and the cited `text` is a substring of that line (after stripping); a miss prints `CITES-BAD <file>:<line>` and exits 1. It prints the denominator n.

<criterion id="AR350-y-AC3J" cell_refs="AR-y-350" judgment="true"/>
`AR350-y-AC3J` (judgment, graded at L9, never by you): the answers follow from the cited lines, a "not found" is said plainly with what was searched, and the recommendation is the one the evidence supports.

<expected_criteria>AR350-y-AC1 AR350-y-AC2 AR350-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~151/` and this order's file (status flip only). You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-350</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~151/IRPT_ANLREQ.TO-AR-y-350.filing-hint-did-you-mean-design-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-350`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR350-y-AC1,AR350-y-AC2,AR350-y-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the cell against the answer shape; the lens: an answer asserted without a read line, a 'not found' said without a search, a binding assumed set because a name exists, a recommendation that widens beyond the cell. The cell requires cited lines checked by script, a stated search for every absence, and a stated recommendation. NOT seen (blind): the live system, the deployed bytes and the compiled bundle (only source at the worktree HEAD is read); denominator: 4 questions, 3 portal form files, 1 catalogue client, 1 upload client, 2 contract schemas, 2 Lambda handlers.
</preflight>

---

## RECORD FACE

- Cut on the CTO's four-lane ruling (msg 8376; PRD v0.12, C-FILING-HINT) while the IB-pr-456 apply is at CloudOps IB2. Workstream `ZZ11` of round 40. Risk LOCAL. Base: `AR350-y-AC1` and `AC2` FAIL as expected (no record, no checker files).
- Its output decides the build cell of the filing hint (portal only, or a backend or wire change that is an ENDPOINT matter for the CTO); nothing is changed by this cell.
