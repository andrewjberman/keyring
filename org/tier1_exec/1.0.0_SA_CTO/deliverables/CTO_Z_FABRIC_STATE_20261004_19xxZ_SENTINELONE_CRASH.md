# Site-Z AMGT fabric: state at the SentinelOne crash (1.0.0_SA_CTO~Z, 2026-10-04 ~19:3xZ)

Ask: `0.0.0_AB_MSTR~Z` msg 29191, record
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261004_191xZ_SENTINELONE_FLEET_CRASH_ASSESS_STATE_BRING_ON_CTO_Z_AND_CTO_O.md`
@4f005a07db. Scope: this CTO's fabric only. The ~O fabric (NFRA_OPLGTW, NFRA_OPALAI, NFRA_MCPINDEX, NFRA_MCPMSP and their
worktrees) belongs to `1.0.0_SA_CTO~O`.

## How it was measured

- Telemetry: `org/mcp/agent_telemetry/*.jsonl`, rows in the window 18:25:00Z to 18:58:20Z. 10 serials appear.
- Git: CLOUD since 12:00Z (11 commits). All 28 worktrees from `git worktree list --porcelain`, each read for tracked-dirty,
  untracked, `CLOUD..HEAD`, and `ls-tree` of `.open_deploys/`. Every file in any worktree changed after 18:20Z was listed.
- Portal: `git -C portal fetch origin DEV PROD`, then ancestry of the DSGN candidate.
- Times are UTC. Commit times were converted from ET.

## Context: the fabric had been running for about 25 minutes

Every site-Z seat stopped at about 03:22Z (cause not measured; tick-44 log @29e44bd234). The PARITY HOLD held all commits to CLOUD
until PARITY CLOSED at 18:1xZ (msg 29158). This seat relayed the resume at ~18:3xZ (msgs 29176-29182). The crash came at 18:58:20Z.
So no fabric seat committed to CLOUD between 03:21:40Z and the crash. The work that was lost or left in flight is in the trees,
not on the trunk.

## Per seat

| Seat | Last tool call | Project | Limb / round at the crash | Uncommitted or unmerged work | Open deploy entries |
|---|---|---|---|---|---|
| `2.0.0_SA_COO~H` | 18:54:59Z (27 calls, 2 Agent) | AMGT_HARVST | Round 44 L7. It was issued 03:21Z: four READ cells grading FWD-2/5/7/12. All four `aq-N.READ.md` exist on disk (17:58Z-18:41Z). The drain-end packet to the CVO was not written. | **Main tree, uncommitted:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round44/` (4 READ files plus their scripts and outputs). Also surprise row `AMGT_HARVST-Z-S82` appended to `surprise-channel/investigations/INVESTIGATION_v1.md` (mtime 18:51:45Z). It holds 64% pre-2026 rows in the served gold mentions and is INERT. | none |
| `2.0.0_SA_COO~Z` | 18:56:06Z (10 calls) | AMGT_RESAPP | Round 67 L7. ONE issuance at 02:26Z (e410b00b27) cut 5 cells: aq-1..aq-4 LOCAL on workers ~219..~222, and aq-5 the redeploy (AE~A, staged). The 03:22Z stall hit the round mid-execution. No cell has been drained. | **Worktree branches, committed, NOT merged:** `C:/tmp/r67-219` `wk-AMGT_RESAPP-219` (aq-1 fix and proof, 2 commits). `C:/tmp/r67-220` (aq-2, 1 commit). `C:/tmp/r67-221` (aq-3, 1 commit). **Uncommitted:** `C:/tmp/r67-222` holds aq-4 partial work: `lib/research/api/scoped_amgt.py` and `tests/conftest.py` modified, plus new `lib/research/coverage/covered_no_block.py`, a new test, and the worker deliverables dir. It has 0 commits. The worker sessions are dead. | none (aq-5 not yet opened) |
| `2.0.0_SA_COO~X` | 18:53:13Z (10 calls) | AMGT_CORPUS | Round 35. ak-1 and ak-2 are drained. The ak-4 never-widen pair is SIGNED: COO 36ad5a67f9, CTO 5eebfe43f1 under 5 conditions. Its legs run AFTER the 2026-10-04 13:00Z FWD-22 acceptance read. That read had not been graded. | **Main tree, uncommitted:** `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/evidence/r35_ak4_gate_dryrun.txt` (18:56:17Z). **Pinned worktree, untracked:** the 13:00Z fire output `opal-pinned/amgt-induction-daily/a864e82a5c4b/.../induction_run_2026-10-0{3,4}_fire.json` is the FWD-22 evidence (10-04: population 1, other 1, called 0, errors 0). | none (ak-4 legs not yet opened) |
| `2.0.0_SA_COO~D` | 18:56:33Z (32 calls, 2 Agent) | DSGN_AMGTV1 | Round 34 CLOSED at 02:10Z (a408efb24a). Candidate portal `055ba370` was APPROVED by this seat under 2 conditions (720f78e6f6). Condition 1 is met (de215bcd50). Condition 2 is the DEV push on Andrew's word by MSTR. It also names 7 reopened outcomes for the next round. | **Portal, committed, unpushed:** `055ba370` on local portal branch `dsgn-r34-onto-dev` (checked out in `C:/tmp/wk-dsgn-amgtv1-92/portal`). It is 12 commits ahead of origin/DEV `c7bc52c8` (fetched 19:3xZ). It is in the shared portal object store, so it is safe. No new worktree was created after 18:20Z, so what the 2 Agent calls ran is not visible here. | none |
| `2.0.0_SA_COO~RV` | 18:56:34Z (13 calls) | ETFS_RIVALS | Round 7 CLOSED (2026-10-03 00:36Z). Round 8 is PREPARED at L5, not issued. By its own record it is cut after the 2026-10-05 grades. Row Z-S20 (BLOCKING/ARMED) stops I-2 at the gate on its cost measurement. | **Branch, committed, NOT merged:** `C:/tmp/rv-fast` `rv-prep8`, 8 commits (decomposition draft, register measure, checks). The tree is clean. | none |
| `3.0.0_SA_CVO~Z` | 18:56:26Z (8 calls) | L8/L9 for all five, plus NFRA_SPRINTWIN | Nothing in flight. Owed now: the NFRA_SPRINTWIN ratified-text half (proportionate). Next owed: HARVST r44, CORPUS r35 and RESAPP r67 compiles, once each COO drains. | none found | none |
| `4.0.0_SA_CRO~Z` | 18:56:34Z (18 calls) | NFRA_SPRINTWIN | Andrew ~18:43Z: CRO~Z builds it SOLO, with no COO lane (record @7ea45d9b41). The build had not started on any branch. | **Branch, committed, NOT merged:** `wt-croz-sprint-census` `croz-sprint-census-20261004`, 5 commits (record, brief, a CLOUD merge). The merge 395f4be3bb is authored bare `0.0.0_AB_MSTR`, which is the known `user.name` leak. The tree is clean. | none |
| `1.0.0_SA_CTO~Z` | 18:55:32Z | the five AMGT_FRIDAY projects plus NFRA_SPRINTWIN | NFRA_SPRINTWIN L3+L4 landed (9f81b531fb, b72b0dbf30). | **Main tree, uncommitted (18:55:12Z):** NFRA_SPRINTWIN `prd/NFRA_SPRINTWIN_PRD.md` and `project.json` record CRO~Z's solo seating. These are committed with this report. Branch `ctoz-sprintwin-20261004` (f15b8a86ce) is SUPERSEDED: its content landed on CLOUD at b72b0dbf30. | none of this fabric |
| `0.7.0_AE_CloudOps~A` | no telemetry after 12:00Z | (RESAPP aq-5, CORPUS ak-4 legs) | Not live. | none | none |

**Open deploy entries:** 0 belong to this fabric's projects. CLOUD HEAD tracks 27 entries, plus 4 IRPT entries untracked on disk in
the main tree. All are laptop-fabric (COO~P/~M/~Y, CRO base, MSTR base), with two exceptions. `d12-sms-origination-identity-activation`
(this seat, HELD-SOVEREIGN-GATED since 09-02) and `leadpanel-price-producer-schedule` (`0.0.3_BG_BBGTerminal`, OPEN since 09-24)
both predate the crash. On worktree branches, every entry missing from CLOUD HEAD was traced to a CLOUD close (`--full-history`
D-filter), including the two AMGT_RESAPP ones (r56 af-6 closed @3373f73c27, r64 an-7 closed @bf4b04b120). None is a live branch-only
deploy.

## Relaunch

| Seat | Relaunch? | Why |
|---|---|---|
| `2.0.0_SA_COO~H` | **YES** | Commit the r44 READ cells and row Z-S82, write the drain-end packet, and hand off to the CVO. |
| `2.0.0_SA_COO~Z` | **YES** | Drain r67 aq-1..aq-3 from their branches. Re-cut or finish aq-4 from the partial in `r67-222`. Then aq-5. |
| `2.0.0_SA_COO~X` | **YES** | Grade the 13:00Z FWD-22 read and run the ak-4 legs under the signed pair. |
| `3.0.0_SA_CVO~Z` | **YES** | Sign the SPRINTWIN half now. It is the L8/L9 seat for the three rounds above. |
| `4.0.0_SA_CRO~Z` | **YES** | Andrew's solo-build word of ~18:43Z is live work. |
| `2.0.0_SA_COO~D` | **YES** | It cuts the next round on the 7 reopened outcomes. The 055ba370 DEV push itself waits on Andrew's word (MSTR's act). |
| `2.0.0_SA_COO~RV` | **LATER** | Round 8 waits on the 2026-10-05 grades by its own record. A relaunch before then has no act to take. |
| `0.7.0_AE_CloudOps~A` | **LATER** | Bring it on when COO~Z reaches aq-5 or COO~X reaches the ak-4 legs. Nothing is open for it now. |
| `3.0.0_SA_CVO~RV`, `4.0.0_SA_CRO~RV` | NO | They were not live before the crash, and round 8 is not cut. |

Loops: every seat relaunches with ZERO crons (org/XXX.md 1b-F). The `1.0.0_SA_CTO~Z` `/self-drive 60m` row and the COO
`/canonical-drive` rows in `org/ref/LIVE_ARMS.md` re-arm only on the operator's word.

## For Andrew (surfaced, not adjudicated)

- Andrew named "COO~RV ... working ETFS_HARVST". `org/missions` has 0 hits for `ETFS_HARVST`; `ETFS_RIVALS` has 8 hits in
  DIRECTIVES.yaml. COO~RV's seat is ETFS_RIVALS.
- The main tree also has uncommitted ~O-fabric edits from 01:34Z (opal-gateway schwab files, NFRA_OPLGTW TO-OG-gr-3 / rl-5 and r16
  checks). They are `1.0.0_SA_CTO~O`'s to account for.
- Cleanup candidates, not caused by the crash and not removed: `wk-hvst-r32-92`, `wk-hvst-r39-90`, `wk-hvst-r39-91`,
  `wk-dsgn-amgtv1-93` (0 ahead), `ctoz-sprintwin` (superseded). Keep `wk-dsgn-amgtv1-92` until 055ba370 is pushed. Removal is
  deletion and needs the operator's confirmation.
