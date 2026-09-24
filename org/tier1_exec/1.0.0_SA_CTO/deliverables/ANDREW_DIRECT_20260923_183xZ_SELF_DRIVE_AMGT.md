# ANDREW-DIRECT -- `/self-drive AMGT`, arming record

**2026-09-23 ~18:3xZ, `1.0.0_SA_CTO~Z` terminal, site Z.** Committed BEFORE tick 1 per skill 0.5.

## HIS WORDS, VERBATIM

> *"I need you to /self-drive AMGT to completion, where completion is testing frontend
> (localhost:5174) and actually displaying relevant data for a security end to end on all
> functions."*

> *"You should be handling these /open-calls , follow /self-drive format and keep your fabric driving
> to completion"*

## ARM TERMS

| | |
|---|---|
| **scope** | `AMGT` -> 3 projects: `AMGT_RESAPP`, `AMGT_HARVST`, `AMGT_CORPUS` (3 of 374 project JSONs) |
| **device** | `sitez` (derived, `agentbus-sqs.sh device`) -- no cross-fabric work |
| **cadence** | operator-driven; this seat drives continuously while the terminal is live |
| **paired_with** | `solo` -- the three COO lanes are CODEX CLOSERS under closer mode, not `/drive` halves |
| ⛔ **COMPLETION TEST -- HIS, AND IT SUPERSEDES THE SKILL's REGISTER-READ DEFAULT** | **the frontend at `localhost:5174` ACTUALLY DISPLAYS RELEVANT DATA FOR A SECURITY, END TO END, ON ALL FUNCTIONS** |
| **stop-condition** | that test passing, or his stand-down word |

⭐ **Why his test supersedes skill §4:** §4 reads DONE from `status: complete` in the register. **He
has named an EXERCISED end-to-end test instead.** That is strictly stronger -- a project can read
`complete` with nothing rendering -- and it is his word, so it binds. **The register read is still
printed each tick as a secondary denominator, never as the stop.**

## REGISTER STATE AT ARM

**All three AMGT projects read `status: active`. 0 of 3 complete.** `AMGT_RESAPP.blocking` carries
*"ROUND 35 (regulator route, HKEX): the L4-R BRIEF half is STALE at PRD..."*.

## ⛔ TWO BLOCKERS ON HIS TEST, MEASURED AT ARM TIME

**1. THE PORT IS AMBIGUOUS ACROSS THREE SOURCES -- and testing the wrong one is a wrong-object error
on the acceptance test itself.**

| source | port |
|---|---|
| **Andrew, this instruction** | **5174** |
| `portal/vite.config.ts:40` | *"Port 5173 discipline: Always use this port, never allow fallback"* (a COMMENT; no `port:` key found in the server block) |
| `CLAUDE.md` Portal section | `bun run dev --port 5175` |

⚠ **Measured now: NOTHING is listening on 5174 or 5175.** The frontend is not running at all.

**2. ⛔⛔ THERE IS NO `/api/scoped/amgt` PROXY IN THE DEV SERVER. `amgt` occurrences in
`portal/vite.config.ts`: ZERO.**

Seven `scoped` proxy entries exist -- `advisor-intelligence` (`:102`), `satellites` (`:124`),
`partners` (`:142`), `data-refresh` (`:169`), `security-scanner` (`:188`) -- **and none is `amgt`.**

⛔ **CONSEQUENCE: a page calling `/api/scoped/amgt/*` from localhost has no proxy, so the request
never reaches CloudFront and no data can render, on ANY port.** ⚠ **And the config records that since
workspace `7abe7552b5` (2026-09-03) the portal authorizer REFUSES any request lacking CloudFront's
`X-Opal-Origin-Verify` header -- so direct-to-API from localhost is not a workaround; the proxy is
the only route.**

⭐ **`rk-123` added the CloudFront behavior for `/api/scoped/amgt/*` -- that is the PROD path, and it
is confirmed landed and held. The DEV proxy entry was never added beside it.**

## WHAT THIS RECORD DOES NOT DO

⛔ It authorizes no deploy, no cutover, no vendor call, no S3 write, and no lane grant. **The
served-output incident's never-widen pair remains unsigned and its deploy remains blocked** -- and
that incident is now ON the critical path to his test, since the page he wants to render is served by
the API currently serving 179 sentences the ratified clause withholds.

-- `1.0.0_SA_CTO~Z`. Commits LOCAL; push owed by `0.0.0_AB_MSTR~Z`.
