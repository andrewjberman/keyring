# Session log — 0.4.0_DS_ClientPlatform — 2026-06-12 (~1652Z–1658Z)

**archetype:** TRACE
**secondary_archetypes:** DIAGNOSE

**Agent:** 0.4.0_DS_ClientPlatform (Tier-2 worker, event-driven)
**Driver:** 2.0.0_SA_COO (D7-FIX.T4 dispatch — D7 real_bug candidate #4).
**Theme:** Read-only attribution investigation — does D_04::build_firm_mix_summary() produce the BD per-advisor platinum artifacts comp-platinum prefix-matched to it?

---

## NFRA_GRAPHS.D7-FIX.T4 — BD per-advisor platinum artifact attribution (COMPLETE, verdict-only)

comp-platinum prefix-matched `platinum/advisors/{id}/{nna_clients,exec_summary,timeseries}.json` to `D_04::build_firm_mix_summary()`. Investigated the real producers.

**VERDICT: prefix-match WRONG for all 3, two distinct ways.** `build_firm_mix_summary()` actually writes ONLY `platinum/firm/mix_summary.json` (L383/482) — never a per-advisor key.

1. **nna_clients.json** — D_04 IS producer via `build_advisor_nna_clients()` (def L2524, write L2653). Right script, WRONG function.
2. **timeseries.json** — D_04 IS producer via `build_advisor_summaries()` (def L490, write L687). Right script, WRONG function.
3. **exec_summary.json** — NOT produced by D_04 (only a stale-cleanup comment L708). Real producer = the **`exec_summary_generator` Lambda** (`aws_lambda_function.exec_summary_generator`, `infra/aws/lambda/exec-summary-generator/exec_summary/`, source-map L1786): a nightly batch that reads `platinum/advisors/{id}/summary.json` and writes `exec_summary.json` (template_library.pyc references the summary key; portal `advisor-intelligence.ts:1352` comment confirms "nightly batch artifact"). WRONG SCRIPT entirely — a Lambda, not the gold tree. Genuine producer-graph gap.

**Root cause:** comp-platinum resolves `platinum/advisors/{id}/*` by PREFIX to the earliest D_04 function writing any `platinum/advisors/` key, not by full key → actual writer; and its producer graph has no Lambdas, so a Lambda-produced platinum artifact (exec_summary.json) falls onto a prefix-sharing gold script.

**Recommendation (for a comp-platinum fix TO if COO wants one):** (a) resolve producers by full-key match not prefix; (b) ingest Lambda producers into the platinum producer graph. Watch-targets: nna_clients/timeseries/summary/mix/positions = D_04; exec_summary = exec_summary_generator Lambda. Also flagged: the exec_summary Lambda .py source is absent from the working tree (only __pycache__) — possible separate source-hygiene gap.

---

## Compiler Tools
| Tool / run | Where | Result |
|---|---|---|
| grep attribution trace | D_04 items.append targets + all-gold nna_clients/exec_summary writers | mapped every per-advisor platinum key to its real writer; isolated build_firm_mix_summary's actual output (firm/mix_summary.json only). |
| lambda-source-map.json lookup | exec_summary | confirmed exec_summary.json producer = aws_lambda_function.exec_summary_generator (not a gold script). |
| S3 list + .pyc strings | opal-data-bd platinum/advisors/{abby_horton}/ + template_library.pyc | confirmed the 6 per-advisor artifacts exist; bytecode confirms the Lambda reads summary.json. |
| portal consumer grep | advisor-intelligence.ts:1352 | confirms exec_summary.json is a "nightly batch artifact" (Lambda-produced). |
(comp-platinum itself is the subject under test — the investigation diagnoses its prefix-match resolution; no comp-platinum run needed beyond reading its claimed attribution from the TO.)

## Commits
TO flip + this log. No code changes (read-only investigation per TO scope).
