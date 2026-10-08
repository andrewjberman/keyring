# Why Opal staff cannot use the gateway's Schwab data, what already exists to fix it, and how the Tax SMA master gets added

**From:** 4.0.0_SA_CRO~Z. **For:** 1.0.0_SA_CTO~O (NFRA_OPLGTW, NFRA_MCPINDEX), at Andrew's word of 2026-10-08 ~17:0xZ.
**Measured:** 2026-10-08 ~16:5x-17:2xZ. Read-only: Alyssa's two forwarded Teams screenshots and her three files on
SharePoint, the gateway code and contract at site-Z HEAD, the Schwab puller code, and a listing plus column-name read of
`s3://opal-data-assets/schwab/`. Nothing was changed, granted, run against Schwab, or downloaded beyond parquet metadata.

## Andrew's words, verbatim

> "I need you to check out the images i sent via Andrew Berman on teams to your opal bloomberg teams inbox. They are the
> images from Alyssas agent, she is detailing the difficulty she has been having with the opalgateway, they are already
> using it but the lack of account names and account numbers basically makes it useless for any opal user, so that needs
> to be assessed and plans made for rectifying associated with the relevant NFRA project on this box. Furthermore, she
> has put three markdown files that i asked for in our shared sharepoint projects folder (look for PRD language to find
> its location), they cover the current schwab needs that she is effectively scraping over chrome which will inform how
> these opalgateway paths need to widen/improve. there are also docs ffor other workflows she is doing on chrome that
> likely would be better handled through he gateway if it has anything to do with data we already collect or any client
> functions."

> "I have brought CTO~O online to receive your findings as they come in."

> "Cost basis data absolutely exists in the aws bucket already, all of that stuff should be routing to silver schwab
> layers in parquet for rapid lookups"

> "Yes that is another thing that we are going to need to go do. we need to add a new master account to the schwab daily
> puller, the one that Alyssa referenced that has the Tax Accounts. We need to assess if that can be managed
> programmatically or if I need to RDP into the schwab ec2 and utilize their SI2 GUI Application ( i would dramatically
> prefer if we can handle this programmatically)."

## Sources read

| Source | Where |
|---|---|
| Two screenshots from Alyssa's agent, forwarded 16:48-16:49Z | Teams chat Andrew Berman / Opal Bloomberg, messages 1791478135904 and 1791478145716; plus her forwarded text 1791478165325 |
| `Schwab Data Needs Brief.md`, `External Chrome Workflows Brief.md` (both 2026-10-08), `PRD.md` | SharePoint site `Shared`, `Product-Alyssa/PRD-004_gateway-data-feeds/assets/` and the folder root. `PRD.md` is the empty template (owner front end Alyssa, back end Andrew). Andrew said three files; I found these two plus two short intake stubs and a one-line notes file |

---

## 1. The answer in five lines

1. **The missing account numbers and names are a design rule, not a gap.** The gateway contract lists `raw_account_id`
   and `account_title` as FORBIDDEN field classes and replaces every account with a keyed hash (`account_ref`).
2. **The data Alyssa asks for is already in Schwab silver.** Unrealized lots, realized lots and the account master
   (numbers, titles, registration) sit in parquet beside the four tables the gateway serves, with 560 to 690 days of
   history. The gateway serves 4 of about 20 tables and 30 of those days.
3. **So most of the fix is widening the contract and the grant, not building a feed.**
4. **The Tax SMA master 0840-3355 is not pulled at all.** It is absent from the bucket and from every repository file.
5. **Adding it looks programmatic.** The puller is a REST client that sends the master number in its request; one
   enumerate run tells whether Schwab will return files for that master to the login the box already holds. Only if it
   returns zero is a Schwab-side entitlement needed, and that is set at Schwab, not on our box.

---

## 2. What Alyssa's agent reported

From the two screenshots and the forwarded text:

| Limit she hit | Her words |
|---|---|
| No account numbers | "accounts show up as a coded `account_ref`, not the real number. To find a client you have to match on something like the exact account value" |
| Tax SMA master missing | "the Tax SMA master 0840-3355 isn't there"; she searched both masters for a client's exact 9/30 value and got no match |
| No cost basis, no realized or unrealized gain/loss, no statements | listed as missing |
| 30 days only | "only the last 30 days (currently 9/15 - 10/7)"; rules out quarter-start versus quarter-end |
| Transactions coded | fees and flows not labelled |

Her short version for Andrew: "add master 0840-3355, a cost-basis lots table, a realized gain/loss table, a lookup from
account_ref to account number, and keep at least 13 months of balances and positions. With those, the quarterly Tax SMA
numbers can run without any Schwab downloads." Her current workaround is driving Schwab Advisor Center in her own Chrome
session, which can trade and move money.

