# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-05 00Z-05Z (ETFS_RIVALS, FULL)

Row: project | limb | round | TOs | cells | thread | act.

## 00Z-02Z
| ETFS_RIVALS | L7 round 8 A+B (built; drain held) | 8 | 9/9 | 9/9 | y | NO-OP x3 (event-gated): drain waits on the 07:00 ET vehicle pull |
## 02Z-03Z
| ETFS_RIVALS | L7 round 8 | 8 | 9/9 | 9/9 | y | DRIVE FORWARD: Andrew-direct records -- drop MTD (@575e7d7250), "Data available since" + IDVZ/PFOE backfill + one-day incremental (@a36e70f335, daily jobs measured incremental), benchmarks ACWI/IWM + clickable tickers + ETFClassifier (@41158af7f9), CTO~Z adjudicates while AFK, 3-year cap (@357e681ddf); CTO~Z PRD v0.15/v0.16/v0.17; rn-1 amended (b11bead42b) and rebuilt; lg-1 amended (25ff7f18e7) and rebuilt (SCHY rival) |
## 03Z-04Z
| ETFS_RIVALS | L6/L7 round 8 C+D | 8 | 11/11 | 11/11 | y | DRIVE FORWARD: WCMG traced (no data before 04-23; CTO~Z ruled accept, msg 29453); ACWI/IWM budget ruled (1M rows, msg 29445); workstream C fc-1 issued @b98cc6d13d and built; workstream D su-1 (gold security_universe) issued @c81854cd9f and built; laptop CTO answered (msg 29471) |
## 04Z-05Z
| ETFS_RIVALS | L7 round 8 (all built) | 8 | 11/11 | 11/11 | y | DRIVE FORWARD: integration of 8 branches: suite 647/0, 18/18 checks PASS; fc-1 AC2 added (@cfd99b593f) and built (47cc8c81ae); runbook in STATUS.md (a2f2b4b4f9); drain cron re-cut |

## Compiler Tools
- comp-surprise, comp-schedule: not re-run this window (no new round cut needed a census).
- comp-find rail refused piped census receivers; native Grep used instead.
- lib.opal_naming address(): accepted security_universe (no registry row needed).
