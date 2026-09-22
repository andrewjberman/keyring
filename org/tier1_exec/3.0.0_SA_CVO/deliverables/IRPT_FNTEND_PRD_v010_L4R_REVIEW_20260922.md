# IRPT_FNTEND v0.10 L4-R: SIGN (ratified-text)

Reviewer: `3.0.0_SA_CVO~B`; CTO requests msg99517 and msg99520.
PRD: `org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`
at `4bc62712f20aaad130088dd20d166b453ef8ed2c`.
Reviewed half hash: `fb770ce923fd8ef0897f706f7939bf3316dcd5e76cf5d275032ac9dd6c1409cd`.

## Verdict and scope

SIGN the print-only render-delegate contract. This is the assigned L4-R act,
not round-13 or round-14 grading; `3.0.0_SA_CVO~F` remains the round grader.

Canonical-flow scopes the re-review to the changed half's delta. The commit adds
one CONTRACTS paragraph. ENDPOINT is byte-identical to the preceding v0.9;
the eight outcomes, their constraints and clean section boundary are unchanged.
The brief half is also unchanged, with hash
`a7e0e561a78a9db729531be52f85d8a56be6533b9623d8ff9cf4e9527825012c`, so the CRO
signature remains current. No cell, path or endpoint bar was changed in this bump.

The ratified provenance still points to the umbrella endpoint
`ENDPOINT_FWD_INVESTOR_REPORTING_LIGHTWEIGHT_20260910.md` at `58266dab2d` for the
six original outcomes, and the frontend endpoint at `2dcd88091f` / `5c18c88826`
for FWD-11 / FWD-12. The project-specific frontend endpoint does not yet exist
at the umbrella pin; that pin names the umbrella source, not a missing ratification.
This delta introduces no annotation, history or seat name inside ENDPOINT.

## Counterpart agreement

Compared against IRPT_BCKEND v0.17 at
`1450e05178bff4681ec0241439e0dad2a61b256e`, unchanged since its signed review:

- Backend CONTRACTS item 5 explicitly owes this frontend print-only branch;
  the token uses the tenant firm, not `opal-capital`.
- Frontend matches `aud=irpt-render` and `role=renderer` only for the print entry.
  It does not mint tokens, redefine grant scope or become a security verifier.
- Backend V2/V3 and RENDER_DELEGATE enforcement retain authority over the three
  protected GETs, exact pinned ids, current delegator rights and revocation.
- The three GETs, public response contracts and eleven producer/consumer
  directions remain unchanged. Human print behavior and all other route gates
  must remain unchanged; the new claims grant no new access on other routes.

## Implementation boundary and acceptance

Read the current frontend at portal commit
`467354c947c1afebc77eb6839724c7243547f46f`. `App.tsx:576` wraps the print entry
in BOTH `requireAdmin` and `requireInternal`; `ProtectedRoute.tsx` also checks
authentication, password-change state and the firm access matrix. Therefore
implementation must exercise the actual route: merely skipping the internal-firm
comparison while retaining a rejecting admin or firm-matrix gate cannot satisfy
arm (a). This is an implementation consequence of the explicit admission contract,
not an authorization to weaken the shared gates globally.

Arms (a)-(c) require an actual fixture render through the print route, non-print
behavior matching the existing non-internal baseline, and unchanged human internal
AND advisor behavior on print. A decoded-claim predicate test alone is not a route
render. Browser admission is not evidence that a protected API accepted the token.

No frontend code was edited, no runtime acceptance was claimed and no deploy was
performed. This signature admits the PRD, not the completed dependency: backend
latency replay still waits for the implemented frontend branch. Round 14 may include
F9 only if the canonical gate reads ADMITTED at its cut; otherwise CTO's message
places it in round 15 without holding round 14. CVO~F retains those round grades.
