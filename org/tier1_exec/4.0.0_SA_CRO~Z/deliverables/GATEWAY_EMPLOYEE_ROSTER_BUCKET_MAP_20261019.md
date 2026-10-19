# Opal employee roster and proposed role-to-bucket map, for Andrew's approval (NFRA_MCPINDEX FWD-25)

**Author:** 4.0.0_SA_CRO~Z, 2026-10-19 ~15:0xZ (11:0x AM ET). **Asked by:** 1.0.0_SA_CTO~Z, msg 35977.
**Order:** Andrew-direct ~14:1xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_141xZ_GATEWAY_INDEXED_ALL_MCPORTAL_SURFACES_TOOLS_TESTED_PER_EMPLOYEE_CHEAT_SHEETS.md`
@4a337dec2e. **PRD:** NFRA_MCPINDEX v0.18 @ea1ce7ba27, "What only Andrew decides (FWD-25)".

**His seeds, verbatim:** "opal-data-assets for the operational team versus opal-data-harvest for the asset management
team vs opal-data-etfs for the CFO, etc etc".

**This file grants nothing.** Every row is a proposal. Each one marked **WIDENS** needs Andrew's yes; then NFRA_OPLGTW
applies it under never-widen. Nothing here was written to any grant store.

---

## 1. Answer first

- **Denominator:** 86 Entra directory users read (Graph `/users`, one page, no nextLink). 39 are members and 47 are guests
  (partner-firm accounts, out of scope). 21 members are enabled and licensed: **17 people** and 4 non-person accounts.
- **Entra's job title and department are blank for all 17 people.** The PRD names those fields as the role source, and
  they hold nothing. Every role below comes from a cited repo record instead, or is marked **UNRECORDED**.
- **Current grant:** 3 of the 17 have a gateway profile (Andrew, Alyssa, plus the non-person Opal Bloomberg account).
  The other 15 have none and use the legacy path. That path already reads opal-data-harvest, opal-data-etfs,
  opal-data-portal-v2, opal-data-mdpf and news. It does **not** read opal-data-assets (the `client_*` tools), Schwab or
  Black Diamond.
- **So only three buckets can widen anyone:** opal-data-assets, Schwab and Black Diamond fees. Every harvest, ETF or
  portal proposal is a **sheet-relevance choice, not a grant change**.
- **6 proposals WIDEN** a current grant: 2 on opal-data-assets for the operations team (his seed), 1 on Schwab for
  Menachem, and 3 optional, each marked as such.

## 2. What a "current grant" is (read 2026-10-19 ~14:4xZ)

| Layer | Source read | Claim |
|---|---|---|
| Tier | Secrets Manager `gateway/principals/rosters` (the deploy script writes it into the gateway's `.env`), matched to Entra object ids | measured |
| Profile + data grant | DynamoDB `gateway-access-state-table`, every `POLICY#` row (25 items, 2,042 scanned, no further page) | measured |
| Per-person narrowing record (`person_access`) | the same scan: **0 records** | measured |
| Identity tool allowlist | `infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt` (no live row) and the code seed (Opal Bloomberg only) | measured from source |
| What each layer admits | `app/data_entitlement.py` `decide()` + `app/tier.py` `resolve_tier()` at HEAD (last touched 366bd9d3aa6, 2026-10-16) | **inferred from source, NOT read from the served `/api/admin/people` view** |

The rules, as the source states them:
- **Tier.** `master_admin` = Andrew. `standard` (write-capable) = Alyssa and the Opal Bloomberg account. Every other
  verified person is `read_only`: no send, upload or write tool.
- **No profile (legacy path).** Every read tool passes except two groups:
  - Schwab: denied;
  - the `client_*` tools and `blackdiamond_list_fees`: master_admin only (OG-bd-2 / OG-ad-1).
- **Active profile.** It confines only the data-grant family (Schwab, `client_*`, Black Diamond). Everything else passes
  as on the legacy path.

To confirm on the served release: Andrew's owner console, `/api/admin/people`, shows the same view per person.

## 3. The buckets (from `workflows/atom_decomposition/catalog_entries/`, 319 rows)

| Bucket | Catalog rows | What a person asks it | Tools | Today, no profile |
|---|---|---|---|---|
| opal-data-assets | 123 | client accounts: holdings, transactions, allocation, fees, by firm | `client_*` (5) | **denied** (master_admin only) |
| Schwab (data grant) | -- | Schwab positions, balances, transactions for the two masters | `schwab_*` (5) | **denied** (profile only) |
| Black Diamond fees | -- | billed fees | `blackdiamond_list_fees` | **denied** (master_admin only) |
| opal-data-harvest | 78 | equity research: fundamentals, filings, peers, chatter, Opal's published views | `harvest_*` (10) | admitted |
| opal-data-etfs | 27 | Opal's ETFs and rivals: holdings, flows, NAV, trades, ownership, monthly report | `etfs_*` (19) | admitted |
| opal-data-portal-v2 + opal-data-mdpf | 30 | model portfolios, AUA/AUM, CMA, macro, market returns, valuation, regime | `portal_get_*`, `mdpf_get_*` | admitted |
| news (DynamoDB + opal-data-news-v2) | 4 | news, market mood, trending topics | `news_*` | admitted |
| Microsoft 365 (own account) | -- | the person's own mail, calendar, files, Teams | Graph tools | reads admitted; send/upload need `standard` |

