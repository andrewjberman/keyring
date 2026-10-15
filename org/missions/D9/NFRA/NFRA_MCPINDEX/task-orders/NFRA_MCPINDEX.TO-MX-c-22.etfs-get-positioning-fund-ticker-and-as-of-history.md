# NFRA_MCPINDEX task order -- `MX-c-22` -- the `etfs_get_positioning` extension: optional `fund_ticker` and as_of history from the gold book and holding tables, the existing answer byte-equal

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-22</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-22</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~46</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant change: the tool reads `gold/book` and `gold/holding` of the ETFs bucket through the catalog rows the internal reader role already covers (NFRA_OPLGTW OG-ap-20 grant). No AWS call in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- the byte-equal difference control (c22.AC1, base tree against new tree) and the planted arms (decomposition R18.4) are the control; the tool is Opal-principal-only and the release that ships it is NFRA_OPLGTW's.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-22` (round 18; CRO G5 spec, existing-tool verdict: keep and EXTEND)

Work in your own worktree (cut from `box/sitez`). Every path below is relative to its root. **First**, run once: `git sparse-checkout add infra/aws/ec2/opal-gateway workflows` (the only sparse change you may make). The tool lives in `infra/aws/ec2/opal-gateway/app/integrations/portal_index/integration.py`, function `etfs_get_positioning` inside `PortalIndexIntegration.register` (about line 397); its answer path is the module's `answer`/`_answer`/`resolve`.

**Why.** `etfs_get_positioning(as_of="")` returns the portal's whole ETF positioning object (the four Opal ETFs DIVZ, IDVZ, PFDE, PFOE) with the object's own as-of date, and refuses any other `as_of`. The CRO's G5 spec (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5_etfs.md`, the proposed-tools table row "`etfs_get_positioning` (EXTEND: add as_of, fund_ticker)": today portal-v2 platinum; history gold/book + holding; inputs as_of, fund_ticker) wants one fund, and a past date, from the gold tables. NFRA_OPLGTW's release carries this change (COO~O msg 34536); you build it.

**What to build.**

1. **Signature**: `etfs_get_positioning(as_of: str = "", fund_ticker: str = "") -> dict` (both optional strings, in that order). Update the tool's docstring: the new arguments, and that with neither the answer is unchanged.
2. **No `fund_ticker`** (empty): the existing answer, BYTE-EQUAL to today's for every `as_of` (the empty one, the object's own date, and a different date, which keeps its `no_data` answer), for the internal principal and for a firm principal (its refusal). Do not touch that code path's output.
3. **`fund_ticker` given** (`DIVZ`, `IDVZ`, `PFDE`, `PFOE`; match case-insensitively, answer with the upper-case ticker). An unknown ticker is `status: no_data` with a `reason` naming the four allowed tickers (not an exception).
   - `as_of` empty or equal to the served object's own date: the same envelope as today's answer (`status ok`, `tool`, `bucket`, `key`, `as_of`, `as_of_field`) with `data` restricted to that one fund: read the served object and keep the one fund block whose ticker matches (inspect the object's real shape in the existing tests' fixtures; keep every other key of the object that is not per-fund, such as its provenance, unchanged).
   - `as_of` another date (history): read the fund's `book` (the book totals) and `holding` (its holdings) for that date from the gold tables through the catalog rows `opal_data_etfs_gold_book` and `opal_data_etfs_gold_holding`: the bucket and the key come ONLY from those catalog rows (their `bucket`, `prefix`, `key_template`, read through the same catalog accessor the module and `app/etfs_funds.py` already use; reuse `etfs_funds` helpers such as its `_holdings`, `_book_totals` and `_dated_parts` where they fit rather than writing new S3 code). The answer: `status ok`, `tool`, `fund_ticker`, `as_of`, `source` naming the two catalog row ids, and `data` with `book` and `holdings`; no gold part for that date gives `status: no_data` with a reason and the nearest earlier date the table holds when it can be read.
   - Opal principals only, as the tool is today: a firm principal is refused exactly as today (the gate), before any read.
