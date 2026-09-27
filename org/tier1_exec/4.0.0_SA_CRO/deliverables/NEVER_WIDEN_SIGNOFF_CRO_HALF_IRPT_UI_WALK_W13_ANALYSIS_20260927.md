# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 13: the Analysis chain, fifth attempt, on resident cw

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W13_ANALYSIS_20260927.md`
blob `49ee40b0d9046a6e776d3d3bb8a3b2984d32cc35` @`eea3452029`. The blob is the same at HEAD and on disk (read
2026-09-27 ~13:5xZ).
**Asked by:** 2.0.0_SA_COO~P msg 101900. This seat is not in the act.

## VERDICT: SIGNED on blob 49ee40b0

- **It is window 11's text plus two deltas.** A word diff against blob `9ee0c7c5`, run here, shows:
  - W13-1, the reason for the attempt: window 11's two resident defects, diagnosed by ~Y, now served as resident
    `fe64236bbb-cw`:
    - `capture_env` strips PYTHON* so the runner's aws CLI no longer crashes;
    - the read-back reads the SAVED portfolio;
  - W13-3: **ONE added YCharts read**, `GET /model_portfolios/fixed/{id}`, after the status reads `available` (CTO
    101897). Every other W11-3 bound is unchanged.
- **Andrew's word still covers it** ("yes you can run as many analysis attempts as needed", @460e2ae8cb): ONE upload,
  ONE Overview, no retry.
- **Carried:** window 11's conditions, as the packet restates them:
  - the bounds are counted from the resident journal;
  - a re-capture keeps the prior secret as AWSPREVIOUS;
  - an overrun is a BLOCKING row the same tick;
  - the ledger prints the running re-capture total across attempts. It is 0 completed after window 11.
- **Order:** window 13 is created only after window 12 closes, so the two superadmin windows do not overlap.

Not measured by this seat: resident cw's census and the W11 evidence (the packet's and ~Y's).
