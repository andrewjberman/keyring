# L4-R BRIEF-HALF RE-REVIEW -- DSGN_REBRND PRD v0.9 @928a3df671 (half hash 3ce6d986a988)

**Reviewer:** `2.0.0_SA_COO~D`, the designated brief-half signer (on the project row, by Andrew's word @`2daf4d8b85`).
**Supersedes:** `laneD_L4R_BRIEF_HALF_REVIEW_DSGN_REBRND_v0.7.md`@`e3e8974ccc`, SIGNED @`f1391bb4cf` against
`2ee54bf076c6`.
**Delivered by:** `1.0.0_SA_CTO`, msgs 96708 (v0.8) and 96710 (v0.9).
- The v0.8 request is answered by this v0.9 review. v0.8 was bumped before it could be bound: at 19:26Z the working
  copy already read v0.9.
- HEAD and the working copy both hash the brief half at `3ce6d986a988` (`prd_signoff_lib.half_hashes`), so the
  bytes reviewed are the bytes bound.

**Scope:** the delta from the v0.7 bytes this seat signed. A word-level diff of v0.7 `c27a779ee7` against v0.9
`928a3df671`, through v0.8 `5dd24300f7`.
- Brief-half lines moved: R5 (`:127`), R9 (`:131`), and PROVENANCE v0.8 and v0.9 (`:263-270`).
- Every other moved line is in ENDPOINT or CONTRACTS, which is `3.0.0_SA_CVO`'s half.

## VERDICT: SIGN

## 1 -- R5 carries RULING A, and nothing else

R5's acceptance changes in three places:
- "exactly" becomes "at most";
- it gains "(none on a route with no primary action)";
- "stays one" becomes "does not rise".

That is RULING A of the round-1 analysis (row W1-S20; PROVENANCE v0.9): a view with no primary action spends the
accent on none. It matches FWD-4's v0.9 ENDPOINT text and the `DesignContract` clause.

It also matches what the round measured. `/market` and `/positioning` have no primary action, and `/portfolio-management`'s
one is in a band (the RB-s-15 pack note). So "at most one" is the reading the product can satisfy, and it is not
weaker than Andrew's budget. His identity set (the five sites and the rail edge) is untouched.

## 2 -- R9 carries RULING V, and nothing else

- R9 now keeps "the 1 visx file (TopicCloud's word cloud)" as FWD-8's named exception, with its reason in the
  contract. It no longer counts that file toward migration.
- That is RULING V (row W2-S1). It matches FWD-8's own CONSTRAINT: it cannot be migrated without changing what it shows.

It is also consistent with this seat's `/market` pass 1 @0aefb3c5, which restored the cloud's yellow family inside
the visx component on Andrew's word, rather than migrating it.

## 3 -- The PROVENANCE entries are accurate

- **v0.8** records `3.0.0_SA_CVO`'s R3 (the band rung's rule, the opaque ladder) and N1/N2 by the review path. Each
  sub-claim resolves in the ratified-text diff at `:105`, `:107`, `:112` and `:143`.
- **v0.9** records RULINGS A and V with their rows, and names G, W and C-S11 as changing no text, pointing at the
  analysis.

## 4 -- One note, NON-BLOCKING, and not in this half

FWD-12's CONSTRAINT (`:107`, ENDPOINT) still reads that the one tooltip role "does not decide Andrew's three tooltip
types -- if his clarification gives them different grounds, the role table grows by his word". Andrew has since given
that clarification, at ~19:0xZ (record @7c7fbe30f3, relayed as 96711):

> "They should all have the smae look as we have in the helper tip, solid indigo no outlines"

That is ONE look. The clause's own condition is now answered, so the next bump can close it. It is `1.0.0_SA_CTO`'s
text, in `3.0.0_SA_CVO`'s half, and it does not bear on signing this one.

## NOT CLAIMED

- **The ratified-text half.** It is STALE at v0.9, and owed by `3.0.0_SA_CVO`.
- **The round-1 analysis's other rulings** (G, W, C-S11). They change no text in this half.
