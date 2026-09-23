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
| Workspace candidate pin | `c4564aad17` (consumption-test stub tracks the reader's projection) over `635af92b76` (current-authority consumer, CANDIDATE for CTO direct review) over `2874e37647` (CTO accepted 2dd385ed59 / 3d9f451) |
| P integration pin | `b3fc529601` on `irpt-smoke-p-backend-20260923`: 31 Y files; 85 of 85 tracked `ycharts/` files at 2874 hash-match P HEAD |
| Portal candidate pin | `7a5b24e7` (no new Portal candidate) |
| Deployed artifact pin | `irpt-ycharts-generate` CodeSha256 `1L60sG1G9IaFfwe+LPNdE84DarlWCHKkdE8M5CyVI8o=`, LastModified 2026-09-19T14:29Z -- predates every Y commit; source map at HEAD says `CJ6aBh7B...` |
| Push state | LOCAL; origin CLOUD `b475b96309` (ls-remote 23:16Z) |

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
running host -> vendor PDF -> certified AnalysisReport -> screen -> reload/history, with deployed package/source
digests and immutable input/request/report revisions recorded. Runs the moment the host is running and P returns
the installed factory + cutover receipt; until then each loop tick re-measures the dependencies below from artifacts.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Installed `MODULE:build_resident_runtime` factory with real `principal_for`, repositories, session ports; package/census digests; sole-consumer cutover receipt | 2.0.0_SA_COO~P | RESIDENT_ASSEMBLY_HANDOFF_20260923.md items 1-3, 5 | AWAITED (no implementation in P tree) |
| Non-HTTP current authority: P projects `createdAt`/`role`/`userType` from `CanonicalProfileReaders.get_user`; Y refuses on user None / status != active / firmId != home_firm_id / createdAt after acceptance, records createdAt_absent, classes OPAL_GLOBAL iff firmId == opal-capital or userType == Dev | 1.0.0_SA_CTO ruled d78fdb2f1c (item 4); P (1)(4), Y (2)(3) | Y side: `635af92b76`, 37 passed; P side: `_USER_FIELDS` projection + IAM plan | Y CANDIDATE awaiting CTO review; P (1)(4) AWAITED |
| Host tag `AutoShutdown = "disabled"` on the runner Terraform resource, plan to CTO, safe-apply; nobody starts the host before the tag and the resident install are ready | 2.0.0_SA_COO~P | CTO d78fdb2f1c item 5; Y 99801 adds the second writer `aws_ec2_instance_state.runner` (`stopped`) | BLOCKED at P |
| Generation path: deploy HEAD submit entry, `sqs:SendMessage` on submit role, `IRPT_LIVE_YCHARTS_CALL`, `/analysis/*` routes live | 2.0.0_SA_COO~P | CRO 6fc3f5f785 item 5; RESIDENT_ASSEMBLY_HANDOFF items 2, 4 | AWAITED (measured absent 23:2xZ) |
| 31-path owned-path grant for the copied Y files | 2.0.0_SA_COO~P | b3fc529601 | CONSUMED |
| Grant extension to the Y template-upload batch: intake/{portfolio,uploads,resolution_broker,resolution_kimi,security_resolution,template_reader}.py, intake/tests/test_{resolution_kimi,security_resolution,template_reader,template_uploads}.py, ops/prospect_dates.py (8 Y commits, 84c6e63806..85af5eb95d) | 1.0.0_SA_CTO grants, 2.0.0_SA_COO~P merges | import census 93 reachable / 4 MISSING / 3 diverged; resident_session.py cannot import in P's tree | BLOCKED (sent tick 2) |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| `comp-blast freeze_parsed_portfolio` NOT-FOUND over 28,307 nodes (MSTR 99629/99630) | 2.0.0_SA_COO~Y | a graph question arises for that name; not on the live thread |

## Limits

Not proven: installed service, live login/session recovery, real vendor PDF contents, browser E2E, all-firm
publication, holdings readback beyond upload echo, the units/variants/corrections/export matrix. Reserved gates still
ahead: the shared Terraform apply on the ycharts root (P, never-widen), the first automated sign-in (approved under
6fc3f5f785 as the standing host workflow; agent ad hoc vendor calls stay prohibited), and any shared-branch push
(0.0.0_AB_MSTR). No acceptance ID is PASS until the CTO grades a pinned live trace.
