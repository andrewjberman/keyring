# TCKT_VNEXT rounds 18 and 19: ONE opal-ticket-api release, both checks REL-OK -- 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY
**Date:** 2026-10-16
**Task Order:** TCKT_VNEXT.TO-R18-REL (AMENDMENT 1) with TCKT_VNEXT.TO-R19-REL folded
**Status:** COMPLETE

---

## Objective

Release the ticket service in ONE apply under the combined never-widen pair (COO half blob `643ba43746`, CTO half blob `2f52cca81d`, `built_from_sha` `de2fdb4a4f`): round 18's three routes, two attachment variables, the meeting coordinator routing and the `TicketAttachmentsTradeForm` statement; round 19's analyst-intake list, the empty client-notice contact map and the fail-closed firm scope. Procedure: the pair and the GO in the TO-R18-REL AMENDMENT 1 (issuer msg 9656, re-issued 9710).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open (5 legs), close-leg x5, close | PASS | entry `tckt-vnext-r18-r19-ticket-service-release-20261016` CLOSED 5 of 5 |
| build-and-upload.sh | `BUILD_ONLY=1`, guard printed 8 at the base | PASS | built 40287 bytes, one member, nothing uploaded by the script |
| terraform plan / safe-apply | plan -out, then apply of the planfile | PASS | 4 add, 1 change, 0 destroy; post-apply plan No changes |
| r18_rel_check.py, r19_rel_check.py | issuer's checks | PASS | both REL-OK |
| proof-of-spec-check.py | with --governing-order, twice | PASS | VALID rc=0 each |
| comp-iam | `service opal-ticket-api` | SKIPPED as evidence | ran; role not mapped, 31 calls UNKNOWN across 0 statements; the policy was read directly instead |

**What worked:** reading the live S3 object version and the downloaded live zip gave a rollback and the member-by-member comparison with no inference. **What failed:** `terraform plan` first refused (the round-18 module blocks were not installed in `.terraform`); `terraform init` fixed it. Python could not spawn the `.tools/aws` shell shim, so reads went through boto3. **Gap found:** `comp-iam` cannot map this role.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | First start, preconditions measured | STOP at precondition 2: `r19_mig_check.py` read MIG-BAD (internal rows 24, not 23: another seat's synthetic staff user, ledger `irpt-fwd1-run3-20261016`). Nothing opened, nothing written. Reported (msg 9664); issuer held it (9667) and cleared it (9710) |
| 1 | Re-measure after the clear | 8 of 8 blobs equal at worktree, HEAD, `de2fdb4a4f`; MIG-OK (19 markers, 23 rows); live CodeSha256 `Fg8MdfvC...`, 10 env keys; 86-tree sweep, no live open ledger names `opal-ticket-api` (2 hits are stale snapshots of entries CLOSED on trunk); 3 of 3 bucket policies and CORS match the pair; terraform v1.15.8 |
| 2 | Ledger opened, S1 closed | 5 legs |
| 3 | Build (sparse throwaway worktree `C:/dev/tv2-rel-r1819` at `de2fdb4a4f`) | zip sha256 `27076700238d...`, base64 `JwdnACONAnxw...`; vs live: delta = `lambda_function.py` only, equal to the tree blob `501c460978` |
| 4 | Rollback saved, package uploaded | previous S3 VersionId `BU27czeb9mc1fcnw.i5aSQbXNavPqt2g` holds the live code; new VersionId `0iVZCJN6gNZGepFpC3Fw2__53OnCuXja`; metadata and round trip equal |
| 5 | `terraform init`, plan -out | 4 to add, 1 to change, 0 to destroy; equal to the pair section 4 (CLIENT_NOTICE_CONTACT_MAP `{}`, ROUTING_MATRIX meeting primary only) |
| 6 | Pre-apply broker read | 0 rows not READ |
| 7 | `safe-apply` of the planfile | rc=0, 4 added, 1 changed, 0 destroyed, ended `2026-10-16T17:57:19Z` |
| 8 | Read-back | Active/Successful, CodeSha256 `JwdnACONAnxw...` equals the package |
| 9 | Checks, results, instances, flips | both REL-OK; two result files; two instances VALID; both orders complete; commit `d12b0d3579` (LOCAL on box/dell2) |

## Verification

```
r18_rel_check.py -> REL-OK code JwdnACONAnxw, 2 env, 3 routes once each, coordinator routing, TicketAttachmentsTradeForm on 3 prefixes
r19_rel_check.py -> REL-OK code_sha256=JwdnACONAnxwqzhsVgqgU+nRoLdmS7MyLmzXmZuXsR4= contact_map_firms=0 intake_firms=3
terraform plan (post-apply) -> No changes. Your infrastructure matches the configuration.
```

---

## Decisions Made

- Held at the first MIG-BAD rather than apply or write a marker to the synthetic row (outside the pair).
- Uploaded the package myself with `put_object` and the `content-sha256` metadata the module reads, after a `BUILD_ONLY` build, so no upload ran inside the build script.

## Blockers

None.

## Current State

`opal-ticket-api` runs package `JwdnACONAnxwqzhsVgqgU+nRoLdmS7MyLmzXmZuXsR4=` on API `7k3ed8px20`, with three new routes and the `TicketAttachmentsTradeForm` statement. **Requester ack and pickup notices are off until the firm contact map is set** (`CLIENT_NOTICE_CONTACT_MAP` is `{}` by the CTO's ruling). The release orders `TO-R18-RUN` were not started. Rollback: release first (re-apply the pre-release tree with S3 version `BU27czeb9mc1fcnw...`), then any marker. Held for rollback: `C:/dev/tv2-rel-r1819` (worktree), `C:/dev/tv2-rel-r1819-out/` (zips, plans). Records: `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r18_rel/` and `r19_rel/`.

## Next Steps

1. `[2.0.0_SA_COO~V2]` Run `TO-R18-RUN`; read the CTO's after-read from the apply-end timestamp `2026-10-16T17:57:19Z` (zero `WE_CLIENT_SENT`, at least one `WE_CLIENT_NO_CONTACT`, events scanned printed).
2. `[2.0.0_SA_COO~V2]` Tell me when the rollback copies and the worktree can go.
3. `[0.0.0_AB_MSTR]` Carry `d12b0d3579` (and this log's commit) from box/dell2 in the integration window.
