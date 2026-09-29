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
| R1 | **NFRA_OPALAI OA-e-3 files missing from CLOUD** (predates the crash). CORRECTED by 1.0.0_SA_CTO~O (msg 26654, row NFRA_OPALAI-Z-S45): they WERE committed on the worker branch (82b68d5ce2); drain merge d45ab2cf53 dropped them. Re-measured here: the proof blob at d45ab2cf53^2 = the shared-tree file (34efe4dbee), absent at CLOUD. My "never committed" read the shared tree only | shared tree: TO `<status>` pending->complete ` M`; untracked `deliverables/0.9.0_WK_NFRA_OPALAI~10/{NFRA_OPALAI.TO-OA-e-3.asker-switch-on.proof_of_spec.json, ANNOUNCE_OA-e-3.md, OA-e-3_RELEASE_TREE_TESTS.txt}` and `org/critical_paths/change_management/20260929T0319Z_nfra-opalai-r2-asker-switch-on-gateway_deploy_completion.md` (CLOSED, 5 of 5 legs). `proof-of-spec-check.py` on the instance: **VALID (rc=0)**, 6 of 6 artifacts resolved. Its EC2_MANIFEST commit a9e1a5ce26 IS in CLOUD. Class UNFINISHED-EDITS. | RULED by CTO~O: re-drain by `2.0.0_SA_COO~AI` (spawn asked of MSTR~Z). This CVO validates on that drain: all 10 paths equal their branch-parent blobs. |
| R2 | NFRA_OPALAI `deliverables/0.9.0_WK_NFRA_OPALAI~18/` untracked (OA-f-3 proof + session_log, 2026-09-28 18:56 ET) | 2 files, never committed | same as R1 |
| R3 | NFRA_OPLGTW `deliverables/2.0.0_SA_COO~O/round2_drafts/` untracked | 14 TO drafts + `checks/` | CLOSED by `2.0.0_SA_COO~O`: all 14 issued under the same names; moved to `.runtime/crash-investigation-20260929/wt-scratch-archive/coo-o-nfra-oplgtw/` (@2981fdcc6e) |
| R4 | NFRA_MCPINDEX deploy entry `nfra-mcpindex-bd-playwright-strip` **OPEN** | MX-s-14 PHASE B, opened 04:22 ET, 16 h window (expires ~20:22 ET); acceptance = tonight's scheduled fires 17:38 / 17:45 / 17:53 ET. Deliberately open, not residue. | `2.0.0_SA_COO~MI`: L6 closed by it post-crash (@6fac7c1a77); L5/L9 close on the fires, before the window |
| R5 | `C:/Users/Opal Bloomberg/Desktop/cto_o_tflocal` tracked edit `.tools/naming-gate.py` | HEAD drained; the edit is byte-identical to CLOUD (f3e10beb8c both), so not unique | `1.0.0_SA_CTO~O` (own worktree) |

This seat's own residue: none. Last act d57669b492 (05:35 ET, MX-r-5 re-sign) answered the last message; delivery
ledger since 00:00Z = 19 of 19 READ; no uncommitted file authored by `~O` under the CVO home. (Two untracked files
there, `*_20260923_Z.md`, are by NAME CVO~Z's AMGT work -- an untracked file carries no author.)

## 2. Worktree assessment (35 in scope: 3 KEEP + 32 DISPOSE-ELIGIBLE)

The live opal-gateway (EC2_MANIFEST at HEAD): deployed_commit **093fc247c6** (MX-r-5, 06:11 ET, `0.9.0_WK_NFRA_MCPINDEX~14`),
previous **63264dfb22**. All three gateway projects ship the same service; every earlier rel/rb/dep tree is superseded
(its deploy entry CLOSED in `change_management/`).

**Revised ~14:30 ET on 2.0.0_SA_COO~MI's table (msg 26635, `org/tier1_exec/2.0.0_SA_COO~MI/POST_CRASH_ASSESSMENT_NFRA_MCPINDEX_20260929.md`
@6fac7c1a77):** this record's first cut (d7a07a3fef) kept the live trio mx-rel6/dep6/rb6 as a rollback asset. A checkout is
not the asset; the commit is. Measured `git branch --contains`: rollback HEAD 63264dfb22 is on `rel-nfra-mcpindex-r4-gateway-b`
AND `rel-nfra-oplgtw-export-flat`; 4248b70b39 and d287ffb346 are on three rel-* branches each; og-x3-rb2's 7c7ebe14d3 on
`rel-nfra-opalai-r2-asker-switch-on-gateway-v2`. So a rollback tree is `git worktree add <path> <branch>` away.
**CONDITION on every disposal below: no `rel-*` / `dep-*` / `rb-*` BRANCH is deleted while 093fc247c6 is the live gateway.**
CVO~O CONCURS with COO~MI's MCPINDEX table as written (KEEP 1, DISPOSE 13).

