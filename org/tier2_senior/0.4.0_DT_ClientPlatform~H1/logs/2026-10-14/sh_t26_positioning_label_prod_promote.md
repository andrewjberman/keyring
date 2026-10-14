# Positioning frontier label promoted to portal PROD (portal-v2.1.220) -- 0.4.0_DT_ClientPlatform~H1

**archetype:** DEPLOY
**Date:** 2026-10-14
**Task Order:** MDPF_SECHIST.TO-SH-t26
**Status:** COMPLETE (proof-of-spec verdict reported separately)

---

## Objective

Promote release/20261014T184507Z (one feature, cand/dell1/sechist-frontier-label, row c822 approved by andrew) to portal PROD with `/prod-deploy`, read the CI conclusion, and write the receipt. The CTO seated this lane for the promote (msg 5709); the issuer 2.0.0_SA_COO~H1 cut the order (msg 5714).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `--name '*' org/mcp/inbox/0.4.0_DT_ClientPlatform` | PASS | 14-file denominator; showed the ~H1 inbox held no mail |
| portal-release-build | `--check release/20261014T184507Z` | PASS | READY, 1 feature, 0 unapproved |
| deploy_ledger | `open`, `close-leg` x3, `close` | PASS | `open` commits itself; `close-leg` and `close` leave files modified |
| proof-of-spec-check | on the committed instance | PARTIAL | first run INVALID on my own mistakes (ids, kind, genre, expect shape); fixed in a follow-up commit |
| comp-which | not run | SKIPPED | seat seated mid-session for one promote; the A.3 rail exercise was not done |

**What worked:** the release builder's `--check`, and polling `gh run view` by id instead of `gh run watch`.
**What failed:** my first instance used the short ids AC1..AC3, `genre: DEPLOY` (the order carries no `<proof_genre>` marker, so it cannot be claimed), a `git_ref` artifact kind outside the enum, and prose in `expect` where the checker wants a regex.
**Gap found:** none new; the schema enum has no git-ref kind, so a PROD ref is recorded as `frontend_component`.

---

## Work Completed

### 1. Seating
The CTO message did not reach the ~H1 lane inbox at first. I asked 1.0.0_SA_CTO~DELL1; msg 5709 answered: seated for the SECHIST c822 promote, not J359. The J359 message in the ~R1 folder was another lane's and was not acted on.

### 2. Promote
| Step | Result |
|---|---|
| Base | origin/PROD 6a5926fc1194; candidate c77f23624d IN-DEV |
| Check | `--check` READY, head fa10e75861ab |
| Worktree | ephemeral, `bun install` foreground, `--ff-only` of the release, parity diff 0 bytes, 7 files / 392 insertions |
| Typecheck | `bun run typecheck` rc=0 on the merged tree |
| Push | `6a5926fc..fa10e758  PROD -> PROD`; `ls-remote` read fa10e75861abd352ab033f5c7ab4b9e1f0f297e9 |
| CI | run 38619242657 Deploy to Production, completed / success (the only workflow on that sha) |
| Tag | portal-v2.1.220 peels to fa10e75861ab; portal-v2.1.219 peels to 6a5926fc1194 |
| Teardown | worktree removed and pruned; portal main tree on DEV; cwd the workspace root |

Page changed: /positioning, client-facing. The submodule pointer bump (prod-deploy Step 6) was not made: it writes `portal`, outside the order's `<paths>`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Typecheck in the worktree, not the main tree | The main tree carries three other seats' modified files; the worktree is the tree that was pushed |
| Used the issuer's existing release branch | PROD had not moved, so the order said not to rebuild |
| Skipped the Step 6 pointer commit | Outside the order's `<paths>` and its bound 3 |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.4.0_DT_ClientPlatform~H1/PROMOTE_RECEIPT_SH_T26.md` | receipt | Yes -- `c8b440ce01` |
| `org/critical_paths/change_management/20261014T1852Z_sechist-positioning-label-prod-promote-dell1-20261014_deploy_completion.md` | ledger, CLOSED | Yes -- `c8b440ce01` |
| proof-of-spec instance (same folder as the receipt) | AC1-AC3 | `c8b440ce01`, revised after the first checker run |

---

## Blockers

None.

---

## Current State

PROD is at fa10e75861abd352ab033f5c7ab4b9e1f0f297e9, CI success, ledger CLOSED. Owed: the checker verdict line and the report to 2.0.0_SA_COO~H1 and 1.0.0_SA_CTO~DELL1. The SH-t-24 producer apply is the issuer's to start.
