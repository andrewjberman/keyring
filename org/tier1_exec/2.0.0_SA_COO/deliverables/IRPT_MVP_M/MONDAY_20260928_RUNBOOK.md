# Monday 2026-09-28 runbook -- 2.0.0_SA_COO~M, IRPT_BCKEND~M

This is the order of every signed act waiting on Monday. Each step names its gate, its read and its rollback. Scripts
and records are in this directory unless another path is given. Work only from the worktrees named here; never
`git stash` in the shared tree. Commit through `safe-commit.sh`.

## A. The first scheduled COT run (after it completes; trading day T-1 = Fri 09-25)

1. **Read back the three R1 legs** before any merge. Each gets `close-leg` with its proof, then `close`:
   - `cot-other-admission-m-20260925` R1: `other` passes through the C_06 mix. Today's value is 0, so its absence
     is not a defect.
   - `cot-cash-admission-m-20260925` R1: z09308463 shows a cash slice (0.37 at 09-22) and its shares sum to 1;
     z09326138 or z09308511 shows 100% cash.
   - `bd-securities-cot-new-p1-m-20260926` R1: COT and BD runs classify the Part 1 keys as written (941 keys;
     receipt `BD_SECURITIES_COT_NEW_P1_RECEIPT*`).
   - If any leg FAILS, stop and do not merge. The failure is the next item, and the matching rollback is in its own
     ledger entry.
2. **Baseline served D_03:** `python cot_served_composition_check.py --out COT_SERVED_COMPOSITION_POSTRUN_20260928.json`.
   It shows the deployed act-1 and cash-admission bytes; the 09-23 July baseline had 9 over 100%.

## B. The COT cash-line act (both halves: CTO + CRO on 9e3f568d42 + 0deac23f1e; S155 re-cut ff63895521)

Pre-deploy (CRO 101595):
- `python cot_cash_line_negative_census.py` must reprint 17 of 29 net negative.
- Print d08's QA value beside C_06's at the read-back.

1. `python .tools/deploy_ledger.py open` for slug `cot-cash-line-m-20260928`. The manifest has four legs, C_06, D_03,
   D_04 and lib/mix_views, and must name:
   - branch `irpt-m-cot-cash-line-act` @0deac23f1e: 8a52e2c352, f28c0d89f2, 9e3f568d42 and 0deac23f1e, the signed
     act;
   - branch `irpt-m-s152-cloud` @ff63895521.
   Commit the OPEN sentinel at once.
   - NOT in this act: ccb9b38dd8 (structured/commodities in COT C_06/D_03/D_04), on `irpt-m-cot-b1`. It is ETF Part
     B's B1 and merges under B1's ledger with ~X's commits, the same split the CTO and CRO ruled for S155 (101686,
     101688). At that merge, the S155 test `test_s152_mix_views_cash_other.py` must take B1's widened list.
2. Merge both branches into CLOUD with `.tools/safe-merge.sh` (clean index, `OPAL_AGENT_SERIAL=2.0.0_SA_COO~M`). COT
   gold deploys on push (S141), so the deploy is safe-deploy of those four scripts under this ledger, HALT_ACK=1.
3. Verify the served bytes: each S3 object's version and sha equal the merged file.
4. After the next scheduled COT run:
   - z09305653's cash slice is about 82.5%;
   - `cot_served_composition_check.py` shows **0 over 100%**;
   - `s152_period_view_identity.py` on that date: per row, |cash + other + unclassified_after - unclassified_before|
     <= $0.02 and total EXACT (CTO 101700, CRO 101702);
   - the firm period row's cash includes the $19,230,791.02 of sweeps;
   - d08 printed beside C_06.
5. Rollback per key: the prior S3 version of each of the 4 scripts, the prior Holdings revision, then a D_04 re-run.

## C. COT-new Part 2 (26 `other` keys; CTO @ab4a2e41bb)

Gate: A.1 passed, AND d08 (and d06) admit `other`. That is ~X's commit 88bf469ebf and 2c23591d48 on
`ds-x-b1-cashline`; they merge and deploy under ETF Part B's B1 ledger first (CTO 101639).

1. `python bd_securities_write_cot_new.py --part 2` under ledger `bd-securities-cot-new-p2-m-20260928`. Read back 26 of 26.
2. Tell 2.0.0_SA_COO~D: z09305589's Other slice is $19,653,063.27.

