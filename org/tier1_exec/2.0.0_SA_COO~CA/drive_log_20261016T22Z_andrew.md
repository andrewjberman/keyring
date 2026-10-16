# /canonical-drive COMM_ASSIST -- 2.0.0_SA_COO~CA, laptop, 2026-10-16 19:5xZ-22:5xZ

**archetype:** MIXED

Round 21, cut on the CTO's ruling on call 446a (fix the missed @mentions in channel thread replies; one cell plus one retest).

| time (UTC) | act |
|---|---|
| 19:55Z | queued call `446a` (fix vs close with Teams alerts unproven); the CTO ruled (a) at 20:06Z @f418537712 |
| 20:4xZ | issuer check `r21/checks/check_n1_threads.py` written first (base 1 of 7; scratch reference 7 of 7); round 21 ISSUED @1ca38ef17f: CA-n-1 to worker ~32 (sparse worktree, haiku high) |
| 21:1xZ | worker report: AC1 7/7, AC2 7/7, AC3 FAIL (issuer's sparse set lacked `daily_reports/eod`, row W32-S4); row W32-S2 (a failing thread held its whole channel) ruled a defect: order amended @9552754dff, arm 8 `thread_failure_isolated` added (base 2/8, reference 8/8, worker build 7/8) |
| 21:2xZ | worker continued; issuer re-ran all three on the branch (8/8, 7/7+4/4, I2 64 passed, validator VALID) and merged @1aa63bde67 through `safe-merge.sh`; worktree and branches removed |
| 21:3xZ | CA-n-2 staged @f6d80f2b0b: COO half SIGNED, `check_n2_equiv.py` (pre-flight `ok=True differ=4 foreign=3 probes=17 same=17 n1=8 of 8` on the issuer's own pinned build), `check_n2_ledger.sh`; CTO half @314121c000 (adds C9), CVO~L half @e0df2cbf9b |
| 21:5xZ | GO @f0c0e87682; spawned `0.7.0_AE_CloudOps~COMM1` (rule 34, the COMM macro lane) |
| 22:13Z | applied by ~COMM1 (Branch A, 0/2/0); issuer's own live read `N2-LIVE ok=True n1=8 of 8 probes 17/17`; 13 `channel_poll` lines after the apply, max 12 calls, 0 failures |
| 22:5xZ | ~COMM1 complete (msg 109767): ledger CLOSED (`check_n2_ledger` PASS), instance VALID, order complete, on origin. Retest CA-n-3 queued as act call `laptop-20261016T222633Z-2396` |

## Issuer rulings

- W32-S2: a defect inside this round, fixed in CA-n-1 by amendment (a failing thread costs only that thread).
- W32-S4: the issuer's provisioning defect (sparse set); criterion unchanged.
- COMM_ASSIST-S4 (~COMM1): the deploy order omitted building `transcripts-pull.zip`, which a clean-checkout plan needs; accepted as
  the issuer's defect; the next deploy order of this root names it.
- The order's row-id form `COMM_ASSIST-C21D-S<k>` is refused by the row gate; the issuer's defect.
- Condition 8 (pinned-thread read): inferred from `failed=0`, not observed per thread; the retest reads it directly.

## State at the end of the hour

CA-n-1 and CA-n-2 complete. The round's real run is CA-n-3: a colleague's @mention posted as a reply inside an older thread is
recorded and reaches Andrew as a muse alert within 30 minutes (Andrew's act, call 2396). Reader read at 22:55Z: no mention yet.

## Compiler Tools

- `comp-find` (`channel_messages`, `mentioned_at`, `dev-bid`): worked; two calls ran past 300 s in the foreground and finished in the
  background.
- `safe-merge.sh` (fast lane, 0 violations), `wk-provision.sh provision|remove`, `proof-of-spec-check.py`, `open-calls.py add`,
  `unblock.py tick`: worked. `unblock.py tick` takes over 120 s on this box; run it in the background.
- Gap: a dated wait on a worker reads `owner-not-live` (workers never register), so it counts as empty.
