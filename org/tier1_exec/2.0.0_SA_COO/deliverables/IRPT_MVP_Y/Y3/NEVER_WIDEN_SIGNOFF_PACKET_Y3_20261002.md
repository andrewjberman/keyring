# Never-widen sign-off packet -- Y-3 + S284's journal: the resident (st14 -> st15) and irpt-ycharts-generate at ONE commit `9bbb38f7a0`, so a named ETF is a comparison key

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-03 ~00:0xZ.

**Authority:**
- CTO rulings batch 178, ruling 4: "`~Y` admits an ETF the classification table holds as a comparison key, through the same
  identity check as an uploaded symbol".
- Batch 189: the three exact-file grants; no PRD half re-opens.
- Batch 192: "Order: Y-3's packet next"; the `gated=` count measures S284.
- Andrew-direct ~18:1xZ: YCharts for cases A-D and the typo file, one at a time, queue empty. Andrew-direct 2026-09-27:
  analysis attempts.

**Ledger:** `irpt-y3-20261002` (U1, U2 closed; D1, D2, V1 open). **Two moves**, in one window, roll back both or neither.
No IAM, route, table, queue or schema moves. No vendor call in D1 or D2.

## 1. What ships

**The code:**
- `bb255c4cb2` (Y-3), merged `ce035e9387`; design `Y3/Y3_DESIGN_ETF_COMPARISON_KEY_20261002.md`.
- `5f93fdbee0` (S284 journal), merged `9bbb38f7a0`.

