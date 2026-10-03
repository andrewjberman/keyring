# Never-widen sign-off packet -- Y-5 finding value: the resident (st18 -> st19) and irpt-ycharts-generate at ONE commit `a163441fb0`, so a ticker finding names the file's own symbol and the page can offer the proxy box

**For:** `1.0.0_SA_CTO` (CTO half; asked in msg 104773). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-03 ~21:5xZ.

**Authority:**
- Andrew ~20:3xZ, "all approved" (CTO 104738): the site-Z review does not cover `~Y`'s YCharts tests; Y-5 then Y-4 run.
- CTO 104634: Y-3 READY, then Y-5 V1, then Y-4 V1, one at a time and spaced. Y-3 is READY and closed.
- The defect, measured live by `2.0.0_SA_COO~D` (msg 104763): the Aproxy upload `UP-852105aa..` answered NEEDS_CORRECTION with
  `TICKER_DATA_NOT_ENTITLED`, row 100, actions `NAME_PROXY`, **value NULL**. The page keys the proxy box and the correction's
  `from_value` on the finding's value, so it drew nothing and nothing could be submitted.

**Ledger:** `irpt-y5v-20261003` (U1, U2 closed; D1, D2, V1 open). **Two moves** in one window, both or neither. No IAM, route,
table, queue or schema move. No vendor call in D1 or D2.

## 1. What ships

**The code:** `1545ec3442`, merged `a163441fb0`; the generate row re-pinned to it at `095968d363` (the whole-bundle rule).

`intake/portfolio.py`, in `freeze_template_portfolio`: the four ticker findings (`TICKER_NOT_FOUND`, `TICKER_DATA_NOT_ENTITLED`,
`TICKER_AMBIGUOUS`, `TICKER_CHECK_UNAVAILABLE`) pass `value` = the template row's own symbol. Nothing else in the function moves.

**Why both the Lambda and the resident:** the resident's resolve writes the NEEDS_CORRECTION row with its findings
(`uploads.py:385-453`, on the resolve_upload message). `uploads.py` is packaged in both components and has a second freeze call
site (`uploads.py:273`); which component reaches it was not traced, so both move. One commit, all or none, as Y-5 packet 1.

**Riding changes** (the whole-bundle rule moves every staged member from `828c37c6f7` / `a6f6e7165e` to `a163441fb0`). Each is
already served elsewhere or inert on these two components:

| member | commit | effect here |
|---|---|---|
| `ops/owned_requests.py`, `OwnedAnalysisRequest.schema.json` | W2-06 `7f1135f0ee` | served in irpt-status since 04:28Z; generate imports only `_storage_kwargs` (unchanged) |
| `ycharts/generate/resident_worker.py` | Y-4 enrichment `4ed0c7b816` | served on the resident since st18; the Lambda composes no resident path |
| `_authz/enforce.py`, `ExportReceipt.schema.json` | IB-pr-302 `8d08ee54e4` | adds a fourth RENDER_DELEGATE operation, `reporting_read`, and remaps path ids for that operation only; every existing operation's check is byte-for-byte the same path. Adds `bundle_id` to the delegate context (additive) |
| `ExportBundle.schema.json`, `export-download.response.schema.json` | IB-pr-301 `b66691eb1b` | export contracts; no generate or resident route reads them |
| `lib/opal_naming.py`, `reporting_policies.json` | X10 IRPT_DASHBD-S12 `b77e2af4d5` | adds families SERVED_SERIES and CLIENT_SUMMARY and an `object` field on SERVED_MANIFEST; the destination builder refuses an `object` family. SERVED_* are named only in `reporting/entry.py`, which is in neither bundle |

**Artifacts (U1, U2 closed):**
- **The generate zip:** version `YImF8vih8CBtZqEM7XksUccMJ63UayVz`, 591,597 bytes, sha256
  `jKsI7pZWzjaTub83yRvk1tass0oiVZkp9jmvr1v9ezQ=`. Built in a `core.autocrlf=false` worktree at `095968d363`: 114 members, 0
  differ from the pin, 0 CRLF. Census vs live `fD2R6OFr..` (`Y5V/census_irpt-ycharts-generate_y5v.json`): identical 105,
  changed 9 (the fix and the eight riders above), added 0, removed 0. Cold-start smoke PASS on its three routes.
- **The resident tar:** `irpt-resident-a163441fb0-st19.tar.gz`, sha256 `1c5bfc1001961188413a200dda45ac7171a347ad4c47475e8aa4a844cb24c517`,
  791,835 bytes, version `IJG0WnOfzvavTqPiurIYncWYL1ISXEfr`.
- **The install script:** `resident_host_install_a163441fb0-st19.sh`, sha256
  `f940529db4853dd76d1cc8fd581b18f05bffb829675c1cf0eef27b47ffbdd261`, version `BHSM0RkX_qwSdbWs163_N4jbBgSuFoY9`. Both keys read
  404 before the upload.
