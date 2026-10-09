# The edge book check is live on both planes, and the fifth probe names the refuser -- 0.7.0_AE_CloudOps~AB2

**Date:** 2026-10-09
**Task Order:** ADVI_BILLING.TO-AB-e-1 (edge-book-probes) @ff89e118c1
**Status:** COMPLETE

**archetype:** VALIDATE

---

## Objective

Prove live, for household `z08219260`, that (a) the CloudFront edge admits an advisor to
`/api/scoped/partners/books/relationship/{id}/*` only when the ownership map lists `{id}` under the JWT's
`advisorId`, with `role`/`firmRole` `admin` bypassing, and (b) the API authorizer refuses a request that did
not come through CloudFront. Five GET probes, five synthetic 10-minute RS256 tokens, under a deploy-completion
ledger, no token or key byte stored.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find --name 'jwtPublicKeys.mjs' infra/aws` | PASS | found the shared key module after the path in `jwt.ts`'s import (`./lib/authkeys/`) turned out to be a build-time mirror that does not exist in the tree |
| comp-find | `comp-find --name 'tier_policy.mjs' infra/aws --limit 5` | PASS | two copies (edge + shared-advisor-router), which is what the file's own header says to expect |
| comp-find | `comp-find --name 'proof_of_spec*' org/standards --limit 10` | PASS | located the schema whose enums this cell's instance had to satisfy |
| deploy_ledger.py | `open` / `close-leg` x5 / `close` | PASS | staged-not-committed each time exactly as the TO warns; seven commits |
| proof-of-spec-check.py | `proof-of-spec-check.py <instance> AB2-1-AC1` | PASS | VALID |
| r2_checks.py | `r2_checks.py . AB2-1-AC1` | PASS | base FAIL, post-work PASS, two mutants fired |

**What worked:** `comp-find --name` twice resolved a path the source's own import statement pointed away
from. The rail's F1 denial caught a `find`-shaped search for the inbox message and printed the remainder,
costing one round-trip.

**What failed:** nothing crashed. `comp-find 'proof_of_spec' org/standards --limit 10 2>&1 | tail -12` was
denied under F4 (a census piped into a receiver that can cut the denominator) -- correct denial, my pipe.

**Gap found:** none.

---

## Deployment Sequence

Nothing was deployed. This cell is five GET requests, one `GetSecretValue` and one `GetObject`; no write to
any AWS resource, no Terraform, no change to any user, role or table.

| Step | Action | Result |
|------|--------|--------|
| 1 | open ledger `advi-billing-edge-probes-r2-20261009`, 5 verify legs | `496e0676e0` |
| 2 | one process: map read, 5 mints, 5 GETs, record written | `4d8f74ffb3` |
| 3 | close-leg L1 (in_book) | `41a5176833` |
| 4 | close-leg L2 (out_of_book) | `45a5a489c6` |
| 5 | close-leg L3 (firm_admin) | `aca2ec52cc` |
| 6 | close-leg L4 (other_firm) | `2a609f5a0a` |
| 7 | close-leg L5 (execute_api_bypass) | `8d9225dd76` |
| 8 | close ledger, sentinel removed | `606da36dc7` |
| 9 | surprise rows D2-S2, D2-S3 | `6e8fe1d122` |

### The five statuses

| class | advisorId | via | status | what refused, measured |
|-------|-----------|-----|--------|------------------------|
| in_book | `chase_bertrand` | cloudfront | 200 | nothing; the map lists `z08219260` under this advisor |
| out_of_book | `abby_horton` | cloudfront | 403 | `Advisor scoping: not authorized for this resource` (`index.mjs:529-543`) |
| firm_admin | null | cloudfront | 200 | nothing; `firmRole admin` short-circuits before any S3 read (`index.mjs:468-470`) |
| other_firm | null | cloudfront | 403 | `Advisor scoping: missing identity claims` (`index.mjs:478-492`) |
| execute_api_bypass | `abby_horton` | execute_api | 403 | `opal-portal-authorizer`, by its own log line |

The fifth status is not left as an inference from `{"message":"Forbidden"}` -- API Gateway returns that body
for a resource-policy deny and a missing authorizer too. `/aws/lambda/opal-portal-authorizer` logged
`Origin verification FAILED - request did not come through CloudFront` at `2026-10-09T09:00:56.511Z`, 1 of 1
matching event since 08:59Z, which places the refusal in the authorizer's `isOriginVerified` branch
(`portal-authorizer/index.mjs:340-351`).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Mint with `opal/auth/jwt-private-key`, not the secret the TO named | The TO names `opal_auth.SECRET_ID`, which is `opal/auth/jwt-public-key` -- the verifier's key, which cannot sign. The private id (`auth-handler/src/jwt.ts:8`) is the only one whose RS256 signature the edge's `verifyWithSlots` accepts. Both ids are recorded; row `ADVI_BILLING-D2-S2`. |
| One process for mint + probe | The only way "never store or log a token" is structural rather than careful: the key and the five tokens exist in one Python process's memory, are never printed and never reach a command line. The record writer refuses on the same `eyJ...` regex the criterion applies. |
| `firm_admin` and `other_firm` carry no `advisorId` | The TO specifies `advisorId` for `in_book` and `out_of_book` and omits it for the other two; the record's field is documented as "(or null)". The cost is that `other_firm` lands on the identity-claims arm rather than the cross-firm one -- row `ADVI_BILLING-D2-S3`. |
| Work in the shared tree, not a linked worktree | The criterion is graded at root `.` and reads the sentinel's ABSENCE; a ledger opened in a worktree is invisible to the shared tree's `deploy_ledger.py check --red`. Four files, tight pathspecs, `safe-commit.sh` guarding the index. |
| Read the authorizer's CloudWatch log | A 403 status alone cannot distinguish the authorizer from a resource policy. The read is not a sixth probe and writes nothing. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.7.0_AE_CloudOps~AB2/AB_E1_PROBES.json` | the record: 5 probes, ledger slug, mint/key-read times, both secret ids | Yes -- `4d8f74ffb3` |
| `org/critical_paths/change_management/20261009T0855Z_advi-billing-edge-probes-r2-20261009_deploy_completion.md` | opened, 5 legs closed, closed | Yes -- `496e0676e0` .. `606da36dc7` |
| `org/critical_paths/.open_deploys/advi-billing-edge-probes-r2-20261009.json` | sentinel created, then removed at close | Yes -- `606da36dc7` |
| `org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md` | rows `ADVI_BILLING-D2-S2`, `-D2-S3` appended | Yes -- `6e8fe1d122` |
| `.../deliverables/0.7.0_AE_CloudOps~AB2/ADVI_BILLING.TO-AB-e-1.edge-book-probes.proof_of_spec.json` | the instance, VALID | Yes -- see the complete commit |
| `org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-e-1.edge-book-probes.md` | `<status>` pending -> complete | Yes -- see the complete commit |

