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
- **Anchor — DERIVE the workspace root; never type a device path** (CLAUDE.md NEVER: *derive, don't
  hardcode*). This procedure runs on more than one device and their roots differ; at least one
  contains a **SPACE**, so quote every expansion or word-splitting silently truncates the path:
  ```bash
  WS="$(git rev-parse --show-toplevel)" && cd "$WS"
  ```
  `$WS` is reused in Steps 4, 6 and 7. **Re-derive it in any new shell — but only while standing at
  the workspace root.** From inside the Step-4 worktree `--show-toplevel` returns THE WORKTREE, so
  carry the value forward rather than recomputing it there.
- Pull inbox (`check-inbox` + `get_agent_status`) — a pending `[STOP]`/`[HALT]` blocks the promote.
- **Declare the freeze window:** MCP COO that a promote is staged. The promote merges LIVE
  `origin/DEV` at GO time — it is NOT a frozen snapshot; any DEV commit pushed during the window
  silently rides into the promote as an unverified passenger
  (`feedback_portal_promote_remerges_live_dev_at_go_not_frozen_snapshot`). COO holds portal/DEV
  pushes until the promote lands.
- **If COO dispatched this promote via GO message:** the freeze is already active — skip the MCP
  notify, just confirm the GO is current (same session, no STOP received since) before proceeding.

## Step 1 — Clean up the DEV tree

```bash
git -C portal branch --show-current   # MUST print DEV — if PROD: git -C portal checkout DEV first (Rule 19)
git -C portal status --porcelain      # working tree must be CLEAN
git -C portal fetch origin
# Two cases — check which applies:
#   Local DEV has new commits not yet pushed (common: the commit you're about to promote):
#     → push DEV first (Step 1a below); do NOT pull (would discard the local commit)
#   Local DEV is behind origin/DEV:
#     → git -C portal pull origin DEV
git -C portal log --oneline origin/DEV..HEAD  # non-empty = local ahead → push case
```
- Stray uncommitted files: commit them properly (own lane) or clear them — never promote around a
  dirty tree.
- **`bun install` belongs in Step 4 (the worktree), not here.** Running it in the main tree is
  wasted work — the worktree gets its own node_modules. See Step 4.

### Step 1a — Push DEV if local is ahead

```bash
git -C portal push origin DEV   # NO MSYS_NO_PATHCONV — see Step 2
```
VALGATE D-1 runs on DEV push. PASS or PASS/WARN proceed; a hard BLOCK means fix the adapter gap
before promoting.

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
WS="$(git rev-parse --show-toplevel)"        # re-derive; do not assume Step 0's shell
WORKTREE="$WS/.runtmp/portal-promote-$(date -u +%Y%m%dT%H%M%SZ)"
git -C "$WS/portal" worktree add "$WORKTREE" PROD
cd "$WORKTREE"

# bun install FOREGROUND — node_modules required for the pre-push tsc gate.
# RESOLVE bun from PATH; NEVER a baked path (CLAUDE.md Portal: "resolve bun via profile, don't bake
# a path"). A device-specific path fails HERE — after the worktree exists — which is a half-landed
# promote (NEVER#2), and it fails looking like an environment problem rather than a procedure bug.
BUN="$(command -v bun)" || { echo "BLOCKED: bun not on PATH — resolve it BEFORE promoting"; exit 1; }
echo "OK: bun -> $BUN ($("$BUN" --version))"   # corruption oracle: echo the resolved path back
"$BUN" install

# Explicit --no-ff with a descriptive message encoding rollback SHA
PROD_BASE=$(git rev-parse origin/PROD)
git merge --no-ff origin/DEV \
  -m "merge DEV->PROD: vX.Y.Z — <description> @ DEV $(git rev-parse origin/DEV). Base $PROD_BASE. Rollback: $PROD_BASE. Authored <serial>."

# Parity gate — MUST be empty; non-empty = something is wrong with the merge
git diff origin/DEV HEAD   # empty = OK; any output = ABORT

# SEV1 HAND-CHECK ON THE MERGED TREE — STRUCK. THE TOOL IS RETIRED AND NOTHING REPLACES IT.
# retired-tombstone: comp-surface-check
#   ^ marks the mentions below as a DOCUMENTED RETIREMENT, not a route. comp-manifest-check's
#     retired-alias check text-matches the name and cannot tell the two apart; without this it
#     would force the explanation to be deleted to satisfy the gate. Exemption is COUNTED and
#     REPORTED by that check, never silent.
# A standing step lived here (COO adjudication 2026-08-04T054422Z, first exercised on the
# canonical-map promote 2d33ea2c) telling you to run `.tools/comp-surface-check check --mode
# blocking` by hand against the merged tree whenever the promote touched model-portfolio /
# benchmark / ADVI surfaces. comp-surface-check was RETIRED 2026-08-06 (Andrew-direct, verbatim:
# "I want comp-surface-check retired. i do not like that tool.") — the binary is gone from disk
# and off PATH, so the instruction was unrunnable. It is struck rather than left standing: an
# operator following it mid-promote gets `command not found` under a step whose own text said
# "silence is not a pass."
#
# ⚠ NO GUARD REPLACES IT. The model-portfolio / benchmark / ADVI surfaces now carry NO automated
# commit-time check — CLAUDE.md Rule 20 records that as the ACCEPTED CONSEQUENCE of the
# retirement, not as a gap to be worked around or re-filled on your own initiative. The promote
# proceeds without it. Building a replacement guard is an Andrew call (Rule 20 + the standing
# no-unrequested-gates rule), not a promote-time decision.
#
# THE PROMOTE SEQUENCE IS OTHERWISE UNCHANGED — nothing renumbered, no step reordered. Struck
# 2026-08-06 by 0.8.0_AE_CloudComp under 1.0.0_SA_CTO~B routing 20260806T213335Z, after an
# estate-wide retired-alias sweep found this live citation of a deleted binary. A change to the
# promote SEQUENCE itself is the DT lane's call, not this strike's.

