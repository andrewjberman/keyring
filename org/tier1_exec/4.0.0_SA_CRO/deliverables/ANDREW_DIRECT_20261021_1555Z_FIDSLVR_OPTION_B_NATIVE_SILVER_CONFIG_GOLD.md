# ANDREW_DIRECT 2026-10-21 ~15:55Z -- NFRA_FIDSLVR: Option B (native silver + config-driven gold)

- Channel: in-session, Claude Code terminal, dell1, to 4.0.0_SA_CRO~FIDELITY. ~15:55Z (11:55 AM ET). A ruling on the A/B discussion.

## Verbatim
> Yse lets go with B here

## The ruling (what B selects)
Silver is **custodian-native and lossless** (Fidelity silver carries Fidelity's own fields from bronze). A **matching config / canonical
dictionary** holds the conforming logic (custodian field -> canonical gold field + transform + approximate-match notes). **Gold** is
constructed from that config (union + attribute). The canonical gold schema is **seeded from the Schwab silver layout**. Rejected: Option A
(conform-at-silver), which would strand Fidelity-only richness (household Groups -- Schwab has NO such table in silver OR bronze, measured)
and bake possibly-wrong field equivalences into the durable layer.

## Consequence for the endpoint
FWD-1 and FWD-2 move their proof point from SILVER to GOLD (a reader runs unchanged against the Fidelity-derived gold). Same spirit; the
CTO re-cuts those two. The rest of the DONE WHEN lines (FWD-3..7) stand -- FWD-5 (gold by config) and FWD-7 (native-id attribution)
already assume B. Context behind the fork: the CRO discussion (this turn) and the .fam measurement.
