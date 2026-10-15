# ANDREW-DIRECT 2026-10-15 ~16:2xZ -- the demo Global Trend uses the staff (Variant 1) code; ride the next portal PROD promote

**Channel:** the `1.0.0_SA_CTO~DELL1` terminal. **Recorded by:** `1.0.0_SA_CTO~DELL1`, same turn. **Answers:** open call
`dell1-20261015T160309Z-33fe` (row MDPF_CANON-D1-S29, CVO `ADJUDICATION_v17.md` D1-C-S90).

## Verbatim, in order

> "I just checked PROD and I dont see any spikes displaying visually."

> "I just checked the trend view for each partner and I dont see any spikes there either"

> "Ok let's just make the Demo View see the same thing as the global view when it comes to this issue, just use the same code as global view, i
> think that would be easier."

> "Because its not in production for anyone, its not high urgency, but it should get added on to the next prod promote of the portal."

## What it settles

- **Reach (measured by this seat, portal origin/PROD):** Variant 2 of the Global Trend is reachable only by a non-internal login whose firm is in
  `MDPF_GLOBAL_VIEW_FIRMS`, which is `['demo']` (`src/pages/ModelPortfolios.tsx:300`, `:389`, `:406-410`). No partner firm reaches it. The
  carried-row roll-forward that overdraws (`src/lib/trendGrouping.ts:241-248`, band set only `pre` at `:228`) is real code, demo-only.
- **Remedy (his choice):** a demo Global session uses the same Trend code as the staff Global view (Variant 1). Variant 2 is not repaired for this.
- **Timing:** not urgent. It lands on DEV and goes out with the next portal PROD promote. No separate push.
- **Owner:** `2.0.0_SA_COO~D1` (MDPF_CANON). D1-S29 disarms on the change at DEV, and is graded on PROD at the promote.

-- 1.0.0_SA_CTO~DELL1
