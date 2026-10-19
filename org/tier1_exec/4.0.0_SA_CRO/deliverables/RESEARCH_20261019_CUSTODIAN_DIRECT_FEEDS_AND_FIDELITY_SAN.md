# RESEARCH 2026-10-19 -- custodian direct file feeds (Schwab, Fidelity) and Fidelity "SAN"

**Seat:** 4.0.0_SA_CRO (laptop) | **Risk class:** WORLD (vendor programs, read from public sources) | **Status:** research, no act taken

## The ask (Andrew-direct, ~15:0xZ, at this terminal, VERBATIM)

> Menachem has told me about some FTP solution where we can get all the relevant information for the various masters
> sent in securely direct from schwab and fidelity. This may be the more realistic solution, he said that it costs 15k
> per year from Fidelity, saying its a "SAN" a Separate Advisor Network, which sounds like some tier plan or something
> maybe provided by the custodian, I want you to look into all that and see if that is spomething that is provided by
> the various custodians and the associated details so we can identify if this is a viable mechanism to integrate a
> clean fact table ingestion across the various masters and custodians.

## Findings

1. **"SAN" is Fidelity's Separate Account Network(R), not a data feed.** It is Fidelity's SMA marketplace: advisors
   custodied at Fidelity outsource sleeves to ~700 third-party managers (as of 2024-11-30), with due diligence, manager
   selection, performance reporting and fee billing. Fidelity discloses that its broker-dealers (FBS, NFS) take "flat,
   annual fees" from certain investment managers to keep their products on Fidelity platforms. A ~$15k/yr figure fits
   that manager-side fee; no price is published. A manager on SAN would see only the SAN-enrolled accounts, not a
   partner master's whole book.
   Source: https://clearingcustody.fidelity.com/app/item/RD_13569_45858/separate-account-network.html ;
   https://clearingcustody.fidelity.com/app/proxy/content?literatureURL=%2F9903967.PDF
2. **The product that does what Menachem describes exists at both custodians: the daily custodial data files.**
   - Schwab: Daily Data Files, close-of-business positions, balances, transactions, pricing/security, cost basis, client
     and account profile, grouped by master account; the RIA chooses the files and the delivery method and may route
     them to service providers. Public pages do not name SFTP; delivery options are a Schwab Advisor Services question.
     https://advisorservices.schwab.com/managing-your-business/tech-integration/daily-data-files
   - Fidelity: Wealthscape outbound "data transmission files" (bulk client data from the core brokerage systems on a
     regular schedule), under Wealthscape Integration Xchange; a firm enrolls a recipient with the "Advisor Firm
     Transmission Request" form in the Wealthscape Forms Library; vendor guides report data flowing 7-14 days after
     approval. Fee not published.
     https://www.wealthmanagement.com/financial-technology/fidelity-updates-wealthscape-platform-integration-xchange ;
     https://help.wealthbox.com/hc/en-us/articles/29980365897243-The-Fidelity-Wealthscape-integration
   These are the same feeds Orion, Black Diamond and Tamarac consume.
3. **Authorization runs through the RIA of record.** For a partner's master (49F, Cottonwood/Alongside, Inflection),
   that firm must authorize Opal as a recipient/service provider at the custodian. Opal cannot order it alone.
4. **What Opal has today (repo + registry, read 2026-10-19):**
   - Schwab: two masters (08242234, 08335338) already arrive as Schwab's own daily files, but through the "Schwab Box"
     (EC2 i-0f3d57a97f14727af) riding a human-established Schwab Data Delivery desktop session and its refresh token
     (`data/assets/docs/SCHWAB_AUTO_PULL_DESIGN.md`, `SCHWAB_BOX_ARCHETYPE.md`). Works; fragile by construction.
   - Fidelity: no direct feed. Fidelity accounts reach Opal second-hand: Inflection via Orion (978 accounts
     `Fidelity_Inflection`, 2 `Fidelity_LH`) and "Fidelity IWS" rows via Black Diamond
     (`infra/logic/registry/catalog_fork_keys.json`).
   - Precedent: an inbound SFTP receiver already exists for SMArtX's official file feed
     (`infra/aws/ec2/smartx-sftp/setup-sftp-receiver.sh`), bounded by the 3-hour EC2 reaper.
5. **Risk to weigh:** Fidelity is applying its $100M custody minimum (assets AT Fidelity) to existing RIA clients by
   2027-06-30; firms below must leave. Each partner's at-Fidelity AUM should be checked before building a Fidelity feed.
   https://www.advisorhub.com/fidelity-to-drop-rias-below-100m-custody-minimum/ ;
   https://www.investmentnews.com/ria-news/fidelitys-100m-ria-custody-minimum-impacts-almost-1000-firms/268505

## Verdict

Viable, and the right source for a clean fact table: one daily file set per master per custodian, normalized once per
custodian format into one positions / balances / transactions / account fact schema. Schwab is already parsed (seven
silver tables); Fidelity needs a new parser for its transmission layouts. SAN is the wrong product for this unless Opal
wants to be a listed SMA manager.

## Open questions (owner: Andrew, with Menachem)

1. What is the $15k quote: the SAN manager fee, or a Wealthscape data-transmission fee? Get the document.
2. Which masters sit at Fidelity, under which RIA of record, and will each sign the transmission request naming Opal?
3. Ask Schwab Advisor Services for server-to-server (SFTP) delivery of the daily files for 08242234 and 08335338 (and
   any partner master), retiring the desktop-session ride.

## Addendum 1, ~15:1xZ -- Andrew-direct, VERBATIM

> Check into current holdings in the three schwab masters that we are pulling from. Furthermore we know there is 700m
> for the Fidelity master. The premise here is that there is a "Alongside RIA" this is essentially the master group
> that inflection/cottonwood/49 financial/etc are all part of. I think all the accounts are grouped with Alongside on
> the backend so we should be safely over the 100m limit there. What i need to know explicitly is what needs to happen
> to get this FTP set up immediately.

**Schwab holdings, business date 2026-10-16** (silver `s3://opal-data-assets/schwab/<master>/silver/dim_balance/`,
sum of `net_mv_plus_cash`; position-file market values agree within 0.01%):

| Master | Name on file | Accounts | Net MV + cash |
|---|---|---|---|
| 08242234 | 49 WEALTH MANAGEMENT LLC | 7,599 | $1,782.0M |
| 08335338 | 49 FINANCIAL | 7,690 | $1,843.3M |
| 08403355 | 49 FINANCIAL | 30 | $42.9M |
| **De-duplicated** | | **7,711** | **$1,843.6M** |

The masters overlap: 7,578 accounts appear in both 08242234 and 08335338, and all 30 of 08403355 appear in 08335338.
Summing the three ($3,668M) double-counts. No master on file is named Alongside, Cottonwood or Inflection.

The $700M Fidelity figure is Andrew's; Opal has no direct Fidelity feed to measure it.

## Limits

Public sources only; Fidelity and Schwab publish no fee schedule or SFTP spec for these feeds. Nothing was asked of
either custodian.
