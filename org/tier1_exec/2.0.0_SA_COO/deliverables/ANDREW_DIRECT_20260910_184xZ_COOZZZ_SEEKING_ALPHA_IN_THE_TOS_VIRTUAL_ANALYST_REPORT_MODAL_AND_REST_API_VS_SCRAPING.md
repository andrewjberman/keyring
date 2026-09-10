# ANDREW-DIRECT 2026-09-10 ~18:4xZ -- Seeking Alpha belongs in the AMGT_RESAPP task orders: the `virtual_analyst_report` modal, and the authenticated REST API explored against scraping

**archetype:** SCRIBE (record) - **recorded by** `2.0.0_SA_COO~ZZZ` - **terminal:** the `2.0.0_SA_COO~ZZZ` terminal (the lane Andrew spawned for `AMGT_RESAPP`)
**channel:** typed into this session mid-turn, between this lane's tool batches; bracketed by the lane's own clock read at `2026-09-10T18:42:22Z` (the message was surfaced with the batch before that read)

> **WHY THIS FILE EXISTS.** `org/XXX.md`: *"ANY AGENT RECEIVING AN ANDREW-DIRECT INSTRUCTION RECORDS IT DURABLY AND BROADCASTS IT -- SAME TURN. DURABLE: a commit quoting him VERBATIM. NEVER A PARAPHRASE. THE PHRASING IS THE RULING. SCOPE: The receiving agent does NOT adjudicate scope. SURFACE, DO NOT ADJUDICATE."* This is that commit. Section 1 is his words and nothing else; sections 2-3 surface what they touch and name the owners; nothing here decides anything.

---

## 1. THE WORDS, VERBATIM AND COMPLETE

One message, quoted in full:

> **"Something I want to fold in to your TOs, there should be a section somewhere in there on Seeking Alpha, pulling info from it and testing SA etl. I want to note that this is a good page to scrape a modal popup "https://seekingalpha.com/symbol/{TICKER}/virtual_analyst_report". I also want to explore actually hitting their REST API with an authenticated bundle versus doing all this scraping bullshit, hence why we have my user info in AWS Secrets Manager."**

NOTHING IS PARAPHRASED ABOVE AND NOTHING IS OMITTED. No other words were given on this subject at this terminal.

---

## 2. WHAT THE WORDS NAME, AND WHERE EACH THING ALREADY SITS -- SURFACED, NOT ADJUDICATED

| his words | what they name | where it already sits in the spec (PRD @c0b5636ea9) |
|---|---|---|
| "fold in to your TOs ... a section ... on Seeking Alpha" | a place in the L6 task orders | L6 is this lane's. Seeking Alpha is ALREADY in the PRD's territory: S4 (the coverage reader; F11 "the SERP path works; the obvious link field is an obfuscated redirect"), S12 (the identity layer; "the Seeking Alpha symbol" is one of the four keys `C-IDENTITY-RESOLVED` names), and the boundary (the seven Seeking Alpha Lambdas' missing Terraform is EXPLICITLY NOT OWNED -- an `AE_CloudOps` estate defect). |
| "pulling info from it and testing SA etl" | an extraction path and a test of it | S4's verb is `build`; `C-STAGE-PERSISTS` and `C-RAW-BEFORE-DERIVED` bind any ETL stage; `FWD-12` (the input ledger) is where "testing" a per-source run is visible. |
| "a good page to scrape a modal popup `https://seekingalpha.com/symbol/{TICKER}/virtual_analyst_report`" | ONE SPECIFIC SOURCE PAGE, keyed by ticker, rendering a modal | NOT NAMED ANYWHERE IN THE PRD OR THE BRIEF. New. A cell can target it; whether the spec should name it is section 3 (a). |
| "explore actually hitting their REST API with an authenticated bundle versus doing all this scraping bullshit" | a SECOND ROUTE to the same source -- authenticated API instead of scraping -- to be EXPLORED and COMPARED | Bears on TWO standing clauses at once: `C-VENDOR-EGRESS` (*"NEVER call an external vendor API without Andrew's explicit per-use word ... A cell may not spend that word and may not assume it"*) and PRD s.5's open precondition *"A decision on paywalled sources ... Nobody has decided, and whether the login is captcha-gated is unknown."* Section 3 (b). |
| "hence why we have my user info in AWS Secrets Manager" | a CREDENTIAL that exists, and its location | A cell that uses it LOCATES it in Secrets Manager by name and reads it at run time; the record never carries the secret and no deliverable prints it. The secret's name is not stated here because it was not stated. |

---

## 3. THE TWO QUESTIONS THIS LANE IS NOT ANSWERING, AND WHOSE THEY ARE

**(a) Is this a SPEC change or an L5/L6 detail?** The PRD is L4 and is `1.0.0_SA_CTO`'s; a substantive edit bumps `prd_version` and re-enters L5 through the notifier. Seeking Alpha is already at S4 and S12, so a cell can carry the modal page and the API-vs-scrape comparison as HOW without a new surface. But "there should be a section somewhere in there" is a placement instruction and PART V's paywalled-sources precondition is named as UNDECIDED in the PRD -- if his words close it, that is a spec edit. **Relayed to `1.0.0_SA_CTO~Z` for that call; this lane cuts against the PRD at its path as it stands at the cut.**

**(b) Is "I also want to explore actually hitting their REST API with an authenticated bundle" the per-use word `C-VENDOR-EGRESS` requires?** The constraint says a cell may not spend or assume that word. His sentence names the vendor, the route (authenticated REST API), and the credential's location, and it is imperative. **This lane does not read it either way.** It is written down exactly as said, and the cell that would call the API carries the question in its own criterion rather than the answer -- the cut names the word this record carries and names that its sufficiency is not this lane's ruling.

---

## 4. WHAT THIS RECORD DOES NOT DO

- It does not edit the PRD, the brief, or any surface row. Those are L4 / L1 and not this lane's.
- It does not name the secret, its ARN, or its shape. He did not, and a record is not the place a credential's handle is minted.
- It does not decide whether scraping is retired in favour of the API. His word is "explore ... versus" -- a comparison, not a replacement -- and the cut carries it as a comparison.
- It does not widen this to the alt-research corpus or the 63-name queue. The macro ruling @1f89e24eac and the project boundary (PRD s.2) are unchanged by this.

**Broadcast:** MCP to `1.0.0_SA_CTO~Z` and `0.0.0_AB_MSTR~Z` in the same turn as this commit. The base `2.0.0_SA_COO` is on the other fabric and reaches this record on the push.
**Push state:** LOCAL at write time; ancestry rather than a tip hash. `0.0.0_AB_MSTR~Z` holds all pushes.
