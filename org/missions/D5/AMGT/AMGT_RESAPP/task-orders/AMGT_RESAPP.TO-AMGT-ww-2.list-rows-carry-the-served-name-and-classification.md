# AMGT_RESAPP task order -- `AMGT-ww-2` -- LIST ROWS CARRY THE SERVED COMPANY NAME AND CLASSIFICATION, JOINED SERVER-SIDE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ww-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~171</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for this cell's own acts (local read-only DynamoDB GetItem in the checks). The Lambda's read of `etf-classifications` is a grant the redeploy (ww-1) adds under its never-widen pair; this cell's report names the exact action(s) its code calls.
comp-adversary: RUN by the issuer at the cut -- AC1 compares the payload to the table row field by field, reads a ticker the table does not hold, and reads every live trending/chatter ranking row; AC2 is the API and print suites (the bound).
EGRESS CLASS, declared: NONE beyond read-only DynamoDB GetItem/BatchGetItem on Opal's own `etf-classifications`. No vendor, no write.
</preflight>

## 1. THE CELL -- `AMGT-ww-2` (round 48, decomposition s.56)

The lead-panel ranking rows (`scoped_amgt.read_rankings(kind, window, ...)`, route `GET /api/scoped/amgt/lead-panel/rankings/<kind>/<window>`)
carry `ticker` as `"BA US"` and no company name. The canonical classification table is DynamoDB `etf-classifications` (region
us-east-1), key `ticker` = the BARE ticker (`"BA US"` -> `"BA"`; `"WALMEX* MM"` -> `"WALMEX*"`; the first space-separated token),
attributes as the table holds them: `name`, `asset_class`, `sub_asset_class` (the GICS sector for a single security), `sector`
(unset on security rows), `management_style`, `last_updated`, `updated_by`.

**Build** `scoped_amgt._classification_for_ticker(ticker) -> dict`:
- the table holds the bare ticker -> `{"status": "SERVED", "name": <name or None>, "classification": {"asset_class", "sub_asset_class",
  "sector"}, "name_state": "SERVED" if name else "ABSENT", "reason": None if name else "<the table holds no name for this ticker>"}`
  -- every value copied as the table holds it (a missing attribute is `None`; nothing guessed, re-cased or filled from the ticker);
- the table does not hold it -> `{"status": "ABSENT", "name": None, "classification": None, "name_state": "ABSENT", "reason": "<not
  held by etf-classifications>"}`;
- a failed read (an exception) -> `{"status": "READ_FAILED", "name": None, "classification": None, "name_state": "READ_FAILED",
  "reason": "<the error class and message>"}` -- distinguishable from ABSENT, never an empty object.
Each row of `read_rankings`' `rows` then carries `name`, `classification` and `name_state` from it (one read per DISTINCT ticker per
call; `BatchGetItem` or cached `GetItem`, your choice). Nothing else in the row changes. Add tests (a stubbed table) pinning each
branch: SERVED with a name, SERVED with no name, ABSENT, READ_FAILED, and the row join.

## 2. BOUNDS

1. **The adapter only.** No page file, no export file, no Terraform, no table write, no change to how a row is ranked or counted.
2. No S3 write, no deploy, no server. Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
3. Python from the repo root with `PYTHONPATH="$(pwd)"`.
4. Your report names the DynamoDB action(s) your code calls, so the redeploy grants exactly those on `etf-classifications`.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/*.py
lib/research/api/tests/**
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~171/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; DynamoDB `etf-classifications`; the S3 inputs `read_rankings` already reads.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ww-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/ww-2.AC1.py; echo "exit=$?"</invocation><expect>ranking rows read: N (N &gt; 0) and LIST ROWS CARRY THE SERVED NAME AND CLASSIFICATION: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ww-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/api-suite.sh; echo "exit=$?"</invocation><expect>pytest reports N passed and 0 failed (308 passed at the cut, plus your new tests) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the built behaviour against the real table and the live rankings; AC2 the bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~171/AMGT_RESAPP.TO-AMGT-ww-2.list-rows-carry-the-served-name-and-classification.proof_of_spec.json`. Report once: what you changed and where, the DynamoDB action(s) the code calls, how many live ranking rows read name_state SERVED, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-47 analysis s.4 row 2 (@657b9283a2). Base: AC1 FAIL ("scoped_amgt has no _classification_for_ticker"),
AC2 PASS (308 passed). SERVED: reaches the Lambda at ww-1 with the DynamoDB read grant. Slot ~171 continues with ww-4 (same file).
Names for 59 library tickers stay ABSENT until a clean source exists (row Z-S300).

<status>pending</status>
**ISSUER CLOSE (`2.0.0_SA_COO~Z`, 2026-09-29 ~12:2xZ):** drained @7ea218afad (worker 1a2ea2c06e). The issuer re-ran both criteria on
the merged FULL tree: AC1 PASS (ranking rows read 2, YES, exit=0); AC2 PASS (315 passed, exit=0). The worker's AC2 FAIL was an
instrument absence the issuer caused -- the sparse cone lacked `infra/logic`, `infra/aws/terraform/harvest` and
`portal/.../__harness__` (rows Z-W171-S1, -S2; no code defect; the 28 non-passes all FileNotFoundError outside the cone). The code
calls `dynamodb:GetItem` only; ww-1 grants exactly that on `etf-classifications`. SERVED: reaches the Lambda at ww-1.
<status>complete</status>
<round>48</round>
<slot>~171</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
