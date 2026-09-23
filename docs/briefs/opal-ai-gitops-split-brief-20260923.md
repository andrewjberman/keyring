# BRIEF -- splitting `opal_ai` off from `ajb_workspace` in GitOps: portal-shaped, done properly

**Author:** `4.0.0_SA_CRO~X` | **Written:** 2026-09-23 (UTC) | **Mode:** NEW
**Asked by:** Andrew, directly at this seat's terminal, 2026-09-23 ~22:0xZ. Verbatim record:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260923_220xZ_OPAL_AI_GITOPS_SPLIT_SPEC.md` @`bd282e03e9`.
**Consumer:** `1.0.0_SA_CTO~Z` `/endpoint --forward`.
**Companion:** `docs/briefs/opal-ai-microproduct-repo-brief-20260923.md` (RCN-0014, @`a47993af9c`) says WHAT goes into
`opal_ai`. This brief says what must happen in git, gates, tooling and deploy for it to live beside the monolith.
**Vintage:** SITEZ @`bd282e03e9`, 2026-09-23 ~22:0xZ-22:4xZ. Repo and local git reads only; no GitHub, AWS or EC2 read.

---

## ANDREW'S WORDS, VERBATIM

> Ok now I need another spec from you where you basically figure out what needs to happen to properly split this off
> in GitOps from ajb_workspace. It should be the same structure as the portal where it is contained in the monolith,
> but it has its own git submodule or whatever so we can keep it clean and separated but still have the benefit of the
> ajb_workspace tooling and process ops and so on.

**Three requirements in his sentence:**
- **contained** -- it sits inside the monolith's tree, the way `portal/` does;
- **separate** -- its own repository and history;
- **tooled** -- the workspace's tooling and process ops still apply to it.

The finding that shapes everything below: **today's portal delivers the first two and only part of the third**
(Part IV finding 3), so "the same structure as the portal" has to mean the portal's SHAPE with the gaps closed. A copy of
how the portal is wired today would not do it.

---

## PART I -- THE OUTCOME TERRITORY

### THE CANDIDATE THREAD (becomes FWD-1 at L2)

**One seat, one device, one gateway file.**
1. A fresh checkout of `ajb_workspace` on either device brings `opal_ai` in at the commit the workspace records.
2. The seat edits one gateway file inside it and commits in `opal_ai`, graded by the same gates a parent commit gets.
3. It bumps the parent's pointer, and a drain lands both.

This is the smallest journey that exercises all three requirements (contained, separate, tooled) end to end.

#### O1. Anyone who checks out `ajb_workspace`, on either device or in a fresh worktree, gets `opal_ai` at the recorded commit with one standard command
Nobody hand-clones a nested repo into place. An empty directory where the product should be is refused, never
silently accepted.

#### O2. A commit inside `opal_ai` is graded by the same gates as a commit in the parent
Syntax and lint on Python, lane ownership, the commit-message rules and the surprise-row check all apply. Nothing
escapes a gate because it lives in the nested repository.

#### O3. The `opal_ai` repository stands on its own
Cloned alone, without the monolith, its template slice builds and its tests run. That is what keeps it "clean and
separated", and it is what a client deployment is later cut from.

#### O4. A COO dispatches a worker whose paths lie in `opal_ai`, and the worker gets its own `opal_ai` worktree and drains it back
The same journey a portal cell has today, without portal-specific code.

#### O5. The Opal Gateway deploys from `opal_ai` with no loss of safety
The clean-tree check and the recorded deployed commit refer to the repository that actually holds the deployed bytes.

#### O6. The Opal Analyst launches on the terminal box after its files move, with its fence, skills and identity binding working
A seat that loses its fence on the move fails this outcome, even if it answers questions.

#### O7. At any moment Andrew or MSTR can say which `opal_ai` commit the workspace pairs with and which one is deployed
The same way the portal pointer bumps say so for the portal today.