57 catalog rows carry no bucket (PRD v0.18 counts the same 57). They are NFRA_MCPINDEX's FWD-23 work, not this file's.

## 4. The roster: 17 people

Column keys:
- **Groups:** role-bearing Entra groups only. All-company, archiving and filter groups are dropped.
- **Current:** the person's current grant: tier, then profile.
- **Proposed:** the buckets the sheet would carry, beyond Microsoft 365, which every person keeps.

| # | Name | Work email | Title / dept (Entra) | Role (source) | Groups | Current | Proposed | Reason | Widens? |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Andrew Berman | Andrew@opalinvest.com | blank | owner; gateway master admin (rosters secret) | OCIO, 49F CIO Office, Consulting, Trade Subm. | master_admin; profile active (Schwab full, 10 portal channels) | all buckets | runs the platform | no |
| 2 | Austin Graff | Austin@opalinvest.com | blank | CEO (`docs/architecture/ASTN_WSJFT_PRD.md`: "Austin (CEO)"); owns the Asset Management IC and OCIO IC meetings (CRO transcript recon) | Accounting, Administration, BSN-Managers, Inv. Mgmt, OCIO, 49F | read_only; no profile | portal-v2/mdpf, harvest, etfs, news | firm-wide view; chairs both ICs | no |
| 3 | AJ Graff | AJ@opalinvest.com | blank | CFO (Andrew, quoted in a record: "AJ, our CFO"); "COO/CFO" in the Azure billing record | Accounting, Administration, BSN-Managers, Inv. Mgmt, OCIO, Consulting, Trade Subm. | read_only; no profile | **opal-data-etfs** (his seed), portal-v2/mdpf AUA/AUM; *optional:* Black Diamond fees | CFO: ETF economics, firm AUM; fees if billing is his | etfs/portal: no. **Fees: WIDENS (optional)** |
| 4 | Adam Muller | Adam@opalinvest.com | blank | Head of Asset Management (AMGT origin record) | Inv. Mgmt, 49F CIO Office, Trade Subm., Inflection | read_only; no profile | **opal-data-harvest** (his seed), etfs, portal-v2 valuation/market, news | runs the analysts; memos use the harvest | no |
| 5 | Lauren Harmon | Lauren@opalinvest.com | blank | equity research analyst, asset management team (`/lauren-report`; AMGT: "an analyst, Adam, Lauren, a PM") | 49support, Inflection | read_only; no profile | **opal-data-harvest**, news | quarterly earnings updates from the harvest | no |
| 6 | Yang Liu | Yang@opalinvest.com | blank | Head of OCIO / PM (`ADVI_TAXSMA_PRD.md`) | OCIO, Trade Subm. | read_only; no profile | portal-v2/mdpf (his models), harvest, etfs; *optional:* Schwab | owns the model portfolios; tax-SMA work needs cost basis | portal/harvest/etfs: no. **Schwab: WIDENS (optional)** |
| 7 | Alyssa Keith | Alyssa@opalinvest.com | blank | operations, day-to-day operator (`ADVI_TAXSMA_PRD.md`; runs the daily Bloomberg dashboard) | 49support, Inflection | standard; profile active rev 5 (Schwab describe/list/query, no download; 10 portal channels) | **opal-data-assets** (his seed), Schwab (keep), portal-v2/mdpf | operational team | **assets: WIDENS** (the `client_*` tools are in the data-grant family and her grant does not carry them) |
| 8 | Menachem Goldstein | menachem@opalinvest.com | blank | operations lead (CRO record, 2026-10-07: "The operations lead's list (Teams 1:1, Menachem Goldstein)") | OCIO, Trade Subm. | read_only; no profile | **opal-data-assets** (his seed), Schwab, portal-v2/mdpf | operational team; a Schwab grant was drafted for him on 09-14 and never activated (`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MENACHEM_SCHWAB_CLAUDE_ACCESS_20260914/`) | **assets: WIDENS. Schwab: WIDENS** |
| 9 | Manav Shah | Manav@opalinvest.com | blank | **inferred:** 49 Financial relationship (also manav.shah@49financial.com in the gateway's mail sender table; asks AUM questions that count Opal's ETFs) | 49F, 49F CIO Office, OCIO, Consulting, Trade Subm. | read_only; no profile | portal-v2/mdpf, etfs | 49F model and AUM questions | no |
| 10 | Keith Wagner | Keith@opalinvest.com | blank | **UNRECORDED** | 49F, 49F CIO Office, OCIO, Consulting | read_only; no profile | portal-v2/mdpf, news (placeholder) | OCIO and 49F groups suggest the model side | no |
| 11 | Jim Reed | Jim@opalinvest.com | blank | **UNRECORDED** | OCIO | read_only; no profile | portal-v2/mdpf, news (placeholder) | OCIO group | no |
| 12 | Wayne Wicker | Wayne@opalinvest.com | blank | **UNRECORDED** | OCIO, Trade Subm. | read_only; no profile | portal-v2/mdpf, news (placeholder); *optional:* opal-data-assets if he works trades | OCIO + trade submissions | placeholder: no. **assets: WIDENS (optional)** |
| 13 | Jeanette Drew | Jeanette@opalinvest.com | blank | **UNRECORDED** | Administration | read_only; no profile | Microsoft 365 only (placeholder) | Administration group | no |
| 14 | Anastasiia Samokhvalova | Anastasiia@opalinvest.com | blank | **UNRECORDED** | 49F | read_only; no profile | portal-v2/mdpf, news (placeholder) | 49F channel member | no |
| 15 | Bobby Pisinski | bobby@opalinvest.com | blank | **UNRECORDED** | 49F | read_only; no profile | portal-v2/mdpf, news (placeholder) | 49F channel member | no |
| 16 | Craig Berberich | Craig@opalinvest.com | blank | **UNRECORDED** | 49support, Inflection | read_only; no profile | portal-v2/mdpf, news (placeholder) | no role signal | no |
| 17 | Jai Mukraj | Jai@opalinvest.com | blank | **UNRECORDED** | 49support, Inflection | read_only; no profile | portal-v2/mdpf, news (placeholder) | no role signal | no |

