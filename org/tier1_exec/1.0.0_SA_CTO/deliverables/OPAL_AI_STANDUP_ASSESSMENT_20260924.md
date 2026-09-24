# ASSESSMENT -- standing up `opal_ai` on site Z so projects can be assigned

**Author:** `1.0.0_SA_CTO~O` | **Written:** 2026-09-24 ~19:1xZ | **Asked by:** Andrew-direct, record
`ANDREW_DIRECT_20260924_190xZ_CTO_O_ASSESS_OPAL_AI_STANDUP.md` (this folder).
**Vintage:** site Z CLOUD after @ab83d531c7. Repo and git reads, one GitHub `ls-remote`, and broker reads. No AWS, no
gateway call, no Teams call.

## 1. The source documents

| document | author | what it says |
|---|---|---|
| `docs/briefs/opal-ai-microproduct-repo-brief-20260923.md` (RCN-0014, @a47993af9c) | 4.0.0_SA_CRO~X | WHAT `opal_ai` is. It holds one agent and one indexed MCP, built in three slices: Opal first, then the template, then clients. It gives the slice-first layout, 12 outcomes, 15 must-be-trues and 8 calls. |
| `docs/briefs/opal-ai-gitops-split-brief-20260923.md` (RCN-0015, @40b964f616) | 4.0.0_SA_CRO~X | HOW it lives beside the monolith. It is a real submodule with the parent's gates. The brief lists 24 work items and 8 calls. |
| `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ASSESSMENT_OPAL_ANALYST_OPLGTW_MCPINDEX_TEMPLATING_20260922.md` (@20de682ede) | 4.0.0_SA_CRO~Z | The predecessor. Andrew approved all 7 of its recommendations on 2026-09-22. |

Both briefs are L1 intake for `/endpoint --forward`. Their named consumer is `1.0.0_SA_CTO~Z`. That seat PARKED both
on 2026-09-23 (@dc3f8a0b75): nobody works them while AMGT is armed, and they un-park when AMGT stands down or Andrew
re-scopes. **No L2 endpoint, no project, no PRD and no task order exists for `opal_ai` today.**

## 2. What moved since the briefs were written (measured today)

| thing | state now | instrument |
|---|---|---|
| GitHub `Opal-Capital/opal_ai` | **does not exist**. `opal_analyst` does not exist either. | `git ls-remote`: "Repository not found"; the portal control resolves |
| `.gitmodules` | 0 bytes. Gitlinks: `portal`, `models/factor_scanner` | `wc -c`, `git ls-files -s` |
| portal checkout | on `DEV` (the detached HEAD in RCN-0015 is fixed); 0 active hooks | `rev-parse`, `ls hooks` |
| nested-repo gate gap | filed again today as row AMGT_RESAPP Z-S255 by 3.0.0_SA_CVO~Z (@d4347b4147) | commit |
| gateway code | still `infra/aws/ec2/opal-gateway/`, 256 tracked files; last touched 09-21 | `git ls-files`, `git log` |
| NFRA_MCPINDEX | 9 of 38 complete, 29 pending, of which 5 are held on gates G-A, G-B, G-Q, G-S; wound down 09-21; no worker running | the last `<status>` tag of each order |
| MCPINDEX held branch `wk-nfra_mcpindex-1-1d` @119a49eef0 (MX-c-4, plus armed row W1-S5) | **not on this box and not on origin**. It lives on the laptop only. | `git cat-file`: not a valid object; `ls-remote`: none |
| NFRA_MCPINDEX placement | `laptop` in SEQUENCE.yaml; D9 is placed LAPTOP in DIRECTIVES.yaml | `sequence-check`, `directives-check` |
| NFRA_OPLGTW | 30 of 33 complete, OG-v-4 and OG-v-5 pending, 0 of 8 FWDs graded. **Stopped on Andrew's word 09-22**: "Finish your work and research on the OPLGTW project and do not go further with it". The G-C order is drafted and not issued. | @5799432c1c |
| D6 "Opal AI" | live, SITEZ, 0 member projects | `directives-check --code D6` |
| Opal Analyst on Teams | **Not working.** It has two independent watch blockers. (1) Its token lives 15 minutes and is minted only by the seat's own gateway call. (2) Reads fail 33 of 33 even with a live token, cause unknown. The gateway also has no tool that fetches `hostedContents`, so Andrew's 09-23 19:40Z message cannot be read. The engine owner named in `TEAMS_DUTY.md`, `0.5.0_AE_OpalETL~Z`, has been dark for 13 days. | `0.0.3_BG_BBGTerminal` log @0646a96553 |
| ~O fabric seats | only `1.0.0_SA_CTO~O` is live. `2.0.0_SA_COO~O` is not live; LIVE_ARMS still records it on the NFRA_OPLGTW drive. | `get_live_agents` |

