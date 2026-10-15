# ANDREW DIRECT -- the replacement's longest-history rule is approved "as an additional qualification" (2026-10-14 ~18:5xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `4.0.0_SA_CRO~DELL2`. He was answering this seat's question after the C-SWAP
provider QA (@30ceaa97fa). The question was how Opal picks the replacement after Kimi K2.6 identifies and classifies an unknown holding:
- **(a)** the ETF in `etf-classifications` with the same asset class and sub-class that Yahoo prices with the longest history (this seat's
  recommendation); or
- **(b)** a short proxy list per sub-class that he approves.

**Verbatim:**

> Yes longest-history is fine as an additional qualification

## What it sets (surfaced, not adjudicated)

- The longest-Yahoo-history rule is approved.
- He calls it an "additional qualification": a test applied on top of the class match, not the only basis.
- This seat's reading is that the replacement is chosen in three stages:
  1. the same asset class and sub-class in `etf-classifications`;
  2. priced by Yahoo;
  3. the longest history among those.
- Whether "additional" also means the rule ranks the model's own proposals (when they pass the class match and the Yahoo check) is not
  stated. The owners read it, or ask him once.

## What it touches

- IRPT_ANLREQ FWD-2 / C-SWAP, steps 3-4: the deterministic proxy. No designated-proxy table exists.
- The QA findings, `SWAP_QA_20261014/SWAP_PROVIDER_QA_20261014.md` item 3.

-- recorded by 4.0.0_SA_CRO~DELL2
