# IRPT_BCKEND~P (Performance) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
(COO_P.md, CONTROL.md apply). Reviewer `3.0.0_SA_CVO` (grades landed pins after the fact while the lease is FAST).
Drive: /canonical-drive loop on Andrew-direct 17:3xZ (cron 57c0067c, every 10m; replaced goal loop f599225b), reading `python .tools/drive-mode.py read IRPT_BCKEND~P` each tick
(C11, CTO 100817). Lease FAST until 2026-09-24T21:14:15Z at 18:25Z. Goal:
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`.
As of 2026-09-25T19:5xZ. Detail history: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/STATUS.md` (09:4xZ; branch-resident).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `irpt-smoke-p-backend-20260923` at `C:/Users/AndrewBerman/Desktop/irpt-smoke-p-backend-20260923` @55b39f2d11 |
| Publish worktree (source map + recorder) | `irpt-p-publish-20260923` @25d91fb405 |
| Workspace candidate pins today | A1 `_authz` log line 4fffe13f01; Y pin abb74dc689; C1 aa3aabe2ca; series-window fix dd1811bbaa; viewer seam 19b38e2f22; hops 2+3 composition a58859baa7; grants 54bc1359f4; M registry 0e8b5da51b; Y 522afcfd17; 49F/INF named refusal 7f6b5589f6; S125 refresh fix 82679477a6; upload contract a47102cc8f (on CLOUD aa21133b67) |
| Portal candidate pin | candidate 8 237bdfda LANDED on DEV by `2.0.0_SA_COO~D` (origin DEV 92d16efc, msg 100835) |
| Deployed artifact pins | irpt-performance-adapter `YPSX1+nS..` 21:28:08Z (49F on our engine + retention grants, ledger `irpt-performance-49f-engine-20260924` S1 open; plan unchanged; before it l3NswChj.. 20:26Z named refusal; the fix NuIaCuqn.. 18:46Z, receipt `IRPT_MVP_P/PERFORMANCE_WINDOW_REARM_APPLY_20260924.json`); irpt-directory-refresh `d5fqVJ0f..` 20:13:37Z (S125, ledger S1 on the 09-25 fire; refresh.py granted to ~M from here, CTO 100876); irpt-ycharts-generate `LdjdnnLh..` 19:49:52Z; resident package f624e8a72f 19:43:01Z (ledger `irpt-upload-hop2-20260924`, S1 open) |
| One-use plan | ARMED, unspent at 18:47Z: plan sha 99052771.., acc_d486fc94.., 2026-01-01..2026-09-24, expires 2026-09-25T00:00Z (Andrew f0bd1c267e) |
| Push state | LOCAL (both worktrees); MSTR pushes |

## Live thread

State: COT journey ARMED, awaiting Andrew's browser act (before 8 PM ET). The first use (106eaa0e..) was SPENT at 13:47:53Z and
refused by the adapter's own series-window equality check; fixed and served at dd1811bbaa / NuIaCuqn... Next failing hop is
unknown until the run: the provider call -> retained report -> reopen -> export.

## Acceptance (goal Done criteria)

| # | Criterion | State | Evidence |
|---|---|---|---|
| 1 | Signed-in journey login -> selection -> provider calc -> retained -> reopen -> export, per firm | COT ARMED; 49F SERVED on our engine (awaiting a signed-in run); INF NOT BUILT live ("Cottonwood calculation only" in bd_selected; 49F/INF requests answer INVALID_INPUT "mapping firm unsupported", log 13:47Z) | ledger `irpt-performance-window-rearm-20260924` S1 |
| 2 | Every active account at each firm resolvable in Performance | MEASURED ee51ffafac: COT 842/842 + INF 875/875 identity resolve; 49F 6692/7454 compute (724 no linkable day, 38 not in engine; both named OBJECT_NOT_COVERED) | `IRPT_MVP_P/PERFORMANCE_RESOLVABILITY_CENSUS_20260924.json` |
| 3 | COT structurally sound, window disclosed not padded | CODE: dates.actual_* = provider window beside requested_* (dd1811bbaa) | test_bd_selected 32/32 |

