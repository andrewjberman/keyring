# ANDREW-DIRECT 2026-10-09 ~03:2xZ (1.0.0_SA_CTO~O terminal, site Z) -- the Bloomberg account gets blackdiamond_list_fees

He gave this in-session at the `1.0.0_SA_CTO~O` terminal, after reading this seat's ruling that `opalbloomberg` gets four
tool rows in r29 and gets `blackdiamond_list_fees` only if the C2 data grant gates each fee read.

## His words, VERBATIM AND ENTIRE

> "yes, include blackdiamond_list_fees for the bloomberg account too"

## What it rules, at the width written

| Item | Reading |
|---|---|
| `infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt` | `opalbloomberg@opalinvest.com blackdiamond_list_fees` is added beside the four rows, in release r29 (OG-rl-15), citing this record. |
| This seat's condition (msg to 2.0.0_SA_COO~O, ~02:2xZ) | Superseded. The row goes in whether or not C2 gates the fee read. |
| NFRA_OPLGTW PRD v2.2 | Item 5 already lists the five tools. Item 2's "no data grant for opalbloomberg" stands for Schwab and Black Diamond account data. This one tool's fee read is admitted by his word. |

## Not said

- No Schwab or Black Diamond account-data grant for `opalbloomberg` beyond this tool.
- Nothing else about r29's terms.
