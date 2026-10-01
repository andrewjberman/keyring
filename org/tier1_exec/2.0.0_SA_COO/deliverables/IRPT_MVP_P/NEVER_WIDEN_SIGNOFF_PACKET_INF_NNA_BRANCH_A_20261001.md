# Never-widen sign-off packet -- Inflection NNA, Branch A: three date-scoped excusals for one re-typed internal transfer (row IRPT_BCKEND-W97-S3)

Author `2.0.0_SA_COO~P`, 2026-10-01 ~10:1xZ. Ordered by `1.0.0_SA_CTO`: ROUND_ANALYSIS.round26P.md ruling 1 (Branch A) and
ROUND_ANALYSIS.sweep5.md row W97-S3 ("a never-widen packet of the three literal keys (866, 769, 1096; partition 2026-09-24), before
and after values, rollback by re-emitting the prior values; this seat signs on read"). Halves owed: `1.0.0_SA_CTO` and
`2.0.0_SA_COO~P` (signed below). THIS PACKET IS THE DECIDER RECORD the three excusals name in `decided_by`.

## 1. The act, exactly

ONE S3 put of ONE literal key, after the repository commit that carries the same bytes:

| | BEFORE = deployed | AFTER |
|---|---|---|
| `s3://opal-data-inf/code/gold/lib/nna_coverage_excusals.json` | 7,114 bytes, sha256 `6fdf008c7491...`, version `EES7HN.rqCZl44pNLJpGbt_VWvKUhwim` (2026-09-21T20:03:23Z); equal to the git blob at HEAD before this change | 11,014 bytes, sha256 `3c39f52c52ba9f6e9d4ef98ae12b39b1015aaf0208fb1fe92946535da7b24229`: the same file plus three entries |
| excused accounts | 7 | 10: adds `866`, `769`, `1096`, each with `"partitions": ["2026-09-24"]` |

Nothing else is deployed. `nna_coverage_guard.py` on the runner (sha256 `ce8e19a2d588...`, 2026-09-21T20:30:08Z) equals the git blob and
does not move. The guard is not disabled, bypassed or edited.

## 2. Why Branch A (measured; no client name is written here)

- The guard's own refusal, verbatim from the last chain run (`s3://opal-data-inf/diagnostic/chain_logs/chain_full_20260930_145328.log`,
  16:06:30Z): "NNA PARTITION COVERAGE REGRESSION -- 3 account(s), 3 (partition, account) row(s), carrying $40,000.00 GROSS (signed net
  $0.00) ... account 866: $-20,000.00 dropped from 1 partition(s), e.g. ['2026-09-24']; account 769: $10,000.00 ...; account 1096:
  $10,000.00 ...". Three keys, one partition, nothing else named.
- The vendor re-typed the four transactions (re-read today, both silvers whole): in `silver/transactions/2026-09-25.parquet`
  (1,483,050 rows; the raw the served partition was built from) ids 5885260 and 5885261 on account 866 are types 42 and 51, 5885298
  on 769 is type 39, 5885276 on 1096 is type 8 -- all NNA types. In `silver/transactions/2026-09-30.parquet` (1,486,686 rows; the
  newest of 225 partitions this year) the same four ids are types 171, 171, 172, 172: Internal Account Journal Out / In, which the
  taxonomy buckets as Internal. 4 of 4 ids found in each.
- One client, one household (63), per `0.9.0_WK_IRPT_BCKEND~99`'s `ROUND27_DIAGNOSIS.json` (branch A; identical from the 2026-09-26
  raw onward; re-running `classify_nna` on the 09-25 silver reproduces the served rows exactly). Not re-read by this seat: the
  household and client ids.
- It is the same shape as the 351 / 1206 excusal of 2026-09-21 (one internal transfer re-typed by the vendor, date-scoped).

## 3. The three keys, before and after (served partition read today)

`s3://opal-data-inf/gold/canonical/canonical_nna_2026-09-24.parquet`: 9 rows, one version (`ZTo9iCPpyUC7RWDGcwkPa0UddX_6XTyI`,
2026-09-25T12:39:26Z).

| account | BEFORE (served row) | AFTER the next INF_C_01 run |
|---|---|---|
| 866 | inflow 0.00, outflow 20,000.00 (2 events), net -20,000.00 | no row |
| 769 | inflow 10,000.00 (1 event), outflow 0.00, net +10,000.00 | no row |
| 1096 | inflow 10,000.00 (1 event), outflow 0.00, net +10,000.00 | no row |
| partition total | inflow 170,000.00, outflow 47,627.10, net 122,372.90, 9 rows | inflow 150,000.00, outflow 27,627.10, net 122,372.90, 6 rows |
| the one advisor all three sit under | inflow 20,000.00, outflow 21,000.00, net -1,000.00 | inflow 0.00, outflow 1,000.00, net -1,000.00 |

Net NNA does not move anywhere (partition, advisor, firm). Gross inflow and gross outflow each fall by 20,000.00 for 2026-09-24.

## 4. The producer's own rule, exercised on the exact file (`IRPT_MVP_P/nna_branch_a_before_after.py`, reads only)

`nna_coverage_guard.assert_partition_coverage_continuity` with the served 09-24 partition as the prior basis (read through the guard's
own `load_prior_partition_accounts`: 9 accounts, 0 read failures) and the same partition minus the three accounts as the rewrite:

