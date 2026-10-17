# TO-AR-g-152 -- the YCharts price adapter sends the form the CRO's captured working series call uses (FWD-7 C-PRICES; CTO msgs 9991 and 10004): securities with the double trailing comma, calcs=id:level, zoom, maxPoints, partner

<to_id>IRPT_ANLREQ.TO-AR-g-152</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~276</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>superseded</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>52</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-152` (`decompositions/IRPT_ANLREQ_DECOMP_R52_G.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none (the adapter and the transport are merged on the trunk). Order: CTO msg 9991 (the tier's `id:<TICKER>,include:true,&zoom=max` is refused HTTP 400 on the host; cut the release with the form the working recipe path uses) and msg 10004.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~276`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-276` (branch `wk-IRPT_ANLREQ-276`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~276 <0.9.0_WK_IRPT_ANLREQ~276@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W276-S<k>` (take the next free `<k>`; check the channel file for `W276` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only in the product file. Do not touch anything outside the `<paths>` block.

### THE CELL (`AR-g-152`, inlined)

File: `infra/aws/lambda/investor-reporting/ycharts/research/price_adapter_ycharts.py`. Today the reader sends, per symbol, `transport("/charts/fund_data.json", {"securities": "id:" + name + ",include:true,", "zoom": "max"})`, and YCharts answers that with HTTP 400. The CRO's captured working series call (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json`, call `benchmark_level_series`, lines 81-93) is the same route with these params, in this order:

    "securities": "id:<SYMBOL>,include:true,,"     (a DOUBLE trailing comma)
    "calcs":      "id:level,include:true,,"
    "zoom":       "max"
    "maxPoints":  "100000"
    "partner":    "basic_2000"

1. Change the one `transport(...)` call in `reader` to send exactly those five params, in that order, with the stripped upper-cased symbol in `securities`. No start or end date is sent (the reader already filters the served points to `start`..`end`). Nothing else in the module changes: one call per symbol, the spacing sleep before every call but the first, the blank-symbol rule, the window filter, the base-100 chaining, errors propagate. Update the module docstring's first paragraph by one sentence naming the form and its source (the CRO's captured `benchmark_level_series`).
2. Move the two existing tests that assert the old form: `ycharts/research/tests/test_price_adapter_ycharts.py` (line 50: the `fake.calls` assertion for `QQQ`) and `reports/tests/test_ycharts_price_tier.py` (line 102: `session.paths`, now `["/charts/fund_data.json?securities=id:SPY,include:true,,&calcs=id:level,include:true,,&zoom=max&maxPoints=100000&partner=basic_2000"]`). Do NOT edit `ycharts/research/tests/test_price_transport_ycharts.py`: the transport takes any params and its test passes its own.
3. Run the three criteria. Commit the code and tests, then the proof and the status flip, as separate commits (code first).
4. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR152-g-AC1" cell_refs="AR-g-152"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g152_checks.py build</invocation><expect>^AR-G152-OK</expect></criterion>

<criterion id="AR152-g-AC2" cell_refs="AR-g-152"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g152_checks.py guard</invocation><expect>^AR-G152-OK</expect></criterion>

<criterion id="AR152-g-AC3" cell_refs="AR-g-152"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g152_checks.py regress</invocation><expect>^AR-G152-REGRESS-OK</expect></criterion>

<expected_criteria>AR152-g-AC1,AR152-g-AC2,AR152-g-AC3</expected_criteria>

- AC1 runs the real reader over a recording transport: the call is the recipe form with the five params in order, the encoded request (`urlencode(..., safe=":,")`) is `/charts/fund_data.json?securities=id:SPY,include:true,,&calcs=id:level,include:true,,&zoom=max&maxPoints=100000&partner=basic_2000`, the four served rows still come back, and the two test files assert the new form (not the old one). At base it FAILs.
- AC2 holds what must not move: the base-100 rows, the spacing sleep (once, 2.0 s, before the second symbol), one call for the first symbol, a blank symbol makes no call, a transport error propagates unchanged, a malformed or empty answer gives `[]`, the window filter and the re-seeding at 100. At base it PASSes.
- AC3 runs each existing adapter, transport, price-source, tier and binding test file on its own and then that the branch changed only your files, your folder, the order and the channel file (against the merge-base with `box/dell2`). At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. The transport, the lease, the tiers list, the budget and every file not listed are not yours.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/price_adapter_ycharts.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_adapter_ycharts.py
infra/aws/lambda/investor-reporting/reports/tests/test_ycharts_price_tier.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~276/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-152.ycharts-price-recipe-form.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R52_G.md</decomp_doc> round 52, workstream ~G, cell `AR-g-152`.
<owned_cells>AR-g-152</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR152-g-AC1, AR152-g-AC2, AR152-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~276/IRPT_ANLREQ.TO-AR-g-152.ycharts-price-recipe-form.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-152`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR152-g-AC1,AR152-g-AC2,AR152-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 4.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one existing module and two existing tests; no deploy, no AWS call, no network. The adapter reaches production only through the r34i resident release under its own never-widen pair; until then the r34h resident keeps the old form (refused 400 by YCharts), which is why the tier stays unused (CTO msg 9991).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the issuer's check `ar_g152_checks.py` was dry-run at the base (build FAIL, guard PASS) and against a scratch copy of the three files with the reference fix (build OK, guard OK) and four mutants (the params with no partner, a single trailing comma in calcs, calcs placed after zoom, a single trailing comma in securities); each fails build. Traps: a form that differs by one comma (the wire form is what YCharts reads), the key order (the request is encoded in dict order), the symbol case. NOT seen (blind): whether YCharts answers this form for a plain ticker (IB2's recipe-form read, AR-g-151, measures it; if it needs a typed id the cell is recut) and the served single-ticker shape (the adapter's fixtures only); denominator: 4 build groups, 8 guard arms.
</preflight>

- Cut on the CTO's ruling (msg 9991) from the CRO's captured map by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: AR152-g-AC1 FAILs, AR152-g-AC2 PASSes, AR152-g-AC3 PASSes (in the worker's worktree).
