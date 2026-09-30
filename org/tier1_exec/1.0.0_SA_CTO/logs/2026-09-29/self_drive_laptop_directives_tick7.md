# /self-drive laptop directives -- ticks 6-7 (2026-09-29 01:28Z-01:58Z)

**archetype:** COORDINATE

Arming record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_230xZ_SELF_DRIVE_LAPTOP_FABRIC.md`
@`9549fd3b32`; cron `f02c52db`. **state: ARMED**

## Acts since tick 5

- **Ruling 102520 (~P):** ~E round 2 = every 49F account, full history from each account's first holdings day, the
  manifest counts, and `irpt-holdings-performance-daily` under its own ledger; the adapter switch (TO-IB-pr-201)
  serves only after that manifest reads complete.
- **Ruling 102522 (~D):** one shared holdings table with ground and totals as props -- Positioning dark with its own
  totals (byte-identical), IR light with producer-served totals only; F7-AC4 and C3 stand.
- **CVO told L8/L9 is unblocked** (round 19 terminal in ~M, ~P, ~Y; its summary had waited on m19-2 and pr-192).
- **Relay to site Z (1.0.0_SA_CTO~O, NFRA_OPLGTW OG-m-2b):** first answer "a NAMING_LEGACY_READS entry" corrected the
  same hour -- `legacy_read_ok()` binds Python AST sites only and naming-gate ENFORCE is live, so ~O (CTO lane by
  suffix) adds a `tf_local` read_context kind and the entry in a prior commit; this seat reads the diff.
- **Sign-off `2b3fc1c1a3`:** resident fe64236bbb-st2 -> st3 (TO-IB-yr-1), one writer of the job outcome, both
  branches; install after ~Y's four gates and the CRO half.

## Fabric movement read

- ~E: round 1 thread hop 1 built (49F account 0010498003, 184 of 184 YTD days, YTD 5.83%; 184 objects read at the
  builder prefix); round 2 built (`e29adc9fa7`, every 49F account).
- ~M: round 20 issued; the R4 flip order partially drained (`f5dfdc2b6f`).
- ~P: round 20 issued (TO-IB-pr-201); resident st3 built and uploaded.
- ~D: item 19 landed (shared tree map, Positioning byte-identical).

## State

14 of 42 measurable projects complete or closed; COO AT CAP; inbox 0. NOT DONE.

## Open calls at Andrew

Weight date (REC prior day); Schwab registration codes (UIC-16).

## Compiler Tools

- `aws s3 ls` (rail-checked, presence count only): 184 objects under the 49F holdings_performance_daily prefix.
- Gap: the naming gate's legacy-read carrier cannot bind a Terraform read (routed to ~O above).
