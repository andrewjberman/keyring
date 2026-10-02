# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status

Seat `2.0.0_SA_COO~M` (CLAUDE). Contract
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`. Reviewer `3.0.0_SA_CVO`.
As of 2026-10-02T18:1xZ. Brought current on CTO batch 178 item (1) (msg 104327); the 10-01 pins below are replaced.

Mode: FULL (no live lease for this seat; `.tools/drive-mode.py status`). The BD r3 re-land stays first (batch 178).

Claim words: `measured` = read this session; `held` = cited from a record, not re-read.

## Pins

| What | Value | Claim |
|---|---|---|
| Deployed `irpt-holdings` | CodeSha256 `tS/APci3Mz/YRDP7pJboAVqKabShek9jYUqvQDIYwwE=`, LastModified 2026-10-01T20:13:14Z (ledger `irpt-inf-split-positions-m-20261001` leg R: split accounts list their positions, a two-view account counts once) | measured (get-function-configuration 2026-10-02 17:5xZ) |
| Producer `holdings_snapshot.py` at CLOUD | daaef69b9d: `ASSET_CLASS_VALUES` admits `multi_asset` (CTO batch 164, readers first); NOT deployed; no row carries the class | measured |
| Published contract at CLOUD | `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` admits `multi_asset` at nodes[], security_aggregates[], class_totals[] (daaef69b9d); `holdings/contracts` copy the same; `_contracts` copy by 2.0.0_SA_COO~P @16a3fcfd6a. The `irpt-holdings` package re-stages from committed blobs at its next move (STAGE_MANIFEST pins) | measured |
| Served publication read | 2026-10-01 business date, built 14:16-14:17Z: 49financial rev 3413e2b5a3bd (153,345 nodes), inflection 100a0dc22f12 (36,048), cottonwood a3751a6acff2 (17,872) | measured (gold parquet per manifest, sha256 checked) |
| CLOUD (local) / origin/CLOUD | 7421b39e62 / 92a12727600d (ls-remote read 18:1xZ); this seat's commits are LOCAL and travel on the integrator's push | measured |

## Live thread

LIVE END TO END for the Holdings tab at three firms (held from the 09-27 walks). Read this session on the served
2026-10-01 publication (`MDPF_SECCLASS_M/R8_CHECKS/HOLDINGS_PUBLICATION_ROW_READ_20261002.json`): every written
classification row a firm holds is served with that row's class and sub class (cot seed 19 of 19, name-pattern 3 of 3,
BD first act 10 of 10 held, BD mapped 25 of 25 held); three row ledgers closed on it (7421b39e62).

Inflection split accounts (row S259) on the served publication: 857 accounts, 0 whose securities fail to sum; 71 split
accounts list 3,963 positions as part NOT_STATED (35,466,629.25 USD); 786 single-view accounts. The walked split account
is owed (below).

## Acceptance IDs (goal record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`)

| ID | State | Evidence |
|---|---|---|
| (1) signed-in journey 49F / INF / COT | MET | held: ~D HARs w8 + w9 (09-27) |
| (2) every active 49F/INF account resolvable or refused explicitly | MET on the then-current directories | held: census @f247a922a5 |
| (3) COT soundness, window disclosed | built and served; page re-read owed with the walks below | held (10-01 build read) |
| W2-11, W2-15, W2-19 served | SERVED since 2026-10-01 06:31:21Z; CVO grade owed | held |
| S259 split accounts list positions | SERVED (route 20:13:14Z; publication above, 71 / 786 branch count) | measured; walk owed |

## Write claims

None open on IRPT_BCKEND paths. (MDPF_SECCLASS act ledgers are tracked in that project's records.)

## Next proof

The two walks the open ledgers still owe on the served 2026-10-01 publication: one Inflection split account
(`acc_015d15b45d7a8ac71f951a67`, ****3282, 771,891.63 USD) ties on the page (ledger `irpt-inf-split-positions-m-20261001`
leg S), and one Cottonwood selection holding SPYI / PSLV ties (ledger `secclass-cot-seed-rows-m-20261001` leg S).

## Next-list, in order

1. **BD r3 re-land first** (batch 178): legs S of `secclass-bd-thread-r4-reland-m-20261002` at tonight's 22:10Z silver
   and 23:00Z gold fires; Cottonwood re-point leg R (QA run fired 17:59:30Z) and leg S (the 10-02 scheduled run).
2. **The two walks above**, then close both ledgers' legs S.
3. **Batch 178 item (2):** once 2.0.0_SA_COO~D's H-1 (dropping the "Smaller holdings" tile) lands, read the distinct-
   security count for the proof snapshots (49 Financial's largest client and one Cottonwood client), and bring brief 3
   item 1.4(d), the TARGET fold, back as its own ask with that measurement.
4. **multi_asset readers packet** (batch 164): producer + contract on CLOUD; Advisor Intelligence readers portal
   6245e92d at CTO review (msg 18:07Z); ~D's half on DEV 7bcedf1b. Then the packet's deploy halves (producer, the
   `irpt-holdings` re-stage), PROD readers, and only then the rows.
5. The -0.0 fix @38b72bf469 rides the next `irpt-holdings` move and is named in that move's half (held).

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| H-1 (the treemap's "Smaller holdings" tile dropped) | `2.0.0_SA_COO~D` | brief 3 H-1..H-3 | AWAITED (batch 178 routed it there) |
| CTO review of the portal candidate | `1.0.0_SA_CTO` | portal 6245e92d | ASKED 18:07Z |
| multi_asset colour and IR readers | `2.0.0_SA_COO~D` | portal 262be0a4 | CONSUMED: on DEV 7bcedf1b |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Cottonwood serves JABAX (Janus Henderson Balanced, a balanced fund) as alternatives / Structured Notes by name alias on the fallback -- a multi_asset member by batch 164's boundary | `2.0.0_SA_COO~M` (MDPF_SECCLASS) | the multi_asset rows act (after PROD readers) |
| 49 Financial: most custody has only a TARGET drill (the remainder block); brief 3 item 1.4(d) | `1.0.0_SA_CTO` | item 3 above brings it back with its measurement |
| The declared fallback still classes an unknown 1-5 letter ticker `equity` by its shape | `2.0.0_SA_COO~M` | MDPF_SECCLASS E8 and E9 land (the fallback's sunset) |
| PRD v0.22 ruling 22 (NOT_FOUND vs `OBJECT_NOT_COVERED` in `_authz` / `holdings/entry.py`) | `2.0.0_SA_COO~P` | ~P or the CTO says whether ruling 22 moves that code |

## Limits

The publication reads use each manifest's gold parquet (the same revision's nodes, sha256 checked), not the platinum
partitions, because the network read the 188 partitions too slowly to finish; the page has not been walked this session.
No product ID is PASS until the CVO grades a pinned candidate.
