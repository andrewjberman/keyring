# Andrew-direct ruling — Codex tilde seat resolution

**Channel:** Andrew Berman → `3.0.0_SA_CVO~X`, direct Codex conversation  
**Date:** 2026-08-27 (US Eastern)  
**Recorded:** 2026-08-27 13:36:01 -04:00  
**Scope:** Repository-local Codex seat loading and registration semantics

## Verbatim instructions

Immediately preceding turn (exact wall-clock timestamp was not exposed to the
agent):

> "first, delete the tier2_senior shadow copy, that should not even be there"

Current turn:

> "second, it should just resolve to 3.0.0_SA_CVO, the difference is it just tags the tilde on in terms of the registration, a tilde is just an additive character for the purpose of parallelizing more of that agent"

## Operational application

- The untracked empty shadow at `org/tier2_senior/3.0.0_SA_CVO/` was removed.
- `codex-seat-load.py` resolves both `role_home` and `seat_home` from the base
  serial (`3.0.0_SA_CVO`).
- The exact suffixed serial remains the registration/runtime identity and keeps
  nested inbox routing (`org/mcp/inbox/3.0.0_SA_CVO/~X/`).
- No exact-suffix repository home is required or inferred.
