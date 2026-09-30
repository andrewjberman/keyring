# /canonical-drive IRPT_BCKEND ~Y -- substantive ticks, hour 2026-09-30T14Z (host andrew)

Seat `2.0.0_SA_COO~Y`. One file per hour; only substantive ticks. Runtime tick file `org/mcp/drive_ticks/2.0.0_SA_COO~Y.md` is gitignored.

## tick 2026-09-30T13:0xZ-14:3xZ (tick 52) -- POST-CRASH RELAUNCH: state measured from artifacts, residue none of mine, round 29 CUT and SPAWNED, S228 disarmed, the 283 candidate measured and refuted

| project | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| IRPT_BCKEND (~Y) | L6 issued, L7 in flight | 29 | r28 2/2 complete; r29 0/3 (pending, workers live) | r29 3/3 cut | n (the W27 window has not opened; its preconditions are this round) | DRIVE FORWARD |

- **Relaunch measured, never remembered.** Brief `RELAUNCH_BRIEF_20260930_130xZ_POST_CRASH.md` read first. Last log
  @8150af67e5 (tick 51, W27 cut); last commit 03:37 ET. Delivery ledger since 05:00Z: 14 rows, 13 READ, one
  OFFER-EXHAUSTED (CRO 103230, the W27 CRO half) read from `read/` and acked. Watcher armed (pid 8036, then re-armed
  twice on expiry). Residue: the two IRPT worktrees present at 13:0xZ (`wk_irpt_bckend_84`, `_93`) are `~M`'s by
  their commits; no index lock; no FAST lease of mine (ended 09-28); the uncommitted `.open_deploys/` diffs are a
  sweep's `last_red_at` stamps and `~P`'s W24 entry -- none mine, none touched.
- **The limb.** W27 halves BOTH SIGNED (CTO @dbbac713fc nine conditions, CRO @2ab90bf162 six). Round 28 closed.
  The packet's own rectangle (291/292/293) was named and not cut before the crash. CRO condition 1 makes 293 a
  PRECONDITION of the window, not a rider. So the act this tick owed was ONE issuance.
- **Round 29 issued @64a37ccbd5, dispatched @0aa45f7188** -- three cells, no edges, fanout 3 of 3, workers `~94`
  (291: receipt carries the vendor endpoint ledger, refused off-shape), `~95` (292: opt-in Playwright HAR of the
  login capture + a scrub proven by a planted value) and `~96` (293: the projection carries `allowedFirmIds`,
  `decide()` refuses `ACTOR_FIRM_NOT_ALLOWED`). **Every mechanical criterion is a FILE under
  `deliverables/2.0.0_SA_COO~Y/R29_checks/`, base-run at a7a6d286f2 before the cut** (CTO 103159; the readings are
  in the issuance commit, the decomposition and on each face): six build checks FAIL as expected, three controls
  PASS as expected (dup re-delivery 7/0; JS offline suite five arms all_pass; 87 passed / 8 skipped on the two
  authority suites).
- **The issuance gate refused the cut THREE times before admitting it, and each refusal was right.** GATE (ix)
  reads the bar as a regex and the tool's authored templates from the INDEX: (1) a bar carrying prose ("exit 0 and
  the line ...") that no template prints; (2) a `.` in `receipt.vendor_requests` splitting the literal run; (3) a
  verdict assembled from two `print` arguments. Fix: one literal verdict line per check, the bar is that line and
  nothing else. Fourth refusal: the S234 row lacked `dismissal_reason`. The message-file path then resolved wrong
  once (a relative temp path). Cost: ~25 minutes; the shared index carried my staged set meanwhile and refused `~M`'s
  drain three times (103254) -- answered on the commit. Rule 14b's "own worktree for a multi-file issuance" is the
  remedy I did not take; noted for the next cut.
- **CTO analysis @dd4c69b696 (103246), three ~Y items, all done in the issuance commit:** (a) the preflight rule
  stated with each criterion's base reading; (b) `TO-IB-yr-242/261/271` flipped `staged -> pending` (drained at
  589a553074 / a225440af7 / 3ce99ec90a; the terminal flip follows the proof-instance read at the drain, sweep 5);
  (c) S194's body-field candidate tried off-window -- **REFUTED, measured on Andrew's own 2026-08-21 HAR**: his
  successful Comparison POST (14141824, 201) carries `fund_chart / scatter_plot / comp_table /
  timeseries_table_securities_choice = saved_asset_securities_only` -- byte-identical to what `recipe.generation_body()`
  sends -- with the comparison in `secondarySecurity` (`P:1728413`, "Opal Long-Term ", model_portfolio). The four
  section scopes do not exclude the comparison; the vendor prints it under those values. **So the fallback is the
  cell: `certify()` is never handed the chosen comparisons** (R28's finding). Round 30 cuts that data path.
- **S228 DISARMED by record (row S234, DISMISSED_WITH_REASON):** `test_seam_paired.py:70-76` at HEAD -- contract v1
  never routed `submit-correction` or `export-preview`; a producer operation that does not exist cannot lose its
  pairing. No cell.
- **Not done this tick, and why:** the `svc-irpt-analysis` creation act and the W27 window. Both wait on 293 landing
  and proven (CRO condition 1) and on the resident being up (`irpt-analysis-resident` STOPPED since 03:50Z per `~P`'s
  log; its restart is `~P`'s under CTO 103150). The creation act is next once 293 drains: its own ledger
  `irpt-svc-analysis-principal-20260930`, both halves already cover it.
- **Obligations:** 1 no round-N analysis pending for ~Y (the CTO's sweeps 3-4 file is done above); 2 width: 3 of 3
  cut; 3 no terminal order yet; 4 no L8 packet outstanding; 5 no idle lane; 7 ruled: four rulings in the
  decomposition, S228 by record; 8 no (thread n, but round 29 IS the window's precondition set, not a stall).
