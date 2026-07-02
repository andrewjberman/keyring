# 0.7.0_AE_CloudOps -- /ycharts-report refined to the blended/model-portfolio flow (Andrew-direct via CTO)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, TRACE, DIAGNOSE, VALIDATE

**Window:** 2026-07-02 ~16:50Z (session start / CTO handoff) -> ~18:05Z.
**Lane:** 0.7.0_AE_CloudOps (base). Andrew-direct handoff via 1.0.0_SA_CTO (164631Z).

## Summary
Brought back onto the `/ycharts-report` skill to extend it to the MODEL-PORTFOLIO / "Blended"
flow from Alyssa's new material. Reverse-engineered the mechanics from the HAR, transcribed the
audio for intent, folded both into the skill (CTO-ACCEPTED), applied the CTO's Q2 refinement, and
attempted the CTO-green-lit live e2e test -- which surfaced the single-seat guardrail (browser
concurrent-sign-in), handled cleanly and escalated. Also landed a small in-lane EC2_MANIFEST fix
handed off by 0.5.0.

## Item 1 -- /ycharts-report blended/model-portfolio refinement (e5faf5b5c + a89661012) -- ACCEPTED
Two Downloads files processed:
- **Blended walkthrough.har** (95.7MB, 865 entries) -- parsed with jq (extracts in scratchpad
  `har_flow_urls.tsv` / `har_bodies.json`). Reverse-engineered the full endpoint sequence + POST/PUT
  request bodies.
- **NW Corporate Blvd 2_6807.m4a** (12MB) -- transcribed via **AWS Transcribe** (uploaded to owned
  S3 scratch prefix `opal-313476888478-lambda-artifacts/_scratch/transcribe/`, job ~80s, pulled the
  1626-word transcript, then DELETED audio+output+job record; scratch verified empty). Client audio
  stayed in-AWS; nothing leaked.

**Key finding:** "Blended" is a NEW PRIMITIVE, not just a new report template. The current skill
only SELECTED an existing portfolio; the walkthrough BUILDS a client portfolio (`label:client_portfolio`)
as a dollar-weighted blend of N Opal models, then reports on it. So I added **Flow B (BUILD)** alongside
**Flow A (SELECT)**, both sharing the `custom_pdf_reports` engine:
- B create: `POST /model_portfolios/fixed/` (multipart portfolio+items) -> 201 EMPTY body / no Location
  -> new `P:<id>` resolved by list-reload (sortColumn=user_modify_date desc, row 1).
- B recalc: `PUT /model_portfolios/fixed/<id>?calculate=true`.
- Report: generate/collection?securityId -> generate/<templateId> -> validate_report_securities ->
  POST /custom_pdf_reports/<templateId> -> presigned S3 PDF. Full generate-POST body schema captured
  (was generic in v1). Transition-analysis surface (serialized_transition_analyses/transitionAnalyses)
  documented as PRESENT-but-UNUSED (transition_analysis/list returned []) -- NOT built (CTO Q1: YAGNI).

**Intent rules folded from the audio (Alyssa):** 3 templates Opal uses (Overview/Comparison/Multi-Comp,
all No-Benchmark) + ask->template decision table ("blend" -> Overview); title = client name only (strip
template suffix, HAR confirms "Louis Aquino "); prepared_for from requester email domain; Dollars weight
input; backtest-range caveat (~Apr-2024 model inception).

**CTO validate (171126Z) -- ACCEPTED.** Q1 transition-analysis = leave documented-surface (done). Q2
advisory fee = keep explicit input+default 1%, demote Dawson-Moses 0.36% to a FLAGGED reference note
(not hardcoded map) -> applied in a89661012. Q3 = green-light live throwaway test (see Item 3).

## Item 2 -- EC2_MANIFEST mdpf-daily-runner cron_schedule fix (eaa6a5352)
0.5.0_AE_OpalETL handoff (owned-paths correctly BLOCKED their commit: lane=SHARED_CLOUD_OPS). The
`cron_schedule` field said `cron(0 15 ? * MON-FRI *)` but the LIVE EventBridge rule is event-driven.
**Re-verified live myself (not trusting the self-report)** via `aws events describe-rule`:
mdpf-daily-refresh-trigger = ScheduleExpression=null, EventPattern=S3 ObjectCreated
opal-data-inf/gold/meta/pipeline-complete.json, State=ENABLED; the only mdpf cron is
mdpf-freshness-check-trigger (cron(45 16)) = the freshness ALARM. Corrected the field with a
self-grounded value. JSON re-validated (jq). Doc-field hygiene; nothing operational changed. CC COO.

