# ANDREW-DIRECT — DS agents get resource deployment ability

**Channel:** Andrew-direct, 0.2.0_DS_PortfolioAnalytics terminal, 2026-08-04 ~18:4xZ, immediately
after the acct-dist heal report (the 3rd committed-but-never-deployed gap in one day).
**VERBATIM:**

> "We need to give DS agents resource deployment ability because this cannot keep happening.
> If you are editing these scripts you need to be able to deploy them so we do not keep
> ending up in this situation."

**Scope as received (surface, not adjudicate):** DS agents who edit scripts must be ABLE to
deploy them — the edit-without-deploy split is the named failure class ("this cannot keep
happening" = today's three instances: trio MISSING_ON_S3, EMIT-1 wiring, the acct-dist 12-day
stale builder).

**Context the executor must ground:** Rule 13 already grants DS the commit→QA-deploy cycle for
`data/*/scripts/{gold,silver,bronze}/*.py` — so the instruction implies the grant is INCOMPLETE
in practice (tree coverage / tooling / doctrine-belief). The mechanism hunt starts at
`.tools/safe_deploy_core.py` PIPELINE_MAP ("bd/inf/cot; mdpf check-only" per the rule text).

**Broadcast:** COO + CTO + MSTR, same turn (this file committed alongside).
