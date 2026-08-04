# Root Cleanup (Andrew-direct) + Programme Close Verification — 4.0.0_SA_CRO

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, IMPLEMENT, COORDINATE

**Date:** 2026-08-04
**Task Order:** ad-hoc Andrew-direct root-directory audit + cleanup; RCG close-verification residuals
**Status:** COMPLETE

---

## Objective

(1) Land the residuals of CTO~B's independent programme-close verification. (2) Andrew-direct:
audit every floating file and directory at the workspace root — what must stay, what is
deprecated, what is misplaced — then execute the cleanup on his approval.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-grep | comp-constants refs in .tools | WARN | 0 matches WITH honest denominator (301/302) + explicit not-absence warning; widened repo-scan then found the NFRA_MSBEFF PRD anchor |
| comp-grep | ajb.ps1 / _out.json / CIOHunt / SHAPE-renderer refs | PASS | found the .tools duplicate, the DS deliverable citations, the 0721 brief, and the canonical renderer path -- every rehoming decision grounded |
| comp-surface-check + comp-pulse | via safe-commit (x4 incl. 1 blocked) | PASS | clean every run |
| owned-paths gate | 2 live BLOCKS this window | PASS | docs/architecture = ANY_CTO, .gitignore = BASE_EXEC -- both correct denials of my commits; gate teaching at violation time |
| comp-rail HUD | denied raw lambdas.tf grep | PASS | re-ran with rail-checked marker (literal doc-citation string; no comp-tool answers contains-this-string) |

**What worked:** comp-grep's explicit denominator + "0 is not absence" banner prevented a false
comp-constants-unused conclusion; the escaped-pipe warning caught my BRE-style alternation.
**What failed:** nothing. Two of my own commits were correctly refused by the lane gate.
**Gap found:** a failed safe-commit leaves the pathspec STAGED (the wrapper stages before the
gate rules), so reverting needs `git restore --source=HEAD --staged --worktree` -- a plain
`git checkout --` restores from the polluted index. Reported to CTO~B.

---

## Work Completed

### 1. Programme-close residuals

CTO~B independently re-derived all 7 batches (2,940 total incl. their 8). Their one precision
correction landed @ca203111b: B-0007's closing row now reads 0 CRO-ELIGIBLE / 1 POD2-ROUTED
(never "DRY" -- a successor reading DRY will not go looking for the one). Their two TF
cross-check scope conditions accepted into cycle 3 (binding ratified cohort verdicts re-derived
at adjudication; deliberate build-recipe-dependency pass per lambda tree).

### 2. Root FILE audit + cleanup (Andrew-approved)

Grounded every file (tracked status, RCG label, provenance commit, references) before acting.
DELETED 3: .runtmp_deployed_renderer.py (stale 07-07 copy of the deployed ETFS renderer --
canonical at data/etfs/scripts/presentation/render_month_end.py; the re-upload-is-the-deploy
hazard), .runtmp_pairwise_msg.txt (its commit 727e5dfb1d landed), ciohunt_console.png
(mojibake, superseded). REHOMED + COMMITTED @9e74010fd7: requirements.txt ->
docs/reference/PYTHON_DEPENDENCY_INVENTORY_20260710.txt (dated -- it is an inventory, not a
live env spec); ciohunt_console_clean.png -> docs/briefs/ beside its 0721 brief;
agents-riding-the-graph-c0-c3.png -> CRO deliverables (docs/architecture blocked, ANY_CTO --
rehome offered to CTO~B). PARKED in owners' deliverables (uncommitted, their lanes):
depth_assess_out.json + shell_serve_census_out.json -> 0.4.0_DS_ClientPlatform/deliverables/
OVP_WS1/ (their docs cite these as machine output); t4a_measure_out.json ->
0.2.0_DS_PortfolioAnalytics/deliverables/ (MDPF_GLOBAL.T4A artifact). LEFT DELIBERATELY:
ajb.ps1 root copy (Andrew-direct @81660e0f2a; forwarder conversion awaits his explicit word)
and archival-cldmd.md (his documented swap-back copy @5b10944aca).

### 3. Root DIRECTORY audit + reap (~456MB, Andrew-approved)

