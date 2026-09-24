# Export hop -- design card (goal criterion 1, last hop, all three firms)

By 2.0.0_SA_COO~P, 2026-09-24T23:5xZ. Measured, read-only; no vendor call; no credential value printed.

## Conclusion

The export hop is NOT BUILT end to end, and most of what is missing is NOT code: the render identity
(PRD `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md:177-262`, Andrew-direct option 2, 2026-09-22) was
built OFFLINE in rounds 17-18 and its live landing was deferred ("provisioned in a LATER round",
`_render_identity/mint.py` header). No later round landed it. Until it lands, every render refuses
`SESSION_ABSENT` by design.

## Measured state (each row read 2026-09-24 23:4x-23:5xZ)

| # | Link | State | Evidence |
|---|------|-------|----------|
| 1 | Served submit route | NOT WIRED: answers `NOT_READY` for every submission | `export/entry.py:188-199`; deployed `irpt-export-render` = `entry.lambda_handler`, CodeSha256 `2gSDyxxB..`, 2026-09-21 |
| 2 | Controller (freeze, persist-before-render, dispatch) | BUILT, unserved | `export/handler.py` `submit_export`; reachable only via `handler.lambda_handler`, which is not the deployed handler |
| 3 | Render host | READY | `dispatch.preflight()`: `i-0167fd745ad906a66` running, SSM document `irpt-export-render-run` v4 present |
| 4 | Host render runs | 11 SSM commands in retention, ALL `Failed`; last 2026-09-21 16:12Z | last stderr: `BLOCKED: SESSION_ABSENT -- the print route answered with a sign-in screen` |
| 5 | Rendered PDFs | 0 `report.pdf` under `opal-data-ycharts/firms/` (2 export objects total) | S3 list, paginated |
| 6 | Render signing keys | ABSENT | `describe-secret` `opal/auth/irpt-render-jwt-private-key` and `-public-key`: ResourceNotFound |
| 7 | V2 authorizer render branch | CODED (`infra/aws/users/lambda/portal-authorizer/index.mjs`, 18971693ad), NOT DEPLOYED | deployed `opal-portal-authorizer` (09-09) and `opal-portal-rest-authorizer` (09-03): 0 `irpt-render` occurrences |
| 8 | V3 edge render branch | CODED (`infra/aws/lambda-edge/auth-validator-edge/render_auth.mjs`, 5efd6b36e8), NOT DEPLOYED | deployed `auth-validator-edge` (09-15): 0 occurrences |
| 9 | Minter | CODED, offline (`_render_identity/mint.py`, bf31746c43) | no caller on the served path |
| 10 | Portal print route admission | BUILT (FE-s-88, `portal/src/components/ProtectedRoute.tsx` `allowRenderClaim`) | on the portal submodule at 13b5356f |
| 11 | Principal resolution for a renderer (PRD item 8) | CODED in `_scope/resolve.py` (28 matches) | not yet exercised live |
| 12 | Finalize (PDF -> receipt) on the served path | NO CALLER | `handler.finalize_export` runs only when invoked; nothing invokes it after the host writes the PDF |

## Build order and owners

A. RENDER IDENTITY LIVE LANDING, outside P's lease surface (the shared portal auth plane):
   A1 mint the two-slot key pair into `opal/auth/irpt-render-jwt-{private,public}-key` (Terraform, never a CLI mint);
   A2 deploy V2 (`opal-portal-authorizer`), the render branch only;
   A3 deploy V3 (`auth-validator-edge`, Lambda@Edge, every portal request crosses it).
   Owner: to be named by 1.0.0_SA_CTO. A2 and A3 are WORLD acts on a verifier every user crosses; each needs its own
   ledger entry and a negative arm (a human token and a render token on a non-print route are both still refused).
B. IN P'S LANE (`export/`, `_render_identity/`), buildable now, dark until A lands:
   B1 serve `submit-export` for a RETAINED report: resolve `(report_id, revision)` through the reports repository
      under the current principal, freeze the bundle with `authorized_report_revisions` = that ref, and the package
      facts carried with the build (the Lambda cannot read portal TS). OPEN: `narrative_packet_ref` is REQUIRED by
      `ExportBundle.schema.json` (`packet_id`, `revision`, `sha256`, no null), so a Performance export needs a
      narrative packet or a contract ruling; the served route must resolve it, never take the browser's sha256.
      Measured: `irpt-narrative` (entry.lambda_handler, 2026-09-21) builds a packet FROM a report the request
      supplies and retains nothing, so no retained packet exists to reference. P's pick, no contract change: submit
      runs `narrative/handler.build_packet` (imported unedited) over the RETAINED report with `cutoff_at` = the
      report's `dates.actual_end`, persists the packet as a retained artifact, and binds its sha256.
      The route answers an `ExportReceipt` with `job_state` `QUEUED` and `facts.validation_status` `NOT_RUN`
      (both in the v1 enums), persisted at `handler.receipt_key`; B3 rewrites it `READY` or `FAILED`;
   B2 mint one render token from the frozen bundle (`mint.py`), passed to the host as a parameter; the SSM document
      gains `RenderToken` and `PortalOrigin`, which `dispatch.render_request` does not send today, so a READY
      dispatch would fail on a missing required parameter;
   B3 finalize: the host's PDF write triggers `finalize_export`, or the served `export-receipt` read finalizes on
      first read (choose the one without a new event source; the header forbids a schedule).
C. PROOF: one real run per firm. COT and 49F each export a retained report; INF follows its own per-use word.

## What this card does not move

It changes no served output, deploys nothing, and does not touch the COT one-use plan (armed, unspent at 23:41Z).