---

## 3. Why the gateway shows no account numbers or names (measured)

| Where | What it says |
|---|---|
| `org/standards/NFRA_OPLGTW_CONTRACT.json` `forbidden_field_classes` | `raw_account_id`, `account_title`, `tax_identifier`, `mailing_address`, and three hidden-operand classes |
| NFRA_OPLGTW PRD line 147 | "Expose a versioned, keyed HMAC account_ref over master plus account ID ... An alias is usable only after resolution against the current authorized account set" |
| PRD line 357 (audit) | the audit excludes raw account ids |
| `app/account_ref.py` | `account_ref = "acr_" + version + "_" + base32(HMAC-SHA256(key, master, account id))`; resolution back to a raw id happens only inside the gateway, never in a response |
| contract `proposed_initial_profile` | the pilot grant was written for one person, `calendar_days: 30`, rolling |

This was a deliberate choice for the original pilot. For Opal staff doing client work it removes the one key they work
by: every request, file name and statement is keyed by account number.

---

## 4. What already exists in silver (measured, master 08335338, newest partition 2026-10-07)

| Table | Rows | What it carries | Fixes |
|---|---|---|---|
| `fact_acc` | 7,620 | `account_id`, `account_title_line_1-3`, `acct_regis`, `acct_type`, `date_opened`, `alias_name`; also taxpayer names, mailing address, email, phone | account numbers and names |
| `fact_uln`, `fact_ult` | 328,684 and 237,250 | lot-level: `acquired_date`, `current_quantity`, `cost_basis_unamortized`, `cost_per_share`, `unrealized_gain_loss`, `days_held`, `disallowed_loss_amount` | unrealized cost basis by lot |
| `fact_upn`, `fact_upt` | 64,559 and 43,861 | position-level cost and unrealized gain/loss | unrealized by position |
| `fact_rld` | 3,245 (one day) | realized lots: `closing_date`, `proceeds`, `acquired_date`, `gain_loss_dollars`, `h_t` (holding term), `disallowed_loss_amount` | realized gain/loss, daily |
| `fact_rly`, `fact_rty` | 327,621 and 115,936 (2026-09-30) | realized year-to-date | realized gain/loss for the quarter and year |
| `fact_trn`, `fact_sec`, `fact_rps` | present | transactions, securities, positions in the vendor's full form | flow labels, descriptions |
| History | 560 to 690 daily partitions per table | | the 13-month ask |

Master 08242234 carries the same set (plus `fact_rlw`). Column names only were read; no row content was opened.

**Andrew's statement is confirmed:** cost basis is already in Schwab silver as parquet. What Alyssa cannot reach is the
gateway's contract scope, not the data.

---

## 5. The Tax SMA master 0840-3355

### 5.1 State

- Not in `s3://opal-data-assets/schwab/` (children: `08242234`, `08335338` only).
- Not in any repository file: `comp-find '08403355|0840-3355|0840 3355'` reads 0 hits across 29,925 files.

### 5.2 How the puller decides which master it pulls

`infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` and `data/assets/docs/SCHWAB_AUTO_PULL_DESIGN.md`:

- The puller is a REST client, not a GUI driver. It reads the standing SI2 Desktop session's refresh token from the
  box's Administrator credential vault and calls Schwab's SDDServices backend directly.
- **The master is a request parameter:** `$req.MasterAccount = [int[]]@([int]$Master)` (line 323). The vendor's own
  field is an array of master numbers.
- **What stops 0840-3355 today is ours:** `[ValidateSet('08242234','08335338')]` on the `-Master` parameter (line 31),
  plus the list of masters in the schedules and the IAM grants.
- It has an `enumerate` mode that lists files and downloads nothing.
- A zero result on a window that contains trading days is treated as a failure, so a missing entitlement would show as
  a loud zero, not a quiet one.

### 5.3 Programmatic or the SI2 GUI

| Case | What decides it | What follows |
|---|---|---|
| The box's SI2 login is already entitled to 0840-3355, and Schwab produces its daily files | one `-Mode enumerate` run for `08403355` returns files | **Fully programmatic.** No RDP, no GUI |
| The login is not entitled, or no file set is produced for that master | the same run returns zero | A Schwab-side change: the SI2 user's master access or the master's data-file delivery. That is set by Schwab or in their administration, not on our box, and RDP into the SI2 GUI does not grant it either |

So RDP is not the deciding step in either case. The one read that decides it is the enumerate run. The design doc also
notes the session is one per box and shared by both masters, so a third master adds no second login; the schedules must
stay at least 30 minutes apart because of the box-wide session lock.

