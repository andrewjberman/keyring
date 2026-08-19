# D7 U4 -- SERVICE-IDENTITY RULING (the Analyst's ticket-creation caller), 1.0.0_SA_CTO, 2026-08-19 ~21:1xZ

**Pulled forward under Andrew's drive word ("do not delay unnecessarily") so TO-D is not
waiting on this gate at its seat's respawn.** Scope: the shape CONSTRAINTS any implementation
must satisfy; the TO's Phase-1 grounding proposes the concrete mechanism for a one-line CTO
confirm -- ruling the frame now, not designing blind.

## RULING -- five binding constraints on the D7 intake service identity

1. **A DEDICATED SERVICE SUBJECT, never a borrowed human token.** The Analyst's POST to
   `/api/scoped/tickets` authenticates as its own principal (subject of the form
   `svc-analyst-intake`); a person's JWT reused by an agent is the stamps-vs-checks confusion
   at the identity layer and is prohibited.
2. **MINIMAL CLAIM SET:** internality + a service marker; NO admin claims, NO firm-user claims
   beyond what the ticket-create path requires. The authorizer treats the service marker as
   sufficient for CREATE only -- claim/complete stay human-token acts (the SLA's acceptance
   and execution legs are human by design).
3. **SAME VALIDATION CHAIN:** the token validates through the existing scoped-route auth path
   (auth-validator chain) -- no bespoke verification, no allowlisted bypass header. Same law
   as the D8 ruling @e697f1450e.
4. **PROVENANCE STAMPED FROM THE TOKEN:** `source = dl_intake:<firm>` from the service's own
   context; `requester` = the original DL sender (body data, DISPLAY-grade); the immutable
   caller identity is the token subject -- requester fields never masquerade as authenticated
   identity.
5. **CREDENTIAL CUSTODY per the existing secrets pattern** (the gateway's identity_scope key
   custody is the named precedent); no key material in repo, config, or prompt text.

**What the TO proposes back (one-line confirm at this gate):** the concrete issuance mechanism
(where the service token is minted, its lifetime/rotation) grounded in the auth chain's real
code -- Phase-1 reads first, then proposes. The five constraints above are not reopened by the
proposal. -- 1.0.0_SA_CTO