4. **No typed key**: the lines you add type no S3 key or bucket (`c22.AC2` scans them).
5. **Tests**: a NEW file `infra/aws/ec2/opal-gateway/tests/test_positioning_extension.py` with at least 10 tests, using an injected getter (`PortalIndexIntegration(getter=...)` and `answer(...)`): the byte-equal answers (use the base module's answer for the same fixture where the existing tests do), case-insensitive ticker, an unknown ticker, the fund restriction, history found, history absent, a firm principal refused, a bad `as_of` shape refused, the signature, no S3 read for a refused call.

### Steps

0. The sparse command above. Then `cd infra/aws/ec2/opal-gateway && PYTHONPATH=. python -m pytest -q -p no:cacheprovider tests/test_portal_index.py tests/test_opal_discover.py tests/test_og_et2.py` passes before you start (a control).
1. Make the change and the tests. Run the same pytest line with `tests/test_positioning_extension.py` added (all pass).
2. Run the three criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. No catalog row, no registry file, no `DATA_CATALOG.yaml`, no other gateway file, no `catalog_entries/` file; no tool other than `etfs_get_positioning`, no grant, route, role, `.env` or AWS change. No deploy. No push.
2. The existing answer must not change by one byte for an existing input (`c22.AC1` compares the base tree `06cfb6db64` with yours on the same canned object).
3. No firm or product name is typed as a whole-string literal in code (the naming gate refuses a NEW hand-kept firm or product token): the four tickers are fund tickers, not firm names, but take them from the catalog row text or the object where you can, and otherwise from one tuple constant.
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
5. The checks are `deliverables/2.0.0_SA_COO~MI/round18/checks/c22.AC1.sh`, `c22.AC2.sh`, `c22.AC3.sh` (python `c22_equal.py`, `c22_check.py`). Read them for exactly what is graded. Do not edit them.
6. Another worker (`~45`) edits the emitter and the tool index at the same time (no shared file).
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/portal_index/integration.py
infra/aws/ec2/opal-gateway/tests/test_positioning_extension.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~46/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W46-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 1)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-22" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c22.AC1.sh; echo "exit=$?"</invocation><expect>DENOMINATOR cases 4 (internal empty, same day, other day, firm); every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-22" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c22.AC2.sh; echo "exit=$?"</invocation><expect>lines added to portal_index/integration.py with a typed S3 key or bucket literal: 0; new tests in test_positioning_extension.py at least 10 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-22" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/c22.AC3.sh; echo "exit=$?"</invocation><expect>pytest rc=0 on test_positioning_extension.py, test_portal_index.py, test_opal_discover.py and test_og_et2.py -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~46/NFRA_MCPINDEX.TO-MX-c-22.etfs-get-positioning-fund-ticker-and-as-of-history.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. (The expect fields are prose; the checker matches `expect` as a regex against your recorded output: encode the literal printed tokens and disclose that in a row. Pin each artifact row to the commit that carried it, not `PENDING-THIS-COMMIT`, when the file was committed before the instance.)
2. Do NOT flip the order's status; the issuer does.
3. Commit through `.tools/safe-commit.sh`, message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL, in two commits: (i) `integration.py` and the test file; (ii) the proof instance.
4. Report once, with: the change by function; the AC1 DENOMINATOR line and the CHECK lines verbatim; one fund_ticker answer (current) and one history answer, no more than 12 lines each (from your tests' fixtures); the test count; the two commit shas.

The issuer then merges and tells `2.0.0_SA_COO~O` the file and the commit so that its remainder release carries it.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 18, worker ~46, an independent chain. Source: CRO G5 spec (line "`etfs_get_positioning` (EXTEND: add as_of, fund_ticker)"; verdict keep and extend), COO~O msg 34536, CTO msg 34551 (MX-c-22: YES). The base dry-run: `c22.AC1` PASS base-against-base (the byte-equal control), `c22.AC2` FAIL (no fund_ticker, no test file), `c22.AC3` FAIL (no test file), as expected. Planted arms: `plant_c22.py` 6 of 6 (a good tree passes AC1 and AC2; an existing answer changed fails AC1; a typed S3 key, the arguments in the wrong order and nine tests each fail AC2). Risk WORLD by the infra path; the cell changes no grant: the gold prefixes are already in the internal reader policy (OG-ap-20).

<status>issued</status>
<round>18</round>
<workstream>ASSETS</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
