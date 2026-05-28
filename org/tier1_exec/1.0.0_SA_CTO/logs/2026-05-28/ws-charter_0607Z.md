# /ws-charter cycle 0607Z — FIX (deploy-green-but-stale doctrine §4a)

**Serial:** 1.0.0_SA_CTO
**Class:** FIX

## Step 0-1
- HALT exit 0. Watcher AUTO-RESPAWN-INTERRUPT-LOST → kill-loop NONE + relaunch.

## Step 2 — Inbox (1 actionable)
- **AE 0.7~B [DOC-NOTE handoff — owned-paths]** — COO GO'd AE to author a build-before-apply doc-note for the deploy protocol (anchored on the v0.7.3 stale-zip near-miss), but `LAMBDA_DEPLOYMENT_PROTOCOL.md` is BASE_EXEC-lane (my ownership); owned-paths guard correctly blocked AE~B's commit. AE handed me ready-to-paste content + reverted working-tree clean (no --force). LD-0116 owned-path routing. ACTIONED.

## Step 4 — Classification + action: FIX
- HARD-BLOCK: none (deploy-protocol doctrine, ws-domain owned-path; not TIER0_LAW, not cross-fabric).
- Ladder: no CVO finding (not REPAIR-AMENDMENT); **FIX** — autonomous deploy-protocol-owner doctrine, no PRD touch.

### Action: §4a deploy-green-but-stale doctrine shipped — `cc20d8593`
`docs/deployment/LAMBDA_DEPLOYMENT_PROTOCOL.md`:
- NEW §4a — S3-sourced pipelines MUST run `build-and-upload.sh` before apply. `terraform apply` only RE-POINTS at the pre-built S3 zip (reads source-map `artifact_sha256`); does NOT build from source. Skipping build-and-upload → green 0-diff plan running STALE code (the trap). Two-model table (archive_file local-zip = no build-step-before-apply; S3-sourced = build-step mandatory). Mandatory S3-sourced sequence. CLAUDE.md Rule 2 precision-note ("commit + build-and-upload before apply").
- NEW anti-pattern row in §4 "What NOT to Do" table.
- Empirical anchor: FIND_INSURE v0.7.3 (3 imo Lambdas re-pointed at prior-day 21:26Z zips, ran stale v0.7.1 score-web `am_prominence=None` american-equity FP rollup=91 despite v3 env; AE 0.7~A refire caught pre-99-IMO-burn; rebuild `e1020554b`). `comp-pipescript deployed {fn}` MATCH = the post-apply structural catch.
- Content authored by AE 0.7~B; committed faithfully in BASE_EXEC lane (minor doc-voice polish only). ACK `20260528T061234Z`.

## Step 3 — Project-state-sweep / Stage 2 status
- **FIND_INSURE** Stage 2 "one-re-apply-from-firing" per COO /drive 179 (`cf9f05b59`): AE~A re-apply with AE~B's fresh v0.7.3 zips (`e1020554b`) → refire am_prominence PRESENT → dispatch_stage2 99-IMO → Phase 1 RAVC2 → [VERIFY-ELIGIBLE-COHORT] web×99 (CVO Mode A#2 trigger). AE~A/AE~B parallel-rebuild cross-wire collapsed (AE~B zips won).
- W1-revision RESOLVED (cycle 0537Z milestone). v0.7.3 classifier deployed-correct after the stale-zip fix.
- **Next ws-CTO decision surface: Phase 1 RAVC2-Accept (CTO+COO ratify)** once Stage 2 99-IMO regrade lands. No ws-CTO gate until then.
- No other RAVC2-pending / CTO-review-pending / Andrew-direct surface.

## Step 5 — Cycle-log
- Per-tick file: this file. Artifact = doctrine commit `cc20d8593`.
- Commit-tag: `ws-charter-cycle:0607Z class:FIX`.

## Next cycle
- Cron `:37`. Expected: Stage 2 99-IMO dispatch fired + regrade in flight; possibly Phase 1 RAVC2-Request landing (→ CTO+COO ratify surface) + 297-cell matrix web-scrape column populating toward VERIFIED. Watch for RAVC2-Accept as the next genuine decision.
