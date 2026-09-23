# IRPT P current state

Updated 2026-09-23 23:52Z. Owner 2.0.0_SA_COO~P (Claude, PID 19936, successor to the Codex seat closed 22:38Z). Andrew's goal record f7aaa01da1: Performance done end to end and linked up for every firm client at 49 Financial, Inflection and Cottonwood (Cottonwood structurally sound, ~May-2026 window disclosed); /loop 20m cron c45ea4b2, STOP on /verify SOUND or Andrew's word. Product incomplete: no signed-in Performance journey proven yet.

## Holdings (P's deployment hop DONE; journey is M's)

Schema repair applied under CTO GO d8e9d68378: irpt-holdings CodeSha l/GQrFcEvWMVPyRmZAGooQLtNdwaHAe+Cvy/23FUDDU= at 23:00:52Z, post-plan No changes, recorder 7a356ba08e, ledger irpt-holdings-schema-20260923 CLOSED (publish branch 5c8d6f8e34). CTO d78fdb2f1c item 1 verified it by a different instrument (Code.Location download = 97f190ac). M's COT publication 93f930c265 verified (item 2). Open at P: the NOT_READY defined-code render -- addressed by the contract addendum below (item 3).

## Performance (candidate installed nowhere; CTO review/GO pending)

Branch irpt-smoke-p-backend-20260923 (LOCAL): 642c3704cb lock; 9f01ffea18 + 560445f857 merges of CLOUD (naming-gate ddfc91b11f and ae754f525f, CTO grants); 561b1b47d5 retained.tf + lambda.tf (naming-gate PASS 4); b3fc529601 the 31 Y files (31/31 hash-equal to Y 2874e37647); 17e94dbdc6 source-map row (61 members pinned at b3fc529601, upload fields); 22c3afda53 receipt PERFORMANCE_INSTALL_CANDIDATE_20260923.json.

Package: s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip VersionId h.hlJhL3dKXAFT5NsNzceZX6Jls_f39V, 358117 bytes, content-sha256 JwJEEQGTENJJukTvrNQt3dq6VIAI8xqioIYA1atL+hk=, 61/61 members read back by version. Delta from the CTO-reviewed v4 (5cdb889b5e): retained.py @f04d1e71bd, authorization.py + runtime.py @068e9ccd85 (CTO item 6 review in progress). Native layer: s3://opal-313476888478-lambda-layers/irpt-performance-native-layer.zip VersionId tf.fKYdfNRbn9AGt1AEHqn35f6bwGqPb, sha256 121b8407415ce803458f52de03d11d81d26791f94d20f4130658a773cd1f39f6. Saved plan .runtime/performance-install/install.tfplan SHA256 f0a189191e4f566f8cd76673ee8fb83f707f78c07e6f75dd7bad1a7d2b247a55: 3 create (native layer version, retained policy, the never-applied selection-read policy), 1 update (irpt-performance-adapter -> runtime.lambda_handler, 120s, 1536MB, both layers, env without transport mode), 0 destroy; artifact data read deferred to apply, disclosed. Live function unchanged: jVktMAiRK+2mYPXEzyst6HjSFFv4xR3Kxm47hAyulyw= (2026-09-21). approved_performance_plan null: no vendor egress, no secret grant. X10 PENDING_ENFORCEMENT: this plan grants COT's two families only; whether install may precede enforcement is the CTO's call. Sent 99804.

NEXT on GO: open a deploy ledger, re-check artifact/layer versions, safe-apply f0a18919 from this worktree, readback, zero-diff, exact-function recorder, then the Anna signed-in journey (selection -> retained report -> reopen without vendor call -> export) at localhost:5174 through CloudFront. Then 49F/INF linkage: no Performance grant for those firms exists in this plan; a bounded per-firm plan follows with the CTO.

## CTO ruling batch d78fdb2f1c (99796) -- P items

- 4(1) DONE: canonical_profile_reads.py projects createdAt (created_at fallback), role, userType; 47 _scope tests pass; commit 185dfb3e7f. The Y-owned test test_canonical_profile_consumption.py:46 must gain the four projection fields (routed to Y; P's edit there was refused by the owned-paths lane, correctly).
- 4(4)+5 PLAN READY: ycharts root ec8b4dda8d, plan 1de760399ca1cd7f42e4b570c705f8e464500a1ba31a3da64a6a329d4c35006d (0 add / 3 change: generate + runner policies gain Query email-index, GetItem opal-users-v2, kms:Decrypt on the users table's own key via DynamoDB -- the Decrypt is flagged as an addition; instance tags gain AutoShutdown=disabled; declared state stays stopped). Receipt YCHARTS_AUTHORITY_PLAN_20260923.json (66ae2d58f6). No apply.
- 3 CONTRACT ADDENDUM: CONTRACT.md names the 14 PUBLIC_REASONS in the FE-s-40 generator's grammar (2cdbe2bd60); 11 become named, CONFLICT/SUPERSEDED/UNEXPECTED cannot under the underscore rule and are recorded. Portal regeneration (gen-named-codes.mjs reads the contract at a committed <WS>/portal layout) follows CTO acceptance.

## Surprises routed, not chased

- Y integration gap: the granted ycharts/generate/normalized_input.py imports TEMPLATE_SCHEMA_VERSION from intake/portfolio.py, which exists only at Y 2874e37647 (that commit also changes 10 intake files outside the 31-path grant). The consumption test fails at collection in P's tree; the resident generate path would import-fail the same way. Owner: CTO (grant scope) + Y.
- YCharts host: Y 99802 asks for aws_ec2_instance_state -> running; not done, per CTO item 5 sequencing (tag first, start when the resident install is ready).

## Runtime / preservation

Backend C:/Users/AndrewBerman/Desktop/irpt-smoke-p-backend-20260923 (this file), publish C:/Users/AndrewBerman/Desktop/irpt-p-publish-20260923 @5c8d6f8e34, frontend C:/Users/AndrewBerman/Desktop/portal-local-live-20260923 @c70855f3. Dirty and preserved: infra/aws/lambda/ci/source-map-reconcile-audit.jsonl, untracked investor-reporting/CHANGELOG.json and .runtime/. The Codex driver PID 3520 for this serial is MSTR's to retire (99775). Shared pushes are 0.0.0_AB_MSTR's; every hash above is LOCAL.
