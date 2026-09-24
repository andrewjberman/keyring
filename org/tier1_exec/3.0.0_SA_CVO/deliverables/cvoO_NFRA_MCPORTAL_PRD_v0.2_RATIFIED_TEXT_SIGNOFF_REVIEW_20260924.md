# L4-R re-review -- NFRA_MCPORTAL PRD v0.2, ratified-text half

Reviewer: `3.0.0_SA_CVO~O`. Subject: `org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md` @87b310f4c2.
Answers my v0.1 refusal @3702879c37. Asks: `1.0.0_SA_CTO~O` msgs 25775 and 25776 (acked). Half hash reviewed:
`b82799cb3b83902ba407e1538bbf87968244a885602607f92f05d4ef0789a691` (`prd_signoff_lib.half_hashes`; it matches the
delivered `b82799cb3b83`).

**VERDICT: SIGN.** The span reviewed is the full `git diff 842f67a802 87b310f4c2` on the PRD. The ENDPOINT is
unchanged in that diff.

| v0.1 finding | v0.2 answer | graded |
|---|---|---|
| P0: C4 had no writer, trust edge or independent identity check | C4 names a separate writer function holding the one POLICY-write role; the gateway gains `lambda:InvokeFunction` on that one function and no `sts:AssumeRole`; `ArnNotEquals` at `schwab_access_state.tf:132` STANDS; the writer verifies `x-amzn-oidc-data` itself against the regional ELB key and matches its OWN owner config; replay inside the window is named as the residual and made visible through the writer's own audit record | CLOSED. The mechanism exists at `app/identity.py:50-60` (printed); A1n adds four negative arms, including a direct AssumeRole |
| P1: C6 amended the OPLGTW contract without saying so | C6 names the amendment, is ENRICHMENT behind G-OPLGTW (holder Andrew, carried with G-MOVE); FWD-1 and A1 move to the `data_entitlement` record type that the store already holds | CLOSED. It no longer contradicts the Scope section's "does not change" list for round 1 |
| P2.1 citation drift | `access_state.py :14-16` at HEAD | CLOSED |
| P2.2 "NFRA_OPALAI's C10" | NFRA_OPALAI gained C10 (`:305`, "Every answer is scoped to the ASKER's entitlement") | CLOSED, measured |
| P2.3 owner list shared with systems accounts | C2 binds a dashboard-only list, boot-refused on any second entry | CLOSED |
| should-have-asked (G-MOVE side) | the handoff builds round 1 on the current path; the move carries the modules | ANSWERED |

## Residual notes (non-blocking, for L5)

1. **C3's stated reason is now half true.** C3 keeps the handlers in the gateway because "a second service would be
   a second identity boundary to keep in step." C4 now adds exactly such a boundary, on purpose. Two owner
   configurations now exist: C2's email list and the writer's Entra object id. Recommend the S4 order carry one
   check: both configurations name the same person, compared once at deploy.
2. **"Equivalent to `opal-gateway-access-admin`" is ambiguous.** The writer's role could be the existing operator
   role trusted by `lambda.amazonaws.com`, or a new role. Either way the trust condition must still refuse the gateway
   role. Recommend the S4 order name which one, under G-LEDGER.

-- 3.0.0_SA_CVO~O
