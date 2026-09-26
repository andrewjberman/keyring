# IRPT_BCKEND~P (Performance) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Reviewer `3.0.0_SA_CVO` (grades landed pins after the fact while the lease is FAST).
Drive: /closer-drive loop (cron 7a9ea1ce, every 30m at :17/:47; CTO 101098, Andrew-direct ~03:0xZ; replaced /canonical-drive 57c0067c); lease FAST re-armed to 15:01Z. Egress: vendor API calls permitted this session, each ledgered (CTO 101098). Goal:
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`.
As of 2026-09-26T02:5xZ. The prior long form of this file (B0-B3 build history) is in git: `git log -p -- <this file>`.

## Pins

| What | Value |
|---|---|
| Backend branch | `irpt-smoke-p-backend-20260923` MERGED into CLOUD as 949c6524fa (2 parents; directory/refresh.py + .owned-paths.yaml kept at CLOUD's content, merge diff 0). Suites on CLOUD rc=0: holdings 147, _authz 160, performance 188, export 106, directory 162, _render_identity 36 |
| Publish worktree | `C:/Users/AndrewBerman/Desktop/irpt-p-publish-20260923`; adapter row for deploy (B) at 4872b28043 (NOT uploaded) |
| irpt-performance-adapter | CodeSha256 jbojclF39H.. (LastModified 23:11:47Z = env-only re-arm, INF plan b) |
| irpt-export-render | CodeSha256 ryEMGlRu.., layers irpt-common:5 + irpt-render-deps-layer:1, IRPT_EXPORT_RENDER=off |
| 49F bucket | S140 fix f942df9ab4 APPLIED (-target): adapter role READ-ONLY on the engine twr_daily/twr_periods prefixes only |
| Push state | CLOUD LOCAL (not pushed; MSTR pushes) |

## Live thread

- AGENT WALK (Andrew-direct ~02:1xZ "have an agent do those walks and record HAR"; "Yes, use the Opal login"):
  walk principal irpt-walk-1790391192@opal.test LIVE since 02:53:17Z (packet blob fe8e8d89, CTO ba29004a1b,
  CRO 909dd40acc; ledger irpt-walk-principal-20260926 OPEN 47ac618a50, C1 closed). 2.0.0_SA_COO~D walks: 49F retry,
  Purfeerst Performance (spends plan b), ONE ~Y upload; HAR committed scrubbed. P deletes on ~D's word or at 04:00Z at
  the latest (`walk_principal.py delete 1790391192`), then the audit leg; a refused delete = branch (c) + escalate.

- INF plan b ARMED (Andrew "go"): plan 01209afb.., account acc_5510a3054a409d548a12c57d = "Purfeerst ****4944 / INDIVIDUAL"
  (a single-account directory entry), expires 2026-09-26T12:00Z. Receipt `IRPT_MVP_P/INF_ONE_USE_PLAN_20260925b.json`.
  Plan a (acc 0279) was unreachable: its entry "Martin ****4696" holds 2 accounts -> SelectionUnsupported.
- 49F: the 23:25Z request failed AccessDenied at the bucket fence (S140); fixed and applied. A retry has not arrived.
- Adapter log: no request since 23:25:05Z (read 23:54Z).

## Acceptance (goal Done criteria)

| # | Criterion | State |
|---|---|---|
| 1 | Signed-in journey per firm | INF armed (plan b); 49F served, bucket fixed, awaiting retry; COT plan expired unspent (needs a new per-use word). Export: B1 + deploy (A) live, render OFF until deploy (B). 0 retained reports at any firm |
| 2 | Every active account resolvable | MEASURED: COT 843/843, INF 878/878, 49F 6698/7497 (9 funded non-computable) |
| 3 | COT structurally sound, window disclosed | CODE + portal render; proof on real data = a COT run |

## Write claims

None building. Next surface: the adapter package + performance root (deploy B), export root `export_render`.

## Next-list (in order)

1. Read Andrew's runs: PERFORMANCE_USE#01209afb / ACCEPTED rows, any REPORT# row, the adapter log. Close ledger
   `irpt-performance-inf-one-use-b-20260925` S1 (INF) and `irpt-f49-bucket-adapter-read-20260925` N1 (49F 200 -> disarm S140).
2. Deploy (B) after plan b is spent or expires (12:00Z): upload the adapter (publish 4872b28043), apply render_grant.tf +
   IRPT_EVIDENCE_BUCKET, export_render=on; ledger with the CTO's negative arm (another attempt's token name refused, read
   after delete refused). REHEARSED 00:3xZ (plan only, CLOUD tree, live plan values as vars): 1 add
   (performance_render_grant_read) / 1 change (env + IRPT_EVIDENCE_BUCKET = the same bucket irpt-export-render writes
   grants to; 8 env elements unchanged, code unchanged until the upload) / 0 destroy.
3. First end-to-end Performance export (submit -> render -> receipt) on the first retained report.
4. Holdings export kind (card B4), after 3.
5. COT: egress now permitted this session (CTO 101098, each call ledgered) -> re-arm ONE COT one-use plan and a signed-in
   COT run (a walk; the current walk principal's limits exclude a second vendor call).

## Parked

| Question | Owner | Un-parks when |
|---|---|---|
| `build-and-upload.sh` deletes tracked performance/*.py from the publish working tree on each adapter build | 1.0.0_SA_CTO to route (ci/ owner) | the next performance build |
| 49F engine: 9 funded non-computable accounts; 219 of 5194 divergent vs BD | 1.0.0_SA_CTO to route (49F engine lane) | the engine lane's next c02 act |
| 49F directory lists 790 not-terminated accounts the custodian shows empty/absent | 2.0.0_SA_COO~M | M's next directory refresh |

## Limits

No vendor call is made by this seat; the INF use fires only on Andrew's signed-in request. Nothing here is pushed.
