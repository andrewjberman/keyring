# ANDREW-DIRECT 2026-10-08 ~15:5xZ, at the `2.0.0_SA_COO~D` terminal (site Z) -- "recs approved"

**Recorded by:** `2.0.0_SA_COO~D`, 2026-10-08 ~16:0xZ. **His words, verbatim, whole:** "recs approved"

**What he was answering:** this seat's `/open-calls` output of 2026-10-08 15:54Z, two cards, printed to him in the turn before.
Both cards are copied below as printed, so the scope of the word is on the record and is not widened or narrowed here.

```
OPEN CALLS AT ANDREW -- 2.0.0_SA_COO~D (2 calls, 2026-10-08 15:54Z)

BLOCKING (something waits on the word)

+-- CALL 1 of 2 ------------------------------------------------------+
  **Push DSGN_AMGTV1 portal candidate dbeb6764 to DEV? (yes / no)**
  CTO-approved (msg 31750). Carries rounds 51-52: one statement of
  inputs, the coverage sentence, officers as served, the pack wording.
  ---------------------------------------------------------------------
  **REC --** Yes. Both round checks, the standing battery and the walks
  on the live function pass, and it touches only Security Analysis
  page files. The integrator pushes; I read DEV after CI is green.
+----------------------------------------------------------------------+

CARRIED (nothing blocked; answer whenever)

+-- CALL 2 of 2 ------------------------------------------------------+
  **Promote portal DEV to PROD? (yes / after call 1 / not yet)**
  PROD is b06863fe; DEV d1b21c97 is 39 commits ahead and carries other
  projects' work as well as this page's rounds 47-50.
  ---------------------------------------------------------------------
  **REC --** After call 1: one promote once dbeb6764 is on DEV and read
  there, so PROD gets rounds 47-52 together. I have not read all 39
  commits; the other projects' owners should confirm theirs first.
+----------------------------------------------------------------------+
```

## What the word covers, read from the two RECs and nothing wider

1. **CALL 1 -- YES.** Portal candidate `dbeb6764` (full sha `dbeb6764eaa688230f44cfcc1763bd73db6e1142`, branch
   `wk-DSGN_AMGTV1-113-portal`, a fast-forward of DEV `d1b21c97`) is pushed to portal DEV. The REC names the actor: the
   integrator pushes; this seat reads DEV after the CI run on the pushed sha is green.
2. **CALL 2 -- AFTER CALL 1.** ONE promote of portal DEV to PROD, once `dbeb6764` is on DEV and read there. The REC carries a
   condition that is part of what was approved: the other projects' owners confirm their own commits in the DEV-to-PROD range
   first. This seat had not read all 39 commits at the time of the card.

## What it does not cover

- AMGT_CORPUS's portal candidate `0498827c975a` (named on the card only as NOT-MINE). Its push word is not given here.
- Any act outside the two cards.

## ADDENDUM -- Andrew-direct 2026-10-08 ~19:4xZ, same terminal

**His words, verbatim, whole:** "Yes your rec is correct, it was not an intentional interrupt, merely was breaking the hang.
Furthermore, I am looking at PROD security analysis right now, what am I lookin for here?"

**What he was answering:** this seat's /open-calls card of ~19:3xZ, one call: how the two post-deploy reads of PROD `f73f9ab0`
are done, (a) this seat does them / (b) his own walk closes them / (c) other. Its REC was (a). Both of his tool-use refusals
that afternoon were, by his words here, not refusals of the act. **(a) was done:** walker read on PROD 19:59-20:04Z, 8 of 8;
NEVER-2 `portal-prod-promote-dsgn-r52-20261008` CLOSED @51e9676468. His own walk on PROD (FWD-1) was in progress at his words.

## Acts that follow, and who holds each

| act | holder |
|---|---|
| the DEV push of `dbeb6764` | `0.0.0_AB_MSTR~Z` (asked by this seat's relay of this record) |
| the post-push read of DEV, after CI is green | `2.0.0_SA_COO~D` |
| confirmation of the other projects' commits in the PROD range | each project's owner; asked through `1.0.0_SA_CTO~Z` |
| the PROD promote, after the three rows above | per the NEVER-2 pattern of this seat's last promote (@f14a8198f7, @13a406a1d4), ledger entry opened first |
