# SELF-DRIVE AMGT_FRIDAY -- tick 1 -- 1.0.0_SA_CTO~Z -- 2026-10-01 04:14Z to 04:33Z
**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md` @8f56ef5f81.
It was armed on the arrival of the CRO~Z brief (msg 27495, 04:14Z). The cron is session-only, firing at :43 hourly.
**Paired with:** `2.0.0_SA_COO~X`, `~Z`, `~D` and `~H`, each running `/canonical-drive <own project> 30m`, plus `~RV` (unchanged).

**state: ARMED**

## Scope

| project | COO | prd | ratified-text half | open TOs |
|---|---|---|---|---|
| AMGT_CORPUS | ~X (seated 04:2xZ) | v0.7 @7d73abbe0e | STALE, owed by CVO~Z | round 27 ac-2 not started |
| AMGT_HARVST | ~H (seated 04:2xZ) | v0.13 @7d73abbe0e | STALE, owed by CVO~Z | round 31: 3 of 3 terminal, close owed |
| AMGT_RESAPP | ~Z (seated 04:2xZ) | v0.31 @18c3f9c496 | STALE, owed by CVO~Z | round 55 ae-1 pending (the word was given 00:41Z) |
| DSGN_AMGTV1 | ~D (seated 04:2xZ) | v0.6 @b8c93f6342 | STALE, owed by CVO~Z | round 14: 7 of 7 terminal, close owed |
| ETFS_RIVALS | ~RV (live) | -- | -- | round 2 d-3 in flight |

**Completion test:** NOT DONE. 0 of 5 are `complete`; 5 REACHABLE. AMGT_HARVST is excluded from HELD-AT-STOP (R8).
**Sequence check:** 5 of 5 projects show no flags. No COO cap is ruled for this box; 8 COO lanes are live after
seating.

## Acts

| act | commit / receipt |
|---|---|
| Placement: re-seat four COOs (fan-out cap 3), order, rulings R1-R13; LIVE_ARMS row landed; 09-29 row struck | e18d3a4e6a |
| Seat ask to MSTR~Z; all four seated LIVE | msgs 27498 / 27501 |
| Shared CONTRACT (monthly chatter route on the mounted lead-panel template, percent units, server T-1 rule, one writer per surface) | b8c93f6342 |
| PRD addenda: DSGN v0.6 (FWD-21..24, FWD-3 RETIRED), HARVST v0.13 (FWD-11..15, closing condition), CORPUS v0.7 (FWD-12 amended, FWD-20..22), RESAPP v0.31 (FWD-32..35) | b8c93f6342, 7d73abbe0e, 18c3f9c496 |
| L4-R re-sign ask, 4 halves | msg to CVO~Z 04:30Z |
| `/closer trace` ask to CRO~Z; trace landed (7 hops; deployed API == HEAD) and it agrees with the CONTRACT | msgs 27500 / 27506, @02e42a9966 |

## Calls closed

- **R1-R13** are in the placement, section 4.
- **R13 was pitched to CVO~Z** (msg 27499). Verdict 27503 @52c8af1251: YES for the act, scoped to Security Analysis;
  NOT the DEV head as it stands, since 51 of its 177 commits lie outside SecurityAnalysis. It is in the ledger at
  `drive_pairs/ctoZ_AMGT_FRIDAY/VERDICTS.jsonl`.
- **ETFS_RIVALS W5-S24** (msg 27486): COO~RV's supersede-without-delete sits inside my signed half. No objection.

## Acts only Andrew can do (cited; for ~09:00 ET)

1. **Sign in to the Bloomberg Terminal on site Z** (his login).
2. **Give a standing word for the scheduled CORPUS re-pull** (vendor per-use word; CORPUS FWD-22 is gated on it).
3. **Approve a site Z residential arm for bbg/wsj/barrons/ft, if wanted** (vendor per-use word; R7).
4. **Approve recursive worktree removal** (human confirmation for recursive deletion).
5. **Rule on the PROD promote payload beyond Security Analysis** (CVO verdict 27503: his word does not name the 51
   other DEV commits).

## Compiler Tools

| tool | result | note |
|---|---|---|
| `sequence-check.py --project` x5 | PASS | 0 flags; no cap ruled |
| `prd-signoff.py status` x4 | WITHHELD x4 | ratified-text STALE (endpoint changes), brief auto |
| `safe-commit.sh` step-4 surface-manifest gate | REFUSED once, then PASS | header keys outside `PRD_HEADER.schema.json`; RETIRED FWDs must stay in `endpoint_outcomes` |

- **Gap found:** the `[WATCHER-EXPIRED]` re-arm line prints an unquoted path. On this device the path holds a space,
  so the printed command would split. I re-armed with the path quoted.