**Group names, short forms:** OCIO = "Opal OCIO". 49F = "49 Financial Internal Channel". 49F CIO Office = "Opal CIO
Office for 49 Financial". Consulting = "Opal Consulting". Trade Subm. = "Opal Trade Submissions and Approvals". Inv.
Mgmt = "Investment Management". 49support and Inflection hold 15 of the 17 people, so they carry no role signal.

**WIDENS count:**
- 3 firm proposals: Alyssa assets, Menachem assets, Menachem Schwab.
- 3 optional: AJ fees, Yang Schwab, Wayne assets.

## 5. Not on the roster (accounted for, so the denominator closes)

| Count | Accounts | Why excluded |
|---|---|---|
| 4 | Opal Bloomberg (opalbloomberg@), Pathfinder ETFs (info@pathfinderetfs.com), Conference Room, Conference Room 2 | licensed but not a person. Opal Bloomberg is the terminal/concierge service identity (standard tier, active profile); its grant is NFRA_OPLGTW's, not a cheat-sheet reader's |
| 4 | Azure Admin (LDTech), Break Glass, Little Dog Tech, Purview Access | enabled, unlicensed admin/service accounts |
| 14 | Billing, Chris Coulter, Conference Room 1, Jay Coulter, Opal 49, Opal Analytics, Opal Capital Information, Opal Invest Cottonwood, Operations, Toni Lee, Trading, Wade Franks, William Wicker, report-phishing-checkpoint | account disabled |
| 47 | guests | external tenants (partner firms); "Opal internal user" excludes them |

17 + 4 + 4 + 14 + 47 = 86.

## 6. What Andrew decides (one line each)

1. **The 3 firm WIDENS** (Alyssa assets, Menachem assets, Menachem Schwab): yes or no each.
2. **The 3 optional WIDENS:** yes or no each.
3. **The 8 UNRECORDED roles** (rows 10-17): name each person's job, or accept the placeholder (portal-v2/mdpf + news,
   no grant change).
4. **Sheet relevance vs grant narrowing.** Today every one of the 17 can already read harvest, ETFs, portal and news. My
   recommendation: the sheet narrows by relevance and the grant stays as it is. That matches the PRD ("only the tools
   their gateway grant reaches, grouped by the buckets relevant to their job").
   - To make the grant match the sheet instead, use the per-person record's `channels_deny`. It exists in the gateway
     (C-PERSON), but no record is written today.
   - That is a NARROWING, which removes reach someone may be using. It is his call too, and I do not recommend it for
     V1.

## 7. Bounds of this file

- **Reads made, all read-only:**
  - Graph `/users`, `/groups` and `/users/{id}/memberOf` (az CLI, signed in as Andrew@);
  - one Secrets Manager get (`gateway/principals/rosters`);
  - one DynamoDB scan of `gateway-access-state-table` (filtered to `POLICY#`).
- **Nothing was written** to Entra, the grant store, the gateway or any secret.
- **Not in the repo:** no object id, account id or secret value. Raw reads stay in the session scratchpad.
- **The role column is the weakest one.** Eight roles are cited from repo records, one is inferred (Manav), and
  eight are unrecorded. A role the repo never wrote down may still be wrong in the repo.
- **The grant column is source-inferred** for what each tier admits (section 2). The served `/api/admin/people` view is
  the confirming read.
