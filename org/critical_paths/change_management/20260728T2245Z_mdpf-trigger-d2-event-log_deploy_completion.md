# Deploy: mdpf-trigger-d2-event-log

**Opened:** 2026-07-28T22:45Z by 0.7.0_AE_CloudOps
**Authority:** CTO 223414Z time-critical insert (D2 / PIN-4, CVO certification pins @d75f736c53) under MDPF_RESET_DIRECTIVE_20260728T2220Z.
**Change:** one self-log line in `mdpf-daily-trigger.lambda_handler` printing the incoming
event payload (`print(f"Event: {json.dumps(event)}")` + rationale comment), copied from the
working estate precedent `inf-portal-publisher/lambda_function.py:919`. No behavior change.

**Why tonight:** CloudTrail has ZERO Lambda data events on both trails, so a scheduled fire
and a hand-run are indistinguishable unless the function logs its own trigger identity.
Tomorrow's ~13:30Z floor / ~15:00Z accelerator fires are the D2 evidence and happen once.

**Legs:** L1 commit (safe-commit, this file + ledger + lambda source) ->
L2 build-and-upload + TARGETED safe-apply `module.mdpf_daily_trigger` (mdpf-pipeline tree
otherwise frozen; scheduled-floor row 10 must not ride) -> 0-diff -> tag.

## Completion

(open)
