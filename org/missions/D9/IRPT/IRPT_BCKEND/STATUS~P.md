# IRPT_BCKEND~P (Performance) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Reviewer `3.0.0_SA_CVO` (grades landed pins after the fact while the lease is FAST).
Drive: /closer-drive loop (cron 7a9ea1ce, every 30m at :17/:47; CTO 101098, Andrew-direct ~03:0xZ; replaced /canonical-drive 57c0067c); lease FAST re-armed to 15:01Z. Egress: vendor API calls permitted this session, each ledgered (CTO 101098). Goal:
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`.
As of 2026-09-26T05:1xZ. The prior long form of this file (B0-B3 build history) is in git: `git log -p -- <this file>`.

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

- AGENT WALK DONE (Andrew-direct ~02:1xZ; CTO 101109 split it: backend acts by API on the SAME principal). Walk principal
  irpt-walk-1790391192@opal.test lived [02:53:17Z, 03:39:08Z last token exp], deleted 03:30:33Z, ~D's reload landed
  /login; ledger irpt-walk-principal-20260926 CLOSED. Log: IRPT_MVP_P/WALK_API_LOG_20260926.jsonl @ff0a6c63bb.
- 49F LIVE: 200 PARTIAL (actual 01-02..09-24 disclosed) with REPORT# retained -- first retained reports at any firm.
  S140 DISARMED (row S142); ledger irpt-f49-bucket-adapter-read-20260925 CLOSED.
- INF FAILED: plan 01209afb SPENT 03:20:31Z; Orion 404 "Object does not exist" to the Scope body (replayed once,
  ledger irpt-orion-scope-diagnostic-20260926). Row S143 ARMED, owner P: the entity/grouping grammar is wrong.
- UI walk deferred: /investor-reporting admits only admin + internal + Dev (portal App.tsx) -- to Andrew as a card (CTO).
- ~Y's upload: irpt-ycharts-generate zip lacks interactive_access / template_reader / security_resolution (~Y 101125,
  IRPT_MVP_Y/P_GENERATE_PACKAGE_MISSING_MODULES_20260926.md @f12cd8bb52) -> P's item.
- C: drive hit 0 bytes free at 03:4xZ (a ledger write truncated; restored from HEAD); ~2.6 GB free after. [STUCK] to MSTR.

## Acceptance (goal Done criteria)

| # | Criterion | State |
|---|---|---|
| 1 | Signed-in journey per firm | INF armed (plan b); 49F served, bucket fixed, awaiting retry; COT plan expired unspent (needs a new per-use word). Export: B1 + deploy (A) live, render OFF until deploy (B). 0 retained reports at any firm |
| 2 | Every active account resolvable | MEASURED: COT 843/843, INF 878/878, 49F 6698/7497 (9 funded non-computable) |
| 3 | COT structurally sound, window disclosed | CODE + portal render; proof on real data = a COT run |

## Write claims

None building. Next surface: the adapter package + performance root (deploy B), export root `export_render`.

## Next-list (in order)

1. S143 FIX PROVEN LIVE 05:07Z (ledger irpt-orion-household-scope-proof-20260926 CLOSED; receipt
   IRPT_MVP_P/ORION_HOUSEHOLD_SCOPE_PROOF_20260926.json): the household-scoped Scope body (entity 5, one-account household)
   -> Orion 200 -> orion_selected.calculate returns a contract-validated Purfeerst report (YTD 0.0682, 01-01..09-25 exact,
   268 points, Account group == 1098). CODE UNCOMMITTED in the backend worktree (orion_account_mapping household check,
   orion_selected entity 5, orion_live HTTP status in the error; tests perf 189 / _authz 160 / reports 87 pass) -- held
   by MSTR's disk rule (asked 05:1xZ). Then: commit, adapter package re-pin, ledgered deploy (rides deploy (B)), a new
   one-use plan on a one-account-household client, and one signed-in run (needs a principal window).
1b. irpt-ycharts-generate package: add the three missing modules (~Y 101125), rebuild, ledgered deploy, the AST
   import-closure walk returns zero missing; then a new principal window for ~Y's one upload (new sign-off).
2. Deploy (B) -- UNBLOCKED (plan b spent 03:20:31Z): upload the adapter (publish 4872b28043), apply render_grant.tf +
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