git push origin PROD       # plain push; no MSYS_NO_PATHCONV; VALGATE + tsc gate runs here
```
The main `portal/` tree stays on DEV throughout — never run the merge there, and never run
`bun run dev` from the `.runtmp` worktree (it hides a stranded main tree).

`bun install` must be **FOREGROUND** — a backgrounded install silently stalls the promote
mid-flight (`reference_portal_promote_backgrounded_bun_install_idle_stall`, v2.1.116: ~26min
alive-but-idle). Without it the pre-push hook fails with `tsc: command not found`.

## Step 5 — Deploy verification (CI does the server deploy + tag)

The PROD push triggers `deploy.yml`: build → deploy to the server → annotated tag `portal-vX.Y.Z`.

```bash
gh -R Opal-Capital/portal run list --branch PROD --limit 1              # grab the run id
gh -R Opal-Capital/portal run view <run-id> --json conclusion,status    # THE verification
```
⛔ **`-R` IS LOAD-BEARING, NOT TIDINESS. `gh` RESOLVES THE REPO FROM CWD, AND THE WORKSPACE ROOT IS A
DIFFERENT GITHUB REPO THAN `portal/`.** Run bare at the workspace root — where Steps 6 and 7 put you —
these query `Opal-Capital/ajb_workspace`, which **has no PROD branch, so they return `[]` with no
error**:
```
at ajb_workspace root :  gh run list --branch PROD -> []        gh repo view -> Opal-Capital/ajb_workspace
inside portal/        :  gh run list --branch PROD -> 3 runs    gh repo view -> Opal-Capital/portal
```
**`conclusion: "success"` is the gate, and an empty list yields no conclusion at all — so a wrong-repo
read is INDISTINGUISHABLE from "still building", on the one step that verifies the promote.** The
failure is silent in both directions: a green promote that never verifies, or a wait for a run that
already succeeded in a namespace you are not reading. Same class as org/XXX.md Step 1a's bare
`git log` inside `portal/`. **Positive-control any empty `gh` result** by dropping the filter and
running `gh repo view --json nameWithOwner` before you conclude anything from a zero.
*(Measured with that positive control 2026-08-28 by 0.4.0_DT_ClientPlatform~Z while loading this
procedure; ruled in by 1.0.0_SA_CTO~Z + 2.0.0_SA_COO~Z.)*
- **A "CI green" claim ENUMERATES WORKFLOWS, listed by headSha — never the branch badge or a
  single run** (CTO-banked near-miss law, 2026-08-04). Multiple workflows run per push
  (`gh -R Opal-Capital/portal run list --json databaseId,headSha,workflowName,status,conclusion`
  filtered to the exact sha — `-R` here for the same reason as above); one can be green while
  another is red on the SAME commit. Incident-as-fixture: on
  `7d544d27`, `CI - Build & Validate` was SUCCESS while the `Surface-Check Gate` was FAILURE
  (runs 30880062803 / 30880062845) — a promote verified on the first workflow alone would have
  launched past a red non-bypassable backstop; it was caught only by listing runs by headSha.
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
cd "$WS"    # the value derived at Step 0/4 — quoted (the path may contain a space)
# ⛔ Do NOT re-derive with `git rev-parse --show-toplevel` HERE. Step 4 left you inside $WORKTREE,
#    which is its own git worktree, so --show-toplevel returns THE WORKTREE, not the workspace root.
#    Derive $WS while standing at the workspace root; carry the value. If $WS is empty (new shell),
#    cd to the workspace root by hand first, then re-derive.
# Main tree should still be on DEV — verify, do NOT checkout (it never left)
git -C portal branch --show-current   # expect: DEV
.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" \
  -m "bump portal pointer -> <DEV-HEAD>; live PROD=<merge-sha> (tag portal-vX.Y.Z), <description>; CI run <id> SUCCESS" \
  -- portal
git push origin CLOUD
```
(The pointer commit records which portal state the workspace pairs with; push goes through the
pre-push safe-deploy/HALTGT net normally. Commit message should encode the PROD merge SHA + tag
for traceability — see session logs for examples.)

## Step 7 — Teardown + flip back to DEV (the conclusion Andrew named)

```bash
cd "$WS"    # same caveat as Step 6 — carry the value, do not re-derive from inside the worktree
git -C portal worktree remove "$WORKTREE" 2>/dev/null || true
git -C portal worktree prune   # cleans git's internal tracking regardless of physical outcome
git -C portal branch --show-current   # MUST print DEV
pwd                                    # MUST be the workspace root (base doctrine)
```
**Windows long-path note:** `worktree remove` frequently fails with "Filename too long" on this
host — the physical `.runtmp/portal-promote-*` directory persists. That is acceptable: it is
gitignored and operationally inert. `worktree prune` cleans git's internal worktree tracking
even when the physical remove fails — run it every time. Do not leave a second `git worktree
add` attempt for the same PROD branch without pruning first (the "PROD is already used by
worktree" error class).

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
