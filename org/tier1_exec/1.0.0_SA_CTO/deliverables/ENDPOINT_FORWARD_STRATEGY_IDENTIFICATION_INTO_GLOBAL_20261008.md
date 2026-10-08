# ENDPOINT (step 2, /endpoint --forward) -- Strategy identification into the Global aggregate

- **Author:** `1.0.0_SA_CTO~DELL1`, L2, 2026-10-08 ~18:4xZ.
- **Brief:** `docs/briefs/mdpf-strategy-identification-into-global-brief-20261008.md` @68aa9dbe9e (`4.0.0_SA_CRO~DELL1`, 194 lines).
- **Order:** Andrew-direct ~18:3xZ, record @4672605201.
- **NOT YET LANDED in a PRD.** No PRD exists. This block goes into the PRD under the section title
  `ENDPOINT (step 2, /endpoint --forward)` once the project code is registered (L3). **RATIFIED** by Andrew ~20:1xZ ("Confirm as
  written"), with FWD-5 amended per his restatement; record `ANDREW_DIRECT_20261008_201xZ_LIQUID_ALTS_TO_ALTERNATIVES_ETF_STRATEGY_SLEEVES_ENDPOINT_CONFIRMED.md`.
- **NOT READ:** the task-order register, the project JSONs of MDPF_GLOBAL / MDPF_TAXSMA / MDPF_SECCLASS, and any open task order.
  Phase 0 reads the brief only.

## Outcomes

```
FWD-1  Andrew sees Cottonwood's PFDE strategy counted in the Global view
       DONE WHEN  EXERCISED -- Andrew (or someone for him) has opened the Global view after a scheduled run and read it
       ACCEPT     the PFDE figure under ETF Strategies in Global equals the PFDE figure in Cottonwood's own view, and Global's
                  total went up by that amount and nothing else
       SOURCE     brief Part I "Candidate thread (FWD-1)", O1

FWD-2  Every Cottonwood strategy outside its Models is added to Global
       DONE WHEN  EXERCISED -- one scheduled run read
       ACCEPT     each strategy Cottonwood's own view shows outside its Models has a matching amount in Global, in the same group
       SOURCE     brief O1; Andrew "additive because those are outside of the Models"

FWD-3  Muni shows as an ALT strategy, at Cottonwood and at Global
       DONE WHEN  EXERCISED -- one scheduled run read
       ACCEPT     Muni dollars sit under ALT Strategies, not under custom models; the large single Muni Income account was checked
                  by a person and either confirmed as Opal Muni or kept out with the reason written down, before any of it counted
       SOURCE     brief O2, F7

FWD-4  A new Opal strategy reaches Global with no engineer involved
       DONE WHEN  EXERCISED -- shown on purpose, not waited for
       ACCEPT     a strategy the system has never seen is introduced, and on the next run it is either counted in the right group
                  or listed by name for a person to place; nobody edits a program to make either happen
       SOURCE     brief O3; Andrew "Tax or Muni for ALT thus far"

FWD-5  Every Opal ETF Strategy sleeve is counted under ETF Strategies, wherever it appears
       DONE WHEN  EXERCISED -- shown on purpose
       ACCEPT     a client sleeve named after an Opal ETF, by its ticker or its full fund name, is found in SmartX, Rebalancer and
                  Eclipse alike and shows in the SMA group under the ETF Strategies drill-down; adding a new Opal ETF to the one
                  list is the only step for its sleeves to be found the same way
       SOURCE     brief O4, F5; Andrew "all the Opal ETFs for ETF Strategies", restated ~20:1xZ: sleeves named by ticker (DIVZ) or
                  full name (Opal Dividend Income) in SmartX, Rebalancer and Eclipse "(so far)", aggregated into the SMA taxonomy
                  category under ETF Strategies. AMENDED in place before ratification (id unchanged).

FWD-6  Nothing in Global is counted twice, and a person can see why
       DONE WHEN  EXERCISED -- shown on purpose
       ACCEPT     for any strategy amount in Global, a person can tell whether it is also inside a Model figure; an account set up
                  to sit in both is held out once and named as held out
       SOURCE     brief O5, F6

FWD-7  What the system could not identify is visible, never absorbed
       DONE WHEN  EXERCISED -- one scheduled run read
       ACCEPT     anything that looks like an Opal strategy but matched nothing is listed with its firm, its name and its dollars,
                  instead of disappearing into a catch-all or into Non-Model
       SOURCE     brief O6
```

## Rulings at L2 (this seat)

- **Brief F2 (basis is one value per strategy, not per firm): RULED.** The basis is held per strategy PER FIRM. Cottonwood's strategies
  are additive at Global (Andrew's word); 49financial's DIVZ and PFOE stay the verified carve-outs they are today. This is a design
  choice inside Andrew's ruling, not a new decision of his: both hold at once only on a per-firm basis.
- **Placement:** asked of the MDPF_GLOBAL owner (laptop `1.0.0_SA_CTO`) via `0.0.0_AB_MSTR~DELL1`, REC dell1.

## Settled by Andrew (~20:1xZ)

The open reading of "all the Opal ETFs" was neither (a) nor (b). ETF Strategies are Opal-managed SMAs that appear as whole client
sleeves named after an Opal ETF (ticker or full name) in SmartX, Rebalancer and Eclipse (so far). They are aggregated into the SMA
taxonomy category under the ETF Strategies drill-down. Direct holdings of Opal ETF shares are not this project's object. FWD-5 is
amended accordingly.