#### O8. Both fabrics integrate `opal_ai` changes without the pointer silently dropping one side's work

#### O9. The moved code keeps its history, and every old citation still resolves
`git log` and `blame` work on the gateway's files inside `opal_ai`. Every existing citation of the form
`infra/aws/ec2/opal-gateway/...@<sha>` still resolves at its pin.

#### O10. The fabric's own reporting counts work done in `opal_ai`
Activity views, the daily sprint and outcome reports see its commits. Today they see only the parent's pointer bumps.

---

## PART II -- WHERE THE BOUNDARY SITS

| This split OWNS | It RELIES ON (and does not change) | Holder |
|---|---|---|
| The repository's existence and wiring: `.gitmodules`, the pointer, the move with history | WHAT moves (RCN-0014's scope and its call 1, one repo) | Andrew + `0.0.0_AB_MSTR~Z` create the repo (outward-facing); `1.0.0_SA_CTO~Z` routes |
| Making the workspace's git gates, lanes, worker provisioning and census tools work for a nested repo | The gates' RULES themselves (Rule 14, lanes, the message rule) -- extended in reach, never in content | the owners of `.tools/` |
| Re-pointing the gateway's deploy path and its two guards | The EC2, its role, the Terraform root, `safe-apply` | `0.7.0_AE_CloudOps` lanes |
| Re-pointing the Analyst's launcher, fence and skills | The Bloomberg operator duty, which stays in the workspace (09-22 ruling, call 1) | `0.0.0_AB_MSTR` (launcher), the fence's owner |
| Mapping `portal` and `models/factor_scanner` in the same act (09-22 ruling, call 5) | The portal's own DEV/PROD flow and CI | the portal's owners |

**Explicitly NOT this split's:** the contents of the three slices; the template's extraction (RCN-0014 Part V item 3);
any change to what the gates enforce; the portal's promote flow; client repositories.

---

## PART III -- THE QUALITATIVE BAR

- **No silent zero.** A tool pointed at the nested repo either sees inside it or says it cannot. Today several read a
  whole nested repository as one unchanged pointer and report "clean" (Part IV finding 5).
- **No fail-open gate.** A gate that cannot find its configuration inside `opal_ai` refuses the commit. It does not warn
  and let it through.
- **No second copy.** At no point do two live copies of the gateway exist, one in the parent and one in `opal_ai`.
- **Separation you can test.** Someone at another firm can clone `opal_ai` and it works without the monolith.
- **One command, both devices.** The same checkout step works on the laptop and on site Z, and in a sparse worktree.
- **The seat is never less safe after the move than before it.** Its fence is proven active by one denied write, not
  assumed.

---

## PART IV -- THE SUBSTRATE (findings, each with what was measured)

### What "the portal structure" actually is today

1. **`portal/` is not a git submodule. It is an independent clone sitting inside the tree, plus a gitlink in the
   parent.**
   - `.gitmodules` is **0 bytes**. `git config --get-regexp '^submodule\.'` returns nothing, and `.git/modules/` does
     not exist.
   - `portal/.git` is a full directory, not a gitfile.
   - `git ls-files -s` shows two gitlinks: `portal` @`10141b6d` and `models/factor_scanner` @`c59b266a`.
   - `git submodule status` FAILS: *"no submodule mapping found in .gitmodules for path 'models/factor_scanner'"*.
   - `models/factor_scanner` is an **empty directory**: a gitlink whose content was never cloned, and nothing says so.

   **So a fresh clone of `ajb_workspace`, or a linked worktree, gets an empty `portal/`.** Today it is populated by
   hand, or by the portal-specific provisioner (finding 6).