## 3. What must happen, in dependency order

### Stage A -- decisions only Andrew can give (nothing below them starts without these)

| # | call | recommendation |
|---|---|---|
| A1 | Does `1.0.0_SA_CTO~O` take the L2 intake of RCN-0014 and RCN-0015 from `1.0.0_SA_CTO~Z`'s park? | Yes. ~Z is armed on AMGT, and the park names his re-scope as the un-park condition. |
| A2 | Is `opal_ai` the one repo, superseding the name `opal_analyst`? (RCN-0014 call 1) | Yes. The gateway and the index become folders inside it. |
| A3 | Create `Opal-Capital/opal_ai`, private, branches `DEV` and `PROD`. This is outward-facing, so it takes your word and `0.0.0_AB_MSTR~Z` acts. | Yes, now. Every repo-wiring item below waits on it. |
| A4 | Placement. Register the program under D6 "Opal AI" (SITEZ, empty, named for this), and move NFRA_MCPINDEX's placement to site Z (your 09-22 "D9 moves to sitez shortly" was never applied to the register). | Yes to both. OPLGTW and MCPINDEX finish as their own projects and deliver into `opal_ai/opal/`. |
| A5 | The Analyst launches from the parent root and reads its product files by path. This re-opens your 09-22 call 4. | Parent root. It keeps the fence, the rail and all 81 skills. |
| A6 | CI in `opal_ai`: py_compile, ruff py39, the gateway tests, and the firm-neutrality check. This is a new mechanical gate. | Yes. |
| A7 | NFRA_OPLGTW stays under your 09-22 stop unless you lift it. | Keep it stopped for now. Stage C does not need it. |
| A8 | `models/factor_scanner` is an empty gitlink. Map it or remove it in the same `.gitmodules` act. | Ask its owner. Remove it if it is not live anywhere. |

### Stage B -- the canonical front end (this seat, same day once A1 is given)

1. **L2**: `/endpoint --forward` on RCN-0014 and RCN-0015 together. FWD-1 is RCN-0014's thread: one staff member asks
   the Analyst one question in Teams, and it answers from the MCP with the figure's date, scope and source.
2. **L3**: register the program under D6 as three workstreams with disjoint write surfaces:
   - **W-REPO**: the GitOps split (RCN-0015 items 1-14, 24);
   - **W-ANALYST**: the Analyst back online on Teams, then its carve-out into `opal_ai/opal/agent/`;
   - **W-GATEWAY+INDEX**: the gateway move and its deploy path (items 15-19), then MCPINDEX's remaining cells re-cut
     onto `opal_ai` paths.
3. **L4**: one PRD. Under proportionate sign-off the CVO signs the ratified-text half once. The brief half is accepted
   because the CRO wrote the brief.
4. **Seats needed on the ~O fabric**: `2.0.0_SA_COO~O` (L5/L6 issuer; seat it fresh or re-use the lane) and
   `3.0.0_SA_CVO~O` (L4-R, L8, L9). `0.0.0_AB_MSTR~Z` creates the repo and pushes.

### Stage C -- work that can start before the repo exists

- **The Analyst back online (W-ANALYST, round 1).** None of this touches the repo split.
  - Fix blocker (2) first: reads fail with a live token. Test the recorded hypothesis that a gateway token is being
    presented to Graph with the wrong audience.
  - Fix blocker (1): replace the 15-minute coupling to the seat's own calls with a refresh the watch owns.
  - Add a `hostedContents` read to the gateway, so a message that arrives as hosted content can be read.
  - Replace the dark engine owner with a live lane.
  - Re-measure speed with the PRD section 11 method (two clocks, timed per stage) against the 5m45s baseline of
    2026-08-20.
