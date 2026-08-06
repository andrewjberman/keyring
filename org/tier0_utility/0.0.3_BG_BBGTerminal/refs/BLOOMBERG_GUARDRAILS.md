# BLOOMBERG GUARDRAILS — view, never download

Andrew-direct 2026-08-06: the agent *"can view bloomberg but cant do downloads; keeps us in
check with our data quota."* This file draws that line concretely. When you decline, quote
the WHY: **Bloomberg data-license quotas are consumed by downloads/exports, and a quota
breach is a real-money, hard-to-reverse event. Viewing is metered differently; that is the
side we stay on.**

## FREE (view-side — serve these)

- Screen reads: looking at a function/screen and describing what it shows.
- Single-security quote lookups through the DAPI paths the daily pipeline already uses.
- Answering from data ALREADY PULLED by the scheduled daily pipeline (the PKLs / the
  served portal artifacts) — that quota was already spent by the schedule; re-reading the
  artifact costs nothing. **This is the preferred path for almost every Teams question:
  answer from the SERVED data, not from a fresh terminal pull.**
- `bloomberg_health` and connectivity checks.

## DENIED (download-side — decline, every time, regardless of who asks)

- Any export: Excel add-in style pulls, `{FILE}`-class retrievals, screen exports,
  "can you pull the full history of X" bulk requests.
- Bulk/historical series requests that would fire fresh terminal data pulls outside the
  scheduled daily job — even small ones; ad-hoc pulls are how quotas die by a thousand cuts.
- Adding securities/fields to the SCHEDULED pull. That changes standing quota consumption
  and is Andrew's call alone — route the request to him with the demand noted.
- Anything you cannot confidently classify as view-side. **Unclassifiable = download-side
  until Andrew says otherwise.** Ask him; the budget for asking is unlimited, the budget
  for guessing is zero.

## The tie-breaker question

Before any Bloomberg-touching action, ask: *"does this cause the terminal/DAPI to deliver
data that was not already delivered?"* If yes or unsure → it is a download → denied.
If it re-reads what a scheduled job already delivered → free.

## Escalate-with-demand

Every denied download request gets logged (your session log) and the DEMAND surfaced to
Andrew — "three people asked for ad-hoc history pulls this week" is exactly the signal he
wants for deciding whether to expand the scheduled pull. Declining silently wastes the signal.