2. **The portal has its own branches and CI, and the parent records it by pointer bumps.**
   - The portal repo is `github.com/Opal-Capital/portal`, with `DEV`, `PROD` and worker branches `wk-*-portal`.
   - `.github/workflows/{ci,deploy,promote-to-prod}.yml`; `deploy.yml` runs on push to `PROD`: typecheck, build, deploy,
     tag.
   - The parent's gitlink moved **44 times since 2026-08-01**, in commits shaped like *"bump portal pointer -> <sha>;
     live PROD=<sha> (tag portal-vX.Y.Z) ... CI run <id> SUCCESS"* (`/prod-deploy` Step 6).
   - Portal commits are authored under agent serials. Since 2026-09-01, `2.0.0_SA_COO~F` 57, `0.9.0_WK_IRPT_FNTEND~1` 36,
     `2.0.0_SA_COO~D` 33, others below.

   **The lifecycle is sound and is the model to reuse.**
3. **The parent's git gates never run on a portal commit.**
   - `portal/.git/hooks/` holds only `*.sample` files (0 active hooks), and `portal`'s `core.hooksPath` is unset.
   - The parent's active hooks (`pre-commit`, `commit-msg`, `post-commit`, `pre-push`) live in the parent's `.git/hooks`
     and are not consulted by a commit in the nested repo.
   - So Rule 14's gate (py_compile + ds-precommit + ruff), the owned-paths lane check, the ASCII message rule and the
     surprise-row gate do not grade portal commits locally. The portal's only mechanical gate is its GitHub CI, and that
     does a typecheck.

   Harmless for a TypeScript frontend with CI. **For `opal_ai`, carrying the 16,185-line Python gateway, it would turn
   Rule 14 ("Universal") into a gate that does not see the product.**
4. **The lane grant for the nested repo is inert.**
   - `.owned-paths.yaml:2172` grants `"portal/**"` to `POD_DE_ANY`. But `owned-paths-check.sh:24-25` reads
     `$REPO_ROOT/.owned-paths.yaml`, where `REPO_ROOT` is `git rev-parse --show-toplevel`: the NESTED repo's root when
     committing inside it.
   - There it finds no file and does `WARN: ... skipping lane check` (`:137-138`). That is fail-open.
   - The parent's grant is graded only for the pointer file `portal` (`:2168`).
5. **From the parent, git sees a nested repo as a single pointer, so every git-based guard reads it as clean or
   empty.**
   - `git diff` or `git log -- portal/...` from the parent sees pointer moves, never file changes. (Banked on this box
     before as "a git census of a SUBMODULE path from the parent returns ZERO".)
   - `/integrate` measured on 2026-09-16 that *"a gitlink is where a merge reads clean and moves nothing real"*
     (`.claude/skills/integrate/SKILL.md:296-299`).
   - Today, resolving a gitlink conflict left the portal on a **detached HEAD** at `10141b6d` (0.0.0_AB_MSTR~Z's 20:47Z
     message; confirmed here: `HEAD detached at 10141b6d`). A seat committing into it lands on no branch.

### What already reaches into a nested repo, and what does not

6. **What reaches in:**
   - **Claude-session hooks**, which see a command's text whatever repo it targets (`never-rules-gate.sh` has 12 portal
     references, `comp-tool-hud.sh` 13). These are active only when the session was launched at the parent root.
   - **Scripts that locate their gates beside themselves.** `safe-merge.sh:47-50` was fixed on 2026-09-10 for exactly
     this: a portal drain resolved `$ROOT/.tools/` inside the nested repo and refused every drain. `safe-commit.sh`
     loads its gates from `SCRIPT_DIR` (`:245-247` and on) but does its git and lane work from `REPO_ROOT`.
   - **Worker provisioning**, hard-coded to one nested repo: `.tools/wk-provision.sh:77` `nested="$main/portal"`,
     driven by the dispatch skill's `--portal-ref` / `portal_ref:` convention (`dispatch/SKILL.md:198-203`).
   - **`proof-of-spec-check.py`** (16 portal references).
   - **Filesystem-walking search.** `comp-find` returned `portal/src/...` files in this session's censuses.
