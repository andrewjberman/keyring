# ASK FOR ANDREW'S WORD -- BD parity census pull (ADVI_BDPARITY P2-2), two words in one card

**Carried by:** `0.0.0_AB_MSTR`, 2026-08-30 09:10Z, VERBATIM from the issuer `2.0.0_SA_COO` (msg 86894).
**The artifact the word is asked ON:** `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_BDPARITY_P2-1_CENSUS_PLAN_20260830.md`
@ `6a99820c40` -- on origin/CLOUD @ `edb9af0a50` (git ls-remote read 09:07:40Z). Graded PASS by `3.0.0_SA_CVO` (86885);
R3 adopted at the gate by `1.0.0_SA_CTO` (86921). Nothing earlier than `6a99820c40` is cited; an earlier interim
figure ("4.1 h vs 5 min") is DEAD -- pass 2 does not batch.
**Egress class:** external vendor API (Black Diamond performance endpoint). Per CLAUDE.md, NEVER without Andrew's
explicit per-use word; the P1 probe's 2026-08-29 21:23Z word covered ONE pull of five accounts and is SPENT.
**The word comes back VERBATIM** to `2.0.0_SA_COO` (issuer) + `0.4.0_DS_ClientPlatform~C` (executor); this seat relays,
never adjudicates wider or narrower. P2-2 fires on W2 only, after PA-4 reads the applied per-feed selector on the
running artifact (`0.8.0_AE_CloudComp~Y`).

## THE ASK (issuer's text, verbatim)

> "BD PARITY CENSUS -- the full-population account-level parity pull against BD's own performance outputs (the P2 of
> the plan your 'check our work / logic must be EXACT' direction set). POPULATION: 5,309 accounts = our twr_daily
> universe (7,370 at the 2026-08-28 vintage, 100% ten-digit) INTERSECT the xref accounts carrying a bd_account_id
> (5,375); the 2,061 of ours BD cannot be asked about and the 66 BD-pullable with no our-side value are PRINTED as
> outcomes, not dropped. ENDPOINT: performance only (the per-feed selector is applied; costBasis/allocation are not
> pulled; the scheduled daily pull is untouched). PASSES: two per account -- pass 1 QTD/YTD/1Y (batchable if BD
> accepts N accounts per request), pass 2 SI at each account's own inception anchor (one range per call, so up to
> 5,309 calls, unknowable until pass 1). COST at the probe's measured 1.40 s/call: N=1 -> 10,618 calls ~4.1 h;
> N=10 -> 5,840 ~2.3 h; N=50 -> 5,415 ~2.1 h. CARDINALITY (accounts per call) has NEVER been measured -- every call
> to date carried one account. TWO WORDS ASKED: W1 (optional): ONE probe call carrying 2 already-pulled accounts in
> one range, to MEASURE pass-1 cardinality before the census is sized (it says nothing about pass 2). W2: the census
> pull itself, on the sizing above (or re-sized on W1's result if W1 is given first). Nothing is pulled on either
> without your word; each word is spent once."

## In one breath (this seat's summary of the same card, not a substitute for it)

- **W1 (optional):** one BD call, two accounts already pulled, one date range -- measures whether BD accepts more
  than one account per call. Changes the pass-1 count by up to 50x; changes the total by at most ~2x.
- **W2:** the census itself -- 5,309 accounts, performance endpoint only, ~4.1 h serial at one account per call,
  ~2.1 h at fifty. 2,061 + 66 residual accounts are reported, never silently dropped.
- Answer forms the fabric can act on: "W1 go" · "W2 go at N=1" · "W1 then W2 re-sized" · "hold" -- or any other
  words, relayed verbatim.

## Also on the record for the same directive, no word asked

- **R3** (open since 08-29): SmartX feed scope -- the $12.29M / 13 nine-digit keys live on the xref plane, NOT in
  this census population (measured 08-30: twr_daily is 100% ten-digit). R3 is unchanged by P2.
- The five never-produced dates 08-11..08-17 now EXIST (C02-g-7 re-drive, 09:0xZ, 5 of 5, byte-identical rewrites);
  if P2-2 runs after it, the hole manifest shrinks to 08-18 alone.
