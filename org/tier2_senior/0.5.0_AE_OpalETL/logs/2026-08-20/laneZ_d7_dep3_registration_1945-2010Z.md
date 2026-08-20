# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-20 1945–2010Z

**archetype:** IMPLEMENT
**Project:** D7 (Ticketing intake) — dep-3, the one-sitting registration act (TAC-3 shape A)

## Summary

**D7 dep-3 EXECUTED — TAC-3 schedule-landed claimed with evidence.** On MSTR~Z's dep-3 trigger
(token minted, secret name stable, LIST exercised PASS at the mint) I took the owner's call —
PROCEED on LIST+send; the CREATE hold is structurally irrelevant to the runner's action set —
and ran the sitting: grounding (COO~Z's DECISION block + PRD §7.3 amendments + the live estate:
API GW **7k3ed8px20** from the lambda's own resource policy; portal origin from the CF aliases;
table keys; secret exercised with the value never printed), then the build @399df8444a
(runner.py + runner_config.json + run_intake.cmd + register_intake_task.ps1), then the battery,
then registration, then the first real fire.

Design as landed: fetch under the svc token with client-side new-since-cursor (the ruled
no-since-param input); send via teams-watch's pinned selection **imported, not re-implemented**
(build ladder — one selection logic, one home), `confirm=true` always; cursor DURABLE OFF-BOX
in `opal-tickets` item `_CONFIG:intake-cursor` (statusless → invisible to every status-filtered
LIST; **ABSENT = refusal**, never a backlog blast — the registration act seeds it deliberately);
receipts on-box append-only; exit contract 0/2/3/4/5 with LastTaskResult as the ruled failure
surface (no monitor — moratorium).

## Evidence — exercised, not reasoned (rc unpiped throughout)

| Leg | Result |
|---|---|
| Harness (8/8) | config refuse exit-4 named · real config all-keys-set · **pinned identity LIVE, verified `opalbloomberg@opalinvest.com` on this profile** · no-match pin exit-2 (real code path) · exit mapping 3/5/0 · real LIST 200 from this box |
| Framed zero | fetch returned 0 open — table scan: **9 items, ALL `completed`** — a true absence, not a broken filter |
| Real-process refusal | pre-seed `runner --dry-run` → exit 4 "cursor config item absent" |
| Seed | `_CONFIG:intake-cursor` put at 2026-08-20T19:58:18.200Z, read back |
| Real-process clean | post-seed dry-run AND bare production invocation both exit 0 |
| SEND_FAILED control | real `main()` + fixture form row + refusing send → **return 3**, cursor-advance assert armed, never tripped |
| Registration | `OPAL_D7_ticket_intake` state=Ready, 5-min 24x7, current-user Limited |
| **First real fire, seat DOWN** | lastRun 15:59:45 local, **LastTaskResult=0**, log: pass 1.3s, `INTAKE PASS OK fetched=0`; BG broker liveness at fire time: NOT REGISTERED — seat-down measured, not assumed |

Surface notes (named, not chased, in msg 2742): the unfiltered-scan board exposure of the
config item; the OAuth send-credential expiry → exit-2-until-next-session failure surface;
the runner as W-B's backstop substrate (Ticket Lifecycle v2 lands ON TOP, nothing changes here).

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-find` ×4 ("refuse-if-unset", "read_chat_messages" earlier, "config item", cf tf name) | Located the spec, the cursor-home clause, and the CF tf with denominators | PASS |
| `comp-routes api-routes` | 21 API GW routes, NO ticket routes in the DESIRED parse (laptop-applied outside parsed tf) — grounded the base instead from the lambda's LIVE resource policy | ROUTED, partial fit — live primitive closed it |
| Live AWS (operational) | sts identity, describe-table, describe-secret, GetSecretValue exercised, seed PutItem+GetItem round-trip | PASS |
| `.tools/commit-gate.sh` runner.py | py_compile + ruff clean | PASS |
| `safe-commit` + risk-reflex | @399df8444a; [RISK] was a filename-match on another tree's runner.py citing the commit-only-flag memory (laptop path, unresolvable here) — its substance (pathspec via safe-commit, no pre-add) is exactly what was done | PASS |

## Blockers

None I hold. TAC-3 schedule-landed claimed — validation COO~Z, acceptance CTO~Z (their reads).
TAC-2' (one real form row → buzz + link) fires at CTO~Z's routing; the schedule is live, so a
routed submission buzzes within 5 minutes with no act from me. W-B (stream accelerator) lands
on this substrate when COO~Z cuts it. The re-mint (CREATE spec gap) changes nothing here.
