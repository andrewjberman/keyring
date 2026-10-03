# Never-widen sign-off packet -- st14 (row S279): the resident (st13 -> st14) and irpt-ycharts-generate, both at ONE commit `f89fc8e731`, so a fund ticker no longer fails the whole upload

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~21:5xZ.
**Authority:** CTO rulings batch 186 (msg 104394): "the st14 fix proceeds: tie YCharts' namespaced fund row to the
requested ticker, carry the provider id, and name the refusing check in the journal. Prove it offline first ... A bad
fund row must refuse THAT row by name, never the whole file." Fold-in batch 178 (Y-1 waits on it). Andrew-direct
2026-10-02 ~18:1xZ (YCharts approved for cases A, B, C, D and the typo file, one at a time, queue empty).
**Ledger:** `irpt-st14-20261002` (U1, U2 closed; D1, D2, V1 open). **Two moves:** D1 (one Lambda code update), D2 (one
resident install). No IAM, route, table, queue, schema or library move. **No vendor call in D1 or D2;** V1 is Y-1's first
lookup under the batch 186 terms.

## 1. What ships

**The code** (`de5e0c6878`, merged `f89fc8e731`; offline proof in its commit message):

| file | change |
|---|---|
| `intake/security_resolution.py` | `classify_batch`: a row `M:<S>` for a requested bare `S` is `S`'s. Verified (display id `S`, `security_id == id`, fields complete): FOUND, reason `EXACT_PROVIDER_FUND_MATCH`, the provider's row kept as the candidate. Unverified: `S` alone reads UNAVAILABLE / `PROVIDER_FUND_ROW_UNVERIFIED` with a closed `fund_row_cause`, never retried. A row no requested symbol owns still refuses the whole receipt, now with one closed cause. The resolver keeps `last_unverified` and `last_funds` |
| `intake/portfolio.py` | a FOUND fund match freezes the provider id (`M:TIMXX`) as the holdings row's `security_id` |
| `ycharts/generate/normalized_input.py` | the identity binding finds a fund row's check by its sole candidate's id |
| `ycharts/generate/resident_worker.py` | RETRY lines read `ROWS_UNVERIFIED_<CAUSE>`; a resolve that saw fund rows prints `IRPT_RESIDENT_RESOLVE_FUNDS matched= refused= causes=` (counts and closed tokens only) |

**Why both carriers:** the resident resolves and freezes the upload; the Lambda replays every frozen input through
`verify_frozen_portfolio` (`intake/uploads.py:450`, and `composition_admission.py:52` at submit). An old Lambda beside a
new resident would refuse every fund portfolio the resident froze (TEMPLATE_REPLAY_MISMATCH).

**Artifacts (U1, U2 closed):**
- `irpt-ycharts-generate.zip`: S3 version `y3LRNAoPvGmdWYZSNb5moyTiEDvo8055`, 582,443 bytes, sha256
  `wjSX3zZoFu2EUintXwZVESW+ac8F+bdRHSWm+YfpmgA=`, read back equal. 113 members; every staged row at `f89fc8e731`.
- Resident tar `irpt-resident-f89fc8e731-st14.tar.gz`: sha256 `4d317c00281a191a03c2f341c698c5843c8d9dc18ec0be50f44cb00d8edf6487`,
  777,996 bytes, S3 version `4N3RhbITXo1u1zIsLkPbc0oYYWNCUVYE`. Install script `resident_host_install_f89fc8e731-st14.sh`:
  sha256 `430d4172c02bd749d9615cc95c9e514c63ef6c35bf7092ca76d9afe9e99bf9a8`, S3 version `9GcYA4bLxx_gIvS_Vq4fYf0YX8mL.fVg`.
  Both keys read 404 before the upload and read back equal by version. Against st13's script, with root names
  normalized, it differs only in the tar pin, the `resident_worker.py` digest and the ledger slug; the library pin
  (`857d90b8..`) is unchanged.
- Gate (`ST14/GATE_OUTPUT_ST14_20261002.txt`): G1 249/249, G2 247/247 equal `git show f89fc8e731:<path>`, G3 100/100, G4
  agree, G5 against the running st13: added 5, removed 0, changed 18, identical 226.
- Cold-start smoke of the built zip on its three routes: PASS, no first-party module from outside the zip
  (`ST14/ZIP_COLD_START_SMOKE_ST14_20261002.txt`).
