# MDPF -- END-TO-END FLOW + PARALLEL-CHANNEL DEPRECATION INVENTORY

**Author:** `2.0.0_SA_COO` - **2026-07-28T175x Z** - **Andrew-direct** ~1741Z (`db9b11524`) + ~1743Z
(`d00d5a3ad`) + ~1755Z: *"I dont care about the alarm, I care that the system has clear flow end to end,
and that legacy and parallel channels are appropriately deprecated."*

**STATUS: PARTIAL AND LABELLED AS SUCH.** The parallel-channel inventory below is MEASURED today and is
the actionable half. **The per-channel feed+schedule trace (Part 1) is NOT done** -- upstream of
`opal-assets-daily-aua` is mapped only as far as today's measurements reach. **Every unmapped edge is
marked `[UNMAPPED]` rather than omitted**, because an omitted edge reads as an absent one.

---

## 1. THE DEFECT, IN ONE TABLE: THREE LIVE "GLOBAL AUA" NUMBERS

| # | Value | Producer | Basis | State |
|---|---|---|---|---|
| 1 | **$1,951,676,164.42** | REVAMP `dim_mdpf_aggregate_aua_timeseries.py` | as-of 07-22, **3 firms** | **SERVING** (hand-restored 13:41Z) |
| 2 | **$1,924,186,044.47** | **the BROWSER** (`ModelPortfolios.tsx:1171`) | model leg (#1) + non-model leg (#3) | **RENDERED to the client** |
| 3 | **$1,783,405,733.70** | platinum daily partition | as-of 07-28, **2 partners, no Cottonwood** | feeds the gold DDB |

**Three producers, three bases, three numbers, no arbitration.** Nothing in the system compares them.
**This is not a risk of drift; it is an inventory of drift already present.**

---

## 2. TARGET: THE CANONICAL FLOW (one path, no parallel writers, no client math)

```
  per-channel source            ONE silver               ONE gold                ONE publisher            portal
  (custodian / vendor)   -->    fact_* tables    -->    generation      -->    atomic, scheduled   -->   READS ONLY
   scheduled + verified          monolith                 gold DDB              full derived set          zero arithmetic
```
**Four invariants. Each one is violated somewhere today.**
- **I1 ONE PRODUCER per served value.** No second path may write a surface the first path owns.
- **I2 ATOMIC over the DERIVED set.** The set comes from what the RENDER CONSUMES, not a hand-list.
  *(Today: measured as FIVE members, not four -- the fourth-member belief was co-signed by CTO and me.)*
- **I3 SCHEDULED, with an event trigger only as an accelerator.** Event-only = a defect (NEVER#4).
- **I4 THE PORTAL TAKES, IT DOES NOT COMPUTE.** Any arithmetic in the client is a drift opportunity.

---

## 3. CURRENT: THE PARALLEL CHANNELS, MEASURED

```
 A. REVAMP (CANONICAL-TO-BE)
    dim_mdpf_aggregate_aua_timeseries.py  [code/scripts/gold/]
      -> opal-data-assets gold/mdpf_revamp/{global,49financial,inflection,cottonwood}/
      -> ***NO PUBLISHER***  -> (hand-restored 13:41Z) -> portal-v2 json/mdpf/{firm}/aggregate-aua-timeseries.json
    STATE: producer FIXED + scheduled-run-verified 07-28 (426 tested / 0 failing, 3 firms, cottonwood 47 slots).
           SERVED SET IS FROZEN -- no automated producer reaches it.

 B. LEGACY ROLLUP  (Stage 4, mdpf-daily-dispatch.sh:391)
    backfill/build_aggregate_aua_timeseries.py
      -> portal-v2 platinum/mdpf/aggregate_aua_timeseries.json        (authoritative write, STILL LIVE)
      -> portal-v2 json/mdpf/aggregate-aua-timeseries.json  + /{firm}/ (mirrors, NOW explicitDeny)
    STATE: UNCHANGED and STILL WRONG -- builds "2 partner(s)", structurally cannot emit cottonwood.
           Its clobber of the served set is BLOCKED, not removed. Andrew ~1351Z: automation NOT WANTED.

 C. LEGACY COMPAT EMIT  (Stage 3.5, dispatch :363-386)
    backfill/build_legacy_compat_emit.py
      -> portal-v2 json/portfolios/{non_model_assets,aum-timeseries}.json
    STATE: NOW explicitDeny -> writes fail, chain tolerates. Both keys FROZEN at 07-27T15:10:07Z.
           *** non_model_assets.json IS THE NON-MODEL LEG THE BROWSER ADDS (channel E). ***

 D. GOLD-DDB EMITTER
    opal-assets-daily-emitter   cron(15 17 * * ? *) ENABLED, ran 07-28T17:15:19Z
      reads  portal-v2 platinum/mdpf/aggregate_aua/{date}.json   <-- the PLATINUM path (channel B's family)
      writes opal-assets-daily-aua (DDB)
    STATE: component HEALTHY. 32 rows/day -> a ROW census reads GREEN.
           Of 32: 5 fresh/complete - 13 rolled-forward - 14 missing - partner_aua_total = 0.
           Source self-certifies as_of 07-28 / status current / rolled_forward_partners {} and
           covers only 49financial + inflection -- COTTONWOOD ABSENT.

 E. CLIENT-SIDE AGGREGATION   *** VIOLATES I4 ***
    portal/src/pages/ModelPortfolios.tsx:1164-1172
      per-firm : TAKES perFirmAumMetrics.total.aum          <- correct shape
      GLOBAL   : COMPUTES trendLastPoint.aum + getNonModelAumForDate(nonModelData...)
                 i.e. channel A's model leg + channel C's non-model leg, SUMMED IN THE BROWSER.
    STATE: LIVE. This is number #2. Delta vs #1 = $27,490,119.95, persistent 2+ weeks.

 F. [UNMAPPED] the platinum daily-partition producer (chain Stage 3 / WS-A) -- writes what D consumes.
 G. [UNMAPPED] per-channel feeds + schedules into monolith silver (Part 1, not started).
```

---

## 4. DEPRECATION ORDER (dependency-forced, not preference)

**The ordering is forced by one rule: never remove a writer before its replacement serves.** Today's serve
is frozen precisely because a decommission (Andrew ~1351Z) landed ahead of its replacement.

| # | Action | Why it is HERE and not earlier |
|---|---|---|
| **0** | **[UNMAPPED] Part 1: per-channel feed + schedule + DDB ARRIVAL census** | **Nothing below is safe without it.** Deprecating a channel whose feed you have not traced is how you discover a consumer by breaking it. |
| **1** | **Fix the gold-DDB input (channel D's source)** | The DDB is *upstream* of the publisher. Build a publisher over a table where 5 of 32 cohorts are fresh and it publishes staleness on a timer, and reads GREEN **because** it is well built. |
| **2** | **Build the atomic scheduled publisher (A -> served set)** | Restores an automated producer to the frozen serve. **Set DERIVED from the render, not hand-listed** (I2). |
| **3** | **Remove the client-side sum (E)** | Cannot land before 2: the browser sums because no server-side artifact carries the composed Global. Remove it first and the number breaks. **After 2, the portal TAKES.** |
| **4** | **Retire C (legacy compat emit)** | Only safe once E no longer reads `non_model_assets.json`. **C is currently frozen-by-Deny, which is a HOLD, not a retirement.** |
| **5** | **Retire B (legacy rollup)** | Its mirrors are already denied; its platinum write still feeds D. **Cannot retire until 1 re-sources D off platinum.** |
| **6** | **Retire the platinum path (F)** | Last. Everything above must be off it first. |

**⚠ THE TRAP IN THIS ORDER:** steps 4-6 all look like "delete a dead thing." **Each has a live reader
today** -- C feeds E, B feeds D, F feeds D. **A channel is not dead because we stopped valuing it; it is
dead when nothing reads it, and that is a measured claim.**

---

## 5. WHAT IS NOT KNOWN, STATED SO IT IS NOT MISTAKEN FOR MAPPED

- **Part 1 in full** -- per-channel feed + schedule + **arrival** for 49F (Schwab 0824, SmartX model +
  roster), Inflection (Eclipse, Orion), Cottonwood (BD allocations / holdings / unrealized / rebalancer).
- **Which producer stamps the file date rather than the data date** (channel D's alarm names the behaviour;
  I have not read the producer).
- **Whether E is the ONLY client-side arithmetic.** One file, one location measured. **The portal-wide
  sweep for re-derivation sites is Part 2 and is not done.**
- **Consumers of C's two frozen keys** beyond E. Un-enumerated; mine.
- **Whether `nonModelData` is itself server-aggregated** before the browser adds it.

**METHOD CONSTRAINT, binding (CTO-endorsed):** map by **enumerating what the RENDER CONSUMES and working
BACKWARDS.** A forward trace from producers is what produced the four-member serving set that CTO and I
co-signed and that was wrong by one member. **The five-member set was found backwards, this afternoon.**

-- `2.0.0_SA_COO`
