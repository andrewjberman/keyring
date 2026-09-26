# NFRA_OPALAI -- DECOMPOSITION (L5) -- ROUND 1, THE THREAD

```json
{
 "project": "NFRA_OPALAI",
 "directive": "D6",
 "macro": "NFRA",
 "fabric": "site-z",
 "decomp_version": "v1",
 "step": 5,
 "prd_ref": "org/missions/D6/NFRA/NFRA_OPALAI/prd/NFRA_OPALAI_PRD.md@f06341327e",
 "prd_half_hashes": {"ratified-text": "SIGNED 3.0.0_SA_CVO~O 12e470e5882a @de941578b7 (and 3.0.0_SA_CVO~Z @85354d424c)", "brief": "SIGNED (auto) CRO-authored brief"},
 "author": "2.0.0_SA_COO~O",
 "round": 1,
 "rectangle": "the FWD-1 thread's hops (PRD v0.3 Canonical handoff steps 1-6) plus the repo wiring the handoff admits beside it (S2, S3, S4)",
 "cells": 10,
 "root_cells": 1,
 "chains_after_root": 7,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~O` (L5 is the COO's). **Input:** PRD v0.4 @`f06341327e` (ADMITTED by `prd-signoff.py status`: the
ratified-text half SIGNED at the current ENDPOINT hash, and the brief half admitted because the CRO wrote the brief). This
file also reads v0.2's C10 (Andrew-direct, record @`6426ebff2b`), v0.3's C3/C4 pull ruling (CTO msg 25759) and v0.4's C11
(the cutover drops nothing silently; CTO msg 25770: fold into OA-t-1 or the cutover window).
**Frozen at the cut.** A cell that looks wrong mid-round is a surprise row, never an edit.

**Rulings reaching every cell:**
- The runtime account and agent are named `Opal_Agent` (C4). No product file names a fabric serial for the runtime agent.
- Existing work is CARRIED and synthesized, never rebuilt (C10, Andrew-direct). Every cell's first act locates the
  implementation it extends.
- Code MOVES and is never copied (C1). Each cell that moves a file removes the parent copy on its own branch. **The
  parent-side removals merge in ONE cutover window at the round's close, never at chain end** (C1: "nothing in between
  serves colleagues from both"). This is the one departure from merge-per-chain-end, and it is stated here for the L10
  read.
- The pull runs as the operator account; `Opal_Agent` holds no GitHub credential; the operator passes it no credential,
  token or environment (C3/C4 v0.3).
- No AWS credential, no broker, no workspace path in any runtime file (C4, C5). Paths are launcher configuration.
- No push, no promote, no vendor call by any worker. Every DEV/PROD push of `opal_ai` is G-PUSH.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

The rectangle is the PRD's Canonical handoff (v0.4, section "Canonical handoff"), verbatim in its order:

```
  1. the agent's product files in opal_ai/opal/agent/ (S5)
  2. the runtime account and read-only checkout (S6, G-ACCT, G-GH)
  3. the runtime Claude setup and launch gate (S7, G-AUTH)
  4. a Teams watch that sees (S8, the minimum for one exchange)
  5. the asker's entitlement on the path (S10 round-1 half, C10)
  6. one live exchange graded against A1, plus one un-admitted asker refused
  + "The repo wiring (S2, S3, S4) is a disjoint write surface and can run beside the thread in round 1."
```

```
  handoff steps ...................................................................... 6
  minus step 6 (the live exchange): the COO's ONE REAL RUN at close, not a cell ....... -1
  plus S1 (repo layout), which step 1 presumes and S5 depends on (manifest row S5) ... folded into OA-t-1
  plus the precondition every opal_ai cell shares: the submodule exists in the
       parent and a worker slot can be provisioned with a nested opal_ai worktree ...... +1  (OA-w-1, the ROOT)
  plus step 5's deploy: C10 is live only when the gateway runs it ...................... +1  (OA-t-6)
  plus S2 (the rest), S3, S4 beside the thread ......................................... +3  (OA-w-2, OA-w-3, OA-w-4)
  -----------------------------------------------------------------------------------------
  CELLS IN ROUND 1 .......................................................................... 10
```

Step 4 (S8) and step 3 (S7) each split by WRITE SET, not by hop: the fence hook and the Teams watch are moved AND
adapted by the cell whose hop needs the adaptation (OA-t-3 the fence, OA-t-4 the watch), so OA-t-1 moves every other
product file and no file has two writers.

