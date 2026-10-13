# TO IRPT_ANLREQ.TO-AR-y-245.server-defaults-the-price-date -- a Shares upload with no price date is priced at the prior trading day's close, by the server

<to_id>IRPT_ANLREQ.TO-AR-y-245</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~77</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-245` (`decompositions/IRPT_ANLREQ_DECOMP_R22S_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~77`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-77` (branch `wk-IRPT_ANLREQ-77`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~77 <0.9.0_WK_IRPT_ANLREQ~77@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W77-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-245`, inlined) -- THE SERVER DEFAULTS THE PRICE DATE. Code and tests only; nothing is released, uploaded or applied.

*Andrew's own test (row D2-S78): the "Price date for share quantities" field is pointless, "the answer is always now, which will translate into market close of the prior trading day". The portal field cannot simply go: the server REFUSES a Shares upload without a date (`intake/portfolio.py` :208-212 raises `PRICE_DATE_REQUIRED`; `intake/uploads.py` :419-421 and :586 pass `options["price_date"]` to `resolve_prices`; template lane `portfolio.py` :401-405 and :477-486 give `SHARES_PRICE_UNAVAILABLE`; the refusal is asserted at `intake/tests/test_portfolio.py` :144). This cell makes the SERVER take the prior trading day's close when no date is sent. A date that IS sent keeps working exactly as today.* Read first: the worker record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~75/r22/PORTAL_PRICE_DATE_CANDIDATE.json` (`server_reads`) and rows `IRPT_ANLREQ-D2-W75-S1` and `-S3` in the channel.

1. **Find the one trading-day source and whether the packages can carry it.** The workspace has ONE frontier for trading days: `lib/trading_calendar.py`. Read how a Lambda of this estate already computes a prior trading day (start from `infra/aws/lambda/investor-reporting/performance/holdings_gold.py`, `holdings-performance/handler.py` and `reporting-gold/handler.py`: which function, which module, how it reaches the package: `PATH_MANIFEST.json`, the source map `staged_from` rows of those functions in `infra/aws/lambda/ci/lambda-source-map.json`). Then say for the TWO places `intake/` is packaged -- the Lambda `irpt-ycharts-generate` (its map entry's `staged_from` rows) and the resident package (`reports/build_resident_package.py` and the release-19 recipe record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/RESIDENT_RECIPE_AND_DELTA.json`) -- whether the calendar module is already a member, or would be ONE added member (name it and its source path), and whether it imports anything that is not packaged there. Record `trading_day_source` {`module`, `function`, `file_lines`, `used_by`} and `packaging` {`ycharts_generate`, `resident`} (each: `already_a_member` yes or no, `members_to_add`, `imports_not_packaged`). **If the calendar cannot be carried without adding more than that one member, or needs a network or a secret, STOP before step 2, file a BLOCKING row, and write the record with `behaviour` absent. Do NOT hand-roll a weekday-or-holiday rule in `intake/`.**
2. **The change.** Where a SHARES unit meets an absent price date (`portfolio.py` :208-212, and the places in `uploads.py` that pass `options["price_date"]`), take the prior trading day from the source of step 1, call `resolve_prices` with it, and record the date that was used where the answer already records its price date (find where `price_date` is stored on the portfolio or the input; do not add a wire member unless the existing answer has nowhere to say it, and if so STOP and ask in a row). A date sent by the caller is validated and used exactly as today; an invalid date sent still refuses as today. The weights and dollars lanes are untouched. Touch `intake/portfolio.py`, `intake/uploads.py` (only if needed) and ONE new test file only; the calendar source is imported, not copied.
3. **The tests, before and after.** New file `infra/aws/lambda/investor-reporting/intake/tests/test_price_date_default.py` with at least 3 tests: (a) a Shares file with no date prices at the prior trading day of a fixed "today" you inject (use a Monday, a day after a holiday and an ordinary Wednesday); (b) a date sent is used as sent; (c) a malformed date sent still refuses as `PRICE_DATE_REQUIRED` (or whatever the code raises today for it: read it); (d) the answer states the date used. `before_arm`: run the new tests against the files at HEAD WITHOUT your change and record that (a) FAILS. Then: the whole intake folder passes (`tests`: counts; the floor is 365 against r19.3) and the existing assertion at `test_portfolio.py` :144 is moved ONLY if it asserted the very refusal this cell removes (say so; every other test stays as it is). `commit-gate` on every `.py`.
4. **Write `r22/PRICE_DATE_DEFAULT.json`:** `trading_day_source`, `packaging`, `behaviour` (what the server does with no date, with a date, with a bad date; with file and line), `tests` {`added`, `passed`, `failed`, `intake_folder`}, `before_arm` {`failed`, `output_tail`}, `files_changed`, `claim`, `not_read`.
5. **In your report:** the source of the prior trading day (file:line), the packaging answer for each place, the before and after counts, and anything that would make the release larger than one member in a leg.

### ACCEPTANCE

<criterion id="AR245-y-AC1" cell_refs="AR-y-245"><invocation>python C:/dev/wk-irpt-anlreq-77/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y245-server --root C:/dev/wk-irpt-anlreq-77</invocation><expect>Y245-SERVER-OK</expect></criterion>
`AR245-y-AC1`: the record names the trading-day source and the packaging of each place, the new test file passes with at least 3 tests, and the whole intake folder passes at 365 or more.

<criterion id="AR245-y-AC2J" cell_refs="AR-y-245" judgment="true"/>
`AR245-y-AC2J` (judgment, graded at L9, never by you): the prior trading day comes from the estate's one calendar source and no weekday or holiday rule was written in `intake/`; a date sent behaves exactly as before; the new test fails without the change; the packaging answer is read from the map and the recipe, not assumed; nothing was released or applied.

<expected_criteria>AR245-y-AC1 AR245-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~77/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/intake/portfolio.py
infra/aws/lambda/investor-reporting/intake/uploads.py
infra/aws/lambda/investor-reporting/intake/tests/test_price_date_default.py
infra/aws/lambda/investor-reporting/intake/tests/test_portfolio.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22S_Y.md</decomp_doc>
<owned_cells>AR-y-245</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~77/IRPT_ANLREQ.TO-AR-y-245.server-defaults-the-price-date.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-245`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR245-y-AC1,AR245-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test edits in a worktree; nothing is released, uploaded, deployed or called (the release is a later pair).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the NEVER rule on trading days (one frontier, lib/trading_calendar.py) and row W75-S1 against the cell; the lens: a hand-rolled weekday rule in intake/, or a default that silently prices a date the person did not mean. The order requires the single calendar source, the date used to be stated in the answer, and a sent date to behave as before. NOT seen: the live package contents and the resident host.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on `AR-y-243`'s BLOCKING row `W75-S1` (the server requires the date) as workstream `YR` round 19. Base: `AR245-y-AC1` FAIL as expected (no record, no test file).
- The portal field's removal (`AR-y-243`, re-cut after this) lands only AFTER the server leg is released: a portal that omits the date against a server that still requires it refuses every Shares upload.
- The release of this server change is a later two-leg pair (Lambda `irpt-ycharts-generate` and the resident), not this order.
