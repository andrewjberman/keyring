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
