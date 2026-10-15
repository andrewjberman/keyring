# TO IRPT_ANLREQ.TO-AR-y-348.staff-firms-and-catalogue-load-read -- the staff firms and catalogue load read: why a staff caller's New Analysis Request shows firms still loading and no models or tickers, how the PROD build differs from DEV, and what the FWD-1 synthetic staff user needs for both to load; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-y-348</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~150</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ9</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of source and a record; nothing is changed, called or deployed)
**Decomp cell:** `AR-y-348` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~150`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-150` (branch `wk-IRPT_ANLREQ-150`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~150 <0.9.0_WK_IRPT_ANLREQ~150@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W150-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`. No AWS call, NO PUSH; the one network act permitted is the read-only git fetch origin PROD DEV in the portal repository (Q3), no edit of any source file. Scratch outside the product tree.

### THE CELL (`AR-y-348`, inlined) -- a READ. The product tree is not edited.

*Context. On 2026-10-15 ~13:54Z an Opal STAFF user opened the PROD Ticket Center, New Analysis Request, and saw 'The Opal model list is not loaded.', no tickers, and the held-submit words 'Your firms are still loading. Wait for them, then choose one.' (the form's own words: `C:/dev/ajb_workspace/portal/src/pages/TicketCenter/analysisRequest.ts` lines about 215-228, `AnalysisRequestParts.tsx` line about 178). The issuer MEASURED, from CloudWatch and Lambda configuration (you cannot repeat these: you make no AWS call): (a) at 13:54:38Z the route `GET /api/scoped/investor-reporting/analysis/comparisons` (served by the Lambda `irpt-ycharts-generate`, operation `comparison-catalogue`) logged `BLOCKED: no directory bucket declared for firm token in IRPT_DIRECTORY_BUCKET_MAP -- a firm this function cannot map is refused, never defaulted` with public reason `FIRM_BINDING`; (b) that Lambda's `IRPT_DIRECTORY_BUCKET_MAP` has the keys `49financial`, `cottonwood`, `inflection` and no staff or Global token; (c) the firms read is `POST /api/scoped/investor-reporting/directory/resolve` (Lambda `irpt-directory-search`): four invocations at 13:54:20-21Z and no error line, yet the form still showed the firms as not loaded and no failure. The FWD-1 run (a synthetic STAFF user, on the DEV build, same live API) files one Analysis Request through this same form, so the issuer must know from SOURCE whether that user will see the firms and the catalogue load. The portal worktree is `C:/dev/ajb_workspace/portal` (a nested repository: read it with `git -C C:/dev/ajb_workspace/portal show <ref>:<path>`; `git -C C:/dev/ajb_workspace/portal fetch origin PROD DEV` is permitted, it is a read of the portal repository and the only network act allowed). The backend source is under `infra/aws/lambda/investor-reporting/` of your worktree.*

Answer these four questions from SOURCE, each with `file:line` evidence read from the worktree or from `git show` (print the lines you cite; a line you did not read is not cited):

1. **Q1, the firms read for a staff caller.** Trace `loadAllowedFirms` (`portal/src/pages/TicketCenter/TicketCenter.tsx` about lines 97-125 and the effect about lines 303-316) end to end for an INTERNAL caller: the client call `resolveDirectoryContext` (`portal/src/api/endpoints/investor-reporting.ts`), the handler of `POST .../directory/resolve` in the Lambda `irpt-directory-search` (find it by a name search over `infra/aws/lambda/investor-reporting/`), and what it returns for the request `{tenant: 'bootstrap', selectedTenant: 'global', requested}`. List every condition under which the page ends with `firms` still `null` and `firmsFailed` false (a promise that never settles, an effect guard such as `firmsAsked`, a thrown error that is swallowed elsewhere) versus `firmsFailed` true, and every condition that makes `firms` an EMPTY list ('No firm is available to you').
2. **Q2, the catalogue for a staff caller.** Trace `GET .../analysis/comparisons` (`portal/src/pages/InvestorReporting/tabs/analysis/comparisonCatalogue.ts` `fetchCatalogue`, and `TicketCenter.tsx` about lines 322-333 where the firm is `filingForm.firm`) to the handler `comparison-catalogue` in `irpt-ycharts-generate`: where `FIRM_BINDING` and the `IRPT_DIRECTORY_BUCKET_MAP` refusal are raised (file:line), what the handler does with a staff caller who sends NO `selected_tenant`, and with one who sends a partner firm (for example `49financial`). State plainly whether the catalogue can load for a staff caller BEFORE a firm is chosen.
3. **Q3, PROD against DEV.** Run `git -C C:/dev/ajb_workspace/portal fetch origin PROD DEV` and read `portal/src/pages/TicketCenter/TicketCenter.tsx`, `analysisRequest.ts` and `AnalysisRequestParts.tsx` at `origin/PROD` and at `origin/DEV`. Does the PROD build carry the sentence 'Opal staff open requests from the queue rather than file them, so this form cannot be submitted from here' (a search; give the file:line at each ref), the staff Firm chooser (`loadAllowedFirms` with `internal`), and the catalogue request with `selected_tenant`? List every difference between the two refs in these three files that bears on firms, the catalogue or the staff held-submit, as short rows `{ref, file, line, text}`; if a ref has no such code say so after naming the search.
4. **Q4, what the synthetic staff user needs.** The FWD-1 run's staff user is a users row with `firmId` `opal-capital`, `userType` `test-filer`, role `user`, status active, NO `allowedFirmIds`, NO MFA attributes (record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/r41/FWD1_DRIVER_RECORD.json`; earlier reads `~146` `FWD1_PREREQ_READ.json` and `~148` `FWD1_LOGIN_DRIVER_READ.json`). From the Q1 handler: for that principal does `directory/resolve` with `selectedTenant: 'global'` return READY firms, which ones and from what source (a table, a bucket map, `allowedFirmIds`, a registry), or none? If it depends on an attribute the minted row lacks, name the attribute and its value form. Then, with a partner firm chosen, does the catalogue (Q2) load? End with ONE line: `RECOMMEND: RUN_AS_MINTED` or `RECOMMEND: MINT_NEEDS <attribute and value form>` or `RECOMMEND: BLOCKED <why>`, and the one fact that decides it. You recommend; the issuer and the CTO rule.


### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-150/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~150/r41/STAFF_FIRMS_CATALOGUE_READ.json` with keys: `base` (the sha your branch started from), `q1` {`handler` {file, line, text}, `returns_for_staff_global` (string), `firms_null_not_failed_when` (a list of strings), `firms_failed_when` (a list of strings), `firms_empty_when` (a list of strings), `evidence` (list of {file, line, text})}, `q2` {`refusal_site` {file, line, text}, `staff_no_selected_tenant` (`loads`|`refused`|`unknown`), `staff_with_partner_firm` (`loads`|`refused`|`unknown`), `catalogue_loads_before_firm_chosen` (`yes`|`no`|`unknown`), `evidence`}, `q3` {`prod_has_staff_not_filing_sentence` (true|false), `prod_has_staff_firm_chooser` (true|false), `prod_catalogue_sends_selected_tenant` (true|false), `differences` (a list of {ref, file, line, text}), `searched` (the terms), `evidence`}, `q4` {`global_firms_for_minted_row` (`ready_firms`|`empty`|`error`|`unknown`), `depends_on` (a list of {attribute, value_form, evidence}), `catalogue_loads_with_partner_firm` (`yes`|`no`|`unknown`), `recommend` (`RUN_AS_MINTED`|`MINT_NEEDS`|`BLOCKED`), `deciding_fact` (string), `evidence`}, and `not_read` (what you did not read: the live system, the deployed bytes). Then write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~150/shape_check.py` and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~150/cite_check.py` named below. Every cited `{file, line, text}` is a path relative to the worktree root.

<criterion id="AR348-y-AC1" cell_refs="AR-y-348"><invocation>python C:/dev/wk-irpt-anlreq-150/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~150/shape_check.py</invocation><expect>^SHAPE-OK </expect></criterion>
`AR348-y-AC1`: `shape_check.py` loads `r41/STAFF_FIRMS_CATALOGUE_READ.json` and prints `SHAPE-OK <keys>` only when every key above is present with an allowed value (`q2.catalogue_loads_before_firm_chosen`, `q4.global_firms_for_minted_row`, `q4.recommend` in their enums) and every answer block has at least one evidence item; otherwise `SHAPE-BAD <why>`, exit 1.

<criterion id="AR348-y-AC2" cell_refs="AR-y-348"><invocation>python C:/dev/wk-irpt-anlreq-150/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~150/cite_check.py</invocation><expect>^CITES-OK </expect></criterion>
`AR348-y-AC2`: `cite_check.py` re-opens every `{file, line, text}` of the record and prints `CITES-OK <n> of <n>` only when each cited line number exists and the cited `text` is a substring of that line (after stripping); a miss prints `CITES-BAD <file>:<line>` and exits 1. It prints the denominator n.

<criterion id="AR348-y-AC3J" cell_refs="AR-y-348" judgment="true"/>
`AR348-y-AC3J` (judgment, graded at L9, never by you): the answers follow from the cited lines, a "not found" is said plainly with what was searched, and the recommendation is the one the evidence supports.

<expected_criteria>AR348-y-AC1 AR348-y-AC2 AR348-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~150/` and this order's file (status flip only). You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-348</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~150/IRPT_ANLREQ.TO-AR-y-348.staff-firms-and-catalogue-load-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-348`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR348-y-AC1,AR348-y-AC2,AR348-y-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the cell against the answer shape; the lens: an answer asserted without a read line, a 'not found' said without a search, a binding assumed set because a name exists, a recommendation that widens beyond the cell. The cell requires cited lines checked by script, a stated search for every absence, and a stated recommendation. NOT seen (blind): the live system, the deployed bytes and the PROD build's compiled output (only source at two git refs is read); denominator: 4 questions, 2 portal refs (origin/PROD and origin/DEV), 3 portal files, 2 Lambda handlers.
</preflight>

---

## RECORD FACE

- Cut on the CTO's msg 8317 (row `IRPT_ANLREQ-D2-S118`, the PROD lists that do not load) while the FWD-1 run waits on the IB-pr-456 apply. Workstream `ZZ9` of round 40. Risk LOCAL. Base: `AR348-y-AC1` and `AC2` FAIL as expected (no record, no checker files).
- Its output decides whether the run's staff user will see its firms and the catalogue load on the DEV build, so whether `TO-RUN-FWD1` flips as written or the mint changes; nothing is changed by this cell.
