# AMGT_RESAPP -- ROUND 46 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~04:3xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26441, READ-acked, subject *"L10 SLUG AMGT_RESAPP round 46
@4be12a2f1a"*, citing `surprise-channel/adjudications/ADJUDICATION_v56.md`. Packet `round46/DRAIN_END_PACKET.md` @`cc1700dfbe`.

**Round 46 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

**Andrew's adjusted-basis ruling is served.** AMD reads 415.64 USD, ratio 0.6591 -- the number round 45 predicted from the
same-basis proxy; served Base cases went 48 -> 70, all inside the price band; the combined scoped-API deploy closed with
nothing stranded. `Z-W163-S1` (the gitlink instruction), `Z-S295`, `Z-S292`, `Z-S293`, `Z-S294` graduated.

## 2. RULINGS

1. **THE FORMULA STRING MUST NOT CLAIM WHAT ITS INPUT DOES NOT CARRY.** `uu-1` AC4 (a) is PARTIAL: the P/E names the
   adjusted basis on 70 of 70; the EPS basis object (`BEST_EPS`, Bloomberg's consensus definition) names it on 0 of 70, yet
   the served `formula` reads "adjusted consensus EPS (FY1)". **Ruling:** the formula names each input as its basis object
   does -- "Bloomberg consensus EPS (FY1, BEST_EPS) x adjusted trailing-median P/E (PX_LAST / IS_COMP_EPS_ADJUSTED)". Nothing
   is claimed about BEST_EPS's basis until a vendor field states it (my uu-4 half s.4 bound, now on the page). A served-text
   change: a never-widen pair; the 70 values do not move.
2. **THE BASE-CASE ANCHOR -- A DESIGN FORK, SENT FOR RESEARCH THIS TICK.** Against the team's own written Base (20 names carry
   both), the rule reads **median 1.44x high, above 1.5x on 8, WDAY 4.36x**, all inside the price band. A ten-year trailing
   median P/E carries multiples the team no longer underwrites on growth names. Under the `/self-drive` routing (a design
   fork: CRO research, then this seat decides), `4.0.0_SA_CRO~Z` is asked for the estate's precedents and the team's own
   practice (which multiple the packs apply; a shorter window; a forward multiple; leading with the team's case where one
   exists). **This seat rules on the tick the research lands.** Nothing changes the rule before then.
3. **Where a team Base exists, the page shows it** (AMGT_CORPUS serves it, cited, by case, with `unit_as_written`; ruling at
   CORPUS round 9). RESAPP's part is the payload: the scoped API carries the dossier's team cases beside the rule's Base, each
   labelled for what it is. The render is DSGN_AMGTV1's (fork F5; its PRD C-ASKS row "the dossier ... is served").

## 3. FWD GRADES

- **`FWD-30`: REALIZED on the served plane at round 46's close** (export-compare 95 of 95, absences missing 0, cases 285 of 285),
  **held from REALIZED as a whole** by the page half: the page fixes sit on portal DEV and the timeline panel push is held by
  Andrew's "lets hold on pushes and merges for now".
- **`FWD-12` limb 3 (the team's cases)**: the data half is met at AMGT_CORPUS; the payload half is ruling 3's cell here.
- The full FWD-1..FWD-31 pass (`uu-1`, 31 of 31 graded, @`44ca72d927`) is the record for the rest.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~Z` cuts for round 47 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **The formula string names each input's own basis** (ruling 1) | served text only; never-widen pair; 70 values unchanged |
| 2 | **The scoped API carries the team's cases** (ruling 3) | from `read_dossier`, cited, by case, `unit_as_written` + nullable `currency`; beside, never replacing, the rule's Base; SERVED, pair |
| 3 | **The two harness breaks** (`Z-W167-S1`, `-S2`) | one repair cell |

**NOT a cell yet:** the Base-case anchor (ruling 2, awaiting the CRO research; decided the tick it lands).

## Compiler Tools

The CVO's team-vs-rule join (20 names, the join's whole population) and its AC4 (a)/(b) split taken as the measurement; the
uu-4 CTO half s.4 bound (@`f266db8833`) as the prior statement of the EPS-basis gap.
