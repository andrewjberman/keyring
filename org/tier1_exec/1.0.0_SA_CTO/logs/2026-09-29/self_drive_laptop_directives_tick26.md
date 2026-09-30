# /self-drive laptop directives -- ticks 25-26 (2026-09-29 10:32Z-11:27Z)

**archetype:** COORDINATE

Arming record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_230xZ_SELF_DRIVE_LAPTOP_FABRIC.md`
@`9549fd3b32`; cron `f02c52db`. **state: ARMED**

## Incident: the 49F adapter switch regressed the served page and was rolled back

- 10:14Z/10:17Z: `hD7G6YT1` served (both halves). 10:26-10:50Z: the CRO's AFTER walk found every 49F YTD/1Y answering
  UNEXPECTED -- `ModuleNotFoundError: parity_period_returns` (104 log events). Cause (CRO, pinned): `_holdings_source()`
  dropped `_engine_source()`'s runners_49f sys.path insert while `f49_engine.ruled_period_for` still imports it lazily;
  since-inception short-circuits before the import, so the cold start and the SI answer passed.
- 10:56Z this seat ordered the same-turn rollback; ~P had already rolled back (10:58-11:00Z, ledger CLOSED @9e0bde13e3);
  MSTR measured qfxZ0DzB live (a false [STUCK] from this seat: ~P was in a long turn). CRO rollback read: live equals
  BEFORE, 0 UNEXPECTED of 31.
- **This seat's miss:** the all-accounts served census it required was computed by running the adapter's rule offline,
  not through the deployed Lambda. The re-ask now needs the census through real deployed invokes, a read-back that
  exercises a ruled period, and the adapter-code census with the runners directory absent (CRO). The 49F re-switch
  ships alone; INF is a separate act.

## Acts

- 901 no-OK-row refusals read: empty accounts, not cash-only (ruling 3 holds).
- z09 -> cottonwood scopes row routed to the CRO lane, landed @de56cfd02f; TO-IB-er-401 given its go; the stale alias
  note corrected (6dcd6df254).
- Portal PROD hotfix widened to 6c163889 + 27eae57a (both additive contract readers), still Andrew's word.
- Sign-off `efaf1a8327`: HoldingsSnapshot CATEGORY contract in its two validators, with the read-back exercising the
  changed validation path.

## State

14 of 42 measurable projects complete or closed; COO AT CAP. NOT DONE.

## At Andrew (acts only)

- The word for the portal PROD hotfix of 6c163889 + 27eae57a.

## Compiler Tools

- The CRO's walk, not a census, caught the regression: a served-path read is the instrument; a rule run offline is not.