## Write claims

Item in hand: none building (B1 blocked on the contract ruling). Claimed surface when it un-parks:
`infra/aws/lambda/investor-reporting/export/`, `infra/aws/terraform/investor-reporting/export/`, the `irpt-export-render` source-map row.

## Next-list (in order)

0. INF ARMED 15:0xZ (Andrew-direct @dd8178481e, CTO 100945): ONE Orion call, account acc_41e2e972281c3e42ef3f7a55 (INF, the
   Transfer on Death account ending 0279 in the "Martin" household -- NOT the Roth ending 4696 the entry shows), window
   2026-01-01..2026-09-25, expires 2026-09-26T00:00Z (plan digest b0b85aa98a09..). Deployed and verified under ledger
   irpt-performance-inf-one-use-20260925 (backend 510b75ef86; modules provider-renamed orion_selected / orion_account_mapping
   d39fa9692d; source map 09b5725451 on the publish branch; CodeSha256 jbojclF3..). S1 = Andrew's signed-in request: INF,
   select ONLY that one account, Performance, YTD (the preset sends today's UTC date) before 00:00Z. A refusal spends it.
   Then read PERFORMANCE_USE#b0b85aa9.., PERFORMANCE_ACCEPTED#, the adapter log; close S1.
0b. CTO RULINGS 100946 (RULINGS_IRPT_20260925.md @75156f2b18): R1 export section A is P's (V2/V3 directories granted to
   IRPT_LIVE_SCOPE_P; grant cherry-picked 5ab28b7175) -- exp leeway REMOVED at V2 and V3 ed0f7447af (not deployed; C-S219 49/49:
   refused 1..120 s past exp, admitted 30 s before); A1 KEYS LIVE 15:2xZ (portal-auth/irpt-render-secrets.tf, row @f855b1912d,
   containers only, material out of band; ledger irpt-render-keys-a1-20260925 closed, negative arm held; WAF drift in the
   same root = row S130, apply only -target'ed there); R2 contract landed 119b0b776e / CLOUD f6fd60f4fd (~D told). A2 (V2 = portal-auth/lambdas.tf
   aws_lambda_function.portal_authorizer, build-nodejs-lambda.sh) WAITS on one row: lambdas.tf env block
   IRPT_RENDER_JWT_PUBLIC_KEY_PEM -- A2 LIVE 15:48Z (row @67ce0f3296; ledger irpt-render-v2-a2-20260925 closed: CodeSha256
   sgQWoygZ.., env == render public key, no-token/bogus deny before+after, 4 human verifications after / 0 failures).
   A3 LIVE 16:2xZ (CTO 100972 permitted the identical versionless WAF ACL re-put; ledger irpt-render-v3-a3-20260925
   CLOSED): auth-validator-edge:21 CodeSha256 Mfo4c4PG.. == built artifact, 26/26 behaviors on :21 (was :20), distribution
   Deployed; WAF rollback record ..._waf_acl_before.json, after-diff 0 of 6 rules, LockToken unchanged; no-token/bogus 401 x4
   before and after; human Auth OK 8 on v21, 0 runtime errors. Targeted re-plan: edge + distribution No changes; the only
   residue is the recurring benign ACL version diff (row S133 corrects S130). Section A (A1 keys, A2 V2, A3 V3) is DONE.
   Edge role reads opal/auth/* incl. both private keys = row IRPT_BCKEND-S132 (owner portal-auth IAM).
   B0 PART 1 LANDED f304108913 (backend): _render_identity/grant.py -- one internal render-grant record per export
   revision (firms/<firm>/generations/<revision>/render_grant.json, key grammar; read back on write) feeding BOTH the
   Enforcer's render ports (pinned accounts + pinned accountSetId/jobId/reportId + the delegator advisor id stamped at
   freeze, answered only for the subject the grant names) and mint_input() for B2. No ExportBundle v1 contract change,
   so the delegator slot needs NO CTO proposal. Test 21 passed (13 new + 8 pin tests unchanged, real served.Entry).
   Real run: S3 round trip in the evidence bucket under synthetic generation GENB0GRANTSYN -- read-back equal; None for
   another subject, a missing revision, another firm. Bucket from IRPT_EVIDENCE_BUCKET only (naming gate).
   B0 PART 2 LANDED bd52efb246 (backend): served.render_ports_from_env() -- None unless the function carries
   IRPT_EVIDENCE_BUCKET (today's refuse-every-render behaviour), else grant.render_ports(); installed on the performance
   (build_entry) and status (build_owned_entry) boundaries. Test 18 passed; regressions _authz 160, performance 183,
   ops 160 (22 skipped), narrative 37 -- all pass; flat-layout cold-start import OK for adapter/status/narrative.
   NARRATIVE installed too: CTO exact row @773be128f1 (cherry-picked 7ac4047de8), 630de21b95 -- all three read
   boundaries now carry the ports; _render_identity + narrative tests 57 passed.
   B1 PREREQUISITE LANDED 164190e2db (backend): MEASURED a render request to the performance route was refused at
   principal resolution (InteractiveAccess -> ProspectOwnershipRefused) before any scope check. Now the grant stamps
   delegator_principal_class and principal_row(grant) EQUALS the delegator's own InteractiveAccess row; performance
   _request_principal() uses it only under the Enforcer's RENDER_DELEGATE scope and only when the grant names the
   verified delegator. 28 new/updated tests; regressions performance 188, _authz 160, narrative 37, ops 160 pass.
   Limit: an operations-user delegator with no advisor id is refused at freeze (named).
   PRINT PAGE (measured 17:3xZ, portal DEV): PrintEntry -> resolveBundle -> getPerformanceReport sends no accountSetId
   (selectedReference throws before any request) and start=end=businessAsOf, not the retained window -> a Performance
   render prints nothing. Interface published: card B2-URL @bc3f70d22c (print URL carries selection/start/end from the
   grant); portal half asked of 2.0.0_SA_COO~D 20260925T173801Z. Backend half is mine: grant pins accountSetId = that
   selection, reportId = the retained report id, jobId = the export's job; B2 builds the URL from the grant.
   B1 CORE LANDED 523890feda (backend): export/retained_export.py -- authorizer (caller IS the stored owner and its
   current scope covers the report), resolve (one report via the real ReportRepository; server-built row, never the
   body's sha), render_grant (accountSetId = owner's selection, reportId, jobId = export revision), print_query
   (REQUESTED window; card corrected). 8 tests over the real repository; export suite 77 passed. Real run blocked:
   irpt-requests has 28 rows and NO REPORT# row at any firm -- no signed-in Performance run has retained a report.
   B1 NARRATIVE LANDED bcb153c789 + test fix 600140b8cf (backend; bcb153c789's "suite passed" was FALSE -- 3 failed on
   a handler-name collision, fixed; export suite 81 passed): export/narrative_submit.py builds the packet at submit
   from the retained report (cutoff = actual_end 23:59:59Z), binds only a contract-validated packet by the sha of the
   stored + read-back bytes (CTO R2). Real run: LIVE opal-news-trending-daily, validated, prose released, persisted
   under synthetic GENB1NARRSYN. Deploy note: stage narrative/handler.py under another name in the export zip.
   B1 SERVICE LANDED 83673d731c (backend): served.py status-only answer ({"_no_data": True} -> `data` omitted, only
   QUEUED/RUNNING); export/submit_service.serve_submit (resolve -> export revision -> narrative bind -> freeze + persist,
   dispatch OFF -> grant -> QUEUED, export id in status.operation.revision). End-to-end test over the real repository,
   narrative builder, controller and envelope: the QUEUED envelope validates against the published schema, 0 errors.
   Suites rc=0 (export 84, _authz 160, performance 188, narrative 37, ops 160, _render_identity 23); _contracts' 33
   failures are all test_seam_paired (pre-existing, unrelated). Live run blocked: no REPORT# row at any firm yet.
   B1 INSTALL LANDED 509d2e8037 (backend): export/entry.py submit_export -> submit_installed.compose -> serve_submit;
   uninstalled answers NOT_READY naming every missing port. 7 tests; export 91 / _authz 160 / performance 188 rc=0.
   Real run vs LIVE AWS from the tree: all 9 ports composed, package read at portal a886aeb49cae, a nonexistent report
   refused by the live index (ReportDenied), 0 objects written.
   B1 PACKAGING LANDED: vendored render manifest backend c5ed2c4173 (portal a886aeb4); publish 1be6e4c39c -- export dir
   from the backend + 25 staged rows (sha-verified) incl. the five CURRENT contract schemas under irpt_contracts/.
   MEASURED: layer irpt-common:5's PerformanceReport / NarrativePacket / ExportBundle schemas are STALE (parsed != tree).
   Flat package probe with the B1 env: missing_ports [], package 1.0.0, schemas from irpt_contracts/, all modules local.
   B1 TERRAFORM LANDED e14cd90571 (backend, NOT applied): b1_submit.tf (GetItem on irpt-requests in the enabled client
   firms' partitions, the PERFORMANCE report prefixes, news Query/Scan, exr_* grant/packet objects) + lambda.tf env
   (contracts + manifest in the zip, requests table); plan 1 add / 1 change / 0 destroy.
   DEPLOY HELD (18:5xZ) on a MEASURED defect: cottonwood's ownership map holds 0 advisors, and the real users (Andrew)
   are internal OPAL_GLOBAL principals (served.verified_internal_subject: x-firm-id opal-capital or user type Dev;
   advisor_id None, home_firm_id opal-capital). B1's grant requires a FIRM_ADVISOR/OPERATIONS delegator with an advisor
   id -> Andrew's export would refuse AFTER the packet + bundle were written; and Enforcer._resolve_render_delegate only
   models advisor delegators. No ledger opened, nothing applied, nothing half-landed.
   OPAL_GLOBAL DELEGATORS LANDED 755c13bc19 (backend): the grant stamps the delegator's full identity (OPAL_GLOBAL allowed,
   advisor id required only for an advisor, home_firm_id); the Enforcer resolves an Opal delegator NOW with a request-local
   roster of that subject (served's own internal seam), intersected with the pin; serve_submit validates the grant BEFORE
   any write. Tests per package rc=0: _render_identity 27, export 92, performance 188, _authz 160, narrative 37, ops 160.
   Limit: an Opal delegator's CLASS is the one verified at freeze; its SCOPE is re-resolved at read time.
   B1 LIVE 19:1xZ (ledger irpt-export-b1-submit-20260925 CLOSED): irpt-export-render CodeSha256 1oJDheft.. (publish
   7bfd665d0e, re-pinned WHOLE at 755c13bc19 -- the old row mixed enforce/errors/loaders/prospect/owner_reads at an older
   pin under a newer served.py; caught by a pin-faithful probe), export root e14cd90571 applied (1 add / 1 change), env +
   irpt-export-render-submit-policy live, re-plan No changes. Negative arm by direct invoke, before -> after: internal
   submit of a nonexistent report UNEXPECTED -> OBJECT_NOT_COVERED; internal receipt UNEXPECTED -> NOT_FOUND (the OLD
   artifact failed every internal user on every export route, silently); ungranted advisor NOT_AUTHORIZED both; 0 writes.
   The positive run (a real QUEUED export) waits on the first retained report -- Andrew's signed-in Performance run.
   B2 DESIGN (19:2xZ): the host authenticates today with an OPERATOR storageState session, not the render token. Measured
   at portal DEV: ProtectedRoute admits ?renderToken=, but the typed client never sends it (only ProtectedRoute.tsx and
   App.tsx read it) -> the print page's reads would be refused. ~D landed the selection/start/end half on local DEV
   (IV-e-26, 08144571); the Bearer half is P's lane (portal/src/api/**, CTO 100919) -- api-client.ts reads ?renderToken=
   on /investor-reporting/print only for a render claim, sends Bearer on scoped reads, never persists (told ~D 192205Z).
   Token carriage: bound 13 bars a credential from an SSM command document -> card B2-CARRY @af9f24f901, (a) Parameter
   Store SecureString per attempt RECOMMENDED; ruling asked of 1.0.0_SA_CTO 192213Z -> RULED (a) 192232Z (msg 101013),
   four conditions: IAM on /irpt/render-token/* only (Lambda Put+Delete, host Get+Delete, aws/ssm or a scoped key);
   delete on EVERY terminal path + a sweep of names older than 15 min at the next export run; the value never logged or
   echoed, command document and output carry only the name; negative arm shows another attempt's name and a
   read-after-delete refused. WORLD: ledger it with the IAM change.
   PORTAL CANDIDATE 5c2fc34d (portal branch p-render-token-20260925, worktree C:/Users/AndrewBerman/Desktop/portal-p-render-token,
   base local DEV 55ed4790): src/api/render-claim.ts + apiRequest -- on the print path with a render claim, Bearer =
   renderToken, nothing stored, a 401 neither refreshed nor redirected. 12 tests (parity with ProtectedRoute over six
   token shapes), tsc -b clean, eslint clean, fe-s-88 5 pass. LANDED on LOCAL portal DEV 19:3xZ (fast-forward
   55ed4790 -> 5c2fc34d; not pushed -- local DEV carries ~D's drains, MSTR pushes; ~D told). Served run on :5174 (the
   shared dev server, now on DEV): the print page's performance read went out with Bearer <renderToken>, stayed on the
   print route (no /login, no refresh call), and displayed "This bundle was not rendered" for the unsigned probe token.
   B2 CORE LANDED 3190ac41e9 (backend, OFF until deployed): _render_identity/carriage.py (SecureString
   /irpt/render-token/<ATT-id>, put-once, idempotent prefix-bound delete, 15-min sweep, value never returned/logged);
   dispatch.render_request gains RenderTokenName + PrintQuery (a name + issued ids/dates); serve_submit with
   ports.render_enabled: sweep -> mint -> put -> preflight/dispatch -> delete if not sent or raised. _render_identity 36,
   export 97 rc=0. Real run LIVE Parameter Store (dummy value): put/readback equal, second put refused, delete, read after
   delete refused ParameterNotFound, 0 names left.
   NEXT (P): (1) done (portal render Bearer on local DEV); (1b) B2 host + infra: SSM document params RenderTokenName +
   PrintQuery; run-export-render.sh reads the name (get-parameter --with-decryption, never echoed), render_export.cjs opens
   origin + print route + PrintQuery + &renderToken= with NO storageState, then deletes the name; submit_installed composes
   ssm/mint/dispatch + IRPT_EXPORT_RENDER=on; IAM per ruling (Lambda Put+Delete+Describe on /irpt/render-token/*, secret
   read of the render private key; host role Get+Delete); ledgered deploy with the ruling's negative arm; (2) under ruling (a): mint at submit + put the token + SSM doc/host script read it (no operator
   session) + dispatch ON; the read functions' B0 deploy (grant.py + enforce at 755c13bc19 + grant read IAM) rides it.
   PARKED (owner P, un-parks at the next irpt-holdings build; ~M 101008, CTO 101007): holdings/resolve.py has drifted from
   its STAGE_MANIFEST pin (_scope/resolve.py@c76b7c7aee) -- build-and-upload refuses irpt-holdings until re-pinned.
   S135 disarmed: ~M landed the schedule fix for P (afefa09d7e).
   AFTER B1-B3 (CTO 100993, from ~D 100992, DSGN_IRPTV1 decomp v4 section 7 @d4add46f46): a HOLDINGS export report kind
   beside performance/analysis, additive on the contract, same freeze + render path; ~D wires EXPORT_KIND_BY_TAB.
   DEPLOY rides B1: package _render_identity/grant.py into the adapter/status/narrative zips, set IRPT_EVIDENCE_BUCKET,
   grant s3:GetObject on firms/*/generations/*/render_grant.json (+ ListBucket on that prefix: missing -> 404 ->
   refusal, not 403 -> raise). The adapter redeploy waits until the INF one-use is spent or expires (00:00Z).
   Then B1 (submit writes the grant at freeze, QUEUED shape) -> B2 mint from mint_input -> B3 finalize.
   R3 hop 4 = option (a): mint the cst_ binding only for a PUBLISHED revision whose scope covers the selection.

1. S1: the COT one-use plan 99052771.. EXPIRED UNSPENT at 2026-09-25T00:00Z (full scan 00:00:18Z: no USE or ACCEPTED
   row for it). A COT run now needs Andrew's new per-use word and a re-arm (var-file pattern `rearm.tfvars.json`).
2. 49F Performance SERVED on our engine (21:28Z): f49_engine 94cf4cd61e + retained 4573b3e3e3 + grants 55b39f2d11;
   contract provider OPAL_ENGINE (on CLOUD 69cac32dce, ~D told). YTD/QTD/1Y, one account; real read-only run: median
   account YTD +6.72%, 182 days linked. BD cross-check DONE on a 300-account sample (ed9ea1ba55,
   `IRPT_MVP_P/F49_BD_CROSSCHECK_20260924.json`): 244 of 293 within 10bp, 286 within 100bp, median 3.3bp, 7 divergent
   (parked below). ~D verified OPAL_ENGINE renders (100895). ALL-ACCOUNTS census DONE db699faf13
   (`IRPT_MVP_P/F49_BD_CROSSCHECK_ALL_20260925.json`): 5194 of 5309 compared, 4372 within 10bp (84.2%), 4975 within
   100bp (95.8%), 219 divergent (4.2%), median 3.3bp, p90 20.8bp -- the sample holds. OPEN: S1 (Andrew's signed-in 49F request).
3. INF (Orion): inf_selected 312e4be3a0 (captured Scope grammar scoped to one account; orion_adapter parse; identity +
   window gates; 7 tests); mapping 55ccf7e99f (reverse of the directory mint; 25/25 served directory ids map back); OrionTransport daffb01f77
   (estate session JWT orion/jwt/current by jwt_freshness's own constant; live token decodes, 8.7h left); per-firm
   one-use gate f4379b44d7 (the LIVE armed COT plan re-verified under it, no claim); retained INF branch d813dcf9c6
   (INF CODE-COMPLETE offline). NEXT = one bundle on Andrew's per-use word (asked via CTO): package + accounts_v2 read
   grant + plan-gated Orion session read + ONE INF plan, deployed together (no INF compose without a plan). Card @925835306a -- mapping direct
   (accounts_v2.account_id), JWT auto-refreshed 09:51Z/21:01Z, request grammar reconstructed (one live proof needed:
   Andrew's per-use word, or a cheaper Orion Performance-screen HAR first). 49F/INF answer UNSUPPORTED_OPERATION
   by name until each lands (7f6b5589f6, served 20:26Z).
3b. DONE 22:2xZ: HoldingsSnapshot admits M's four classification members (767ac83009; v1 on CLOUD 7251000daa) -- M 100906
   step 1; ~D accepts next, then M emits.
3c. DONE 13:3xZ (row S126 ARMED, disarm owner P, ~M msg 100941): the directory refresh fired 09:00 ET (13:00Z), 8 min
   after the shared runner host's 12:52Z start, and failed HAND_OVER_RUNNER_OFFLINE at all 3 firms. Now fires 09:30
   America/New_York (86a3d27224 on the publish branch, applied under ledger irpt-directory-refresh-schedule-s126-20260925,
   closed; live get-schedule verified; re-plan No changes). Disarm row S127 @61bce7ee33. CORRECTED (row S128): the apply landed
   before 09:30 ET, so the schedule fired TODAY 13:30:29Z -- hand-over Success at all 3 firms, directories republished 13:30:4xZ
   (49F as_of 09-24, was 09-17; INF 09-25; COT 09-22). ~M corrected in the broker 13:38Z. Criterion 2's 49F census read the
   09-17 directory -- RE-RUN on the fresh directories (below).
4. Criterion 2 census DONE (ee51ffafac). 49F's 762 non-computable accounts NARROWED 45ec3dd692
   (`IRPT_MVP_P/F49_UNRESOLVED_BALANCES_20260925.json`, custodian dim_balance 2026-09-23, net_mv_plus_cash): 722 empty
   + 38 absent from the custodian = 760 directory-termination gaps; 2 funded accounts (~$105K) are the real engine gap.
   RE-READ 13:4xZ on today's republished directories (receipt PERFORMANCE_RESOLVABILITY_CENSUS_20260925.json,
   F49_UNRESOLVED_BALANCES_20260925b.json): COT 843/843, INF 878/878; 49F 6698 of 7497 (72 now TERMINATED), 790 hold
   nothing, 9 FUNDED (~$945K) non-computable -- the real 49F gap, up from 2.
5. EXPORT HOP NOT BUILT -- design card `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/EXPORT_HOP_DESIGN_CARD_20260924.md`.
   Served submit answers NOT_READY; 11/11 host renders Failed (SESSION_ABSENT); 0 PDFs; render signing keys ABSENT;
   V2/V3 render branches coded, not deployed. A (keys + V2 + V3, shared auth plane) is outside P's surface: owner
   asked of 1.0.0_SA_CTO. B1 (serve submit-export for a retained report) is BLOCKED on a v1 contract ruling: the
   submit-export response requires a complete ExportReceipt (artifact sha256, page_count >= 1), so a submitted,
   not-yet-rendered export has no honest answer (asked of 1.0.0_SA_CTO). Measured for B1: evidence keys accept
   `RPT-<32 hex>` as the generation segment at all three firms; the export zip stages 15 files vs performance's 61
   (no reports/, narrative/ or registry modules). B2 first half LANDED 7b0b59b77f (backend branch, LOCAL, not
   deployed -- rides the B1 deploy): dispatch now sends `PortalOrigin`, which the live SSM document requires with no
   default (read-only check: pre-fix set missing it; post-fix none missing, none undeclared); 69 export tests pass.
6. Y compositions: hops 2+3 SERVED (ledger `irpt-upload-hop2-20260924`, S1 = Y's live 12.03 acceptance). Hop 4 custody:
   card `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/CUSTODY_HOP4_CARD_20260925.md` -- installer, reader and
   interpreter ports never constructed; no served writer of the `cst_` binding; the portal sends the holdings
   `sourceSetRevision` where the reader accepts only `cst_<64 hex>`, so every custody submit refuses. Link-3 decision
   (who mints the binding) asked of 1.0.0_SA_CTO.
7. C-S219 COMPLETE d2e014dbf9 (43 of 43, offline; receipt `IRPT_MVP_P/RENDER_CHAIN_C_S219_20260925.json`): one
   render token on all three routes; swapped ids refused; expiry measured (admitted up to 60 s past exp -- on the
   export card for section A); actual V1 refuses the render token; a human token unaffected at V3, full V2 and
   served.Entry; pinned bodies read and an unpinned same-account report refused through a real served.Entry. Fix
   fe854ce6f1 (LOCAL, not deployed): Enforcer object pin + `served.Entry(render_ports=...)`. MEASURED: no deployed
   function installs render ports, so every render read refuses today -- export card B0.
8. A1 `_authz` log-line fix (4fffe13f01): SERVED on irpt-ycharts-generate; rides the next rebuild of the others.
   Census fix 1fcefdad74 (LOCAL, not deployed): all 17 published routes resolve and read guarded -- installed entry
   modules resolve from their staged rows; `served.installed_entry` gives performance/runtime, generate_installed and
   status_installed an earned mark (build at first call, refused unless the Entry matches its declared routes);
   `_authz` 152 passed (was 7 failed). Rides each function's next rebuild; its source-map pins move then.
   Reports suite green in one run a22cdc8578 (87 passed; was 3 failed): the currency refusal arm follows Andrew's
   49F/INF USD attestations (815dbc5507); each installer test pins its own `entry`. Suites: _authz 152, performance
   179, reports 87, export 69.
   Directory suite green f3cca0b550 (160; was 6 failed): stale tests only -- checked first as a possible selection-hop
   defect, none found. The owned-read guard's after-compute re-check is now proven (Opal viewer, owner without principal).
   COLD-START HAZARD FIXED 892f4b6099 (LOCAL): the publish worktree's source map (the real build input) does not
   package the INF modules, while retained.py / authorization.py imported them at module level -- re-pinning
   either (e.g. for 1fcefdad74) would have shipped a Performance zip dying at import for every firm (measured at
   pre-fix HEAD). INF now composes only when packaged, like 49F's engine port. Check:
   `IRPT_MVP_P/flat_import_check.py --map-root <publish worktree>` -- all 7 functions import, guarded. Performance
   suite 183 passed (the commit message's "187" is wrong: 179 + 4 new = 183). No IRPT user traffic 22:5x-01:5xZ
   (logs, keep-warm control 108 on directory-search): no signed-in run yet, no live defect seen.
   RE-PIN RULE for the next rebuild of each function: run flat_import_check --map-root first.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| The COT browser run | Andrew | a NEW per-use word (plan 99052771.. expired unspent) | NOT ASKED |
| A per-use word for 49F and for INF | Andrew | card 2 shape, one each | NOT ASKED (build first) |
| Portal renders dates.actual_* (criterion 3, COT window disclosed) | 2.0.0_SA_COO~D | PerformanceReport v1 dates block | MET IN CODE (read 02:2xZ, portal@13b5356f): Summary.tsx:28-50 shows the answered window; MethodsAndSources.tsx:112-131 shows requested vs answered and, when they differ by trading days, the note that history outside the answered window is not represented. Proof on real data = the COT signed-in run. |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| `build-and-upload.sh` removes tracked `performance/*.py` from the publish worktree's working tree on every irpt-performance-adapter build (18:41Z and 20:2xZ; restored from HEAD each time; generate/refresh builds do not) | 1.0.0_SA_CTO to route (ci/ owner) | the next performance build |
| 49F engine: 9 FUNDED accounts (~$945K, net_mv_plus_cash, directory 09-24) with no linkable YTD day (was 2 on 09-17); vs BD: 219 of 5194 DIVERGENT over all accounts (db699faf13); in the 300 sample, 7 of 293 DIVERGENT (3 engine coverage gaps of 35-98 neutral days; 1 in-kind signature +4452% vs +96%, the open ADVI_49F.c02-CFINPUT clause; 3 fully linked at 108-496bp), receipt F49_BD_CROSSCHECK_20260924.json | 1.0.0_SA_CTO to route to the 49F engine lane (DS) | the engine lane's next c02 act |
| 49F directory (as of 2026-09-24, 72 TERMINATED) still lists 790 not-terminated accounts the custodian shows empty (752) or absent (38) on 2026-09-24 -- criterion 2's denominator counts them active (45ec3dd692) | 2.0.0_SA_COO~M (directory refresh) | M's next directory refresh or termination source |
| `holdings/tests` 44 fail in the P worktree at HEAD (test_publication_entry 39, test_runner_destination 3, test_snapshot 2) | 2.0.0_SA_COO~M (holdings lane) | M reads it against its own branch |
| portal `bun test src/pages/InvestorReporting` 89 fail on origin/DEV 5e339ffd (87 unique), not CI-run | 2.0.0_SA_COO~D | ~D's S6/S7 rows |

## Limits

COT has no live use (plan expired unspent); 49F is served on Opal's engine; INF is not composed live. No vendor call is made by this seat; the one use fires only
on Andrew's signed-in request. Nothing here is pushed.
