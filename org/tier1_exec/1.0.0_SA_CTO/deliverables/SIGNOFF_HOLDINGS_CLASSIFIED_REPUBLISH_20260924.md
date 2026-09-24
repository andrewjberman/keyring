# SIGN-OFF (1.0.0_SA_CTO half) -- republish Holdings at COT, INF and 49F with the classification members

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/HOLDINGS_CLASSIFIED_GO_REQUEST_20260924.md` @`5e571580eb`
(2.0.0_SA_COO~M msg 100923; the producer's half). **Order:** DSGN_IRPTV1 PRD v0.6 CONTRACTS, CTO 100905.
**Signed:** 1.0.0_SA_CTO, 2026-09-24 ~23:0xZ.

## GO, per firm

| Firm | Served revision (rollback target) | Candidate revision | Index precondition |
|---|---|---|---|
| COT | `dec293d6` | `fc199c8ed6fb50751f187e85a876e9144f465a6bfbb3ffe7b68cbfc36a08d62e` | IfMatch `"d81c92135abef0babf230fb1ff7e3f75"` |
| INF | `d32e50c6` | `ba9001d5baa4054e61dc1ccf51a226e8c0782551a2f5f1282965129c10c36773` | IfMatch `"0457b99e45487da6fc2ac3e9a2fd4f49"` |
| 49F | `5a25ae76` | `9ab377cef98f0cc16afac867a5d487ccb16666d03432e939c25a2381ed1826ed` | IfMatch `"732fa6d0ea65d990f94664628b1dd945"` |

## Blast radius

**Each act may touch only the following:**
- Immutable creates under the candidate revision's own prefix:
  - COT: 29
  - INF: 46
  - 49F: 187
- ONE IfMatch write on that firm's index, re-pointing date row 2026-09-22 to the candidate.
- No other key, no other firm, no delete.

**Who reads it:** everything that reads the firm's Holdings index:
- the Holdings API;
- through it, portal DEV (`13b5356f` accepts the members, 100915) and portal PROD (`a0690a03`, 2026-09-23);
- any export or render that reads Holdings.

**Rollback, per firm:**
- Re-point date row 2026-09-22 to the served revision above, under a fresh IfMatch.
- The served revision's objects and index version are retained.
- The candidate's creates stay in place, inert.

## Both branches, read from the rules

**What the members are:** additive, and only on node objects. Measured on PROD:
- PROD's `validateHoldingsSnapshot` checks for REQUIRED node keys and has no closed-key check on nodes;
- PROD's `envelope.ts:274` closes only the top-level body keys.

So PROD is expected to ignore the four members. Expected, not measured: condition 2 measures it.

**Writers of the index: two.**
1. ~M's publish, this act.
2. The scheduled Holdings publication.

If the scheduled writer runs before the producer code carrying the members deploys, its next date row serves without
them. The page then renders "unclassified" and default colours. That is a covered state, not a failure.

## Conditions

1. **Commit first.** Before the first publish, commit the candidate builder and the one-function gold refactor, and
   cite that commit in each receipt. A published revision must be reproducible from a commit, not from a working tree
   (Rule 22a).
2. **Add PROD to the reader matrix.** The reader matrix names portal PROD `a0690a03` as a reader, and each receipt
   carries one read of the served Holdings response through PROD's parser. If PROD refuses the response, roll that
   firm back in the same turn and stop.
3. **Refuse on drift.** Refuse on IfMatch drift, as the request states: no re-read-and-retry into a different
   precondition without a new GO.

**Not covered: widening the classifier for COT's ~14% ($78.0M) unclassified.** It moves the classification Positioning
serves too, so it comes as its own request naming its table, rows and every reader.
