# IRPT_BCKEND round 76, workstream ~Y -- L8 COMPILE (drain-end task-order packet; release 6 part 1, the custody factory installed)

**By** `2.0.0_SA_COO~Y2` (issuer, dell2) **for** `3.0.0_SA_CVO`, 2026-10-09. Risk WORLD (served code and IAM declarations). Nothing
deployed.

## The order

**1 of 1** order is terminal: `IRPT_BCKEND.TO-IB-yr-761` (worker `0.9.0_WK_IRPT_BCKEND~223`), status complete, proof VALID. Drained
@2ae4d86e00. `round-close-check.py --round 76`: orders=3, all complete; proofs 3/3 ok; verdict=MAY-CLOSE.

**What it did:**
- `reports/generate_installed.py` now routes a submission with no `input_id` to `build_accepted_custody_entry(AcceptedCustodyReader(...))`.
  It no longer raises `CUSTODY_FACTORY_REQUIRED`. An `input_id` submission still reaches the prospect factory.
- It staged the 4 modules the path needs.
- It attached the AWSSDKPandas layer (row `IRPT_BCKEND-D2-S19`).
- It declared the `generate_custody_factory` policy in `ycharts/generate.tf`.

| criterion | worker | issuer re-run at the drained base |
|---|---|---|
| Y76-1-AC1 statement -> custody factory; `input_id` -> prospect | 6 passed | 6 passed |
| Y76-1-AC2 no staged commit ships split | `split=0` | `rows=88 commits_checked=33 split=0`, PASS |
| Y76-1-AC3 symbol closure of the built zip | `missing=0` | `modules=66 pairs=296 missing=0 optional_fallbacks=2`, PASS |

Census at the base: `changed_members=11` (release 5b's 6 plus this round's members).

## AMENDMENT 1 (issuer ruling, on the worker branch @b9cc978f94)

- **Row `D2-W223-S1`:** ~M2's `holdings_publication_port.py` keeps a guarded fallback, `except ImportError: from publication import ...`.
  The fallback names a module the package deliberately does not stage. The symbol closure now treats an ImportFrom inside an
  `except ImportError`/`ModuleNotFoundError` handler as optional, but only when every primary import in that try resolves in the
  package. An unguarded import, or a failed primary import, is still graded. Both negative controls still FAIL.
- **Row `D2-W223-S2`:** `opal-data-assets` is SSE-S3 (AES256), so no KMS statement is needed. The grant is unchanged.
- **Row `D2-W223-S3`:** the stale `CUSTODY_FACTORY_REQUIRED` assertion in the sibling `test_generate_installed.py` path is admitted to
  the cell. That suite now passes: 13 passed.
- **Row `D2-W223-S4`** records that the amendment holds.

## Next

- **Release 6 pair** (a fresh never-widen pair, after this drain). It carries:
  - the census (11 members) and the three gates at the pin;
  - the read grants printed beside the statement: exactly ~M2's read set, plus ~P2's silver read and `custody_reports` (CTO/CVO
    conditions, msg 2162);
  - the AWSSDKPandas layer;
  - the service principal for IRPT_CUSTDY E2a's scoped POST;
  - the after-read: a statement submission no longer raises `CUSTODY_FACTORY_REQUIRED`.
- **Release 5b** (`TO-APPLY-Y75`) is still at the applier queue.
