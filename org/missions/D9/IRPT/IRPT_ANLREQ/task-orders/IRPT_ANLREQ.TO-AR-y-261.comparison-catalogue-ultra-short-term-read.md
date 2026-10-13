# TO IRPT_ANLREQ.TO-AR-y-261.comparison-catalogue-ultra-short-term-read -- why the Opal Ultra Short-Term model is missing from the Analysis Request form -- a read, nothing changed

<to_id>IRPT_ANLREQ.TO-AR-y-261</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~86</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-261` (`decompositions/IRPT_ANLREQ_DECOMP_R22_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~86`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-86` (branch `wk-IRPT_ANLREQ-86`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~86 <0.9.0_WK_IRPT_ANLREQ~86@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W86-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-261`, inlined) -- WHY IS THE OPAL ULTRA SHORT-TERM MODEL MISSING? READ ONLY. Nothing is built or changed.

*Andrew (relayed by the CTO, msg 7151, filing on DEV after his smoke ~18:2xZ), verbatim: "we're missing the Opal Ultra Short-Term, also they should be arranged in canonical order with canonical color checkboxes that take that color when checked. Also the Advisory Fee doesn't need to be included ... These would largely be from prospects so we'd have no way of knowing their fees ... also add commentary checkbox doesnt do anything." Rows `IRPT_ANLREQ-D2-S79` to `-S82`. The form lists the entries of the served comparison catalogue (`GET /api/scoped/investor-reporting/analysis/comparisons?selected_tenant=<firm>`, `comparisonCatalogue.ts`; the entries are `{key, label, ticker, name_source}`, 'model-catalogue entries first, then tickers in ticker order'); the form itself renders what it receives (portal/src/pages/TicketCenter/AnalysisRequestParts.tsx :105-123). The CTO's ruling (msg 7151, item 1): every Opal model in the catalogue is listed, Ultra Short-Term included; read why it is missing.*

1. **Find the server code that builds the catalogue** (the route above; `comp-find` over named folders under `infra/aws/lambda/investor-reporting/` or `Grep` on a named folder; the scoped GET, its handler and the model-catalogue source it reads: a file, an S3 object, a table; name it by file:line). Record `server` {`route_handler`, `catalogue_source`, `entries_built_how`, `files_read`}.
2. **Find the model catalogue itself** (the list of Opal models the estate keeps: look first for the source the handler reads, then for the portal's own model list `portal/src/lib/chartColors.ts` MODEL_PORTFOLIO_COLORS and `ModelPortfolios.tsx`, and the iv-e-11 model-color tests which name `Ultra Short-Term`). Record `models_in_the_estate` {`source`, `names`, `has_ultra_short_term`}.
3. **Say why it is missing.** Compare the model catalogue to what the handler serves: does `Ultra Short-Term` exist in the source and get filtered out (a filter, a status, a tenant rule, a name mismatch such as `Ultra Short Term` against `Ultra-Short Term`), is it absent from the source, or does the portal drop it? Run what you can offline (the handler's own tests, or a constructed call of the builder with the real source file if it is a repo file; label anything you did not run as READ). Record `why_missing` {`verdict` (one of: filtered in code, absent from the source, dropped by the portal, not reproducible), `evidence` (file:line and the offline run), `fix` (what would change, in which file, in which project's lane: say whether the surface belongs to IRPT_BCKEND or to this project and what the owned-paths lane would be), `risk` (what else the same cause may be hiding: list any other Opal model absent from the served catalogue by the same cause)}.
4. **The canonical order.** Andrew wants the models "arranged in canonical order". Record `canonical_order` {`where_defined` (the estate's one definition of the model order, file:line; if there are several, list them and say which the holdings tab uses), `names_in_order`}. If the estate holds no single order, say so plainly and propose none (the CTO rules).
5. **Write `r22/ULTRA_SHORT_TERM_READ.json`:** `server`, `models_in_the_estate`, `why_missing`, `canonical_order`, `claim`, `not_read` (the live served catalogue and the live DEV bundle: nothing was called).
6. **In your report:** the verdict in one sentence, the file:line, whose lane the fix is in, the canonical order.

### ACCEPTANCE

<criterion id="AR261-y-AC1" cell_refs="AR-y-261"><invocation>python C:/dev/wk-irpt-anlreq-86/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y261-read --root C:/dev/wk-irpt-anlreq-86</invocation><expect>Y261-READ-OK</expect></criterion>
`AR261-y-AC1`: the record names where the catalogue is built and sourced, whether Ultra Short-Term exists in the source, a verdict on why it is missing with file:line evidence and the lane of the fix, and the canonical order's one definition.

<criterion id="AR261-y-AC2J" cell_refs="AR-y-261" judgment="true"/>
`AR261-y-AC2J` (judgment, graded at L9, never by you): the cause is read from the code and the source (not guessed), the verdict names whose lane the fix is in, any other model missing by the same cause is listed, and nothing was changed or called.

<expected_criteria>AR261-y-AC1 AR261-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~86/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22_Y.md</decomp_doc>
<owned_cells>AR-y-261</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~86/IRPT_ANLREQ.TO-AR-y-261.comparison-catalogue-ultra-short-term-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-261`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR261-y-AC1,AR261-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reads of source files and tests in the worktree; nothing is called, changed or applied; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading Andrew's smoke words (rows D2-S79 to D2-S82) against the cell; the lens: a test that passes without the change, a color or order invented instead of reused, or a change that fixes the form the worker imagined and not the one Andrew filed on. The order requires the new test to FAIL on the DEV tip without the change, and the words a person sees to be stated as rendered. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on Andrew's smoke of the Analysis Request form (CTO msg 7151, rows `D2-S79` to `-S82`) as workstream `Y` round 22, the CTO's O1 issuance, ahead of anything else. Base: `AR261-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