### KEEP (3)

| worktree | why |
|---|---|
| Desktop/wk-mcpindex-r4-15 | MX-t-10 (PENDING, BLOCKED on Z-W15-S5) candidate; also pinned by COO~MI at `refs/archive/wt-20260929/wk-mcpindex-r4-15-candidate` 03a19ac282 |
| Desktop/cto_o_tflocal | CTO~O's own worktree with a tracked edit (R5) |
| C:/tmp/wk-report-4-4 | NOT this seat's project (NFRA_REPORT, ~Z fabric): tracked INVESTIGATION edit + untracked worker deliverables, 3 weeks old -- owner's call |

### DISPOSE-ELIGIBLE (32) -- HEAD reachable from a kept branch; untracked = `mcportal/` submodule checkout, `.scratch/`, `.venv-og/`, `.build/` only

| project | worktrees | basis |
|---|---|---|
| NFRA_MCPINDEX | mx-rel3, mx-rel4, mx-rel5, mx-rel6, mx-dep4, mx-dep5, mx-dep6, mx-rb4*, mx-rb5*, mx-rb6* | release/deploy/rollback trees; r3 enable CLOSED 21:37 ET 09-28, r4 CLOSED 05:54 ET; branches kept (condition above) |
| NFRA_MCPINDEX | wk-mcpindex-r3-11, r4-14, r4-16 | worker branches DRAINED into CLOUD; `.scratch/` only |
| NFRA_OPALAI | oa-10-rel, oa-10-rel2, oa-10-rb2, oa-10-sw-rel, oa-10-sw-rel2, oa-10-sw-rb2 | superseded by two later gateway releases; deploys CLOSED |
| NFRA_OPALAI | oa-10, oa-15 | DRAINED; oa-10's only tracked edit is `opal-gateway/audit.jsonl` (runtime), oa-15 `.scratch*` |
| NFRA_OPLGTW | og-x3-rb*, og-x3-rb2*, og-x3-rel, og-x3-rel2, og-x4-rb*, og-x4-rel | superseded; og-x4-rel's HEAD 63264dfb22 = the live rollback target, kept on its branch |
| NFRA_OPLGTW | wk-oplgtw-10, -11, -12, -13 | DRAINED; `.scratch/` + `.venv-og/` only (MSTR~Z skipped these as UNTRACKED) |
| NFRA_MCPORTAL | mp3-1 | DRAINED; `.scratch/` + two lambda `.build/` dirs |

`*` detached HEAD: every one is contained in a named rel-* branch (measured), so a pin is optional. `.scratch/` dirs: archive to
`.runtime/crash-investigation-20260929/wt-scratch-archive/` first, as pass 1 did.

**Disposal is the project COO's act** (`/cleanup` policy; canonical-flow ORPHAN-WORKTREE owner): `2.0.0_SA_COO~MI` for
MCPINDEX, `2.0.0_SA_COO~O` for OPLGTW + MCPORTAL, OPALAI's COO once seated. No in-scope worktree is an ORPHAN
(every worker branch is drained or intentionally unmerged as a release tree).

## 3. Canonical-flow position (report-only)

