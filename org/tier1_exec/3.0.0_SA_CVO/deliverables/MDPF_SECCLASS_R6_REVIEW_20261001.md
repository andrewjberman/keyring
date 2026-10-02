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