7. **What does not reach in:**
   - the parent's git hooks (finding 3);
   - the lane file (finding 4);
   - the commit-census tools: `activity-check.py`, `fabric-commits.py`, `daily-sprint.py` and `to-check.py` carry
     **0** references to the nested repo. That they therefore see only pointer bumps is INFERRED from finding 5, not
     exercised.

### The gateway's deploy path, which the move breaks

8. **Both deploy scripts locate the workspace by directory depth and read git from the parent.**
   - `deploy-to-ec2.sh:26-27`: `WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"`, then `SRC=` under it (`:61`)
     and `SHA="$(git -C "$WORKSPACE_ROOT" rev-parse --short HEAD)"` (`:62`).
   - `infra/aws/ec2/safe-ec2-deploy.sh` runs its clean-tree check as `git diff --quiet "$SOURCE_PATH"` from the parent
     (`:145`) and records `CURRENT_COMMIT=$(git -C "$WORKSPACE_ROOT" rev-parse HEAD)` (`:187`) into `EC2_MANIFEST.json`
     (`:207`).
   - The manifest entry today: `source_path: infra/aws/ec2/opal-gateway`, `deployed_commit: 1764e54a16...` (a
     parent-repo commit), `deployed_at: 2026-09-18T05:58:16Z`.

   **With the source inside a nested repo, the clean-tree check passes over uncommitted changes (finding 5), and the
   recorded commit names the wrong repository.** Neither failure would be visible; both would read as a normal deploy.

### Cross-repo dependencies to cut

