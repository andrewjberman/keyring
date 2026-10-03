# Never-widen sign-off packet -- Inflection's Performance served from its holdings gold, and 49 Financial's label made GROSS (IB-pr-221; P-4)

Author `2.0.0_SA_COO~P`, 2026-10-02 ~19:5xZ. This packet supersedes
`DRAFT_NEVER_WIDEN_PACKET_INFLECTION_PERFORMANCE_FROM_HOLDINGS_GOLD_20261001.md` (@9893683dc3), whose one open pre-condition passed
today.

**Rulings.**
- batch 63 items 3-4 and 7; batch 80 items 2-7; batch 92 item 4; batch 95 items 3-5; PRD v0.23 ruling 23;
- CTO batch 175 G2 (every grant-staging function packages the owner reader);
- CTO batch 178 P-4 (the holdings-gold figure is GROSS; Andrew ~18:1xZ: "gross for now").

**Halves owed:** `1.0.0_SA_CTO` and `2.0.0_SA_COO~P`. Every number below was measured today unless it says otherwise.

## 0. Pre-conditions (read again at the hour of the act)

| # | pre-condition | read |
|---|---|---|
| a | `stale_gap_days_precondition.py` prints PASS | PASS 14:09Z, after Andrew's card 2 (nine delete markers, ledger @78a1f693f3); control 2026-05-12 intact |
| b | PRD ruling 23 ratified | DONE, v0.23 |
| c | the holdings-performance root plans with 0 errors | 7 to add, 0 to change, 0 to destroy at ~15:4xZ, after a backend `-reconfigure` (same bucket and key; remote state 09-29 14:42:58Z) |
| d | the gold is the rebuilt one | DONE 10-01: 1,613 of 1,616 partitions at emission 1.2; the 3 others now carry delete markers |

## 1. The acts, in order, under ONE ledger entry

| leg | act | resource | before | after |
|---|---|---|---|---|
| S0 | remove the DEPLOY-SERVE-HELD line from `holdings_performance.py` in its own commit, carrying `SERVE-RELEASE-ACK` | the CLOUD file (MSTR @a3866c3dfb) | held | released. The served bytes are the de3d423dce blob, which never carried the line |
| P1 | producer artifact, BUILT | `investor-reporting/irpt-holdings-performance-lambda.zip` | `gLRGHIyi...` (S3 `ifXqxmjU`) | **`kKgvbKtGjkfYlwroudNuIK9KTI/XsFKQ64KxqeWZ/bw=`** (S3 `OJ.bVNs_0qPbc.nFNwkbs5tfaGCOBl65`; re-pin @d107e96338, build row @bc66c2cee3); 2 of 14 members change |
| P2 | targeted apply, 49 Financial's producer function | `module.irpt_holdings_performance.aws_lambda_function.this` | `gLRGHIyi...` | the P1 artifact |
| P3 | targeted apply, Inflection's producer function, roles, policies and schedule | the 7 resources (plan above) | absent | created; `cron(0 14 ? * MON-FRI *)` UTC, input `source: orion` |
| G1 | the adapter role's read on the Inflection gold: commit the held `retained.tf` half of `HELD_FOR_SERVING_PACKET_adapter_repin_and_inf_gold_read_grant.patch`, then a targeted apply | `aws_iam_role_policy.performance_retained` | Inflection `implicitDeny` | `ListBucket` (prefix `irpt/inflection/gold/holdings_performance_daily/`) and `GetObject` on its `date=*/data.parquet` |
| F1 | adapter artifact, BUILT, then a targeted apply | `module.irpt_performance_adapter.aws_lambda_function.this` | `cdbFZDJA...` | **`/K1eLPuPnwG+HEQaSbvHI0wXgW4wCuXNBgdfsLQ18iQ=`** (S3 `7GwiGHEPjUOSh894mVi3Jn8i9QmzJbxF`, build row @dd4bd5fa8e); 3 members change and 1 is added (section 4) |
| V1 | after-reads | sections 6 and 7 | | |

