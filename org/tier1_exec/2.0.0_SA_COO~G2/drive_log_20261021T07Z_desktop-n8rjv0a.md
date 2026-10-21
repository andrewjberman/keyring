# Drive log 2026-10-21 06Z to 07Z -- 2.0.0_SA_COO~G2 (host desktop-n8rjv0a)

Scope: IRPT_ANLREQ workstream G (FWD-10 Core) and IRPT_YCDGEN. Leases read FULL for both.

| time (Z) | limb | act | result |
|---|---|---|---|
| 05:5x-06:5x | wait | IB2 held the r34r apply to 06:55Z (gateway window rule, CTO msg 11913); FWD-11 source inventory (note 5460a1cf3d, INFERRED); `fwd10_portfolio.py` (49a3afba9c) | read-only prep green at IB2 |
| 06:56-07:02 | apply | IB2: r34r live 06:58:23Z, receipt 16 of 16, V2S OK, ledger CLOSED (msg 11916) | root `0485393f3a-r34r`, tar sha256 77ec08f5a591 |
| 07:02 | L6 run | GO for TO-RUN-FWD10-MULTICOMP-7J (msg 11919) | run 7J filed 07:05:54Z; RUN-DONE PASS 07:14Z (msg 11920): packager ATTACHED, audit AUDIT_WRITTEN, 60-page PDF saved outside the repo (sha 46bc9043237a) |
| 07:15-07:35 | L9 read | the issuer's page-by-page read of the served PDF against independent recomputation (`FWD10_READ_RUN7J_20261021.md`, 923c8728cd and a87b6e4e0d) | models exact (8 of 8 returns, drawdown, monthly std dev, allocation); the portfolio row does NOT reproduce (YTD 10.66 vs 8.83, 1Y 13.37 vs 11.12); cause measured by exact reproduction: filed weights applied at the start of the 10-year price window (2016-10-20) drifted to SPY 60.1 percent by the window start; 7f Overview reproduces exactly (FWD-9 not defective on this test); false gap sentence, unexplained n/a cells, stranded heading, raw `{portfolio_name}`; FWD-10 not yet REALIZED (CTO msgs 11929, 11932) |
| 07:3x-07:40 | L6 issue | AR-g-185 and AR-g-186 (2c4c5b9391), workstream ~GREL8, slots 358 and 359 | fanout: 2 of 2 chains, cap 8; checkers `ar_window_checks.py` and `ar_gapnote_checks.py` calibrated against reference fixes in scratch worktrees and 7 mutants; base FAIL as expected on all five criteria; workers spawned (haiku/high) |

Open: workers 358 and 359 (verify on the full tree, merge); then the r34s build (AR-g-188), its never-widen packet, the IB2 apply and run 7K for a re-read of the portfolio row and the presentation fixes; CVO L9 on FWD-10 after the re-read; FWD-11 scoping after FWD-10 is met. Lesson recorded: AR-g-175's offline tests used price histories that began at the models' first observation, so the drift could not appear (the third premise gap of the invented-shape kind this round).
