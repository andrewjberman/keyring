# MDPF_SECHIST decomposition -- ROUND 5, enrichment (issuer 2.0.0_SA_COO~H1, dell1; cut 2026-10-09 ~16:4xZ)

**Status: ISSUED** in one issuance. **Cut on:** the CTO's round-4 analysis `org/missions/D8/MDPF/MDPF_SECHIST/ledger/ROUND_ANALYSIS.round4.md`
(msg 2828), PRD v0.3 (CVO sign @cc57bafcdb). Section 3 is the rectangle (items 1-4).

## The rectangle

| item | FWD | cell | order | worker | depends on | risk |
|---|---|---|---|---|---|---|
| 1 + 4 | FWD-9, FWD-1 | `SH-t-19` ONE batched repair: C-MMF to the daily-return field (level dropped from the pull; blank when null, never the level; seam test re-pointed; negative arm null -> blank -> filled), plus rows S1/W1-S1 (depth re-plan bound) and S2/W2-S1 (three gold suites runnable from the worktree root) | `TO-SH-t19` | `~18` | none | SERVED |
| 3a | FWD-7 | `SH-t-20` dated read of the 2026-10-12 11:00Z scheduled pull (replaces carried TO-SH-t18 / TO-SH-t12) | `TO-SH-t20` | `~19` | EVENT: that pull | SERVED |
| 3b | FWD-9 | `SH-t-21` dated read: the as-of 2026-10-12 money-market null served BLANK (replaces carried, void TO-SH-t17) | `TO-SH-t21` | `~20` | EVENT: SH-t-19 drained + both deploys + the as-of 10-12 run | SERVED |
| 3c | FWD-9 | `SH-t-22` dated read: the same day served FILLED on the as-of 2026-10-13 run | `TO-SH-t22` | `~21` | EVENT: SH-t-21 OK + the next run | SERVED |
| 2 | FWD-4, FWD-5, FWD-9 | deploys, not cells: SH-t-8 (as repaired) at site Z, then gold (SH-t-7 + SH-t-15 + SH-t-19) to `etf-positioning-producer` with R1's ONE IAM statement; both after SH-t-19 drains | halves `NEVER_WIDEN_HALF_REQUEST_SECHIST_{SH_T8_SITEZ,GOLD_LAMBDA}_DEPLOY_20261009.md` | -- | SH-t-19 | WORLD |

Numbering note: the analysis's "SH-t-17 and SH-t-18" are the carried orders; their round-5 replacements are SH-t-21/22 (FWD-9) and
SH-t-20 (FWD-7). Carried ids are never reused.

## R1 -- the gold pair's IAM statement (D1-W14-S1, REMEDIATION_v3)

ONE statement on `etf-positioning-producer-role`: `s3:PutObject` on `arn:aws:s3:::opal-data-etfs/bloomberg/etfs/silver/history_gaps/*`, the
prefix `lib/opal_naming.address("bloomberg","etfs","silver","history_gaps", ...)` builds (read: `s3://opal-data-etfs/bloomberg/etfs/silver/
history_gaps/as_of=2026-10-12/gap_record.json`). Applied in the gold deploy through `safe-apply` by 0.7.0_AE_CloudOps~DELL1; rollback
re-applies the prior policy; a plan showing ANY other IAM change is a STOP.

## R2 -- the four stale remediation rows (owner 2.0.0_SA_COO~H1)

- `MDPF_SECHIST-S1` and `MDPF_SECHIST-W1-S1` (one finding, two ids): CARRIED into SH-t-19 repair (3); clears at its drain on
  `PULLR-TESTS-OK` (`test_depth_plan_skips_exhausted_ticker`), and live when the first scheduled plan after the take no longer names
  2602335D / PFDE / PFOE a second time.
- `MDPF_SECHIST-S2` and `MDPF_SECHIST-W2-S1` (one finding, two ids): CARRIED into SH-t-19 repair (4); clears at its drain on `GOLD-SUITES-OK`
  (the three suites, worktree root, no env set-up).
- Round 5's packet closes each with the drain commit, or carries it with this owner and the condition above.

## Rule 24

Domain: analysis section 3, items 1-4. Subtraction: 1 -> SH-t-19; 2 -> deploy pair (not a cell); 3 -> SH-t-20, SH-t-21, SH-t-22; 4 -> R2
into SH-t-19. Remainder: none. State coherence: SH-t-19 moves no served value until the gold deploy; the pull change (level dropped) moves
no served value (today's gold ignores the column).

## Write sets

- SH-t-19: `integrations/bloomberg/pipeline/etf_daily_pull.py`, `integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py`,
  `data/etfs/scripts/gold/etf_positioning_gold.py`, `data/etfs/scripts/gold/test_etf_positioning_mmf_rule.py`, and the three gold suites
  `test_etf_positioning_{upgrade_forward,per_fund_asof,industry_group}.py`.
- SH-t-20, SH-t-21, SH-t-22: evidence only (read cells, spawned after their events).

## Edges and fan-out

SH-t-19 -> deploys -> SH-t-21 -> SH-t-22. SH-t-20 independent (event: the 10-12 pull).
`fanout: 4 of 4 cells cut; 1 chain spawned now (SH-t-19); SH-t-20, SH-t-21, SH-t-22 event-gated; cap 8`.

## Battery (every criterion dry-run at the base 2026-10-09 ~16:4xZ, each FAILS as expected)

`MMFR-TESTS-BAD not-passed=all three`, `PULLR-TESTS-BAD not-passed=both`, `GOLD-SUITES-BAD failing=all three (rc 2, 2, 3)`,
`FWD7-READ-BAD no-scheduled-manifest-since 2026-10-09`, `FWD9-BLANK-BAD no-scheduled-partition D=2026-10-12`,
`FWD9-FILLED-BAD no-null-on-D-to-fill D=2026-10-12`. Control for `r5_fwd9_read.py`: `blank 2026-10-08` reads SALXX 0.0097 / FXFXX 0.0104
in history (the served 1D reads 0.0097 for SALXX) and returns BAD `no-null-on-D` -- the organic branch reads as itself.