The only GUI case I can see is the existing one: if the standing SI2 session lapses, a person re-establishes it on the
box console. That is unchanged by adding a master.

### 5.4 The code-side edits, if the enumerate run returns files

Counted by file today (references to the existing two master numbers):

| Change | Where |
|---|---|
| Add `08403355` to the `-Master` ValidateSet | `sdd-daily-pull.ps1:31` |
| A third EventBridge rule and SSM target, staggered at least 30 minutes from the other two | `infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf` (2 refs), `canonical-schwab-si2-schedule/main.tf` (5) |
| The box's write-only grant to `schwab/08403355/bronze/*` | `canonical-schwab-ec2/monolith-iam.tf` (17 refs), `iam.tf` (4) |
| Silver conversion over the new master | `infra/aws/terraform/opal-assets/silver.tf` (7), `monolith.tf` (4) |
| A backfill, if history is wanted | `sdd-backfill-08335338.ps1` is the model |
| The gateway: master, prefixes, reader role | the contract's `masters`, `data_prefixes`, `completion_prefixes`; `opal-gateway/schwab_reader_iam.tf` (10 refs) |
| Name and LGIC conformance | `lib/opal_naming.py` registry, if a new resource name is minted |

The puller lands raw bytes and quarantines a file whose vendor prefix disagrees with the requested master, so a new
master cannot be mixed into another master's folder.

---

## 6. The plan, by NFRA project

### NFRA_OPLGTW (the Schwab gateway; CTO `1.0.0_SA_CTO~O`)

| # | Change | Kind | Whose word |
|---|---|---|---|
| G1 | **Account identity for Opal staff.** A grant-level switch that returns `account_id` and `account_title_line_1` (and registration) to a named internal principal, with every such read audited. Taxpayer names, tax ids, mailing address, email and phone stay forbidden | PRD amendment: the forbidden list and C2 | Andrew: it reverses a ratified rule |
| G2 | **History.** A grant date mode beyond 30 days (13 months, or since inception), since silver already holds it | contract and grant | Andrew sets the depth |
| G3 | **New datasets** from existing silver: unrealized lots (`fact_uln`/`fact_ult`), realized lots (`fact_rld`/`fact_rly`/`fact_rty`), and an account list (`fact_acc`, restricted to G1's columns) | contract, catalog, engine schemas | CTO |
| G4 | **Flow labels** on transactions, from `fact_trn` codes | catalog and semantics | CTO |
| G5 | **Master 0840-3355**, after section 5's enumerate run | puller, schedules, IAM, silver, gateway | the enumerate run is an act on the production box; owner seat plus Andrew's word for a new vendor read |

### NFRA_MCPINDEX (the tool index; same CTO)

| # | Change | From Alyssa's Chrome brief |
|---|---|---|
| I1 | opalinvest.dev reads as tools: model performance by period, AUA by basis, account counts with month-end history | C2, her P0 "cheapest win"; partly covered by the `mdpf_get_*` tools, which she does not report using |
| I2 | YCharts data tools: she reports `ycharts_time_series` 403 and `ycharts_snapshot_metrics` 404 | C1 |
| I3 | Read-class "download to a local or synced folder" for mail attachments and SharePoint files (today `write_class_denied`) | C6 and her section 6 |
| I4 | Mail move/folder and Teams send as write classes, approval per batch | C4, C5. These are write tools: Andrew's word |

### Ordering

1. G5's enumerate run first: it is one read and it decides whether the Tax SMA quarter can come off Chrome at all.
2. G1 and G3 together: either alone leaves her matching on dollar values.
3. G2, then G4. I-items in parallel; I4 last.

---

## 7. Calls that are Andrew's

1. **G1:** account numbers and titles to named Opal staff. It reverses the pilot's ratified rule. Recommendation: yes,
   for internal principals only, columns limited as in G1, audited per read.
2. **G2:** history depth. Recommendation: 13 months now, since inception later.
3. **G5:** the one enumerate run for master 08403355 on the Schwab box (a single list request on the existing route,
   no download). Recommendation: yes.
4. **I4:** whether the gateway gains mail-move and Teams-send write tools.

## What bounds this

- Silver was read for master 08335338's newest partition, column names and row counts only. I did not check that the
  cost-basis tables tie to Schwab's own totals, or that every daily partition is complete.
- I did not read the silver converter to confirm it handles every table type for a new master without change.
- "Entitled" in section 5.3 is my reading of how SDD master access works from the code and design doc; I have no
  Schwab documentation for it.
- Alyssa's briefs mark their own items as verified or inferred; I took them as written.
- Andrew mentioned three markdown files; I found two substantive ones. If a third exists elsewhere, it is not covered.
