# Post-crash residue + worktree assessment -- 3.0.0_SA_CVO~O, 2026-09-29 ~14:15 ET

**Order:** `org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/ANDREW_DIRECT_20260929_1755Z_POST_CRASH_RESIDUE_CLEANUP_AND_WORKTREE_ASSESSMENT.md`
**Scope:** the four projects whose row names `3.0.0_SA_CVO~O` as CVO -- NFRA_MCPINDEX, NFRA_OPALAI, NFRA_OPLGTW, NFRA_MCPORTAL
(all `EXECUTING`, fabric site-z, CTO `1.0.0_SA_CTO~O`; no closer_contract; drive-mode FULL on the first three).
**Method:** `git worktree list` at ~14:05 ET (57 linked; 35 in scope incl. cto_o_tflocal and wk-report-4-4), per worktree: HEAD ancestor of local CLOUD 0bbde7112f,
`git status --porcelain` (tracked edits excluding portal/opal_ai/mcportal gitlinks + EC2_MANIFEST), untracked set.
Nothing below was touched by this seat. Disposal = checkout removal only (branch kept; detached HEAD pinned to
`refs/archive/wt-20260929/<name>` first), per the MSTR~Z reclaim mechanism.

## 1. Crash residue / loose ends (in scope)

| # | item | measured | owner of next act |
|---|---|---|---|
| R1 | **NFRA_OPALAI OA-e-3 finished but never committed** (predates the crash: 2026-09-28 23:19 ET) | shared tree: TO `<status>` pending->complete ` M`; untracked `deliverables/0.9.0_WK_NFRA_OPALAI~10/{NFRA_OPALAI.TO-OA-e-3.asker-switch-on.proof_of_spec.json, ANNOUNCE_OA-e-3.md, OA-e-3_RELEASE_TREE_TESTS.txt}` and `org/critical_paths/change_management/20260929T0319Z_nfra-opalai-r2-asker-switch-on-gateway_deploy_completion.md` (CLOSED, 5 of 5 legs). `proof-of-spec-check.py` on the instance: **VALID (rc=0)**, 6 of 6 artifacts resolved. Its EC2_MANIFEST commit a9e1a5ce26 IS in CLOUD. Class UNFINISHED-EDITS. | NFRA_OPALAI COO = `2.0.0_SA_COO~AI`, **not respawned** -> `1.0.0_SA_CTO~O` to seat it or name a COO. This CVO validates the commit against the TO's criteria when it lands. |
| R2 | NFRA_OPALAI `deliverables/0.9.0_WK_NFRA_OPALAI~18/` untracked (OA-f-3 proof + session_log, 2026-09-28 18:56 ET) | 2 files, never committed | same as R1 |
| R3 | NFRA_OPLGTW `deliverables/2.0.0_SA_COO~O/round2_drafts/` untracked | 14 TO drafts + `checks/` | `2.0.0_SA_COO~O` (its own drafts: commit or discard) |
| R4 | NFRA_MCPINDEX deploy entry `nfra-mcpindex-bd-playwright-strip` **OPEN** | MX-s-14 PHASE B, opened 04:22 ET, 16 h window (expires ~20:22 ET); acceptance = tonight's scheduled fires 17:38 / 17:45 / 17:53 ET. Deliberately open, not residue. | `2.0.0_SA_COO~MI`: close on the three fires, before the window |
| R5 | `C:/Users/Opal Bloomberg/Desktop/cto_o_tflocal` tracked edit `.tools/naming-gate.py` | HEAD drained; 1 modified file | `1.0.0_SA_CTO~O` (own worktree) |

