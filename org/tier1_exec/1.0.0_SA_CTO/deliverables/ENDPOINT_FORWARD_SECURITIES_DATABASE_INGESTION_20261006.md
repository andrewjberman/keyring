# ENDPOINT (step 2, /endpoint --forward) -- Opal's securities database: ingestion and maintenance

Author `1.0.0_SA_CTO`, 2026-10-06 ~18:0xZ (2:0x PM Eastern). **STATUS: PROPOSED, for Andrew to confirm. NOT LANDED:** no project
registered, no PRD.

**Brief read:** `docs/briefs/securities-database-ingestion-maintenance-brief-20261006.md` @901edd46a2 (`4.0.0_SA_CRO~P`, 157 lines,
read in full). Andrew's words: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_160xZ_NEW_SECURITY_LIFECYCLE_AND_HISTORY_BACKFILL.md`
("this is really how Opal builds its internal securities database and the associated ingestion and maintenance logic").

**Proposed home (L3, this seat's call):** a NEW project, D8/MDPF, code `MDPF_SECHIST`. Reason: MDPF_SECCLASS owns what a security
IS (the table row); this owns what a security DID (its stored history, the pull plan, the depth rules), with a different write
surface (the Bloomberg pull at site Z, the series store) and its own COO. It extends MDPF_SECCLASS's detector and table; it does
not re-own them.

```
  FWD-1  The morning after an Opal ETF first buys a security, an analyst opens it on the Positioning
         page and sees its class, sector, clean name and every return window a year of history supports,
         with nobody having asked for a pull
         DONE WHEN  EXERCISED -- one real new holding read the next morning, every hop real
         ACCEPT     an analyst picks a security an Opal ETF bought yesterday, opens it on the Positioning
                    page this morning and reads its classification and its returns from one week to one
                    year; nobody ran anything by hand to make that happen
         SOURCE     brief PART I, candidate thread (DIVZ; CSCO and BX the live negative case)

  FWD-2  A client's security shows performance for the whole time the client has held it
         DONE WHEN  EXERCISED -- one client-held security read back to its first appearance in the account
         ACCEPT     an Investor Reporting reader sees a held security's performance from the day it first
                    appeared in the client's account, not from the day Opal started tracking it
         SOURCE     brief O2; Andrew's rule, "from first appearance"

  FWD-3  Anyone can read, for any security, where it came into Opal and how far back its history must go
         DONE WHEN  EXERCISED -- one security with two sources read, and the deeper rule shown governing
         ACCEPT     for any security an operator sees each place it entered (an Opal ETF, a client account by
                    firm, a rival fund) and how much history each requires; the deepest requirement wins
         SOURCE     brief O3

  FWD-4  An operator can see whether each security's history is complete, without asking Bloomberg
         DONE WHEN  EXERCISED -- the stored range, the required range and any gap read for every tracked
                    security
         ACCEPT     for any security an operator reads what history Opal holds, what it should hold, and
                    exactly which days are missing
         SOURCE     brief O4

  FWD-5  Missing days fill themselves, and a gap never shows as a wrong number
         DONE WHEN  EXERCISED -- a real gap filled by the next run, and a window over an unfilled gap read
                    blank
         ACCEPT     when a security misses days in the daily pull, the next run fetches them; until then a
                    return covering those days is shown blank, never calculated across the missing days
         SOURCE     brief O5; PART III, "a blank is acceptable, a wrong number is not"

  FWD-6  Every held instrument is its own security, with its own row and its own history
         DONE WHEN  EXERCISED -- a preferred share, a numeric ticker and an identifier-only holding each
                    read with their own row and series
         ACCEPT     an instrument that is not a plain stock ticker (QXO B is the live case) has its own
                    classification and its own history and never borrows another security's
         SOURCE     brief O6

  FWD-7  The day's Bloomberg spend on history is visible and stays inside one budget
         DONE WHEN  EXERCISED -- one day's spend read against the budget, with a backfill in it
         ACCEPT     an operator reads what history cost today against the shared budget; a security's
                    backfill is paid for once; a backfill never causes a production pull to fail
         SOURCE     brief O7

  FWD-8  A security reads the same on every screen
         DONE WHEN  EXERCISED -- one security read on Positioning, Investor Reporting and Advisor
                    Intelligence, same answer on all three
         ACCEPT     a security's class, sector, clean name and its return for a given period are the same
                    wherever an Opal person looks it up
         SOURCE     brief O8; PART III, the second answer retired

  FWD-9  A money-market fund's performance is shown by one stated rule, never silently blank
         DONE WHEN  EXERCISED -- SALXX read across a week that includes a Monday
         ACCEPT     a reader sees performance for a money-market fund such as SALXX every day under one
                    stated rule, instead of it disappearing whenever the vendor leaves a day empty
         SOURCE     brief O9
```

## Calls for Andrew

1. **Rival funds' depth.** Andrew named two ingestion points (Positioning one year; client account from first appearance). REC:
   rival funds keep the three years MDPF_SECCLASS already set; Advisor Intelligence is not a separate point, because it reads the
   client firms' holdings.
2. **One series per security or one per holding.** REC: one series per security, starting at the earliest first appearance in any
   account. Each screen then reads the same series (FWD-8), and a holding's window is cut from it.
3. **Money-market funds (FWD-9).** REC: work out the day's return from the fund's own total-return level instead of the vendor's
   daily-return field, which is the field left empty on Mondays; a day with neither is blank.

## Provenance

GROUNDED ON: the brief, read in full. NOT READ: the grounding analysis it cites, the code it cites (its line references are the
CRO's), the register. The `MDPF_SECHIST` name is a proposal; L3 registers it.

-- 1.0.0_SA_CTO
