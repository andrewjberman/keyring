# 0.5.0_AE_OpalETL~Z — D7 TO-F half (b): the write path (1428–1450Z)
**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE (Phase-1 existence census), VALIDATE (authz battery + mutant), COORDINATE

**Lane:** `~Z` (site Z). Logged in the BASE agent folder, lane-prefixed.

## What happened
- 14:28Z CTO~Z [ROUTING 2336] under Andrew-direct *"proceed those projects to completion"*: TO-F split by HALF — **(b) the write path → me NOW**; (a) form + proof + portal-side exercise → DE~Z (LIVE pid 31384 per COO~Z tick-2). ACK'd same turn; Phase-1 existence checks run + recorded (comp-routes behaviors: the submit path is COVERED by CF behavior 12 `/api/scoped/tickets/*` → no CF change; trace TicketCenter; comp-iam FLOOR 12 DDB calls, action set unchanged, grant `main.tf:98-116` covers it → no new IAM/secret; comp-cache none; schema-check baseline WARN; **`comp-blast create_ticket` TIMED OUT at 3 min** — tool hazard, named). Design reads: the authorizer's context fields (`portal-authorizer/index.mjs:194-210`), D8's internality predicate (`firmId == 'opal-capital'`), U4's five constraints, the trade-workflow-handler SoD pattern.
- **LANDED @4bede18189** — `opal-ticket-api` rewritten around the §7.3.2 per-action deny-by-default matrix AS AMENDED (@1d524d06ca + @2cb58ecf22): server-derived principal classes (internal-human / client-human / svc-ticket-form / svc-analyst-intake by `sub`+`userType=="service"` / unresolvable→403), `POST /api/scoped/tickets/submit` (client session authenticated by the existing authorizer; body keys limited to `{ticket_type,title,description}` — anything else 400; requester/firm from the context; written UNDER `svc-ticket-form` with `source=dashboard_form:<firm>` + a `created` event), CREATE hardened (created_by = token subject; requester_firm only inside allowedFirmIds; `dashboard_form:*` reserved), SoD on claim/complete; TF `ticket_routes.submit` pure-add; 11-test authz battery on the REAL handler incl. the D7F-9 in-process mutant → **11/11 OK**; commit-gate clean. Record + **laptop apply request** (build-and-upload → safe-apply → 0-diff → tag → source-map → deployed-bytes sha check → the §7.3.4/D7F-5..10 exercise rows) authored; ferried via MSTR~Z to 0.7.0_AE_CloudOps; the submit contract sent to DE~Z.
- Also this window: v0.3 TO STAGED read (GO at the v0.2 port landing); two law-edit broadcasts READ-acked (COO~Z scoped `/drive` re-arm; nothing for me to arm); MSTR~Z's A.2 watch line retired; COO~Z's [SYNC] honoured (broker summary → WORKING).

## Corrections (the honest column)
- The test file's first gate run failed ruff E702 (semicolon-joined statements) — split; my line-splitter also split a docstring sentence on `; ` — fixed by hand. The `python -m unittest infra.aws.lambda...` form in my first docstring cannot work (`lambda` is a keyword) — corrected to the by-path invocation.
- Behaviour change stated, not hidden: an internal human who files a ticket for themselves can no longer self-claim/self-complete it (SoD rule 1) — relaxable at one chokepoint if CTO~Z rules.

## Blockers
None I hold. The apply is the laptop's (0.7.0_AE_CloudOps via MSTR~Z's ferry); its CONFIRM = DE~Z's GO-to-exercise for D7F-3..10 + leg-3's D7F-3 first-PASS trigger. svc-subject rows (D7F-10) need TO-D's minted tokens.

## Compiler Tools
| Tool + command | Result | Note |
|---|---|---|
| `comp-routes behaviors` / `comp-routes trace TicketCenter` | behaviors 12+13 [AUTH]; trace = 5 board calls | submit path covered by 12 — no CF change |
| `comp-iam service opal-ticket-api` | 12 DDB calls [UNKNOWN] (role unmapped) — a FLOOR | action set unchanged; TF grant read at source |
| `comp-blast create_ticket` | **TIMED OUT 3 min** | named; consumers from trace + tickets.ts |
| `comp-cache map \| grep ticket` / `collisions` | none | |
| `comp-transform schema-check TicketCenter` | WARN no types.ts (baseline) | pre-existing |
| `.tools/commit-gate.sh` | clean ×2 | ruff E702 fixed first |
| authz battery (this seat's own, 11 tests, real handler + FakeTable) | 11/11 incl. the D7F-9 mutant flip | |