This seat's own residue: none. Last act d57669b492 (05:35 ET, MX-r-5 re-sign) answered the last message; delivery
ledger since 00:00Z = 19 of 19 READ; no uncommitted file authored by `~O` under the CVO home. (Two untracked files
there, `*_20260923_Z.md`, are by NAME CVO~Z's AMGT work -- an untracked file carries no author.)

## 2. Worktree assessment (35 in scope: 6 KEEP + 29 DISPOSE-ELIGIBLE)

The live opal-gateway (EC2_MANIFEST at HEAD): deployed_commit **093fc247c6** (MX-r-5, 06:11 ET, `0.9.0_WK_NFRA_MCPINDEX~14`),
previous **63264dfb22**. All three gateway projects ship the same service, so only the CURRENT release trio is a
rollback asset; every earlier rel/rb/dep tree is superseded (its deploy entry CLOSED in `change_management/`).

### KEEP (6)

| worktree | why |
|---|---|
| C:/tmp/mx-rel6 (rel-nfra-mcpindex-r4-gateway-b, a7e15b2220) | release of the LIVE gateway |
| C:/tmp/mx-dep6 (dep-nfra-mcpindex-r4-gateway-b) | deploy tree of the LIVE gateway |
| C:/tmp/mx-rb6 (detached 63264dfb22) | the one-step rollback target (= previous_deployed_commit) |
| Desktop/wk-mcpindex-r4-15 | MX-t-10 (PENDING) byte-frozen candidate: 5 tracked edits + 1 untracked catalog entry exist nowhere else |
| Desktop/cto_o_tflocal | CTO~O's own worktree with a tracked edit (R5) |
| C:/tmp/wk-report-4-4 | NOT this seat's project (NFRA_REPORT, ~Z fabric): tracked INVESTIGATION edit + untracked worker deliverables, 3 weeks old -- owner's call |

### DISPOSE-ELIGIBLE (29) -- HEAD reachable from a kept ref; untracked = `mcportal/` submodule checkout, `.scratch/`, `.venv-og/`, `.build/` only

| project | worktrees | basis |
|---|---|---|
| NFRA_MCPINDEX | mx-rel3, mx-rel4, mx-rel5, mx-dep4, mx-dep5, mx-rb4*, mx-rb5* | superseded gateway releases (r3 enable CLOSED 21:37 ET 09-28; r4 CLOSED 05:54 ET) |
| NFRA_MCPINDEX | wk-mcpindex-r3-11, r4-14, r4-16 | worker branches DRAINED into CLOUD; `.scratch/` only |
| NFRA_OPALAI | oa-10-rel, oa-10-rel2, oa-10-rb2, oa-10-sw-rel, oa-10-sw-rel2, oa-10-sw-rb2 | superseded by two later gateway releases; deploys CLOSED |
| NFRA_OPALAI | oa-10, oa-15 | DRAINED; oa-10's only tracked edit is `opal-gateway/audit.jsonl` (runtime), oa-15 `.scratch*` |
| NFRA_OPLGTW | og-x3-rb*, og-x3-rb2*, og-x3-rel, og-x3-rel2, og-x4-rb*, og-x4-rel | superseded; og-x4-rel's HEAD 63264dfb22 is duplicated by the KEPT mx-rb6 |
| NFRA_OPLGTW | wk-oplgtw-10, -11, -12, -13 | DRAINED; `.scratch/` + `.venv-og/` only (MSTR~Z skipped these as UNTRACKED) |
| NFRA_MCPORTAL | mp3-1 | DRAINED; `.scratch/` + two lambda `.build/` dirs |

`*` detached HEAD: pin to `refs/archive/wt-20260929/<name>` before removal. `.scratch/` dirs: archive to
`.runtime/crash-investigation-20260929/wt-scratch-archive/` first, as pass 1 did.

**Disposal is the project COO's act** (`/cleanup` policy; canonical-flow ORPHAN-WORKTREE owner): `2.0.0_SA_COO~MI` for
MCPINDEX, `2.0.0_SA_COO~O` for OPLGTW + MCPORTAL, OPALAI's COO once seated. No in-scope worktree is an ORPHAN
(every worker branch is drained or intentionally unmerged as a release tree).

## 3. Canonical-flow position (report-only)

| project | limb | open TOs (to-check --all) | class |
|---|---|---|---|
| NFRA_MCPINDEX | L7, round 4 (round-3 slug answered: ROUND_ANALYSIS.round3) | 2 pending: MX-s-14, MX-t-10 | IN-PROGRESS/STALLED per COO~MI's probe; R4 open deploy |
| NFRA_OPALAI | L7, round 2 | 4 pending: OA-e-6, OA-e-8, OA-t-1, OA-t-3 | UNFINISHED-EDITS (R1, R2) + no live COO |
| NFRA_OPLGTW | L7, round 2 | 1 pending (OG-g-1, AE_CloudOps~O) + 5 staged | R3 drafts uncommitted |
| NFRA_MCPORTAL | EXECUTING (not measured further) | -- | mp3-1 only |

Workflow restart for this seat: event-driven at L8 when each round's drain lands; nothing is owed by the CVO now.
