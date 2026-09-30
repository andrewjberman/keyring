# Never-widen sign-off packet, R3 -- the 49F re-switch alone: hD7G6YT1 plus the runners_49f sys.path fix

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-29 ~12:5xZ.
**Ledger:** `irpt-adapter-holdings-gold-49f-r3-20260929` (U1 and P1 closed @23126d4739; D1 and A1 open).

**Why:** the r2 switch (packet blob a4679360, artifact hD7G6YT1) served from 10:14Z. Every 49F YTD, QTD and 1Y then
answered UNEXPECTED with `ModuleNotFoundError: parity_period_returns`, and the switch was rolled back at 10:58Z
(9e0bde13e3; CTO 102736, CRO 102735). The cause: `installed._holdings_source` replaced `_engine_source`, which had put
`data/assets/scripts/gold/runners_49f` on `sys.path`. Since inception skips `_period_for`, which is why the cold start
and the since-inception smoke passed.
- **Fix:** TO-IB-pr-201 amendment 2, WK~77, drained @66469ce943. `build_runtime` puts the packaged runners_49f
  directory on `sys.path` beside `lib` and `investor_reporting`, and a test covers it. P20-3-AC1, P20-1-AC2 and
  P20-2-AC1 all PASS on the issuer's re-run on CLOUD.
- **Ruled by 1.0.0_SA_CTO 102746:** 49F ALONE. No Inflection change rides this artifact; INF (pr-221) follows as its
  own act.

