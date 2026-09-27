# IRPT_BCKEND~P (Performance) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Reviewer `3.0.0_SA_CVO` grades landed pins after the fact while the lease is FAST.
Drive: the /closer-drive loop resumed on Andrew-direct "recs approved for all" (CTO 101296); cron 312e843c.
Goal: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`.
As of 2026-09-27T00:5xZ. Earlier forms of this file are in git (`git log -p -- <this file>`).

## Pins (served)

| What | Value | Ledger |
|---|---|---|
| irpt-performance-adapter | `Ll6t4VPa..` since 21:28:13Z: P-REOPEN-01 (260399e940), both timing lines (8d7a8b10fe, b18cb77c7d), S147 fix M (52604d790b); INF one-use plan env kept as live | irpt-reopen-authz / irpt-adapter-timing2 / irpt-authz-memo-20260926 CLOSED |
| irpt-ycharts-generate | `/iFhTAvT..` since 19:33:52Z = 85TXFzzv + ~Y's six hop-3 files (a219094b1a) | irpt-hop3-generate-resident-20260926 CLOSED |
| Resident (i-0167fd745ad906a66) | `/opt/irpt-resident/fe64236bbb-h7` since 21:20:44Z = f624e8a72f + the hop-3 six + hop-7 certify.py (ad817b55ea); rollback roots fe64236bbb, f624e8a72f kept | irpt-hop3-... / irpt-hop7-certify-resident-20260926 CLOSED |
| irpt-status | `bMMJ/bQ+5..` since 19:56:53Z (+interactive_access.py); irpt-status-role reads BY VERSION | irpt-status-reads-20260926 CLOSED |
| irpt-directory-search | `o1TXq5PH..` since 22:54:12Z: UIR-07 exact full-name match first in search AND browse(q) (49b935c213); -target apply | irpt-uir07-search-rank-20260926 CLOSED |
| irpt-export-render | render ON behind the S148 fence | irpt-export-deploy-b-20260926 |
| Backend branch | `irpt-smoke-p-backend-20260923` @aede6418c6 (not pushed) |  |
| Publish worktree | `irpt-p-publish-20260923` @d25a491d9e (not pushed) |  |
| Push state | LOCAL, unread against origin this turn; MSTR pushes |  |

## Live thread

- **49F Performance, account-level:** served. A second authorized viewer now reopens a retained report (arm 1 PASS);
  window 4's K7 refusal was this defect.
- **Hop 3 (Analysis generate):** the title producer, the packaged settings path and template-lane admission are served
  in generate AND the resident, content-proven 6/6 (`IRPT_MVP_P/HOP3_DEPLOYED_CONTENT_PROOF_20260926.md`).
- **Hops 8-9 (status reads):** served; ~Y's no-overlay proof 4/4; IAM 10/10.
- **Next window (CTO 101441/101466):** ONE window runs upload, generate, READY, sections and history for Analysis. It
  is cut once ~Y's offline pre-flight of hops 5-9 is pinned. K5's measured write set: ~Y 101484 @f36c5ee4c4.

## Acceptance (goal Done criteria)

| # | Criterion | State |
|---|---|---|
| 1 | Signed-in journey per firm | 49F served (account-level, reopen fixed). INF: S143 fix served in the adapter; needs a one-use plan + a signed-in run. COT: needs a new per-use word. Export: render ON; the first real export is not run yet (K8) |
| 2 | Every active account resolvable | MEASURED: COT 843/843, INF 878/878, 49F 6698/7497 (9 funded non-computable) |
| 3 | COT structurally sound, window disclosed | CODE + portal render; proof on real data = a COT run |

## Write claims

None building. Window 6's residue is read at the 01:17Z tick.

## Next-list (in order)

1. **Window 6 residue (CTO 101673):** principal deleted 00:21:32Z.
   - K4 NORMALIZED (00:10:04Z, input portfolio_4c5c85d0..); K5 QUEUED (00:12:05Z).
   - Job REQ-3a1b73a8 is stuck at hop 6: receive 1's session capture failed (S151), and receives 2+ fail because the
     principal was deleted (S150; branch (e) is struck).
   - It reaches the DLQ at about 01:12Z. At the 01:17Z tick: read the row; if it stays non-terminal, bring a one-line
     packet amendment naming how the row is closed or why it is left alone (the CTO signs it the same tick). Then close
     ledger legs V1/A1 (the route audit of ~Y's logs + ~D's HAR c25-rewalk; K9 already traced, 49F REPORT# 17 -> 19).
2. **The next Analysis window** is BLOCKED on S151: one live YCharts wrapper run to find why the capture fails, on
   Andrew's word (owner ~Y). Future packets keep the principal until every job is terminal (CTO 101673).
3. **The cross-viewer title binding** (f8c72944f3) ships in generate + the resident with the next Analysis deploy.
4. **INF:** a new one-use plan on a one-account-household client, then one signed-in run. **COT:** a new per-use word.
5. **K8, the first real export**, rides a later Performance window.

## Parked

| Question | Owner | Un-parks when |
|---|---|---|
| The kept test inputs and reports from windows 1-6 in cottonwood (UPLOAD#/INPUT#/analysis#/REPORT# rows and objects owned by deleted walk principals) must be excluded from any firm viewer's lists, or removed, before the route opens to firm users; closes as not needed if history lists by owner only (4.0.0_SA_CRO 101609) | the release cutter | the route opening to firm users |
| The backend worktree's directory Terraform root predates M's holdings resources (a full plan would destroy 11); UIR-07 used -target | 2.0.0_SA_COO~P | the next directory-root apply: merge CLOUD into the backend worktree first |
| `build-and-upload.sh` deletes tracked performance/*.py from the publish tree on each adapter build | 1.0.0_SA_CTO to route (ci/ owner) | the next performance build |
| `build-and-upload.sh` zips a source_dir JSON with the checkout's EOL (CRLF here), and its artifact record passes through MSYS path conversion (`/iFh..` became `C:/Program Files/Git/iFh..`) | 1.0.0_SA_CTO to route (ci/ owner) | the next build of a function whose hash starts with `/`, or that hashes a JSON member |
| The performance root's per-apply `approved_performance_plan` variable: an apply without it disarms INF's plan and destroys its session policy | 2.0.0_SA_COO~P | the INF plan's expiry (1790424000) or the next INF arm |
| 49F engine: 9 funded non-computable accounts; 219 of 5194 divergent vs BD | 1.0.0_SA_CTO to route (49F engine lane) | the engine lane's next c02 act |
| 49F directory lists 790 not-terminated accounts the custodian shows empty/absent | 2.0.0_SA_COO~M | M's next directory refresh |

## Limits

No vendor call is made by this seat without its per-use word; the INF use fires only on a signed-in request. Nothing
here is pushed.
