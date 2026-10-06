# L1 BRIEF -- Q-2: advisory-fee billing, buy or build

- **Author:** `4.0.0_SA_CRO` (L1), 2026-10-06 ~19:5xZ (3:5x PM Eastern). **Mode:** NEW (research phase).
- **Order:** Andrew-direct 2026-10-06 ~18:3xZ, voice transcript verbatim in
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_183xZ_FOUR_BOX_ACCELERATION_PROJECT_CENSUS_AND_Q4_GOALS.md`:

  > we're going to make number two solely focused on billing that means that we simply need to figure out who manages
  > billing and how they manage it i i think that uh that morningstar wealth buy all platform is is the way that
  > they're all doing it we need to figure out if it's a buy or build play here if we can basically front that
  > relationship we just sit in front of it we just provide an easy user interface that ports them over there i think
  > that's probably the easiest solution but we need to assess feasibility for that we need to understand what that
  > looks like we need to understand the demands of billing and what is expected what information is required for this
  > where it has to go and what workflows overlap with it

  Public web research approved ~19:2xZ ("4.) Yes"; read-only, no vendor accounts or API calls).
- **Evidence:** `docs/briefs/q2-billing-desk-research-20261006.md` ("the research"; 40 public sources, cited by number).
- **Consumer:** `1.0.0_SA_CTO`, `/endpoint --forward` at L2. Andrew said he will bring counterparty information "in the
  weeks to come"; this brief is the first version.

---

## PART I -- THE OUTCOME TERRITORY

### The candidate thread

**One 49 Financial billing group's quarterly fee, computed outside Black Diamond and shown in Opal.** For one household,
the fee for one quarter is calculated from Opal's custodial values and flows, produces the Schwab fee file and the
client's fee statement, and an advisor reads it in Opal. The first run reproduces a quarter already billed, and matches
the fee Schwab actually debited.

### O1 -- Andrew knows who calculates each firm's fees today, and how

For 49 Financial and Cottonwood: which system bills (Black Diamond, Orion, a spreadsheet), on what terms, and where
Morningstar sits in the chain. The research's reading (section 4): the "buy all" product is almost certainly Morningstar
ByAllAccounts, which gathers account data and does not bill; Morningstar's billing product (Morningstar Office) was
retired on 2026-02-28 and its users were steered to Black Diamond.

### O2 -- An advisor sees each client's fee in Opal, with how it was calculated

The billable value, the schedule and tiers, proration for flows, and exclusions, per account and household.

### O3 -- The quarter's Schwab fee file is produced without Black Diamond

The file Schwab Advisor Center accepts, with each account validated before upload (research section 5).

### O4 -- Each client's fee can be traced to the contract term that produced it

The fee agreement per account or group, effective-dated, with an audit history. This is the SEC's most-cited fee
problem area (research section 5, source 9).

### O5 -- Andrew can choose buy or build on measured facts

A comparison of the standalone billing vendors that take uploaded values (the research names Envestnet BillFin and
SmartKx; Altruist only on Altruist custody) against an Opal-built engine, with the risks of each.

---

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:** the inventory of today's billing per firm, the fee-agreement record, the choice of engine, the
Schwab fee-file path, and the fee display in Opal.

**It relies on, and does not own:** the custodial values, flows and households (the Q-1 programme and its projects); the
Opal portal; any vendor contract (Andrew's).

**Out of scope, by Andrew's own correction in the transcript:** the integrations he named (Plaid for banking, DTCC for
insurance and annuity data, a home-value API). They are a later project.

---

## PART III -- THE QUALITATIVE BAR

1. No client is billed a different amount because Opal took over.
2. An advisor can answer "why is my fee this number?" from Opal alone.
3. A regulator's question about any fee is answered from one record.
4. Andrew decides buy or build knowing the price, the risks and what each firm does today.

---

## PART IV -- THE SUBSTRATE: what exists, measured

- **F1. Billing is a defined calculation** with defined inputs (values, flows, open and close dates, households, fee
  schedules, custodian identifiers) and outputs (per-account fee, custodian file, invoice, payout report, audit
  history) (research section 2).
- **F2. Opal already holds most of the inputs** for 49 Financial: Schwab custodial data (Q-1 brief F1) and households.
  Fee schedules per agreement are not known to be held anywhere in Opal.
- **F3. Opal may already read Black Diamond's fee data:** the Opal gateway exposes a tool named `blackdiamond_list_fees`
  (present in this session's tool list; not called).
- **F4. Standalone billing engines exist** that accept uploaded values (research section 3).
- **F5. The custodian path is a file** uploaded to Schwab Advisor Center; Schwab is changing account-number formats now
  (research section 5).

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- **The firms' answers** to the research's section 7 questions: today's billing system; SEC or state registration
  (state registration adds itemized-invoice rules); fee terms per agreement; custodians beyond Schwab; whether clients get
  invoices; who signs off each run.
- **A commercial conversation** with any vendor is Andrew's; no seat contacts a vendor.
- **The first live run's timing:** with the switch at 2027-01-01, the first live bill is the 2026 Q4 arrears bill or the
  2027 Q1 advance bill, in early January 2027 (research section 6, an inference).
- **A one-time conversion check** (recompute the last billed quarter, reconcile to the actual debits), never a standing
  comparator.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-06 ~19:2xZ to ~19:5xZ. No project is registered for billing. Research done from public sources only.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- The research's vendor facts come from public sources and were not checked against the vendors; several are marked
  UNCONFIRMED in the research.
- It does not recommend a vendor. The research leans to "buy and front" for the January cutover; the choice is Andrew's.
- It does not know either firm's fee agreements.

## REFS

```
  BRIEF PATH        docs/briefs/q2-billing-buy-or-build-brief-20261006.md
  RESEARCH          docs/briefs/q2-billing-desk-research-20261006.md
  PROJECT           NONE-YET
  ANDREW'S WORDS    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_183xZ_FOUR_BOX_ACCELERATION_PROJECT_CENSUS_AND_Q4_GOALS.md
                    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_192xZ_DELLS_SECHIST_LIFT_PUSH_RHYTHM_RESEARCH_EGRESS_Q3_OPS_WORKFLOW.md
  RELIES ON         the Q-1 programme (docs/briefs/q1-custodial-investor-reporting-programme-brief-20261006.md)
  MEASURED AT       2026-10-06 ~19:2xZ to ~19:5xZ
```
