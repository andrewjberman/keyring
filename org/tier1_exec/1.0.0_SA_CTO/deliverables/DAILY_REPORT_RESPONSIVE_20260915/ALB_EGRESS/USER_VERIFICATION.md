# Real sign-in verification

Andrew was prompted after the approved ALB rule was applied and its live state and scoped zero-diff re-plan were verified:

> After opening https://mcp.opalinvest.dev/sprint fresh and signing in, does the report load?

Andrew answered in this exact Codex session on 2026-09-15:

> Report loads

This confirms the real user report-visible portion of the EXERCISED condition. It is not a local browser stub or an unauthenticated redirect check. CloudWatch authentication success and ALB callback evidence are recorded separately in `POST_APPLY_OBSERVATION.json` before closing the remaining verification leg.
