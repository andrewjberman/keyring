# SIGN-OFF (1.0.0_SA_CTO half) -- the Performance adapter reads 49F from the holdings-basis gold; the engine read retires

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_HOLDINGS_GOLD_49F_20260929.md`
@`bdc080a0a1`, blob `189aaef213dd77848572f60d47960b1949e2a39d` (2.0.0_SA_COO~P msg 102578). **Signed:** 1.0.0_SA_CTO,
2026-09-29 ~04:2xZ. The 4.0.0_SA_CRO half is asked separately. Ledger `irpt-adapter-holdings-gold-49f-20260929`.
Ordered by PRD v0.19 rulings 10 and 12; weights per Andrew-direct `a9b5489af6`.

## Signed, as the packet reads it

- **Three surfaces, one act:** adapter `qfxZ0DzB` -> `qosuSxAf` (census 69 -> 70, `holdings_gold.py` added, four
  named members); the adapter role policy's List/Get move from `twr_daily` to the builder's
  `irpt/49financial/gold/holdings_performance_daily/`; the 49F bucket fence's adapter allow-list moves the same way,
  `DenyForeignFirmPrincipals` unchanged. Plans: performance 0/2/0, shared-infra 0/1/0.
- **Precondition met:** ~E round 2's manifests complete (557 of 557 days); applies only after window 21 closes.
- **Writers 1, readers 2** (compute and retained reopen), branches A-F as tabled. Cottonwood and Inflection unchanged.

## Read at signing

- The period figure links status-OK days and discloses the rest as PARTIAL; no missing day is filled with zero or
  rolled forward (FWD-12 ACCEPT).
- The apply gap (performance root, then shared-infra, same minute) refuses by name; no figure is wrong in it.

## Conditions of this half

1. **The rollback branch is READ, not predicted.** After the switch, an account's accepted pointer can name an
   OPAL_HOLDINGS report. Before the apply, measure what `qfxZ0DzB` does when it reopens an OPAL_HOLDINGS retained
   report (a fixture on the live zip's own members, its schema lacking OPAL_HOLDINGS), and write the outcome into the
   ledger. If it is anything but a named refusal or a correct reopen, the rollback also restores each written pointer
   to its prior accepted revision, and the ledger lists them.
2. **Latency:** the after-invoke's real Since-inception answer (557 partitions) prints its wall time; at or over 80% of
   the 60 s timeout it is a rollback, not a pass.
3. The CRO's BEFORE and AFTER reads as section 3 names them; D1 closes only on both.
