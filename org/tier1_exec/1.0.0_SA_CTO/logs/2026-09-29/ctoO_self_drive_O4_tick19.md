# /self-drive ticks 18-19 -- ~O fabric, four projects (1.0.0_SA_CTO~O)

**archetype:** COORDINATE

- Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md`
  @7612f001c4. Cron `0eef1ea2`.
- Ticks covered: 18 (06:43Z, runtime line) and 19 (07:13Z, the one-hour floor, plus calls ruled). **state: ARMED**

## Scope at tick 19

| project | status | dep_stage | open TOs |
|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 6 / 53 |
| NFRA_OPALAI | active | EXECUTING | 4 / 35 |
| NFRA_MCPORTAL | active | EXECUTING | 2 / 18 |
| NFRA_MCPINDEX | active | EXECUTING | 4 / 73 |

16 of 179 open, down from 19. Inbox: 0 unread. Sequence flags: none. REACHABLE 4. All four project.json `blocking`
fields are now current (tick-17 finding closed).

## Calls ruled by the driver since tick 17

1. **MCPINDEX R-15 read** (COO~MI 26470, 26475). The BD transaction document drives the live silver merge. All 4 BD
   documents have a dead Playwright step (70 of 70 fail) but a live merge (70 of 70 succeed).
   - CONFIRMED COO~MI's correction of this seat's round-3 analysis: disable nothing (MX-i-5 superseded, 0 disabled).
     MX-s-14 strips the Playwright step and the credential read from all 4 documents, keeps each merge byte-unchanged,
     and adds no new REST pull (item 6 superseded).
   - Condition: one never-widen ask naming the 4 document writes, the merge byte-unchanged, the next merge's row count
     against the prior day's, and rollback per document version.
2. **OPLGTW R-4 contingency** (COO~O 26485: export memory grows with rows at 11 columns; the maximal query is at
   286.7 MB against the 268,435,456-byte cap). RULED (a): a remedy cell first; the contract numbers stand.
   - Criteria: flat within 10% across 25k/125k/250k at 11 columns; the maximal query under 80% of the cap;
     OG-x-2 re-run at full width.
   - A PRD revision follows only if the remedied code still fails.
3. **MCPINDEX Z-W15-S5** (the naming gate refuses the ETF key in the catalog). This is the LGIC gate owner's call, so
   it was routed via `0.0.0_AB_MSTR~Z` with this seat's REC. Laptop `1.0.0_SA_CTO` APPROVED the `catalog_key` kind in
   design (102627).
   - A fork is building the patch and controls. It must handle the key being NEW in both files, and must stop if no
     live remediation covers `platinum/etfs`.
   - MX-r-5 ships without the ETF tool meanwhile, and MX-t-10's bytes are frozen.

Design forks: 0. Governance forks: 0.

## Acts only Andrew can do (cited)

- G-ACCT step 5, the setup-token sign-in (his login).
- G-ACCT step 6, one MFA (his MFA).
- Create the M365 test user for G-C (tenant-admin login, plus licence spend).
- MCPORTAL G-2ND, the Opal Bloomberg sign-in (his login).
- MCPORTAL G-CLOSE and OPLGTW G-D, the person-operated runs (his login).
- The BD/SmartX rotation, "later" (credential owner).

## Completion test

NOT DONE: 0 of 4 complete.

## Compiler Tools

- `sequence-check.py --project` x4: flags none.
- The order-file census: 16 of 179 open.
- `lib/opal_naming.address()` with a None scope raises ("scope must be a non-empty ASCII string"). The builder cannot
  emit the scope-less legacy ETF key, so route (a), a registry row, is closed.
