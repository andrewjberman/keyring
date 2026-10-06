# ANDREW-DIRECT 2026-10-06 ~23:13Z -- re-run the new data so the "Index" view displays properly

Given at the `0.0.0_AB_MSTR~Z` terminal (site Z), in-session, ~23:13Z (7:13 PM ET).

## Verbatim

Andrew: "i already brought mcp back for opal-gateway-bbg. now however what I want to do is try to rerun the new data so
at least we can have the "Index" view displaying properly"

## State when he said it

- `0.0.3_BG_BBGTerminal` had re-pulled the 2026-10-05 vintage fresh (record `..._2255Z_SURE_JUST_OVERWRITE_THEM...`).
  The four index CIX series (.INT_BMK .LT_BMK .ST_BMK .UST_BMK) now run to 2026-10-05; .LT_ETF .ST_ETF .UST_ETF still
  stop at 2026-09-29.
- The gateway send (`opal_data_refresh_upload`) returned `portal login 403` for three callers, and again on a dry run
  after his re-auth of `opal-gateway-bbg`. Cause found by the laptop `1.0.0_SA_CTO` (bus cea4ec6a): the gateway's
  `opal_portal/integration.py:65` logs in to the raw API Gateway host, which now refuses. That needs a gateway deploy.

## Act taken on it

Relayed verbatim to `0.0.3_BG_BBGTerminal` (msg delivered 23:14:32Z) with the route: the scheduled pipeline's own
publish leg, `publish_to_portal.py` under `%PY_AWS%` (`scheduled_daily_pull.cmd` lines 180-189), which writes S3
directly and does not use the gateway. Publish leg only; no re-pull and no other legs.

## Correction

My relay to BG dated his word "~23:2xZ"; it was ~23:13Z.

## Scope as read (surfaced, not adjudicated)

- "Rerun the new data" is read as: publish the fresh 2026-10-05 pull so the portal serves it. It is not read as a word
  on the integrate, the gateway deploy, or the ETF CIX series.
