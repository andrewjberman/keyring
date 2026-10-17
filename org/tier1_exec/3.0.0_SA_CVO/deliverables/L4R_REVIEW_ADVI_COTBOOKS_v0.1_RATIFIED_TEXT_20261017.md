# L4-R review -- ADVI_COTBOOKS PRD v0.1 @087fb97ca4, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-17 ~03:3xZ. Delivered by 1.0.0_SA_CTO~DELL1 msg 7202 (acked). Half hash `b3b6a73a5078`.
**Read:** the whole PRD at 087fb97ca4; open call `dell1-20261017T030813Z-0cf5` in `org/devices/state/dell1/open_calls.json`; the counterpart
MDPF_CANON PRD v2.24 FWD-10.

## Verdict: REFUSE (two grounds; both are fixed before Andrew confirms, in one pass)

## Ground 1 -- the ENDPOINT is not yet ratified

The PRD says it itself: "Andrew's confirmation is held on the box's open calls (`dell1-20261017T030813Z-0cf5`). This PRD goes to L4-R only
after he confirms." At this review the call reads `"state": "OPEN"`, `"closed": null`, escalated to Andrew at 03:17:38Z. Its header also
reads `"status": "DRAFT"`. There is no ratified pin to read the ENDPOINT against verbatim, so this half cannot be signed yet. Re-deliver
after he confirms, with the ENDPOINT re-pasted if he changes a line.

## Ground 2 -- FWD-2 contradicts C-SCOPE

- **FWD-2:** "Every Cottonwood account belongs to exactly one advisor's book". Its DONE WHEN says "no account sits in two books, none is
  lost", and its ACCEPT says "none goes missing".
- **C-SCOPE:** "Books cover the supervised book only ... Unsupervised accounts appear in no book." This follows MDPF_CANON FWD-10
  (Andrew-direct ~01:0xZ and ~01:5xZ).
- **The conflict:** read as written, FWD-2 fails on every Unsupervised account, which C-SCOPE deliberately keeps out of every book.
- **Fix:** put the population in FWD-2 itself, for example "Every supervised Cottonwood account belongs to exactly one advisor's book".
  Change the DONE WHEN's "none is lost" to count over the supervised accounts of the pull. Because the ENDPOINT is still unconfirmed, the
  fix costs nothing now; after confirmation it would be an ENDPOINT change and a re-sign.

## Read and found sound (carried to the re-delivery, so it can be signed quickly)

- **C-BOOK and C-RULE are deterministic and readable.** The order of steps, `book_rule` and `shared_with` are named, and the
  reordered-copy proof catches any dependence on file order. This is a value carrying its claim.
- **C-SCOPE ties to MDPF_CANON FWD-10.** The book totals sum to the supervised firm total to the cent. The two PRDs agree.
- **C-OWNER places the writer correctly:** `A_00` is ADVI_COTBKF's, so the rule cell is cut there first. One writer, named.
- **C-AUTHZ checks on the server, not only in the page,** and its proof is a refused request at the service.

## Nits (not grounds)

1. **C-RULE's count.** It says "(1 today)" for accounts in two or more named advisor groups, and also "the 11 Shipley-shared accounts land
   in Shipley's book". If the 11 are shared with "No Advisor", they resolve at step (2), not step (3). Say which, so the proof's expected
   count is unambiguous.
2. **FWD-4 waits on Andrew.** It depends on C-ROSTER's mapping, which only Andrew supplies. Under rule 27 L2, a necessary wait is stated
   on the outcome with its reason and Andrew's word. Name it there, or in OPEN AT ANDREW against FWD-4.
3. **FWD-3 compares two different populations.** If Black Diamond's group view counts Unsupervised accounts, every book will differ by
   them. C-TIEOUT's "every difference named" covers this, but the tie-out cell should check which population BD's group view counts
   before it reads any differences.

-- 3.0.0_SA_CVO
