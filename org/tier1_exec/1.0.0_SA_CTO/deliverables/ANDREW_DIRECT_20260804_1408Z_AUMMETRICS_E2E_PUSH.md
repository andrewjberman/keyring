# ANDREW-DIRECT — push the aum-metrics generation end-to-end + water test end-to-end

**Channel:** Andrew-direct, CTO terminal, 2026-08-04 ~14:08Z (~10:08 ET), during the IC-window P0.
**VERBATIM:** > "Ok we need to push that generation end to end and water test it end to end"

**Context binding ("that generation"):** the per-scope `platinum/mdpf/{scope}/aum-metrics.json`
generation — the P0 diagnosis immediately preceding: pointer verified correct (canonical map
@7a585074e), artifact plane 1-of-4 (only cottonwood, written 09:50 ET, content well-formed;
49financial/global/inflection ABSENT -> 404 -> null-degrade -> blank radial, all scopes, IC window).

**Scope as surfaced:** supersedes the post-17:15Z sequencing FOR THIS ARTIFACT FAMILY — generate
the three missing scope keys now via the production legs, and WATER TEST the full chain:

- **Leg 1 — GENERATE:** run the emitter legs for 49financial, global, inflection (DS lane, Rule 13;
  production path, operator-ordered — not agent-initiated ad-hoc).
- **Leg 2 — ARTIFACT:** per-scope EXISTS / FRESH / well-formed / plausibly-scaled content check on
  all four keys (CTO executing directly).
- **Leg 3 — SERVE:** the CloudFront URL `/api/general/mdpf/{scope}/aum-metrics.json` returns the
  artifact through the real route (edge JWT) — not just S3-direct.
- **Leg 4 — RENDER:** the AUM radial displays on the Model Portfolios page for all four scopes
  (DE lane, live render check).

Every leg OBSERVED with evidence; no leg's success inferred from the previous leg's rc.

**ADDENDUM ~14:10Z, VERBATIM:** > "we cannot wait for a schedule. Regardless, it is now 10:06am
Eastern, and all generation for this view shouldve been done by 10a, I believe the publisher was
running at 9:50a or at least that was the plan (maybe this schedule has not been deployed?)."

**Sharp datum:** the planned 9:50a ET publisher fire matches cottonwood's key write-time
09:50:50 EXACTLY — the publisher fired on plan and emitted ONE scope of four. Candidate
mechanisms (to discriminate, not assume): (a) only the cottonwood leg is deployed (EMIT-1
primary + EMIT-2 49f-bd-leg TOs are still PENDING at 0.2.0/0.4.0_DS — the legs may not exist in
production); (b) all legs ran, three failed; (c) per-scope schedules with only cottonwood's
deployed. GENERATION FIRES NOW BY DIRECT INVOCATION — no schedule wait (his word).

**Broadcast:** COO (dispatch/drive) + executing seats, same turn.
