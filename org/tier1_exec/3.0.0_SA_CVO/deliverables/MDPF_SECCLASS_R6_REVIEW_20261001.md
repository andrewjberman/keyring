# MDPF_SECCLASS -- round 6: L8 compile and L9 review, with the FAST interval (`3.0.0_SA_CVO`)

**Packet:** `2.0.0_SA_COO~M` 103405, `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/2.0.0_SA_COO~M/DRAIN_END_R6_20260930.md`
@2744a9fc57: SC-e13, SC-e14, SC-e15, all `complete` at HEAD, `<risk>WORLD`, proofs VALID by the issuer's re-run.
**Outside this compile:** SC-e12 (`parked`, `0.7.0_AE_CloudOps`). **Watermark:** 2026-09-30T23:45Z. **Carriers:**
`ADJUDICATION_v4.md` (C-S11), `REMEDIATION_v4.md` (10 rows, 3 closed), and S4 closed IN PLACE in `REMEDIATION_v3.md`
by its clocks alone. Co-committed. This compile was read 05:45Z after the 03:09Z reboot (the packet sat unread from
23:45Z); everything below was read 06:2xZ to 06:4xZ at CLOUD HEAD.

## L9

No order carries a JUDGMENT criterion (0 in 3 files). The packet asks for three deviations to be judged:

| deviation | reading | judgment |
|---|---|---|
| 1. SC-e14 amendment 1: the two contract assertions became a version floor and a superset check | `test_classified_by_v2.py:57-70` asserts `version >= (0, 2, 0)` and that the original four values are a subset; the contract reads 0.3.0 | **A weakening, as the packet says.** A regression of the contract to 0.2.0, or the loss of the fifth value, passes both tests. Graduated on row W11-S1; remedy is the exact pin (STATUS next-list item 6) |
| 2. SC-e15 amendment 1: AC1 expects the census line; the tolerance bar moves to the MODEL_ROWS act | the half, line 201: "The MODEL_ROWS act is REFUSED unless a fresh census immediately before it prints `MODEL-READER-TOLERATED`" | **Accepted as a relocation, not a lowering.** The order's criterion now proves the census ran; the bar still gates the only act it protects. It holds only while that half stays unsigned until a TOLERATED print exists, which is its state today |
| 3. SC-e13 amendment 1's ordering ("Leg 0 first") | the act as run: the three `_shared` keys 06:11:37Z to 06:11:46Z, document version 5 at 06:14:59Z, next silver fire 22:10Z | **The amendment's order was wrong and the act did not follow it.** Sources first, then the document, in one gap. Row W10-S5 closed on that reading |

## What this seat read live or at HEAD

| read | result | bears on |
|---|---|---|
| `aws ssm describe-document opal-bd-asset-dim-download` | DefaultVersion 5, LatestVersion 5, Hash `d3a38c7b...d3f407`, equal to `git show HEAD:` of the document; `$LATEST` content names `_shared` on 5 lines | W10-S1 closed |
| `s3api head-object`, three keys under `opal-data-bd` `code/gold/lib/_shared/` | all present, 06:11:37Z to 06:11:46Z; ETag of the client `181e1902667beb928a9ea993bd17d349`; absent-key control 404 | W10-S1, W10-S5 |
| `comp-pipescript deployed --firm bd` | C_06, D_03, D_04, `build_bd_assets_dim.py` MATCH; 41 MATCH, 0 STALE, 0 MISSING; overall NOT-DECIDABLE (1 head-object deferred) | S5 (bytes on the prefix) |
| `r6_deployed_layout_import.py` | DEPLOYED-LAYOUT-IMPORT modules=5 of 5 files=8; silver files_staged=10 | S5 |
| `r6_model_reader_census.py` | readers=34 tolerates=23 read_only=8 crashes=3 refuses=0 fails_contract=0; `UNCENSUSED .../reports/generate_installed.py` | W12-S1 closed; W12-S2, W12-S3 open |
| `R7_CHECKS/test_seed_model_correction.py` | 4 passed | W12-S1, and the FAST pin 9053ffba73 |
| `gold_dispatch.sh` | 0 lines with an E_ id; control 57 lines with a C_ id | W10-S2 |
| `.tools/test_safe_deploy.py` | 7 failed, 7 passed | W10-S3 |
| `test_seed_etf_constituents.py` | 1 failed, 7 passed | W11-S2 |
| the two `v2_portal` test directories, one process | 1 failed, 93 passed | W11-S1 (the four condition-string tests pass) |
| `label-legacy-classified-by.py:89`, `set-instrument-kind.py:96` | `attribute_exists(ticker) AND attribute_not_exists(<attr>)` | S4 closed in place |

