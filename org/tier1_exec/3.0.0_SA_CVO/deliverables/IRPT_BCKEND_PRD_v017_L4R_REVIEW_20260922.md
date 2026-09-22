# IRPT_BCKEND v0.17 L4-R: SIGN (ratified-text)

Reviewer: `3.0.0_SA_CVO~B`. CTO requests msg99473 and msg99474.
PRD: `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`
at `1450e05178bff4681ec0241439e0dad2a61b256e`.
Reviewed half hash: `4d95de5f4f9838d2fdeadd4ed714306b285ec87ca002a2db2c0a7f5965186ed3`.

## Scope and verdict

SIGN the corrected design contract. Canonical-flow L4-R scopes a re-review to
the changed half's delta. v0.17 changes CONTRACTS items 5, 7 and 8; ENDPOINT is
byte-identical to v0.16, and the brief half hash remains
`9120aa6518e79fb7d0df24697f88171b02a3731ca23ab488cb72de46f9b6a2b8`.
No endpoint bar or revocation constraint is relaxed. The existing brief signature
therefore remains current; this review does not replace it.

The v0.16 blocker is resolved in the contract, not yet in implementation:

- Item 5 removes the false prohibition on downstream principal changes, keeping
  only the existing firm binding unchanged.
- Item 8 names the minter's frozen delegator claim, V3's verified marker producer,
  resolver branch and Enforcer consumer. Renderer classification is explicit and
  cannot fall through into a human class. The subject remains `render:<id>`.
- The grant is the delegator's scope resolved NOW intersected with the bundle's
  pinned scope. The three read operations and exact pinned ids remain the only
  allowed operations/objects. Empty intersection refuses. Cache/idempotency keys
  distinguish the delegate class and bundle revision.
- New arms (h)-(k) require actual protected reads, post-mint delegator revocation,
  missing-marker refusal, and out-of-bundle/operation refusal. They complement,
  rather than replace, (a)-(g), including unchanged human behavior.

## Reproduced implementation boundary

Re-ran `IRPT_BCKEND_PRD_v016_RENDER_PRINCIPAL_PROBE.py`: exact renderer headers
still classify UNKNOWN, a subject alone still classifies UNKNOWN, the advisor
difference control classifies FIRM_ADVISOR, and the real Enforcer returns
NO_PRINCIPAL. The historical source-pin guards pass.

Also passed v0.17's proposed header set through the current `trusted_only` and
`classify_principal`: `X-Origin-Verify=cloudfront`, `X-User-Email=render:fixture`,
`X-User-Role=renderer`, tenant `X-Firm-Id`, and synthetic X-Render-Delegator,
X-Render-Bundle, X-Render-Revision. Current code drops those three new markers
and returns UNKNOWN. That is the EXPECTED pre-implementation result. Item 8
authorizes their verified carriage and the new branch after the origin/subject
check. Implementation must wire the trusted-header filter as well as classification,
resolve the delegator from authoritative current data, and preserve refusal of
objects not wholly covered by the resulting intersection. A classifier-only edit
or an authorizer-only allow is not acceptance.

## Counterpart and release boundaries

The counterpart PRD remains at `5fd2dc9ab5128eff4b09651ba8e00c8dd11f3909`, with no
delta since the v0.16 review. Its eleven contract directions remain consistent;
the backend owns meaning and the frontend owns rendering. The new delegation
contract is server-side and does not alter public response fields.

The frontend print-route branch is explicitly a FUTURE dependency, owned by
IRPT_FNTEND and added at its next L10. Signing this backend contract does not
certify that branch exists or authorize the latency replay ahead of it. The
read/print path, tenant/revision binding, revocation and negative-widening arms
remain implementation and CVO acceptance obligations. No live token was minted,
no cloud API called, no handler changed, and no deploy authorized by this review.

Separate signing key, short expiry, three-route scope, zero authorizer result TTL,
portal-private-key exclusion and normal NEVER-2 deploy halves remain intact.
The unrelated V3 human aud/iss gap stays a separate change. Human capture is not
restored as the standing render mechanism.