- The ycharts root's FULL plan (`ST14/plan_ycharts_full_st14.txt`): 1 to change, `module.irpt_ycharts_generate.aws_lambda_function.this`,
  `s3_object_version` `rtq1e9oT..` -> `y3LRNAoP..` and `source_code_hash` `E+FqSWwE..` -> `wjSX3zZo..`. Nothing else.

## 2. Every member changed since what runs now

**Censuses:**
- Resident vs running st13: 18 changed, 5 added, 0 removed, 226 identical.
- Generate zip vs live `E+FqSWwE..`: 13 changed, 1 added, 0 removed, 99 identical, 14 EOL-only.

**Reach:** read statically. The resident was traced from `reports/resident_installed.py` and
`ycharts/generate/resident_worker.py`; the Lambda from `generate_installed.lambda_handler`, `generate.tf:302`.

| member (where) | commits | the resident | the generate Lambda |
|---|---|---|---|
| `security_resolution.py`, `portfolio.py`, `normalized_input.py`, `resident_worker.py` (both) | `de5e0c6878` st14 (+ `951afdf4e6` st11 in `resident_worker.py`, Lambda only: the resident runs st11 since 07:18Z) | section 1 | section 1. `resident_worker.py` is packaged in the Lambda, but its loop is the resident's |
| `uploads.py`, `transport.py` (Lambda) | `951afdf4e6` st11, `9718ac5c87` st12 | already served (st11 07:18Z, st12 09:21Z) | the words of st11 and st12 ride, as their packets said: a busy resolve reads `RESOLVE_PROVIDER_BUSY` with action CORRECT; the transport write-back is reached only by vendor-calling paths, which run on the resident |
| `ops/owned_requests.py` (both), `ops/read_memo.py` (resident) | `4c23ef5d98` E6, `f27418381d` item 22, `c4210d2785` E7b, `f4be46173f` + `cee32dcf47` M2 | reached (`frozen_worker.py:37,99`, publisher), but the changes are only in `read()` and `history()`. The resident calls `_validate`, `_materialize` and `_final`, which are unchanged. `fresh_reads` is unchanged and inert on a plain Table | packaged, not on the served path (only the direct-invoke import check loads it) |
| `_authz/enforce.py` (both), `grant.py` (Lambda) | `7605bbf5ab` IB-pr-293, `23d839c618` IB-pr-291 | not reached (only importers are inside custody functions the resident never calls) | imported (`served.py:759`); new optional `load_report_owner`; the prospect branch runs only for a render bundle carrying `prospect_scope`. This Entry has no render ports, so there is no change for existing callers |
| `_authz/served.py` (both), `report_owner.py` (Lambda, ADDED) | `7605bbf5ab`, `2ad49400f8` IB-pr-295, `acce364286` IB-pr-296 | not reached | imported at load (`generate_installed.py:368-375`). The `client_id` allowlist applies to `analysis-request-history`, which this Entry does not declare. `render_ports_from_env` and the third render port are unused here. `report_owner.py` is staged so `served.py`'s import resolves (the hazard row S271 names for another function). Cold-start smoke PASS |
| `_contracts/AnalysisReport`, `ExportBundle`, `HoldingsSnapshot` and the docs copies (both) | `1dae563e21` IB-pr-294, `16a3fcfd6a`, `4cc72587d6` | no validator on a resident path loads them (the schema loaders read docs v1 and key by `$id`; ids there were already v1). `required` is unchanged for AnalysisReport; ExportBundle's one-of rule and HoldingsSnapshot's `multi_asset` are validated by nothing reached | registered as resources only. A digest of the packaged schemas stamps new accepted requests; only its presence is checked (`owned_requests.py:163`) |
| `ops/entry.py`, `owned_report.py`, `pdf_link.py`, `reports/status_installed.py`, `routes.json`, the two AnalysisRequestPdf schemas and two fixtures (resident; 5 ADDED) | irpt-status work: hop 11, E7b, M2 (served on irpt-status since 17:04Z) | packaged, never imported. `AnalysisRequestPdf.schema.json` joins `schemas/` with a unique `$id`, so startup is unaffected | not packaged |
| `reports/resident_bindings.json` (resident) | generated | the bindings carry the pinned digests | -- |
| `fixtures/har/report.pdf` (Lambda) | EOL only | -- | a 193-byte test fixture carried with CRLF line endings; no runtime module reads it |

