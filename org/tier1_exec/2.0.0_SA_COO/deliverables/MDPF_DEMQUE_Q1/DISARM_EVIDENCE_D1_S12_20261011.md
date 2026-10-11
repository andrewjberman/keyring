# Disarm evidence: MDPF_DEMQUE-D1-S12 (BLOCKING, INERT) -- `2.0.0_SA_COO~Q1`, 2026-10-11 ~17:2xZ

**Row:** `MDPF_DEMQUE-D1-S12` (`org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md`): FTHSX and PFORX
held by 4 and 11 accounts in `silver/positions` `date=2026-06-23`; whether a client page values them through the Yahoo price files was not traced.

## The act that answers it

TO-DQ-t35 (`0.9.0_WK_MDPF_DEMQUE~27`, merged `9ae2f2d054`, proof VALID, AC2 judgment for the CVO):
`org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~27/VALUATION_TRACE.md` and `.json`.

## Measured (read from the artifacts, re-read here for the figures)

- The production gold run reads and writes `opal-data-cot` (`BD_S3_BUCKET`, SSM `opal-cot-gold-run`, `infra/aws/terraform/cot-pipeline/ssm.tf`
  L304-331). In that bucket `silver/historical_prices.parquet` and `config/ticker_lookup.json` are absent (404), so the canonical price build
  skips its Yahoo tier; the five names of these two families carry no Yahoo row.
- The value a client page shows for a position comes from `gold/canonical/holdings/<date>.parquet` (B_00): price = BD market value / units
  (`bd_snapshot`). FTHSX is held in 188 current accounts at about 57.6, PFORX in 334 at about 9.45. That is not the Yahoo file.
- The 15 June positions have no applied account link: none of the 15 numbers is MATCHED or LINKED; two are AWAITING_PERSON near matches
  (0.765). No served household artifact names the three CUSIPs.
- Re-resolve through the existing resolvers: FTHSX none, RPIFX none, PFORX candidates PFBPX 42.9, PFONX 42.5, PFUIX 0.0 (a name-stem match, not a
  resolver output). None reaches 90.

## Ruling applied

CTO ADDENDUM 4 (msg 4020): disarm to "no client page reads the file"; nothing goes to Andrew; the three funds stay unresolved (already on the
FWD-5 list, reason `REJECTED:LOW_TRADE_AGREEMENT`, open since 2016-07-15 / 2017-07-14); the comparability question is row D1-S13.

## What this does not do

This seat does not write the clock: `disarm.state` ARMED/BLOCKING -> DISARMED is the CVO's. Residual, named: the trace is of the production chain
as deployed on 2026-10-11; a chain that landed `silver/historical_prices.parquet` (FWD-1's last hop, round 10 cell 1) would put these three
names' files in the page's input, and then `held`/unresolved handling is what stands between them and a page.
