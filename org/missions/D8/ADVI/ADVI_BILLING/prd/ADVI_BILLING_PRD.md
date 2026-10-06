# ADVI_BILLING -- Q-2: advisory-fee billing, buy or build: fees worked out from Opal's own data, traced to the agreement, the Schwab fee file without Black Diamond

```json
{
 "project": "ADVI_BILLING",
 "directive": "D8",
 "fabric": "laptop",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/q2-billing-buy-or-build-brief-20261006.md@cf7721ed30",
 "endpoint_outcomes": [
  "FWD-1",
  "FWD-2",
  "FWD-3",
  "FWD-4",
  "FWD-5",
  "FWD-6"
 ],
 "status": "RATIFIED"
}
```

**Author:** `1.0.0_SA_CTO` (L2-L4), 2026-10-06. **Brief:** `docs/briefs/q2-billing-buy-or-build-brief-20261006.md@cf7721ed30`. **Endpoint proposal:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_Q2_BILLING_BUY_OR_BUILD_20261006.md`.
**Confirmed by Andrew:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_210xZ_SEVEN_CALLS_RDP_LOCK_Q1_Q2_Q3_CONFIRMED_NO_BD_SHAPE.md`. **Sign-off:** `3.0.0_SA_CVO` signs the ratified-text half; the brief half is accepted because the CRO
wrote the brief. **COO:** UNSEATED at registration; seating is `0.0.0_AB_MSTR`'s on Andrew's word.

## ENDPOINT (step 2, /endpoint --forward)

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

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-NO-VENDOR-YET | Andrew ~19:5xZ ("not yet") | No seat contacts a billing vendor; the comparison (FWD-6) is built from public sources and Opal's own trial. |
| C-TRIAL-FIRST (FWD-1) | Andrew, call 5, "rec approved" | The first act recomputes one already-billed 49 Financial quarter for one household from Opal's data and the fee lines Opal already holds, compared once with the actual debit (a one-time check, never a standing comparator). |
| C-NO-UPLOAD (FWD-5) | brief | The fee file is produced and checked; it is uploaded only by the person who does it today, on Andrew's word. |
| C-SHAPE | Andrew, Q-1 call 6 | Inputs come in the custodian's shape (IRPT_CUSTDY C-SHAPE); Black Diamond's fee data is a reference, not the model. |
| C-FIRM / C-NAMES / C-MORATORIUM | law | One firm per key; names are builder output; no alert or monitor. |

## THREAD -- FWD-1, round 1

FWD-1 as written above is round 1's one journey, every hop real; the other outcomes are the enrichment
backlog in their numbered order.

-- 1.0.0_SA_CTO
