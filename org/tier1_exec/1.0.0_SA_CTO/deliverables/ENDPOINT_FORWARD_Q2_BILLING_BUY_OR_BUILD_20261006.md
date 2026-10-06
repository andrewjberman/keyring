# ENDPOINT (step 2, /endpoint --forward) -- Q-2: advisory-fee billing, buy or build

Author `1.0.0_SA_CTO`, 2026-10-06 ~19:5xZ (3:5x PM Eastern). **STATUS: PROPOSED, for Andrew to confirm. NOT LANDED.**

**Brief read:** `docs/briefs/q2-billing-buy-or-build-brief-20261006.md` @cf7721ed30 (`4.0.0_SA_CRO`, 131 lines, read in full); its research
`docs/briefs/q2-billing-desk-research-20261006.md` was NOT read (cited by the brief). Andrew's words: `..._183xZ_FOUR_BOX_ACCELERATION_PROJECT_CENSUS_AND_Q4_GOALS.md`
(under `org/tier1_exec/4.0.0_SA_CRO/deliverables/`).

**Proposed register shape (L3, this seat's call):** ONE new project, `ADVI_BILLING` (D8/ADVI, the per-firm stacks). It relies on the
Q-1 programme for values, flows and households, and owns the fee agreements, the engine choice, the Schwab fee file and the fee
display. Plaid, DTCC and home values stay out, by Andrew's own correction.

```
  FWD-1  One 49 Financial household's fee for one past quarter is worked out outside Black Diamond, shown
         in Opal, and matches what Schwab actually took
         DONE WHEN  EXERCISED -- one already-billed quarter recomputed for one household and compared
                    with the actual fee debit
         ACCEPT     for one 49 Financial household and one quarter that has already been billed, the fee
                    is worked out from Opal's own account values and flows, an advisor reads it in Opal,
                    and it equals the fee Schwab debited, or the difference is shown with its reason
         SOURCE     brief PART I, the candidate thread

  FWD-2  Andrew knows who works out each firm's fees today, and how
         DONE WHEN  EXERCISED -- the answer read for 49 Financial and Cottonwood, confirmed by each firm
         ACCEPT     for each firm, Andrew reads which system bills today, on what terms, who signs off each
                    run, and where any Morningstar product sits; each firm agrees the description is right
         SOURCE     brief O1; PART V, the firms' answers

  FWD-3  An advisor sees each client's fee in Opal, with how it was worked out
         DONE WHEN  EXERCISED -- one client's fee read with every step shown
         ACCEPT     an advisor reads a client's fee per account and household and sees the value it was
                    charged on, the schedule and tiers, any adjustment for money moved in or out during
                    the quarter, and anything left out; they can answer "why is my fee this number?"
         SOURCE     brief O2; PART III item 2

  FWD-4  Every client's fee traces to the agreement term that set it
         DONE WHEN  EXERCISED -- one fee traced to its agreement, with the agreement's history
         ACCEPT     for any client's fee, a person reads the agreement term behind it, from when it applied
                    and every change to it; a regulator's question about a fee is answered from that one
                    record
         SOURCE     brief O4; PART III item 3

  FWD-5  The quarter's Schwab fee file is produced without Black Diamond
         DONE WHEN  EXERCISED -- one quarter's file produced and checked account by account, before any
                    upload
         ACCEPT     the file Schwab accepts for a quarter's fees is made without Black Diamond, every account
                    in it checked before anyone uploads it; nothing is uploaded except by the person who
                    does it today, on Andrew's word
         SOURCE     brief O3

  FWD-6  Andrew chooses buy or build knowing the price, the risks and what each firm does today
         DONE WHEN  EXERCISED -- Andrew reads the comparison and records his choice
         ACCEPT     Andrew reads, side by side, the billing products that accept uploaded values and an
                    Opal-built engine: what each costs, what each risks, and how each fits what the firms do
                    today; he can make the call from it
         SOURCE     brief O5; PART III item 4
```

## Calls for Andrew

1. **Buy or build is yours (FWD-6)**; the research leans "buy and front" for January. REC: decide after FWD-2 and FWD-1 are done.
   Recomputing one past quarter in Opal tells you how much engine is really needed before any vendor talk.

## Acts only Andrew can do

The firms' answers (today's billing system, registration, fee terms, sign-off) and any vendor conversation (brief PART V).

## Provenance

GROUNDED ON: the brief, read in full. NOT READ: the research file, any firm data, the `blackdiamond_list_fees` gateway tool (not
called; a call would be a vendor-data read needing its own word).

-- 1.0.0_SA_CTO
