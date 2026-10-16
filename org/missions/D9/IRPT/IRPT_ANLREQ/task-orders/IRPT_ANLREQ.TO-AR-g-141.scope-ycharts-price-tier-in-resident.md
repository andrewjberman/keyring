# TO-AR-g-141 -- SCOPE the YCharts price tier in the resident (FWD-7, C-PRICES): a read-only record of what exists and what is missing, nothing under infra/ changes

<to_id>IRPT_ANLREQ.TO-AR-g-141</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~268</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>46</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-141` (`decompositions/IRPT_ANLREQ_DECOMP_R46_G.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none (r34g carries the pricing binding with the tiers estate and yfinance). Order: CTO msg 9694 (the YCharts tier is owed with item 4) and msg 9620 (the Opal-built report is the next ENGINE cell).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~268`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-268` (branch `wk-IRPT_ANLREQ-268`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~268 <0.9.0_WK_IRPT_ANLREQ~268@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W268-S<k>` (take the next free `<k>`; check the channel file for `W268` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- **READ-ONLY on the product.** You change nothing under `infra/`, `lib/` or `reports/`. Your only output is one JSON record in your folder. No network, no AWS call, no push.

### THE CELL (`AR-g-141`, inlined)

C-PRICES and FWD-7 say each security's price comes, in order, from: the estate's own stores; Yahoo (yfinance, cut at T-1); YCharts through the stored session, ONE symbol per call; then the backend replacement (C-SWAP). The resident prices the Opal producer's report only when the pricing binding is enabled, and today it builds readers for TWO tiers, `estate` and `yfinance` (`infra/aws/lambda/investor-reporting/reports/resident_installed.py`, the `PRICING_TIERS` constant near line 78, the binding validation near lines 115-124 and `_pricing_extras` near lines 373-394). `ycharts/research/price_source.py` already lists the chain `("estate", "yfinance", "ycharts")`, and `ycharts/research/price_adapter_ycharts.py` already holds `make_reader(transport, ...)`, a YCharts price reader over an INJECTED transport that makes one `fund_data` call per symbol. What does not exist is the third tier in the resident. Your job is to find, by reading, EVERYTHING a later cell needs to add it, and what is missing.

Read at least: `reports/resident_installed.py` (the lines above and where `_pricing_extras` is used), `ycharts/research/price_source.py`, `ycharts/research/price_adapter_yfinance.py` and `price_adapter_bbg.py` (the tier readers that exist, as templates), `ycharts/research/price_adapter_ycharts.py`, `ycharts/session/operation_lease.py` and `ycharts/session/resident_session.py` (how the resident's stored session and the provider lease make a YCharts call, and the SPACING it enforces), `ycharts/research/runner.py` (the research runner's count-per-window rule near lines 201-211 and 547), and the tests that pin the pricing binding (`reports/tests/test_opal_pricing_binding.py`). Search with the Grep and Glob tools for `make_reader`, `PRICING_TIERS`, `price_readers`, `transport(` and `fund_data`.

Write ONE file: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~268/YCHARTS_PRICE_TIER_SCOPE.json` (create the folder). Shape (a JSON object):
- `entry_points_read`: list of the repo-relative paths you read first (each must be a file that exists).
- `rows`: one row per finding, each with: `site` ("repo-relative/path.py:LINE"), `line_text` (that exact line, stripped), `what` (one sentence), `role` (exactly one of READER_TEMPLATE, PRICE_FETCH, SESSION_OR_LEASE, WIRING, TIER_LIST, CAP_OR_BUDGET, TEST_FIXTURE, OTHER), `use` (one sentence: what a later cell does with this line, or must change in it), `claim` ("MEASURED" if you read the line and followed what it calls, "INFERRED" if you reasoned past what you read). The set of rows must include at least one of each of: READER_TEMPLATE (a tier reader the new tier copies), PRICE_FETCH (the YCharts call that returns a price series for one symbol), SESSION_OR_LEASE (how a call through the resident's stored session and the provider lease is made, and its spacing), WIRING (where the resident builds tier readers and where the pricing keys reach the Opal producer), TIER_LIST (every place the tier names are enumerated or validated).
- `summary`: `{"rows": <number of rows>}`.
- `gaps`: a list of strings, each a thing a later cell needs and you could NOT find in the repository (for example, no transport object over the stored session exists for the price adapter; the lease is not reachable from the Opal producer's process). An empty list means you found none; say so only if you are sure.
Do not guess a line number: copy it from a Read or Grep result.

1. Run the two criteria. Commit the record, then the proof and the status flip, as separate commits (record first).
2. **Report** the commit hashes, the row count, the `gaps` list in full, the sites with role WIRING and TIER_LIST, and both criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR141-g-AC1" cell_refs="AR-g-141"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g141_checks.py verify org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~268/YCHARTS_PRICE_TIER_SCOPE.json</invocation><expect>^AR-G141-OK</expect></criterion>

<criterion id="AR141-g-AC2" cell_refs="AR-g-141"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g141_checks.py scope box/dell2 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~268 org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-141.scope-ycharts-price-tier-in-resident.md</invocation><expect>^AR-G141-SCOPE-OK</expect></criterion>

<expected_criteria>AR141-g-AC1,AR141-g-AC2</expected_criteria>

- AC1 checks the record is well formed and every citation is real: each `site` exists at that line and its `line_text` equals the file's line; every row has a role from the closed list, a claim word, what and use; the summary equals the rows; the five roles the cell needs are all present; `gaps` is a list. At base (no record) it FAILs. It does not grade whether the scope is complete: the issuer reads the content.
- AC2 checks (against the merge-base with `box/dell2`) that your branch changed nothing outside your own folder, your order, the channel file and the issuer's issuance files. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. READ-ONLY on the product.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~268/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-141.scope-ycharts-price-tier-in-resident.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R46_G.md</decomp_doc> round 46, workstream ~G, cell `AR-g-141`.
<owned_cells>AR-g-141</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR141-g-AC1, AR141-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~268/IRPT_ANLREQ.TO-AR-g-141.scope-ycharts-price-tier-in-resident.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-141`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR141-g-AC1,AR141-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 2.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- a read-only scope record; the only write is one JSON record and the proof in the worker's folder. Nothing deployed, no AWS call, no network.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call. comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. 
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; a read-only scope record.
comp-adversary: RUN -- the issuer's verifier `ar_g141_checks.py` was dry-run on a good record and on four bad ones (a missing required role, a wrong line_text, a summary that does not equal the rows, no gaps list) and a missing file: the good one passes, each bad one fails. Traps: a cited line that does not hold the quoted text; a scope that lists only the first hit of each term; a tier reader invented rather than found; a gap left out because a search found nothing in the wrong place. NOT seen (blind): whether the scope is COMPLETE (the verifier checks citations and the five roles, not coverage; the issuer reads the content before cutting the build cell); denominator: the files named in the cell.
</preflight>

- Cut on the CTO's msgs 9620 and 9694 (the YCharts price tier is owed; the Opal-built report is the next ENGINE cell) by the issuer inside its own decomposition. Risk LOCAL (a record). Base: AR141-g-AC1 FAILs (no record), AR141-g-AC2 PASSes (in the worker's worktree).
