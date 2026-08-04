# ANDREW-DIRECT — Global-scope T+2 lag solution: interim roll-forward, overwritten by real values

**Channel:** Andrew-direct, CTO terminal, 2026-08-04 ~17:15Z (~13:15 ET).
**VERBATIM:**
> "Also I have a better idea for 'Cottonwood'. Here is the issue, 49 Financial and Inflection
> are both reliably T+1, but Black Diamond, which is the Cottonwood data sources, is for all
> practical purposes T+2. The issue that we're encountering is that we don't know how to
> aggregate the 'Global' Scope aggregate-aua-timeseries.json and aum-metrics.json with that
> lag. Here is my solution: We just roll forward the last day's value as an interim solution
> and that is overwritten by the real value as it comes in. This keeps everyone in the same
> time period. This change would have to be managed in both the 'Global' aum-metrics.json,
> account-distribution.json, and aggregate-aua-timeseries.json. Let's get it scoped by
> 0.4.0_DS_ClientPlatform and I will bring in 0.5.0_AE_OpalETL to handle the cloud
> implementation."

## Scope as surfaced (CTO read; his phrasing is the ruling)

- **Problem:** 49f + inflection are reliably T+1; Black Diamond (cottonwood's source) is
  effectively T+2 — the Global fold cannot aggregate a common frontier without either lagging
  everyone to T+2 or stripping cottonwood from the tail.
- **Ruling:** the Global scope ROLLS FORWARD cottonwood's last real value as an INTERIM value
  on the lagged date(s); the real value OVERWRITES it when it arrives. Everyone stays in the
  same time period.
- **Surfaces:** Global `aum-metrics.json` + `account-distribution.json` +
  `aggregate-aua-timeseries.json` (his enumeration).
- **Seats (his naming):** design scoping = **0.4.0_DS_ClientPlatform**; cloud implementation =
  **0.5.0_AE_OpalETL** (Andrew brings them in himself — no spawn from the fabric).

## Two interactions with existing law (SURFACED, and dispositioned by the plain reading)

1. **The spine contract's no-LOCF rule (§2.1, canonized this session):** honest-None / no LOCF
   was ratified for PER-FIRM artifacts (the $107.2M false-dip class — absence rendered as a
   value). This ruling is a **sovereign refinement scoped to the GLOBAL FOLD**: a roll-forward
   that is (a) explicitly MARKED interim in the artifact, and (b) OVERWRITTEN by the real value,
   is not the false-dip class — it is a declared carry, the same family as the already-ruled
   cottonwood carry-window machinery (`gate_policy.per_partner_max_lag_trading_days`) and the
   CARRY-IMPORT leg class. Per-firm artifacts stay honest-None; the Global fold carries,
   marked. **DS's scoping states the marking mechanism explicitly** (pointClass /
   provenance field naming carried dates + which firm + overwrite semantics), so a reader can
   always tell interim from real.
2. **The 1646Z frontier edict (Global displays the complete-data frontier):** the plain
   reading — the FE clamp is the IMMEDIATE fix and stands; this roll-forward is the DURABLE
   data-layer fix that makes the clamp naturally non-binding (with the carry, the Global
   frontier is always complete at T+1). The edict's deploy gate is unchanged; when the
   roll-forward ships, the clamp simply stops clamping. If Andrew intends the roll-forward to
   REPLACE the clamp instead, his word says so — not assumed.

## Routing (same turn)

- Scoping ask -> 0.4.0_DS (Andrew-named seat) via COO, folded into the MDPF_CANRTE program
  frame (it is a Global-fold L3 contract item; W1 binding rows carry per-firm lag declarations
  naturally). Sequencing relative to their W1/W2 + ~02Z load is COO's + the seat's call.
- Broadcast: COO + MSTR (record+broadcast law). 0.5.0_AE_OpalETL contact is ANDREW'S act, not
  the fabric's — recorded so nobody double-dispatches.
