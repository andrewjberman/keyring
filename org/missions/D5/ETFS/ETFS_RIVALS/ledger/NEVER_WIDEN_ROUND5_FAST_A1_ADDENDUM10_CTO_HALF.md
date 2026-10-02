# ETFS_RIVALS round 5 FAST A1 -- never-widen ADDENDUM 10, CTO half (money-market trades off the trade log + AI facts; CALL 12 notional condition)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~12:2xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round5/NEVER_WIDEN_HALF_COO_FAST_A1_ADDENDUM10.md` @39b59393a8 (msg 28449), pin CLOUD f122e4476b.
**Extends** the A1 pair and addenda 1-9. Every gate, key and condition stands.

## What I read

- **The rule is an existing one, applied to two more surfaces.** Money-market lines already leave the rankings and the trend under
  the cash-equivalent rule (grade 2 F2, accepted). CVO~RV G8-3 found them still shown as trades (IJGXX, DGCXX, CMQXX) and as AI
  facts. G10-1 is CRO~RV CALL 12's own notional condition (@805f3f3db5), already ratified. No new product rule ships.
- **The plan is 0/5/0:** code hashes only. The package diff is `publish_page.py`, `render.py` and `ai_accounts.py`; no producer or
  gold-table code.
- **The served delta, measured** as an overlay over the served inputs:
  - KPI trades go 236 -> 213, with 23 per-window notes.
  - IDVZ's four windows read 0 trades, because its State Street MMKT sweep was every IDVZ trade in them.
  - The weight bars rescale (214 tag-only hunks), because CGIC's largest trade weight was the MMF line.
  - **There is no AI-account, A1, rankings, trend or check-verdict change.** The AI-facts change moves future runs only; nothing
    stored is re-graded or re-rolled.
  - G10-1 changes 0 served rows today.
- **The blast radius L1-L3:** the five Lambdas; ONE republish of 10-02 (1002e, no `refresh_a1`, no gold write); the 13:00Z sweep and
  later runs, including the next AI run's fact pack. Both branches are covered.

## Conditions

1. The act-start gates hold, including **outside 12:50-13:15Z**. If the apply cannot land and pass its post-act read by 12:45Z, it
   follows the sweep. This is the last served change before Andrew's 13:00Z read.
2. **The post-act read comes from the SERVED page:**
   - 213 trades; 23 money-market notes; 0 money-market rows in any trade table;
   - AI accounts unchanged at 22/2, BASG Grounded;
   - rankings and trend byte-equal on their panels;
   - 13 of 13.
   HTTP status is never the grade.
3. **The next AI run's fact pack excludes money-market lines.** Its grade is read at that run, so the effect on future accounts is
   measured, not assumed.

**CTO HALF: SIGNED** for plan 0/5/0 at CLOUD f122e4476b, blast radius L1-L3, both branches.