**Carried unchanged from r2** (`NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_HOLDINGS_GOLD_49F_R2_20260929.md`, blob a4679360):
section 1 (the CRO's section-6 items as done), section 3's served-rule design, the two IAM surfaces and the rollback
shape.

## 1. What ships

| surface | before (live) | after |
|---|---|---|
| Lambda `irpt-performance-adapter` | `qfxZ0DzB` (S3 LQvugN7E) | `+h/AH/RY` (S3 `TBy0pL.rwpHBE1BBqkyIDYC6Dky4QS7j`, 12:23:58Z) |
| role policy `performance_retained` | engine prefixes (`gold/advi/canonical/twr_daily/`) | `irpt/49financial/gold/holdings_performance_daily/` (list + `date=*/data.parquet` get) |
| bucket policy `opal_data_49financial`, the two adapter Deny statements | engine prefixes | the holdings-gold prefix |

- **Artifact census:**
  - vs hD7G6YT1: ONLY `installed.py` differs (blob cd2f1d86, pinned @66469ce943).
  - vs live: 69 -> 70 members; `holdings_gold.py` added; `PerformanceReport.schema.json`, `entry.py`, `installed.py`
    and `retained.py` differ.
  - Flat census pin skew 0. ~Y's zip_module_census FAIL set is a strict subset of live's.
  - Cold start with /var/task mapped: IMPORT OK, the named envelope.
- **Plans (P1):** performance 0/2/0 (the role policy + code only); shared-infra `-target` bucket policy 0/1/0. Both
  are identical to r2's. The TF bytes are ae20e904e6's, restored from 9e0bde13e3~1.

## 2. Pre-apply evidence on the BUILT bytes (sweep-2 section 1; CRO 102752 (c))

Each check below runs in a fresh interpreter whose import path is ONLY the extracted artifact. Repo paths are stripped,
so the runners directory is absent from the harness path. `installed.build_runtime` composes the service over the
real S3 client and a table stub that refuses every call. Each exception is classified by the built Entry's own
reasons table.

**Every served period, cold** (`checks/r20/adapter_cold_periods.py`, end 2026-09-28, the latest gold day):

| account | YTD | QTD | 1Y | 3Y | SI |
|---|---|---|---|---|---|
| ..498003 (thread) | +5.10% | -1.62% | +7.70% | UNSUPPORTED_OPERATION | +39.32% (from 2024-11-07) |
| ..884180 | +186.51% | -15.42% | +186.51% | UNSUPPORTED_OPERATION | +186.51% (from 2026-03-16) |
| ..064180 | +6.04% | -1.21% | +8.57% | UNSUPPORTED_OPERATION | +23.72% (from 2024-07-09) |
| ..480090 | +7.08% | -0.67% | +9.12% | UNSUPPORTED_OPERATION | +11.39% (from 2025-08-20) |

- Every figure is provider OPAL_HOLDINGS. 3Y is `HoldingsWindowNotRuled`, a named refusal. 0 UNEXPECTED.
- **Control:** hD7G6YT1 under the same harness fails with `ModuleNotFoundError: parity_period_returns`, the served
  defect.
- **Wall time:** the SI answers took 5.7-6.9 s locally, reading 558 partitions.

**All-accounts census, the adapter's own code on the built bytes** (`checks/r20/adapter_cold_census.py`):

End 2026-09-28, every account with a row on that day (7,548), run on the gold AFTER row S205's remedy.

The first run of this census found 14 accounts at about +1,368%. The cause was the scheduled producer, which ran
pre-v0.20 code. It was fixed under its own ledger (`irpt-holdings-performance-producer-v021-20260929`, CLOSED
@969b4deffd, both halves), 2026-09-28 was re-emitted, and S205 is disarmed by row S209.

| period | figures | named refusals | UNEXPECTED | >= +100% | <= -100% |
|---|---|---|---|---|---|
| YTD | 6,766 | 782 OBJECT_NOT_COVERED | 0 | 2 (..4180 +186.5%, ..2297 +145.4%) | 0 |
| QTD | 6,726 | 822 OBJECT_NOT_COVERED | 0 | 0 | 0 |
| 1Y | 6,775 | 773 OBJECT_NOT_COVERED | 0 | 3 (..4180, ..8562 +138.5%, ..2297) | 0 |
| SI | 6,831 | 717 OBJECT_NOT_COVERED | 0 | 6 (..2297 +224.8%, ..2191 +212.2%, ..4180, ..7477 +127.9%, ..8562 +125.4%, ..4060 +101.1%) | 0 |

- Every refusal is `HoldingsGoldRefused: holdings gold carries no OK row inside the window`: the empty accounts of
  the r2 breakdown, account value 0.
- The >= +100% set is r2's known set (r2, to 09-25: YTD 2, 1Y 4, SI 7), less the accounts whose chains moved below
  +100% over 09-26..09-28.
- 1.0.0_SA_CTO 102832's condition is met: the census re-ran on the rewritten 09-28 gold, and this packet cites it.

## 3. The rollback branch, READ (the CTO r2 condition 1)

The r2 window 10:14-10:58Z was the rollback branch, measured live. Under the restored qfxZ0DzB, the CRO's walk
20260929T110814Z read:
- the control YTD at 5.93% on the engine;
- NEW-01 YTD and 1Y as the named `DEPENDENCY_UNAVAILABLE`;
- 3Y and SI as `UNSUPPORTED_OPERATION`;
- 0 UNEXPECTED of 31 answers (102752).

The r2 carry stands: a by-id open of an OPAL_HOLDINGS record under qfxZ0DzB refuses as UNEXPECTED. A rollback of this
act returns to that same, measured state.

## 4. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. BEFORE: the CRO's read on qfxZ0DzB. The 11:08Z rollback read (102752) is the baseline; the CRO re-reads the
   control and one of the six SI accounts in section 2 at apply time.
3. The S3 latest version equals `TBy0pL` just before the apply, written in the ledger. Fresh plans equal P1.
   safe-apply performance, then shared-infra `-target` (halt gate; HALT_ACK=1 only on 0 STOP items).
4. **Read back:** CodeSha256 == `+h/AH/RY`; the role and bucket policies as planned; re-plan both: No changes.
5. **Deployed invokes (CRO 102752 (a); CTO 102736):** the first signed-in presses after the apply land on a fresh
   container.
   - The CRO presses YTD, 1Y and SI on the control account.
   - This seat reads the adapter's log for that window and prints: Init, each answer's code or figure, the SI REPORT
     Duration and its `irpt_holdings_phases` line.
   - **Rollback triggers:** any UNEXPECTED, or SI at or over 48 s (80% of the 60 s timeout).
6. **AFTER (A1; CRO 102752 (b)):** the CRO presses YTD, QTD, 1Y, 3Y and SI per account over r2 section 4's set
   (NEW-01, the control, ..0273, ..0695, one ..4581) plus the six SI accounts at or above +100%.
   - This seat reads every adapter invocation in the window: counts by code, and 0 UNEXPECTED.
   - COT and INF unchanged. Any unnamed difference triggers a same-turn rollback.

**What "the census through the deployed Lambda" means here:**
- The deployed census is the named set of step 6, pressed through the page. A deployed read needs a verified viewer
  identity, and each fresh answer writes an accepted report. So a deployed read of all ~8,000 accounts is not an act
  either half has signed.
- The all-accounts census is section 2's: the adapter's own code, on the built bytes, the runners directory absent.
- If a half wants the deployed census wider, it names the set.

**Rollback per key:**
- **Lambda:** S3 version LQvugN7E (`qfxZ0DzB`) copied as latest, then re-apply performance.
- **Role policy and bucket fence:** revert 23126d4739's two .tf files to 9e0bde13e3's bytes, then re-apply both
  (the r2 rollback, measured at 10:58Z).

## Carried from the S205 producer halves

- **CRO condition 3:** Wednesday 2026-09-30's 11:30Z scheduled fire is read from its partition (0 OK rows at |r| >= 1,
  and the source named in the fire's log). It is written into this ledger's A1 leg.
- **CTO 102832:** the INF switch's packet names a SCHEDULED Inflection producer and fire. TO-IB-er-501 (drained
  @d110bee556, plan only) is that schedule's build. INF is not in this act.

## What the halves sign against

This file's committed blob; 23126d4739; artifact `+h/AH/RY` (S3 `TBy0pL`); the section 2 evidence; the apply protocol
of section 4.
