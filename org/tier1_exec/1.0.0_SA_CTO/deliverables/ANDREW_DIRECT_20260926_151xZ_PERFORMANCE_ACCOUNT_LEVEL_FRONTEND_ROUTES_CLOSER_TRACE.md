# ANDREW-DIRECT 2026-09-26 ~15:1xZ -- Performance is account-level; frontend route structure from three /closer traces

**Channel:** the 1.0.0_SA_CTO terminal. **Recorded by:** 1.0.0_SA_CTO, the same turn.

## Verbatim

"Performance is always going to be account-level, not client level. To me, this is just a frontend code issue rather
than a backend data issue. I think we need to have a 4.0.0_SA_CRO agent run a /closer trace on several surfaces: 1.)
The Performance tab, 2.) The Holdings tab, 3.) The header/identity panel and the adjacent search function. We need to
take that data and come up with a refined route structure to manage this, on the frontend specifically."

## What it decides

1. **Performance is account-level.** The backend's one-account rule (`performance/retained.py:77-80`, "performance
   computes exactly one selected account") is CORRECT by design. A client- or relationship-level selection is a
   frontend routing defect, not a backend gap.
2. **R8 is SUPERSEDED** (`RULINGS_IRPT_20260925.md`):
   - option B (a backend per-account loop composing a multi-account report) is NOT built;
   - option A (a set-level aggregate method) is withdrawn, together with its CRO research ask (101266).
3. **4.0.0_SA_CRO runs `/closer trace`**, read-only, on three surfaces:
   - (1) the Performance tab;
   - (2) the Holdings tab;
   - (3) the header/identity panel and the adjacent search.
4. **From those traces, a refined FRONTEND route structure** that carries a client selection down to an account for
   Performance. The CRO proposes it; the CTO lands it in `DSGN_IRPTV1_PRD.md` as an addendum. It goes to
   2.0.0_SA_COO~D's round 6.

## Routed

| seat | message | what |
|---|---|---|
| 4.0.0_SA_CRO | the traces and the route proposal | the ask |
| 2.0.0_SA_COO~P | B stops | decision copy |
| 2.0.0_SA_COO~D | account-level Performance goes to round 6 | decision copy |
