# Never-widen sign-off packet -- Y-5 packet 1: the resident (st15 -> st16) and irpt-ycharts-generate at ONE commit `34088050e0`, so a user-named proxy continues an upload and a gated fund row is named plainly

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-03 ~01:5xZ.

**Authority:**
- CTO rulings batch 178, ruling 5: "WIRE BOTH ... the swap gate ... accepts a user-named proxy ticker that YCharts
  verifies, so Case D's stated proxy (SGOV) is reachable whatever the gate suggests".
- Batch 192: Case A's READY moves to Y-5.
- Andrew-direct 2026-10-03 ~00:4xZ, card 3 (msg 104485): "we're not mutual fund data buying". The Y-5 proxy is the
  standing path for gated funds. Make the page's message for a gated row plain to the user.
- Batch 196: build from a `core.autocrlf=false` checkout and compare members byte for byte (S286).

**Ledger:** `irpt-y5-20261003` (U1, U2 closed; D1, D2, V1 open). **Two moves** in one window, both or neither. No IAM,
route, table, queue or schema move beyond the additive request field. No vendor call in D1 or D2. **V1 needs the YCharts
session**, which is EVICTED (S288): it runs after Andrew's attended sign-in (option A).

## 1. What ships

**The code:** `a42ad6b675`, merged `34088050e0`. Design: `Y45/Y45_DESIGN_CHECK_AND_SWAP_GATES_20261002.md` and its
addendum.

| file | change |
|---|---|
| `intake/portfolio.py` | `template_corrections` validates `{finding_code, from_value, to_value}`. `freeze_template_portfolio(corrections=)` replaces a row's symbol for the check, the price and the holdings, and never touches the template. `disclosures.corrections` lists each correction with `approved_by` = the owner, in the PRD AnalysisRequest shape. `document.options` carries the corrections, so the replay reproduces them. A correction for a ticker no row holds -> `CORRECTION_UNMATCHED`. A gated row -> `TICKER_DATA_NOT_ENTITLED`, actions `[NAME_PROXY]`. `TICKER_NOT_FOUND` gains `NAME_PROXY` |
| `intake/uploads.py` | `corrections` is accepted on the template lane only, and added to the options ONLY when sent: every pre-Y-5 revision hash is unchanged. The resolver reads the replacement symbols. The locked words copy gains the two proxy codes, which keep their own actions |
| `ops/status.py` | the plain words for `TICKER_DATA_NOT_ENTITLED` and `TICKER_NOT_FOUND`. It is packaged in the resident; irpt-status is not moved by this packet |
| `docs/contracts/.../AnalysisUploadRequest.schema.json` | optional `corrections` on the template lane; the legacy CSV branch refuses it. Additive |

**Artifacts (U1, U2 closed):**
- **The generate zip:** version `oew.wOPKuZQKvi30OCFECa5x7Dk_9MOL`, 586,808 bytes, sha256
  `aug0YyWcP6wwRwwnkyWYH+GBfT8gN9irrmEMCz/Vvj8=`, read back equal.
  - It was built from an LF checkout: 113 members, **0 differ from `git show 34088050e0`, 0 carry CRLF** (S286 remedied).
  - Census vs live `VZvhvWRM..`: identical 109; EOL-only 14 (live's CRLF copies become LF); changed 4 (the contract,
    `portfolio.py`, `uploads.py`, the `report.pdf` fixture's EOL).
  - Cold-start smoke PASS on its three routes.
- **The resident tar:** `irpt-resident-34088050e0-st16.tar.gz`, sha256
  `4d2315197e80173b1c7b706205b5f4b27bad680523fd8fa0e4fdaede29c44075`, 784,084 bytes, S3 version
  `eB6EYhL7W5R9SWNmwtOnDZnkFhL1kcCA`.
- **The install script:** sha256 `ee864bf3e9d72a5c50b02febca52346922f2c5157c4bbf482085a7768b768542`, S3 version
  `cBX09ViGMXenXFxtK8Cd6goAVXjFEZeo`. Both keys read 404 before the upload.
- **The gate:** G1-G5 PASS, G2 247/247 at the pin; G5 vs the running st15: changed 5 (the four files + the bindings),
  added 0, removed 0.
- **The full ycharts plan:** 1 change, the generate code (`VZvhvWRM..` -> `aug0YyWc..`).

## 2. Blast radius

| caller | before | after |
|---|---|---|
| an upload with no `corrections` | as today | the same options, so the same revision hash. A not-found row's finding gains words and `NAME_PROXY`. A gated fund row reads `TICKER_DATA_NOT_ENTITLED` (was `TICKER_CHECK_UNAVAILABLE`) with words |
| a re-post with `corrections` | refused `UPLOAD_FIELDS` | the next normalization revision. The replacements are read by the same securities_info check. NORMALIZED only if every row (corrected or not) verifies. Revision r is never rewritten |
| a CSV-lane upload with `corrections` | refused | refused (`UPLOAD_FIELDS`); the contract's CSV branch also refuses it |
| a frozen input from before Y-5 | replays | replays (no `corrections` in its options) |
| the page today | -- | it sends no `corrections` until `2.0.0_SA_COO~D` wires the field (interface sent 01:32Z); its findings gain a `description` |

## 3. Proofs

**Offline:** `ycharts/generate/tests/test_y5_proxy_corrections.py`, 16 tests. Negative control: on HEAD's sources 15 of
16 fail. Suites: the same 12 pre-existing failures as HEAD, 1006 passed. The generate offline suite equals HEAD's except
the CRLF fixture.

**V1, after option A (one job at a time under the solo gate, spaced):** Case A from the page.
- The easy file's row 100 (TIMXX) reads `TICKER_DATA_NOT_ENTITLED` with the words.
- The user names SGOV.
- The re-post resolves NORMALIZED with SGOV in the holdings and the correction disclosed.
- The Overview reaches READY.

Y-3's READY (ULT + IWM) runs first after the sign-in (CTO 104482).

## 4. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. **Before-read:**
   - generate `VZvhvWRM..`, the key's latest `oew.wOPK..`;
   - root `9bbb38f7a0-st15`;
   - queue 0/0, no non-terminal job, the lease holder empty.
3. **D1:** a fresh targeted plan (code only); ONE `HALT_ACK=1 safe-apply`; CodeSha256 read back `aug0YyWc..`; the cold-start
   smoke live.
4. **D2:** `head-object` of the script key printing `cBX09ViG..`; `Y5/install_fetch_and_run.sh` over Systems Manager
   (sha256 checked against `ee864bf3..`). Read back: root `34088050e0-st16`, the st16 digests, unit active, queue 0/0.
5. V1 after option A, then the ledger closes.

## 5. Rollback

- **D1:** re-promote S3 `jFLj0wX5E0cybH52ZTxSVdVApAoNIypy` as the key's latest, then a targeted apply. The code returns to
  `VZvhvWRM..` (Y-3).
- **D2:** root `9bbb38f7a0-st15` stays on the host; the install script's rollback branch restores it.
- A corrected input replays only on st16 code. Roll back both or neither.

## 6. Not claimed

- The page half: `2.0.0_SA_COO~D` wires the proxy field and shows the words.
- The check gate (Kimi typo suggestions) and Kimi swap suggestions are Y-4 and packet 2.
- Live proof: V1 waits on the session.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-03 ~01:5xZ, on this packet's bytes at the commit that carries it. The write set is one Lambda code update
and one resident root with its unit's ExecStart and cutover receipt. The blast radius is section 2. The rollback is
section 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
