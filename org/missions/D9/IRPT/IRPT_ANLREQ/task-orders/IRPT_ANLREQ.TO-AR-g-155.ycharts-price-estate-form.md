# TO-AR-g-155 -- the YCharts price adapter asks YCharts in the estate client's own form, by calling the estate builder unchanged (FWD-7 C-PRICES; CTO msgs 10040, 10070 and 10079): a URL-only subclass of ycharts_client.YChartsClient, calc price (level for a ^ index), byte-equal to the request that answered 200

<to_id>IRPT_ANLREQ.TO-AR-g-155</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~278</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>53</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-155` (`decompositions/IRPT_ANLREQ_DECOMP_R53_G.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none (the adapter and the transport are merged on the trunk). Order: CTO msgs 10040 (r34j re-adds the tier on the estate form by CALLING the estate builder), 10070 and 10079 (option C accepted, with two pinning tests). The measured request: IB2's `PRICE_FORM_READ.txt` (HTTP 200, 1,256 points for SPY).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~278`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-278` (branch `wk-IRPT_ANLREQ-278`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~278 <0.9.0_WK_IRPT_ANLREQ~278@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W278-S<k>` (take the next free `<k>`; check the channel file for `W278` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only in the product files. Do not touch anything outside the `<paths>` block. `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py` is READ ONLY: never edit it.

### THE CELL (`AR-g-155`, inlined)

Today `price_adapter_ycharts.make_reader` sends `transport("/charts/fund_data.json", {"securities": "id:" + name + ",include:true,", "zoom": "max"})`, which YCharts refuses with HTTP 400. The estate already has the form that answers 200: `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py`, `YChartsClient.fund_data(yc_symbol, calc="level", max_points=100000)` (lines 219-249): 41 query parameters, `calcs=id:<calc>,include:true,,`, calc `price` for a security or ETF and `level` only for a `^` index. That client sends through its OWN credentials and `urllib`, so it must never be called as it stands from the resident (it would bypass the provider lease and the host budget). The way in, ruled by the CTO: call its builder UNCHANGED with the sending taken away.

