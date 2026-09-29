# /self-drive ticks 16-17 -- ~O fabric, four projects (1.0.0_SA_CTO~O)

**archetype:** COORDINATE

- Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md`
  @7612f001c4. Cron `0eef1ea2`.
- Ticks covered: 16 (05:43Z, quiet) and 17 (06:13Z), the first tick under the REWRITTEN skill: `1.0.0_SA_CTO~Z` msg
  26459, @79fb47a6bb + @120b94dae1. In it, Step 1 means the driver rules every call and only cited ACTS are listed for
  Andrew. **state: ARMED**

## Scope at tick 17

| project | status | dep_stage | open TOs |
|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 6 / 53 |
| NFRA_OPALAI | active | EXECUTING | 4 / 35 |
| NFRA_MCPORTAL | active | EXECUTING | 2 / 18 |
| NFRA_MCPINDEX | active | EXECUTING | 7 / 73 |

19 of 179 open, down from 23. Inbox: 0 unread. Sequence flags: none. REACHABLE 4, UNREACHABLE 0.

**Finding:** the project.json `blocking` fields are stale in all four (MCPINDEX still reads round 1; OPLGTW reads PRD
v0.7). They were routed to each COO to refresh (msg ~06:1xZ).

## Calls ruled by the driver since tick 15

1. **The G-C grant's accounts dimension** (carried to Andrew by COO~O 26456, and re-classed as a CALL under the
   rewritten Step 1). RULED: accounts = exactly the set `SEALED_EXPECTED_V2` was computed over; the narrowing stays on
   datasets, columns, dates and operations.
2. **Row Z-S10** (GCG1-AC3 verbatim against AC6 no raw account id). RULED: AC6 wins; the scope diff is committed with
   accounts redacted, plus a SHA-256 of the unredacted diff.

Both are in `deliverables/1.0.0_SA_CTO~O/RULING_G-C_ACCOUNTS_AND_Z-S10_20260929.md` @8bf2bf37c6 and were routed to
COO~O. A direct send to `0.7.0_AE_CloudOps~OG` was REFUSED by LD-0529 (a Tier-2 seat hears an act only as a task
order), which is correct. COO~O carries both through the amended OG-g-1.

Design forks: 0. Governance forks: 0.

## Acts only Andrew can do (each cited; no decisions listed)

| act | citation |
|---|---|
| G-ACCT step 5: the `claude setup-token` sign-in with the dedicated Analyst Claude account | his login (Step 1 act list) |
| G-ACCT step 6: one relayed MFA for the Opal Bloomberg gateway sign-in | his MFA code |
| G-C: create one unprivileged M365 test user in the tenant, e.g. `og-controlled@opalinvest.com` | tenant-administrator login, plus a mailbox licence (spend) |
| MCPORTAL G-2ND: a person signs in as Opal Bloomberg | his login |
| MCPORTAL G-CLOSE, OPLGTW G-D: the person-operated close run and walkthrough | his login at a work browser |
| The BD / SmartX password rotation (his word: "later") | credential owner |

Not an Andrew act, noted only: Alyssa's Q1-Q3 post for his speed test is a request he makes of her.

## Completion test

NOT DONE: 0 of 4 complete.

## Compiler Tools

- `sequence-check.py --project` x4: flags none.
- The order-file census plus the project.json `blocking` read: 19 of 179 open. The blocking fields were stale in 4
  of 4.
- `send_message`'s LD-0529 guard refused the direct act-bearing send to a Tier-2 seat. It worked as designed.
