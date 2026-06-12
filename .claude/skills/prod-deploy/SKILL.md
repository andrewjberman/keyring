---
name: prod-deploy
description: DT-only — the canonical portal DEV->PROD promote procedure (Andrew-direct 2026-06-12). The exact process, in order — clean up the DEV tree, zero typescript errors, re-assert local PROD from origin, merge forward to PROD in an EPHEMERAL worktree (the main portal tree NEVER leaves DEV), push (CI deploys to the server + tags), verify the CI conclusion via gh run view --json (gh run watch can hang on benign warnings), update the workspace submodule pointer on CLOUD, tear down the worktree, confirm the main tree is back on DEV, end at the workspace root. Folds every banked promote footgun: PROD-branch dry-run pollution (Step-2 update-ref), MSYS_NO_PATHCONV breaking the VALGATE pre-push gate, the not-a-frozen-snapshot re-merge window (hold DEV pushes), foreground-only bun install, annotated-tag peeling for verification. Other agents invoking this halt at Step 0 — portal PROD promotes are a DT lane.
---

# /prod-deploy — portal DEV → PROD promote (DT canonical procedure)

The exact process for shipping the portal to production. **DT-only** — any other serial halts at
Step 0 and routes to the pod DT. Every step exists because skipping it has bitten us; the
incident anchors are cited inline. Design history: `docs/briefs/portal-main-tree-stays-on-dev-rule-20260526.md`
+ the promote-footgun memory cluster.

**Two invariants frame everything:**
1. **The main `portal/` tree NEVER leaves DEV** (CLAUDE.md Rule 19). The promote executes in an
   ephemeral worktree; if you ever find the main tree on PROD, `cd portal && git checkout DEV`
   before anything else.
2. **Portal is a work-site, not your base** (org/XXX.md Step 1a). Start from and end at the
   workspace root.

## Step 0 — Gate + freeze window

- **DT-only check:** if your serial is not a `0.x.0_DT_*` (or explicitly Andrew-directed), HALT —
  route to the pod DT.
- Anchor: `cd /c/Users/AndrewBerman/Desktop/ajb_workspace`.
- Pull inbox (`check-inbox` + `get_agent_status`) — a pending `[STOP]`/`[HALT]` blocks the promote.
- **Declare the freeze window:** MCP COO that a promote is staged. The promote merges LIVE
  `origin/DEV` at GO time — it is NOT a frozen snapshot; any DEV commit pushed during the window
  silently rides into the promote as an unverified passenger
  (`feedback_portal_promote_remerges_live_dev_at_go_not_frozen_snapshot`). COO holds portal/DEV
  pushes until the promote lands.

## Step 1 — Clean up the DEV tree

```bash
cd portal
git branch --show-current        # MUST print DEV — if PROD: git checkout DEV first (Rule 19)
git status --porcelain           # working tree must be CLEAN
git pull origin DEV              # the promote ships origin/DEV; local must match
```
- Stray uncommitted files: commit them properly (own lane) or clear them — never promote around a
  dirty tree.
- If dependencies changed: `bun install` **FOREGROUND** — a backgrounded install silently stalls
  the promote mid-flight (`reference_portal_promote_backgrounded_bun_install_idle_stall`,
  v2.1.116: ~26min alive-but-idle).

## Step 2 — Zero TypeScript errors

```bash
bun run typecheck                # 0 errors required — fix or abort, never promote a red tree
```
The VALGATE D-1 pre-push gate re-runs checks at push time. **NEVER `export MSYS_NO_PATHCONV=1`
for portal git operations** — it mangles the hook's `/c/` path resolution and fail-closes the
push; the tell is typecheck PASSES locally but the push blocks
(`feedback_no_msys_pathconv_on_portal_git_push`). That env var is for Terraform/ARN work only.

## Step 3 — Re-assert local PROD from origin (kills the dry-run-pollution class)