- **MCPINDEX recovery**: the laptop pushes `wk-nfra_mcpindex-1-1d` to origin, or the cell is re-run here. Until then
  MX-c-4's work and row W1-S5 cannot be reached from site Z.

### Stage D -- the repo wiring (W-REPO; physical order is fixed)

1. Repo created (A3).
2. `.gitmodules` with `portal`, `opal_ai`, and `models/factor_scanner` mapped or removed.
3. **Lane file BEFORE hook.** `opal_ai` carries its own `.owned-paths.yaml`, or the hook reads the parent's through
   `--show-superproject-working-tree`. Installing the hook first blocks every commit, because the missing-file branch is
   fail-closed in block mode.
4. A hook installer for submodules, applied to `opal_ai` and `portal` alike.
5. Run `safe-commit.sh` once inside a nested repo and fix what it cannot find there.
6. Add `git submodule update --init` to the startup protocol, `wk-provision.sh` and the sparse-cone recipe.
   `wk-provision.sh` is generalised beyond its hard-coded `portal`.
7. A pointer-bump convention; `/integrate` learns the gitlink; the census tools (activity-check, fabric-commits,
   daily-sprint, outcome-check) iterate submodules.
8. CI (A6).
9. The law-text edits to CLAUDE.md Git and XXX.md Step 1a. These need your `ANDREW_LAW_EDIT_ORDER`.

### Stage E -- moving code in (by moving, never copying)

1. **The agent first** (your 09-22 call 6). Its product files (prompt, refs, tools, skills) go to `opal_ai/opal/agent/`.
   Runtime state (threads, logs, deliverables) stays in the workspace. The fence allowlist and the launcher follow in
   the same change. Proof: one denied write from the relocated seat.
2. **The gateway second.** It moves with its history, and the parent paths are deleted in the same commit that adds the
   pointer. `deploy-to-ec2.sh` and `safe-ec2-deploy.sh` are re-pointed in the same window, because a deploy from a
   nested path otherwise passes its clean-tree check over uncommitted changes and records the wrong repo's commit. The
   three `parents[N]` reaches and the four parent-to-gateway reaches are cut. Terraform stays in the parent.
3. **MCPINDEX third.** Its 29 open orders name `infra/aws/ec2/opal-gateway/` in their paths.

   **Recommended: close MCPINDEX round 1 now rather than execute it on the old paths.** No worker is running. The COO
   sends the L10 slug with the unstarted orders superseded, and I answer with a round-2 analysis re-cut onto `opal_ai`
   paths. The alternative is to run 29 orders against a path that is about to move, then re-cut the survivors anyway.

### Stage F -- later, not assignable yet

- The template slice starts after a proper V1, even V2, of the Opal agent. It is extracted by moving code from
  `opal/`, never by copying it.
- The vendor-access kit's self-heal module waits on AUTH_SELFHEAL's design.
- The monitor conflict in the Third-Party Standard is settled as fail-loud with no alarm (RCN-0014 call 6).
- Client slices wait on a named first client (your 2026-08-20 zero-partner ruling).

## 4. What can be assigned on this box the moment A1-A4 are given

| project / workstream | first act | seat |
|---|---|---|
| program L2 + L3 + L4 | `/endpoint --forward` on both briefs | 1.0.0_SA_CTO~O |
| W-ANALYST round 1 (Teams back online) | trace blocker (2), then the four fixes above | 2.0.0_SA_COO~O issues; workers |
| W-REPO | repo creation, then D2-D6 | 0.0.0_AB_MSTR~Z (create, push); COO~O issues the rest |
| NFRA_MCPINDEX | laptop pushes the held branch; round-1 L10 slug; round-2 re-cut | laptop MSTR; COO~O; this seat |

## 5. What this assessment does not claim

- The Teams blocker figures are `0.0.3_BG_BBGTerminal`'s own measurements from this morning. I did not re-run them.
- Gateway liveness is taken from 2.0.0_SA_COO~O's 09-22 log ("UP and healthy"). It was not re-measured.
- The laptop was not read. The MCPINDEX held branch is presumed to be there from the 09-21 position document.
- Every RCN-0015 finding other than those re-measured in section 2 is carried at its 09-23 vintage.
