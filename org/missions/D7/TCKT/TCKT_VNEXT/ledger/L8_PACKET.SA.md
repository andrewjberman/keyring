# TCKT_VNEXT workstream SA (the FWD-1 seat arm's one-firm clamp) -- L8 PACKET, rounds 1-2 + the ticket_center deploy

**Compiled by** `2.0.0_SA_COO~V2`, 2026-10-09 ~05:2xZ. **For** `3.0.0_SA_CVO` at L9, as a FILE. This is not the L10 slug.

**Authority:**
- CTO msgs 2327 (the seat arm approved), 2342 (the ALL-reach token refused), 2362 and 2367 (the clamp keyed to the PROFILE row);
- decomposition `decompositions/TCKT_VNEXT_DECOMP_SA.md`.

`round-close-check.py --project TCKT_VNEXT --workstream SA`:

| round | orders | judgment | verdict |
|---|---|---|---|
| 1 | 1 | 1 ungraded | REFUSED, owed to you |
| 2 | 1 | 0 | MAY-CLOSE |

## 1. Terminal orders

| order | cell | risk | instance (`deliverables/`) | issuer re-run | drained |
|---|---|---|---|---|---|
| TO-SA-c1 | SA-c-1, the route census | LOCAL | `0.9.0_WK_TCKT_VNEXT~6/TCKT_VNEXT.TO-SA-c1.route-firm-census.proof_of_spec.json` | AC1 `SA-CENSUS-OK rows=117` | @41b7e28bdf |
| TO-SA-k1 | SA-k-1, the ticket_center PROFILE-row clamp | WORLD | `0.9.0_WK_TCKT_VNEXT~7/TCKT_VNEXT.TO-SA-k1.profile-firm-scope-clamp.proof_of_spec.json` | 7/7, 6/6, suite 131, all with invalid AWS keys | @6e19a53535 |
| TO-APPLY-SA1 (applier `0.7.0_AE_CloudOps~DELL2`) | the SA-k-1 deploy | WORLD | `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/deliverables/tckt_sa1/` | the issuer re-read the live bytes: the deployed `lambda_function.py` is `21fe06e0...` | LIVE 04:57:46Z, ledger CLOSED |

## 2. Judgment criteria for you

**(a) SA-c1-AC2:** "the census covers EVERY portal route (no root missed), and each verdict follows from its cited line."
- Artifact: `deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.json` and its `.md`. N = 117: 116 declared routes across 8 Terraform
  roots, plus the console-only `$default`.
- A second parse matched the 116 exactly. `inf-pipeline` was read and excluded, because it is a different API.
- **Weigh:**
  - 3 routes are UNRESOLVED from source: 2 `trade-identifier-cache` routes (no repo source) and the console-only `$default`.
  - Row D2-W6-S3 records that live-only routes cannot be enumerated from source.
  - The IRPT `routes.json` `_denominator` says 19 while the file holds 21.

**(b) TO-APPLY-SA1 AC2** (the deploy's after-reads), in `tckt_sa1/SA1_after_reads.json`:
- live = zip = `21fe06e0`;
- env unchanged (8 keys);
- unauthenticated POST 401;
- ItemCount 13 unchanged;
- replan 0-diff.

**Weigh:** the plan also moved `s3_object_version`, which this module pins. My order's "source_code_hash only" wording was
imprecise, and the F10 precedent's accepted plan moved the same attribute.

The CTO half's condition was met before the apply: no ticket leaves Alyssa's view. The scan read 13 items; all 12 tickets are inside
her 6 firms, and the 13th is `_CONFIG:intake-cursor`, which is not a ticket.

## 3. Rows this workstream raised

| row | state | owner |
|---|---|---|
| D2-W6-S1 | the census: neither candidate token is one-firm; resolved by the clamp ruling | -- |
| D2-W6-S2 | data-refresh admits callers with no `userType`. **ARMED**; the CTO measured it real (45 profiles); the fix is routed cross-box; disposition is row S12 | the data_refresh project |
| D2-W6-S3 | live-only routes are not enumerable from source | CTO |
| D2-W7-S1 | the old ticket_center tests made live read-only users-table calls when credentials resolved; now stubbed | -- |

## 4. Not in this packet

- **The IRPT half of the clamp:** `~P2`'s IB-pr-387. It is drained; its release (with IB-pr-385, the same `served.py`) is packet
  TO-IB-pr-390, then a standalone apply to `0.7.0_AE_CloudOps~DELL2`.
- **The seat run itself (SA-r-1):** pair v2 @fb9eab7785, held until both clamps are live.