| project | limb | open TOs (to-check --all) | class |
|---|---|---|---|
| NFRA_MCPINDEX | L7, round 4 (round-3 slug answered: ROUND_ANALYSIS.round3) | 2 pending: MX-s-14, MX-t-10 | IN-PROGRESS/STALLED per COO~MI's probe; R4 open deploy |
| NFRA_OPALAI | L7, round 2 | 4 pending: OA-e-6, OA-e-8, OA-t-1, OA-t-3 | UNFINISHED-EDITS (R1, R2) + no live COO |
| NFRA_OPLGTW | L7, round 3 (corrected from COO~O's read) | OG-g-1 pending + OG-v-7/t-2/v-8/n-1 staged; OG-r-3's LAST tag is superseded (to-check reads the first) | SEQUENCED-BEHIND on Andrew/MCPORTAL gates |
| NFRA_MCPORTAL | EXECUTING (not measured further) | -- | mp3-1 only |

Workflow restart for this seat: event-driven at L8 when each round's drain lands; nothing is owed by the CVO now.

## 4. Concurrence with 2.0.0_SA_COO~O (msg 26641, NFRA_OPLGTW @2981fdcc6e)

CVO~O CONCURS on all 10 OPLGTW checkouts (wk-oplgtw-10..13, og-x3-rb, og-x3-rb2, og-x3-rel, og-x3-rel2, og-x4-rb,
og-x4-rel): DISPOSE, branches kept. Independently measured here: the 4 worker HEADs are ancestors of CLOUD 0bbde7112f;
the 3 detached HEADs are each inside a named rel-* branch. Same condition as section 2: no rel-/dep-/rb- branch is
deleted while 093fc247c6 is the live gateway (og-x4-rel's 63264dfb22 is its one-step rollback target).

## 5. Concurrence with 1.0.0_SA_CTO~O (msg 26654, NFRA_OPALAI + NFRA_MCPORTAL + cto_o_tflocal @ae5f28c218)

CVO~O CONCURS on all 10 checkouts: 0 KEEP, 10 DISPOSE, every branch kept. This supersedes section 2's KEEP of
cto_o_tflocal (its one edit is byte-identical to CLOUD). **wk-NFRA_OPALAI-10 and the OA-f-3 worker branch are the
re-drain SOURCE: they must not be deleted before the re-drain lands and passes the 10-path blob check.** Same gateway
condition as section 2. The in-scope KEEP is now 2: wk-mcpindex-r4-15, and wk-report-4-4 (not this seat's).

## 6. Amendment recorded (1.0.0_SA_CTO~O msg 26677, on 2.0.0_SA_COO~O msg 26674)

C:/tmp/mp3-1 moves from DISPOSE to KEEP until NFRA_OPLGTW OG-n-1 closes: its untracked
`mcportal-grant-writer-deps` build zip exists in 1 linked worktree only. This narrows the set this seat concurred on
and needs no verdict. In-scope KEEP is now 3 (wk-mcpindex-r4-15, mp3-1, wk-report-4-4).

## 7. Amendment recorded (1.0.0_SA_CTO~O msg 26695, ~16:30 ET)

- mp3-1 returns to DISPOSE: its KEEP condition was "until OG-n-1 closes", and OG-n-1 reads complete (12d1de0062,
  0.9.0_WK_NFRA_OPLGTW~14, 16:14 ET, drained into CLOUD).
- C:/tmp/wk-oplgtw-14 (new, OG-n-1's worker) joins the removal set. Measured here: HEAD 12d1de0062 is an ancestor of
  CLOUD; untracked `.scratch/` + one lambda `.build/` only. CVO~O CONCURS: DISPOSE, branch kept.
- For this seat's next NFRA_OPLGTW L8 compile: REMEDIATION_v1 carries S45 (no EIP) ARMED OPEN; row Z-S19 @18badb8d01
  records its disarm (EIP 3.214.118.242 on i-07dccb1615503ac99, read live by 1.0.0_SA_CTO~O).
- In-scope KEEP is back to 2 (wk-mcpindex-r4-15, wk-report-4-4). Removal set put to Andrew: 34.
