# J359 satellite factsheet promoted to portal PROD (portal-v2.1.221) -- 0.4.0_DT_ClientPlatform~H1

**archetype:** DEPLOY
**Date:** 2026-10-14
**Task Order:** ADHOC.j359-satellite-factsheet-portal-promote (org/tier2_senior/0.4.0_DT_ClientPlatform~H1/task_orders/ADHOC.j359-satellite-factsheet-portal-promote.md @37f558999f)
**Status:** COMPLETE except the workspace submodule pointer (see Blockers)

---

## Objective

Promote cand/dell1/satellite-factsheet-prod @6e69a05e43 (row dell1-20261014T192307Z-de27, approved by andrew, client-facing) to DEV and then PROD, read the CI conclusion, and read the deployed bundle for the two new strings. GO: msg 5769 from 2.0.0_SA_COO~J1.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| open-calls | `approval-status --branch cand/dell1/satellite-factsheet-prod` | PASS | APPROVED valid=yes, head_sha equal to the ls-remote tip |
| portal-merge-forward | `cand/dell1/satellite-factsheet-prod --push` | PASS | result=MERGED pushed=yes |
| portal-release-build | build, then `--check release/20261014T193116Z` | PASS | READY, 1 feature, 0 unapproved, 1 client-facing |
| deploy_ledger | open, close-leg x4, close | PASS | 4 legs, CLOSED |
| comp-routes | `origins` | PARTIAL | named the S3 origin but is DESIRED-plane; the public host came from the alias in cloudfront-distribution.tf instead |
| comp-which | one routing question | PARTIAL | tied scores, no host; comp-routes and the .tf answered it |

**What worked:** the precondition union, polling `gh run view` by id, and crawling the chunk graph (the new strings live in a lazy chunk, not the six files index.html names).
**What failed:** the first `git show origin/PROD:path` was mangled by MSYS path conversion; rerun with MSYS_NO_PATHCONV=1 per CLAUDE.md. My per-worktree listing printed every file and truncated; reduced to a unique union.
**Gap found:** none new.

---

## Work Completed

| Step | Result |
|---|---|
| Precondition a | approval-status APPROVED valid=yes, head_sha 6e69a05e43774a140d28e6e6a5e21fcb27f55c27 = ls-remote tip |
| Precondition b | clock 19:29Z, 91 minutes before 21:00Z |
| Precondition c | 36 worktrees, 59 unique .open_deploys entries; none a live promote (devpln-r8 is fully closed, opened 12:19Z, PROD moved past it); portal CI had no run in progress |
| DEV | merge-forward result=MERGED pushed=yes; DEV 9e637fe51e -> 9de7c7e3227c321d45c2b6d3d3ccf72590b20710 (ls-remote read) |
| Release | release/20261014T193116Z, base PROD fa10e75861, head 5ab67a651a626e7224de0a2cf03a2223f99dc15e; --check READY |
| PROD | worktree ff-only, parity diff 0 bytes, 4 files / 718 insertions, typecheck rc=0, push fa10e758..5ab67a65; ls-remote PROD read 5ab67a65 |
| CI | run 38624676588 Deploy to Production completed / success (only workflow on that sha) |
| Tag | portal-v2.1.221 peels to 5ab67a651a62; portal-v2.1.220 peels to fa10e75861ab |
| Served read | https://opalinvest.dev (alias from infra/aws/terraform/portal-auth/cloudfront-distribution.tf): 68 paths in the chunk graph, 62 read OK, 6 HTTP 403 (file-name string literals, not assets). `data-asset-class-chip` in 1 file and `Trailing Returns` in 1 file, both index-TKcdTAwZ.js. Negative control: a nonsense string in 0 of 68. Source control: both strings absent at fa10e75861 and present at 5ab67a651a |

Page changed: Positioning (Satellites mode, factsheet popup), client-facing, Andrew's word cited in the order.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not stash or discard to fast-forward the main portal tree | Another seat has uncommitted edits to src/lib/firmAccess.ts, which the DEV merge also changed; the ff-only merge refused |
| Did not bump the workspace submodule pointer | The main tree is at local DEV 0a06280a, behind origin DEV 9de7c7e3; a pointer commit would pair the workspace with a stale portal state |
| Wrote no proof-of-spec instance | The order's scope asks for a report, not an instance; offered to the issuer if wanted |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| org/critical_paths/change_management/20261014T1930Z_j359-satellite-factsheet-portal-promote-dell1-20261014_deploy_completion.md | ledger, CLOSED | with this log |
| this log | session log and receipt | with this log |

---

## Blockers

Not blocked. OWED, not done: the workspace submodule pointer bump (prod-deploy Step 6). It needs the main portal tree fast-forwarded to origin/DEV 9de7c7e3, which `git merge --ff-only origin/DEV` refuses while src/lib/firmAccess.ts carries another seat's uncommitted edit. Owner: that seat, or the integrator 0.0.0_AB_MSTR.

---

## Current State

DEV 9de7c7e3227c321d45c2b6d3d3ccf72590b20710, PROD 5ab67a651a626e7224de0a2cf03a2223f99dc15e, CI success, ledger CLOSED, worktree removed, main portal tree on DEV. Requester check (for the issuer to relay): open each satellite popup on Positioning.
