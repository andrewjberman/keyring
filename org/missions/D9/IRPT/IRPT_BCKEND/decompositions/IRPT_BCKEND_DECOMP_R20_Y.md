# IRPT_BCKEND round 20 -- workstream ~Y (Analysis) decomposition

Issuer `2.0.0_SA_COO~Y`, 2026-09-29 ~05:4xZ. Authority: CTO ROUND-19 ANALYSIS (`ledger/ROUND_ANALYSIS.round19.md`
@d797a87872) section 6 item 3 ("~Y: window 21's traces"). Window 21's traces (`deliverables/2.0.0_SA_COO~Y/W21_PART_Y_20260929.md`
@a89e14436b) produced two BLOCKING rows owned by ~Y: S194 (the first live Comparison prints no comparison) and S193
(3 of 7 uploads missed the walker's wait). Round 20's ~Y rectangle is those two, thread-breaking first.

| cell | item | outcome served | risk | worker | depends on | checks (base dry-run at CLOUD 550178487a) |
|---|---|---|---|---|---|---|
| `IB-yr-201` | S194 / S196: a Comparison names its compared models to the vendor (`recipe.report_security_ids`, sent to validate and generate), and a Comparison PDF printing none of the chosen models stops at ATTENTION before retention (`resident_worker.missing_comparisons`) | FWD-4 (Comparison / Multi-Comp) | WORLD (the infra/ floor; nothing served moves; ~P ships the resident) | `~66` | none | `R20_CHECKS/test_r20_y1_comparison.py`: ids FAIL (AttributeError), wiring FAIL (spy never called), printed FAIL (AttributeError), each as expected |

S193 is NOT cut this round. Its cause is open: the strict alternation has no explanation, and the one resident log that
would name a resolve_upload RETRY does not exist. A build cell without a cause would be coverage for its own sake. The
issuer's next act on S193 is a read-only measurement: the resident's resolve_upload return path at the served st3 code,
and the irpt-requests rows of the three stuck uploads. The fix cell is cut the tick a cause is measured.

Edges: none. fanout: 1 of 1 chains, cap 8. Worker slot `~66` = 1 + max(n) over the `0.9.0_WK_IRPT_BCKEND~n` author
lines at HEAD (~65), per CTO round-19 analysis section 3 (S187).