- **The gate:** G1-G5 PASS (`Y5V/GATE_OUTPUT_Y5V_RESIDENT_20261003.txt`). G5 vs the running st18: changed 6 (`intake/portfolio.py`,
  `_authz/enforce.py`, two `ExportReceipt` schema copies, the export-download response schema, the generated bindings), added 0,
  removed 0. The capture library and wrapper hashes equal st18's.

## 2. Writers of the changed field

ONE constructor writes a finding's `value`: `template_reader.finding` (`str(value)[:160]`, else null). Its call sites that set
it, all read: `template_reader` (HOLDING_LIMIT x2, WEIGHTS_LOOK_LIKE_PERCENT, WEIGHTS_DO_NOT_SUM_TO_ONE,
WEIGHT_RESIDUAL_NORMALIZED; unchanged); `portfolio` CORRECTION_UNMATCHED (unchanged); and the three ticker `emit` calls in
`portfolio.freeze_template_portfolio` (the change; four codes). The CSV lane's `freeze_parsed_portfolio` sets no finding value
(unchanged). `upload_suggestions` adds `suggestion` only.

## 3. Reader census of the changed field

- **Backend:** no reader of a finding's `value` (search over `infra/aws/lambda/investor-reporting/**/*.py`: only the two new test
  assertions). The resident's replay (`verify_frozen_portfolio`, `portfolio.py:295-308`) replays NORMALIZED documents only, and a
  NORMALIZED document holds no ticker finding (each one is an ERROR and keeps the upload NEEDS_CORRECTION): unchanged.
- **The page** (`portal/src/pages/InvestorReporting/tabs/analysis/prospect.ts:48-58`, `ProspectComposer.tsx:283, 406`): a
  finding is offered a proxy box only when its actions include NAME_PROXY, its code is TICKER_DATA_NOT_ENTITLED or
  TICKER_NOT_FOUND, and its value is a ticker. After the move:
  - TICKER_DATA_NOT_ENTITLED: the box appears (the Y-5 design);
  - TICKER_NOT_FOUND: the box appears (NAME_PROXY was already in its actions); with a verified suggestion the accept is
    offered as before, and the accept can now name `from_value`;
  - TICKER_AMBIGUOUS, TICKER_CHECK_UNAVAILABLE: the value is set, no box (their actions are REPLACE_FILE);
  - the findings list's words are unchanged (they use description, code and row).
- **Stored rows:** new NORMALIZATION# rows carry the value; rows already written are not rewritten.

## 4. Blast radius

| path | after |
|---|---|
| an upload with no ticker finding | unchanged |
| an upload with a ticker finding | the finding gains `value` = the file's symbol; state, code, row, column, actions, words unchanged |
| a NORMALIZED upload, a submission, a generation | unchanged (no ticker finding exists there) |
| a correction re-post | unchanged validation (`template_corrections`); the page can now fill `from_value` |
| export routes | not served by these two components; the riders are additive |

## 5. Rollback, per key

- **irpt-ycharts-generate:** re-promote S3 version `w2yfeweDcOFLnVFLFidK1_VCv5EFPCmb` (sha256 `fD2R6OFr..`, the live code;
  `Pglv_ED9BeWk3nd6H1SFi84b9BYWxJmU` holds the same bytes) with ONE targeted plan and safe-apply; CodeSha256 read back.
- **The resident:** the unit back to `/opt/irpt-resident/a6f6e7165e-st18`, which the install script keeps on the host; unit
  active and queue 0/0 read back.
- All or none: a failed D2 rolls D1 back in the same window.

## 6. Proofs

**Offline:** `test_y5_proxy_corrections` asserts `value == "TIMXX"`; `test_y4_check_gate` builds the accept from the finding
alone (`from_value = item["value"] == "APPL"`). Negative control: on HEAD's `portfolio.py` both fail (`None == 'TIMXX'`); with the
fix 32 passed. Suites: intake 272 passed 1 skipped; ycharts/generate 396 passed 30 skipped.

**V1 (YCharts, under the solo gate):** `2.0.0_SA_COO~D`'s Aproxy from the page, Cottonwood chosen.
- Row 100 reads TICKER_DATA_NOT_ENTITLED with its words and **value TIMXX**; the page draws the proxy box.
- The user names SGOV; the re-post resolves NORMALIZED with SGOV and the correction disclosed.
- The Overview reaches READY.

## 7. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. **Before-read, STOP on any difference:** generate CodeSha256 `fD2R6OFr..`; root `a6f6e7165e-st18`, unit active; queue 0/0, no
   non-terminal job, the provider lease not held.
3. **D1:** a fresh targeted plan of `module.irpt_ycharts_generate.aws_lambda_function.this` (code only, 1 to change); ONE
   `HALT_ACK=1 safe-apply`; CodeSha256 read back `jKsI7pZW..`; the cold-start smoke live.
4. **D2:** `head-object` of the script key printing `BHSM0RkX..`; `Y5V/install_fetch_and_run.sh` over Systems Manager (sha256
   checked against `f940529d..`). Read back: root `a163441fb0-st19`, the portfolio digest, unit active, queue 0/0.
5. V1, then the ledger closes.
