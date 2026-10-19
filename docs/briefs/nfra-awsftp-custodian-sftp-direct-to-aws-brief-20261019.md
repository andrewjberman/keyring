# NFRA_AWSFTP -- custodian daily files by SFTP, straight into AWS (L1 brief)

**Author:** `4.0.0_SA_CRO` (laptop) | **Date:** 2026-10-19 | **Mode:** NEW | **Consumer:** `1.0.0_SA_CTO` `/endpoint --forward`

**Andrew-direct, 2026-10-19 ~15:2xZ, at the 4.0.0_SA_CRO terminal, VERBATIM:**

> Yes write the brief. This should go into NFRA_AWSFTP. I would prefer to run it direct into AWS, so that is how it
> should be designed.

The ask it answers (same session, ~15:1xZ, VERBATIM): "What i need to know explicitly is what needs to happen to get
this FTP set up immediately." The research behind it, with its own verbatim asks and sources:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_CUSTODIAN_DIRECT_FEEDS_AND_FIDELITY_SAN.md`.

**Design direction, fixed by Andrew's word:** the custodians deliver by SFTP to an endpoint Opal runs IN AWS, landing
directly in S3 (a managed SFTP service writing to S3). Not a desktop session, not a box in the office, not a vendor
in the middle.

---

## PART I -- THE OUTCOME TERRITORY

### Candidate thread (becomes FWD-1)

**An Opal operations person opens one Schwab master's positions for yesterday in the fact table, and those rows came
in by SFTP to AWS with nobody logging in to anything.** Coarse grain: one firm (49 Financial), one Schwab master
(08242234, whose files Opal already parses), one business date. Every hop in between (custodian sends, AWS receives,
file kept as sent, parsed, readable) is exercised once, end to end. The thread can be driven on demand before Schwab
ever sends a file: Opal pushes a recorded file set through the same endpoint under a test credential, and the
custodian's first real delivery is the organic case. The other outcomes are enrichment.

### O1 -- Operations sees each master's daily files arrive without anyone keeping a session alive

Menachem (or any ops person) can say, for each Schwab and Fidelity master, that today's files came in, without any
Opal person keeping a desktop login, a refresh token or a Windows box alive for it. The thing it displaces is the
Schwab Box, where a lapsed human-established session silently stops the feed.

### O2 -- A custodian reaches one Opal endpoint in AWS and can touch only its own drop

Schwab's and Fidelity's file-transfer teams each connect to one stable Opal SFTP address with their own key-based
credential. Each sees only its own landing folder, cannot list or read another custodian's or another firm's files,
and cannot delete what it already sent.

### O3 -- Anyone can read, per master per business day, whether the expected files arrived

An ops person, or an agent, reads one record that says for each master and trading day: which files arrived, when,
and whether the set is complete, late or missing, judged against the trading calendar (Friday's files are Monday's
answer). It is a record to READ. It sends nothing (see Part II, the alert moratorium).

### O4 -- Every file is kept exactly as the custodian sent it

An auditor or an engineer re-running a parse can retrieve the byte-for-byte file a custodian delivered on any past
date, with when it arrived and from which credential, and prove it was not altered.

### O5 -- One fact table across custodians and masters

An analyst asks "what did account X hold, what was its cash, what moved" and gets the same columns whether the
account is custodied at Schwab or Fidelity, each row saying which custodian and master it came from. They no longer
need to know that Schwab and Fidelity name the same idea differently.

### O6 -- An account under several masters counts once

A firm-level AUM figure built on the fact table counts each account once, even where one account appears under two or
three masters. Measured today: summing the three Schwab masters counts $3.67B; the distinct accounts hold $1.84B
(Part VI).

### O7 -- Each firm's accounts stay in that firm's home, even from a shared master

When one custodian master carries accounts of more than one firm (the Fidelity master Andrew describes as grouped
under Alongside, spanning Inflection, Cottonwood and 49 Financial), each firm's accounts land and are read only in that
firm's home. No pipeline reads another firm's data.

### O8 -- Adding a master or a custodian is a registry row and a credential, not a new pipeline