Not read by this seat: the BD gold runner (ledger leg X is open), any served BD page, the live bytes of the
`bd-asset-dim-trigger` Lambda, the MODEL-CENSUS (it calls the vendor).

## Rows: 11 undispositioned, all compiled

| row | disposition | basis |
|---|---|---|
| W10-S4 | dismissed (C-S11) | a record of W10-S1's repo disarm; superseded by the live document |
| W10-S1 (BLOCKING, ARMED) | CLOSED: DISARMED + REMEDIATED | document version 5 live with the HEAD hash; the three keys exist |
| W10-S5 (ARMED) | CLOSED: DISARMED + REMEDIATED | sources before document, one gap, by this seat's timestamps |
| W12-S1 (BLOCKING, ARMED) | CLOSED: DISARMED + REMEDIATED | 9053ffba73; 4 passed; census fails_contract 1 -> 0 |
| S5 (BLOCKING) | graduated, OPEN, `2.0.0_SA_COO~M` | bytes deployed; the runner import is ledger leg X |
| W12-S2 (BLOCKING) | graduated, OPEN, `2.0.0_SA_COO~M` | 3 crashes reproduced; blocks MODEL_ROWS through the half |
| W12-S3 | graduated, OPEN, `2.0.0_SA_COO~M` | the stated bound is now met: one UNCENSUSED file and one new reader |
| W10-S2 | graduated, OPEN, `2.0.0_SA_COO~M` | E_18 has no trigger; an open ledger's acceptance cannot fire |
| W11-S1 | graduated, OPEN, `2.0.0_SA_COO~M` | deviation 1 |
| W11-S2 | graduated, OPEN, `2.0.0_SA_COO~M` | a red guard on the constituents seeder |
| W10-S3 | graduated, OPEN, `1.0.0_SA_CTO` (placement) | the deploy tool's test file is half red |
| S4 (v3) | CLOSED in place: REMEDIATED | both conditions carry the clause at HEAD |
| W6-S2, S2, W5-S2 | carried, not restated | not re-read |

No BLOCKING or ARMED row is undispositioned. Two BLOCKING rows stay OPEN with an owner: S5 (until leg X) and W12-S2
(it holds the MODEL_ROWS act, not the BD thread).

## The FAST interval (from 2026-10-01T05:39Z, lease `MDPF_SECCLASS`, CTO DECISION 103498 (a))

| pin | claim | read | grade |
|---|---|---|---|
| `9053ffba73` (W12-S1 fix) | a seed correction of a model row drops the two model-only fields | 4 passed; census fails_contract=0 | PASS on a test run; no table row is written by the fix |
| BD_THREAD_R3, legs S1 and L0 (ledger `secclass-bd-thread-r3-m-20261001`, both halves @8769ffe8d5) | six files and three shared modules on the code prefix, then the document | four scripts MATCH; three keys present with the signed ETag on the client; document version 5 with the HEAD hash; order sources-then-document | PASS on deployed bytes for the two legs. **NOT_EVALUATED for the thread:** legs X (runner import), A1 (23:00Z gold fire), A2 (22:10Z silver fire) and B4 (the page) are open |

## What you should have asked but did not

- **Q1. Five triggers read their SSM document at `$LATEST`, so a "restore the default version" rollback is void on all
  five.** `infra/aws/lambda/bd-pipeline/`: `bd-asset-dim-trigger`, `bd-allocation-trigger`, `bd-transactions-trigger`
  (line 58 each), `bd-realized-trigger`, `bd-unrealized-trigger` (line 63 each) pass `DocumentVersion='$LATEST'`
  (5 hits over `infra/aws/lambda/**/*.py`). Row W10-S5 found one, and cites ledger
  `nfra-mcpindex-bd-asset-dim-rest-schedule` leg L2 as already recording such a rollback for it (not re-read here). Any future half that moves one
  of the other four documents needs the same two-part rollback, or the triggers pin a version. For `1.0.0_SA_CTO`.
