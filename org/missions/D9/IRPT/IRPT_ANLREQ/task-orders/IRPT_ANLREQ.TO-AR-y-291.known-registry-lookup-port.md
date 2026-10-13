# TO IRPT_ANLREQ.TO-AR-y-291.known-registry-lookup-port -- C-SWAP step 1: the registry identity port reads etf-classifications and MDPF_SECHIST's index, KNOWN is evidence

<to_id>IRPT_ANLREQ.TO-AR-y-291</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~105</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-291` (`decompositions/IRPT_ANLREQ_DECOMP_R23C_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~105`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-105` (branch `wk-IRPT_ANLREQ-105`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~105 <0.9.0_WK_IRPT_ANLREQ~105@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W105-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-291`, inlined) -- THE KNOWN PASS. Code and tests only; every test on fakes; nothing is released.

**C-SWAP (PRD `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` :104), steps (1) KNOWN and (2) the YFINANCE CHECKER, and the CTO's rulings (msg 7210) on the read `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~99/r23/C_SWAP_STEPS_1_2_READ.json` (cell `AR-y-278`, drained @de81ce19c1):** one pass per unknown holding; a holding the provider (YCharts `securities_info`) answers NOT_FOUND is checked against the registry (step 1) and then with ONE yfinance `history(period='1mo')` call (step 2); rows greater than 0 with a finite positive last close means KEPT (KEEP still requires history). Rulings: **K = 10 unknown symbols checked per upload, one call each, paced at 1 s**; unknowns beyond 10 get the EXISTING proxy prompt, worded 'not checked'; **a yfinance exception, a timeout, or an error-shaped empty frame reads CHECK_FAILED, shown in words and never treated as absent: make the client raise** (yfinance hides exceptions by default and returns an empty frame: MEASURED, ALPPL, BREIT and CCCQ returned 0 rows with no exception, ALPPL printed an HTTP 404 'Quote not found'); a 401, 403 or 429 stops the step for the rest of the upload. No Andrew word is needed for the Yahoo egress: standing law, CLAUDE.md Agent Autonomy ('Egress is open on every channel, except Bloomberg'; 'other vendor APIs need no per-use word'; Andrew-direct 2026-10-09, `ANDREW_DIRECT_20261009_024xZ_LAW_EDIT_*`), which postdates the MDPF_SECHIST addendum's limit: cite it in the record. MEASURED: `TIMXX` returns 20 daily rows, last close 1.0 (a money-market fund): KEPT, no proxy. The registry row and the price landing for a KEPT symbol are MDPF_SECCLASS's and MDPF_SECHIST's (dell1) and are NOT this cell's (the CTO routes them). The withdrawn Kimi model-proposed swap is retired and reverted (@c822052bc4): do not touch `resolution_kimi.py` or `upload_suggestions.py`.
**THE INTERFACE (fixed here so the three cells build in parallel):** a new module `infra/aws/lambda/investor-reporting/intake/yfinance_check.py` (cell B) exposes `class YfinanceChecker(*, history=None, sleep=time.sleep, clock=time.monotonic, cap=10, pace_seconds=1.0)` with `check(symbols) -> dict` mapping each UPPER-CASE symbol to `{'state': 'KEPT' | 'NOT_KEPT' | 'CHECK_FAILED' | 'NOT_CHECKED', 'rows': int, 'last_close': float | None, 'reason': str}`; `history(symbol)` is an injected port returning a list of `(date_iso, close)` pairs and RAISING on any error (the default builds the real yfinance call with exceptions made to raise); `NOT_CHECKED` is a symbol beyond the cap; `CHECK_FAILED` carries a reason word (`EXCEPTION`, `TIMEOUT`, `PUSHBACK`, `ERROR_FRAME`); `NOT_KEPT` is a clean empty answer. The resolver (cell C) consumes it: the resolution result for a symbol the provider answered NOT_FOUND gets a new state `KEPT` (reason `YFINANCE_HISTORY`, `price_source 'yfinance'`, the checker's rows and last close, NO provider receipt) when the checker says KEPT; `CHECK_FAILED` and `NOT_CHECKED` keep the symbol unknown and carry their reason words to the finding.

1. **Read first:** the read record above (`estate.registry`, `design.step_1_known`), `infra/aws/lambda/investor-reporting/intake/security_resolution.py` :204-212 (the identity port and the comment that a registry hit is evidence, not FOUND), `ycharts/generate/resident_worker.py` :610-630 (the identity argument, stubbed to None at :619-620), `ycharts/session/resident_session.py` :130-150 (`template_resolver`), `infra/aws/terraform/yang-pipeline/etf-classifications.tf` :1-60 (the table: hash key `ticker`; READ only), `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` (`ETFClassifier.get_classification`, how the estate reads it), and the resident role's permissions as the repo declares them (`infra/aws/terraform/` for the resident's IAM: search a NAMED folder; READ only; the read record says the resident's IAM for the table is NOT read). Record `read` {`identity_port_contract` (what the port receives and must return: file:line), `table_read_shape`, `resident_iam_for_the_table` (yes, no or NOT READ, with the file:line that decides), `sechist_index` (where MDPF_SECHIST's per-security index is and how it is read; read only; NOT READ is a legal answer)}. **If the resident's role cannot read `etf-classifications` (or the table's ARN is not in its policy), do NOT edit IAM or Terraform: build the port with the table client INJECTED, state the IAM need in `release_needs`, and continue.**
2. **The port.** Wire the identity port to a read-only lookup: `GetItem` (or a batch get of at most 25 keys) on `etf-classifications` by upper-case ticker, via an injected client (the default is built from the resident's AWS session where the session factory builds its other clients; the table NAME comes from `lib/opal_naming.py` output or the estate's existing constant, never typed from memory: read how the other table names reach the resident). A hit returns the registry identity as EVIDENCE (the reference), exactly as the file's comment requires: **it never turns a provider NOT_FOUND into FOUND**; a registry hit with no provider row is `KNOWN` for the report of the upload (cell C reads it; define the key the resolver returns, e.g. `registry: {ticker, asset_class, sub_asset_class}`), and a KNOWN symbol is not sent to the yfinance checker. Any read error is `registry_unavailable` for that symbol (never a guess), and the resolver continues as today. No write of any kind. MDPF_SECHIST's index is read only if the read found a read-only way for the resident; else leave it out and say so.
3. **Tests, offline, on fakes (at least 8), new file `ycharts/generate/tests/test_registry_identity_port.py`:** a hit is evidence and does not make FOUND; a miss returns nothing; a read error returns `registry_unavailable` and the resolver result is today's; the lookup is by upper-case ticker and batches at most 25; no write method is ever called on the client (a spy); the port is used only for provider NOT_FOUND symbols; no port injected: byte-identical to today; the table name comes from the constant, not a literal in the port. Plus `intake/tests` additions if the resolver changes (a small file `intake/tests/test_registry_known.py`). `before_arm`: the evidence test FAILS at HEAD (the port is a None stub). Then `intake/tests` (370 floor) and the `ycharts/generate/tests` files that collect (known baseline: 4 custody failures).
4. **Write `r23/KNOWN_REGISTRY_PORT.json`:** `read`, `port` (files, lines), `tests`, `before_arm`, `release_needs` (IAM, Terraform, a package member), `claim`, `not_read`.
5. **In your report:** whether the resident can read the table today, the port's contract, the counts, `release_needs`.

### ACCEPTANCE

<criterion id="AR291-y-AC1" cell_refs="AR-y-291"><invocation>python C:/dev/wk-irpt-anlreq-105/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y291-known --root C:/dev/wk-irpt-anlreq-105</invocation><expect>Y291-KNOWN-OK</expect></criterion>
`AR291-y-AC1`: the record states the port's contract and whether the resident's role can read the table (file:line), a new test file with at least 8 passing tests whose evidence case fails at HEAD, and the intake folder passes at 370 or more.

<criterion id="AR291-y-AC2J" cell_refs="AR-y-291" judgment="true"/>
`AR291-y-AC2J` (judgment, graded at L9, never by you): a registry hit is evidence and never FOUND, the lookup is read-only (a spy proves no write), a read error is `registry_unavailable` and never a guess, no IAM or Terraform was edited, the table name is not a typed literal, and nothing was released.

<expected_criteria>AR291-y-AC1 AR291-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~105/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/intake/security_resolution.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/session/resident_session.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_registry_identity_port.py
infra/aws/lambda/investor-reporting/intake/tests/test_registry_known.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23C_Y.md</decomp_doc>
<owned_cells>AR-y-291</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~105/IRPT_ANLREQ.TO-AR-y-291.known-registry-lookup-port.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-291`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR291-y-AC1,AR291-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test edits in a worktree; every test on fakes; nothing is released, deployed or called; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the PRD's C-SWAP and the CTO's rulings (msg 7210) against the cell; the lens: an outage read as absence, a KEPT holding without history, a symbol beyond the cap silently dropped or silently checked, a model in the loop, a live call from a test. The order requires the client to raise, CHECK_FAILED in words, the cap and the 1 s pace pinned, and every test on fakes. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's rulings on the C-SWAP read (msg 7210: 'Cut A to C'; K = 10, 1 s pace, CHECK_FAILED never absent) as workstream `Y` round 25. The grant names every file the cell writes. Base: `AR291-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
