# ETFS_GUARDRAIL round 1 from three running workers to ROUND_CLOSE in one night: eleven drains, eight face amendments on the issuer's own cut defects, one false drift caught by three hashes, the L8 packet, the CVO's L9 and the CTO's L10 -- 2.0.0_SA_COO~B

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Date:** 2026-09-05
**Task Order:** ad-hoc -- the scoped /drive loop on ETFS_GUARDRAIL under Andrew-direct via 1.0.0_SA_CTO 94224/94225 (record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260904_170xZ_COOB_GOAL_AND_DRIVE_LOOP_ETFS_GUARDRAIL_DISPATCH_DRAIN.md` @329d71c079)
**Status:** IN PROGRESS at the project (dep_stage ROUND_CLOSE; 1 REALIZED + 7 NOT_EVALUATED until the scheduled fires); COMPLETE for every limb this lane owns (L5, L6, L7, L8)
**Window:** 2026-09-04 19:4xZ (the previous log, three workers just spawned) -> 2026-09-05 15:2xZ. Drive ticks 6 through 54.

---

## Objective

Drain the fourteen task orders of ETFS_GUARDRAIL round 1 through three worker subagents in their own worktrees, hand each slot its next order in dependency order, rule every row the workers filed, compile the L8 packet for the CVO as the orders went terminal, and carry the round to the CTO's L10 read -- without messaging a worker, without pushing, and without an act outside this project.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| proof-of-spec-check | `python .tools/proof-of-spec-check.py <instance> <ids>` x14 at HEAD after each drain | PASS | 14 of 14 instances VALID rc 0 with coverage checked; the issuer's own run, never the worker's |
| safe-merge | `bash .tools/safe-merge.sh wk-ETFS_GUARDRAIL-<n> -m ...` x14 drains | PASS | every refusal correct: peers' staged files (4x), a transiently malformed peer channel (1x); channel conflicts united by row id and `--continue`d (8x) |
| to-pipeline-gate / owned-paths / surprise-row-gate / missions-tree-check | at every safe-commit and merge | PASS | one owned-paths refusal on the worker (CHANGELOG.json, W2-S5) was the gate working; the row gate refused a `--continue` once on a peer's mid-edit file and passed on the re-run |
| owned-paths-validate | `--check-agent 2.0.0_SA_COO~B` on `build-zip.sh` and `.gitattributes` | PASS | both refused for this lane, which decided the routing of W1-S5 and S2 |
| comp-surprise | `--project ETFS_GUARDRAIL --json` | PARTIAL | lists items/open/armed with denominators; carries no CVO watermark key, so the CVO's L9 state had to be read from the tree |
| comp-state | `--self-test`; `comp-state` | PASS | 4/4 planted verdicts; the one BEHIND on ETFS_GUARDRAIL.json was lexical (the row already read ROUND_CLOSE) |
| comp-schedule | `--help`; the C1 grammar read at `safe_deploy_core.py:290` | PASS | nothing is stored: the dated reads went in as DEPLOY-SERVE-HELD sentinels in `ledger/SCHEDULE_GATES.round1.yaml` (this log's second file) |
| git ls-remote / rev-parse / worktree | every tick | PASS | push state measured per tick; origin moved twice (@b000632f27, then @76c5f90155 which equals the round's last commit) |

**What worked:** the checker at the issuer's seat with coverage ids, run after every merge, never before; `safe-merge.sh` refusing exactly the unions that were not mine; three hashes (live bytes, LF rendering, CRLF rendering) settling a "drift" that two workers, two rulings and a packet revision had taken as real.
**What failed:** `comp-schedule --help | sed` and `comp-surprise | head` were rail-refused (correctly); `git worktree add` from CLOUD exceeds the Bash tool's 120 s bound on this repo (30,317 files) and ran in the background; the never-rules gate refused a `safe-commit` paired with `$(` in the same call twice under time pressure.
**Gap found:** no comp-tool reads a Terraform plan's hash back to the checkout that produced it; the false-drift discriminator (hash the live bytes and both line-ending renderings) is a memory entry now, not a tool. comp-surprise has no CVO-watermark key.

---

## Work Completed

### 1. Eleven drains, fourteen orders terminal (L7)
Every worker report was read with its proof instance, the branch merged through `safe-merge.sh`, the instance re-graded at HEAD by this seat with the expected ids, the worktree torn down and re-created from CLOUD for the next order, and the next face passed verbatim in a continuation. Drains at `108d9fa67f` (EG-s-11), `a8e3ac7927` (EG-s-12), `62cc386d94` (EG-s-4), `c866edd324` (EG-s-1), `745cd6b354` (EG-s-7), `fb0776daae` (EG-s-2), `c50c72f92a` (EG-sb-7), `1c5603a696` (EG-s-5), `f036a438fb` (EG-s-8), `c17da2f4a8` (EG-s-6), `9ce1de85e7` (EG-s-9, the last). Six deploys under NEVER-2 ledger entries, every apply through `safe-apply` on terraform v1.9.8, all three remote states still at 1.9.8.

### 2. Eight face amendments, each on a worker's row, each a cut defect of this seat
`de8693863c` (the flip grant wording; the calendar layer per CTO~Z's ruling), `83d8175729` (the instance filename = the task order's basename), `2baa6af162` (by-target applies; the terraform binary; real pytest functions), `75985f2068` (CHANGELOG.json into EG-s-2's grant), `446a064491` (the false-drift correction on EG-s-8/9; the `--gate` seam as deliverable 5 + S8-AC9), `e32bdf96ea` (S9-AC2 HEADER_SITES=3). Plus one audited lane override `4b35d14ff4` (the bd-pipeline CHANGELOG deploy record, lane CLOUD_OPS_OR_ETL, rule 14a's named escape).

### 3. Three seat rows
S1 at the cut (the discriminator's principal); S2 (the reporter `user_data` drift was a CRLF checkout artifact: live sha1 `e47b615c` == the LF rendering, the plan's `434774b5` == the CRLF rendering; 414 of 414 `.tf` CRLF in every fresh worktree on this autocrlf box); S3 (no cell owned passing `--gate` from the orchestrator to the renderer).

### 4. The L8 packet, nine revisions in place, the drain-end one at `05e0b5bbd8`
`ledger/L8_PACKET.round1.partial.md`: fourteen orders with the instance and commit each was graded at, fourteen judgment criteria, 21 rows with their standing, a CORRECTION banner over its own earlier drift story. The one drain-end read to the CTO 09:33Z; the obligation-4 pointer to the CVO 10:00Z.

### 5. L9 and L10, read and recorded
The CVO's `13b57fbb0e` (fourteen judgment criteria PASS on its own instruments; 21 of 21 rows dispositioned; the slug with S3 closed and S2 open) and `f2ef16d70a` (its framing correction); the CTO's `0557afa38a` (ROUND_CLOSE; 8 of 8 outcomes served, no addendum; FWD-6 REALIZED, seven NOT_EVALUATED; FWD-4 NOT_EVALUATED because a synthetic-fixture unit test is APPLIED, not EXERCISED; S2 carried into the CTO's queue). Message 94366 ACKed. No recut owed.

### 6. The schedule ledger entries (this invocation)
`ledger/SCHEDULE_GATES.round1.yaml`: three DEPLOY-SERVE-HELD sentinels compiled by comp-schedule's C1 carrier -- the 2026-10-01 14:00Z monthly-run read (FWD-2/3/5/7/8), the 2026-09-07 Labor Day read at that render (FWD-4), and the undated first-recovered-day read on the producers' daily fires (FWD-1); owner `1.0.0_SA_CTO` on each, discharge stated, the sweep rule in the header.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Apply BY TARGET in etfs-reports (W1-S7) | a second resource in the plan is never applied under a worker's order; the class (a `user_data` change stops and starts the instance) is confirm-with-Andrew. The premise turned out false (S2); the stop was still right |
| Provision `.tools/terraform.exe` and LF `.tf` files into every worker worktree | the binary is gitignored and the checkout is CRLF; a PATH substitute re-pins remote state, a CRLF heredoc hashes as drift |
| Land the CHANGELOG deploy record under the audited override | the worker had flipped, a terminal order grants nothing, the record would have died with the worktree |
| Mint S8-AC9 mid-round on row S3 | a seam no face owned would have left the 10-01 fire ungated; the order was open on its owner |
| No nudge to the CVO until obligation 4's tick; then a pointer only | the spine's three tracks share files, never the work product; the pointer cost nothing and the L9 landed within the tick |
| Flip nothing at ROUND_CLOSE/CLOSED; keep the loop at its recorded cadence | the flips are the CTO's (spine :347, :403); the cadence and stop condition are Andrew's record, surfaced in the tick-40 log and the stage report |

---

## Files Modified

See commit messages: `108d9fa67f` .. `9ce1de85e7` (the eleven drains), `de8693863c` `83d8175729` `2baa6af162` `75985f2068` `446a064491` `e32bdf96ea` (amendments), `4b35d14ff4` (override), `05e0b5bbd8` `18be639a6c` `6dcd8c92eb` `75a0f909f8` `e17adfafa3` `3816e1b0e9` `aae3f7900f` `0a9bf936af` (packet + drive logs), `fc69a70eb2` `5e4baca85f` (ticks 39-40). This invocation: this log and `org/missions/D8/ETFS/ETFS_GUARDRAIL/ledger/SCHEDULE_GATES.round1.yaml`.

---

## Blockers

None. The project waits on scheduled fires, not on any seat. Three open remediation items have owners (W2-S1 the inf-pipeline lane, W1-S5 CLOUD_OPS_OR_ETL, S2 the CTO).

---

## Current State

> Primary handoff point. Write as if briefing someone with zero prior context.

ETFS_GUARDRAIL (D8, laptop) round 1: `org/missions/D8/ETFS/ETFS_GUARDRAIL/project.json` reads `dep_stage: ROUND_CLOSE` (the CTO @`0557afa38a`); all fourteen task orders under `task-orders/` read `complete`; every proof instance under `deliverables/0.9.0_WK_ETFS_GUARDRAIL~{1,2,3}/` is VALID at HEAD; the L8 packet is `ledger/L8_PACKET.round1.partial.md` @`05e0b5bbd8`; the CVO's adjudication and slug are `surprise-channel/adjudications/ADJUDICATION_v1.md` and `remediations/REMEDIATION_v1.md` @`13b57fbb0e`/`f2ef16d70a`; the CTO's analysis is `ledger/ROUND_ANALYSIS.round1.md`. On the applied plane: `cot-etf-ownership-daily` and `bd-49f-etf-ownership-daily` carry the reporting-obligation catch-up and a probe mode with the `opal-trading-calendar-layer:1`; `etfs-reports-reporter-role` carries `InvokeProducersForRemediation`; `etfs-reports-orchestrator` carries the terminal send, `--gate` in `_render_command` and `EMAIL_RECIPIENT=aj@opalinvest.com,andrew@opalinvest.com`; the renderer with the coverage package is at `s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/`. No ETFS_GUARDRAIL worktree or branch remains. The dated reads still owed are declared in `ledger/SCHEDULE_GATES.round1.yaml` (comp-schedule C1). Push state: every round-1 commit is on origin (origin/CLOUD @`76c5f90155` by ls-remote 14:39Z). The scoped /drive cron (job 6cc3a870, `13,33,53 * * * *`) keeps ticking until `CLOSED` or Andrew's word.

---

## Next Steps

1. **Read the 2026-10-01 monthly run's artifacts** the same day and log them -- the five EXERCISED grades hang on it (gate 1 in the schedule ledger).
2. **[1.0.0_SA_CTO] Grade FWD-1..FWD-8 on the fires** and flip `CLOSED`; land `*.tf text eol=lf` in `.gitattributes` (S2, in the CTO's queue).
3. **[Andrew] Say whether the 20-minute /drive loop on this project stops or slows** before October; it has nothing to fire until the reads above.
4. **At the next cut anywhere, run the pre-spawn face census** (seams, censuses vs predecessors, deploy-tool paths, instance names, standing rulings, untracked binaries) -- the round's cost went into the cut, twice across the fabric.
