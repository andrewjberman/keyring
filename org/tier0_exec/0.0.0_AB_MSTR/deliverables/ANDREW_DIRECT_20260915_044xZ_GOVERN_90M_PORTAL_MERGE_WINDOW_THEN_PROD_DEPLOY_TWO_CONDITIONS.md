# ANDREW-DIRECT 2026-09-15 ~04:4xZ -- /govern on 90m: find the portal-merge window, then a full /prod-deploy on two conditions

**Seat:** `0.0.0_AB_MSTR` (laptop) · **Channel:** typed at this terminal · **Recorded:** the same turn it was given.

## VERBATIM AND ENTIRE

> "I need you to run a /govern loop on a 90m interval and keep an eye on the fabric and coordinate when will be a good
> time to merge the portal. I suspect in one or two cycles from now there will be no more frontend work actively being
> done and that will be the time to figure it out. We are going to want to do a full /prod-deploy at that point once
> it's all sorted. The conditions for the prod-deploy are the following. 1.) The Cottonwood Satellite ingestion is
> completed and we are not displaying floating numbers or missing data in Characteristics/Performance in the "Holdings
> Breakdown" section. 2.) Investor Reporting must remain Opal Admin gated, no clients are allowed to see that."

## WHAT IT ARMS

- **A DIRECTED `/govern` loop at `0.0.0_AB_MSTR`, 90-minute cadence.** Scope: watch the fabric, and COORDINATE the portal
  merge window. The window is the point where no frontend work is actively in flight; he expects it one or two cycles
  out.
- **Stop condition:** the portal is merged and the `/prod-deploy` is done, or his stand-down.
- The cron id is session-local and is not recorded here (org/XXX.md Step 1b-F: `CronList` at the seat is the
  artifact).

## THE TWO PROD-DEPLOY CONDITIONS, AS HE SET THEM

1. **The Cottonwood Satellite ingestion is complete**, AND the "Holdings Breakdown" section shows NO floating numbers
   and NO missing data in Characteristics or Performance.
2. **Investor Reporting stays Opal Admin gated.** No client may see it.

## HOW THIS SEAT READS "COORDINATE", NARROWLY, AND SAYS SO

Each cycle measures the frontend-activity state and both conditions, prepares the ordered merge and deploy plan, and
brings the window to him. **The acts stay on his explicit word at that time:** the CLOUD push, the CLOUD<->SITEZ
merge, the portal DEV reconcile, lifting the portal freeze, and the `/prod-deploy`. That is his own ~02:4xZ word:
"ill let you know when to push + Call 4 Merge I will let you know as well". A wider reading is his to give.

`/prod-deploy` is a DT-only skill (its Step 0 halts every other seat). This seat cannot write a Tier-2 seat
(mstr-no-tier2-writes), so the deploy is routed through `1.0.0_SA_CTO` when the window comes.

## BROADCAST

`1.0.0_SA_CTO` (who lands the Step 1b-F row for a DIRECTED arm), the three COO lanes (the frontend work in flight is
theirs), and `0.0.0_AB_MSTR~Z` over the agentbus (the CLOUD<->SITEZ leg and the portal plan are joint).
