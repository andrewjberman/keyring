# VERDICT — TO-W3-CCY3 · NFRA_SUBSTRATECARDING wave 3 · 0.8.0_AE_CloudComp~Y

**Verifier:** 3.0.0_SA_CVO~X · **Verdict:** **VERIFIED PASS at TO level** · 2026-08-27 ~07:2xZ
**Delivery:** @`fbb8a94c17` (5 files, 967 insertions) — lane-declared LOCAL behind the LD-0367
rail with firing ancestor controls; recorded as stated.

## Battery at this seat

| check | result |
|---|---|
| proof-of-spec gate | **VALID** (stdout token) · 8/8 criteria · 28/28 forward · 28/28 backward |
| v2 schema | 4 of 4 cards 0 errors (validated at this seat during the CCX3 re-gate; the lane additionally ran BOTH Draft7 and Draft2020-12) |
| COMMIT STATE | 5 of 5 TRACKED, untracked scan empty |
| pin containment | first+last probes resolve at the certified vintage @`049ff4ca4a` (2/2) |

Notable: the lane shipped its instance VALID on delivery because it hit the SAME 11 wrapper
violations as CCX3 first, fixed them, and then handed CCX3 the fix (74905) with a positive
control proving the checker passes a correctly-shaped instance — two lanes drifting from the
contract in the same three ways, independently, is a schema-ergonomics fact for the contract
owner, not a lane defect.

## Verdict census and what the cards carry

**QUALIFIED ×4, none SOUND.** The floor rule caught a real over-claim by the lane's own account
(W3-bzgw persistence.basis demoted to inferred — the scalar followed the MIN over the map, and
the sub-claims were NOT upgraded to clear the gate, which is the rule used in the direction it
exists for). Findings of record, each multi-plane with the bound stated:

1. **A protection ruled BLOCKING has never executed** (W3-uuxp): `_archive_superseded` reachable
   only from `_stamp_cas`, CAS off by default on the live Lambda, zero objects in the history
   prefix — three planes, each able to return the opposite answer, with the empty-prefix
   ambiguity on a non-versioned bucket honestly bounded (the CODE plane closes it).
2. **A 259,918-byte valid batch one prefix away from its consumer for 50 days, every instrument
   green** (W3-dljc): the consumer paginates `cse_ingest/pending/`, the producer writes
   `cse_ingest_staging/` — and a sweep of an empty prefix and a sweep with nothing to do are the
   same event. Intent unmeasured, file NOT moved, the unowned seam named as the finding.
3. **The 6-of-14 silent fall-through** (W3-thav): eight ARN classes drop to a suppressed
   `logger.debug` while the better-recognized UNKNOWN case warns — the asymmetry is the defect,
   with a control pair proving the module's logging works.
4. **CodeSha256 matched and the package was still stale** (W3-uuxp): vendored `_provenance.py`
   6,557 bytes of real divergence after CRLF was controlled for (641 bytes) — then bounded the
   reassuring way: the drift confined to a surface the write path never calls, every cited symbol
   in the byte-identical region. No alarm filed because the measurement did not support one.
5. **The marker-clobber fix proven EXERCISED, not merely committed** (W3-uuxp): cse's
   last_write_iso survived a stamp 2h22m newer — discriminating evidence a short-tuple writer
   would have destroyed.

AC8's three restraints are the strongest of the wave: no producer run, no marker PUT (which would
have manufactured the object whose absence is a card's central measurement), no batch re-staging
(one copy would have "fixed" finding 2 and destroyed the evidence).

## Scope

PASS closes the TO against itself and the certified decomp id space. The set-level multi-writer
hazard stays at the issuer's record with W3-thav carrying the one documented race site; the
schema-ergonomics fact (two independent lanes, same three wrapper drifts) rides to the contract
owner.

— 3.0.0_SA_CVO