## Item 3 -- Q3 live e2e test: BLOCKED on single-seat guardrail (escalated, no fire)
Attempted the green-lit throwaway BUILD+Overview live test. Injected the `ycharts/credentials` cookie
bundle into Playwright via a gitignored file (no fresh login -- caveat b honored), navigated to
`/model_portfolios/list/` -> **bounced to `/accounts/logged_out/concurrent_sign_in`** ("You've Been
Signed Out"). STOPPED per guardrail; did NOT fresh-login (would evict a possibly-mid-session Alyssa);
cleaned up (removed stale injection file; no artifacts created in ycharts).

**Grounded diagnosis (corrected my own first read before the CTO acted):** the credential is NOT dead.
`mcp ycharts_freshness` = {ok:true, HTTP 200} -> the gateway's server-side GET works; the deployed
ycharts_* MCP integration is HEALTHY, no outage. The block is BROWSER-INTERACTIVE-only: same cookie,
server-side GET succeeds but an interactive browser session is evicted (200-vs-bounce divergence).
Mechanism (interactive-route eviction vs stateless-API) = labeled HYPOTHESIS, not proven.

**CTO call (180131Z) then Andrew-direct (180400Z):** C' (dedicated YCharts SERVICE seat, YALP_MDSRC)
= the DURABLE fix, CTO flagging to Andrew on his cadence. A' (clear-seat window) = the eventual
live-validation. Andrew-direct: *"we don't need to re-sign in for ycharts, that can wait."* -> the live
browser exercise is **DEFERRED-by-operator** (not blocked). Flow-B stays code-complete + accepted; no fire.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| (none of comp-*) | see note | -- |

No comp-* tool triggered a gate this window: the work was skill-doc reverse-engineering (jq over a
95MB HAR + AWS Transcribe), a JSON doc-field hygiene fix, and live browser/gateway verification --
no gold run (comp-pipescript deployed), no iam.tf change (comp-iam gaps), and the EC2_MANIFEST edit
was a description-string-only change with no behavior/blast-radius (comp-blast moot). The EventBridge
correction was ground-truthed directly via `aws events describe-rule` and the gateway health via
`mcp ycharts_freshness` (both live), which is the right grounding for those claims.
**Gap found:** none new. (Prior comp-rail HUD false-positive on quoted `aws iam` substrings still stands.)

## Verification (actual output)
- `aws events describe-rule mdpf-daily-refresh-trigger` -> ScheduleExpression=null; EventPattern S3
  ObjectCreated opal-data-inf gold/meta/pipeline-complete.json; State=ENABLED. mdpf-freshness-check
  -> cron(45 16 * * ? *). (2 mdpf rules total.)
- `mcp ycharts_freshness` -> {"ok":true,"detail":"HTTP 200"} (gateway credential valid server-side).
- Playwright nav /model_portfolios/list/ -> redirected /accounts/logged_out/concurrent_sign_in.
- Commits: e5faf5b5c, a89661012 (skill), eaa6a5352 (manifest) -- all safe-commit surface-check OK,
  pushed CLOUD (e5faf5b5c..a89661012).

## Blockers
- **None.** Q3 live e2e test is **DEFERRED-by-operator** (Andrew-direct 180400Z: "we don't need to
  re-sign in for ycharts, that can wait"), NOT blocked. The single-seat concurrent_sign_in bounce was
  verified live (gateway 200 = credential valid; browser-interactive contention only); Flow-B is
  code-complete + CTO-accepted + HAR-verified. The live browser exercise resumes on Andrew's cadence
  (a clear-seat window or after the YALP_MDSRC service seat lands -- CTO will ping). Nothing actionable
  by me now; not a code defect.

## Current State (handoff)
- `.claude/skills/ycharts-report/SKILL.md` @a89661012: two-mode skill (Flow A SELECT + Flow B BUILD),
  shared custom_pdf_reports engine, exact HAR request-body schemas, Alyssa's intent rules, fee-as-input,
  transition-analysis as documented-surface, roadmap note (front-end intake form -> DE-lane candidate,
  CTO surfacing to Andrew). Frontmatter description updated (harness re-read it live).
- `infra/aws/ec2/EC2_MANIFEST.json` @eaa6a5352: mdpf-daily-runner.cron_schedule corrected to
  event-driven (live-verified 2026-07-02).
- YCharts gateway (ycharts_* MCP): HEALTHY (freshness 200). Skill Flow-B: code-complete, HAR-verified,
  NOT yet live-exercised (Q3 pending clear-seat).
- Scratchpad (client-PII, NOT committed): blended_flow_digest.md, har_bodies.json, har_flow_urls.tsv,
  transcript_plain.txt.

## Next Steps
- **[0.7.0_AE_CloudOps]** YCharts loop DONE + accepted; Q3 deferred by Andrew. Available for the next
  cloud-ops slice -- signalling COO. When Andrew wants the live-validation (CTO pings, clear-seat or
  post-YALP_MDSRC service seat): resume the injection-only BUILD+Overview test (throwaway blend, clean
  up after) + RAVC CTO -> closes the deferred Q3.
- **[1.0.0_SA_CTO]** (future, Andrew's cadence) flag the YALP_MDSRC dedicated YCharts service seat as
  the durable fix for browser-driven runs; ping me for the live-validation when Andrew wants it.
- **[2.0.0_SA_COO]** DATA_PLATFORM DC1/DC2 recon TOs re-slot (held per COO); ~A on ETLFIX gated-tails.
  Base 0.7.0 available for the re-slot / next queue.
