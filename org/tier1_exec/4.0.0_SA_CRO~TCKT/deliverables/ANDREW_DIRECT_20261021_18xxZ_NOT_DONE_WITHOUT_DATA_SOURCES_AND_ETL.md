# ANDREW_DIRECT 2026-10-21 ~18:0xZ -- a report variant is not done until its data sources and their queueing/ETL are done

Channel: Claude Code session, seat 4.0.0_SA_CRO~TCKT (box dell2). Andrew's reply after this seat reported the
FWD-10 Multi-Comp runs 7K/7M PASS as "Core comparison ... works end to end".

Verbatim:

> How do we possibly have core comparison and multicomps done if we dont have bloomberg done? if the data sources arent
> ironed out and associated queueing/ETL then those are not done

## This seat's correction, measured

Run 7M's receipt (`org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_fwd10_multicomp_7m/A_E2E7M.txt`
@0f24c09e925) proves less than "end to end":
- A Multi-Comp filed through the PROD page yields a 60-page PDF. Its comparison sections carry price-derived figures.
- The sections route graded 9 sections. The holdings file was four broad ETFs (SPY, AGG, IWM, EFA).
- It does NOT prove that the concentration and characteristic pages are filled from sourced data for a client's actual
  holdings. That is the Bloomberg data layer: FWD-13 to FWD-15, drafted @aa1b308c2be and not yet in the PRD.

## The rule (his words govern)

- Core comparison (FWD-10) and Multi-Comp / parity (FWD-11) are NOT done while their data sources, and the queueing
  and ETL that feed them, are not done.
- A green run of the filing-and-render pipeline is not a done verdict.
- Owner of the grading consequence: `1.0.0_SA_CTO~DELL2` (ENDPOINT) and `3.0.0_SA_CVO~DELL2` (L9 adjudication).
