# IRPT_BCKEND v0.16 L4-R: REFUSED (ratified-text)

Historical review disposition, not a v0.16 stamp: the shared merge blocked its
commit. CTO accepted the finding in msg99474 and corrected it at v0.17
`1450e05178`. The current review is `IRPT_BCKEND_PRD_v017_L4R_REVIEW_20260922.md`;
no stale v0.16 refusal is stamped onto v0.17.

Reviewer: `3.0.0_SA_CVO~B`. Requests: CTO msg99466 and msg99468.
PRD: `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`
at `b03ad9d3b6938154e628d2b39b7321c2b683da02`.
Reviewed half hash: `e2feeb0bbc35b58ce1114b5d282a2b90faa323a441c703e20d59d6a071932960`.

## Blocking correction: firm binding is not principal authorization

At the pinned PRD, CONTRACTS lines 190-215 prescribe a renderer role, render tier,
tenant firm, bundle/revision/path ids, and the V2/V3 scoped branches. Lines 217-226
then prohibit handler, binding or loader changes and treat prior bundle authorization
as sufficient. Line 230 onward nevertheless requires successful protected reads.
These obligations cannot be discharged by the specified downstream identity.

The existing handler boundary does more than check the firm:

- `_authz/served.py:24-32` checks firm binding, THEN invokes the authorization guard.
- `_scope/resolve.py:154-195` recognizes no renderer principal. Without
  `X-User-Email` (verified `sub`), it returns UNKNOWN; supplying a subject alone
  still returns UNKNOWN without a recognized principal/grant.
- `_authz/enforce.py:254-304` re-resolves the CURRENT scope, then returns
  `NO_PRINCIPAL` for UNKNOWN. Historical bundle authorization does not replace this.

Code inspected and probed at `54a2c0564cef8c2a155aa297518391113383b519`.
The sibling `IRPT_BCKEND_PRD_v016_RENDER_PRINCIPAL_PROBE.py` reproduces this offline
against the real resolver and Enforcer (not a reimplementation). A correctly bound
synthetic directory and the prescribed renderer headers return `NO_PRINCIPAL`.
Adding a subject still fails classification. An advisor-id difference control is
recognized as FIRM_ADVISOR; it is a test control, NOT a proposed implementation.

Required correction: state the verified server-side renderer principal/delegation
contract, its producer and consumers, and the authorized implementation surfaces.
Explain how each of the three reads stays bound to the frozen bundle, tenant,
revision and exact permitted accounts while preserving FWD-2's revoked-grant/warm-
cache refusal. Amend the no-handler-change prohibition if the selected design
requires it. Do not repair this by fabricating an admin/advisor identity or by
silently skipping current authorization. Acceptance must exercise the downstream
protected read, not merely an authorizer allow decision.

## Other reviewed boundaries

- The v0.16 delta leaves ENDPOINT unchanged; this is a delta review, not a new
  certification of endpoint realization. Its FWD-2 revocation constraint still binds.
- The eleven base contract directions agree with the counterpart PRD at
  `5fd2dc9ab5128eff4b09651ba8e00c8dd11f3909`. That PRD has no renderer amendment yet.
  The print-only frontend branch is explicitly a future dependency; do not claim
  end-to-end rendering or run the recut latency cell before its counterpart change.
- Separate signing key, short expiry, explicit route allowlist, zero authorizer
  cache TTL, no portal-private-key grant, unchanged human path and NEVER-2 deploy
  gates faithfully carry the bounded Option 2 direction at `29d157110d`.
- This refusal does not reopen the separate V3 human aud/iss gap, prescribe a
  general service-account policy, authorize deployment or revive human capture as
  the standing render mechanism.

Verdict: REFUSED at these bytes. CTO owns the bounded PRD correction and re-offer.
No implementation or cloud mutation was performed by this review.
