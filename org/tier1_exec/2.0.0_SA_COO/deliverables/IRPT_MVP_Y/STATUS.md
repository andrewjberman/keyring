# IRPT Analysis (COO~Y) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE, since 2026-09-23 23:01Z; the Codex seat and its 600 s driver are retired).
Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.4; COO_Y.md and
CONTROL.md apply; CTO reviews directly (no CVO queue). Goal + loop authority:
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md` @fc17929b64
(/loop 20m, stop on /verify SOUND or Andrew's stand-down). As of 2026-09-23T23:30Z.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `irpt-mvp-y-20260922` at `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922` |
| Workspace candidate pin | `7fec957269` (prospect dates bind v2 template documents) over `79c53e1abe` (custody-retained stub) over `c4564aad17` (consumption stub) over `635af92b76` (current-authority consumer, CTO ACCEPTED 9baf67bb5f) over `2874e37647` (CTO accepted 2dd385ed59 / 3d9f451) |
| P integration pin | `b3fc529601` on `irpt-smoke-p-backend-20260923`: 31 Y files; 85 of 85 tracked `ycharts/` files at 2874 hash-match P HEAD |
| Portal candidate pin | `7a5b24e7` (no new Portal candidate) |
| Deployed artifact pin | `irpt-ycharts-generate` CodeSha256 `1L60sG1G9IaFfwe+LPNdE84DarlWCHKkdE8M5CyVI8o=`, LastModified 2026-09-19T14:29Z -- predates every Y commit; source map at HEAD says `CJ6aBh7B...` |
| Push state | CLOUD: on origin @`69e36619ae` (MSTR push on Andrew's word, ls-remote 00:5xZ) for every Y CLOUD commit through af7ecf5e87; this commit LOCAL until the next push. Y branch `irpt-mvp-y-20260922` @79c53e1abe: LOCAL, never pushed by Y |

## Live thread

State: NOT LIVE. Last trace: none (18 focused offline cases + 4 controls at 2874, CTO 2dd385ed59; no installed/live proof).
First failing hop: 0. Always-on host `i-0167fd745ad906a66` is STOPPED (enforcer StopInstances 21:21:18Z; Terraform
`ycharts/instance.tf:131-135` declares `stopped`; no `AutoShutdown=disabled` tag) -> nothing consumes `irpt-generation`.
Next hops measured behind it, all P shared surfaces: deployed generate Lambda is stale against the source map; its
role has no `sqs:SendMessage`; `IRPT_LIVE_YCHARTS_CALL` is unset; `/analysis/inputs`, `/analysis/requests*` liveness
UNDETERMINED by comp-routes (one `/api/scoped/investor-reporting/*` behavior to API Gateway).

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| Y1 selected custody + owned CSV/XLSX + disposition + catalogue | OFFLINE ONLY | TEMPLATE_UPLOAD_HANDOFF_20260923.md, UPLOAD_RESOLUTION_IMPLEMENTATION_20260923.md @2874 |
| Y2 immutable normalized input, corrections, reconciliation | OFFLINE ONLY | normalized_input.py / frozen recipe @2874; 12.03 Dollars freeze offline |
| Y3 retained acceptance, durable dispatch, idempotency, recovery | OFFLINE ONLY | resident_worker.py, durable_job.py @2874; CTO 2dd385ed59 |
| Y4 identity/settings/holdings readback, Overview/Comparison/Multi-Comp PDFs | NOT STARTED (live) | session_* @2874 offline only; no vendor PDF ever produced by the resident |
| Y5 extraction/certification into typed report | OFFLINE ONLY | publisher.py / census 195040 B @2874 |
| Y6 polling/history/reload/corrections/downloads | NOT STARTED (live) | Portal 7a5b24e7 |
| Y7 one reconciled full trace per required case | NOT STARTED | none |

Offline-only work grades nothing until the live thread is live.

## Write claims

None in flight. Landed at `635af92b76`: `generate/current_authority.py` (new), `generate/resident_worker.py`
(`profile_for` port, decision replayed at start / every guard / release / reopen), `generate/tests/test_resident_worker.py`.
P's next integration batch takes these three files over the 31 already at b3fc529601. Untracked and preserved:
`.tools/irpt-y-portfolio-commit-message.txt`, `.tools/irpt-y-submission-commit-message.txt`.

## Next proof

Real login -> CSV AAPL 10.01 + VNQ 2.02 Dollars -> frozen 12.03 -> Overview acceptance/queue -> resident worker on the
running host -> vendor PDF -> certified AnalysisReport -> screen -> reload/history -> same-revision export, run
exactly as `RUNBOOK_1203_LIVE_JOURNEY_20260923.md` (ten hops, per-hop call, readback and refusal signatures, the
evidence list, the resident acceptance command). Runs the moment preconditions A-F land at P; until then each loop
tick re-measures the dependencies below from artifacts.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Installed `resident_installed:build_resident_runtime` factory (P 5e05823f4e, 11 controls) + package builder (217 members); Y review tick 6: principal shape lacks `principal_class` (repository/retention/owner_reads gates deny every cross-firm read for an Opal actor) and `authorize` is same-actor-only (denies the original input creator's artifacts) -- exact fixes sent; enrolled_user_id must be MEASURED from the D1 bundle at cutover (secret has no versions); library pin is the LF blob 41ffebbe | 2.0.0_SA_COO~P | RESIDENT_ASSEMBLY_HANDOFF_20260923.md; Y tick-6 message; P fix 32062e39d2 verified by Y in P's tree (factory 11 passed, resident worker 37 passed, per file) | FACTORY ACCEPTED BY Y; cutover sequence AWAITED: SSM read of the host copies, LF package upload, D1 sign-in, enrolled id pinned, receipt, install-resident.sh, in ONE plan with the host-state flip |
| Non-HTTP current authority: P projects `createdAt`/`role`/`userType` from `CanonicalProfileReaders.get_user`; Y refuses on user None / status != active / firmId != home_firm_id / createdAt after acceptance, records createdAt_absent, classes OPAL_GLOBAL iff firmId == opal-capital or userType == Dev | 1.0.0_SA_CTO ruled d78fdb2f1c (item 4); P (1)(4), Y (2)(3) | CTO 9baf67bb5f: Y `635af92b76` ACCEPTED bounded (home-firm fallback confirmed, caveat recorded for a firm admin on a descendant firm); P 185dfb3e7f ACCEPTED; plan 1de76039 APPLIED 00:17:29Z (P 99840): Query/GetItem/kms:Decrypt on both roles, zero-diff, ledger closed | CONSUMED (Y); runtime grant APPLIED |
| Host tag `AutoShutdown = "disabled"` on the runner Terraform resource, plan to CTO, safe-apply; nobody starts the host before the tag and the resident install are ready | 2.0.0_SA_COO~P | Tag `AutoShutdown=disabled` APPLIED 00:17Z and KEPT by Andrew (ruling 4, 69e36619ae); host `stopped`; writer B `aws_ec2_instance_state.runner` flips to running in the SAME plan as the resident install cutover, then one start | Writer A done and ratified; writer B SEQUENCED behind the factory/cutover plan (P) |
| Generation path: deploy HEAD submit entry, `sqs:SendMessage` on submit role, `IRPT_LIVE_YCHARTS_CALL` | 2.0.0_SA_COO~P | CRO 6fc3f5f785 item 5; RESIDENT_ASSEMBLY_HANDOFF items 2, 4 | AWAITED (measured absent 23:2xZ) |
| Route plane for hops 1 and 9: `POST .../analysis/inputs`, `GET .../analysis/requests`, `GET .../analysis/requests/{requestId}` are `NO-HANDLER-AT-HEAD` in routes.json (not in Terraform), LiveClient flags `false` (`responses.ts:423-425`); no Lambda wires `build_upload_entry`; deployed `irpt-status` (built 09-21) predates the history/read handlers (`8e8498c9c0`, 09-22) | 2.0.0_SA_COO~P (routes, factory composition, irpt-status redeploy, flags) | RUNBOOK_1203_LIVE_JOURNEY_20260923.md preconditions D-E | AWAITED (measured 00:1xZ) |
| 31-path owned-path grant for the copied Y files | 2.0.0_SA_COO~P | b3fc529601 | CONSUMED |
| Registry family `ORIGINAL_HOLDINGS` (the template lane's original bytes, `intake/uploads.py:162`): absent from `infra/logic/registry/reporting_policies.json` (12 families), so `ArtifactRepository` refuses the upload at `reports/repository.py:325` -- hop 1 of the 12.03 journey | Row WRITTEN by 2.0.0_SA_COO~M at 58ee5b36dd (LOCAL, codex/irpt-m-completion): table `original_holdings`, extension csv (xlsx suffix cosmetic: the readback parses by retained `file_type`, uploads.py:301); policy_sha256 -> 7a7ed8f6; 1.0.0_SA_CTO accepts; 2.0.0_SA_COO~P grants Put/Get on `irpt/<firm>/state/original_holdings/*` to the upload function | TEMPLATE_UPLOAD_HANDOFF item 3; Y 99915 item 3; M 99925; Y answer tick 7 | ROW WRITTEN; acceptance + grant AWAITED |
| Resident cutover plan 04c77cbe / 9b6e6fa98e (runner-resident policy + host state -> running, one apply) | 2.0.0_SA_COO~P applies on CTO GO; then SSM read, LF package upload, D1 sign-in, enrolled id pinned, receipt, install-resident.sh; Y runs `--once` | Y review 99915: family sets correct, single plan right | AWAITING CTO GO |
| `ops/prospect_dates.py` re-copy at 7fec957269 (v2 binding) with the irpt-status rebuild; its test file has no P row | 2.0.0_SA_COO~P (copy), 1.0.0_SA_CTO (row) | Y 7fec957269 | AWAITED |
| Grant extension to the Y template-upload batch: intake/{portfolio,uploads,resolution_broker,resolution_kimi,security_resolution,template_reader}.py, intake/tests/test_{resolution_kimi,security_resolution,template_reader,template_uploads}.py, ops/prospect_dates.py (8 Y commits, 84c6e63806..85af5eb95d) | 1.0.0_SA_CTO grants, 2.0.0_SA_COO~P merges | CTO 9baf67bb5f item 6: seven rows granted at c4564aad17 (resolution_kimi, security_resolution, template_reader + their tests, current_authority.py); portfolio.py / uploads.py / prospect_dates.py DIVERGED -> P three-way merges from 10627906f2, Y confirms semantics in ONE exchange before P commits | INTEGRATED at P d3f612d94d + 9e87bb4202 (merges == Y blobs; resolution_broker.py copied; `resident_main.py --help` imports in P's tree). Two Y-lane test files (consumption test b35cb286b1, custody-retained stub 6ab91ac03a) now carry P rows at 79c53e1abe (`.owned-paths.yaml:1281,1284`, CTO 69e36619ae); P copies at its next sync (DIFF at P d5c1f4be40) |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| `comp-blast freeze_parsed_portfolio` NOT-FOUND over 28,307 nodes (MSTR 99629/99630) | 2.0.0_SA_COO~Y | a graph question arises for that name; not on the live thread |
| Portal at c1ac41ec: `__tests__/mvp-selection/directory-browse.test.ts` "directory revision is distinct from entitlement and absent stays absent" FAILS (1 of 59 in the Analysis/upload/selection run; the other failure is the route-table test walking up from the detached portal worktree, an environment artifact). Selection/directory is P/M's surface | 2.0.0_SA_COO~P (portal contracts) | P's next portal sync; not on the Analysis thread |

## Limits

Not proven: installed service, live login/session recovery, real vendor PDF contents, browser E2E, all-firm
publication, holdings readback beyond upload echo, the units/variants/corrections/export matrix. Reserved gates still
ahead: the shared Terraform apply on the ycharts root (P, never-widen), the first automated sign-in (approved under
6fc3f5f785 as the standing host workflow; agent ad hoc vendor calls stay prohibited), and any shared-branch push
(0.0.0_AB_MSTR). No acceptance ID is PASS until the CTO grades a pinned live trace.