1. **New module** `infra/aws/lambda/investor-reporting/ycharts/research/price_form_ycharts.py`, exactly this behaviour (write it in this shape):

        def _client_module():
            # import ycharts_client; if it is not importable (the repository layout), put the sibling Lambda directory on sys.path and import it:
            # os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "ycharts-market-data-pull"))
            ...

        def request_path(symbol):
            name = symbol.strip().upper()
            if not name:
                raise ValueError("PRICE_FORM_SYMBOL_BLANK")
            yc = _client_module()
            class _UrlOnly(yc.YChartsClient):
                def __init__(self):      # no secret read
                    pass
                def _request(self, url, body=None):      # no network call: hand back the URL
                    return {"url": url}
            url = _UrlOnly().fund_data(name, calc="level" if name.startswith("^") else "price")["url"]
            if not url.startswith(yc.BASE + "/"):
                raise ValueError("PRICE_FORM_URL")
            return url[len(yc.BASE):]

   A module docstring says what it is and why (the estate builder called unchanged; the sending is the lease transport's), in the repository's plain style. Importing it and calling `request_path` reads no secret and makes no network call.
2. **The adapter.** In `price_adapter_ycharts.py` add `import price_form_ycharts` (beside `import tr_level`) and replace the one `transport(...)` call in `reader` by `answer = transport(price_form_ycharts.request_path(name), {})`: the transport (`price_transport_ycharts`) sends a path with no params unchanged. Nothing else in the module changes (one call per symbol, the 2 s spacing sleep before every call but the first, the blank-symbol rule, the window filter, the base-100 chaining, errors propagate), except the module docstring: one sentence naming the form and its source (the estate client's fund_data builder, calc price), and one saying the served levels are PRICE levels so the chained series is a price return, not a total return.
3. **Two new test files** in `infra/aws/lambda/investor-reporting/ycharts/research/tests/` (offline, no network, no AWS):
   - `test_price_form_ycharts.py`: (a) `request_path(" spy ")` is BYTE-EQUAL to the SPY path literal `EXPECT_SPY` in the issuer's checker `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g155_checks.py` (copy that literal into the test; it is the request IB2's HTTP 200 read made, 41 parameters, 760 characters); (b) `request_path("^spxtr")` carries `calcs=id%3Alevel%2Cinclude%3Atrue%2C%2C` and `securities=id%3A%5ESPXTR%2Cinclude%3Atrue%2C%2C`; (c) `request_path("AAPL")` carries `calcs=id%3Aprice%2Cinclude%3Atrue%2C%2C`; (d) a blank symbol raises `ValueError`; (e) with `urllib.request.urlopen` and a fake `boto3` module whose `client` raises, building a path still works (no network, no secret). The file must contain the strings `aiSummaries=` and `chartCreator=false` (they are in the literal).
   - `test_ycharts_client_pin.py`: the subclass leans on a private method, so pin the client: with `inspect.signature`, `str(inspect.signature(YChartsClient.fund_data))` equals `(self, yc_symbol: 'str', calc: 'str' = 'level', max_points: 'int' = 100000) -> 'dict'` and `str(inspect.signature(YChartsClient._request))` equals `(self, url: 'str', body: 'bytes | None' = None) -> 'dict'`; and `inspect.getsource(YChartsClient.fund_data)` contains `self._request(`. Import the client through `price_form_ycharts._client_module()`. A change to either signature fails this test, by design.
4. **Move the two existing tests that assert the old form:** `ycharts/research/tests/test_price_adapter_ycharts.py` (the `fake.calls` assertion for `QQQ`: now `[(price_form_ycharts.request_path("QQQ"), {})]`; import `price_form_ycharts` in the test) and `infra/aws/lambda/investor-reporting/reports/tests/test_ycharts_price_tier.py` (the `session.paths` assertion for `SPY`: now a one-element list holding `price_form_ycharts.request_path("SPY")`; the file needs `price_form_ycharts` importable the way its other research modules are). Do not edit `test_price_transport_ycharts.py`.
5. Run the three criteria. Commit the code and tests, then the proof and the status flip, as separate commits (code first).
6. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR155-g-AC1" cell_refs="AR-g-155"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g155_checks.py build</invocation><expect>^AR-G155-OK</expect></criterion>

<criterion id="AR155-g-AC2" cell_refs="AR-g-155"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g155_checks.py guard</invocation><expect>^AR-G155-OK</expect></criterion>

<criterion id="AR155-g-AC3" cell_refs="AR-g-155"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g155_checks.py regress</invocation><expect>^AR-G155-REGRESS-OK</expect></criterion>

<expected_criteria>AR155-g-AC1,AR155-g-AC2,AR155-g-AC3</expected_criteria>

- AC1 runs the real module and the real adapter: the estate client's two signatures are the pinned ones; `request_path(" spy ")` is byte-equal to IB2's request; a `^` index gets calc level and a plain symbol calc price; a blank symbol raises; building a path reaches no network and no secret; the adapter's one call is `(the SPY path, {})`; the two new test files exist with the pins in them; the two moved tests assert the new form. At base it FAILs.
- AC2 holds what must not move: the base-100 rows, the spacing sleep (once, 2.0 s, before the second symbol), one call for the first symbol, a blank symbol makes no call, a transport error propagates unchanged, a malformed or empty answer gives `[]`, the window filter and the re-seeding at 100. At base it PASSes.
- AC3 runs each existing adapter, transport, price-source, tier and binding test file on its own plus your two new test files, then that the branch changed only your files, your folder, the order and the channel file (against the merge-base with `box/dell2`). At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. `ycharts_client.py`, the transport, the lease, the tiers list, the budget and every file not listed are not yours; `ycharts_client.py` is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/price_form_ycharts.py
infra/aws/lambda/investor-reporting/ycharts/research/price_adapter_ycharts.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_form_ycharts.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_ycharts_client_pin.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_adapter_ycharts.py
infra/aws/lambda/investor-reporting/reports/tests/test_ycharts_price_tier.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~278/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-155.ycharts-price-estate-form.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R53_G.md</decomp_doc> round 53, workstream ~G, cell `AR-g-155`.
<owned_cells>AR-g-155</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR155-g-AC1, AR155-g-AC2, AR155-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~278/IRPT_ANLREQ.TO-AR-g-155.ycharts-price-estate-form.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-155`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR155-g-AC1,AR155-g-AC2,AR155-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 6.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- two new product files, one changed, four test files; no deploy, no AWS call, no network. The change reaches production only through the r34j resident release under its own never-widen pair; until then the r34i resident does not use the YCharts tier at all (its bindings list estate and yfinance). The estate client is read, never edited.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the issuer's check `ar_g155_checks.py` was dry-run at the base (build FAIL, guard PASS) and against a scratch copy with a reference fix (build OK, guard OK) and six mutants (calc always price, no upper-casing, the client's BASE not stripped, params not empty, a blank symbol that does not raise, calc level for every symbol); each fails build. Traps: sending the estate client's own request (its credentials and urllib path bypass the lease and the budget: the subclass skips __init__ and returns the URL), the encoding (the request is the client's own urlencode defaults, %3A and %2C, which is what answered 200), the private _request the subclass leans on (pinned by signature). NOT seen (blind): a symbol other than SPY (one sample), the signed-out call, whether YCharts keeps answering this form (it answered 67 of 67 in May and once on r34h); denominator: 7 build groups, 8 guard arms.
</preflight>

- Cut on the CTO's rulings (msgs 10040, 10070, 10079) from the CRO's research @c9f3005376 and IB2's HTTP 200 read, by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: AR155-g-AC1 FAILs, AR155-g-AC2 PASSes, AR155-g-AC3 PASSes (in the worker's worktree).
