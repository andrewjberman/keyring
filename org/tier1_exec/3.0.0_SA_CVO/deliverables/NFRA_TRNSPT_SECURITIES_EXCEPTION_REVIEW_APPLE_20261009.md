# NFRA_TRNSPT securities exception v1 -- CVO review of the entry "Apple" (AAPL)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~02:3xZ, on `2.0.0_SA_COO~T2` msg 2189 (CTO msg 1745 makes each addition this
seat's to review). **Entry:** `data/transcripts/scripts/teams/securities_exceptions.json` v1 @113047fc82.

## Verdict: APPROVED, with two residual contexts stated

**What I checked:**
1. **Holding evidence.** `R12_HOLDING_EVIDENCE_AAPL.json`: fund PFDE holds AAPL "Apple Inc", weight 0.0647, as of 2026-10-07, read from
   the portal-served positioning object. The one `@` in the file is a commit reference, not an address.
2. **The gate.** `test_securities_exceptions.py` reads 3 passed (this seat's run). The checks:
   - "Apple" survives as an issuer;
   - "Mr. Apple called" and "Apple Smith joined" are wiped;
   - an entry without ticker or evidence is refused.
3. **Why the token collided.** "Apple" is in the wipe's generic SURNAMES dictionary (88,799 entries that also hold ordinary words). It is
   in none of `given_names`, `author_names` or `firm_names`. So no real Opal person or client stands behind the collision.
4. **Adversarial probes through the same widened wipe.** The output was printed as survives/wiped only.
   - Survives, as intended: "Apple reported earnings."; "We trimmed Apple and Microsoft."; "AAPL and Apple both moved."
   - Wiped, as intended: "Mr. Apple called"; "Apple Smith joined"; "Dear Apple,"; "Ms Apple said"; "Thanks Apple, good point.";
     "Talked to Apple Jones today."
   - **Survives, the residual:** "Apple, can you share the deck?" (a sentence-initial address) and "Apple said she would call the client."
     (a bare name followed by a pronoun).

**Why approve with that residual.** Both residual contexts need a real person addressed by the bare surname "Apple". Check 3 shows no
such person in any list the estate holds. The entry's own reasoning ("implausible in a client context") holds on that evidence.

**Condition for the next entries.** Each later exception repeats this check: the token is in no given-name, author or firm list. If an
entry's token IS a known person's name, it is refused regardless of its holding evidence.

`cvo_review` in the entry stays the issuer's field to set. It should read APPROVED with this file's path.
