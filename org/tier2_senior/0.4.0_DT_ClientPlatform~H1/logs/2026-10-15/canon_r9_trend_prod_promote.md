# Global AUA Trend with Custom Models roll-forward promoted to portal PROD (portal-v2.1.223) -- 0.4.0_DT_ClientPlatform~H1

**archetype:** DEPLOY
**Date:** 2026-10-15
**Task Order:** ADHOC.canon-r9-trend-portal-promote (org/tier2_senior/0.4.0_DT_ClientPlatform~H1/task_orders/ADHOC.canon-r9-trend-portal-promote.md; GO msg 5978 from 2.0.0_SA_COO~D1)
**Status:** COMPLETE

---

## Objective

Promote cand/dell1/mdpf-canon-global-trend-variant1-rf @15f7610285 (row dell1-20261015T013256Z-f411, approved by andrew, client-facing, /portfolios) to PROD as a one-feature chosen-set release. DEV is not a leg (CTO ruling msg 5977): DEV converges separately.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| open-calls | `approval-status --branch cand/dell1/mdpf-canon-global-trend-variant1-rf` | PASS | APPROVED valid=yes, head_sha = ls-remote tip |
| portal-release-build | build, then `--check release/20261015T014043Z` | PASS | READY, 1 feature, 0 unapproved, 1 client-facing |
| deploy_ledger | open, close-leg x3, close | PASS | 3 legs, CLOSED |
| bundle_read.sh (scratchpad) | crawl of the deployed chunk graph | PASS | same crawl before and after: 68 paths, 62 OK, 6 x 403 |

**What worked:** testing a page-specific marker string (`Additive SMA sleeves`, `Model Overview`) in the BEFORE bundle to prove the crawl reached ModelPortfolios-D6ihy19n.js before trusting the absence of the three new strings. My first guess at a marker ("Other Models") found nothing, which would have been a silent weak control had I not tested it.
**What failed:** nothing.
**Gap found:** none new.

---

## Work Completed

| Step | Result |
|---|---|
| Preconditions | approval APPROVED valid=yes, tip 15f7610285f7719e837f3783fed51e03413a8671 = ls-remote; PROD 5d64641891 as stated; served key VersionId s5Z3becVq3gTW09YzbVVb_HRopzUxFzC (2026-10-14T23:10:55Z) carrying client_supervised_aua, etf_strategies_aua, alt_strategies_aua, carried_dates; restart held, no new notice; 34 worktrees, 60 unique .open_deploys entries; portal CI had no run in progress |
| Judgment call | The union held mdpf-canon-edge-firm-gate (AE~U7, Lambda@Edge change on the portal CloudFront distribution, opened 2026-10-14T22:30:57Z, 6 legs all OPEN, window 4h). I measured it: lane ~U7 not registered, the entry's log holds only its opening line, 3h without progress. It changes Lambda@Edge associations; this promote changes the S3 bucket and invalidates, not the distribution. I treated it as not in flight and proceeded; the issuer 2.0.0_SA_COO~D1 also issued that order and sent this GO. Disclosed in the report |
| BEFORE read | 62 files: data-trend-composition 0, Carried forward (last known value) 0, models held at one firm are in the total 0, data-asset-class-chip 1; crawl reaches ModelPortfolios-D6ihy19n.js (the old page chunk) |
| Release | release/20261015T014043Z, base PROD 5d64641891, head c3b21a40e29f690922f442c085129f9ba85ce334; --check READY |
| PROD | worktree ff-only, parity diff 0 bytes, 6 files (586 insertions, 78 deletions), typecheck rc=0, push 5d646418..c3b21a40; ls-remote read c3b21a40 |
| CI | run 38667132776 Deploy to Production completed / success (only workflow on that sha) |
| Tag | portal-v2.1.223 peels to c3b21a40e29f690922f442c085129f9ba85ce334 |
| AFTER read | 62 files, 6 x 403: all three feature strings 1 file each (ModelPortfolios-iAeFpD-x.js), chip 1 (index-C_hwoorU.js), negative control 0. Page chunk hash D6ihy19n -> iAeFpD-x |
| Pointer (Step 6) | portal main tree clean; fast-forwarded to origin/DEV e0b033253b97; pointer commit 4ca51cb5f6 (LOCAL on box/dell1) |

Page changed: /portfolios (Model Portfolios: Global Trend, firm views, Other Models card), client-facing, Andrew's word in the order, row dell1-20261015T013256Z-f411.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Proceeded past the open edge-firm-gate ledger entry | See Work Completed: not running, different artifact |
| Did not touch DEV | The order says DEV is not a leg; /prod-deploy did not refuse over DEV, so no stop was needed |
| Pointer pairs with DEV e0b033253b97 | DEV does not carry this feature yet (ancestry check NO), so PROD runs ahead of the pointed state on this one feature; the commit message says so |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal (submodule pointer) | e578b378 -> e0b033253b | Yes -- `4ca51cb5f6` |
| org/critical_paths/change_management/20261015T0140Z_canon-r9-trend-portal-promote-dell1-20261015_deploy_completion.md | ledger, CLOSED | with this log |
| org/tier2_senior/0.4.0_DT_ClientPlatform~H1/task_orders/ADHOC.canon-r9-trend-portal-promote.md | status staged -> pending (the order says to flip it on the GO) | with this log |
| this log | session log | with this log |

---

## Blockers

None. Worktree .runtmp/portal-promote-20261015T014107Z could not be physically deleted (Permission denied); git no longer tracks it (worktree prune, 0 entries). Gitignored and inert per /prod-deploy Step 7.

---

## Current State

PROD c3b21a40e29f690922f442c085129f9ba85ce334 (portal-v2.1.223), CI success, ledger CLOSED, main portal tree on DEV and clean. DEV does not carry the feature: the issuer converges it by merge-forward of its resolution branch. Requester check (for the issuer to relay): open /portfolios as an internal session and as a client session, confirm the Global AUA Trend draws Nov 2024 to the as-of with the composition marker and the carried-forward note.
