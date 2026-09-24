# IRPT P current state

Updated 2026-09-24 00:42Z. Owner 2.0.0_SA_COO~P (Claude, PID 19936). Andrew's goal record f7aaa01da1: Performance done end to end and linked up for every firm client at 49 Financial, Inflection and Cottonwood; /loop 20m cron c45ea4b2, STOP on /verify SOUND or Andrew's word. Product incomplete: no signed-in Performance journey proven yet.

## Performance -- INSTALLED (CTO-verified), journey not yet proven

Applied under CTO GO 99821 item 1 at 00:07:15Z from irpt-smoke-p-backend-20260923: irpt-performance-adapter CodeSha256 JwJEEQGTENJJukTvrNQt3dq6VIAI8xqioIYA1atL+hk= on runtime.lambda_handler, 120 s / 1536 MB, layers irpt-common:5 + irpt-performance-native-layer:1 (EhuEB0Fc..., 69899991 bytes), policies irpt-performance-retained-policy and irpt-performance-adapter-selection-read-policy, env six keys, no approved-plan env. Postflight 7/7, post-plan No changes, state serial 17, recorder ac8e2cf502, ledger irpt-performance-install-20260923 CLOSED (1af100468e), receipt PERFORMANCE_INSTALL_APPLY_20260924.json. CTO verified live on its own readback (85d1fce246).

P-REOPEN-01 landed in source at 9074dba320: the accepted pointer is keyed on {firm_id, sorted account_ids, start, end} (schema irpt-performance-accepted-v2, no owner / principal / selection in the pointer); authorization re-derived through the repository at reopen; 11 focused tests pass. Not deployed: rides the next Performance package (new pin, build-and-upload, plan, CTO GO).

X10 PENDING_ENFORCEMENT (CTO item 4): the installed function refuses reserve/promote/reopen until ACTIVE. P's next Performance deliverable toward ACTIVE is the enforcement matrix (36 destinations x deployed writer coverage; COT two families LIVE, the rest DECLARED). Then the Anna signed-in journey is Andrew's browser act at localhost:5174 (dev server up, node scripts/dev-live.mjs, CloudFront d2n2nzpeqf34ge).

49F / INF: provider calculations wait on Andrew's per-use words (CRO SmartX bounded capture plan; Orion Reporting/Scope for a real INF client) and the currency attestations (P writes the two ANDREW_ATTESTATION records into CurrencyAuthorities.json on his word, CTO 99836/99848). Structural three-firm families/IAM follow-on plan not yet drafted.

## Holdings NOT_READY render -- contract named, portal regenerated (branch only)

CONTRACT.md names the 14 PUBLIC_REASONS: 2cdbe2bd60 (accepted, cherry-picked to CLOUD as c80b8ccb41) + 2a87fa8edf (CONFLICT/SUPERSEDED/UNEXPECTED rewritten in the public_reason_code grammar; CTO re-acceptance + MSTR cherry-pick pending). Portal: worktree irpt-smoke-p-backend-20260923/portal, branch p-reason-codes-20260924 over c70855f3, commit c1ac41ec: CONTRACT_NAMED_REASON_CODES = 16 codes @2a87fa8edf, reading rule widened (public_reason_code prefix admits single-word codes), reason-codes.test.ts 2 pass, tsc -b clean. Not on the live branch codex/local-live-data-20260923 nor DEV: the live 5174 screen still flags NOT_READY until that commit is promoted (MSTR/DT act).

## YCharts authority + host tag -- APPLIED

Plan 1de76039 applied 00:17:29Z under GO 99821 item 3 (0/3/0): both roles carry Query email-index / GetItem opal-users-v2 / scoped Decrypt on key 64f25291; host i-0167fd745ad906a66 tagged AutoShutdown=disabled, still stopped (declared state unchanged; the start rides the resident cutover plan). Ledger irpt-ycharts-authority-20260924 CLOSED (c427ca4a76), receipt YCHARTS_AUTHORITY_APPLY_20260924.json.

## Y integration -- 92 of 93 reachable files exact; factory imports

d3f612d94d (7 exact copies at c4564aad17 incl. current_authority.py; 3 three-way merges == Y blobs; resident_worker.py + test at 635af92b76) and 9e87bb4202 (intake/resolution_broker.py). resident_main.py --help imports (rc 0). Per file: intake tests + resolution broker green; resident worker 29 passed with 8 errors in Y's cross-firm cases whose stub pins the 7-field profile projection literal (USER#synthetic) -- Y's file, routed. The consumption test at Y blob b35cb286b1 is refused to P by the owned-paths hook (lane IRPT_COMPLETION_Y) and stays with Y; the copy sits uncommitted in this worktree.

NEXT (Analysis side, P-owned): build_resident_runtime (ResidentAssembly with shared repositories, principal_for, profile_for = CanonicalProfileReaders(client).get_user, census), package + SHA256SUMS, cutover receipt, host role delta for the queue consumer; then Y's route-plane rows (three analysis routes DECLARED + handler composition in the generate function, irpt-status rebuild at a pin carrying 8e8498c9c0).

## Runtime / preservation

Backend C:/Users/AndrewBerman/Desktop/irpt-smoke-p-backend-20260923 (this file); publish C:/Users/AndrewBerman/Desktop/irpt-p-publish-20260923 @5c8d6f8e34; live frontend C:/Users/AndrewBerman/Desktop/portal-local-live-20260923 @c70855f3; portal worktree for regeneration at <backend>/portal (node_modules junctioned from the live portal; the `portal` gitlink reads modified in this worktree and is never staged). Dirty and preserved: infra/aws/lambda/ci/source-map-reconcile-audit.jsonl (recorder appends; owner 0.7.0_AE_CloudOps~O at the drain), the consumption test copy, untracked .runtime/. Every hash LOCAL; shared pushes are 0.0.0_AB_MSTR's.
