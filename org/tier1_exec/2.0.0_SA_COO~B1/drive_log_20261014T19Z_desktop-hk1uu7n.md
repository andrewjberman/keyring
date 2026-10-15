# 2.0.0_SA_COO~B1 drive log -- ADVI_FIRMBKTS, 2026-10-14 19:20Z to 20:20Z (substantive ticks)

**archetype:** COORDINATE. Times are UTC (commit dates, local EDT + 4 h). Continues `drive_log_20261014T16Z_desktop-hk1uu7n.md`. Push state of every hash below: LOCAL on `box/dell1` unless stated (not re-measured at write time).

## The ticket trade-form pair (an act outside the round-8 orders; 19:54Z to 20:19Z)
- 19:54Z msg 5805 (acked): the laptop CTO's ruling `RULING_20261014_195xZ_TCKT_TRADE_FORM_FIRM_BUCKET_ACCESS_ROUTE.md` @ee287446e1 approved TCKT_VNEXT's request (FWD-10, Andrew's P2 Ticket Center, due 2026-10-24) as bounded: one role (`opal-ticket-api-role`), two actions (Get, Put), one prefix per bucket on `opal-data-49financial`, `-inflection`, `-cottonwood`, plus CORS. Route: the CRO writes three `exemptions.json` rows, the fence generator regenerates, one laptop CloudOps scoped apply sequenced with M02, this seat writes the COO half, the laptop CTO signs his; target 2026-10-20.
- 19:59Z `6d89e6698a`: COO half (permitted set, the generator's rendered statements per row, expected N 10/2/1 from today's scoped-row counts 9/1/0, CORS origins printed from a live read of the deployed portal API `7k3ed8px20` (PROD two hosts, DEV `http://localhost:5174`), preconditions, both branches, rollback). Row spec sent to `4.0.0_SA_CRO~DELL1`; the laptop CTO asked about a hosted DEV hostname and who authors the CORS blocks.
- 20:01Z the CRO's rows `89beb84dd9` (with an added `arn`, required by `validate()`); read back (49financial 29 rows, inflection 8, cottonwood 7). 20:02Z `99665eb416`: amendment 1. The CRO flagged `ticket-attachments` as out of pattern; V2 (`2.0.0_SA_COO~V2`) asked.
- 20:13Z msg 5833 (acked): the prefix is `ticket_attachments` (snake_case; V2's corrected request @8c10f053d1). 20:14Z the CRO's `51f1051aa1` corrected the rows. 20:15Z `706b0f0b72`: amendment 2.
- 20:18Z msg 5842 (acked): the laptop CTO amended his ruling (@bc7493406e): the prefix is `address()` output, never typed. 20:19Z `a7a3c2bd65`: amendment 3: I ran `address("portal", <firm>, "state", "ticket_attachments", "trade-form")` for the three firms; each row's prefix at HEAD equals its key plus `/` (3 of 3, by code).
- Open: the laptop CTO's half and his DEV-origin answer; then the laptop CloudOps apply with the baseline-plan precondition.

## Round 8 (unchanged)
5 of 7 orders terminal; FB1 LIVE and WAITING (act 3 prepared). Dated waits (owner FB1): guard arm (a) 2026-10-15 about 13:00Z read by 14:00Z; act 3 the same day if MET; first-day reads 2026-10-16 by 18:00Z.

## Compiler Tools
Run: `lib/opal_naming.py address()` (read-only, by code), `iam get-role` and `apigatewayv2 get-apis` (one live get each, rail-checked), `open-calls.py list`, `unblock.py tick`. Worked: reading the generator's source (`opal_name/main.tf`) before writing the half gave the exact statement ids; comparing the rows to `address()` by code caught nothing wrong and closed the CTO's check. Failed: nothing this hour. Gap: the COO half's expected-N table is computed from today's registry and not from a generator render (a render needs a scratch Terraform root); the applying lane's plan is the reading.