```bash
git fetch origin
git update-ref refs/heads/PROD refs/remotes/origin/PROD   # non-destructive
```
A prior verify-without-push dry-run leaves a committed merge on LOCAL PROD that the next
worktree-add would silently base on (`feedback_portal_promote_dryrun_pollutes_local_prod_branch`,
v2.1.114 stale 47b3d5d7). Step 3 is mandatory on EVERY promote, not just after known dry-runs.

## Step 4 — Merge forward to PROD in an EPHEMERAL worktree

```bash
cd /c/Users/AndrewBerman/Desktop/ajb_workspace/portal
git worktree add ../.runtmp/portal-promote-$(date -u +%Y%m%dT%H%M%SZ) PROD
cd ../.runtmp/portal-promote-*/
git merge origin/DEV --no-edit   # the forward-merge: DEV -> PROD
git push origin PROD             # plain push; no MSYS_NO_PATHCONV; VALGATE gate runs here
```
The main `portal/` tree stays on DEV throughout — never run the merge there, and never run
`bun run dev` from the `.runtmp` worktree (it hides a stranded main tree).

## Step 5 — Deploy verification (CI does the server deploy + tag)

The PROD push triggers `deploy.yml`: build → deploy to the server → annotated tag `portal-vX.Y.Z`.

```bash
gh run list --branch PROD --limit 1                 # grab the run id
gh run view <run-id> --json conclusion,status       # THE verification
```
- **`gh run watch` can HANG on benign warning output** (Node 20 deprecation, cache 400) — watch
  silence is NOT a stall signal and NOT a success signal. Always confirm the final outcome via
  `gh run view --json conclusion` (DT anomaly, v2.1.121 promote 2026-06-12). `conclusion:
  "success"` is the gate.
- **Tag verification — peel the annotated tag:** `git ls-remote --tags` shows the TAG OBJECT sha,
  not the commit. Compare `git rev-parse <tag>^{commit}` against the PROD head
  (`reference_annotated_tag_lsremote_shows_object_sha_not_commit` — the v2.1.114 false
  double-merge misread).
- Optional live smoke for user-facing changes: load the served site; for ADVI/MDPF data-path
  changes confirm the served artifact, not a proxy.

## Step 6 — Workspace submodule pointer (CLOUD)

```bash
cd /c/Users/AndrewBerman/Desktop/ajb_workspace
git -C portal fetch && git -C portal checkout DEV && git -C portal pull origin DEV
.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" \
  -m "portal(promote): submodule pointer -> portal-vX.Y.Z (PROD <commit>)" -- portal
git push origin CLOUD
```
(The pointer commit records which portal state the workspace pairs with; push goes through the
pre-push safe-deploy/HALTGT net normally.)

## Step 7 — Teardown + flip back to DEV (the conclusion Andrew named)

```bash
git worktree remove .runtmp/portal-promote-*        # ephemeral worktree gone
git -C portal branch --show-current                  # MUST print DEV
pwd                                                  # MUST be the workspace root (base doctrine)
```
If the main tree is on PROD here, that IS a strand incident — `git -C portal checkout DEV` now
and note it in the log; do not leave it for the missing-DEV-feature symptom to reveal.

## Step 8 — Report + release the freeze

RAVC report to COO (releases the DEV-push hold) + session log. The artifact table is the report:

| Field | Value |
|---|---|
| PROD commit | `<hash>` |
| Tag | `portal-vX.Y.Z` (peeled-verified) |
| CI run | `<id>` + `conclusion: success` |
| Workspace pointer | `<CLOUD hash>` (pushed) |
| Main tree | back on DEV (verified) |

## Abort path

Any gate failure (typecheck red, VALGATE block, CI `conclusion != success`, merge conflict you
cannot adjudicate): STOP, do not improvise around the gate. Tear down the worktree, leave PROD
untouched (or if the push landed but CI failed: surface to COO + CTO immediately — do NOT
re-push or revert unilaterally), release the freeze window with an ABORTED status, log the
failure with the actual output.