**Not determined:** a dynamic import of `served` or `enforce` other than the two found.

## 3. Proofs

**Offline (no vendor call; the fund row's shape is the CRO capture `04_suggest_BREIT`, `M:BREIT.S` displayed `BREIT.S` --
no `M:` answer is recorded in the journal):**
- 16 new tests. classify: a match, an entitlement-gated fund (per-row), the provider's own id, five bad-fund shapes
  (each refuses only that row, with its cause), six stray rows (each still refuses the whole receipt, with its cause);
  the resolver's cause and counts; the resident end to end: AAPL+TIMXX resolves NORMALIZED with holdings
  `[AAPL, M:TIMXX]`, `prepare_normalized_upload` binds it, `step_upload` reconciles on YCharts' echo; a bad fund row is
  deleted from the queue unretried and the answer names row 3, column A.
- **Negative control:** the same tests on HEAD's four modules: 17 failed, 2 passed (the unchanged WAF and login classes).
- Suites: intake + generate + session 711 passed (HEAD 695; the same 1 POSIX-only failure and 13 collection-order errors on
  both). The generate offline suite equals HEAD's.

**V1, after D1 and D2 (Y-1, batch 186's terms):** queue 0/0 and no non-terminal job; `2.0.0_SA_COO~D` runs Case A from the
page with `yh-submit-case.mjs`; this seat joins it with `backend_join.py --journal`. PASS: the resolve journal prints
`IRPT_RESIDENT_RESOLVE_FUNDS matched=1` (TIMXX), the upload reads NORMALIZED with `M:TIMXX` among its holdings, on the FIRST
lookup with no WAF challenge. A first-read WAF challenge stops traffic and is reported (the outcome record, section 3). The
Overview then runs to READY under the same run.

## 4. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob.
2. **Before-read:** generate CodeSha256 `E+FqSWwE..`, the key's latest `y3LRNAoP..`; the resident's running root
   `c657a5966d-st13`, unit active; queue 0/0, no non-terminal job, the provider lease holder empty.
3. **D1:** a fresh targeted plan of `module.irpt_ycharts_generate.aws_lambda_function.this` showing only the code move;
   ONE `HALT_ACK=1 safe-apply`; CodeSha256 read back `wjSX3zZo..`. The cold-start smoke re-run against the live function's
   configuration.
4. **D2:** one `head-object` of the script key, printing `9GcYA4bL..`; `ST14/install_fetch_and_run.sh` through Systems
   Manager (fetch by key, sha256 checked on the host against `430d4172..`, run). Read back (its V1 lines): running root
   `f89fc8e731-st14`, the st14 member digests and `IRPT_RESIDENT_RESOLVE_FUNDS` present, the library unchanged, unit active,
   queue 0/0.
5. **V1** (section 3), then the ledger closes.

D1 and D2 land in the same window: between them, an upload with a fund ticker would still fail as today, and no new
behaviour is reachable (the old resident freezes no `M:` id).

## 5. Rollback, per key

- **D1:** re-promote S3 `rtq1e9oTWYgCvsz8F0wgjoeEOw7dcTZr` as the key's latest (`copy-object` of that version), then a
  targeted apply: CodeSha256 returns to `E+FqSWwE..`.
- **D2:** the root `c657a5966d-st13` stays on the host; the install script's rollback branch restores the unit's ExecStart
  and the receipt.
- A fund portfolio frozen under st14 stays readable only by st14 code: rolling back D1 alone would refuse it at replay.
  Roll back both, or neither.

## 6. Not claimed

- That YCharts answers a bare fund ticker with an `M:` row: inferred from the capture and the measured whole-batch refusal;
  V1 measures it. If the row's shape differs, st14 names the refusing check in the journal and the file still fails --
  per row for a fund row, whole-file only for a row no symbol owns.
- That YCharts' portfolio upload accepts `M:<ticker>` as an identifier: `step_upload` reconciles on the echo; V1's READY
  measures it.
- The WAF challenge's current state: the first spaced read measures it.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~21:5xZ, on this packet's bytes at the commit that carries it. The write set is one Lambda code update
and one resident root with its unit's ExecStart and cutover receipt. The blast radius is section 2. The rollback is
section 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