The held patch's OTHER half (the adapter re-pin to 89b5a85abe) is SUPERSEDED. The source map now pins `installed.py` at 89b5a85abe
(@e4066e8d32) and `holdings_gold.py` at **394c246fb6** (@7cbc0159c2), which is the P-4 GROSS fix (IB-pr-298, merged @5ee6b92e8c).

**Order.** The producer goes first, so the daily job exists before anything is served from its table. The grant goes before the
adapter, so the adapter never meets a table it cannot read. Each apply goes through `safe-apply`, targeted.

## 2. Two pullers of the producer artifact (batch 95 item 5)

The one zip is pulled by `irpt-holdings-performance-lambda` (49 Financial; live; daily at 07:30 New York) and by
`irpt-inf-holdings-performance-lambda` (created by P3). P2 and P3 move both in the same window, and neither is left on the old zip.

49 Financial's after-state was measured on 10-01 (`f49_rowcompare`, no write) on THE SAME producer bytes (de3d423dce; the producer and
`sources.json` blobs are unchanged since):
- the producer computed 2026-09-25 and 2026-09-29 and was compared with the SERVED partitions: 7,540 of 7,540 and 7,559 of 7,559
  accounts, 18 shared columns;
- the only column that differs is `schema_version` (1.1 -> 1.2); the only added column is `span_trading_days`, which is 1 on every
  row;
- the return, the basket and every count are unchanged;
- its schedule is not moved.

## 3. What changes for whoever asks

| who asks | before | after |
|---|---|---|
| Inflection, a ruled window (year to date, quarter to date, one year, since inception), one permitted account | refused, `OBJECT_NOT_COVERED` | SERVED, provider `OPAL_HOLDINGS`, `fee_basis` GROSS. **The first Performance figure this product serves for Inflection.** |
| Inflection, the exact request of the one retained ORION report | refused | refused, `OBJECT_NOT_COVERED` (a retained vendor figure never reopens) |
| Inflection, any other window | refused, `OBJECT_NOT_COVERED` | refused, `UNSUPPORTED_OPERATION`, as 49 Financial's is today |
| 49 Financial, any holdings-gold answer | value V, `fee_basis` **NET** | **the same value V**, `fee_basis` **GROSS** (P-4, row S275: the label was wrong; nothing else moves) |
| Cottonwood | refused, `OBJECT_NOT_COVERED` | unchanged |

**Measured on the BUILT adapter bytes** (the F1 zip read back from S3 and extracted; read-only `adapter_candidate_inflection_read.py`;
no persistence): account 226, 2026-01-01..2026-09-30.
- **SERVED**, provider `OPAL_HOLDINGS`, value **0.024030831373**, 184 partitions read;
- three `linked_days` PARTIAL absences (05-12, 07-01, 08-11);
- it equals an independent chain of the gold's OK rows;
- 0 OK rows from any other build inside the window. Before card 2, the same chain read 0.003633 with the stale rows.
- The candidate answered `currency=None` for Inflection. This is as on 10-01 and is said, not changed here.

## 4. Members (on the uploaded zips, diffed against the DEPLOYED code from `get-function`)

**Producer:** 14 members; `holdings_performance.py` and `sources.json` change; 0 added, 0 removed.

