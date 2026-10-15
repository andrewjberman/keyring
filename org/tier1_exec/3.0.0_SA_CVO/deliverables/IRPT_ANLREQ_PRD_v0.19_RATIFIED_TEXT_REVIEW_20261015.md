# IRPT_ANLREQ PRD v0.19 -- L4-R review, ratified-text half (the unmatched-ticker decision tree)

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-15 ~21:5xZ. **Delivery:** msg 8705. **PRD:**
`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @70a3edb0eb. **Compared against:** v0.18 @c0993a9bbe, which this seat signed.
**Authority:** `ANDREW_DIRECT_20261015_215xZ_TICKER_DECISION_TREE_YES_REPLACE_NO.md` @78ed0c8908, recorded by this seat. Andrew said it at this
seat's terminal.

**Verdict: SIGN.** Only the C-FILING-HINT row moved in this half. The ENDPOINT is unchanged.

| his words | the row |
|---|---|
| "If there is a ticker that doesn't connect, we check it." | every holding the door cannot match is CHECKED by the door |
| "If the ticker doesn't exist outright, we assume it may be a typo and the agent can do a 'did you mean?' prompt" | (A) `TICKER_NOT_FOUND`: 'Did you mean <symbol> (<name>)?' from the door's provider-verified `suggestion` |
| "If yes, we accept the swap" | Yes: the upload is re-posted with that correction |
| "if replace we try it with the replaced ticker(s) and rerun the process for those" | Replace: an input for the filer's ticker(s), re-posted and CHECKED AGAIN by the same tree |
| "if no, then we say that Opal Staff will manage the replacement" | No: files UNRESOLVED with 'Opal Staff will manage the replacement.' |
| "text ... says replace the missing ticker with a proxy, but there is no input to do so" (the contradiction) | `NAME_PROXY` retired; "no text tells the filer to replace without an input to do it" |

The row agrees with C-SWAP: every UNRESOLVED holding goes to the backend pass, and the report names the replacement. It also agrees with
C-PRICES and FWD-2. The form makes no vendor call.

**Two readings where his word is silent, for Andrew to confirm with one word (not reasons to refuse):**
1. **(B), a ticker that EXISTS but cannot be priced** (`TICKER_DATA_NOT_ENTITLED`, the PROD row-100 case). It gets no prompt and goes
   straight to No. His tree speaks only to a ticker that "doesn't exist outright". The CTO's reason is that choosing a stand-in for a real
   security would be a filer swap. The alternative would be to offer Replace here too. One word from Andrew settles it.
2. **With no suggestion, the prompt offers Replace and No only.** That is consistent with his tree, since Yes needs something to accept.

-- 3.0.0_SA_CVO~DELL2
