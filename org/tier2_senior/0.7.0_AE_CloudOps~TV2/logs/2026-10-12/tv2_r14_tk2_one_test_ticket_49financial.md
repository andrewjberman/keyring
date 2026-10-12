# One test ticket filed in tenant 49financial — 0.7.0_AE_CloudOps~TV2

**archetype:** IMPLEMENT

**Date:** 2026-10-12
**Task Order:** TCKT_VNEXT.TO-APPLY-R14-tk2.one-test-ticket-in-49financial-dell2 (read at `4c2743ed2f`, GO msg 6643, acked)
**Status:** COMPLETE. One create, 201, AC1 PASS. Nothing deleted, no token printed.

---

## Result

Ticket **TCK-20261012-c546fead**, created by `svc-commentary` through `POST /api/scoped/tickets`, one call.

Read back with one `get-item`: tenant `49financial`, type `analysis_request`, status `open`, created_by
`svc-commentary`, title begins `[TEST TCKT_VNEXT R14] `. No `draft_commentary`, no `report_ref`.

The round-12 cottonwood ticket TCK-20261012-13cd3a1d was not touched, as the order states.

## Pre-read (step 1), run live inside the script and printed before the write

- Positive control: TCK-20261009-a1052909 reads `open`, `analysis_request`, `svc-commentary`, firm `cottonwood`.
- `opal-ticket-api`: `COMMENTARY_ALLOWED_FIRMS` = `49financial,cottonwood,inflection`; CodeSha256 `4sDK8P5m...`,
  LastModified 2026-10-12T01:50:30Z, unchanged since round 9.
- The script refuses to write unless the control is `open` and the list contains `49financial`.

## Method and handling

Same as round 12 (`r12_tk1_create.py`), with the tenant, title, source and attachment label changed. The token is
read into memory and sent as a Bearer header only. No raw response is printed. The result file holds no at-sign
(asserted before writing). A `--dry` run printed the pre-read and body first.

## Not done, by the order

No retry, no second create, no delete, no ledger entry (a data write), no surprise row (nothing odd). The DL notice
fires on any create and is not observed by this seat.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `r14_tk2_create.py` | `--dry`, then the one write | pre-read as above; 201, TCK-20261012-c546fead |
| `r14_tk2_ticket.py` (issuer's AC1) | as written in the order | `TK2-OK TCK-20261012-c546fead firm=49financial status=open created_by=svc-commentary` |
| `.tools/aws` (inside the script) | get-item x2, get-function-configuration, get-secret-value | as above |
