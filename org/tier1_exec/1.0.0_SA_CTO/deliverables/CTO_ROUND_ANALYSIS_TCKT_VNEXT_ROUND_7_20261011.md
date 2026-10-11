# CTO ROUND-7 ANALYSIS -- TCKT_VNEXT -- answering the round-6 L10 slug (2026-10-11 ~23:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D7/TCKT/TCKT_VNEXT/ledger/L10_SLUG_R6.md` @956ad1d547
(2.0.0_SA_COO~V2 msg 6065), sections 3 to 7 read. **Prior:** the round-6 analysis @0b932076f0.
**PRD ADDENDUM 3 (v0.4) is written with this analysis and answers the slug's ENDPOINT question.**

## 1. Where the project stands

FWD-2 is MET for the ticket (the reviewer's grade @86ea741068): another firm's client is refused the ticket, the list and a
missing id, by CLASS; the control was served. For the attached file it is met by the route's firm binding for a firm-scoped
internal caller and NOT READ for a client caller or at the owner check (arm F2, 2.0.0_SA_COO~Y2's cell). FWD-1 not run.

## 2. The slug's question: should "no users row" refuse? YES -- ADDENDUM 3

Ruled in the PRD, v0.4: an internal caller the users table does not know is refused. The code already refuses every other
case in which it cannot establish a scope; the one it admits is the one where it knows least. A row with no firm list still
reads every firm, and that is said, not changed.

## 3. The other items

- **Row D2-S46 (ARMED, owner this seat): any holder of the invoke permission can be any caller.** It is the instrument three
  proofs used today, and it is a fact about the account, not about this project. Who holds `lambda:InvokeFunction` on the
  functions behind the portal authorizer is a census this box cannot make. It is carried to the laptop's CTO, whose lane holds
  IAM, with the three functions this fabric read today. Until that answer the row stays ARMED and is cited in every pair that
  uses a direct invoke.
- **The four staged reads cannot be made from the log.** Accepted as found: each uses the caller's own record of the answer it
  received, supplied with the trigger, or a direct-invoke pair for the ticket's events. No log statement is added to the
  handler to make them possible.
- The reviewer's caveat on FWD-2 is entered in the outcome's record: if a client is ever to open its own ticket, the firm
  fence becomes the only thing between two firms' clients, and it has not been exercised for clients.

## 4. ENRICHMENT LIST for round 7 (ONE issuance, after ADDENDUM 3 is signed)

1. The no-row refusal: built, tested, and its pair (the count of internal users' rows; both arms by direct invoke).
2. The row for the empty firm list (what it means on each surface that reads it), as a read, nothing built.
3. Carried on their named events: the four staged reads; arm F2 and `commentary_sent` on the page (2.0.0_SA_COO~Y2); the
   secret's readers (the laptop); run 3's request id; the crawl and the staff list (Andrew).

## 5. Acts only Andrew can do

- His sitting on an Opal report on DEV (IRPT_YCDGEN PRD FWD-1 ACCEPT).
- Any change of how Opal's automation reaches the vendor: a vendor use no word of his names.
- The crawl and the Ticket Center's staff notification list: parked by his own word.

## 6. What this analysis did not measure

No live read was made by this seat.

-- 1.0.0_SA_CTO~DELL2
