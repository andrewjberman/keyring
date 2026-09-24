# ANDREW-DIRECT 2026-09-24 ~18:1xZ (~2:1x PM ET) -- C11: the P/M/Y goal loops read a FAST lease on IRPT_BCKEND

**Channel:** the `4.0.0_SA_CRO~A` terminal, in reply to this seat's recommendation (~18:1xZ).
**Recorded by:** `4.0.0_SA_CRO~A`, same turn, at 18:13Z by the system clock.

## Verbatim

> Yes agreed, do it

## What he agreed to (as recommended)

The IRPT return brief's gap G2
(`IRPT_CLOSER_TO_CANONICAL_RETURN_BRIEF_20260924.md` section 5): `2.0.0_SA_COO~P`, `~M` and `~Y` run `/goal-set`
20-minute loops that never read a lease. So they keep blast-mode freedoms when Andrew is away, while `2.0.0_SA_COO~D`
drops to FULL.

The fix, written as C11 in report 2 section 14:
1. **One FAST lease on IRPT_BCKEND names all three seats, each with its own backend surface.** Today
   `.tools/drive-mode.py` holds one seat per project, so it gains a multi-seat form with pairwise-disjoint surfaces.
2. **Each seat's goal loop reads the IRPT_BCKEND lease at the start of every tick** (a `/goal-set` change):
   - **FAST:** today's blast-mode freedoms. The seat lands on DEV itself, the CVO grades after landing, and the search
     rail is stood down.
   - **FULL:** the seat keeps working, under the closer contract's normal checks. The CVO grades each change before it
     counts, and the CTO lands DEV candidates.
   - **HOLD:** the seat pauses.
3. **The lease extends with Andrew's presence** exactly as `~D`'s does (call 5's hook), so all four seats change pace
   together.

Owner: `1.0.0_SA_CTO`. The surfaces are the CTO's to set from each seat's STATUS write claims; this record names none.
