# work_0113Z — AE 0.7~C Phase 3 trio sister-pre-stage v0.7.0

| | |
|---|---|
| Agent | 0.7.0_AE_CloudOps~C |
| Tick | 2026-05-28T~01:13Z (manual continue per Andrew direction; off-cron) |
| Spawn | MSTR-DIRECT SPAWN-WITH-DIRECTION 2026-05-27T~23:35Z |
| Lane scope | Phase 3 serving-deploy sister-pre-stage |
| Cycle outcome | v0.7.0 substrate pre-staged commit 9cfff17a9 + RAVC1 routed |

## Substance

Per ws COO §6.3 ratify direction 00:08Z + lesson absorbed from URGENT-unblock 1e195e276 incident: author DS~E TO .022 trio sister-deploy TF skeleton with HCL `/* */` block-comment guard from the author moment, not as remediation pass.

3 Lambdas covering .022 brief §B.1-B.3 deliverables (Phase 3 IR-team-facing serving tables):
- `find-insure-serving-companies` — companies-table emitter (99-IMO cross-channel)
- `find-insure-serving-employees` — employees-table emitter (Phase 2A subset + GDPR opt-out)
- `find-insure-serving-scoring` — methodology+thresholds+version-stamp emitter

## Shipped

`9cfff17a9` (origin/CLOUD `1e195e276..9cfff17a9`) — 2 files / +230 lines:
- NEW `infra/aws/terraform/imo-pipeline/phase3-serving-trio-lambdas.tf` — 3 module + 3 permission resources wrapped in single HCL `/* */` from author moment with explicit UN-COMMENT TRIGGER marker
- MOD `infra/aws/lambda/ci/lambda-source-map.json` — +3 entries with `_pre_stage:true` + `_pre_stage_blocker` documentation

Sizing per brief §B.4:
- companies + employees: 1024MB / 600s (99-IMO cross-channel scan + parquet write)
- scoring: 256MB / 60s (methodology config-class lightweight)

## Forward-flagged for COO/CTO routing

**(a) Parquet layer dependency** — find-insure-data-deps layer (pandas+pyarrow) NOT yet provisioned. Sub-task at v0.7.0 build moment; flagged in TF comment block + commit message. RAVC1 §3(b) asks whether to author layer in pre-stage class also (separate TF + source) on subsequent /work tick.

**(b) SCOPE-OVERLAP `.022` ↔ `.023`** — both Lambdas write `serving/scoring.json` per current spec (.022 §B.3 methodology vs .023 §AC2 ranked-companies). DS~E disposition needed pre-source-ship. RAVC1 §3(c) routes SYNC-ASK to DS~E via COO; 3 disposition options surfaced (split-paths / fold-to-2-Lambdas / namespace-distinct).

Pre-stage TF authored under option (i) "keep both Lambdas; split paths" assumption since least-churn at apply moment. AE TF may collapse to 2 Lambdas or namespace-shift post-DS~E disposition.

## Operating-pattern absorbed (lesson from URGENT-unblock)

**Pre-stage TF authoring discipline:** any TF file that embeds yang-lambda module references MUST wrap module + permission blocks in HCL `/* */` from the author commit. The module's internal `data "aws_s3_object" "artifact"` lookup evaluates at `terraform plan` time and errors fabric-wide if the artifact zip doesn't exist. Commented-out TF parses cleanly + preserves substrate intent verbatim for un-comment at paired-apply moment.

Banking as workspace operating pattern; will propose to memory `feedback_pre_stage_tf_must_be_comment_wrapped_from_author_moment` if not already captured.

## Standing posture

- COO §3 ratify on (a)+(b)+(c) — RESUME proactive work per §3(b) direction
- DS~E `.022` source-ship trigger → v0.7.0 paired apply
- DS~E `.023` source-ship trigger → v0.6.0 paired apply
- DS~E SYNC-ASK disposition on scope-overlap → TF refactor if needed
- /work 20m cron continues (CronCreate aa388021)

No further proactive pre-stage work to author this turn — all 4 Phase 3 serving Lambdas now have TF skeleton pre-staged. Forward motion = ratify + DS~E source + paired-apply moments.

## Authority + audit

- tier0_commit_hash: 746464ed1
- spawn_anchor: MSTR-DIRECT SPAWN-WITH-DIRECTION 2026-05-27T~23:35Z (Andrew direct 23:25Z parallelize)
- COO direction anchor: ws COO MCP 2026-05-28T~00:08Z §6.3 "next /work tick author .022 trio TF skeleton sister"
- Per LD-0116: RAVC1 → ws COO only (primary); CC ws CTO (parallel TF-content ratify)

work-cycle:003
