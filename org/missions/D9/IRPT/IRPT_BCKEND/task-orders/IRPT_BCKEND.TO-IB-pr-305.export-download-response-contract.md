# TO IRPT_BCKEND.TO-IB-pr-305 -- the export-download RESPONSE contract follows the server: a response-only download_route with the signed url and expires_at, plus top-level sha256 and byte_length (CTO batch 211; nothing served)

<to_id>IRPT_BCKEND.TO-IB-pr-305</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~108</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 211 (@827e6c8bed, msg 104557), on row IRPT_BCKEND-W101-S13.
The ruling calls it "one contract commit with its test, cut now as hygiene, never held for a round". GATE (x) puts this in ROUND 40
(row S267). | **Decomp cell:** `IB-pr-305` (decomposition section 32) | **outcome_ref:** E4 (the export download the page reads) |
**depends_on:** none

---

## WORKER FACE

**The measurement (batch 211).**
- The served `export/entry.py:282-288` returns a `download_route` that carries `route`, `requires_reauthorization`, `url` and
  `expires_at`. It also returns `sha256` and `byte_length` beside it (`export/download.py:176`: a SigV4 link valid at most 300 s).
- `docs/contracts/investor-reporting/v1/responses/export-download.response.schema.json` is `additionalProperties: false` WITHOUT
  those fields. So the server's own answer violates its published contract, and a strict parser drops four fields.

**The ruling.** The contract follows the server, and the signed link lives ONLY in the response.
1. The response schema defines its OWN response-only `download_route`. Its properties are `route`, `requires_reauthorization`,
   `url` and `expires_at`:
   - `url` is required and https only: a `pattern` starting `^https://`;
   - `expires_at` is required and a UTC `Z` date-time: `format: date-time`, and/or a pattern ending `Z$`.
2. `sha256` (`pattern` `^[0-9a-f]{64}$`) and `byte_length` (`type: integer`, `minimum: 0`) are declared exactly where the server
   sends them. Read `entry.py` and `download.py` for the level.
3. **`ExportReceipt.schema.json` (both copies) stays EXACTLY as it is.** The receipt is the durable record, and a 300 s signed link
   never belongs in it.
4. Bump the response contract's revision marker (follow the file's own versioning fields).
5. Add `infra/aws/lambda/investor-reporting/export/tests/test_download_response_contract.py`, at least 2 tests, naming
   `export-download.response.schema.json` and `download_route`:
   - the live handler's download answer (driven through the handler with stubs, as `test_download_signed_answer.py` does)
     validates against the revised schema;
   - an answer missing `url` or carrying a non-https url is rejected.
   - If no JSON-schema validator is importable, validate with the one the contracts suite already uses; read
     `infra/aws/lambda/investor-reporting/_contracts/tests/`.

<criterion id="IB40-1-AC1" cell_refs="IB-pr-305"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r40/p40_download_response_contract.py" . IB40-1-AC1</invocation><expect>IB40-1-AC1 PASS</expect></criterion>
`IB40-1-AC1` -- the schema declares the response-only `download_route` (url https and required, expires_at a date-time and
required) and the integrity facts. Both ExportReceipt copies are byte-unchanged. Base: FAIL.

<criterion id="IB40-1-AC2" cell_refs="IB-pr-305"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r40/p40_download_response_contract.py" . IB40-1-AC2</invocation><expect>IB40-1-AC2 PASS</expect></criterion>
`IB40-1-AC2` -- the contract tests pass (at least 2), and the export suite passes at least 190 (188 at the base), 0 failed. Base:
FAIL (no file).

<expected_criteria>IB40-1-AC1,IB40-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. No server change: do not edit `entry.py` or `download.py`.
- **AWS:** none.
- **Refusal clause.** Any edit to `ExportReceipt.schema.json`, or to the server's code, is a defect: stop and file a row. No client
  name in any record.
- **ISSUER RULING (2026-10-03 ~07:0xZ, on row W108-S1, ARMED).**
  - `_contracts/tests/test_seam_paired.py`'s positive control for `export-download` builds the response's `data` as a slice of
    the ExportReceipt valid fixture. That slice can never carry the response-only `download_route` url and expires_at, or
    `sha256` and `byte_length`, which batch 211 requires and forbids in the receipt. So the control turns red by design, not as a
    regression.
  - The file is GRANTED for that one control: give `export-download` a response-shaped valid document by supplementing the
    receipt slice with the response-only fields (a well-formed https url, a Z date-time, 64-hex sha256, a non-negative
    byte_length).
  - The negative control must still fire. No other operation's control may move.
  - The `_contracts` suite must read 0 failed. W108-S1 is disarmed by this ruling.

<paths>
docs/contracts/investor-reporting/v1/responses/export-download.response.schema.json
infra/aws/lambda/investor-reporting/export/tests/test_download_response_contract.py
infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~108/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/`, `docs/contracts/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 32 (round 40, workstream ~P), cell `IB-pr-305`.
<owned_cells>IB-pr-305</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB40-1-AC1, IB40-1-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~108/IRPT_BCKEND.TO-IB-pr-305.export-download-response-contract.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB40-1-AC1,IB40-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the download_route definition;
- where sha256 and byte_length sit;
- the revision marker;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one published response contract (docs/contracts/.../export-download.response.schema.json) and one new test; 0 served bytes move; no server change and no deploy (batch 211: additive).
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- the route and its handler are unchanged; only its published response shape catches up.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB40-1-AC1 base FAIL (no response-only download_route), IB40-1-AC2 base FAIL (no file), dry-run at the base 2026-10-03 ~06:3xZ.
lane: the <paths> block IS the grant.
</preflight>
