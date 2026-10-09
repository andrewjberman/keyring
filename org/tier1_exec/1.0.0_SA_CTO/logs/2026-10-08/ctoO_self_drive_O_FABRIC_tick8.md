# 1.0.0_SA_CTO~O -- /self-drive 30m ~O fabric, tick 8 (2026-10-09 01:31Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_215xZ_SELF_DRIVE_30M_O_FABRIC_FOUR_PROJECTS.md`
@ba8c4598fb. Cron d7c133e4. `state: ARMED`.

## Scope

| project | status | dep_stage | open TOs | sequence flags |
|---|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 5 (OG-rl-15, r29, issued @dbc700a9c8) | - |
| NFRA_OPALAI | active | EXECUTING | 4 (OA-f-11 amended @997238e4fc) | - |
| NFRA_MCPORTAL | active | ROUND_CLOSE | 0 (round-4 analysis landed; round 5 owed by 2.0.0_SA_COO~MP) | UNPLACED |
| NFRA_MCPINDEX | active | EXECUTING | 1 | - |

Inbox: 0 unread. Acked: 32203, 32208, 32211, 32221. The CVO~Z DONE note (W1-S1) carried no Msg-ID line, so it is unacked.

## Since tick 7

**NFRA_OPLGTW:**
- OG-tm-1 CTO half SIGNED @4149c01c23. It ratifies the label "Tax SMA basis" and the `slm` disposition
  `NOT_PUBLISHED_FOR_MASTER` as condition 2's minimum change. Condition 1 is accepted, and the QA pull proves it. Leg C is
  held on row Z-W39-S4.
- r29 (OG-rl-15) was cut @dbc700a9c8 after its four build cells drained. It carries md-1, sf-1, rf-1, cm-1 and the 13-month
  grants. Phase B is a deploy by 0.7.0_AE_CloudOps~Z in the window 11:00Z-23:00Z. Amendment A1 @7a1fc887c2 fills the v1.9
  domain table: five named parties, and a party with no domain is left out.
- Laptop COMM_ASSIST (relay 32211) asked for md-1 with the five parties' domains and a MAIL_BEARER by secret. Routed to
  2.0.0_SA_COO~O, and the reply went to laptop 2.0.0_SA_COO~R through 0.0.0_AB_MSTR~Z.

**NFRA_MCPORTAL:**
- L10 analysis for rounds 3-4 @460bc0af2f, on CVO~Z's slug 32208. Round 5 is MP-x-3, then MP-x-4, then MP-x-5. MP-c-1 and
  MP-v-1 are staged. R-17 places Z-S14 (the gateway full-suite stall at `app/integrations/schwab/engine.py:1103`) on NFRA_OPLGTW
  round 33's batch repair cell.
- W1-S1 / C-S3 was flipped DISARMED and REMEDIATED by 3.0.0_SA_CVO~Z @17b10b0dbf. ARMED now reads 5, down from 6.

**Law edits relayed (no act owed here):** @538f0f51a7 (per-box branches) and @c55a7b39cd (rule 30's naming gate REFUSES).

## Carried to NFRA_OPLGTW round 33 (this seat's list)

- FWD-14 to FWD-19 (PRD v2.1).
- The OG-bf-1 option Y leg (the dispatcher skip), unless 2.0.0_SA_COO~O places it in an OG-bf-1 amendment.
- Z-S14's stall, as the batch repair cell.
- The v2.1 item 7 wording: name corporate actions and statement PDFs as not served.

## Observed (fabric, not this scope)

`send_message` to `2.0.0_SA_COO~MP` twice returned `[Errno 13] Permission denied` on a message that WAS delivered: the file
was in the recipient's `read/` dir, 669 B and 628 B. The first time, a retry produced a duplicate. The error is raised after
delivery, likely as the recipient's watcher moves the file. Recorded here for the broker's owner, `0.0.0_AB_MSTR`'s lane. The
send-side rule meanwhile: on Errno 13, list the recipient's inbox and `read/` before any retry.

## Open calls in scope

No open calls in scope (tick 8) beyond the act below.

## Acts only Andrew can do

- Widen the gateway identity allowlist for the Bloomberg account by five read tools (opal_discover, opal_describe,
  blackdiamond_list_fees, find_sharepoint_site, search_files). Citation: the header of
  `infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt` ("Widening is an Andrew ruling only (PRD 4.3)"). Asked at the
  terminal at ~01:0xZ; no answer yet. Still owed as of this tick: no row was added (COO~O msg 32195; no commit since).

## Completion test

NOT DONE: 0 of 4 projects read `status: complete`. REACHABLE 4, UNREACHABLE 0.

## Compiler Tools

- `sequence-check.py --project` x4 and `to-check.py --all --project` x4 worked.
- `comp-surprise --project NFRA_MCPORTAL` worked, but only when redirected to a file: the rail refuses a census piped into a
  filter.
- Gap: `comp-surprise` prints the ARMED count but not the ids by default. This seat read the ids from the adjudication files.
