# ANDREW_DIRECT 2026-10-16 ~01:3xZ -- f086 on dell1, 7686 internal, the CRM match key, c02c to the dell2 desktop

Channel: the laptop `1.0.0_SA_CTO` terminal, in answer to this seat's tick-88 report (four calls held for him).
Recorded by 1.0.0_SA_CTO, same turn.

## His words, VERBATIM

First message (~01:36Z):

> It should live on Dell1 (f086). 7686 it doesnt matter if its in production because it isnt visible for anybody outside
> opal. 9987/3256 that is in the "Files" zip in downloads, need you to go find what needs to be found. c02c we will get to
> this later i just need that list/message file on dell2 desktop.

Second message (~01:40Z, mid-turn):

> we just need to figure out what if anything could be used as a key for account matching

## What each word settles

| call | box | his word settles | carried to |
|---|---|---|---|
| `dell1-20261016T013032Z-f086` | dell1 | The M365 workflow activity spine project lives on DELL1 (dell1's option b). | `1.0.0_SA_CTO~DELL1` via `0.0.0_AB_MSTR` |
| `dell2-20261016T001759Z-7686` | dell2 | The candidate's pages are not visible to anyone outside Opal. That makes it Opal-internal, not client-facing, so the building box's CTO approves it (CLAUDE.md Portal). | `1.0.0_SA_CTO~DELL2` via `0.0.0_AB_MSTR` |
| `dell1-20261016T004131Z-9987`, `laptop-20261015T233750Z-3256` | dell1, laptop | The CRM export is the local copy `C:\Users\AndrewBerman\Downloads\Files.zip`. The real question is which field, if any, can serve as an account-matching key. The answer is in the findings below. | `1.0.0_SA_CTO~DELL1` via `0.0.0_AB_MSTR` |
| `dell2-20261015T054327Z-c02c` | dell2 | The send is deferred ("we will get to this later"). Put the list and message file on the dell2 desktop now. The call stays OPEN. | `1.0.0_SA_CTO~DELL2` via `0.0.0_AB_MSTR` |

## Findings: account-matching key (measured 2026-10-16 ~01:4xZ, laptop, read in memory, nothing extracted)

Only column names, counts and value SHAPES were read; no client value is written here.

`Files.zip` (3,218,239,946 B, 2026-10-15 21:27 local) holds 5 entries: `CRM_CottonwoodCapitalAdvisors.zip`
(26,485,027 B), `Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip`, and three
document archives `4XF.zip`, `HJH.zip` and `HKE.zip`. Each archive is named for an advisor code, and their listings carry
the folders `S58`, `HKJ`, `HJH`, `HKE`, `4XF` and `71Z`.

1. **The CRM has no account number.** Its seven files are Crmhouseholds (270 rows, 95 cols), Contacts (676 rows, 156 cols),
   C360households, Connections, Activities, Manualinsurance and Users. None has an account, custodian or registration
   column. Its keys are internal: `HouseholdID`/`HHID` (270 distinct of 270) and `ContactID` (676 distinct of 676).
   The person fields are `TaxID` (517 of 676 filled, 514 distinct, shape SSN), `DateOfBirth` (572), the names, the
   address and the email. `ClientStartDate` is filled on 106 of 270 households, which is relevant to c02c.
2. **The portfolio-accounting extract has no person or household field.** Positions, Transactions and Performance carry
   `Advisor_ID` plus `AccountNumber`/`Account_Number` only, across 83 distinct accounts.
3. **The only field the two share is `AdvisorID`.** Portfolio values: HKJ, S58 and HKE. CRM values: HKJ, S58, HJH and HKE.
   With four values it narrows candidates; it is not a key.
4. **The bridge is in the document-archive listings** (`<folder>/<code>/Listing.csv`):
   `CLNT` pairs `Account` with `ClientName` (247 accounts); `STMT` pairs `Acct` with `DisplayName`, the registration title
   (701 accounts); `TXRP` lists `AccountNumber` with no name (563); `NCSD` lists `HouseholdName` as "Last; First & First" with
   no account (184).
5. **Measured reach of that bridge:**
   - 46 of the 83 portfolio accounts appear in some document listing; 37 appear in none (13 of the 37 are 11-digit numeric
     and 13 are `A9999999`; possibly non-custodial or outside-held, unread).
   - 27 of the 83 reach exactly ONE CRM contact by name: 25 through the STMT title (the first and last name both appear in
     the title) and 8 through the CLNT `ClientName` (an exact first+last match). The two routes overlap.
   - 19 of the 46 listed accounts match no CRM contact by either route.
   - 19 of the CRM's 651 first+last pairs are shared by more than one contact, so a name match is ambiguous there.
   - NCSD household surnames: 160 of 162 are found among CRM household surnames, but 31 CRM surnames belong to more than
     one household.

**Answer:** nothing in these files is a clean account-matching key. The CRM's strong person key, `TaxID`, has no partner
in the account-side files. The best available route is account -> STMT/CLNT name -> CRM contact -> `HouseholdID`, with
`AdvisorID` used to block: 27 of 83 accounts resolve uniquely. A clean key needs one file this bundle lacks: Commonwealth's
account-registration file (account number with owner SSN or TaxID), or an Orion/CRM account-to-household link export.
Ask Cottonwood for either.

## Addendum ~02:1xZ: Andrew asked "is there anything else in here that can be used as a key?"

Second pass, same instrument, counts only:

- **CRM activity notes are the best route.** `Activities` has 109,883 lines. The free text mentions 52 of the 83
  portfolio account numbers, and each line's `regardingid` names a CRM household (97 mentions) or contact (12 mentions);
  17 mentions name something else. 51 accounts resolve to a household this way: 50 to a single household, and 1 to
  several (the majority is taken).
- **Insurance policy numbers:** 5 of the 91 `Manualinsurance.PolicyNumber` values equal a portfolio account number, and
  those rows carry `HHID`. None of the 5 overlaps the activity route.
- **The routes agree.** On the 20 accounts that both the activity route and the name route resolve, 20 of 20 land on the
  same household.
- **Union of the three routes (activity, name, insurance): 63 of 83 accounts reach a CRM household; 20 do not.**
  The remaining 20 by shape: 11 `AAA999999`, 5 `A9A999999`, 5 11-digit, 3 `999999AAA`, 2 `A9999999`, 1 `AA999999999`.
- **Not keys:** the CRM custom fields (Electronic Delivery, Preferred Contact Method, Net Worth, Referred by, FinaMetrica
  Score, Golf); the NCSD `Folder` (15 values, equal to no account suffix); the transaction notes (generic
  transaction text); the archive `ReadMe.txt` (it confirms that the folders are rep codes under the primary PlanID).
- **Handling:** 86 activity lines carry SSN-shaped text. Any copy of `Activities` must be treated as sensitive.

Instrument: `python -I` over `zipfile`, in memory, with scripts in this session's scratchpad (not committed). The
S3 copy under `s3://opal-data-cottonwood/commonwealth/cottonwood/bronze/crm/` stays unread from the laptop:
`Andrew_Berman` gets 403 on HEAD and an explicit bucket-policy deny on ListBucket (read 2026-10-16 ~01:4xZ).
