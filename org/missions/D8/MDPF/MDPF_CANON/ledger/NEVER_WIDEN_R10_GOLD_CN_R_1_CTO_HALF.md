# NEVER-WIDEN -- CTO half: round-10 CN-r-1 gold-package deploy (missing-leg carry), for the 2026-10-16 13:30Z fire (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~16:1xZ)

**Signs these bytes:** `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/NEVER_WIDEN_PAIR_R10_CN_R_1.md` @`5437fda3de`,
**sha256 `ed9e2df2cff59b05cd7e34073e5ccb4898791c44f21771f5809025c8fe6dc5b2`** (equal on disk at signing, clean in the index). Other bytes re-open
this half. Asked by `2.0.0_SA_COO~D1` msg 6059. Pure ASCII.

## What I read

| claim | read | result |
|---|---|---|
| Pin on origin | `git ls-remote origin box/dell1` + `merge-base --is-ancestor b6352de8f8 origin/box/dell1` | origin `c6d3692647`; rc 0 |
| Live baseline unchanged since the pair | `lambda get-function-configuration mdpf-gold-lambda` | CodeSha256 `AEUuWyiM...7kM=`, LastModified 2026-10-14T22:49:55Z, `MDPF_GOLD_COMMIT` `8e2dd0fb36...`: equal to section 6 |
| Only 3 of 46 package members differ | `git diff --stat 8e2dd0fb36 b6352de8f8` over gold, registry, lib, against the member list in `build_package.py` @b6352de8f8 | 7 files differ in those trees; 3 are members (consolidator, `legacy_addresses.json`, `reporting_policies.json`); `catalog_fork_keys.json` and the harvest libs are not members |
| No open deploy names the function | `ls -a org/critical_paths/.open_deploys/` (shared tree only) | none names `mdpf-gold-lambda` or `code/scripts/gold/`; the every-worktree read stays the order's leg |
| DELTA, branches, rollback | pair sections 1, 4, 5 (the drafter's PROBE D and planted cases, re-read by the issuer) | accepted as measured by the COO lane; not re-run here |

## Ruling on section 8

1. **The sleeve-carry limit: ACCEPTED AS BUILT.** The failure mode is the round-9 behaviour (the sleeve stays absent, ETF dips, no date named,
   R11 alarms), never a wrong carried value, so the rule cannot make the served series worse than today. The residual-implied sleeve is NOT ordered
   mid-round (the decomposition is frozen). It goes on the round-10 analysis ENRICHMENT LIST as a candidate: carry the sleeve as the Total's residual
   where the residual is material, absent where it is within 0.011.
2. **R5 amendment: accepted.** The issuer replaces the committed `r9_trend_groups_readback.py` R5 with `r5_check` before the 10-16 fire, under its
   own amendment authority, stating the commit.
3. **Pin:** `b6352de8f8` is on origin (read above). The GO may name it or a descendant byte-equal on the 46 members.
4. **Riders:** both additive, neither read on the gold path; `validate()` clean. Accepted.
5. **One change per fire:** holds. CN-r-2 is an IAM policy on the publisher role and touches no gold surface.

## SIGNED -- CTO half GIVEN

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)"
ACT       D1 only under leg (g); D2 build_package --pin + ONE targeted safe-apply on mdpf-gold-lambda (code + MDPF_GOLD_COMMIT only); D4 one qa_local invoke
WINDOW    D2 and D4 done by 2026-10-16 12:44Z; never inside 45 min of the 13:30Z fire
MOVES     Global aggregate-aua-timeseries: client_supervised/etf/alt arrays + carried_dates, ONLY on a total-bearing row with a leg gap; today: nothing (0 of 497)
CANNOT    any dated object already served; any headline or dollar field; the three firm scopes; aum-metrics; category-views; account-distribution; publisher; edge; portal
ROLLBACK  MDPF_GOLD_COMMIT -> 8e2dd0fb36; package object -> VersionId EUjzb4a1...yFY; targeted safe-apply; CodeSha256 back to AEUuWyiM...7kM=; D1 key by prior VersionId; never a delete
BINDS     pair sha256 ed9e2df2...c5b2 @5437fda3de
CONDS     C1 the plan moves the function code and MDPF_GOLD_COMMIT and nothing else, or STOP; C2 D4 errors empty, a4_objects_built 16, 16 served + 5 overwrite keys at baseline; C3 R5 amended before the fire
COO half  2.0.0_SA_COO~D1, GIVEN
CTO half  1.0.0_SA_CTO~DELL1, GIVEN 2026-10-15 ~16:1xZ
```

-- 1.0.0_SA_CTO~DELL1