9. **The gateway reaches into the parent in three places, each by fixed depth.** The rest of its imports are
   self-relative.
   - `app/integrations/schwab/catalog.py:183` reads `org/standards/NFRA_OPLGTW_CONTRACT.json` via `parents[7]`. It
     fails closed on a missing file, which is safe but stops the Schwab tools. An env override `NFRA_OPLGTW_CONTRACT_PATH`
     already exists.
   - `ops/schwab_entitlement_admin.py:49-50` and `ops/schwab_status.py:53-54` read the same contract via `parents[5]`.
   - `app/entity_resolution/` reads `data/_contracts/smartx_bd_join_disposition.yaml` (D3's contract) from a repo root
     it climbs to.
10. **The parent reaches into the gateway in four live places.**
    - `daily_reports/scripts/check_responsive_report.py:28` puts the gateway on `sys.path`: a runtime import.
    - `workflows/atom_decomposition/emit_catalog_v02.py` and `validate_catalog_v02.py` write and validate the gateway's
      `app/refs/DATA_CATALOG.yaml`. **That makes the catalog's writer a cross-repo writer**, which lands on MCPINDEX's
      open C1 question (who the catalog's one writer is).
    - `infra/logic/registry/systems.json:171` names the gateway's repo trees as the `opal` system's basis.

    Everything else is prose or history: 2,936 hits across 530 files in all, of which `org/missions` holds 233 and
    `org/mcp` 121. Those are historic records, and they stay resolvable at their pins.

### The Analyst seat

11. **Where the seat launches from decides which tooling it keeps, and the 09-22 ruling pointed the other way.**
    - The parent's `.claude/` carries 81 skills and the hook groups that make up the rail and the fence (PreToolUse 3,
      PostToolUse 2, SessionEnd 1). The BG fence `bg-concierge-gate.sh` is wired there.
    - 09-22's approved call 4 said to *"launch with cwd inside `opal_analyst/` so its skills and hooks load"*. Followed
      literally for `opal_ai`, the seat would launch without the parent's hooks, including its own fence, unless the
      product repo re-wires them. That cuts against today's *"still have the benefit of the ajb_workspace tooling"*
      (Part VIII call 2).
    - What Claude Code loads from PARENT directories of the launch directory is carried here as UNTESTED.
12. **The seat's runtime state does not belong in a product repo.**
    - Its folder holds `threads/` (5 thread dirs of staff conversations plus a per-person `INDEX.md`), `logs/` and
      `deliverables/`, alongside the product files (prompt, refs, tools).
    - `opal_ai` becomes a template and client artifact (RCN-0014), so conversation history moved there would ship with
      it.
    - Live consumers of the seat's paths: the launcher's F8 block (`.tools/ajb.ps1:262-276`), the fence and its test
      suite, `.tools/hooks/mstr-no-tier2-writes.sh`, the gateway's `identity_scope.py` / `server.py` / `tools.py`,
      `integrations/ticketing/intake/runner.py`, `emit_catalog_v02.py`, and the two Teams skills. The Bloomberg operator
      scripts under `integrations/bloomberg/` also name the serial; they stay with the operator duty.

### The mechanism, "or whatever"

13. **Four ways to be contained and separate, measured against his three requirements:**

    | mechanism | contained | separate | tooled | what it costs |
    |---|---|---|---|---|
    | **(A) real submodule** (`.gitmodules` entry + gitlink) | yes | yes | yes, once findings 3-10 are closed | a `git submodule update --init` in the checkout step; the gaps below |
    | **(B) nested clone + gitlink** (the portal today) | yes | yes | partial (findings 3-7) | a fresh checkout is empty; nothing maps the path to its remote |
    | **(C) `git subtree`** (the code merged into the parent's history) | yes | NO -- one history, separation by discipline | yes | two-way sync by hand; the standalone repo is a copy that drifts |
    | **(D) sibling repo outside the tree** | NO | yes | no | fails "contained in the monolith" |

    **(A) is the only row that meets all three**, and it is also what the 09-22 ruling approved for the portal and the
    factor scanner (call 5).

---

## PART V -- WHAT NEEDS TO HAPPEN

The spec he asked for. Grouped by what each item touches, with its owner class. Items are NOT sequenced beyond the
physical dependencies marked with ⊣; ordering is L5's.

**Repository and wiring**
1. **Create `Opal-Capital/opal_ai`**, private, beside `Opal-Capital/portal`. This is outward-facing: Andrew's word,
   `0.0.0_AB_MSTR~Z`'s act.
2. **Branch model.** `DEV` for integration and `PROD` for what is deployed, as the portal has. The shared-branch push law
   (only MSTR, on Andrew's word) and the never-rebase rule extend to both, and the Claude-level never-rules gate is taught
   the new repo.
3. **Move the code with its history, and delete it from the parent in the same change that adds the submodule** ⊣ 1.
   History is preserved by a path-filtered split of the parent's history; which tool does it is L5's call. The parent's
   old paths are removed and the gitlink added in ONE commit, so no moment has two live copies (the build-alongside
   veto). The old citations keep resolving because the parent's history is not rewritten.
4. **Write `.gitmodules` with three entries** -- `portal`, `models/factor_scanner`, `opal_ai` -- each with its URL and
   branch. `models/factor_scanner` is empty on this box: map it or remove its gitlink, on its owner's word (Part VIII
   call 6).
5. **Put `git submodule update --init` into every checkout path:** the startup protocol, `wk-provision.sh`, and the
   sparse-cone recipe used for worktrees. A checkout with an uninitialised submodule is refused loudly by whatever
   reads it.

**Gates**
6. **Make the parent's git gates run inside `opal_ai`.** An installer sets the submodule's hooks to a
   submodule-aware version of the parent's, so Rule 14, the ASCII message rule and the surprise-row gate grade commits
   made there. Same act for `portal`, whose commits skip them today (finding 3).
7. **Make the lane check find its lanes in a nested repo, and fail CLOSED if it cannot.** Either `opal_ai` carries its
   own `.owned-paths.yaml`, or the hook reads the parent's through `git rev-parse --show-superproject-working-tree` with
   the submodule prefix. The `WARN ... skipping` branch (`owned-paths-check.sh:137-138`) becomes a refusal for any repo
   that is a registered submodule.
8. **Exercise `safe-commit.sh` inside a nested repo once** and fix what it does not find there. Its gates load from
   `SCRIPT_DIR`, but its lane file and git state come from `REPO_ROOT`. `safe-merge.sh` already works (the 09-10 fix).
9. **CI in `opal_ai`**: py_compile, ruff at the py39 target, the gateway's test suite, and RCN-0014's firm-neutrality
   check on `template/`. Local hooks exist only on a device that ran the installer; CI is the gate that travels with the
   repo and with a client's copy. This is a NEW mechanical gate, so it needs his word (Part VIII call 4).

**Fabric tooling**
10. **Generalise `wk-provision.sh`** from `portal` to any submodule listed in `.gitmodules`, and the dispatch skill's
    `portal_ref:` to a per-submodule ref named in the issuance's `fanout:` data.
11. **A pointer-bump convention for `opal_ai`**, the analogue of `/prod-deploy` Step 6: who bumps it, when, and the
    message shape. The message names the `opal_ai` commit, the deployed commit, and the deploy record.
12. **Teach `/integrate` the `opal_ai` gitlink** as the member class it already names for portal. A gitlink merge is
    settled by `is-ancestor` inside the nested repo, and leaves the nested checkout on a branch, never detached (finding
    5).
13. **Teach the commit-census tools to iterate submodules** -- `activity-check`, `fabric-commits`, `daily-sprint`,
    `/outcome-check` -- so work inside `opal_ai` is counted (O10).
14. **Search and graph.** Verify `comp-find` covers `opal_ai` once initialised; move the gateway's tree paths in
    `infra/logic/registry/systems.json:171`, `org/modules/graph/nerves-risk-edges.json` and any graph builder input that
    names them.

**Deploy**
15. **`deploy-to-ec2.sh` finds the workspace by asking git, not by counting directories** ⊣ 3. That means the
    superproject's working tree, or an explicit env var. `SRC` points into the submodule, and `SHA` is the `opal_ai`
    commit.
16. **`safe-ec2-deploy.sh` runs its clean-tree check and its commit read INSIDE the source's own repository**
    (`git -C <source repo>`) ⊣ 3. `EC2_MANIFEST.json` records both the `opal_ai` commit deployed and the parent pointer it
    paired with, and `source_path` moves. Until this lands, a deploy from the new path is unsafe (finding 8).
17. **Terraform stays in the parent** (recommendation, Part VIII call 7). `infra/aws/terraform/opal-gateway/`, `safe-apply`
    and the CloudOps lanes are estate infrastructure under LGIC. The template carries a Terraform MODULE for other firms
    later; the Opal instance's root stays where the estate's IaC lives.

**Code seams**
18. **Replace the three fixed-depth reaches** (finding 9).
    - `NFRA_OPLGTW_CONTRACT.json` is the gateway's own enumeration authority. It moves with the gateway, or it is passed
      through the env override that already exists.
    - D3's join-disposition contract stays in the parent and is passed by path.
    - Either way, no `parents[N]` survives.
19. **Cut the four parent-to-gateway reaches** (finding 10).
    - The responsive-report check stops importing gateway code by path.
    - The catalog writer and its validator move into `opal_ai`'s `index/` beside the file they write. That settles the
      cross-repo half of MCPINDEX C1.

**The Analyst seat**
20. **Decide the launch root, then exercise the fence once** (Part VIII call 2). Recommended: on the terminal box the
    Opal seat launches at the parent root, keeping every parent skill and hook, and reads its product files from
    `opal_ai/opal/agent/` by path. `opal_ai` also carries its own `.claude/` for standalone, template and client use.
    Proof: one denied write from the relocated seat.
21. **Re-point every live consumer of the seat's paths** (finding 12). The launcher block, the fence's allowlist
    (whose writable paths MUST follow the runtime state, or the seat is locked out of its own memory), the MSTR
    tier-2 write hook, the gateway's identity scope, the ticketing intake runner and the catalog writer.
22. **Runtime state stays in the workspace** (Part VIII call 3). `threads/`, `logs/` and `deliverables/` are the Opal
    instance's data and never enter the product repo. The integrator sweep that commits them is unchanged.

**Records and in-flight work**
23. **Do not move code out from under open task orders.** NFRA_OPLGTW (2 pending) and NFRA_MCPINDEX (29 pending) name
    `infra/aws/ec2/opal-gateway/` in their `<paths>`. The move lands after their current rounds reach L10, and the COO
    re-cuts the paths of the orders still open. This restates RCN-0014's call 3 with its reason.
24. **Update the live law text that names the monolith's nested repos.** That is CLAUDE.md's Git section ("portal
    submodule `DEV`/`PROD`") and `org/XXX.md` Step 1a ("`portal/` is a work-site, never a base"), both of which apply
    to `opal_ai` too. Historic records are left as they are.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-09-23 ~22:0xZ-22:4xZ at SITEZ @`bd282e03e9`; origin/SITEZ read `1586a6dc0b` just before this seat's record
commit.

| thing | state | instrument |
|---|---|---|
| `.gitmodules` | 0 bytes | `wc -c` |
| gitlinks | `portal` @`10141b6d`, `models/factor_scanner` @`c59b266a` | `git ls-files -s` mode 160000 |
| submodule config / `.git/modules` | none / absent | `git config --get-regexp`, `ls` |
| `git submodule status` | fatal on `models/factor_scanner` | command output |
| `models/factor_scanner` on disk | empty directory (Jul 10) | `ls -la` |
| portal checkout | detached HEAD at `10141b6d`; `DEV` at `b3d5f59b` | `git -C portal branch` |
| portal active hooks | 0 (samples only); `core.hooksPath` unset | `ls portal/.git/hooks` |
| portal CI | `ci.yml`, `deploy.yml` (on push to PROD), `promote-to-prod.yml` | `git -C portal ls-files .github` |
| parent pointer bumps for portal | 44 since 2026-08-01 | `git log --since -- portal` |
| gateway deploy record | `deployed_commit 1764e54a16` (parent), `deployed_at 2026-09-18T05:58:16Z` | `EC2_MANIFEST.json` |
| references to the gateway path | 2,936 hits across 530 files (72,796 scanned) | `comp-find -i --all` |
| references to the seat's tokens | 12,277 hits (72,798 scanned) | `comp-find -i --all` |
| `opal_ai` repository | not present in this tree; GitHub UNREAD | `git ls-files`; no remote read |

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

1. **No GitHub read.** Whether `Opal-Capital/opal_ai` or `opal_analyst` already exists, and the portal's branch
   protection settings, are unread.
2. **What Claude Code loads from a PARENT directory of a session's launch directory** (settings, hooks, skills) was not
   exercised. Part V item 20 makes that exercise its first act. The 09-22 assessment carried the same fact the same way.
3. **The commit-census tools' blindness to nested commits is INFERRED** (finding 7), from their having no reference to a
   nested repo plus finding 5. No tool was run against a known portal commit to show it missing.
4. **`safe-commit.sh` was not run inside a nested repo.** Its behaviour there is read from source, not exercised.
5. **The history-preserving split was not tried.** The tool that performs it, and whether the moved paths' history
   carries across renames, are L5's to measure.
6. **Hit counts are line-hit censuses.** They certify the sweep, not that every hit is a live dependency. The live
   consumers named in findings 9, 10 and 12 were read at their lines; the rest were classed as historic by directory, and
   an unscoped read of those 530 files was not done file by file.
7. **Deploy-time behaviour was read from the scripts, not exercised.** Nothing was deployed.
8. **The portal's lifecycle is described from its skill text and git history**, not from a live promote observed this
   session.

---

## PART VIII -- CALLS THIS BRIEF SURFACES (NOT OUTCOME-BEARING; each with a recommendation)

| # | call | recommendation |
|---|---|---|
| 1 | **Mechanism:** a real submodule, or the portal's nested clone as it is today? | **A real submodule** (finding 13, row A), and map `portal` in the same act (already approved 09-22, call 5). The nested-clone form is what leaves fresh checkouts empty. |
| 2 | **Where does the Opal Analyst seat launch from?** 09-22 call 4 said inside the product repo so its skills load. Today's word asks to keep the workspace tooling. | **The parent root**, reading its product files by path, so it keeps the rail, the fence and all 81 skills. `opal_ai` still ships its own `.claude/` for standalone and client use. This re-opens a ruling you made, so it is yours. |
| 3 | **Where does the seat's runtime state live?** | **In the workspace**, never in `opal_ai`: staff conversations must not ride into a template or a client's copy. |
| 4 | **Gates for the new repo:** local hooks only, or local hooks plus CI? | **Both.** Hooks give the fabric its usual gates on this box; CI travels with the repo. CI is a new mechanical gate, so it needs your word. |
| 5 | **Branch model** | `DEV` and `PROD`, as the portal has, with the push law and never-rebase extended to them. |
| 6 | **`models/factor_scanner`** is an empty gitlink. | Ask its owner. Map it if it is live elsewhere; remove the gitlink if it is not. Either way, `.gitmodules` stops failing on it. |
| 7 | **Terraform location** | **Stays in the parent.** The template carries a Terraform module for other firms; Opal's root stays with the estate's IaC. |
| 8 | **Timing** | After NFRA_OPLGTW's current round reaches its L10, with the COO re-cutting the open orders' paths (Part V item 23). The deploy-path fixes (items 15-16) land in the same window as the move, never after it. |

---

## REFS

```
  BRIEF PATH        docs/briefs/opal-ai-gitops-split-brief-20260923.md
  ANDREW RECORD     org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260923_220xZ_OPAL_AI_GITOPS_SPLIT_SPEC.md @bd282e03e9
  COMPANION         docs/briefs/opal-ai-microproduct-repo-brief-20260923.md (RCN-0014) @a47993af9c
  PREDECESSOR       org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ASSESSMENT_OPAL_ANALYST_OPLGTW_MCPINDEX_TEMPLATING_20260922.md
                    (calls 4 and 5, approved)
  PROJECT           NONE-YET
  SIBLING PROJECTS  NFRA_OPLGTW, NFRA_MCPINDEX (open orders name the gateway path); the portal flow (/prod-deploy)
  PRIOR ART         the portal lifecycle: .claude/skills/prod-deploy/SKILL.md Step 6; portal/.github/workflows/*
                    nested-repo tooling: .tools/safe-merge.sh:47-50; .tools/wk-provision.sh; .claude/skills/dispatch/SKILL.md:198-203;
                              .claude/skills/integrate/SKILL.md:290-300
                    gates:    .tools/git-hooks/owned-paths-check.sh:24-25,137-138; .tools/safe-commit.sh:149,245-247;
                              .owned-paths.yaml:2168-2174
                    deploy:   infra/aws/ec2/opal-gateway/deploy-to-ec2.sh:26-27,61-62; infra/aws/ec2/safe-ec2-deploy.sh:23,145,187,207;
                              infra/aws/ec2/EC2_MANIFEST.json (opal-gateway)
                    seams:    app/integrations/schwab/catalog.py:86,175-183; ops/schwab_{entitlement_admin,status}.py;
                              app/entity_resolution/disposition_contract.py:27; daily_reports/scripts/check_responsive_report.py:28;
                              workflows/atom_decomposition/{emit,validate}_catalog_v02.py; infra/logic/registry/systems.json:171
                    seat:     .tools/ajb.ps1:262-276; .tools/hooks/bg-concierge-gate.sh; .claude/settings.json (hook groups)
  MEASURED AT       2026-09-23 ~22:0xZ-22:4xZ, SITEZ @bd282e03e9, local repo and git reads only
```
