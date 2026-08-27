# ANDREW-DIRECT — MDPF_CANON B1 ruled: Option 1, keep the leg, repoint the source

**Channel + time:** the base `1.0.0_SA_CTO` terminal, 2026-08-27 19:05Z (clock read at record time).
**Verbatim:** **"Option 1 with a repoint is fine"**

## What the words rule

Option 1 as put to him in the same exchange (this terminal, ~18:5x–19:0xZ): **keep** the
partner-held-ETF leg (the §3.3 ownership decomposition + reconciliation identity_2 are wanted),
and **B1 = repoint its source** — land the Schwab RPS silver feed through `opal-data-assets`
in-pattern and repoint `data/mdpf/scripts/feeders/wsd_partner_held_etf.py`; the legacy
`opal-data-bd/schwab/silver/rps/` read retires with the repoint. Option 2 (retire the leg +
re-scope the WS-A contract identity) is NOT taken.

## The investigation this ruling closes (evidence in-session, 2026-08-27 ~18:4x–19:0xZ)

Commissioned by his words: *"Can you identify the end of the line of that action, what artifact
that is going to, where it ends up?"* Traced with comp-find (denominator 27,333 files; portal
coverage positively controlled via `AdvisorBookView.tsx` resolving in the same scope):

- **Zero portal components read any of it.** No client-facing MDPF product consumes
  partner-held-ETF AUA.
- Termini, all internal: (1) **reconciliation identity_2** inside `mdpf_aggregate_aua.py`
  (`etf_total == Σ held + public_residual`) — the feed exists because the prior target-weight
  ESTIMATE over-attributed (PFOE held_total above its net assets) and hard-failed the scheduled
  WS-A run; (2) the **held_by_partner block** inside `platinum/mdpf/aggregate_aua/{date}.json`
  (served bucket, zero portal readers); (3) **`platinum/mdpf/etf_ownership_timeseries/{ticker}.json`**
  (MDPF_OWNTS — internal analytics, zero portal readers).

## Companion ruling recorded with it (same call-6 split, ruled earlier today)

**B2** (`opal-data-inf/orion/jwt/current.json`) = **standing declared exception** — a credential
artifact, never pipeline data (Andrew via the CTO~X relay 76365, "Recs approved, including
call 6", confirmed in the CTO-base discussion this terminal). Formal D10 exceptions-record entry
owed when D10's register wakes, per D10's own acknowledge-and-record clause.

## Consequences

1. `docs/architecture/MDPF_CANON_PRD.md` rows B1/B2 updated this commit; **§7.2 shrinks** —
   B1/B2 no longer wait on D10-2; 7.2 remains open for the legacy buckets themselves only.
2. The B1 build leg (in-pattern `opal-data-assets` RPS landing + reader repoint) is
   **2.0.0_SA_COO's to cut when prioritized — NOT D2-cohort work**; it naturally pairs with
   re-establishing the RPS feed's standing landing (recorded frozen at date=20260723 per
   `build_mdpf_wse_49f_non_model_aua.py:60` — verify at cut time, that note is a code comment
   not a fresh measurement).
3. Nothing executes tonight; sequencing sits behind the D2 drive per his session priorities.