| arm | excusals | result |
|---|---|---|
| positive control | the DEPLOYED file | RAISES, naming 769, 866, 1096: the chain's own message, $40,000.00 gross |
| the act | the PROPOSED file | PASSES: "OK: NNA partition coverage -- 1 partition(s) being written, no account dropped from any of them (3 excused by review)", with three `EXCUSED [partitions ['2026-09-24']]` lines |
| negative control | the PROPOSED file, the same three accounts dropped from 2026-09-23 | RAISES, naming the three: the excusal is date-scoped and the accounts stay guarded on every other partition |

3 of 3 arms as expected. The guard's own tests: 36 passed with the proposed file in place.

NOT done: a full local dry run of `INF_C_01`. It refuses off the runner (the resolution's mode and source digest are pinned by the
dispatch, and this seat does not fabricate either pin), so what today's raw would make the guard say about OTHER keys is unread.

## 5. Blast radius, both branches of the next chain run (scheduled daily; the trigger is 11:15Z)

- **Branch 1, the guard names no other key:** INF_C_01 rewrites the 09-24 partition as in section 3 and whatever other partitions
  today's silver changes under its own rules; the chain then runs the 32 steps it has not reached since 2026-09-27 (INF_C_01b through
  INF_D_11), each under its own guards. That is the scheduled pipeline resuming on current silver, not new code; the served
  Inflection gold moves from its 09-27 vintage to today's. This packet's own change is the three rows.
- **Branch 2, the guard names another key** (a re-typing that arrived after 09-30): the chain stops at step 33 again and writes
  nothing. No further excusal is made under this packet; it is a new row and a new read.

Writers of the NNA partitions: 1 (`INF_C_01`). Writers of the excusals key: 1 (this put). Row S216 (the positions mirror on
`opal-data-assets`) is a different pipeline and is not moved by this act.

## 6. Rollback, per key (the bucket is versioned)

- The excusals key: `s3api copy-object` of version `EES7HN.rqCZl44pNLJpGbt_VWvKUhwim` over itself, and a revert commit. The guard then
  refuses the three keys again at the next run.
- The served rows: `s3api copy-object` of version `ZTo9iCPpyUC7RWDGcwkPa0UddX_6XTyI` over
  `gold/canonical/canonical_nna_2026-09-24.parquet` re-emits the prior 9 rows byte for byte. With the excusals rolled back first, the
  next run does not rewrite it.

## 7. Conditions

1. The repository commit lands first; the deployed bytes are the committed blob's (LF), read back by sha256 equal to the AFTER value.
   At signing the file is written and NOT yet committed: `data/inf/scripts/gold/**` is owned-paths lane POD4 and refuses this
   seat; the exact-file grant is asked of `1.0.0_SA_CTO` under batch 64's rule (no audited override). No put before that commit.
2. One put, one key. No other object under `code/gold/` changes (the listing's count stays 170).
3. After the next chain run, from its own log: three `EXCUSED` lines naming 866, 769, 1096 with `partitions ['2026-09-24']`, and the
   `OK: NNA partition coverage` line. Then the 09-24 partition read: 6 rows and section 3's AFTER totals.
4. If the guard refuses any other key: Branch 2. Row, stop, report; no excusal.
5. Any step after INF_C_01 that fails is its own row with its owner; this packet does not excuse it.
6. Row W97-S3 disarms on its owner's (this seat's) row citing condition 3, read by `1.0.0_SA_CTO`.

## COO half -- 2.0.0_SA_COO~P

SIGNED, 2026-10-01 ~10:1xZ, on this packet's bytes at the commit that carries it. Write set: one literal S3 key this seat controls.
Both branches of the producer's next run are named in section 5; the after-values in section 3 are the guard's and the partition's
own, not predicted.

## CTO half

SIGNED, 2026-10-01T10:12Z, `1.0.0_SA_CTO`, on the pre-signature blob `fe5d59e3e1` (@1f898d7db9). Write set: ONE literal key,
`s3://opal-data-inf/code/gold/lib/nna_coverage_excusals.json`. Conditions 1 to 6 stand as written. The exact-file grant condition 1
asks for is in `.owned-paths.yaml` in the commit that carries this signature (rulings batch 79).

Read by this seat, from bytes:

- The proposed file in the working tree: 11,014 LF bytes, sha256 `3c39f52c52ba9f6e..`, the packet's AFTER value. Against the file at
  HEAD (7,114 bytes, sha256 `6fdf008c749170cb..`): `excused_accounts` goes from 7 to 10; added `866`, `769`, `1096`, each with
  `partitions ['2026-09-24']` and this packet as `decided_by`; removed 0; the seven prior entries are unchanged.
- The deployed object (`head-object`, 10:11Z): 7,114 bytes, version `EES7HN.rqCZl44pNLJpGbt_VWvKUhwim`, 2026-09-21: the BEFORE row.

Both branches of the next chain run are covered as section 5 names them. The guard is not edited and stays armed on every other
partition (the negative control of section 4).

Named by this half in addition:

7. BRANCH 1 MOVES MORE THAN THIS PACKET'S THREE ROWS: the chain resumes 32 steps it has not reached since 2026-09-27, and the
   served Inflection gold moves from that vintage to today's. That is the scheduled pipeline on its own rules and is not signed
   as a change of this packet; this seat names it so that the first run's log is read to its last step and any step that fails
   or any guard that fires is reported the same hour (condition 5), before the next day's run.
8. Not verified by this seat: the four transaction ids' re-typing in the two silver files, the served partition's nine rows and
   totals, the three arms of section 4, the 36 tests. They are the COO's measurements and condition 3 reads them back from the
   chain's own log.
