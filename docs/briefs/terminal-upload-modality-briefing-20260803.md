# Briefing: the /terminal-upload modality (new agent-driven path onto the Yang dashboard pipeline)

**Date:** 2026-08-03 · **Author:** `0.0.0_AB_MSTR~Z` (Andrew-direct: brief the main fabric so
issues arising from this modality have a referable record) · **Commissioned same day as, and
folding the lessons of, the MDLP_MONPUB ST incident.**

## What it is

`/terminal-upload` — a skill that runs the daily Bloomberg dashboard refresh end-to-end from
the terminal machine (site Z) with **no portal UI**: Yang's two notebooks via
`run_daily_pull.py` (cma env) -> the leg-2 tripwire -> the gateway's server-side
`opal_data_refresh_upload` -> pipeline watch -> live-manifest confirmation -> an independent
served read. Operator-invoked, one-shot, no loops. Forms: bare (real send), `dry`
(pending/ only, no pipeline fire), `send-only`, `pull-only`, `--allow-stale N`, `--date`.

**Two copies exist, deliberately:**
- CANONICAL: `.claude/skills/terminal-upload/SKILL.md` (this repo).
- DEVICE-HOME: `%USERPROFILE%\.claude\skills\terminal-upload\SKILL.md` on the terminal
  machine — self-contained, so ANY Claude session there (no repo checkout, no fabric
  context, e.g. Alyssa's) can run it. `bloomberg` + `opal` MCPs are USER-level on that box
  (verified), so the skill resolves outside the repo. Both copies carry a SYNC RULE
  tripwire; **the home copy is NOT in git — the main fabric cannot see its state.**

## Backend records every run leaves (the queryable trail)

Same wire path as the UI — uploads to `s3://opal-data-portal-v2/uploads/` + `manifest.json`
-> `yang-pipeline-trigger` -> `YangDataPipeline` Step Function -> `Generate*` lambdas ->
served JSONs. Query points, in triage order:

1. **Step Function executions**: `aws stepfunctions list-executions --state-machine-arn
   arn:aws:states:us-east-1:313476888478:stateMachine:YangDataPipeline` — names like
   `20260803_v1-<id>`; `describe-execution` input carries the manifest content (which files,
   which as-of date). NOTE the pagination trap: `--query 'length(...)'` counts a PAGE.
2. **MCP audit lake** (`s3://opal-mcp-audit`): every `opal_data_refresh_upload` call is
   audited — **this is the discriminator between agent-initiated and UI-initiated uploads**
   (the wire path is identical; the audit entry is not).
3. **S3 object versions** on the served keys (`json/benchmarks/model_portfolio_benchmarks.json`
   etc. — versioning ENABLED): every publish is a version with `data_as_of`/`generated_at`
   in the body. The instrument that unwound the 08-03 incident.
4. **DataRefresh status endpoint** (`data_refresh` Lambda `handle_status`) — with the W3
   caveat until it ships: Pass/Skip states are structurally invisible in its history view.
5. **Agent-side**: the skill mandates a fixed end-of-run report (PREFLIGHT/PULL/TRIPWIRE/
   UPLOAD/SERVED) in the session transcript; tripwire FAILs are reported verbatim.

## Failure classes to watch (each with its existing control)

| Class | Looks like | Control in place |
|---|---|---|
| Upload without a tripwire PASS | upload record with no PASS in the invoking transcript | skill hard-rule: FAIL = nothing sent, no override; audit lake shows the call |
| Month-end duplicate rows (the 07-31 class) | `cannot reindex on an axis with duplicate labels` in the SFN execution | notebook guard (Yang, 08-03 13:08Z) + tripwire dup check + skill stop-and-escalate; >=7 months of prior vintages carried it silently (Dec/Mar censuses in the W4 trace doc) |
| Wrong-instrument custom-index resolution (the 0730 class) | plausible pipeline SUCCESS, garbage model row (e.g. ST 1D +2.22 / vol ~20) | root-fixed 08-03 (deprecated `.ST` deleted from BBG); skill carries the shape as a stop signature; `PARSEKYABLE_DES` pin remap table in the trace doc if it ever recurs |
| Bloomberg account review | `-4003 LIMIT/REVIEW "Access pending review [nid:...]"` at pull time | skill: stop + escalate, no retry-hammer (retries deepen the review) |
| Backward/duplicate re-upload | operator re-runs while another upload is in flight | W2 monotonic publish guard (deployed 08-03) rejects backward writes loudly; same-date re-send idempotent |
| Skill-copy drift | home copy behavior diverges from canonical | SYNC RULE line in both copies; home copy is device-local and unversioned — treat "which copy ran?" as a real triage question |
| dry-run residue | files accumulating under pending/ | harmless by design (no trigger); worth knowing they're expected |

## Reference chain

- Incident + mechanisms: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/MDLP_MONPUB_W4/TRACE_0730_WRONG_INSTRUMENT.md`
  (with addendum + closing update) and the MDLP_MONPUB records (spec, W1-W4 TOs, CVO
  validation log).
- Dedup + interval-verification instruments: `deliverables/MDLP_MONPUB_W4/{dedup_0731.py, interval_compare.py}`.
- The wrapped process itself: `tools/run_daily_pull.py` + `tools/bbg_pkl_tripwire.py` in the
  OneDrive project (`...\202511 Model Portfolio Exposure\`); human-flow doc `tools/BBG_DAILY_SKILL.md`.
- This briefing exists per Andrew-direct 2026-08-03 (~17:4xZ, site-Z terminal): the fabric
  gets the heads-up BEFORE an issue, and this file is the thing to cite when one arises.
