# ANDREW-DIRECT 2026-10-09 ~04:3xZ -- pushes do not need him (one exception); and the CTO self-drive covers them (ARMING RECORD)

**Channel:** the `1.0.0_SA_CTO~Z` terminal, site Z. Recorded the same turn by `1.0.0_SA_CTO~Z`.

## His words, VERBATIM

> "Do you have self-drive running? Pushes should not require me. The only Push that requires my express approval is any push to
> portal PROD that touches anything that clients see. Therefore if its just edits to Security Analysis page, or Investor
> Reporting, or Freshness, or etc., then pushes to PROD are fine for portal (as these pages are all opal-internal). Other than
> that, You should never ask me about pushes, that should entirely be covered between the CTO self-drive and the MSTR govern
> loops."

## What it rules

1. **Pushes need no word from Andrew,** except ONE class: a push to portal PROD that touches anything clients see. A portal PROD
   push that touches only Opal-internal pages (his examples: Security Analysis, Investor Reporting, Freshness) is "fine". Every
   other push (DEV, opal_ai, mcportal, workspace branches) is settled between the CTO's self-drive and the MSTR's /govern. It is
   never asked of him.
2. **Consequence, executed the same turn:** the held call `sitez-20261009T041311Z-0266` (push opal_ai DEV and PROD,
   de5ce25fa3 -> 8cdc7b9735) is CLOSED on this word, and `0.0.0_AB_MSTR~Z` pushes it.
3. **Never-widen still binds a push that moves served output** (CLAUDE.md NEVER-1: CTO and COO halves). His word removes HIS
   approval from a push; it does not remove the pair. A client-facing portal PROD push needs both the pair and his express
   approval.
4. His question presumes a running CTO self-drive. The previous loop stopped at ~02:0xZ when its five projects moved to DELL1
   (its arming record carries the stop). **This record re-arms it** over the site-Z fabric that remains.

## ARM TERMS

| term | value |
|---|---|
| scope | the live site-Z projects whose CTO is this seat: NFRA_SPRINTWIN, NFRA_IAMROLES202609, NFRA_OPSEC202609, NFRA_REPORT, NFRA_MCPMSP, NFRA_MCPORTAL, NFRA_OPALAI, NFRA_MCPINDEX (8, read from tree rows `fabric: site-z` at 04:3xZ). NOT NFRA_OPLGTW, which `1.0.0_SA_CTO~O` drives |
| cadence | 60m |
| call routing | `/self-drive` Step 1: this seat rules every call; design forks to `4.0.0_SA_CRO~Z`, governance forks to `3.0.0_SA_CVO~Z`; pushes per item 1 above |
| acts listed for Andrew | only those Step 1 cites, plus item 1's one class: a client-facing portal PROD push |
| paired_with | the site-Z COOs' own `/canonical-drive` loops (`~AI`, `~MP`, `~MI`, `~MS`); `0.0.0_AB_MSTR~Z` `/govern` carries the pushes |
| stop | DONE read from the register for all eight, HELD-AT-STOP, or his stand-down |

-- 1.0.0_SA_CTO~Z

## ADDENDUM, ~04:4xZ, same terminal, VERBATIM

> "yes also make sure that all COOs are running /canonical-drive on their attached projects."

Executed: `2.0.0_SA_COO~AI` (cron 102d96c4), `~MP` (620d0d66), `~O` (c8b9b42b) and `~MI` (e822f7e3) report `/canonical-drive` armed on their
projects (msgs 32392, 32393, 32394, 32396). `0.0.0_AB_MSTR~Z` is asked to seat `~MS` (NFRA_MCPMSP), `~ZI` (NFRA_IAMROLES202609), `~ZZ` (NFRA_REPORT)
and a new lane for NFRA_SPRINTWIN (NEEDS-SLOT), each to run `/canonical-drive` (msg 04:50:36Z). Cron of this loop: `6403bef8`, hourly at :23.

-- 1.0.0_SA_CTO~Z
