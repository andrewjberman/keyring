# TO-AR-g-90 -- the resident switches its Opal reports to priced runs from an optional binding: the BBG-history and Yahoo readers on the host's own clients, and T-1 from the clock

<to_id>IRPT_ANLREQ.TO-AR-g-90</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~190</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-90` (`decompositions/IRPT_ANLREQ_DECOMP_R17_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** `AR-g-86` (merged `1c84d38bf4`, the price stage and its `stores` keys), `AR-g-81` and `AR-g-83` (merged, the readers), `AR-g-85` and `AR-g-87` (merged, which edited the same file).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~190`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-190` (branch `wk-IRPT_ANLREQ-190`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/` and `org/missions/D9/IRPT` on disk (it has no portal sub-worktree; your cell does not touch the portal). Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~190 <0.9.0_WK_IRPT_ANLREQ~190@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W190-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

### Read first (under `C:/dev/wk-irpt-anlreq-190/infra/aws/lambda/investor-reporting/`)

- `reports/resident_installed.py` (the whole file: `load_bindings`, `make_opal_stores`, `_opal_map_loader`, and `build_resident_runtime` where `make_opal_stores(...)` is called) and `reports/tests/test_resident_installed.py` (the `package` fixture, `fake_clients`, `rewrite`, `opal_record`, `sha`).
- `ycharts/research/price_adapter_bbg.py` (`make_reader(s3, *, partitions=None)`: reads `opal-data-etfs/bbg/...` through the client it is given), `ycharts/research/price_adapter_yfinance.py` (`make_reader(*, fetch=None, yf=None)`) and `ycharts/research/opal_producer.py` (the `stores` keys `pricing`, `price_readers`, `as_of`, documented in its docstring).
- `ycharts/generate/resident_worker.py` `load_opal_producer` (line 189): it puts `ycharts/research` on `sys.path` and imports `opal_producer`.

### THE CELL (`AR-g-90`, inlined)

`AR-g-86` made the Opal producer able to price its report from three `stores` keys (`pricing`, `price_readers`, `as_of`), but no caller sets them. This cell makes the resident set them, from an OPTIONAL binding that is off unless it says otherwise, so the capability ships dormant and is switched on by a bindings edit once the host has the libraries. Only two tiers are wired: `estate` (the BBG history reader on the host role's own S3 client; the host role already holds the `bbg/*` read grant) and `yfinance` (the Yahoo reader on its own default fetch; the `yfinance` library is imported only when a symbol is asked). The YCharts tier and the DEMQUE tier are NOT wired here (the first needs the session transport, the second needs a bucket grant the CTO has not ruled).

**`reports/resident_installed.py`, exactly this:**
1. Add the import `import datetime` (alphabetical among the existing imports) and, next to `OPAL_MAP_BINDING`, a comment and the constants `OPAL_PRICING_BINDING = "opal_pricing"` and `PRICING_TIERS = ("estate", "yfinance")`. The comment says the binding is `{"enabled": bool, "tiers": [...]}`, that the producer prices when it is enabled, that absent or not enabled it runs unpriced as before, and that the tiers are the chain tiers this resident can read today.
2. In `load_bindings`, before the `commentary_ready_queue_url` / packager check, validate the binding when the key is present, refusing with `ResidentInstallRefused("RESIDENT_PRICING_BINDINGS")` (that exact text, no suffix) unless ALL hold: it is a `dict` whose keys are exactly `enabled` and `tiers`; `enabled` is a real `bool` (`type(x) is bool`); `tiers` is a `list` of `str`, each one of `PRICING_TIERS`, with no repeat; and `tiers` is non-empty when `enabled` is true. Absent key: nothing changes.
3. New module function `_t_minus_1(epoch)`: the UTC date of `epoch` (seconds), minus one day, then minus further days while it is a Saturday or Sunday; returned as `YYYY-MM-DD`. (It is never later than the true T-1, so no row of the run's own day is read; on a holiday it is earlier by a day that has no row, which the chain skips.)
4. New module function `_pricing_extras(bindings, clients, clock)`: returns `None` unless `bindings.get(OPAL_PRICING_BINDING)` is a dict with `enabled` exactly `True`; otherwise returns a function `extras()` that: calls `resident_worker.load_opal_producer()` (imported inside, as `make_opal_stores` imports `producer_for`) so `ycharts/research` is on `sys.path`; builds the readers dict for each tier of the binding IN ITS ORDER (`estate` -> `price_adapter_bbg.make_reader(clients["s3"])`, `yfinance` -> `price_adapter_yfinance.make_reader()`; each adapter imported inside the function); and returns `{"pricing": True, "price_readers": readers, "as_of": _t_minus_1(clock())}`.
5. `make_opal_stores(...)` gains the keyword `pricing_extras=None`. In the returned `opal_stores(principal, record)`, after the `stores` dict is built and BEFORE `stores.update(extras or {})`: `if pricing_extras is not None: stores.update(pricing_extras())`. So the offline `extras` still win. Nothing else in the function changes.
6. `build_resident_runtime` passes `pricing_extras=_pricing_extras(bindings, clients, clock)` to `make_opal_stores`.
7. Nothing else changes: not `build_resident_package.py`, not the bindings file in the package, not `opal_producer.py`.

**Tests.** A NEW file `reports/tests/test_opal_pricing_binding.py`, offline, importing the fixtures and helpers of `test_resident_installed.py` as the neighbouring tests do (`from test_resident_installed import fake_clients, opal_record, package, rewrite, ri, sha`, with `# noqa: E402,F401,F811`), with these exact test function names (the checker looks for each by name). Build the runtime with the `package` fixture, an `opal_map` binding to a tiny map file (as `with_opal` does in that file), `clock=lambda: 1_800_000_000` (a Friday, 2027-01-15), and an Opal record that `producer_for` admits without the allow list (`opal_record(...)` plus `"ticket_confirmed": True`, an unlisted owner):
`test_absent_binding_adds_nothing` (no `pricing`, `price_readers` or `as_of` in the stores), `test_enabled_binding_supplies_pricing_readers_and_t_minus_1` (tiers `["estate", "yfinance"]`: `pricing` is True, both readers callable, `as_of` is `"2027-01-14"`), `test_t_minus_1_skips_weekends` (a Monday and a Sunday of your choosing), `test_bad_bindings_refuse_the_load` (several bad shapes, including a tier outside `PRICING_TIERS`, an empty enabled list and a non-dict), `test_estate_tier_uses_the_host_s3_client_and_the_bbg_prefix` (a fake `s3` whose `list_objects_v2` records its keywords and returns `{"Contents": [], "IsTruncated": False}`; the estate reader called for one symbol returns `[]` and asked `Bucket="opal-data-etfs"`, `Prefix="bbg/"`), `test_offline_extras_win` (`make_opal_stores(..., extras={"pricing": False}, pricing_extras=lambda: {"pricing": True})` returns `pricing` False).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR90-g-AC1" cell_refs="AR-g-90"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g90_checks.py g90</invocation><expect>^AR-G90-OK</expect></criterion>

<criterion id="AR90-g-AC2" cell_refs="AR-g-90"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g85_checks.py regress</invocation><expect>^AR-G85-REGRESS-OK</expect></criterion>

<expected_criteria>AR90-g-AC1,AR90-g-AC2</expected_criteria>

- AC1 builds the real runtime with the issuer's 25 tests (no keys when the binding is absent or disabled; the keys when enabled; only the named tiers; T-1 over a week and a weekend; the estate reader's bucket and prefix on the host client; 14 bad bindings refused with the exact text and 3 good ones loaded; the offline extras winning), then checks your six named tests exist and pass. At base it FAILs.
- AC2 runs seven existing test files one at a time (66 tests) and needs all of them to pass. At base it PASSes. Run it under `timeout 300`.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_opal_pricing_binding.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~190/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-90.resident-pricing-binding.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R17_G.md</decomp_doc> round 17, workstream ~G, cell `AR-g-90`.
<owned_cells>AR-g-90</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR90-g-AC1, AR90-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~190/IRPT_ANLREQ.TO-AR-g-90.resident-pricing-binding.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-90`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR90-g-AC1,AR90-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the functions you changed or added with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `make_opal_stores` is called once, by `build_resident_runtime` in this file (and by tests); the new keyword defaults to `None`, so every caller is unchanged. `load_bindings` is called by `build_resident_runtime` and the release build's checks: an absent `opal_pricing` key changes nothing, and no shipped bindings file carries it. The producer's keys (`pricing`, `price_readers`, `as_of`) are read only by `opal_producer`. Nothing is deployed, so no edge changes until the release cell ships the file; even then the capability stays off until a bindings edit enables it.
comp-iam: DECLARED-NOT-APPLICABLE in this cell -- no AWS call and no permission change; the estate tier reads `opal-data-etfs/bbg/*` through the host role's S3 client, which already holds that grant (R11 decomposition, `resident.tf` line 140), and the Yahoo tier needs egress and the `yfinance` library on the host (a CloudOps pair, in the release cell).
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the compose read (q4, the pricing-flag seam) and the R11 host facts. Traps: T-1 set to the run's own day (today's partial row read); a weekend T-1 (a day with no row, then the chain still works, but the date claim is wrong); a tier outside the wired two accepted by the binding (YCharts or DEMQUE named, then silently ignored); `enabled` truthy rather than `True` (the string "false" turns pricing on); the tiers ignored; the host S3 client not the one passed to the reader (the estate tier then reads nothing); the offline `extras` overridden by the binding. The checker feeds a green arm (a reference build passes the 25 issuer tests, the six named tests and the 66 regress tests) and seven mutant arms (T-1 = the run day: 2 issuer tests fail; weekends not skipped: 1; "ycharts" admitted: 1; the estate reader built on no client: 1; offline extras overridden: 1; `enabled` ignored: 2; tiers ignored: 1).
</preflight>

- Cut on the compose read (`q4`), the R11 host facts and the issuer's reference build. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR90-g-AC1` FAILs and `AR90-g-AC2` PASSes (66), as expected.
- The binding is OPTIONAL and the shipped bindings file is the release cell's: until it enables the binding, every Opal job runs unpriced exactly as before. The YCharts and DEMQUE tiers join in later cells.
