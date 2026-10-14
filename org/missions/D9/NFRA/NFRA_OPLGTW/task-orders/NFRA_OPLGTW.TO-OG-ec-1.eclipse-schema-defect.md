# NFRA_OPLGTW task order -- `OG-ec-1` -- the Eclipse converter's reviewed schema edit: admit defaultTradingEngineId to portfolios_simple (row Z-S117), re-vendored, proven on the real bronze

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ec-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ec-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~86</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ec-1` (row Z-S117, workstream FWD22-W8, FWD-22 client data)

The reviewed edit to `mirror_schemas.py` that admits the vendor's new Eclipse column, the byte-identical re-vendored eclipse copy, and its tests; no apply, no deploy.

FWD-22's client data reads the vendor silver folders of `opal-data-assets` (Andrew-direct via CTO msg 34134); a converter defect that keeps a client table from landing is carried here (CTO msg 34152, PRD v3.5). THIS CELL is the
reviewed edit and its proof; the deploy and the re-drive are a later applier order. NO apply, NO deploy, NO invoke of any Lambda.

**The defect (row Z-S117, measured by `0.7.0_AE_CloudOps~Z`).** Since 2026-10-10 the vendor's Eclipse `portfolios_simple.json` carries one extra column, `defaultTradingEngineId`. The converter's drift check raises
`VendorDriftError("eclipse/portfolios_simple: vendor shape DRIFT -- extra=['defaultTradingEngineId'] missing=[] (declared 22 cols). A schema change is a reviewed edit to mirror_schemas.py; this boundary never absorbs one silently.")`
(`infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/mirror_conversion.py`, the `raise VendorDriftError(... "vendor shape DRIFT -- extra=" ...)` near line 202), and because the check fires during a run that converts the folder, EVERY Eclipse bronze object of the run
failed: 12 distinct keys (nine `model_composition_*.json`, `models.json`, `portfolios_full.json`, `portfolios_simple.json`). The drain emptied the DLQ, so nothing retries them; the bronze objects are in place.
The issuer measured the drift START independently: `eclipse/inflection/bronze/<date>/portfolios_simple.json` for 2026-10-08 and 10-09 carry no extra column; 10-10 through 10-14 each carry exactly `defaultTradingEngineId` (846 rows each).

**What to do (read first, then edit once, then prove).**
1. **Read before editing.** Read `infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/mirror_conversion.py` (the whole drift function and where the declared schema is read) and the `("eclipse", "portfolios_simple")` declaration in `data/assets/scripts/silver/mirror_schemas.py` (line 317; 22 declared columns).
   Read the REAL values of `defaultTradingEngineId` in `eclipse/inflection/bronze/2026-10-14/portfolios_simple.json` in bucket `opal-data-assets` (read only; print the distinct types and a count of nulls, never row content) and choose the declared type from them (`int64` if every non-null value is an integer; `string` if mixed; say which in a comment).
   The CTO also measured that the eclipse and orion vendored `mirror_schemas.py` copies differ from the source: the issuer measured the diff is 11 lines in each, all of them BD-only (`BD_TABLE_EXTENSIONS` and two BD column names), absent from the vendored eclipse and orion copies. Confirm that, and say so in your report; it is benign for Eclipse.
2. **The one edit.** In `data/assets/scripts/silver/mirror_schemas.py` add `'defaultTradingEngineId': "<the type>",` as the LAST column of the `("eclipse", "portfolios_simple")` declaration (the converter's column order is the declaration's order: append, never reorder). Change nothing else in that file.
3. **Re-vendor** the eclipse copy byte-identical to the source: `infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/mirror_schemas.py` (the repo's convention is a byte-identical copy of the source; `cmp` must report no difference). Do NOT touch the orion, blackdiamond or etf copies (Orion's drain was clean; no other family drifted).
   Check `infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/BUILD_MANIFEST.json`: if it records a hash of `mirror_schemas.py`, update that field through the repo's own build script or by recomputing exactly as the script does (read how it is produced; never type a hash by hand) and name the script or the rule in your report.
4. **Tests,** `infra/aws/lambda/opal-assets/tests/test_og_ec1.py` (read how the existing tests in `infra/aws/lambda/opal-assets/tests/` import the Lambda modules and copy that, never a new import trick):
   - `test_ogec1_ac01`: the source declaration of `("eclipse", "portfolios_simple")` now has 23 columns, the last is `defaultTradingEngineId`, and the first 22 are unchanged and in the same order.
   - `test_ogec1_ac02`: an offline fixture shaped like the vendor object with the extra column converts through the eclipse converter's drift check WITHOUT `VendorDriftError`, and the resulting schema carries the column with the declared type.
   - `test_ogec1_ac03`: the guard still guards: a fixture with a DIFFERENT unknown column, and one with a missing declared column, each STILL raise `VendorDriftError` for `eclipse/portfolios_simple`.
   - `test_ogec1_ac04`: `infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/mirror_schemas.py` is byte-equal to `data/assets/scripts/silver/mirror_schemas.py`, and the other three vendored copies are NOT edited by this cell (their bytes equal their bytes at the base of this branch).
5. **The live probe** is the issuer's AC2: against the real bronze objects of 2026-10-10 to 2026-10-14 the vendored eclipse schema declares every column the object carries (no extra, and no missing beyond the converter's own `_`-prefixed provenance columns). Run the same read yourself first.
6. Report once: the type chosen and its evidence, the BD-only diff confirmation, the BUILD_MANIFEST handling, and what the applier order must do (the Terraform path for the eclipse Lambda code, the ledger, and how the 12 bronze objects of 2026-10-10 onward are re-driven).

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer
  registers every tool and re-pins the counts at the merge, in one commit. Do not edit them; name the registration you
  expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address, or an object's
  text body into a report, a row or a log; write the catalog file (`app/refs/DATA_CATALOG.yaml` is NFRA_MCPINDEX's alone);
  override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
data/assets/scripts/silver/mirror_schemas.py
infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/mirror_schemas.py
infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/mirror_conversion.py
infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/BUILD_MANIFEST.json
infra/aws/lambda/opal-assets/tests/test_og_ec1.py
infra/aws/lambda/opal-assets/tests/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~86/`. Rows: id `NFRA_OPLGTW-Z-W86-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ec-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ec1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ec-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ec1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)eclipse portfolios_simple: bronze objects checked [3-5] \(2026-10-10\.\.2026-10-14\); extra columns 0; missing columns 0; vendored copy byte-equal to source yes; defaultTradingEngineId declared yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the schema declares the column last and unchanged otherwise, the converter's drift check passes the new shape and still refuses any other drift, and the vendored copy is byte-equal.
- `AC2`: against the real bronze portfolios_simple objects of 2026-10-10 to 2026-10-14 the vendored schema declares every column they carry.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ec-1.eclipse-schema-defect.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (row Z-S117; PRD v3.5 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- CTO ruling msg 34152 (PRD v3.5): a vendor-silver converter defect that keeps a FWD-22 client table from landing is a WORLD defect cell here. This cell is the reviewed edit; the Terraform deploy with a ledger and the re-drive are the applier order that follows its merge (OG-ec-2).
- The issuer registers the tools and re-pins counts at the merge (CUT BY WRITE SET: hookups belong to no cell).
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe absent).

<status>complete</status>
<round>37</round>
<workstream>FWD22-W8</workstream>
<slot>~86</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
