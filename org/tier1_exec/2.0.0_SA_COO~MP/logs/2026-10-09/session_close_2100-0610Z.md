# 2.0.0_SA_COO~MP -- session close 2026-10-08 ~21:00Z to 2026-10-09 06:10Z -- NFRA_MCPORTAL control plane (FWD-14 thread)
**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

## Summary

The session re-seated this lane on NFRA_MCPORTAL, which Andrew un-parked ~18:4xZ 2026-10-08 (PRD v0.5 @cecf26d2c9, FWD-14 to
FWD-19, the control plane). Four things happened:
1. Round 4 built and verified the FWD-14 handler and page.
2. Rounds 3 and 4 closed at the project grain.
3. Round 5 was issued; the gateway read grant is LIVE.
4. Round 6 (FWD-15 to FWD-17) was drafted, ruled by the CTO and given its producers.

At close, Andrew approved issuing FWD-15 to FWD-17 as workstream CP2 AFTER the reboot (record below).

## Current State (zero-context handoff)

| Item | State | Evidence |
|---|---|---|
| Project | `org/missions/D6/NFRA/NFRA_MCPORTAL/`, PRD v0.5, lease FULL, `dep_stage` EXECUTING, round 5 | project.json `blocking` |
| FWD-14 handler `GET /api/admin/fabric/boxes` | BUILT and drained, NOT live | `infra/aws/ec2/opal-gateway/app/admin_fabric.py`, drain @1cf3a1dce5 |
| FWD-14 page (Control Plane, refreshes every 60 s) | BUILT, NOT live | mcportal `d60b4e0`, LOCAL on mcportal branch `wk-NFRA_MCPORTAL-r4-6-mcportal` |
| Gateway read grant `gateway-mcportal-fabric-read-policy` | LIVE on `opal-gateway-role`: GetObject on `fabric/activity/v1/*` and `fabric/open-calls/v1/*`; ListBucket conditioned on both | MP-x-3 complete @93052772a7; ledger `nfra-mcportal-r4-fabric-read-grant` CLOSED |
| Host cold read (pre-release probe, 04:2xZ) | 21.3 s cold, 0.8 s warm, 3,004 records; R-13 bar is 30 s | the applier was told by message |
| Live gateway | `deployed_commit` aa75078e1b (r28); `mcportal_commit` a3bff71 | `infra/aws/ec2/EC2_MANIFEST.json` |
| Site Z activity hook | installed 05:11Z by `0.0.0_AB_MSTR~Z` | msg 32424 |
| Applier lane | `0.7.0_AE_CloudOps~MP` (fresh lane; `~Z` refused by the seating rule), LIVE | spawned ~02:0xZ via /mstr-spawn |
| Drive loop | cron `620d0d66`, `/canonical-drive NFRA_MCPORTAL once` at :22/:52, session-only (dies at the reboot) | LIVE_ARMS row + @ba8c4598fb |

**Round 5 orders** (`task-orders/`, decomposition v5):

| Order | Status | Assignee | Gate |
|---|---|---|---|
| MP-x-3 grant | complete | 0.7.0_AE_CloudOps~MP | -- |
| MP-x-4 release | staged | 0.7.0_AE_CloudOps~MP | G-REL: NFRA_OPLGTW r29 drained (`2.0.0_SA_COO~O` msg 32304: deploy >=11:00Z, drain ~12:00-14:00Z); release on r29's base |
| MP-x-5 close run (JUDGMENT) | staged | worker ~5 | MP-x-4 drained + one card to Andrew (G-SEE) |
| MP-c-2 FWD-1 close run | staged | worker ~1 | G-CLOSE: r29 live + Andrew's sitting with Alyssa |
| MP-v-2 FWD-2 live arms | staged | worker ~3 | MP-x-4 drained + G-2ND (a person signs in as Opal Bloomberg) |

**Round 6 / CP2 inputs:**
- Draft `deliverables/2.0.0_SA_COO~MP/round6/R6_DECOMP_DRAFT.md` (@54c2fd91b6, with the ruling note).
- `1.0.0_SA_CTO~O` msg 32404: Q1-Q3 (a), gateway read side only; the `requests/` PutObject grant is a never-widen cell for
  `0.7.0_AE_CloudOps~MP`.
- Producers by the laptop `4.0.0_SA_CRO` @5bf8350baa. Read back from S3:
  - `fabric/open-calls/v1/box=laptop/open_deploys.json`, schema with `entries[]` (29 entries);
  - `fabric/activity/v1/gitstate/box=laptop/latest.json`, schema `fabric-gitstate/1`;
  - close requests go to `box=<B>/requests/<id>.json`, schema `open-calls-close-request/1`, with results under
    `request_results/`.
- Andrew-direct approval:
  `deliverables/2.0.0_SA_COO~MP/ANDREW_DIRECT_20261009_060xZ_CP2_WORKSTREAM_APPROVED_START_POST_REBOOT.md`.

## Key decisions and rulings this session

- **Z-S18 (C11 grant vs. CLDGRPH R3):** routed cross-fabric; ruled (a) by the laptop NFRA_CLDGRPH owner (msg 107359, relay
  32030).
- **Z-S19:** the one-issuance limb refuses a late new order file and takes no override. Gated cells are issued STAGED in the
  first issuance.
