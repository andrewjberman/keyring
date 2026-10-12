# One test ticket filed in tenant cottonwood — 0.7.0_AE_CloudOps~TV2

**archetype:** IMPLEMENT

**Date:** 2026-10-12
**Task Order:** TCKT_VNEXT.TO-APPLY-R12-tk1.one-test-ticket-in-cottonwood-dell2
**Status:** COMPLETE. One create, 201, AC1 PASS. Nothing deleted, no token printed.

---

## Result

Ticket **TCK-20261012-13cd3a1d**, created by `svc-commentary` through `POST /api/scoped/tickets`, one call.

Read back with one `get-item`: tenant `cottonwood`, type `analysis_request`, status `open`, created_by
`svc-commentary`, title begins `[TEST TCKT_VNEXT R12] `. It carries **no** `draft_commentary` and **no**
`report_ref`, as the order required. The route accepted a body with neither, so the order's STOP (a refusal for a
missing draft) did not arise.

## Pre-read (step 1)

- Positive control: TCK-20261009-a1052909 reads `open`, `analysis_request`, `svc-commentary`, firm `cottonwood`.
- `opal-ticket-api` environment: `COMMENTARY_ALLOWED_FIRMS` = `49financial,cottonwood,inflection`; CodeSha256
  `4sDK8P5m...`, LastModified 2026-10-12T01:50:30Z (the round-9 build).

## Method and handling

- Body: the order's list only. `answers` = advisor (synthetic), firm, report_type, add_commentary; no household key.
  Attachment is a synthetic pointer (`test-r12-tk1-20261012`, `portfolio_` + sha256 of a TEST label).
- The script (`deliverables/r12_tk1/r12_tk1_create.py`) reads the token from the secret into memory, sends it as a
  Bearer header, and never prints it. It prints no raw response, because the response carries routing addresses;
  it extracts `ticket_id` and read-back fields only. A `--dry` run printed the body first, no network.
- The result file holds no at-sign (the script asserts it before writing).
- Known side effect, unchanged by this order: a CREATE fires the distribution-list notice, which carries no draft text.

## Not done, by the order

No retry, no second create, no delete (a ticket has no delete route and the ruling forbids one here), no ledger entry
(a data write, not a deploy), no surprise row (nothing odd was found). Closing the ticket is a human act on the board.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `.tools/aws` dynamodb get-item | earlier ticket; new ticket | open / read back as above |
| `.tools/aws` lambda get-function-configuration | `opal-ticket-api` | allowed-firms list contains cottonwood |
| `r12_tk1_create.py` | `--dry`, then the one write | 201, TCK-20261012-13cd3a1d |
| `r12_tk1_ticket.py` (issuer's AC1) | as written in the order | `TK1-OK TCK-20261012-13cd3a1d firm=cottonwood status=open created_by=svc-commentary` |

Gap: the skill file `/watcher` hardcodes a `Users/AndrewBerman/Desktop` path; on this box the workspace is
`C:/dev/ajb_workspace`, so I armed the monitor with `/c/dev/ajb_workspace/...` instead.
