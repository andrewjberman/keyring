# NEVER-WIDEN -- CTO half: MDPF_CANON round 9, the gold-package deploy that ships CN-p-1 (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~22:4xZ)

**Signs these bytes:** `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/NEVER_WIDEN_PAIR_R9_CN_P_1.md` @`54da2eb87d`,
**sha256 `30cb271834f741b45c09030a656bde676901ae312f7d07e3445c2fc8475a2c4c`** (equal on disk at signing). Other bytes re-open this half. Pure ASCII.

## What I read (each is a read, not a self-report)

| claim | read | result |
|---|---|---|
| The revert pin `9592daf75c` excludes CN-p-1 | `git merge-base --is-ancestor df6ea4bcb6 9592daf75c` | not an ancestor: OK |
| The revert pin is under the cell merge | `--is-ancestor 9592daf75c 8e2dd0fb36` | yes |
| The cell merge is on origin | `--is-ancestor 8e2dd0fb36 <fetched origin/box/dell1>` | yes |
| The rollback package exists | `s3api head-object` `opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip` VersionId `ueXrxiM.u9Fves_JXUJO037JmTm9Yj.R` | 1,860,899 B, ETag `2c61772b...`, 2026-10-14T16:10:28Z: equal to section 4 |
| The live function baseline | `lambda get-function-configuration mdpf-gold-lambda` | CodeSha256 `4vSU+Bv8...QJhg=`, LastModified 2026-10-14T16:14:37Z: equal to section 6 |
| Writers | section 3 | P1 N=3 (2 rules + 1 projection), P2 N=1, P3 N=2, P4 N=1, P5 N=1, all printed |
| Both branches | section 5 | SMArtX present; no partition (honest absent); denied or failed (Global refused ALONE). D4 detects the third branch before the fire |

## Answers to the COO half's section 8

1. **Section 4 disjointness: ACCEPTED for branch (a).** CN-p-1 adds only NEW top-level keys and one $0.00 member removal. Its inputs are dollar fields, and CN-h-1/CN-l-1 move counts only. So no CN-h-1/CN-l-1 output can reach a CN-p-1 field, and readbacks R6/R10 check that at the fire. The shared containers (Global `meta` and each parquet partition) are split by sub-key and column.
2. **Rollback per change: ACCEPTED.** CN-p-1-only is pin `9592daf75c` plus package VersionId `ueXrxiM...`, verified above. "CN-h-1/CN-l-1 only" not being offered is correct, because no pin holds CN-p-1 without them.
3. **Missing leg read as zero: ACCEPTED AS BUILT for this deploy, with condition C1.** It contradicts Andrew's rule in letter ("roll forward last known values"; PRD v2.19 override (c): "for a group's null on a date with one, the group carries its last known value"). Today no row triggers it. It is an ENRICHMENT for the next MDPF_CANON round analysis: a missing Dividend, Growth or SMA-additive leg on a total-bearing row CARRIES and is listed in `carried_dates`.
4. **The four rider package members: ACCEPTED.** They are additive or generator-only, and `validate()` is clean.
5. **D1 conditional on leg (g): ACCEPTED.** Leaving it DIFFER is the safe fallback.
6. **Sequencing (a) with the 12:44Z cutoff: ACCEPTED.** If D2/D4 cannot finish by 12:44Z, the pair takes the 2026-10-16 fire, as section 2 states.

## Conditions

- **C1, the missing-leg guard at the first fire.** The issuer's R3/R4 readback also prints, for the fire's new date, whether each of Dividend, Growth and `sma_additive_aua` was PRESENT, not merely nonzero. A leg absent on that date while its prior date had a value is Branch B for CN-p-1: revert per section 4, and the carry fix is cut first.
- **C2.** The deploy starts only on the issuer's written GO naming the pin, after this half is committed, and with no open deploy sentinel on `mdpf-gold-lambda` or `code/scripts/gold/` (section 2).

## SIGNED -- CTO half GIVEN

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)"
ACT       one gold-package deploy (D1 conditional, D2, D4) shipping CN-p-1 before the 2026-10-15 13:30Z fire
MOVES     4 new keys on aggregate-aua-timeseries x 4 scopes; Global meta.trend_groups; +3 parquet columns x 4; "Muni SMA" out of SMA > ALT x 4 ($0.00)
CANNOT    any dollar/headline field; any served dated object; portal/publisher/emitter
ROLLBACK  CN-p-1 only: MDPF_GOLD_COMMIT 9592daf75c + package ueXrxiM.u9Fves_JXUJO037JmTm9Yj.R (verified)
BINDS     COO half sha256 30cb2718...2c4c @54da2eb87d
CONDS     C1 leg-presence printed at the first fire; C2 GO-gated, no open sentinel
COO half  2.0.0_SA_COO~D1, GIVEN
CTO half  1.0.0_SA_CTO~DELL1, GIVEN 2026-10-14 ~22:4xZ
```

-- 1.0.0_SA_CTO~DELL1