- **Rounds 3-4 L10 deadlock:**
  - MP-c-1 and MP-v-1 were superseded (never spawned) @39ea2d5e3e, on the round-2 precedent, and re-cut as MP-c-2 and
    MP-v-2.
  - `<to_id>` was added to all orders @5e59e66320.
  - The CTO's analysis followed @460bc0af2f.
- **Z-S21:** the policy name was refused at apply and pinned by AC1. Amendment 1 @807220a352 uses the builder name
  `gateway-mcportal-fabric-read-policy`.
- **Z-S20:** disarmed the four round-1 ARMED rows transferred by R-18.
- **C12 "streaming"** means the page updates while open (CTO msg 32041). MP-x-2 amendment 1 implements it.

## MCP traffic

About 45 messages handled, all acked. The significant ones:
- the CTO analysis (32001 PRD landed, the analysis);
- rulings 32021, 32030, 32041, 32404, 32426;
- G-REL timing 32304;
- the applier reports 32307, 32334 and 32353;
- MSTR relays 32061, 32162, 32227, 32297, 32312, 32363, 32390, 32423 and 32424.

Sent:
- ruling asks to 1.0.0_SA_CTO~O (C11, Q1-Q3, CP2);
- the L8 packet and nudge to 3.0.0_SA_CVO~Z;
- the GO and the rulings to 0.7.0_AE_CloudOps~MP;
- the r29 ask to 2.0.0_SA_COO~O;
- the hook and index-drift asks to 0.0.0_AB_MSTR~Z.

## Blockers

None of this seat's. Event-gated:
- MP-x-4 on NFRA_OPLGTW r29's drain (2.0.0_SA_COO~O, msg 32304);
- MP-x-5, MP-c-2 and MP-v-2 on Andrew's acts.

## Next Steps

1. **[2.0.0_SA_COO~MP, after the reboot] Start workstream CP2, per Andrew's approval.**
   - Cut decomposition `CP2` round 1 from `R6_DECOMP_DRAFT.md`, with `<workstream>CP2</workstream>` beside `<round>` on
     every order.
   - FWD-15 overlap, FWD-16 git state and FWD-17 calls: one handler cell each, plus the panels cell.
   - The never-widen `requests/` PutObject grant goes to `0.7.0_AE_CloudOps~MP`.
   - The CP2 release cell is staged on MP-x-4. Issue it in ONE issuance, with the gated cells STAGED.
2. **[2.0.0_SA_COO~MP]** Re-arm `/canonical-drive NFRA_MCPORTAL` at :22/:52, `/watcher` first.
3. **[2.0.0_SA_COO~MP]** On r29's drain (`2.0.0_SA_COO~O`), send the GO for MP-x-4 to `0.7.0_AE_CloudOps~MP`. That seat
   must re-check the cold read against R-13's 30 s bar at release time.
4. **[2.0.0_SA_COO~MP]** After MP-x-4 drains: one card to Andrew (G-SEE), write `x5_seen.json`, and spawn the MP-x-5 worker.
5. **[Andrew]** The page look (G-SEE), Alyssa's sitting after r29 (G-CLOSE), and a second-account sign-in (G-2ND).
6. **[Andrew]** Two drained worktrees, `C:/tmp/mp-r4-5` and `C:/tmp/mp-r4-6`, hold only untracked `.scratch/`. Removing
   them is a forced (recursive) delete and needs his word, or `/cleanup`.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| prd-signoff.py status | STALE -> SIGNED | v0.5 ratified half by 3.0.0_SA_CVO~Z |
| to-pipeline-gate (via safe-commit) | PASS / REFUSED | issuances admitted; late MP-x-3 file refused (Z-S19); MP-x-3 flip refused on an INVALID instance, then PASS |
| round-close-check | REFUSED -> MAY-CLOSE | fixed by `<to_id>`, bare status and supersede |
| missions-tree-index check/derive | PASS | 0 violations after each stage change; two foreign drifts surfaced and routed |
| proof-of-spec-check | INVALID -> VALID | MP-x-3 instance, 11 violations fixed by the applier |
| comp-surprise | PASS | 45 rows, 12 armed (round 1-3), owners seated |
| comp-state --self-test | PASS 4/4 | -- |
| surprise-row-gate | REFUSED x2 then PASS | time format; in-place mutation refused (append-only) |
| mstr-spawn pre-flight | PASS | 1pt 0/12, markers 0, concurrency 4/20, 1d clean |
| unstick --peek | PASS | no keys sent; showed the applier working |
| IAM simulate (x3.AC2) | PASS 6/6 | positive and negative arms |
| SSM host probe | PASS | read-only scratch copy, removed |

**What worked:**
- Re-running every worker's checks in a fresh worktree before draining.
- The seating lint catching a 3-project applier.
- `round-close-check` exposing the missing `<to_id>`.

**What failed:**
- My decomposition's "cut gated cells later by amendment" plan (Z-S19).
- My own policy name, refused at apply (Z-S21).
- A commit-message hook tripping on backticks inside an embedded python heredoc. I split the command and nothing ran.

**Gap found:**
- The commit naming limb RAISEs an interpolated name that the apply limb later refuses (Z-S21 option (c), left for the gate
  owner).
- `deploy_ledger.py close-leg` silently overwrites a closed leg's proof (reported by the applier).

**Push state:** LOCAL. box/sitez HEAD 40b39ad88d; origin box/sitez read 44eb421ef6 at 06:1xZ (ls-remote). This seat
never pushes; box-sync carries it.
