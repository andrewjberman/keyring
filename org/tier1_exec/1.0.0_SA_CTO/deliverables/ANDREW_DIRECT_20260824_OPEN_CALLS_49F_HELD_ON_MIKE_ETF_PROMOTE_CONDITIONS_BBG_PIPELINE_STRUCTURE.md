# ANDREW-DIRECT 2026-08-24 ~15:2xZ (base CTO terminal) -- rulings on the six /open-calls cards: 49F sourcing HELD on Mike's confirmation; ETF promote NOT YET (two named conditions); constituent accrual goes through the Bloomberg /terminal-upload pipeline structure; the Bloomberg-first / Pathfinder+TrueShares-fill / Bloomberg-enrich layering

**Recorded by:** `1.0.0_SA_CTO` (addressed seat) - **archetype:** SCRIBE / COORDINATE
**Context:** his answers to `/open-calls` at this terminal (six cards, ~15:15Z). Quoted exactly as typed.

## VERBATIM

> "1.) We need confirmation from Mike at 49 before making choices on exactly where we want to
> source/merge data from for 49, so I'm hesitant to make any promotes for that until that is decided.
> 2.) We are not positioned to promote yet. Until data pipeline is complete with full data structure
> for daily bloomberg data for all ETFs, and it displays properly on DEV build with GICS replaced for
> sub-categories on frontend. 3.) This needs to be handled via Bloomberg pipeline structure. We should
> be accruing all data in same shape via daily bloomberg /terminal-upload schedule with a scoped
> additional script for this purpose, with that data accruiing in correct structure in a relevant
> opal-data-etfs subfolder. 4.) Not relevant right now until we get confirmation from Mike on how to
> run this. 5.) Rec agreed. 6.) If Bloomberg cannot provide consitutents, then we need to decide what
> we can get from Bloomberg, and fill out the rest from Pathfinder and Trueshares sources, then enrich
> via the underlying holdings as needed via Bloomber."

(Card numbering as presented: 1 = session order / spawn order; 2 = ETF page PROD promote; 3 =
TrueShares capture deploy timing; 4 = 49F history floor fork; 5 = 08-20 MDPF gap-day backfill; 6 = BQL
entitlement for constituents.)

## WHAT EACH BINDS (unwidened; the phrasing is the ruling)

- **(1) 49F sourcing = HELD ON MIKE (49 Financial).** No sourcing/merge CHOICES for 49F, and no
  49F-related promotes, until Mike confirms. `ADVI_49FSRC` stays at stage 2 (PRD v0.1 draft as the
  brief for that conversation); **no stage-3 decomp, no TOs** on it until his confirmation lands.
  The 49F switch stays HELD (two conditions unchanged) -- and now ALSO pends Mike. He did NOT
  ratify the spawn order as a whole with this line; what he ruled is the 49F half of it.
- **(2) ETF Positioning promote = NOT YET, TWO NAMED CONDITIONS, both his:** (i) the data pipeline
  is COMPLETE with the FULL data structure for daily Bloomberg data for ALL ETFs (the four books,
  every field the shape needs, accruing daily); (ii) it DISPLAYS PROPERLY on the DEV build with
  **GICS replaced by sub-categories on the frontend**. These become s.11.1 DONE conditions of
  `ETFS_POSITIONING`; DT's staged promote stays staged. (The dormant-ADVI-machinery breadth
  question is moot for now -- the promote is not positioned regardless.)
- **(3) The TrueShares capture is NOT deployed as wired.** Constituent/holdings accrual is handled
  **via the Bloomberg pipeline structure**: the daily Bloomberg `/terminal-upload` schedule (site-Z
  vehicle) with **a scoped additional script for this purpose**, all data accruing **in the same
  shape**, in the **correct structure**, in a **relevant `opal-data-etfs` subfolder**. TO-4 Half 2
  (@4e5800fde0, the laptop-side call site + env var) is SUPERSEDED as the delivery mechanism -- the
  capture's SOURCE (the issuer sheet; egress GRANTED 08-21) survives, its VEHICLE moves into the
  daily pull structure. Amendment to the L1 order at site Z (MSTR bridges; MSTR~Z executes).
- **(4) 49F history floor fork = NOT RELEVANT NOW; pends Mike.** No ruling on (a)/(b)/(c); the PRD
  keeps all three priced.
- **(5) 08-20 MDPF gap-day backfill = HOLD** (rec agreed) until the DS trace of the cottonwood/global
  08-19 upstream anomaly lands; likely one act with the 08-19 re-emission ruling (CTO+COO's).
- **(6) Constituent layering, ruled:** Bloomberg FIRST -- decide what Bloomberg CAN provide (the
  entitlement question is subsumed: it is "what can we get", not "buy BQL"); **fill the rest from
  Pathfinder and TrueShares sources** (the two issuer sides: PFDE/PFOE via the Pathfinder feed,
  DIVZ/IDVZ via the TrueShares sheet); then **enrich via the underlying holdings as needed via
  Bloomberg**. This is the A3 spec, and it lives inside the (3) pipeline structure.

## CONSEQUENCES FOR THE SESSION ORDER (map v0.1 -> v0.2)

- Phase 1 paper: ADVI_49FSRC PRD stays a DRAFT-FOR-MIKE; the D4 work gains a **round-2 scope**
  (conditions (i)+(ii) + the (3)/(6) pipeline structure) -> ETFS_POSITIONING s.11 amendment -> COO
  round-2 decomp -> TOs (DS data structure; DE GICS->sub-categories on DEV; site-Z scoped script via
  the L1 order amendment; AE TO-5 schedule apply stands).
- Phase 2 spawn order, revised: COO + CVO (D1 cert/TOs; ETFS round-2 decomp) -> DS (cottonwood/global
  cell; D1 gold; ETF data structure) -> DE (D1 portal; GICS->sub-categories) -> AE (TO-5 apply; TO-4
  as-wired STANDS DOWN) -> 0.8.0 (D0). Site Z: L1 amendment (the scoped additional script) via MSTR.
  **Spawns still need his word** -- not inferred from these rulings.

## BROADCAST
MCP to every seat that holds a touched item (live or queued): MSTR (integration; site-Z bridge), CRO,
COO, CVO, AE (TO-4 stands down), DS, DE, DT (promote stays staged). Same turn.
