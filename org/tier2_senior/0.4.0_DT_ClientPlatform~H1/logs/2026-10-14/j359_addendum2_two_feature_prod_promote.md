# J359 addendum 2 + TRSB Excel fix promoted to portal PROD in one release (portal-v2.1.222) -- 0.4.0_DT_ClientPlatform~H1

**archetype:** DEPLOY
**Date:** 2026-10-14
**Task Order:** ADHOC.j359-addendum2-footnote-deletion-promote (org/tier2_senior/0.4.0_DT_ClientPlatform~H1/task_orders/ADHOC.j359-addendum2-footnote-deletion-promote.md; GO msgs 5897 and 5901 from 2.0.0_SA_COO~J1)
**Status:** COMPLETE

---

## Objective

One PROD release carrying two approved features: cand/dell1/satellite-returns-method @714f8e48c8 (deletes the hypothetical-returns disclaimer and exclusions footnote under Trailing Returns; client-facing; row fbdf) and cand/dell1/trsb-history-excel-download @040b152f41bf (Download Excel reads download_url; opal-internal; row c2b9). Andrew-direct via the CTO, record ANDREW_DIRECT_20261014_205xZ_ONE_PROMOTE_TRSB_FIX_PLUS_J359_DELETION.md @4bbfec5238.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| open-calls | `approval-status` for both branches | PASS | both APPROVED valid=yes, head_sha = ls-remote tip; TRSB tip IN-DEV |
| portal-merge-forward | `cand/dell1/satellite-returns-method --push` | PASS | MERGED pushed=yes |
| portal-release-build | build with both features, then `--check` | PASS | READY, features=2, unapproved=0, 1 client-facing |
| deploy_ledger | open, close-leg x4, close | PASS | 4 legs, CLOSED |
| bundle_read.sh (scratchpad) | crawl of the deployed chunk graph | PASS | same crawl before and after: 68 paths, 62 OK, 6 x 403 |

**What worked:** running the SAME crawl before and after, so the denominators are identical; confirming the crawl reaches trade-submission code (3 files carry the marker) before trusting the `download_url` absence.
**What failed:** nothing. The order was amended twice while I read it (restart hold, then the second feature); I re-read the full diff of the order against HEAD before acting on either.
**Gap found:** none new.

---

## Work Completed

| Step | Result |
|---|---|
| Preconditions | restart held (record 11a1d08ef0, Andrew-direct ~20:49Z); clock 20:54Z; approval APPROVED valid=yes, tip 714f8e48c8 = ls-remote; served key VersionId Qh56dS_IliDOh0owKxjToBgEjgJ0pb8v (20:15:50Z) as the order states; 35 worktrees, 59 unique .open_deploys entries; portal CI had no run in progress |
| Judgment call | The union held j359-addendum2-satellite-returns-deploy-dell1-20261014 (AE producer deploy, all 6 legs OPEN in the snapshot at wk-canon-r7-25 only). It writes the Lambda and the data key, not portal PROD, and the key it produces already reads as the order requires, so I did not treat it as a competing promote |
| BEFORE read | 62 files: holdings at today 1, left out for lack of one 1, chip 1, Trailing Returns 1, download_url 0; trade-submission code present in 3 files (so the absence is a real negative) |
| DEV | MERGED pushed=yes; DEV bbad56e354 -> e578b378d332ad1505018be3801466dac7aeeade (ls-remote read) |
| Release | release/20261014T205906Z, base PROD 5ab67a651a62, head 5d64641891207b68998973e7c82c0dd0260b4dab; --check READY |
| PROD | worktree ff-only, parity diff 0 bytes, 4 files (49 insertions, 114 deletions), typecheck rc=0, push 5ab67a65..5d646418; ls-remote read 5d646418 |
| CI | run 38637040693 Deploy to Production completed / success (only workflow on that sha) |
| Tag | portal-v2.1.222 peels to 5d64641891207b68998973e7c82c0dd0260b4dab |
| AFTER read | 62 files, 6 x 403: holdings at today 0, left out for lack of one 0, chip 1, Trailing Returns 1, download_url 1 (index-JYduzYBC.js), presigned_url 0, negative control 0. Main bundle hash index-TKcdTAwZ -> index-i8K0Vhin |
| Pointer (Step 6) | portal main tree was clean, fast-forwarded to origin/DEV e578b378, pointer commit 4aabecd63b. It also closes the pointer step I left owed after the first J359 promote (5ab67a651a62) |

Pages changed: Positioning (Satellites mode, factsheet popup), client-facing, Andrew's word cited in the order; Trade Submission, opal-internal, row dell1-20261014T204814Z-c2b9.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Verified the TRSB approval row and DEV membership myself | The widening reached me as an order amendment; `approval-status` is a one-line read and the release builder refuses unapproved branches anyway |
| Treated the AE producer ledger entry as not a competing promote | See Work Completed |
| Fast-forwarded the main portal tree only after it read clean | Last time another seat's uncommitted edit blocked it, and I would not stash it |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal (submodule pointer) | 9de7c7e3 -> e578b378 | Yes -- `4aabecd63b` |
| org/critical_paths/change_management/20261014T2058Z_j359-addendum2-two-feature-portal-promote-dell1-20261014_deploy_completion.md | ledger, CLOSED | with this log |
| org/tier2_senior/0.4.0_DT_ClientPlatform~H1/task_orders/ADHOC.j359-addendum2-footnote-deletion-promote.md | status staged -> pending (the order says to flip it on the GO) | with this log |
| this log | session log | with this log |

---

## Blockers

None.

---

## Current State

DEV e578b378d332ad1505018be3801466dac7aeeade, PROD 5d64641891207b68998973e7c82c0dd0260b4dab (portal-v2.1.222), CI success, ledger CLOSED, worktree removed, main portal tree on DEV and clean, pointer committed LOCAL on box/dell1. Requester check (for the issuer to relay): open each satellite popup on Positioning and confirm no disclaimer or footnote under Trailing Returns; open Trade Submission and use Download Excel.