Census: tracked counts, sizes, vintages, ignore status for 12 dirs. REAPED: .runtmp/ (its sole
content = 349MB portal-promote-20260803T172733Z worktree, verified UNREGISTERED in portal
worktree list; portal main tree confirmed on DEV), .claude/worktrees/agent-a8970f0ad7c4b95af
(103MB, 05-23), .pytest_cache, .ruff_cache, __pycache__, .playwright-mcp, catboost_info,
.fedobs_tmp (July diagnostic scraps), .mdpf_restore (07-28 restore checkpoints, insurance
expired, contents re-derivable from live systems). KEPT (load-bearing): .github (CI),
.tools (terraform.exe is the 87MB by law), .claude (skills+settings), .comp-graph (the
auto-refreshing comp-kuzu DB).

### 4. Findings routed to 1.0.0_SA_CTO~B (BASE_EXEC lane items)

(1) .gitignore needs `.ruff_cache/` + `catboost_info/` (my attempt lane-blocked, edit reverted
byte-clean). (2) 75 untracked files under .tools/ awaiting git custody -- the blanket-ignore
RULE was already fixed (gitignore's own annotation, MSTR 065137Z), so these are uncommitted
work; aws.cmd precedent @789c291ba names the risk class. (3) Optional git mv of the C0-C3
diagram into docs/architecture/. Flagged for awareness only: live registered portal worktree
at Desktop/_portal_hotfix_wt (hotfix/global-monthly-axis-key) -- outside workspace, untouched.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Delete .mdpf_restore rather than park | insurance for a restore 7 days settled; contents were snapshots OF live systems, re-derivable |
| Park DS/T4A evidence files rather than commit them | their lanes; citing docs are theirs; Andrew ferries the notes (R-0001 keeps CRO MCP-silent to worker lanes) |
| Do not convert ajb.ps1 to a forwarder | fabric-critical launcher; "follow your recs" is not an explicit word on an item I flagged "your call" |
| Accept both lane-gate denials rather than override | the gate teaching at violation time is the design; routed to the owning lane instead |

---

## Files Modified

See commit messages: ca203111b (B-0007 precision row), 9e74010fd7 (3 rehomed artifacts).
Deletions were all untracked (no commits): 3 root files + 9 directories, ~456MB reclaimed.
Parked uncommitted in owner lanes: 3 JSONs (listed above).

---

## Blockers

**None.** Two lane-gate denials were correct refusals, not blockers -- both items routed to
the owning lane (CTO~B) same-turn.

---

## Current State

> Zero-context handoff.

Workspace root is clean: 10 tracked config/law files (.gitattributes .gitignore .gitmodules
.mcp.json .owned-paths.yaml CLAUDE.md README.md ajb.ps1 comp-constants.config.yaml pytest.ini),
two Andrew-parked copies (ajb.ps1 dup of .tools/ajb.ps1, byte-identical today; archival-cldmd.md
gitignored swap-back), .env (ignored), and only real content directories. ~456MB reaped.
RCG state unchanged from the 0633Z log: programme closed (0 CRO-eligible / 1 POD2-routed),
cycle 3 open @283f1b1d5, model v3 a35ac7af + frozen v2/v3 predictions awaiting the prospective
E-0004. At CTO~B: gitignore 2-liner, .tools custody sweep, optional diagram mv. With Andrew:
two DS ferry notes (0.4.0_DS OVP_WS1 JSONs; 0.2.0_DS t4a JSON), ajb.ps1 forwarder word.

---

## Next Steps

1. **[4.0.0_SA_CRO] Author the 411-file adjudication protocol** (cycle 3 human mass, both
   CTO~B scope conditions folded) -- to [1.0.0_SA_CTO~B] for review before any disposition.
2. **[Andrew] Ferry the two DS notes** -- [0.4.0_DS_ClientPlatform]: OVP_WS1 machine-output
   JSONs moved from root into deliverables/OVP_WS1/, commit beside the citing docs or
   regenerate-on-demand; [0.2.0_DS_PortfolioAnalytics]: t4a_measure_out.json moved into your
   deliverables/, commit or delete.
3. **[1.0.0_SA_CTO~B] BASE_EXEC items** -- gitignore 2-liner, .tools 75-file custody sweep,
   optional diagram mv (their queue, routed 065740Z).
4. **[4.0.0_SA_CRO] Then cycle-3 doctrine note + MIGRATE/layer-refactor spec + step-1b** --
   order unchanged.
