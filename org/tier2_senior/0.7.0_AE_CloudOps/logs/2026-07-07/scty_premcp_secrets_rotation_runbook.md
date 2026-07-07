# 0.7.0_AE_CloudOps~B -- SCTY_PREMCP secrets-rotation runbook + JWT break-glass

**archetype:** SCRIBE
**secondary_archetypes:** TRACE, DIAGNOSE

Window: ~1811Z -> ~1845Z. Pulled from today's /prd-delta dashboard sweep (COO), self-contained,
no gate.

## Summary

Wrote `docs/runbooks/m365-gateway-secrets-rotation.md` covering the 3 secrets the m365-mcp-
gateway needs to function: the RS256 JWT signing key, the Fernet cache key, and the Graph
(Entra) client secret. Fully source-grounded before writing a single command (Rule 22
mechanism-grounding, not symptom-only) -- read `app/config.py`, `oauth_as.py`,
`token_broker.py`, `revocation.py`, `deploy-to-ec2.sh`, and `secrets-iam.tf` end to end before
drafting.

## What grounding actually surfaced (not obvious without reading source)

1. **No runtime Secrets Manager calls at all.** The gateway reads everything from `os.environ`
   / `.env`; secrets are fetched ONLY at deploy time by `deploy-to-ec2.sh`'s on-box SSM step.
   There is no Secrets Manager rotation schedule/Lambda configured for any of the 3 -- rotation
   today is 100% manual.
2. **The JWT signing key is a single in-memory keypair, no JWKS multi-`kid` support.**
   `oauth_as.py::validate_access_token`/`validate_refresh_token` both call
   `jwt.decode(token, _public_key, ...)` against ONE key loaded at process start. This is the
   load-bearing fact for the whole break-glass section: rotating the key + restarting the
   service INSTANTLY invalidates every previously-issued token for every user, atomically --
   the rotation IS the token-invalidation mechanism, no separate revocation-list bulk-populate
   needed.
3. **A faster, surgical kill-path already exists** (`revocation.py`'s `revoke-jti`/`revoke-user`
   CLI, hot-reloaded deny-list, no restart) for a single-user/single-token suspected compromise
   -- documented as the FIRST response before reaching for the full key rotation, since it
   doesn't force every other user to re-authenticate. Verified the CLI's EXACT argv handling
   (only `revoke-user <email>` is exposed -- the underlying function supports an optional
   cutoff timestamp, but the `__main__` block never passes one through) rather than assuming
   the function signature was the CLI's interface.
4. **Rotating the Fernet key breaks every existing encrypted per-user token cache** (same
   single-key-no-rotation-support shape) -- documented as expected fallout for a routine
   rotation, not a bug to route around.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-which/rail` | native Read/Grep for source grounding across 6 app files + deploy script + TF; native `aws` was not needed (no live AWS calls required for a doc-only TO) | rail respected -- pure source-reading task |

## Files Modified

- `docs/runbooks/m365-gateway-secrets-rotation.md` (new).

## Blockers

None.

## Current State (zero-context handoff)

Runbook committed (`465a9ba7f`), covers routine rotation (all 3 secrets) + JWT break-glass.
Every command in it was checked against live source, not assumed -- including fixing two
things I initially got wrong before committing: (a) the deploy invocation must go through the
canonical `safe-ec2-deploy.sh` wrapper (Rule 7), not the service script directly; (b) the
`revoke-user` CLI does not actually expose a cutoff-timestamp argument, only the underlying
function does.

## Next Steps

- [2.0.0_SA_COO] TO ready for close -- both acceptance criteria met (concrete/source-grounded
  runbook exists; break-glass addresses token invalidation explicitly). RAVC incoming.
- Flagged in the runbook itself (not actioned, out of this TO's scope): no JWKS `kid`-rollover/
  graceful-transition mechanism exists in this codebase -- every key rotation (routine or
  emergency) forces ALL users to re-authenticate. Worth a future design conversation if that
  blast radius becomes an operational problem; not something this doc-only TO should fix.