- **Q2. The new Analysis comparison catalogue reads this table, and MODEL_ROWS would change what it lists.**
  `2.0.0_SA_COO~Y`'s catalogue (IRPT_BCKEND `efde229443`) lists every ticker row that carries a `name`: 317 of 2,309
  today (this seat's scan). MODEL_ROWS writes 260 rows, 130 of them flagged low-confidence. If those rows carry a
  name they enter a list an adviser picks comparisons from, with no sign of `classified_by = model` or the flag. The
  half's reader table predates this reader. It should name the catalogue's behaviour before it is signed; this is
  the concrete case of rounds 4-5's Q2 (who reads the flag on a model row).
- **Q3. The census rewrites a tracked record on every run.** `r6_model_reader_census.py` rewrites
  `MDPF_SECCLASS_M/R6_MODEL_READER_CENSUS_20260930.json`, which reads modified in the shared tree since before this
  session. A record dated 09-30 that changes whenever anyone runs the check is not a record. Write to a dated or
  scratch path, or print only.
- **Q4. An open ledger cannot close as written.** `secclass-e18-iam-and-deploy-m-20260930` waits on E_18's first
  scheduled run, which no schedule produces (W10-S2). Until the trigger exists that entry ages toward RED for a
  reason no one can clear.

-- 3.0.0_SA_CVO

## CORRECTION, 2026-10-01 ~07:1xZ -- row W12-S2's evidence was stale when this compile was committed

This seat's census run that read `crashes=3` was made before 06:26Z. `2.0.0_SA_COO~M`'s fix a96e00c279 (the client
and its two copies sum any class the table holds) merged to CLOUD at 06:30:25Z (0b7b794514), before this compile's
commit. The row's evidence line and the table above therefore describe the tree before that merge, and the slug
(103556) repeated "3 crashes". Re-read at CLOUD 453c6430ec:

- `r6_model_reader_census.py`: `MODEL-READER-CENSUS readers=34 tolerates=26 read_only=8 crashes=0 refuses=0
  fails_contract=0`; `UNCENSUSED infra/aws/lambda/investor-reporting/reports/generate_installed.py` still prints, so
  TOLERATED is still not printed.
- The three source copies are identical (md5 `4cc11d3e7448...`).
- The deployed shared client on the BD code prefix is still the pre-fix bytes: ETag
  `181e1902667beb928a9ea993bd17d349`, the BD_THREAD_R3 signed candidate. The two positioning Lambda bundles were not
  read.

What stands: W12-S2 stays OPEN in `REMEDIATION_v4.md` (the gate admits only clock moves in place, so the evidence
text is corrected here, not there). Its state is now "fixed in source, not deployed": the remedy's remaining part is
the deploy of the three copies, which is a served act with its own half. W12-S3 is unchanged (one UNCENSUSED file).
The mistake was this seat's: a read taken at one HEAD was written into a row committed at a later one without a
re-read.

-- 3.0.0_SA_CVO

## Grade, 02:xZ 2026-10-02 -- MDPF_SECCLASS BD thread r3 legs A2, A1 and item 4

| claim | this seat's read | grade |
|---|---|---|
| A2: the 22:10Z silver fire ran document v5 and `silver/bd_assets_dim.parquet` advanced | SSM command `0da1ded9` at `$LATEST` (default 5, latest 5, hash `d3a38c7b..3f407`), requested 22:11:06Z on `i-0e6f6dc014fdcf1cd`, Success 1 of 1. The key advanced at 22:11:40Z (979,746 bytes; prior 2026-09-30 22:11:33Z); rows 12,148 to 12,176, the same 22 columns | PASS |
| A1: at the 23:00Z gold fire C_06, D_03 and D_04 exit 0 and the served keys advance | `gold_incremental_2026-10-02_20261002_010256.log` from 23:00:45Z: `C_06 done (rc=0)`, `D_03 done (rc=0)`, `D_04 done (rc=0)`, `PARALLEL CHAIN COMPLETE`, `COMPLETE (exit code: 0)` at 01:02:56Z. Of the half's five named keys 3 advanced (`firm_composition` 00:13Z, `platinum/clients/z08327149/summary` 00:35Z, `platinum/firm/mix_summary` 00:33Z); 2 did not (`mix_daily_summary`, `client_timeseries/z08327149`, last version 2026-10-01 05:1xZ) | PASS as worded. **Limit:** C_06 read `To process: 0 ... No new partitions` (watermark 2026-09-29): it imported the shared client and computed nothing. Its first compute under the new client is the 2026-10-02 04:00Z fire, and its two keys advance only then |
| item 4 (ledger `secclass-e18-trigger-dispatcher-m-20261001`, leg A): PHASE_B3b runs E_18 rc 0, 0 CALGUARD lines, the chain exits 0 with B4 onward | `E_18 done (rc=0)`, `PHASE_B3b complete (7s)`; 0 CALGUARD lines; PHASE_B4 to D5 complete; written/refused `0 / 0` with 1 candidate unresolved; a table scan finds `updated_by = e18-scheduled` on 0 of 2,690 rows | PASS as worded. Vacuous on the write branch: 0 rows written, so CTO addition (3) (the first branch-B row against the fallback's class) is NOT_EVALUATED |
| CTO `e5b4a67464`: SPYI, PSLV, FPNIX absent after the 23:00Z fire, stop (b) stands | E_18 wrote 0 rows, which agrees. Now all three are PRESENT (consistent get-item): SPYI structured / Options Income, PSLV commodities, FPNIX fixed_income, each `classified_by seed`, `updated_by seed-script`, `last_updated` 02:12:11Z: `2.0.0_SA_COO~M`'s seed act (ledger `secclass-cot-seed-rows-m-20261001`), not the detector. Control WMT. Served BD silver of 22:11Z predates the seed (SPYI equity/bd, PSLV alternatives/etf_classifier_fallback, FPNIX fixed_income/bd) | PASS: the detector did not take them first |
| ledger state | `deploy_ledger.py list` in the shared tree (this seat, 02:5xZ), 20 of 20 sentinels: `secclass-bd-thread-r3-m-20261001` OPEN, age 20.7h, window 20.0h, PAST-WINDOW, stranded A1 and B4; `secclass-e18-trigger-dispatcher-m-20261001` OPEN, in window, stranded A. Nothing is half-landed: code and document are deployed and verified; what remains is reads | Owed by `2.0.0_SA_COO~M`: close A1 and E18 leg A on this log; B4 (the page read) remains |

**Two runner findings from the same log**, filed as rows (not grades): the runner prints `WARN: comp-freshness not
found in PATH -- freshness gate skipped.` on every start read (2 of 2 in the prior log's tail, 1 of 1 in the 23:00Z
run); and three starts on 2026-10-01 (09:47Z, 12:45Z, 21:47Z) end in silver prep with no COMPLETE line before the next
start re-executes.

**Limits.** The log tail was read, not the whole object. B4 (the page) is not read. The seed rows reach served BD
silver at the 2026-10-02 22:10Z fire at the earliest; not read.

-- 3.0.0_SA_CVO

## ~M Cottonwood 19 seed rows (merge `96e945c649`), read 03:xZ-04:xZ 2026-10-02

Ledger `secclass-cot-seed-rows-m-20261001` (`3eac28eae3` open, `485c7f37dd` legs M, W, R closed); CTO half `e5b4a67464`.

| claim | this seat's read | grade |
|---|---|---|
| 19 rows written as signed | consistent batch-get on etf-classifications: 19 of 19 present, all `classified_by seed`, `updated_by seed-script`, `last_updated` 2026-10-02T02:12:11Z; 112 of 112 field values equal the seed source at HEAD (asset_class, management_style, sub_asset_class, sector, name, instrument_kind) | PASS |
| the four choices | MEAR, EVSM, VMLUX Short Duration with sector Municipal; FPNIX Short Duration, EIBIX High Yield; PSLV commodities, SPYI structured; BRK.A and BRK.B `single_security` equity | PASS |
| no other row touched | full consistent scan: 2,719 rows; 48 carry `last_updated` from 2026-10-01T20Z on: these 19, and 29 `CUSIP:` rows written 03:40Z by `mdpf-secclass-cusip-rows` (a separate act, graded below); 0 others | PASS |
| tests | `R7_CHECKS/test_seed_cot_top_tickers.py`: 22 passed | PASS on a test run |

**Limits.** Legs S (the 2026-10-02 14:15Z publication) and G (gold fire) are not read; the served Holdings move
(15,497,641.12 USD) is not read.

-- 3.0.0_SA_CVO

## ~M Cottonwood 29 bank-CD `CUSIP:` rows (deploy `afa9d2d4bb`), read 04:1xZ 2026-10-02

Halves: COO `ffe6235c2a`, CTO `9cbda02990` (batch 108, blob `56a1db3d3e`). The CTO half lists as not verified by it:
the writer's 10 tests, the generated set file, the dry runs, the reader census. This grade reads the first two and the
write itself.

| claim | this seat's read | grade |
|---|---|---|
| the stops at CLOUD: writer `6dfcd7fc75`, set `85f1bff9a4` | `git hash-object` on `R7_CHECKS/write_cusip_rows.py` and `COT_CUSIP_ROWS_WRITE_SET_20261002.txt` in the shared tree: equal, both clean | PASS |
| the writer's tests | `R7_CHECKS/test_write_cusip_rows.py`: 10 passed | PASS on a test run |
| 29 rows written as the set states | the set: 29 rows, 29 distinct CUSIPs. Consistent batch-get of `CUSIP:<cusip>`: 29 of 29 present; 29 of 29 equal the set on asset_class (fixed_income), empty sub class and name, with `classified_by scheduled`, `updated_by mdpf-secclass-cusip-rows`, `identifier_namespace CUSIP`; `last_updated` 2026-10-02T03:40 on 29 of 29 | PASS |
| they follow the peer | `CUSIP:66476QFV5`: fixed_income, namespace CUSIP, classified_by scheduled; differs only in `updated_by` (`mdpf-secclass-scheduled`), which CTO half item 1 accepts | PASS |
| no existing row touched | full consistent COUNT scan: 2,719 rows, equal to the close's 2,690 + 29. The second-wave scan above found 0 rows outside the seed and CUSIP acts written since 2026-10-01T20Z | PASS |

**Limits.** No served move is claimed and none is read: the 3,005,499.29 USD of bank CDs reads fixed_income only after
the Cottonwood re-point ships (leg R held). The comparison-catalogue skip of the CUSIP namespace is the CTO's read, not
repeated. The dry runs and the reader census are not re-run.

-- 3.0.0_SA_CVO

## Grade, 08:3xZ 2026-10-02 -- V1 of the BD r3 rollback: the one restore run (CTO RULINGS batches 117-118, row MDPF_SECCLASS-S9)

Rollback `a741b8e3d1` (code to the pre-r3 versions), watermark reset, restore run fired 06:25Z (`25f11c3975`). V1 is
batch 117 item 3(c), read on this run's output. Fallback deadline 11:00Z.

| claim | this seat's read | grade |
|---|---|---|
| the run completes on the old code | `logs/gold-layer/gold_incremental_2026-10-02_20261002_083113.log` (583,473,043 bytes), last 12 MB: RUNNER STARTED 06:26:07Z; C_06 `To process: 1`, `C_06 done (rc=0)`; `D_03 done (rc=0)`; `D_04 done (rc=0)`; `COMPLETE (exit code: 0)` 08:31:13Z; 0 `Classification not found` lines (the r3 run: 11,878); 0 Traceback, IndexError or BLOCKED lines | PASS |
| `platinum/firm/mix_summary.json` sums to 100 percent, composition about 1,843 M | version 08:02:29Z, data_as_of 2026-09-30: equity 1,416,599,516.32 (0.7686), fixed_income 387,678,776.24 (0.2103), alternatives 38,836,010.23 (0.0211); shares sum 1.0000; market values sum 1,843,114,302.78, equal to the composition total 1,843,114,302.78. The r3 version (05:37Z) summed 0.758 and 1,397,402,073.27 | PASS |
| client z08327149 carries VXX again | `platinum/clients/z08327149/summary.json` 08:04Z: mix equity 0.8845, fixed_income 0.0997, alternatives 0.0157 (sum 0.9999). The r3 versions at 05:39Z and 00:35Z read `other: 0.0` and no alternatives class. The VXX lots in `detail/tax/open_lots` are present in all three versions (11 nodes); what returns is VXX's class in the client's mix | PASS |

**Found in passing (for row S9).** The r3 code's 23:00Z fire, which computed no C_06 partition, still served part of
the regression: z08327149's summary of 00:35Z already had no alternatives class. The served window was about 00:35Z to
08:04Z for that client, and 05:37Z to 08:02Z for the firm mix.

**Limits.** The advisor, account and other client families were not read one by one; the gold views
`firm_composition.json` and `mix_daily_summary.json` were rewritten at 07:41Z and were not compared value by value.

-- 3.0.0_SA_CVO

## ~M 36 CUSIP rows for the BD re-land residual, read 12:xZ 2026-10-02

Halves: COO `d022796535` (12:14Z), CTO `757ae975ee` (12:17Z, batch 162). Write 12:18:51Z. Ledger
`secclass-bd-residual-cusip-rows-m-20261002`: leg W CLOSED, leg R OPEN.

| claim | this seat's read | grade |
|---|---|---|
| packet blob `2a4428eb24`, set blob `2e47dd1663` | `git hash-object` on the working tree equals HEAD and `d022796535` for both; 0 dirty | PASS |
| the writer is the one signed in batch 108 | `R7_CHECKS/write_cusip_rows.py` = `6dfcd7fc75` in the tree, at HEAD and at `d022796535` (the 29-row grade's blob) | PASS |
| the writer's tests | `R7_CHECKS/test_write_cusip_rows.py` 10 passed; the builder `build_residual_cusip_set.py` has no tests and was not run (it rewrites the tracked set) | PASS on a test run |
| 36 rows written as the set states | the set: 36 rows, 36 distinct CUSIPs; consistent batch-get: 36 of 36 present, 0 unprocessed; 36 of 36 equal the set on asset_class, sub class, name, `classified_by scheduled`, `updated_by mdpf-secclass-cusip-rows`, `identifier_namespace CUSIP`; `last_updated` 12:18:51.945705Z on 36 of 36 | PASS |
| the class follows the peer | 30 WRITE_PEER rows: the peer's live row equals the written class and sub class on 30 of 30; the 6 `structured / Hedge` rows match the ruled pair | PASS |
| table 2,841 | consistent COUNT scan: 2,841 (2,805 + 36) | PASS |
| no row outside this act changed in its window | full consistent scan of 2,841 rows: rows dated 12:00-12:40Z 36, all in the set; since 11:00Z 52 (these 36 and 16 `seed-script` rows at 11:21:06Z, a separate act); 0 after 12:18:52Z | PASS |
| one name is ASCII | `CUSIP:025083882` carries U+00AE (registered mark), the only non-ASCII name among 2,841 rows | FAIL on the record: row MDPF_SECCLASS-S15 |
| the BD r3 re-land's condition (CTO half `a1deb42063`, packet blob `f926b46157`) | legs M, G, W, R and S run only after portal `eb90f2ad` is on PROD; `merge-base --is-ancestor eb90f2ad origin/PROD` rc 1 (on DEV rc 0); positive control `b3a1d8a6` on PROD rc 0 | condition NOT MET now |

**Limits.** No served move is claimed or read (leg R held). The per-name kind readings, the five same-security
identities, the dry runs and the 68-name census were not re-run. The halves label their signing "12:3xZ" and "~12:4xZ";
their commits are 12:14Z and 12:17Z, both before the 12:18:51Z write; this seat goes by the commits.

-- 3.0.0_SA_CVO

## Grade, 00:5xZ 2026-10-03 -- BD r3 re-land (r4) served, read against row S9's measure

Half `NEVER_WIDEN_HALF_REQUEST_BD_THREAD_R3_RELAND_20261002.md` (leg R acceptance at :75); ledger
`secclass-bd-thread-r4-reland-m-20261002`, leg R closed green by `2.0.0_SA_COO~M` (821bb7b891).

| claim | this seat's read | grade |
|---|---|---|
| the firm mix lists every class and sums to 100 pct (S9's measure) | `platinum/firm/mix_summary.json` 2026-10-02 16:14Z (as of 2026-09-30) and its 00:37Z rewrite: 8 classes (alternatives, cash, commodities, equity, fixed_income, other, structured, unclassified); shares sum 1.0000; market values 1,843,114,311.70 = the composition total, within 8.92 of the restored 08:02Z figure (1,843,114,302.78). No class dropped, nothing missing | PASS |
| unclassified at or under 5.0 pct (leg R) | 76,259,973.86 = 4.14 pct (the half predicted 4.63 pct, 86,480,584.86) | PASS |
| the move matches the signed blast radius | equity 73.77 pct (restore 76.86), fixed_income 20.40 (21.03), structured 1.43 (half 1.22), alternatives 0.09 (half 0.01; restore 2.11), commodities 0.08 (half 0.07), cash 0.11, other 0.00. The gap to the half's figures is plausibly the 36 CUSIP rows written at 12:18Z (12.05 M), after the half was signed (not attributed row by row) | PASS within the half; difference inferred |
| client z08327149 carries VXX under structured / Hedge (leg R) | not re-read here | NOT_EVALUATED |

**Row S9's clock.** The regression S9 recorded (classes absent from the mix, 24 pct of the firm missing) does not recur on
the re-land: unclassified is carried as its own class, as the CTO's batch 117-118 condition required.

-- 3.0.0_SA_CVO

## Grade, 01:2xZ 2026-10-03 -- the 2026-10-02 23:00Z BD gold fire on r4 (seed rows' leg G, partly)

| claim | this seat's read | grade |
|---|---|---|
| the fire completes on the r4 code | `logs/gold-layer/gold_incremental_2026-10-03_20261003_010843.log` (590,267,203 B), last 12 MB: RUNNER STARTED 23:00:46Z; E_18, C_06, D_03, D_04 rc 0; `COMPLETE (exit code: 0)` 01:08:43Z; 0 Traceback/IndexError/BLOCKED | PASS |
| the firm mix stays whole | `Mix snapshot (C_06): 8 classes, date=2026-09-30, total_mv=$1,843,114,215`; C_06 `To process: 0` (no new partition: the 04:00Z fire is the next compute) | PASS |
| the seeded tickers resolve (leg G) | `Classification not found` lines: 33,463, over 145 distinct tickers (the S9 run: 290 distinct); 0 of 9 seeded tickers among them (SPYI, PSLV, FPNIX, MEAR, EVSM, VMLUX, EIBIX, BRK.A, BRK.B); IYR and ITB still not found, now counted under unclassified | PASS on the classifier read; the lots' served classes NOT_EVALUATED |

Under r4 a not-found ticker is carried as `unclassified` (the mix lists it), so the 33,463 lines are expected and are the
residual the half names, not S9's loss.

-- 3.0.0_SA_CVO

## BD gold 2026-10-02 23:00Z fire, the second scheduled run on the r4 re-land code (read 04:4xZ 2026-10-03)

Trigger `bd-gold-nightly-fallback` `cron(0 23 ? * MON-SAT *)` ENABLED. Log
`s3://opal-data-bd/logs/gold-layer/gold_incremental_2026-10-03_20261003_010843.log` (590,267,203 B, cumulative; this
run's section read from the last `RUNNER STARTED`, 23:00:46Z to 01:08:43Z).

| check | this seat's read | result |
|---|---|---|
| run | `=== COMPLETE (exit code: 0) ===` 01:08:43Z; validation `PASS=0 WARN=0 FAIL=0 SKIP=1 ERROR=0` (00:13:46Z) | PASS |
| C_06 computed | PHASE_C5 `C_06 done (rc=0)`, 16.5 s, checkpoint `gold/.checkpoints/2026-10-02/C_06.done`; 3,197 of 3,197 client C_06 timeseries read by the publisher | PASS |
| firm mix served | `platinum/firm/mix_summary.json` version `wma_kZ0XFi..` written 00:37:50Z, `data_as_of` 2026-09-30 | -- |
| every class listed | 8 keys (equity, fixed_income, alternatives, commodities, structured, cash, unclassified, other), 7 nonzero, `other` 0 | PASS |
| sums to 1.0 | pct sum 1.000000; MV sum $1,843,114,311.70 = composition `total_market_value` | PASS |
| nothing dropped | identical to the r4 re-land served at 16:14:37Z (version `0Pwq0AY3..`): same MV to the cent, same 8 classes, unclassified 4.1376% (bar 5%); the S9 regression version (05:37:54Z, pct sum 0.758174) is not repeated | PASS |
| row S9's measure on a scheduled run | the scheduled recompute on r4 code reproduces the re-land exactly | PASS |

**Noted, not a row.** The run's classification stage and its C_06 line print a total of $1,843,114,215, which is
$96.70 below the served mix (5.2e-8 of the total). It is a stage-level figure, and the served file sums to its own
total.

**Not yet read.** The Saturday run launched at 04:00:25Z (instance running at 04:50Z); its log is expected around
06:05Z and carries the next `data_as_of`.

-- 3.0.0_SA_CVO

## BD gold 2026-10-03 04:00Z run (Saturday; the first r4-code run at data_as_of 2026-10-01), read 06:0xZ-06:4xZ

Log `gold_incremental_2026-10-03_20261003_060352.log` (section 04:00:41Z to 06:03:52Z).

| check | this seat's read | result |
|---|---|---|
| run | exit 0; validation `PASS=0 WARN=0 FAIL=0 SKIP=1 ERROR=0`; C_06 rc 0; 3,193 of 3,193 client timeseries read | PASS |
| every class listed | mix version `HvABa_JI45..` (05:35:25Z), `data_as_of` 2026-10-01: 8 keys, 7 nonzero | PASS |
| sums to 1.0 | pct 1.000000; MV $1,764,886,987.32 = composition total; unclassified 4.0566% | PASS |
| nothing dropped | total down $78,227,324.38 (4.24%) from 09-30; 335 OPEN accounts ($78,634,159.20 on 09-30) absent from the 10-01 positions cube with no transaction, zeroed in their served AUA by `synthetic_correction` (sum -$78,504,236.80) | FAIL: row MDPF_SECCLASS-S18, BLOCKING, ARMED |

Fixed income fell 5.6% and cash 10.6%, which is not a one-day market move. Population counts: classification rows
532,932 -> 526,676 and clients 3,197 -> 3,193, while A_03 read 6,528 accounts (11,220 in the 23:00Z run).

**Limits.**
- Cause not determined.
- The 335 accounts' source is not traced: they appear in none of the daily transaction files read (09-30 to 10-03).
- Whether Saturday's 23:00Z fire repeats the drop is not known.
- Nothing was written; no served object was touched.

-- 3.0.0_SA_CVO

## MDPF_SECCLASS-S18 restore graded (ledger `secclass-s18-restore-0930-m-20261003`; CTO half batch 219 `5ec7db4eea`), read 08:2xZ 2026-10-03

| leg or claim | this seat's read | result |
|---|---|---|
| 0, H: no fire during or after the act | runner `i-01003b035d2988dfb` stopped; `bd-gold-nightly-fallback` and `bd-canonical-prices-daily` DISABLED (describe-rule) | PASS |
| C: 23,541 keys restored | the ledger: 23,578 rows -> 23,541 RESTORED, 36 SKIP-CREATED, 0 refused; 1 ETag mismatch (`client_tax_liability.parquet`, multipart source) resolved by a content sha256 match | accepted on the ledger's per-key log; this seat re-read the served results below |
| V: firm mix | `platinum/firm/mix_summary.json` version `5ACI.iHP..` (07:58:18Z): `data_as_of` 2026-09-30, 8 classes, MV sum $1,843,114,311.70, pct 1.000000 = the pre-run version | PASS |
| V: the 335 accounts | served `platinum/accounts/<id>/summary.json` for 335 of 335: 317 end at 2026-09-30 with value (sum $77,876,945.70), 12 have never had a summary (0 versions), 6 end on earlier dates that predate the run; 0 end at 10-01 | PASS |

**S18 is disarmed in the world.** The served BD platinum reads as of 09-30 again, and no fire can run until leg R.

**Still open:**
- The cause: why the 10-01 build dropped 335 open accounts, and why trade date 10-01 was partly delivered.
- Leg R: watermarks back to 09-30 and the rules re-enabled before Mon 10-05 04:00Z, under the class cell.

**Left as is, under the half:**
- 36 run-created keys remain served at the run's vintage: 28 under `platinum/clients`, 5 under `platinum/accounts`, 3
  under `platinum/advisors`. Deleting them needs human confirmation.
- gold intermediates outside the restore set (`gold/entities/accounts/*/aua_timeseries.json`) still carry the 10-01
  zeros; this seat did not find a served route reading `gold/entities`.

-- 3.0.0_SA_CVO

## MDPF_SECCLASS-S18 class cell (ledger `secclass-s18-cell-m-20261003`), independent read of leg V, 12:5xZ 2026-10-03

Legs P, G, W, Q, V and R are closed (R at 12:44Z: both rules ENABLED). Leg S, the first scheduled fire after R, is
this seat's (CTO batch 224 condition 2). The production run booted at 12:45:15Z; its log is awaited.

| acceptance (half, Branch A) | this seat's read | result |
|---|---|---|
| 2: mix as_of 10-01, every class, pct 1.0, MV within 2.0% of $1,843,114,311.70 | `platinum/firm/mix_summary.json` version `bKrQZIB6..` (11:39:59Z): data_as_of 2026-10-01, 8 classes (7 nonzero), pct 1.000000, MV $1,843,207,824.50 (+0.0051%), unclassified 4.1213% | PASS |
| the 335 return | the S18 run's 10-01 cube (version `E8dXQImv..`, 04:13:24Z) against 09-30 gives the 335; the cube now (`R9SpLSJ.T6..`, 10:15:44Z) holds 332 of them; still absent: z0818919951, z0821124151, z0822808251, the three the half names as traded out | PASS |
| 3: z0812888131 non-zero at 10-01, near 27,904.62 | gold 27,814.59 and platinum `summary.json` last point 2026-10-01 at 27,814.59 | PASS |
| 4: the 335's 10-01 synthetic_correction about 0 | gold `aua_timeseries` for 335 of 335: 09-30 $78,634,159.20, 10-01 $78,460,457.73 (-0.22%), synthetic_correction -$10,143.16 (the S18 run: -$78,504,236.80) | PASS (about 0 against the drop; not exactly 0) |
| served platinum for the 335 | 321 end at 10-01 (sum $77,770,557.05), 12 have never had a summary, 2 end on earlier dates that predate S18 | PASS |

**Not yet read.** Leg S, the 12:45:15Z production run (A_03 'Liveness ... 6,710 carry forward' and 'frontier whole' in
its own log; the served state after it). This seat records it when the log lands.

-- 3.0.0_SA_CVO

## MDPF_SECCLASS-S18 cell, leg S: the 12:45:15Z run is not the fire that closes it (read 14:5xZ 2026-10-03)

~M's ask (msg 104611) names the 12:45:15Z production floor as the first scheduled BD gold fire after R.

| read | result |
|---|---|
| CloudTrail StartInstances i-01003b035d2988dfb at 12:45:16Z by `advi-49f-gold-dispatch` | the floor started the runner |
| `/aws/lambda/advi-49f-gold-dispatch` 12:45:15-12:48:12Z: event `{"run_class": "production", "source": "advi.49f.scheduled-floor"}`; dispatched SSM document `advi-49f-chain-dispatch` (command 63f7686c..); "chain completed within the poll window", 177 s | a 3-minute advisor-intelligence chain |
| writes after 12:44Z in opal-data-bd: checkpoints S_00, A_00, A_02 (12:48:06-15Z); `gold/meta/fee_rate_history_watermark.json`; their telemetry. No A_03, C_06 or D_04 checkpoint; no gold_incremental log after 12:10Z; the served mix unchanged (`bKrQZIB6..`, 11:39:59Z) | A_03 did not run |

**Verdict.** Leg S is NOT CLOSED by this run. The 12:45Z chain did not execute A_03, the step the cell changed, so it
cannot show 'Liveness ... carry forward' or 'frontier whole'. The first scheduled fire that runs the fixed A_03 is
`bd-gold-nightly-fallback` at 23:00Z today (cron(0 23 ? * MON-SAT *), ENABLED). This seat reads that one.

**Open question for the cell's owner.** Today's checkpoint DIR already holds the QA run's A_03 to D_04 marks
(10:15-12:06Z). Whether the 23:00Z fire recomputes or skips steps carrying a same-day checkpoint is not read here; if it
skips, the first full fire is 04:00Z Sunday.

-- 3.0.0_SA_CVO
