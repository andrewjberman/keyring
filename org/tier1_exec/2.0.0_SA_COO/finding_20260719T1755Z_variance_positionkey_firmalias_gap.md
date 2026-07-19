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

## CTO ARCH-GATE ADJUDICATION + ROUTING RULING (180033Z, under PROCEED-ALL-NFRA)

CTO ruled routing **(c): ~C owns it under proceed-all** (my "hold" call crossed Andrew's wave release). ~C added to the MSTR allocation wave; ~D stays PH2-scoped (do NOT widen ~D into ~C's mechanism). CTO gave arch-gate DIRECTION now (final gate on the actual diff):
- **CORRECT TARGET = 3-way grouping.** The variance mechanism's PURPOSE is cross-firm variance detection (the ontology's founding "firm-VARIANCE" question); etf-ownership-daily across bd/cot/inf is ONE logical position, bd just names it with the "49f" client infix. Normalizing firm-alias (49f->bd) in `_position_key` is correct-direction.
- **FIRM-SEP: NOT VIOLATED (CTO adjudicated my flag).** This is ONTOLOGY/graph ANALYTICAL grouping over resource summaries/metadata -- NO bucket cross-ref, NO data-plane, NO firm DATA mixing. Firm-sep (IAM/bucket) governs data ACCESS, not whether the ontology may OBSERVE that two firms both run a pipeline. Safe. (My sensitivity flag was correct to raise; CTO resolved it -- the fix is analytical, not a data-plane firm mix.)
- **~C GATE CONDITIONS (CTO gates the diff before it lands):** (1) COMPLETE firm-alias map -- enumerate EVERY client alias, do not hand-patch only 49f; (2) OVER-MERGE guard -- do not collapse genuinely-distinct resources; (3) confirm NO SERVED-output firm-leak -- this grouping is internal comp-tool analysis, but if any variance output is served to a firm-scoped consumer, the served-firm-sep question REOPENS as a separate downstream gate.

## IMPACT QUANTIFICATION (folded from ~D 180037Z + CVO's independent scan)

CVO independently re-verified both halves from its OWN estate scan. NEW blast-radius context: the gap makes **~2 of the 5 fork-shadows** (cot/inf-etf-ownership-daily) MAGNITUDE ARTIFACTS -- if bd were correctly grouped 3-way they'd likely re-verdict to twin/canonical. So "5 fork-shadows" is ~2 inflated by the position_key gap. Does NOT affect the PH2-C2 PASS (render stays honest -- advisory candidate, not debt); it is adjudication blast-radius for ~C.

**Status: ROUTED TO ~C under PROCEED-ALL-NFRA (CTO ruling (c)). CTO direction + 3 gate conditions given; CTO gates the diff. Impact quantified (~2/5 fork-shadows are gap artifacts). LOW urgency. COO coordinates ~C's drive as part of the wave; hands ~C this record + CTO's conditions on spawn.**
