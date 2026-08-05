# ANDREW-DIRECT — instruments cleared, cycle-4 ratification proceeds, v6 next

**Received:** 2026-08-05 ~00:2xZ, Andrew at the `1.0.0_SA_CTO~B` terminal. **VERBATIM:**

> "Comp-cochange and comp-heat are good to go, please make sure they are both ready to rock
> (officially registered through comp-tool canonical registration). Cycle-4 Ratification should
> be able to proceed. Then can look into v6"

**Surfaced scope (not adjudicated):**

1. **Both Friction instruments cleared by the sovereign** — this discharges the Phase-0 sequencing
   gate he set ~20:0xZ 2026-08-04 (*"wait for me to provide input until we totally lock in/dial
   comp-heat and comp-cochange"*). Readiness verified by EXERCISE, not registration-read (below).
2. **Cycle-4 ratification proceeds** — the RCG Cycle-4 Execution Policy addendum +
   MIGRATE/layer-refactor spec (both CTO~B-reviewed PASS 212158Z) are cleared to move. Under the
   policy's own s.2 this authorizes ratified batch execution; nothing executes outside a RATIFIED
   batch row.
3. **v6 after** — the v6 uncertainty band (172 files @465f15ce) is the next item at his attention.

**Readiness verification performed this turn (exercise-grade, per Rule 22a):**

| Check | comp-heat | comp-cochange |
|---|---|---|
| On disk + git-tracked | YES | YES (engine `comp_cochange.py` tracked) |
| Canonical registration (`tools_index` + coverage-map, gate-enforced) | registered | **born-registered**, `status: canonical` |
| `comp-manifest-check completeness` | **PASS** — registration-invariant 88 executables all accounted; routable + placement + self-routes + existence PASS | same run |
| Resolves bare on PATH | YES | **WAS NOT — FIXED** this turn (`provision-path-shims.sh`, 96 tools x2 forms) |
| EXERCISED (ran, read output) | `freshness --json` on a live tree: `half_life_days` declared, `summary.mean_score`, per-path `score` — the exact F2 scores-only contract | `--self-test` 7/7 + 4/4 + substrate smoke; live `matrix --since "2 days ago"` returned pairs w/ shared_files, jaccard, both denominators, HEAD anchor |
| Curated directive entry (`comp-tools.yaml`) | present | **ADDED** this turn (@69e800bbd; two-phase override discharged @02d3cb1c3) |

**The one real readiness defect found:** comp-cochange was canonically registered and gate-PASSING
while **not resolving on any agent's PATH** — the registration invariant scopes to tracked+committed
disk presence, not shell reachability. *A tool can be fully registered and unreachable; the gate
cannot see the difference.* Fixed; both now exercise bare.