**The unscoped control.** Read from the SURFACE MANIFEST instead of the handoff (14 rows): S1 -> OA-t-1; C11 -> OA-t-1 (the map) + the cutover record; S15 -> outside round 1 (the first enrichment, v0.4); S2 -> OA-w-1 +
OA-w-4; S3 -> OA-w-2; S4 -> OA-w-3; S5 -> OA-t-1 + OA-t-3 (fence) + OA-t-4 (watch); S6 -> OA-t-2; S7 -> OA-t-3; S8 ->
OA-t-4 (minimum only); S10 -> OA-t-5 + OA-t-6 (round-1 half only). **Outside round 1, by the handoff's own words:** S9
(speed), S10's other half (admit, narrow, remove, explain), S13 (release flow), S11 and S12 (G-MOVE), and S14
(NFRA_MCPINDEX). Read from the acceptance matrix: A1 is this round's close run; A7 is partly served (the gate's
checks are built and shown refusing on the wrong account); A10, A13 and A14 are partly served by the wiring cells; the
rest are enrichment. No manifest row falls outside both lists.

**Status vocabulary:** `MEASURED` (evidence in hand at the cut, instrument named), `DECLARED` (the PRD or a ruling
asserts it; not independently measured here), `NOT-EVALUATED`, or `N/A`.

---

## 2. THE RECTANGLE -- 10 cells x 6 fields

Measured on site Z at CLOUD `1645cbb7ab`, 2026-09-24 ~21:1xZ, unless stated.

