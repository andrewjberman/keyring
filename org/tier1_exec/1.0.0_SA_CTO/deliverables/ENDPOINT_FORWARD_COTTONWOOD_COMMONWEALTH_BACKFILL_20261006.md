# ENDPOINT (step 2, /endpoint --forward) -- the Cottonwood 10-year backfill from Commonwealth

Author `1.0.0_SA_CTO`, 2026-10-06 ~17:1xZ (1:1x PM Eastern). **STATUS: PROPOSED, for Andrew to confirm. NOT LANDED:** no project is
registered and no PRD exists.

**Brief read:** `docs/briefs/cottonwood-commonwealth-10y-backfill-brief-20261006.md` @902feb3a4f (`4.0.0_SA_CRO`, 249 lines, read in
full). Andrew's words: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_16xxZ_COTTONWOOD_COMMONWEALTH_10Y_BACKFILL_SPEC.md`
(the order, and "Disregard MSTR instruction on using a cottonwood specific bucket. We will use the opal-data-asset format").

```
  FWD-1  An analyst picks one Cottonwood account and reads its whole transaction history, 2013 to
         June 2026, from Opal's own store, and can trace each row to the file Commonwealth sent
         DONE WHEN  EXERCISED -- one real account's history read end to end and one row traced back
         ACCEPT     an analyst names one Cottonwood account and reads every transaction Commonwealth
                    recorded for it, oldest to newest, from Opal's store; for any row they can say which
                    delivered file it came from. Nothing is read from Box, from a download folder or
                    from a spreadsheet someone made
         SOURCE     brief PART I, the candidate thread

  FWD-2  Anyone can find the whole Commonwealth delivery in Opal's store, exactly as it arrived
         DONE WHEN  EXERCISED -- each delivered file found and its size and fingerprint matched
         ACCEPT     all five files Commonwealth shipped are in Opal's store, byte for byte, each with its
                    size and fingerprint written down beside it; nobody has to go back to Box or to a
                    download folder for any of it
         SOURCE     brief O1

  FWD-3  An analyst reads each Cottonwood account's monthly and yearly returns, after fees, back
         to 2013
         DONE WHEN  EXERCISED -- one account's returns read across the whole span
         ACCEPT     for any Cottonwood account in the delivery, an analyst reads its monthly, yearly and
                    since-inception returns after fees, with the benchmark Commonwealth recorded beside
                    them, as Commonwealth reported them
         SOURCE     brief O3

  FWD-4  An analyst reads Cottonwood's client relationship records as Commonwealth held them
         DONE WHEN  EXERCISED -- one household read with its people, relationships and activity
         ACCEPT     households, the people in them, how they are related, the advisors, insurance
                    policies and the logged activity are readable as Commonwealth kept them
         SOURCE     brief O4

  FWD-5  An analyst finds any client document by account, type and date, and opens it
         DONE WHEN  EXERCISED -- one statement and one tax form found by account and date and opened
         ACCEPT     a person searches by account, document type and date and opens the one document
                    they need, without unpacking an archive by hand; a document that appears in more than
                    one advisor's archive is listed once
         SOURCE     brief O5; F4 (duplication across the three archives)

  FWD-6  A person can see what this backfill covers and what it does not
         DONE WHEN  EXERCISED -- the coverage read by someone who was not told it
         ACCEPT     a person can tell, for each kind of record, how far back it goes: thirteen years of
                    transactions and returns, ten of activity, twelve months of statements, two tax
                    years, one day of positions; nobody mistakes one for another
         SOURCE     brief O6; F5; PART III item 4

  FWD-7  Cottonwood clients' most sensitive personal details are held only where Andrew decided,
         and a reader can say who can see them
         DONE WHEN  EXERCISED -- the places those details exist listed, and an unauthorised read refused
         ACCEPT     tax numbers, dates of birth, driver's license and passport numbers exist only where
                    Andrew said they may; anyone can list those places and who can read each; a person
                    without that right who tries is refused
         SOURCE     brief O7; F6; PART V

  FWD-8  An analyst can line up an old Commonwealth account with the same client's account today,
         or see that the match is not yet known
         DONE WHEN  EXERCISED -- the match list read for every account in the delivery
         ACCEPT     for each Commonwealth account, a person sees the matching current Cottonwood account,
                    or a plain statement that it is not yet matched, and why
         SOURCE     brief O8
```

## Reachability

All eight need no vendor call and no new box. FWD-7 needs Andrew's decision first (below). Every address needs one registry row
for Commonwealth, added through the naming registry's owner. Gold and anything shown on a page are outside this endpoint (brief
PART II).

## Three calls for Andrew

1. **The sensitive personal details (FWD-7).** Recommended: they stay only in the raw delivery files, which are locked to a small
   named group; the readable tables carry the person without them (a date of birth kept as the birth year only, so ages still
   work). The naming canon's rule is that readable tables keep every column the vendor sent, so this is a declared exception that
   needs his word on record.
2. **Which date labels the delivery.** Recommended: the date in the vendor's files, 2026-06-23, which is what the data describes;
   the day Opal received it, today, is written down beside it.
3. **Where the individual documents live.** Recommended: each unique document is unpacked once and kept on its own, listed by
   account, type and date, so opening one never touches a 1.5 GB archive. The raw archives also stay whole, as received.

## Provenance

GROUNDED ON: the brief, read in full. NOT READ: the delivery itself (the brief's structure counts are the CRO's measurements), the
naming doctrine's text (cited by the brief), any code. NOT CHECKED by this seat: whether the 1,533 accounts are all current or
former Cottonwood clients (the brief says unmeasured).

-- 1.0.0_SA_CTO