When a partner opens a new master, or a third custodian appears, an engineer adds its registry row and issues its
SFTP credential, and its files flow through the same landing, record and fact table.

### O9 -- The desktop-session pull retires, master by master, in one move each

For each Schwab master, the switch from the Schwab Box pull to SFTP is a single cutover with a same-window rollback.
No long side-by-side run and no standing comparison job (Andrew's veto on shadow pipelines and parity comparators).

---

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:**
- the SFTP endpoint in AWS, its custodian credentials and their isolation (O2);
- the landing of raw files in S3, and the per-master arrival record (O3, O4);
- the Fidelity file parser into silver (new; no Fidelity parser exists);
- the cross-custodian fact table's shape and its de-duplication rule (O5, O6), and the per-firm split at landing (O7);
- the cutover of each Schwab master from the Schwab Box to SFTP (O9).

**It relies on, and does not own:**
- **The custodian paperwork.** Signed by each master's firm of record, driven by Andrew and Menachem: Fidelity's
  outbound transmission rule per G-number, or its "Advisor Firm Transmission Request"; Schwab Advisor Services
  switching the daily files to SFTP delivery. This project cannot order a feed itself.
- **The existing Schwab silver parsers** and their consumers: the silver tables under
  `opal-data-assets/schwab/<master>/silver/` (dim_balance, dim_position, dim_transaction, fact_*), and
  `data/canonical/schwab/`. The SFTP landing feeds those parsers the same files they read today. It does not rewrite
  them.
- **Consumers it must not break:** MDPF (gold), TCKT_EARLYWARN (reads Schwab silver daily), NFRA_OPLGTW (the gateway's
  Schwab tools), IRPT, ADVI.
- **The LGIC registry and naming builders.** `lib/opal_naming.py` `address()` and `name()`, and the rows in
  `infra/logic/registry/`, owned by `4.0.0_SA_CRO` for rows.
- **AWS applies.** CloudOps, under the deploy ledger and never-widen sign-offs.

**Siblings, named:**
- **ADVI_SCHWABAUTO / OPAL_ASSETS C3** is the Schwab Box pull this replaces. It keeps running until each master's
  cutover (O9).
- **NFRA_FIDUPL** (dell1, D8; brief `docs/briefs/auto-fidelity-uploader-brief-20261019.md`) is the live half of the
  Fidelity route off Black Diamond. It lands the Wealthscape daily custom export (accounts, positions, balances,
  prices, securities, transactions) through a signed-in session. Per `1.0.0_SA_CTO` msg 109859 and record
  `ANDREW_DIRECT_20261019_184xZ_CLUSTER_PRIORITIES_PER_BOX_COHERENCE.md` (b3785dd745), this brief is the held half,
  and the two share ONE Fidelity landing home. The Fidelity silver parser and landing address are designed once,
  across both.
- **The SMArtX SFTP receiver** is the EC2 listener at `infra/aws/ec2/smartx-sftp/`. Out of scope. Folding it into this
  endpoint later is a consolidation choice for its own owner, not a rider here.
- **Orion and Black Diamond feeds.** Today these are the only path for Fidelity accounts (Inflection via Orion, Fidelity
  IWS via Black Diamond). They stay. Whether the direct Fidelity feed retires either one is not decided here.

**Explicitly not this project:**
- **Alerts, notifications or monitors of any kind.** The standing moratorium (CLAUDE.md section 5) holds; O3 is a
  record to read.
- **Fidelity's Separate Account Network.** It is an SMA marketplace, not a data feed (research file, finding 1).
- **Any trading or order flow to custodians.**

---

## PART III -- THE QUALITATIVE BAR

- Menachem stops asking "did Schwab come in today": he reads the answer himself, and it is right on a Monday morning
  after a Friday close.
- On the morning a Schwab master's feed fails, the reason reads as a custodian-side or a transport-side fault. It never
  reads as "an Opal person's session lapsed".
- A partner's compliance reviewer, shown the design, can confirm that a custodian credential cannot reach another
  custodian's files or another firm's accounts, from the configuration alone.
- An analyst comparing a Fidelity account with a Schwab account in the fact table does not have to look up which
  custodian calls cash what.
- The firm-level total that used to double-count accounts present under two masters now matches the count an ops
  person would make by hand.

---

## PART IV -- THE SUBSTRATE (findings, each measured 2026-10-19)

1. **No managed SFTP exists in the estate.** `aws transfer list-servers` returned `"Servers": []`.
2. **The Schwab data already arrives as Schwab's own daily files**, but through a desktop session. Three masters land
   in `s3://opal-data-assets/schwab/{08242234,08335338,08403355}/bronze/<feed>/`. 08242234 shows 17 feed folders: acc,
   rld, rlu, rlw, rly, rps, rtu, rty, sec, tcf, tcfx, tnn, trn, uln, ult, upn, upt. They are pulled by the Schwab Box
   (EC2 `i-0f3d57a97f14727af`), which rides a human-established Schwab Data Delivery session and its refresh token in
   Administrator's Windows vault (`data/assets/docs/SCHWAB_AUTO_PULL_DESIGN.md`, `SCHWAB_BOX_ARCHETYPE.md`). This is
   the failure class O1 removes.
3. **The silver parsers exist and are current.** Silver `dim_balance` and `dim_position` for all three masters carry
   business date 2026-10-16, the T-1 frontier for a Monday read.
4. **The naming builders already home Schwab master bronze.**
   - `address('schwab','08242234','bronze','trn','date=2026-10-16')` returns
     `s3://opal-data-assets/schwab/08242234/bronze/trn/date=2026-10-16`.
   - The same call for 08403355 REFUSES: `scope '08403355' resolves to no scopes.json row`.
   - A Fidelity call REFUSES: `source 'fidelity' is not a systems.json key`.
   - `name()` has no kind for a managed SFTP server or user: `transfer` and `server` both refuse.
   Each refusal is a missing registry row (CLAUDE.md rule 30), not a reason to hand-type.
5. **Firm tenancy is registered for three firms:** 49financial, inflection and cottonwood, each with its own bucket.
   - Schwab masters 08242234 and 08335338 are MASTER rows under 49financial.
   - Cottonwood's master row is `z09` (Black Diamond); Inflection's is `4698` (Orion).
   - There is no row for any Fidelity master and no "alongside" firm.
6. **A precedent for inbound SFTP exists, and it is the shape to avoid copying.** The SMArtX receiver is an EC2 listener
   squeezed into a window under three hours, because the estate's idle-instance reaper takes any box that sits
   above three hours at under 1% CPU (`infra/aws/ec2/smartx-sftp/setup-sftp-receiver.sh`). A managed SFTP service has
   no idle box for that reaper to take. This is one reason Andrew's "direct into AWS" fits the estate better than
   another listener box.
7. **Fidelity reaches Opal only second-hand today.** Orion carries 978 `Fidelity_Inflection` accounts and 2
   `Fidelity_LH`. Black Diamond carries "Fidelity IWS" rows (`infra/logic/registry/catalog_fork_keys.json`).

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- **Fidelity authorizations.**
  - The firm of record on the Fidelity master (Andrew believes Alongside) supplies its G-number(s).
  - It adds an outbound transmission rule per G-number in Integration Xchange, or files the Advisor Firm Transmission
    Request naming Opal as recipient.
  - A Letter of Understanding may need to be on file.
  - Vendor-reported lead time is 7-14 days after approval (research file, sources).
- **Schwab delivery change.** 49 Financial asks Schwab Advisor Services to deliver the daily files for the three masters
  by SFTP to Opal's endpoint. Schwab does not publicly document SFTP delivery, so whether it is offered is the open
  question.
- **The $15k Fidelity figure.** Is it a data-transmission fee, a Separate Account Network manager fee, or something
  else? Unresolved.
- **Push or pull, and network terms.**
  - Does each custodian push to Opal, or expect Opal to pull from it?
  - Does it need a fixed IP to allowlist?
  - Does it need PGP on top of SFTP?
  The endpoint's shape follows the answers.
- **The Fidelity file layouts** come from Fidelity (fixed-width or delimited), and the parser waits on them.
- **Registry rows** (CRO lane), each named by a refusal in Part IV finding 4:
  - a scope row for 08403355;
  - a `fidelity` source in `systems.json`;
  - a scope row for each Fidelity master and its firm tenancy;
  - NAMING_SCHEMA kinds for the SFTP server and its users.
- **A ruling on a multi-firm master's landing home.** The Fidelity master spans firms, and per-firm buckets forbid
  reading one firm's data from another's tree. So either the file is split by firm on landing, or a master-level home
  is ruled, with its cross-firm guard named.
- **Personal data.** Custodian files carry SSNs and names. The PRD needs:
  - whether to ask Fidelity for SSN masking, given that the fact table keys on account number;
  - KMS on the landing prefixes;
  - who may read bronze.
- **Never-widen sign-offs** for any write into a firm bucket or the client-data monolith (CLAUDE.md section 5).
- **Account identity across masters.** A rule for which master's row wins when one account appears under several (O6).

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-19 ~15:1xZ by `4.0.0_SA_CRO`, from silver `dim_balance` at business date 2026-10-16. The figure is
the sum of `net_mv_plus_cash`, and the position-file market values agree within 0.01%.

| Master | Name on file | Accounts | Net MV + cash |
|---|---|---|---|
| 08242234 | 49 WEALTH MANAGEMENT LLC | 7,599 | $1,782.0M |
| 08335338 | 49 FINANCIAL | 7,690 | $1,843.3M |
| 08403355 | 49 FINANCIAL | 30 | $42.9M |
| distinct accounts across all three | | 7,711 | $1,843.6M |

- 7,578 accounts appear under both 08242234 and 08335338. All 30 of 08403355 appear under 08335338.
- The Fidelity master is about $700M, per Andrew. Opal cannot measure it today.
- Fidelity's $100M custody minimum counts assets held at Fidelity and applies to existing RIA clients by 2027-06-30.
  Andrew's premise is that the Alongside grouping puts this master well above it.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **No custodian was contacted.** Delivery methods, fees, lead times and layouts come from public pages and vendor
  guides, several of them years old.
- **Schwab SFTP delivery is unconfirmed.** If Schwab offers only its desktop tool or an approved-vendor route, O1 and
  O9 for Schwab change shape.
- **Not verified:**
  - that Alongside is the firm of record on the Fidelity master;
  - the $700M figure;
  - which firms' accounts that master holds.
- **No price is given** for the managed SFTP service or Fidelity's feed. Part III forbids inventing one.
- **The fact table's column list is not designed here.** Neither is the choice of which existing silver tables it reads.
- **"Alongside" as the umbrella RIA comes from Andrew's description.** No registry row or file Opal holds names it.

---

## REFS

```
  BRIEF PATH        docs/briefs/nfra-awsftp-custodian-sftp-direct-to-aws-brief-20261019.md
  PROJECT           NFRA_AWSFTP (named by Andrew; not yet registered -- L3, 1.0.0_SA_CTO)
  EXISTING PRD      NONE
  SIBLING PROJECTS  NFRA_FIDUPL (dell1; shared Fidelity landing home), ADVI_SCHWABAUTO / OPAL_ASSETS C3 (Schwab Box
                    pull), SMArtX SFTP receiver, TCKT_EARLYWARN,
                    NFRA_OPLGTW, MDPF, IRPT, ADVI (consumers of Schwab silver)
  PRIOR ART         data/assets/docs/SCHWAB_AUTO_PULL_DESIGN.md; data/assets/docs/SCHWAB_BOX_ARCHETYPE.md;
                    infra/aws/terraform/canonical-schwab-ec2/; infra/aws/ec2/smartx-sftp/setup-sftp-receiver.sh;
                    Schwab silver under s3://opal-data-assets/schwab/<master>/silver/; data/canonical/schwab/;
                    infra/logic/registry/scopes.json; lib/opal_naming.py
  RESEARCH          org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_CUSTODIAN_DIRECT_FEEDS_AND_FIDELITY_SAN.md
  MEASURED AT       2026-10-19 ~15:1xZ (holdings, business date 2026-10-16; registry and builder probes; Transfer list)
```
