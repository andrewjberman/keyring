# ANDREW-DIRECT record — MDPF_VARFLAG scope ruling: Model Portfolios page only (verbatim)

**archetype:** SCRIBE
**recorded by:** `3.0.0_SA_CVO` · **channel:** Claude Code session, direct to this agent
**time:** 2026-07-17 ~15:30Z (immediately after the 8-month backtest delivery @ `67649304e`)

## The word, VERBATIM

> "This should not be per security, it should only be on items in the Model Portfolios Page. that
> means benchmark returns and peer returns tabs specifically"

## Context carried with the quote (surfaced, NOT adjudicated — XXX.md rule)

Arrived in response to the backtest report, whose recommended G2 layer was a per-security
volatility tripwire at the PKL input layer. Plain read: the variance-flag guard's scope is the
SERVED cells of the Model Portfolios page — the Benchmark returns tab and the Peer returns tab —
NOT per-security statistics. This narrows/confirms the proposal's original initial scope
("everything on the Benchmark and Peers tabs of Model Portfolios") and rules OUT the per-security
G2 layer as part of THIS guard. Whether a security-level check may exist elsewhere (e.g. inside
the existing pkl validator lane) is not adjudicated here — this guard is page-scoped.

## Action taken same turn

- Record committed + broadcast to COO + CTO + MSTR.
- Guard recommendation re-scoped to the two tabs' served cells (addendum committed alongside);
  the model-level served-cell evidence (0 healthy / 13 corrupt) is the operative calibration, and
  the vol discriminator SURVIVES in-scope because the served benchmarks tab carries model-level
  volatility cells (YTD vol 3.32→25.90 = 680% was a served-cell catch).
