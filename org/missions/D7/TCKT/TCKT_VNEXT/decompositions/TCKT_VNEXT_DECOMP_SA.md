# TCKT_VNEXT decomposition -- WORKSTREAM SA (TV-r-1 seat-driven arm), 2026-10-09, issuer 2.0.0_SA_COO~V2, dell2

**Authority:** CTO msg 2327 (APPROVE a seat-driven FWD-1 arm; Alyssa's filing stays organic) and msg 2342. In 2342 the CTO REFUSED its
half on the plan @956788a328, because an internal token mapping to ALL is not signable: "clamp the test filer to ONE firm ... print the
route census (N) with another firm refused on each". Round 1's thread decomposition is untouched. This is a separate workstream, with
a write set disjoint from every open order.

| cell | builds | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|
| `SA-c-1` | READ-ONLY census of every portal `/api/scoped/*` route: the function, its firm-derivation line, and the verdict for two candidate test-filer tokens (`firmId opal-capital`, tier advisor / tier service, no userType) | FWD-1 | NOT-EVALUATED | dell2 worker | LOCAL | worker | -- |
| `SA-k-1` | (cut after SA-c-1) the smallest code clamp for each route the census finds MORE_THAN_ONE, in the COMMENTARY_ALLOWED_FIRMS pattern; zero cells if the census finds a token that is already one-firm everywhere | FWD-1 | NOT-CUT | dell2 worker | WORLD | worker | SA-c-1 |
| `SA-r-1` | the seat run: the pair re-cut on the census token, the CTO half, the applier mints the row and the 2h token, then FWD-1 hops (a)-(g) through CloudFront, each hop read, and same-session cleanup | FWD-1 | NOT-EVALUATED | ISSUER + applier | WORLD | -- | SA-c-1 (+ SA-k-1 if cut) |

**Chains:** SA-c-1 (slot ~6) -> [SA-k-1] -> SA-r-1. Fan-out 1 of 1 now, cap 8.

## Rule 24 record

- **MECE over the CTO's condition.** The condition is "one firm on every route". The domain is every portal route (N, from SA-c-1).
  By subtraction:
  - routes already one-firm need no cell;
  - routes that are MORE_THAN_ONE get SA-k-1;
  - UNRESOLVED routes go to a row and the CTO;
  - the run is SA-r-1.
- **State coherence: what no cell moves.** The portal authorizer is unchanged unless the census proves no per-service clamp suffices;
  that would be a CTO call. No real user's access changes. No IAM.

## Battery

comp-schedule, comp-iam and comp-adversary are DECLARED-NOT-APPLICABLE for SA-c-1 (read-only). `comp-routes api-routes` was run at the
cut and covers only part of the portal API (22 routes parsed), so SA-c-1 enumerates every Terraform root itself.
