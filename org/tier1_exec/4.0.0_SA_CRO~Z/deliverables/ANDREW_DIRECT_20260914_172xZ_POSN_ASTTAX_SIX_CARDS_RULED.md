# ANDREW-DIRECT 2026-09-14 ~17:2xZ (~1:20 PM ET) -- POSN_ASTTAX: the six /open-calls cards RULED

**Author:** 4.0.0_SA_CRO~Z (Chief Research Officer, site-Z lane)
**Channel:** Andrew at the 4.0.0_SA_CRO~Z terminal, in-session, answering this seat's `/open-calls` frame
(six cards, ~17:0xZ) that descended from brief v0.2 @f846dd72da s.6.
**Received:** after this seat's 17:14:32Z send to `1.0.0_SA_CTO~Z`; clock read at the commit of this file.

## VERBATIM, ENTIRE (the phrasing is the ruling)

> "Call 1, they should be summed because the goal is not to see what's yangs models versus what's external
> residuual in the satellite; it is to see total GLD listed as Commodity Asset, Metals Sub-Asset, and to see
> Total VXX (or whatever hedge securities) as Structured Asset, Hedge Sub-Asset. Call 2 Yes. Call 3, mint some
> yellow color, yes. Call 4 Yes. Call 5 Yes. Call 6, definitely B, models do not get updated because they are
> not changing, Satellites simply need to have an additional lambda to do weighted characteristics aggregates ."

## THE CARDS HE ANSWERED (this seat's text, so the word binds to a known question)

| card | the call as put | his word |
|---|---|---|
| 1 | Satellites toggle = Black Diamond's holdings coalesced by ticker; Models toggle = Yang; the two disclosed side by side and NEVER summed. yes / no | *"they should be summed ... the goal is not to see what's yangs models versus what's external residual ... it is to see total GLD listed as Commodity Asset, Metals Sub-Asset, and ... Total VXX (or whatever hedge securities) as Structured Asset, Hedge Sub-Asset"* |
| 2 | FWD-6's form: (a) rewrite to the Positioning page's own surfaces, or (b) keep the text and grade CMA deferred | *"Yes"* (the card's one-word form was (a)) |
| 3 | Commodities colour: (a) mint a new gold token, or (b) reuse amber | *"mint some yellow color, yes"* |
| 4 | Add GLD and VXX to the Bloomberg daily ETF pull today. yes / no | *"Yes"* |
| 5 | Benchmark policy for the three new classes: (a) explicit "no benchmark" label, or (b) name a benchmark ETF per class | *"Yes"* (the card's REC was (a) now, (b) later with Yang) |
| 6 | Reconcile Yang's model file to Black Diamond's models? (a) yes, Yang updates the PKL; (b) no, the Models toggle stays the design | *"definitely B, models do not get updated because they are not changing, Satellites simply need to have an additional lambda to do weighted characteristics aggregates"* |

## WHAT THIS SEAT READS, STATED AS A READING AND NOT ADJUDICATED

- **Card 1 -- the DISCLOSURE half of the card is REJECTED; the SOURCE half stands.** He does not want a
  Yang-vs-residual split on the page. He wants ONE TOTAL per ticker per satellite, classified. In Black
  Diamond's data that total IS the coalesced weight summed across the satellite's sleeves (GLD in Sat 30 =
  ST 6.26 + INT 1.00 = 7.25). ⚠ **The one hazard this reading must carry into every cell:** "summed" means
  summed ACROSS SLEEVES (and, conceptually, in-model + residual), which BD's figure already IS. It does NOT
  mean Yang's copy ADDED to BD's copy -- LT VXX 1.87 (BD) and 1.50 (Yang) are one position on two planes,
  and 3.37 would be a double count. This seat has put that one line back to him for confirmation; until he
  says otherwise the mechanism is: total = BD coalesced, Yang not added.
- **Card 1 also RULES SUB-ASSET LABELS:** GLD -> asset `Commodities`, sub-asset **`Metals`**; VXX and
  "whatever hedge securities" -> asset `Structured`, sub-asset **`Hedge`**. The live table today reads
  GLD `sub_asset_class=Gold`, VXX `sub_asset_class=Volatility`. So the retag cell (R1) changes BOTH levels
  for the affected rows, not the top level alone. ⚠ `Hedge` as a SUB-asset value must be kept distinct
  from the legacy TOP-level value `hedge` that C-VOL-HEDGE-STRUCTURED dissolves -- same word, third job.
  The encoding is the CTO's L4 call.
- **Card 3:** a NEW token, coloured yellow. Not amber (Cash).
- **Card 4:** routed the same turn to `0.0.3_BG_BBGTerminal` (its working tree, its two-phase sign-in
  state); this seat does not edit that file.
  ⛔ **CORRECTED ~17:2xZ, TEN MINUTES LATER -- THE CARD'S LANE FIELD WAS THIS SEAT'S ERROR.**
  `0.0.3_BG_BBGTerminal` returned a RAVC blocker (msg 22847): its gate denies every file write outside its
  own org home and every git mutation. The lane, read at `.owned-paths.yaml:1506-1507` by this seat and
  independently by `0.0.0_AB_MSTR~Z` (22853): `integrations/**` -> `ANY_EXEC_OR_AE`. The act is a
  working-tree DEPLOY on this box (scheduled tasks run the working tree), so it is gated by
  `1.0.0_SA_CTO~Z` and landed by an exec/AE seat -- never by the CRO (charter s.3). Re-routed to
  `1.0.0_SA_CTO~Z` + `0.0.0_AB_MSTR~Z` (22850/22851). **"Today" carries a second act:** the scheduled
  chain ran 2026-09-14 07:00 ET, so an edit now first fires 2026-09-15; capturing 09-14 needs a same-day
  ad-hoc Bloomberg ETF pull (download-class). Whether he wants (a) the edit only, first data 09-15, or
  (b) the edit plus the ad-hoc pull, is put to him at this terminal and is not assumed.
- **Card 6 -- (b), AND a design instruction:** the Models toggle is untouched, and the satellites'
  weighted characteristics (fee / yield / duration / beta / returns aggregates over the coalesced holdings)
  are computed by *"an additional lambda"*, i.e. SERVER-SIDE, not in the portal adapter. This supersedes
  brief v0.2 s.8 N2's recommendation to compute the overlay in the adapter (moot -- no overlay is shown) and
  refines R4: the characteristics join happens in the lambda. Whether "additional" means a second output of
  the existing `cot-satellites-registry-producer` or a separate function is an L4 / AE build-ladder call;
  surfaced, not decided here.

## WHAT THIS RECORD DOES NOT DO

It amends no PRD, cuts no cell, signs nothing. The L4 act (PRD v0.7) is `1.0.0_SA_CTO~Z`'s; the L5/L6 cut is
`2.0.0_SA_COO~Z`'s. Andrew's gate stands: no worker until he aligns on the breakdown.

## Broadcast

Same turn, MCP to `1.0.0_SA_CTO~Z`, `0.0.0_AB_MSTR~Z`, `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z` (per-recipient
result recorded in the session log); card 4 relayed to `0.0.3_BG_BBGTerminal`.
