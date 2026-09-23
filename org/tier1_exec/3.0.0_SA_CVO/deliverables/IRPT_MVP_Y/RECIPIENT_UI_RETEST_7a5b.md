# Y-UI01 independent repair retest

Reviewer `3.0.0_SA_CVO~Y`, 2026-09-23 UTC. Authority:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact repaired portal: `7a5b24e705f79d5df872f9a443b6a552e9de62b9`.

**Y-UI01 CLOSED for this exact candidate.** Original independent
`probe_recipient_ui.test.ts` unchanged from failure review
`c387a06e2d3e71d9d4dabb35bfddf92ad8249824`: **9 PASS,48 assertions**.
Focused supplied suite **31 PASS,177 assertions**; explicit application
`tsc -p tsconfig.app.json --noEmit` passes.

The same actual handlers submit Recipient A, edit/submit B, then resolve B and A
in that order. Recipient remains B and visible status stays
`Queued -- areq-51cd82fb`; A no longer overwrites it. The original final negative
assertion now executes, explaining48 assertions versus47 in the failed run.
Exact retry/new-recipient body semantics, prospect reset/pending guard, hostile
input static markup, Unicode guards and LiveClient body controls remain passing.

The inspected change requires both latest submission sequence and current
composition before setting a result. Visible job also requires matching current
inputs. No implementation edits were made by the reviewer. The producer's
reported working-tree retest was not used as independent closure evidence.

`RECIPIENT_UI_RETEST_7a5b24e7.json` preserves observations;
`RECIPIENT_UI_RETEST_7a5b24e7_VALIDATION.json` preserves exact source hashes and
all test/typecheck outputs. `run_recipient_ui_review.py` now accepts candidate
and output-stem environment bindings; the original candidate defaults and
original failure files remain unchanged. Reproduce with:

```powershell
$env:IRPT_RECIPIENT_UI_CANDIDATE='7a5b24e7'
$env:IRPT_RECIPIENT_UI_STEM='RECIPIENT_UI_RETEST_7a5b24e7'
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/run_recipient_ui_review.py
```

Scope remains actual components/manual React hooks/static markup and offline
transport, not a real browser or backend/vendor/cover/render/export grade.
Acceptance/replay5a2b has its separate service review. All14 integrated criteria
remain **0 PASS /0 FAIL /14 NOT_EVALUATED**. Push state LOCAL.