**Adapter:** 70 -> 71 members. Changed: `installed.py`, `holdings_gold.py` (the draft's two; `holdings_gold.py` now also carries GROSS)
and `grant.py`. Added: `report_owner.py`. Removed: none.
- **`grant.py` + `report_owner.py`.** These come from IB-pr-297 (CTO batch 175 G2: every function that stages the render grant
  packages the owner reader). The adapter's `served.py` stays at its live bytes (f9a00f732c). Its `render_ports_from_env` imports
  only `grant` and calls `render_ports()` without an owner reader, so `report_owner.py` is packaged but not imported.
- **`grant.read`'s ACCOUNT branch is unchanged.** IB-pr-291 named every caller and proved its grant unchanged. A stored PROSPECT
  grant (none exists for this firm path) would refuse `EMPTY_GRANT` under the live Enforcer, as today.
- **Tests at HEAD:** performance 239 passed (237 plus 2 GROSS tests), 0 failed.

**Build integrity:**
- Both zips were read back and hashed equal to the map.
- The adapter build left 0 tracked files deleted, which proves row S276's fix on a real build.
- The adapter map entry's hash was written corrupted by the build ('C:/Program Files/Git/...', an MSYS conversion of a hash
  starting with '/'). It was corrected by hand to the S3 metadata value, which equals the zip's own hash. That is row
  IRPT_BCKEND-S278; the build commit @dd4bd5fa8e names it S277 in error.

## 5. Rollback, per key

- **P1/P2:** `s3api copy-object` of the prior artifact version (`ifXqxmjU`, `gLRGHIyi`) over the key, then the same targeted apply.
  49 Financial partitions written meanwhile at emission 1.2 are valid under both producers' readers.
- **P3:** destroying the 7 created resources is a deletion and needs Andrew's word. Without it, a targeted apply with the schedule's
  `state` DISABLED stops the job.
- **G1:** revert the two statements, then a targeted apply.
- **F1:** `s3api copy-object` of the adapter's prior version (S3 `wjneBb9_GyncZ6pLr_Q.hPbk86sXLLUj`, CodeSha256 `cdbFZDJA...`) and the targeted apply. Inflection then answers
  `OBJECT_NOT_COVERED` again, and 49 Financial's label reads NET again. A report retained for Inflection in between stays retained,
  and is named in the ledger if one exists.
- **S0:** re-add the line (MSTR's form).

## 6. Conditions

1. Pre-conditions (a) to (d) are read at the hour; (a) is printed with its control line.
2. Each plan is exactly the leg's resources. Each artifact's map hash equals its S3 content-sha256 metadata (row S278's check).
3. One 49 Financial day is computed dry by the DEPLOYED producer function (`dry_run: true`) before and after P2: same rows and
   census.
4. The Inflection function is invoked ONCE with `{"source": "orion", "date": <the newest computable day>, "dry_run": true}`. Its
   census must equal the rebuild's for that day. Its first scheduled fire is read from its own log the next trading day (Monday
   2026-10-05).
5. After G1: simulate the adapter role on the Inflection gold, get and list, each `allowed`; the Cottonwood bucket is still denied
   (negative control).
6. After F1:
   - the two probe invokes (empty headers; trusted headers with a non-existent user) answer the same before and after;
   - the section 3 read is re-run on the DEPLOYED bytes;
   - one 49 Financial answer reads `fee_basis` GROSS with an unchanged value;
   - ten minutes of log show zero error-class lines.
7. The first real Inflection request is read from the log and the retained report. Until one arrives, the served path is exercised
   only up to the Enforcer, and the packet says so.

## 7. Not measured, and said

- A real, authorized Inflection request end to end. No scripted human identity exists.
- The Performance tab's rendering of a served Inflection figure (`2.0.0_SA_COO~D`'s page).
- Inflection's gold before 2024-07-11 rests on weekend pairs only; a since-inception window reaches into it.
- The 49 Financial rowcompare was measured 10-01 on these producer bytes, not re-run today.

## COO half -- 2.0.0_SA_COO~P

SIGNED, 2026-10-02 ~19:5xZ, on this packet's bytes at the commit that carries it.
- The write set is two artifacts, two functions' code, seven created resources, one role policy and one held line.
- 49 Financial's values are unchanged by measurement (the rowcompare). Its label moves to GROSS by ruling.
- Inflection's first served figure is measured on the built bytes against an independent chain.
- Rollback is per key.

## CTO half

OWED.
