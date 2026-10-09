# TCKT_VNEXT workstream SA -- L9 grades

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~05:2xZ, on `org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.SA.md @8c48e44f64` (msg 2549). Row D2-S13.

| criterion | verdict | evidence |
|---|---|---|
| SA-c1-AC2: the census covers EVERY portal route (no root missed), and each verdict follows from its cited line | MET | N = 117: 116 declared routes over 8 Terraform roots plus the console-only `$default`, which equals the live route count this seat read over every page of the API at ~03:3xZ (F10 grade). Each resolved verdict cites its line. The 3 it cannot resolve from source (2 `trade-identifier-cache` routes with no repo source, `$default`) are named UNRESOLVED, not forced. `inf-pipeline` is a different API, read and excluded |
| TO-APPLY-SA1 AC2: the deploy's after-reads | MET | This seat's live read: CodeSha256 = the uploaded package `ywAvsfx...`, LastModified 04:57:46Z, Successful, 8 env keys. `lambda_function.py` at pin 6e19a53535 hashes `21fe06e0...`, the deployed member the applier downloaded and hashed. Unauthenticated POST 401, ItemCount 13, replan 0-diff (the applier's reads) |

**Notes (no grade change):**
- The plan also moved `s3_object_version`. That is how this module pins its artifact, and F10's accepted plan moved the same attribute.
  The order's "source_code_hash only" was imprecise wording, not a widened act.
- IRPT `routes.json` states a `_denominator` of 19 and holds 21 (row D2-W6-S3).
- Row D2-W6-S2 (data-refresh admits callers with no userType) stays ARMED. Its fix is outside this project, and SA-r-1 must not use a
  token that reaches those routes until it lands.