---

## Blockers

None.

---

## Current State

TO-AB-e-1 is COMPLETE: `AB2-1-AC1 PASS` (`in_book=200; out_of_book=403; firm_admin=200; other_firm=403;
execute_api_bypass=403`), the ledger `advi-billing-edge-probes-r2-20261009` is CLOSED with all five verify
legs proven and its sentinel removed, and the proof-of-spec instance validates. Two sealed mutants fired as
expected (a dropped probe class -> FAIL on the five-class test; `ledger_slug` re-pointed at a slug whose
sentinel is still open -> FAIL on the closed test) and the record was restored from git with a clean
`git status`. Nothing is deployed or pending on the applied plane. Two rows are open for the issuer:
`ADVI_BILLING-D2-S2` (the order's named signing secret cannot sign) and `ADVI_BILLING-D2-S3` (the cross-firm
arm of the edge check is ABSENT, not exercised-against).

---

## Next Steps

1. **[2.0.0_SA_COO~B2] Read the five statuses against FWD-1's expectations** -- all five matched what the
   order stated, but `other_firm` matched for the wrong reason (row `ADVI_BILLING-D2-S3`), so what round 2
   may claim about cross-firm containment is narrower than the status table suggests.
2. **[2.0.0_SA_COO~B2] Decide whether a later cell cuts the cross-firm probe** -- one GET with `firmId`
   mockadv plus an `advisorId`, plus a `head-object` on `platinum/mockadv/ownership_map.json` to predict
   which of the three arms should fire. This order's refusal clause forbids a sixth probe here.
3. **[0.7.0_AE_CloudOps~AB2] Event-driven hold** -- act on the next `[INBOX]` event the same turn; re-arm
   the Monitor on its `[WATCHER-EXPIRED]` line, same turn, one call, no skill load. Seated for ADVI_BILLING
   only.
