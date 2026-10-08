# Open calls -- gateway Schwab usability for Opal staff (1.0.0_SA_CTO~O, 2026-10-08 ~17:3xZ)

> **SUPERSEDED 2026-10-08 ~17:5xZ.** Andrew had already ruled all four calls at the 4.0.0_SA_CRO~Z terminal:
> `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261008_174xZ_GATEWAY_SCHWAB_FOUR_CALLS_ANSWERED.md`
> @116d52009d. That record governs. A1 = (a) WIDENED to every name and title field (tax ids, addresses, email, phone
> stay forbidden); A2 = 13 months; A3 = yes, and on files back in the same shape, add 08403355 to the daily job;
> A4 = later, with a subagent-written brief. The four rows this seat added to the box list could not be closed (row
> NFRA_CTLPLN-Z-S4). The spot-checks and the G3/G4 rulings below still stand. PRD pen: handed to this seat by
> 1.0.0_SA_CTO~Z (msg 31931).

**Source:** `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPLGTW_SCHWAB_USABILITY_AND_TAX_MASTER_ASSESSMENT_20261008.md`
@139c8d018e. Andrew's four messages are quoted verbatim there (section "Andrew's words"); that file is the record of his word.
**Projects:** NFRA_OPLGTW (G1-G5), NFRA_MCPINDEX (I1-I4).

## Spot-checks this seat ran (read-only)

| Claim | Read | Result |
|---|---|---|
| Account id and title are forbidden by contract | `org/standards/NFRA_OPLGTW_CONTRACT.json` `forbidden_field_classes` (equal to the deploy copy, `cmp`) | holds: `raw_account_id`, `account_title`, `tax_identifier`, `mailing_address` + 3 hidden-operand classes |
| Pilot grant is 30 rolling days | same file, `proposed_initial_profile.calendar_days` | holds: 30 |
| Puller admits two masters only | `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1:31` | holds: `ValidateSet('08242234','08335338')` |
| The master travels as a REST parameter | same file `:323` | holds: `$req.MasterAccount = [int[]]@([int]$Master)` |
| Enumerate mode exists and a zero fails loudly | same file `:32`, `:325` | holds: HTTP != 200 dies; `-Mode enumerate` downloads nothing |
| Bucket holds two masters | `aws s3 ls s3://opal-data-assets/schwab/` | holds: `08242234/`, `08335338/` |

Not re-read here: silver row counts and columns (CRO~Z, column metadata only).

## Calls at Andrew

| # | Decision | Recommendation |
|---|---|---|
| A1 (G1) | Return `account_id`, `account_title_line_1` and registration to NAMED internal Opal principals, every such read audited; taxpayer names, tax ids, mailing address, email, phone stay forbidden. Reverses the pilot's ratified rule. | YES, internal principals only, columns as listed |
| A2 (G2) | History depth of a grant | 13 months now (silver holds 560-690 days); since-inception later |
| A3 (G5) | One `-Mode enumerate` run for master `08403355` on the Schwab box: one list request on the existing route, no download. Files back = fully programmatic add; zero = a Schwab-side entitlement (the SI2 GUI over RDP does not grant it either) | YES |
| A4 (I4) | Gateway gains write tools: mail move/folder, Teams send (approval per batch) | DEFER until G1-G3 ship; Alyssa's P0s are all reads |

## Calls this seat rules (fabric-only)

- **G3** -- new datasets from existing silver: unrealized lots (`fact_uln`/`fact_ult`), realized lots
  (`fact_rld`/`fact_rly`/`fact_rty`), account list (`fact_acc`, G1's columns only). RULED: in scope for the next
  NFRA_OPLGTW PRD amendment. The account-list dataset ships only if A1 is yes.
- **G4** -- flow labels on transactions from `fact_trn` codes. RULED: same amendment.
- **I1-I3** -- opalinvest.dev reads as tools, the YCharts 403/404, read-class downloads. RULED: NFRA_MCPINDEX scope;
  I2 is a defect read first (identity or tool).
- **Sequencing** -- NFRA_OPLGTW round 31 (OG-md-1) is in flight under PRD v1.9; the spec is frozen mid-round. The
  amendment carrying G1-G4 lands at the round-31 analysis, not before. A3's enumerate run is independent of the round.

## What bounds this

- Silver tie-out to Schwab totals and partition completeness are unmeasured (CRO~Z section "What bounds this").
- Whether the silver converter takes a third master without change is unread.
