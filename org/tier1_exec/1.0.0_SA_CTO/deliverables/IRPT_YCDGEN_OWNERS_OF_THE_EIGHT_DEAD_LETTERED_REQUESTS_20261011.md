# Owner class and firm of the eight dead-lettered generation requests -- read only

Executor: `1.0.0_SA_CTO` on the laptop, 2026-10-11 14:17:52Z, for `2.0.0_SA_COO~G2`'s cross-box ask `XB-20261011T141307Z-3739`
(`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r13/CROSSBOX_ASK_OWNERS_OF_THE_EIGHT_20261011.md`; CTO~DELL2
round-13 analysis @7fa981f907 s.2 item 2). What leaves the laptop: class names, one of three kind words (a service subject's
name is not a person), firm ids, yes/no, state names. No address, no account id, no advisor id.

Method: `irpt-requests` queried per tenant partition, records matched on `logical_id`; the ACCEPTED record is the `ARTIFACT#`
record (its `RETENTION#` sibling carries the same owner block, read as a control; the `analysis#` record carries no owner block).
Kind decided on the laptop from `owner.principal_id`: `svc-` prefix -> SERVICE:<subject>; `@opalinvest.com` and not a service
subject -> OPAL_STAFF; anything else -> OTHER. `irpt-jobs` read now.

| # | request id | tenant | principal_class | kind | firm_id | home_firm_id | prospect_input_id present | job state / outbox_state now |
|---|---|---|---|---|---|---|---|---|
| 1 | REQ-ef7b39c548d08cbb4822f7cc | cottonwood | OPAL_GLOBAL | OPAL_STAFF | cottonwood | opal-capital | yes | RECEIVED / SENT |
| 2 | REQ-8966d24ffefa1c28269ef26c | cottonwood | OPAL_GLOBAL | SERVICE:svc-irpt-analysis | cottonwood | opal-capital | yes | RECEIVED / SENT |
| 3 | REQ-1f8b4cc4682f2d929cc70215 | 49financial | OPAL_GLOBAL | SERVICE:svc-irpt-analysis | 49financial | opal-capital | yes | RECEIVED / SENT |
| 4 | REQ-3d76e5b49dae4f91db1694b0 | 49financial | OPAL_GLOBAL | OPAL_STAFF | 49financial | opal-capital | yes | RECEIVED / SENT |
| 5 | REQ-9d59d4d2334f841152914569 | 49financial | OPAL_GLOBAL | OPAL_STAFF | 49financial | opal-capital | yes | RECEIVED / SENT |
| 6 | REQ-f7ddede91f98562412314b6e | 49financial | OPAL_GLOBAL | OPAL_STAFF | 49financial | opal-capital | yes | RECEIVED / SENT |
| 7 | REQ-448d42480cadd873fa74c3cf | 49financial | OPAL_GLOBAL | SERVICE:svc-irpt-analysis | 49financial | opal-capital | yes | RECEIVED / SENT |
| 8 | REQ-4b5155ac2ea9467ab771b414 | 49financial | OPAL_GLOBAL | OTHER | 49financial | opal-capital | yes | RECEIVED / SENT |

Denominator: 8 of 8 ids have an accepted (ARTIFACT) record; every RETENTION sibling agrees with its ARTIFACT record on all
five items (control). No job state changed since the 10:5xZ read (all RECEIVED / SENT): no finding.

Reading, for the packet: all eight carry `principal_class` OPAL_GLOBAL and `home_firm_id` opal-capital, with `firm_id` the
tenant; three were submitted by the service subject `svc-irpt-analysis`, four by Opal staff, one (#8, the request the
commentary-ready message names) by a principal that is neither (kind OTHER). All eight carry a `prospect_input_id`.

Not done: no write to either table, no queue receive, no delete, no redrive, no purge, no grant.
