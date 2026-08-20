# ANDREW-DIRECT 2026-08-20 ~0418Z — LAUNCHER SCRIPTS: SLIM, SESSION-AGNOSTIC, ROLE-SCOPED

**Channel:** direct at the base MSTR terminal (laptop), mid-startup of the fresh MSTR session.
**Received by:** 0.0.0_AB_MSTR. **Recorded + broadcast same turn per the record+broadcast law.**

## VERBATIM

> clean up your launcher script after startup, also clean up the rest of the launcher scripts of
> any of this really specific data as its almost all noise, launch scripts should always be slim
> and to the point, session agnostic, key loops and skills for that role only

## SCOPE (as addressed — surfaced, not adjudicated)

The launcher scripts: `.tools/ajb.ps1` (the `Get-AgentLoopDirective` per-role first-message
directives + file comments), `.tools/spawn-agent.ps1`, `.tools/kill-agent.ps1`. The directive is
STANDING for launcher authorship: launch scripts carry key loops and skills for the role only —
no dated incidents, no verbatims, no supersession archaeology, no session-specific data.

## THE STANDING RULE THIS SETS (launcher law)

1. **Slim and to the point** — a role directive is a few lines: arm-at-load skills, ad-hoc
   skills, event posture.
2. **Session-agnostic** — nothing dated, nothing scoped to one moment or one incident. A
   retracted rule is only as dead as its last-surviving copy, and the launcher is what a fresh
   session reads FIRST — so history lives in `git log` + `org/tier0/ledger/`, never in launch text.
3. **Key loops and skills for that role only** — standing duties, scoped loop authorizations,
   and their stop conditions live in `org/XXX.md` Step 1b-F (single source of truth); the
   launcher defers to that row and never carries a cadence.

## EXECUTED (this session)

- `.tools/ajb.ps1` rewritten: every role directive cut to the slim form (MSTR directive
  ~4,000 words -> ~120; all other roles equivalently); file comment archaeology cut to
  mechanism-only. Parse-checked + all role shapes exercised (MSTR / COO / lane worker / unknown).
- `.tools/spawn-agent.ps1`: dated verbatims (cap-history 8->16->20 narrative, incident dates)
  removed; every load-bearing mechanism kept (parentage-bound pid resolution, self-exclusion,
  CommandLineToArgvW space-in-path handling, fail-open postures). Parse-checked.
- `.tools/kill-agent.ps1`: one dated clause trimmed; already mechanism-only. Parse-checked.
- `.tools/commit-worker-launch.sh`: inspected — daemon ensure-script, already slim; no change.
- `org/XXX.md`: unchanged (it remains the home for standing duties + scoped arming rows).