| file | change |
|---|---|
| `_scope/maintained_sources.py` | a key that is no model but a ticker the `etf-classifications` table NAMES is admitted as a `MAINTAINED_RECORD` at `dynamodb:etf-classifications` (vendor_id = the ticker, type etf, evidence the row's sha). An unnamed or absent ticker stays refused; a failed table read refuses; no reader admits models only |
| `reports/request_composition.py` | a comparison source is a maintained model, or a `MAINTAINED_RECORD` at exactly the classification table, typed etf |
| `reports/generate_installed.py`, `ycharts/generate/prospect_submission.py` | the catalogue route's own `read_classifications` port reaches the submission |
| `ycharts/generate/recipe.py` `step_comparison_identity`, `resident_worker.py` | before `holdings_upload`, ONE securities_info read of the classified tickers. Each must be an exact provider match typed etf, with no feature needed, or the job ends `VENDOR_COMPARISON_IDENTITY_REFUSED`. A job with no classified comparison sends nothing |
| `intake/security_resolution.py`, `resident_worker.py` (S284) | a verified fund row the account is not entitled to counts `gated=` (never `matched=`), and its feature token is named: `IRPT_RESIDENT_RESOLVE_FUNDS matched= gated= features= refused= causes=` |

**Artifacts (U1, U2 closed):**
- **The generate zip:** version `jFLj0wX5E0cybH52ZTxSVdVApAoNIypy`, 584,914 bytes, sha256
  `VZvhvWRMqD6mdaF8COT5JcUcnMxdvzCJe82Gs/9cnRk=`, read back equal. Cold-start smoke PASS on its three routes.
- **The resident tar:** `irpt-resident-9bbb38f7a0-st15.tar.gz`, sha256
  `af49e7029825a227911a5817e5d0556d9e21f7a7cad34ac2f67aa6f771ee3b56`, 782,217 bytes, S3 version `Cs1gMHYpJVcbzk2X3fP7cDdree7b5y89`.
- **The install script:** sha256 `1a282fd48118713e7e4ee174f2b89e06c856e00217ffa528893a92a072c34483`, S3 version
  `ELQvAnfndlcYl6Z.I4o1JnBHGq3iuKFC`. Both keys read 404 before the upload.
- **The gate:** G1 249/249, G2 247/247 at the pin, G3 100/100, G4 agree; G5 vs the running st14: changed 10, added 0,
  removed 0.
- **The full ycharts plan** (`Y3/plan_ycharts_full_y3.txt`): 1 change, the generate code (`wjSX3zZo..` -> `VZvhvWRM..`).

## 2. Every member changed since what runs now (st14 on both)

| member | commits | the resident | the generate Lambda |
|---|---|---|---|
| the six Y-3 files + `security_resolution.py` | section 1 | section 1: the identity step runs only for a classified comparison; the admission runs in the Lambda | section 1: admission and composition at submit. `recipe.py` and `resident_worker.py` are packaged but are the resident's loop |
| `_contracts/HoldingsSnapshot.schema.json` + docs copy | `9e58503be1`, `41ffd770d6`, `be81c7da2c` (~M/~P, the TARGET fold) | no validator on a resident path loads it (the st14 packet's section 2, the same schema family) | registered as a resource only |
| `reports/resident_bindings.json` | generated | the pinned digests | -- |
| `fixtures/har/report.pdf` (Lambda) | EOL only | -- | a test fixture with CRLF line endings |

## 3. Proofs

**Offline** (`ycharts/generate/tests/test_y3_etf_comparison.py`, 22 tests; the S284 tests in `test_security_resolution.py` and
`test_resolve_upload.py`):
- the admission beside a model, five refusal shapes and a failed read;
- composition admits only the classification location typed etf;
- the identity step's pass, six not-ok shapes, and the no-pin refusal;
- the resident: an Overview sends no identity read and reaches READY; a refused identity ends ATTENTION before any upload;
- a gated fund row reads `gated=1 features=<token>=1`, never `matched`.

Negative control: 19 of 22 fail on HEAD's modules. Suites: 875 passed vs HEAD 853, with the same 11 pre-existing
failures. The generate offline suite equals HEAD's.

**V1, after D1 and D2, one job at a time under the solo gate, at least 10 minutes apart:**
- **V1-a (Case C's shape on a fund-free file).** The scripted runner uploads the 12.03 file (AAPL, VNQ) and submits a
  Multi-Comp, `comparison_keys = [opal_ultra_long_term, IWM]`. PASS:
  - the submission admits IWM (accepted, no refusal);
  - the resident's identity read verifies 1 of 1 on the first read, with no WAF challenge;
  - the job reaches READY;
  - the request read names both comparisons.
  It is also ULT's first live run.
- **V1-b (S284 measured).** One upload-only run of AAPL+TIMXX (K4 only, no submission). PASS = the resolve line reads
  `gated=1 features=<token>`, or `matched=1` (then TIMXX normalizes and S284's inference is wrong). Either result is
  recorded.
- A first-read WAF challenge stops traffic and is reported.

## 4. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. **Before-read:**
   - generate `wjSX3zZo..`, the key's latest `jFLj0wX5..`;
   - root `f89fc8e731-st14`;
   - queue 0/0, no non-terminal job, the lease holder empty.
3. **D1:** a fresh targeted plan of `module.irpt_ycharts_generate.aws_lambda_function.this` (code only); ONE `HALT_ACK=1
   safe-apply`; CodeSha256 read back `VZvhvWRM..`; the cold-start smoke against the live configuration.
4. **D2:** `head-object` of the script key printing `ELQvAnfn..`; `Y3/install_fetch_and_run.sh` over Systems Manager (fetch
   by key, sha256 checked against `1a282fd4..`). Read back: root `9bbb38f7a0-st15`, the st15 digests, unit active, queue
   0/0.
5. V1, then the ledger closes.

## 5. Rollback

- **D1:** re-promote S3 `y3LRNAoPvGmdWYZSNb5moyTiEDvo8055` as the key's latest, then a targeted apply. The code returns to
  `wjSX3zZo..` (st14).
- **D2:** root `f89fc8e731-st14` stays on the host; the install script's rollback branch restores it.
- An accepted request naming an ETF comparison replays only on st15 code (the composition check). Roll back both or neither.

## 6. Not claimed

- That ULT runs to READY on the vendor: V1-a is its first live run.
- That every named classification row is an ETF YCharts prices for this account: each job's identity read decides.
- S284's cause: V1-b measures it.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-03 ~00:0xZ, on this packet's bytes at the commit that carries it. The write set is one Lambda code update
and one resident root with its unit's ExecStart and cutover receipt. The blast radius is section 2. The rollback is
section 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