## D. R4 in the host window (~12:52Z onward)

0. **Before the QA fire, re-mint the Holdings packages from CLOUD** (irpt_holdings_{49f,inf,cot}, STANDALONE_BUNDLES,
   manifest-stamped) under their own ledger. Do it after B has merged `holdings_snapshot.py` (the cash rule on
   `display.description`). The scheduled producer runs the S3 package, not CLOUD, so without a re-mint the rule is not
   served. Read back members-sha256 and confirm it changed from 83f6a81aab34.

1. N1: `python r4_monday_negative_arm.py --send`, then `--read`. COT must be refused on opal-data-bd and 49F refused
   on opal-data-cot, while own reads are allowed. Close leg N1 of `irpt-holdings-principals-dispatch-m-20260925`.
2. The QA fire: `aws lambda invoke --function-name irpt-holdings-refresh-lambda --payload '{"qa": true}'`, then read
   holdings_qa.
3. Re-run the pinned diff (`account_mask_publication_diff.py dry --pin-served`) and the INF name census, then fill
   `NEVER_WIDEN_HALF_REQUEST_R4_ENABLE_DRAFT.md`. It carries:
   - ETF Part A, 16 keys including VNQ to alternatives (Andrew-direct 00:1xZ 09-27);
   - the own-mask labels;
   - the Holdings cash-line rule (`display.description`).
   Send it to the CTO and CRO.

## E. Not Monday-gated, but open

- ETF B2 (13 keys): waits on B1 landed, ~D's C34 SERVED (on local portal DEV a28c0172 only) and a re-census at
  0 RAISE / 0 drop.
- Goal /verify: waits on ~D's walk HAR.
- 6 stale served COT composition files: after A.2, if they are still stale, a delete needs Andrew's confirmation.

## F. Drain notes

- Surprise ids: ~X's branch rows S150-S153 are already on CLOUD as S153-S156 (@92244581d2, CTO 101771). At the ~X
  drain, drop the branch's copies; CLOUD's S150-S152 stay. The COT mix_views row is S155.
- After D.3's first enabled publication, check that INF holdings as-of is at or after 09-25; that disarms CLOUD S152
  (~P's). INF upstream is complete through 09-26.

## G. Merge order (Andrew-direct 12:4xZ 09-27, "rec approved"; ANDREW_DIRECT_20260927_124xZ_MERGE_TO_CLOUD_AFTER_MONDAY_R1.md)

Everything on ~M's branches reaches CLOUD. Gold paths go only after A's R1, each under its ledger: first B (cash-line
act plus S155), then B1 (`ds-x-b1-cashline`, `irpt-m-cot-b1`, and comp-constants 9135feae97 with ~X's BD commit). ~X's
four records ride the `ds-x-b1-cashline` merge (only ~X may commit its deliverables folder).

## H. History purge before any merge (Andrew-direct ~19:5xZ 09-27 via the CTO, call 2; record @fce766f6ed)

- 0.0.0_AB_MSTR rewrites history to purge 34 client PNGs. Every commit after 9b5eed8f9d gets a new hash, and all six
  ~M branches contain it (is-ancestor read 19:5xZ).
- NEVER merge an old-history branch into the rewritten CLOUD: it re-introduces the PNGs.
- Before G: confirm that MSTR's rewrite covered these refs (asked 19:57Z). If it did not, re-cut each branch by
  cherry-picking its own commits onto the rewritten CLOUD (scratch branches; this is not a shared-branch rebase).
- Map every cited hash (0deac23f1e, ff63895521, ccb9b38dd8, 146876e75a, 9135feae97) through MSTR's committed commit-map,
  and put the new hashes in the ledger entry. Sign-offs verify blobs, and blobs do not change.
- The enable packet reaches the CRO ~15:00Z Monday, latest 18:00Z (CRO 102054, answered 19:57Z).

## I. Parked from the same ruling (call 1)

- "2.0.0_SA_COO~M validates" the Comparison/Multi-Comp permission. It waits on 2.0.0_SA_COO~Y versioning
  `templates.json` comparison_catalog after ~P's identity reads (4 read-only securities_info GETs) in ~P's next window.
