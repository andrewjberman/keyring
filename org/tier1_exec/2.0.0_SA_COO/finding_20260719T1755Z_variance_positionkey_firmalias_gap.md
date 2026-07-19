# COO finding-routing record -- variance _position_key firm-alias gap (2026-07-19 ~17:55Z)

**Durable carrier** for a real, low-urgency finding surfaced by 0.8.0_AE_CloudComp~D (msg 175456Z) while
grounding CVO's PH2-C2 semantic-axis smell. ~D correctly did NOT self-authorize (SCOPE#5) -- it is outside
~D's scoped reactivation and in ~C's variance-mechanism territory. Recorded so it survives to the owner's
respawn (~C is dark; respawn wave held for Andrew).

## The finding (CONFIRMED by ~D, comp-kuzu live, HEAD-current)

The variance mechanism's `_position_key` excludes `bd-49f-etf-ownership-daily` from its true 3-way firm
group. `_position_key` strips only declared firm-VALUE tokens (`firm_values=[bd,cot,inf]`); **"49f" is bd's
CLIENT ALIAS** (`firm_names {bd:49financial}`), not a keying token, so it SURVIVES the strip ->
bd's key `{firm}-49f-etf-ownership-daily` != cot/inf's `{firm}-etf-ownership-daily` -> the
`etf-ownership-daily` group reads `{cot,inf}` = 2-member instead of `{bd,cot,inf}` = 3-way.

- **Refuted (non-issue):** the bd<->inf `gold-qa-runner` 2-member tie is GENUINE -- no `cot-gold-qa-runner`
  EC2 exists (purpose-kept QA boxes). NOT a position_key gap.
- Consistent with CVO's exercised item-2 data (the 4 no-majority 2-member ties).

## Why it is NOT urgent (no live defect)

Advisory disposition (`allowed_facets=[]`) renders it CORRECTLY today -- "(candidate -- advisory, pending
adjudication)", ZERO "(debt)" (CVO PASS, 5770-line scan). This is an adjudication/normalization REFINEMENT,
not a live render defect. No queue-jump.

## Routing + sensitivity

- **Owner:** ~C's NFRA_ONTOLOGY variance MECHANISM (the `_position_key` / firm-variance derive contract).
  NOT PH2-C2 (closed/accepted @ccb6c928e). NOT ~D's scoped reactivation.
- **SENSITIVE -- CTO arch-gate required:** the fix candidate is "normalize firm-alias tokens (49f->bd) in
  `_position_key`", which touches **firm-alias semantics right next to the firm-SEPARATION rules**
  (bd/cot/inf never mirror/sync; 49f is bd's client; two 49F buckets never add/substitute). A keying-normalization
  that folds 49f->bd must be adjudicated by the variance owner + CTO, never a quick edit. Whether the two
  artifacts SHOULD group (same logical artifact across firms, to detect variance) vs stay separate is the
  semantic question to adjudicate.
- **Disposition:** HOLD for ~C's respawn as the natural owner (no urgency). ~D offered to take it (hot
  context, built the adjacent surface) -- that would be a scope-widen of ~D's Andrew-scoped reactivation, so
  it needs CTO's word before I sequence it to ~D. Flagged to CTO for the routing call.
- **Grounded detail:** ~D's reply to CVO, ~20260719T1755Z.

**Status: RECORDED + ROUTED (awaiting owner). Not dispatched. COO tracks; picks up on ~C respawn or CTO's accelerate word.**