| cell | hop / surface | what is built | current state | existing work carried | risk |
|---|---|---|---|---|---|
| `OA-w-1` | ROOT: S2 minimum | `.gitmodules` maps `portal` (`https://github.com/Opal-Capital/portal.git`) and `opal_ai` (`https://github.com/Opal-Capital/opal_ai.git`, branch `DEV`); the gitlink `opal_ai` at `90ca424fc7`; `.tools/wk-provision.sh` gains `--nested <path>=<ref>` for ANY mapped submodule (portal's behaviour unchanged, `node_modules` only for portal) and refuses loudly on an uninitialised submodule in the main tree | `MEASURED`: `.gitmodules` 0 bytes; gitlinks `portal` @`46c0ae112c` and `models/factor_scanner` @`c59b266adf`; `git ls-remote` opal_ai HEAD = DEV = PROD = `90ca424fc7`; `wk-provision.sh` hard-codes `portal` at `:77`, `:81`, `:100`, `:217-218` | `wk-provision.sh cmd_portal` (`:46-160`), its self-test arms (`:259-`) | LOCAL |
| `OA-t-1` | hop 1: S1 + S5 | in `opal_ai`: the slice-first layout (`README.md`, `opal/README.md`, `template/README.md`, `clients/README.md`, `docs/README.md`) and `opal/agent/` receiving `prompt.md`, `refs/**`, `tools/portal_lookup.py`, `skills/bbg-teams-assist/SKILL.md`; the parent copies removed on the same branch. `prompt.md`'s On-launch section is rewritten for the runtime (no `register_agent`, no `/watcher`, no Secrets Manager read; the whoami identity gate KEPT); `PORTAL_RETRIEVAL.md` names the gateway tool `opal_asker_query` as the runtime data mechanism; `prompt.md` gains a RUNTIME MECHANISM MAP: each APPROVED catalog row (8) mapped to a mechanism `Opal_Agent` can reach (`opal_asker_query` where `DATA_CATALOG.yaml` holds a key for it) or to C11's plain, quotable "not available from the Analyst yet" reason naming who to ask (row 7, Bloomberg view, is the known case). Every hard line and every catalog row is byte-unchanged (C7); `REQUEST_CATALOG.md` is NOT edited | `MEASURED`: seat folder `org/tier0_utility/0.0.3_BG_BBGTerminal/` = 86 tracked files: `prompt.md` 148 lines, `refs/` 11, `tools/` 1 (`portal_lookup.py` 389 lines, boto3 + the box's AWS profile), `threads/` 23, `logs/` 39, `deliverables/` 9; `.claude/skills/bbg-teams-assist/SKILL.md` 150 lines | the files themselves, moved | WORLD (floor: it re-points 11 lines of the gateway's `DATA_CATALOG.yaml`, an infrastructure path) |
| `OA-t-2` | hop 2: S6 | `opal_ai/opal/runtime/provision/provision-account.ps1` (idempotent: creates `Opal_Agent` as a standard local user, asserts it is in neither `Administrators` nor `CodexSandboxUsers`, creates the checkout and state directories named by a config file, ACLs the checkout read+execute for `Opal_Agent` and the state dir modify, stores the generated password DPAPI-protected in the OPERATOR profile, outside every repo) and `verify-boundary.ps1` (runs a read of one named workspace file AS `Opal_Agent` and requires Access Denied, plus a positive read of the state dir); the script REFUSES without elevation and changes nothing | `MEASURED`: this session is Medium integrity (`whoami /groups`), not elevated; `Opal_Agent` absent (`Get-LocalUser`); workspace ACL per PRD ground truth | the design's ACL facts (`OPAL_AI_RUNTIME_ISOLATION_DESIGN_20260924.md` s.3 @`45ce8406fc`) | LOCAL (the build); the elevated run is gate G-ACCT at close |
| `OA-t-3` | hop 3: S7 + the fence | `opal_ai/opal/runtime/`: `CLAUDE.md` (imports `../agent/prompt.md`; names the agent `Opal_Agent`), `.claude/settings.json` (registers the fence), `mcp.json.example` (lists `opal-gateway-bbg` only; never `opal-gateway`), `launcher.ps1` (operator side: fetch PROD `--ff-only` with the G-GH credential; then start the gate + agent AS `Opal_Agent` passing no operator credential, token or environment), `launch-gate.ps1` (as `Opal_Agent`: (a) the workspace probe read must be DENIED, (b) the checkout clean at the PROD commit just fetched, (c) the account in neither admin group; any failure refuses); `opal_ai/opal/agent/hooks/concierge-gate.sh` = `.tools/hooks/bg-concierge-gate.sh` MOVED and adapted so it binds unconditionally in the runtime and its write allowlist is the configured state dir; G2-G4 unchanged in content | `MEASURED`: the fence fires only for serial `0.0.3_BG_BBGTerminal` (`bg-concierge-gate.sh:11-14`, `:87-91`) and allowlists workspace paths (`:23-24`) -- inert in a runtime that has neither | `bg-concierge-gate.sh` G1-G4 (219 lines); the design's launch-gate text (C4) | LOCAL |
| `OA-t-4` | hop 4: S8 minimum | `.claude/skills/teams-assist/teams-watch.py` MOVED to `opal_ai/opal/agent/teams_watch/teams-watch.py` and changed so (1) it holds its OWN gateway OAuth refresh family (registered through the gateway's dynamic client registration; the refresh and cursor files live in a configured state dir) and never reads `~/.claude/.credentials.json`; (2) the read failure is diagnosed and fixed; the operator's `/teams-assist` `SKILL.md` re-pointed to the new path | `MEASURED` by the Analyst's log @`0646a96553` (`logs/2026-09-24/teams_watch_two_blockers_and_a_dark_owner_1145-1315Z.md:18-59`): blocker 1, the watch reads Claude Code's 15-minute token and never refreshes (`teams-watch.py:36-38`); blocker 2, 33 of 33 reads failed with a LIVE token, cause a HYPOTHESIS (an MCP-audience token presented to Graph), untested | `oauth_as.py`: `GRANT_TYPES` incl. `refresh_token` (`:99`), DCR (`:558-579`), refresh families with reuse revocation (`:835-876`); `teams-watch.py` cursor discipline (`:26-34`) | LOCAL |
| `OA-t-5` | hop 5: S10 round-1 half (C10) | NEW `infra/aws/ec2/opal-gateway/app/asker_scope.py` + the MCP tool `opal_asker_query(chat_id, message_id, key, params)`: the gateway reads the Teams message ITSELF, takes the sender's Entra `tid`+`oid`, loads `POLICY#<tid>#<oid>` through the existing store, refuses an asker with no profile with a plain how-to-get-access line, intersects the asker's grant with the calling identity's allowlist (`identity_scope.py`), and serves through query_v0's catalog-gated fetch within that scope; any identity field the agent passes is ignored; the audit row names the asker oid, key and verdict and carries no values | `MEASURED`: `/query/v0` is a bearer REST route (`server.py:558-582`), not an MCP tool; the policy model keys on `tid`/`oid` (`data_entitlement.py:1-45`); no tool reads a Teams message's sender for authorization | `data_entitlement.py`, `access_state.py`, `identity_scope.py`, `tier.py`, `query_v0.py`, the `_run` chokepoint in `tools.py` | WORLD (floor: gateway code under `infra/`; the build itself deploys nothing) |
| `OA-t-6` | hop 5, live | deploy the merged gateway (OA-t-5 at CLOUD HEAD) to the EC2 host through `safe-ec2-deploy.sh`, with the NEVER-2 entry opened first, the census of EVERY gateway change since the deployed manifest's commit named in it, the rollback named, and three post-act reads: health, `opal_asker_query` listed, and one un-profiled asker refused LIVE | `NOT-EVALUATED`: the deployed manifest's commit; NFRA_MCPINDEX's row states the live gateway "has no valid rollback" | `deploy-to-ec2.sh`, `safe-ec2-deploy.sh`, `EC2_MANIFEST.json` | WORLD |
| `OA-w-2` | S3 | a commit made inside a nested repo is graded by the PARENT's gates: `.tools/git-hooks/owned-paths-check.sh` resolves the superproject's `.owned-paths.yaml` and validator when run in a nested repo (today `REPO_ROOT/.owned-paths.yaml`, `:25-26`, fails closed at `:133-142`); lane rows for `opal_ai/**` land in `.owned-paths.yaml` BEFORE any hook; `install-owned-paths.sh` can install into a named submodule's hooks dir; `safe-commit.sh` works from inside a nested repo (`REPO_ROOT` from `--show-toplevel`, `:149`). Proven on a SCRATCH superproject fixture only: the real install into `opal_ai`'s hooks dir is the COO's act at the round's last merge, because a hook in the shared nested common dir would grade every other worker's nested commits mid-round | `MEASURED` at the lines cited | `owned-paths-check.sh`, `owned-paths-validate.py`, `safe-commit.sh` | LOCAL |
| `OA-w-3` | S4 | `opal_ai/.github/workflows/ci.yml` (on every push: `bash opal/checks/run_checks.sh`) and `opal_ai/opal/checks/run_checks.sh` (py_compile over `opal/`, `ruff check --target-version py39`, the ASCII rule on product code, a no-device-path rule, and any `pytest` under `opal/`), runnable from a standalone clone with no workspace | `MEASURED`: opal_ai holds a README only; `ruff` at `...Python311/Scripts/ruff.exe` | Rule 14's three checks, restated as the product's own | LOCAL |
| `OA-w-4` | S2 census | `.tools/fabric-commits.py` (`--json` gains `by_repo`) and `.tools/activity-check.py` (header gains `repos: ...`) count commits in the parent AND inside every mapped submodule; an uninitialised mapped submodule reads `UNINITIALISED`, never 0 | `MEASURED`: neither iterates any submodule today -- both run one `git log` in the parent (`fabric-commits.py:54`, `activity-check.py:107-108`), so portal's commits are not counted either | the two tools | LOCAL |

**Load-bearing `DECLARED` / `NOT-EVALUATED` rows, stated:** (a) that a Graph `chatMessage` read by the gateway carries
the sender's `oid` and `tenantId` is DECLARED by the Graph schema, not measured here; OA-t-5 measures it. (b) How a
query_v0 catalog key maps onto the policy scope's dimensions (`datasets`, `operations`) is NOT-EVALUATED; OA-t-5
measures it and refuses rather than invents a dimension. (c) The 33-of-33 read failure's cause is a hypothesis; OA-t-4
measures it. (d) The deployed gateway commit is NOT-EVALUATED; OA-t-6 reads it before acting.

---

## 3. THE CELLS -- 10 (round 1)

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1: prefix `OA`, axis `t` = thread hop, `w` = repo wiring.
Paths are parent-relative; a path under `opal_ai/` is a file of the nested repository.

| cell | serves | writes | reads (never writes) |
|---|---|---|---|
| `OA-w-1` | FWD-10 | `.gitmodules`, `opal_ai` (gitlink), `.tools/wk-provision.sh` | `portal` gitlink, `.tools/wk-provision.sh` self-test |
| `OA-t-1` | FWD-1, FWD-6 | `opal_ai/README.md`, `opal_ai/opal/README.md`, `opal_ai/template/README.md`, `opal_ai/clients/README.md`, `opal_ai/docs/README.md`, `opal_ai/opal/agent/prompt.md`, `opal_ai/opal/agent/refs/**`, `opal_ai/opal/agent/tools/portal_lookup.py`, `opal_ai/opal/agent/skills/bbg-teams-assist/SKILL.md`; parent removals: `org/tier0_utility/0.0.3_BG_BBGTerminal/prompt.md`, `.../refs/**`, `.../tools/portal_lookup.py`, `.claude/skills/bbg-teams-assist/SKILL.md` | the seat's `README.md`, `threads/`, `logs/`, `deliverables/` (all STAY: state, C5) |
| `OA-t-2` | FWD-1, FWD-7 | `opal_ai/opal/runtime/provision/provision-account.ps1`, `opal_ai/opal/runtime/provision/verify-boundary.ps1`, `opal_ai/opal/runtime/provision/runtime.config.example.json` | the design doc s.3 |
| `OA-t-3` | FWD-1, FWD-7 | `opal_ai/opal/runtime/CLAUDE.md`, `opal_ai/opal/runtime/.claude/settings.json`, `opal_ai/opal/runtime/mcp.json.example`, `opal_ai/opal/runtime/launcher.ps1`, `opal_ai/opal/runtime/launch-gate.ps1`, `opal_ai/opal/agent/hooks/concierge-gate.sh`, `opal_ai/opal/agent/hooks/test_concierge_gate.sh`; parent removals: `.tools/hooks/bg-concierge-gate.sh`, `.tools/hooks/tests/test_bg_concierge_gate.sh` | `opal_ai/opal/runtime/provision/runtime.config.example.json` (OA-t-2's key names, fixed below) |
| `OA-t-4` | FWD-1, FWD-2 | `opal_ai/opal/agent/teams_watch/teams-watch.py`, `opal_ai/opal/agent/teams_watch/test_teams_watch_lineage.py`, `.claude/skills/teams-assist/SKILL.md` (re-point); parent removal: `.claude/skills/teams-assist/teams-watch.py` | `infra/aws/ec2/opal-gateway/app/oauth_as.py`, the Analyst log @`0646a96553` |
| `OA-t-5` | FWD-1 (C10) | `infra/aws/ec2/opal-gateway/app/asker_scope.py` (new), `infra/aws/ec2/opal-gateway/tests/test_asker_scope.py` (new), `infra/aws/ec2/opal-gateway/app/tools.py` (the tool's registration), `infra/aws/ec2/opal-gateway/app/data_entitlement.py` (the new tool's classification line only) | `access_state.py`, `identity_scope.py`, `tier.py`, `query_v0.py`, `graph_read.py`, `graph.py`, `token_broker.py`, `refs/DATA_CATALOG.yaml` |
| `OA-t-6` | FWD-1 (live) | `org/critical_paths/change_management/<entry>.md`, `org/critical_paths/.open_deploys/<slug>.json`, `infra/aws/ec2/EC2_MANIFEST.json` (written and committed by `safe-ec2-deploy.sh`), the S3 artifact and the deployed host (WORLD) | `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, `.tools/safe-ec2-deploy.sh`, `EC2_MANIFEST.json` |
| `OA-w-2` | FWD-9, FWD-10 (A14) | `.tools/git-hooks/owned-paths-check.sh`, `.tools/git-hooks/install-owned-paths.sh`, `.tools/safe-commit.sh`, `.owned-paths.yaml` (the `opal_ai/**` lane rows), `.tools/tests/test_nested_repo_gates.sh` (new) | `.tools/owned-paths-validate.py` |
| `OA-w-3` | FWD-13 | `opal_ai/.github/workflows/ci.yml`, `opal_ai/opal/checks/run_checks.sh` | Rule 14's `commit-gate.sh` |
| `OA-w-4` | FWD-10 | `.tools/fabric-commits.py`, `.tools/activity-check.py` | `.gitmodules` |

**Fixed names across cells, so no cell waits on another's text:** the tool `opal_asker_query`; the config keys
`checkout_dir`, `state_dir`, `workspace_probe_file`, `prod_ref` in `runtime.config.example.json`; the agent directory
`opal_ai/opal/agent/`; the runtime directory `opal_ai/opal/runtime/`; the fence at `opal/agent/hooks/concierge-gate.sh`;
the watch at `opal/agent/teams_watch/teams-watch.py`. **Every surface of the rectangle has a cell, and no file has two
writers.** The only shared files are hookups: `.claude/settings.json`'s fence registration line (removed) and the
`ajb.ps1` BG launch line. These belong to NO cell; the COO changes them in the cutover commit.

---

## 4. PLACEMENT AXIS

**Every cell executes on SITE Z**, the box the runtime lives on. Each cell is served by `0.9.0_WK_NFRA_OPALAI~<n>` in a
worktree off HEAD (`.tools/wk-provision.sh provision NFRA_OPALAI <n> --path <abs>`). A cell writing `opal_ai/` gets a
nested `opal_ai` worktree through OA-w-1's `--nested opal_ai=<ref>`, where `<ref>` is the main tree's `opal_ai` HEAD at
the spawn. So every `opal_ai` cell spawns after OA-w-1 is merged and the COO has run `git submodule update --init
opal_ai` in the main tree (the root's hookup). OA-t-5 and OA-t-6 touch no nested repo and spawn at the cut.

---

## 5. DEPENDENCY EDGES AND CHAINS

```
  ROOT   OA-w-1  -->  every cell that writes opal_ai/ or needs a mapped submodule
                      (OA-t-1, OA-t-2, OA-t-3, OA-t-4, OA-w-2, OA-w-3, OA-w-4)
  chain A   OA-w-1 --> OA-t-1                 the product files (the root's own slot continues here)
  chain B   OA-t-2 --> OA-t-3                 OA-t-3's launcher reads OA-t-2's config keys and provision paths
  chain C   OA-t-4                            the watch
  chain D   OA-t-5 --> OA-t-6                 build, then the WORLD deploy of the merged build
  chain E   OA-w-2                            nested gates (scratch fixture only)
  chain F   OA-w-3                            CI
  chain G   OA-w-4                            census tools
```

**CHAINS: M = 7 after the root** (A..G pairwise disjoint in write set). Read strictly as connected components, the root
joins six of them into one component. That reading would serialise six disjoint chains behind a cell every one of
them already waits for, so this cut counts components WITHOUT the root and states the root separately. This is the
DSGN_IRPTV1 v2 join-cell precedent, applied at the head of the graph instead of the tail.

**Fan-out:** `N = 7 of M = 7 chains, cap 8; root_cells: 1 (OA-w-1)`. At the cut, spawn slot `~1` (OA-w-1, then OA-t-1)
and slot `~2` (OA-t-5, then OA-t-6). When OA-w-1 drains, spawn `~3` (OA-t-2, then OA-t-3), `~4` (OA-t-4), `~5`
(OA-w-2), `~6` (OA-w-3) and `~7` (OA-w-4).

---

## 6. BATTERY DISPOSITION (a thread round)

- **`comp-adversary` -- DECLARED-NOT-APPLICABLE:** thread round; the lens runs on the enrichment round that touches its
  surface.
- **`comp-schedule` -- DECLARED-NOT-APPLICABLE:** thread round. No cell arms a cron, alarm, monitor or cadence.
  The Teams watch is the product's existing detector, moved and repaired, not a new monitor.
- **`comp-iam` -- DECLARED-NOT-APPLICABLE, with the reason measured:** no cell writes an AWS IAM surface. OA-t-5's new
  tool reads S3 and DynamoDB through the gateway host's EXISTING role, on the same prefixes query_v0 and the policy
  store already read. OA-t-6 moves code, not a role. The Windows ACLs of OA-t-2 are an OS boundary, not IAM. Bound: if
  OA-t-5 needs an action or resource the host role does not hold, that is a BLOCKING row at the cell, never a grant here.

---

## 7. RULE 24 FOUR-POSTULATE RECORD

**(i) MECE over a declared domain.** Section 1: six handoff steps, minus the close run, plus the root, the deploy and
three wiring surfaces, gives ten cells. This is falsified against the 14-row manifest and the 14-row acceptance
matrix: every row is either inside a cell or named outside round 1 by the handoff's own words. Write sets are
exclusive (section 3). The two surfaces that span cells (S5 across t-1/t-3/t-4, S10 across t-5/t-6) are split by FILE,
never shared.

**(ii) SAME GRAIN.** Every cell is one hop adapter or one wiring surface, and each is graded by (a) its built
behaviour, (b) a seam probe against its real neighbour where reachable (the GitHub remote, the live gateway's OAuth
metadata, the live policy store, the current account as the wrong-account control), and (c) at most one further check.

**(iii) INTENT COHERENCE.** One axis: the FWD-1 journey from a colleague's Teams message to a scoped answer from the
released copy, plus the repo wiring that lets engineering seats build it. Out of scope: speed, the admit/narrow/remove
tooling, the release flow, the gateway move, the index, hosted content, and the Bloomberg view server's placement.

**(iv) STATE COHERENCE -- what each remedy does NOT move.**
- `OA-w-1` maps and provisions. It does NOT move the portal gitlink, portal's provisioning behaviour or `models/factor_scanner`.
- `OA-t-1` moves files. It does NOT change a hard line, a catalog row, the bucket allowlist or the identity gate. It
  does NOT move the seat's thread memory, logs or deliverables.
- `OA-t-2` builds scripts. It does NOT create the account (G-ACCT), and it does NOT change the workspace's own ACL.
- `OA-t-3` builds the launcher and gate and adapts the fence's scope and allowlist. It does NOT change G2-G4's
  denials, and it does NOT start the agent.
- `OA-t-4` changes where the watch gets its token and fixes its read. It does NOT change the cursor discipline, the
  emit format or the identity pin.
- `OA-t-5` adds one tool. It does NOT change any existing tool's gate, the legacy path for unprofiled users of
  EXISTING tools, query_v0's REST route, or any policy record.
- `OA-t-6` ships the merged gateway. It does NOT change Terraform, the host, its role or its secrets.
- `OA-w-2` extends the gates to a nested repo. It does NOT change a parent lane's verdict (its bound check).
- `OA-w-3` adds CI. It does NOT push; the first real CI run is on G-PUSH.
- `OA-w-4` counts. It does NOT change the parent repo's own count (its bound check); portal's commits become counted,
  which they are not today (measured, section 2).

---

## 8. GATES, THE CUTOVER, AND THE CLOSE RUN

**Gates the close run needs, each an act a named holder takes on demand:**
- **G-ACCT:** one ELEVATED run of `provision-account.ps1` on this box. Holder: Andrew, or a seat he names, in an
  elevated shell. This departs from the PRD's "a worker under this project": the session is Medium integrity and
  `New-LocalUser` requires elevation (row `NFRA_OPALAI-Z-S1`).
- **G-GH:** mint the read-only, `opal_ai`-scoped GitHub credential into the operator profile. Holder: `0.0.0_AB_MSTR~Z`.
- **G-PUSH:** push `opal_ai` DEV and merge DEV into PROD. Holder: `0.0.0_AB_MSTR~Z`, on Andrew's word.
- **G-AUTH:** as `Opal_Agent`, the first Claude Code login, the `opal-gateway-bbg` OAuth, and the watch's own OAuth
  family, with MFA to Andrew's phone. Holder: Andrew.
- **G-ASKER:** Andrew names the colleague for A1 and the scope they may see; their profile and grant are written
  through the EXISTING operator path. Holder: Andrew (the admit tooling itself is enrichment).
- **OA-t-6's deploy** is a WORLD act inside the round: it adds the CTO's exercised read.

**The cutover window (C1).** One sequence, at the round's last merge:
1. merge the `opal_ai`-side branches into `opal_ai` DEV locally;
2. G-PUSH;
3. merge the parent-side removals, bump the gitlink, and make the hookups (the settings.json fence line and the
   ajb.ps1 BG launch line) in ONE parent commit;
4. launcher run -> gate -> agent live as `Opal_Agent`;
5. the workspace seat's Teams duty stops in the same window;
6. the cutover record lists every APPROVED catalog row answered with C11's decline (from OA-t-1's map) and the enrichment
   that restores each.

**The close run (step 6, A1):** one live exchange traced hop by hop with the named colleague, plus one un-admitted asker
refused. The artifact goes to `deliverables/2.0.0_SA_COO~O/round1/`. The drain also runs the thread's hygiene once per
merge: py_compile, ruff py39, and the gateway suite.

---

## 9. WHAT THIS DECOMPOSITION DOES NOT CLAIM

1. No cell has been exercised; every target state is a specification.
2. The Graph sender fields, the catalog-to-scope mapping, the read failure's cause and the deployed gateway commit are
   measured by their cells, not here (section 2).
3. The Bloomberg view server's reachability from `Opal_Agent` is untested and outside round 1 (S15, the first
   enrichment); FWD-1 is a portal figure, and row 7 is declined plainly under C11 until S15 lands.
4. `/integrate`'s nested-repo clause, the sparse-cone recipe, the startup protocol's submodule init (G-LAW) and
   `models/factor_scanner`'s mapping are NOT in this round.
5. NFRA_MCPINDEX's pending orders that name gateway paths are not re-cut here; OA-t-5 writes a new module plus two
   registration lines, disjoint from NFRA_MCPINDEX's `tools-portal` order's `app/integrations/portal_index/`. Its COO owns that round.

---

## ADDENDUM A1 -- Z-S18's server-side fix, pulled forward on Andrew's word (option 2, record @bda25438c8; CTO msg 25935)

Two direct-act cells, ahead of round 2. They are not thread cells, and each declares `<direct_act>true</direct_act>`.

| Cell | Builds | Risk |
|---|---|---|
| `OA-f-1` | `app/identity_scope.py` keys a scoped row on (identity, OAuth client_id): the overlay grammar gains an optional `client=<id>`, and a qualified row admits ONLY that client. `opal_data_refresh_upload` goes to the operator's registered client only. The verified token's client_id is threaded to `check()` at both chokepoints (`tools._run`, `integrations.base.run_integration_tool`). `tests/test_identity_scope.py::test_scoped_deny_by_default` reads a fixture overlay, never the live file | WORLD (infra floor) |
| `OA-f-2` | the NARROW gateway release of OA-f-1: cut at the deployed commit read at its own cut, plus OA-f-1's commits only; announced through `0.0.0_AB_MSTR~Z` before the act (CTO ruling @75117e60d6); rollback pre-acked (row NFRA_MCPORTAL-Z-S8) | WORLD |

Chain: `OA-f-1 --> OA-f-2`. OA-f-2 waits for any earlier-announced gateway deploy (the laptop CTO's Teams fixes) to close.
**What this does NOT close today:** the Analyst seat and any operator session on this box share ONE OS account, so ONE
client. TODAY's reach closes at the cutover, when Opal_Agent's own sign-in registers a different client, or with a
fence change. Andrew's answer on who runs the daily upload picks the interim (CTO msg 25935).

---

## ADDENDUM A2 -- a portal-only asker grant, so Alyssa Keith can be admitted to portal figures only (Andrew's call 2; CTO ruling (B), msg 25996; row Z-S23)

Three direct-act cells, ahead of round 2. The CTO's direction (build ladder, rung 2):
- extend the EXISTING grant grammar, so a grant may carry zero Schwab masters and a portal-channel scope that
  opal_asker_query honours;
- build no second grant store; the NFRA_OPLGTW contract may be amended, because its stop is lifted;
- resolve Alyssa's Entra oid from the directory by the operator path, without waiting for her to sign in.

| Cell | Builds | Risk |
|---|---|---|
| `OA-g-1` | `app/data_entitlement.py` gains the scope dimension `portal_channels` (channel ids of `app/refs/DATA_CATALOG.yaml`). `masters`, `accounts`, `datasets` and `columns` may be EMPTY only when `portal_channels` is non-empty, and existing records parse unchanged. `app/asker_scope.py` serves a catalog key only if its channel is granted. `ops/schwab_entitlement_admin.py` validates portal-only candidates against the amended contract `org/standards/NFRA_OPLGTW_CONTRACT.json` | WORLD (infra floor) |
| `OA-g-2` | the NARROW gateway release of OA-g-1, cut at the live commit read at its own cut, announced through `0.0.0_AB_MSTR~Z` | WORLD |
| `OA-g-3` | Alyssa Keith's oid is resolved from the directory, and her grant is written through the operator command: `portal_channels` = the catalog's portal channels, `operations` = [query], zero Schwab masters | WORLD |

Chain: `OA-g-1 --> OA-g-2 --> OA-g-3`. OA-g-2 follows OA-f-2 (one gateway deployer at a time). OA-g-3 is written
after OA-g-2, because the live gateway's current parser would read a zero-master grant as Malformed and deny her.
