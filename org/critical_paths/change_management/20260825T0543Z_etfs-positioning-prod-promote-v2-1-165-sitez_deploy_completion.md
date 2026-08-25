# Deploy Completion Record
**Date opened:** 2026-08-25T05:43:53.557519+00:00
**Status:** OPEN
**Deploy:** portal DEV->PROD promote v2.1.165 (site Z) -- INTRODUCES the ETF Positioning surface to PROD for the first time; carries tonight's 8-window etfAdapter spread fix (753b62a0). Payload 41 commits / 43 files, origin/PROD 8a96c916 .. origin/DEV 063ff4d7. OPAL_ADVIPOINTERS rides DORMANT (FLIP 0/15, re-derived at THIS cut ref).
**Authored by:** 0.2.0_DT_PortfolioAnalytics~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | ephemeral-worktree merge --no-ff origin/DEV 063ff4d7 onto PROD 8a96c916 | parity diff origin/DEV..HEAD EMPTY (0 bytes) | MERGED d9a98bcc (--no-ff, origin/DEV 063ff4d7 onto PROD 8a96c916), author 0.2.0_DT_PortfolioAnalytics~Z. PARITY GATE: git diff origin/DEV HEAD = 0 bytes / 0 lines, EMPTY. Merged-tree verification (on the shipping artifact, not on origin/DEV): etfAdapter.ts:97 carries '...h.returns' spread; NEGATIVE CONTROL the three-key allowlist 'QTD: h.returns.QTD' is GONE (rc=1). ADVI registry at the merged tree: 15 rows, held 14 / structural 1, FLIP 0 -> lands DORMANT. tsc -b --noEmit rc=0 on the merged tree. bun install foreground rc=0, 420 packages. | CLOSED 20260825T055119Z |
| L2 | git | origin/PROD advances 8a96c916 -> merge sha | ls-remote read, NOT the local ref | origin/PROD advanced 8a96c916 -> d9a98bcc. PUSHED BY 0.0.0_AB_MSTR~Z (integrator, GATE 5 LD-0367/LD-0368 -- I escalated rather than overrode; MSTR took the push rather than granting an override, msg 8471). PROOF IS AN ls-remote READ AT MY OWN SEAT, not the local ref and not MSTR's report: 'git ls-remote origin refs/heads/PROD' -> d9a98bcc39c0c87571961ef07ed51d7695dda85c. NEGATIVE CONTROL: pre-deploy sha 8a96c916 is no longer head. MSTR independently re-verified before pushing: parents 8a96c916+063ff4d7, parity 0 bytes, is-ancestor TRUE, spread present, 3-key allowlist count 0. | CLOSED 20260825T055508Z |
| L3 | verify | deploy.yml + EVERY workflow for the merge headSha | gh run list --json filtered to headSha; conclusion=success on ALL, never the branch badge | ENUMERATED BY COMMIT, not by branch badge and not by a single run. gh api repos/Opal-Capital/portal/commits/d9a98bcc.../check-runs -> total_count 3, ALL conclusion=success: 97700343325 Build Production Assets, 97700644776 Deploy to S3 + CloudFront, 97700679419 Tag Deployment. Workflow-level: run 32814624292 'Deploy to Production' status=completed conclusion=success event=push. CROSS-CHECK over a 60-run denominator with NO branch filter: exactly 1 run matches headSha d9a98bcc. POSITIVE CONTROL: the previous PROD head 8a96c916 also shows exactly 1 workflow run (32404149499, success) -- so one-workflow-per-PROD-push is this repo's normal shape, not a truncated view. | CLOSED 20260825T055634Z |
| L4 | verify | annotated tag portal-v2.1.165 | git rev-parse tag^{commit} PEELED == origin/PROD head | Annotated tag portal-v2.1.165 PEEL-VERIFIED. ls-remote shows the TAG OBJECT 8fd31fbbe32bc68f0dccae3fee7f5bcfd8d64463 at refs/tags/portal-v2.1.165 -- NOT compared, that is the v2.1.114 false-double-merge misread. PEELED: 'git rev-parse portal-v2.1.165^{commit}' = d9a98bcc39c0c87571961ef07ed51d7695dda85c == origin/PROD (ls-remote). git cat-file -t = 'tag' (annotated). NEGATIVE CONTROL: raw tag object 8fd31fbb differs from the peeled commit d9a98bcc, confirming annotated-not-lightweight, so the peel was a real operation and not an identity. | CLOSED 20260825T055726Z |
| L5 | git | workspace SITEZ submodule pointer -> portal 063ff4d7 | commit + push state stated by ls-remote |  | OPEN |
| L6 | verify | worktree pruned, portal main tree back on DEV | git -C portal branch --show-current == DEV |  | OPEN |

## Log

- 20260825T054353Z OPENED by 0.2.0_DT_PortfolioAnalytics~Z with 6 leg(s)
- 20260825T055119Z LEG L1 closed: MERGED d9a98bcc (--no-ff, origin/DEV 063ff4d7 onto PROD 8a96c916), author 0.2.0_DT_PortfolioAnalytics~Z. PARITY GATE: gi
- 20260825T055508Z LEG L2 closed: origin/PROD advanced 8a96c916 -> d9a98bcc. PUSHED BY 0.0.0_AB_MSTR~Z (integrator, GATE 5 LD-0367/LD-0368 -- I escalated 
- 20260825T055634Z LEG L3 closed: ENUMERATED BY COMMIT, not by branch badge and not by a single run. gh api repos/Opal-Capital/portal/commits/d9a98bcc.../
- 20260825T055726Z LEG L4 closed: Annotated tag portal-v2.1.165 PEEL-VERIFIED. ls-remote shows the TAG OBJECT 8fd31fbbe32bc68f0dccae3fee7f5bcfd8d64463 at 
