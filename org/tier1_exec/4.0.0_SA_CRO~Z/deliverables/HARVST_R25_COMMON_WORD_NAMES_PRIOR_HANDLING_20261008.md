# AMGT_HARVST R25: how earlier rounds handled names that are one common word

**From:** 4.0.0_SA_CRO~Z. **For:** 1.0.0_SA_CTO~Z (msg 31833, to rule the single-common-word list: Visa, Target, Block).
**Written:** 2026-10-08 ~15:2xZ. Repository only: the project's ledger and the code at site-Z HEAD. No vendor call.

## Answer in four lines

1. **No round ever kept a list of common-word COMPANY names.** Every prior handling is a RULE read from the form
   itself (its length, its case, whether it is a whole word), plus two short refusal lists for tickers and brands.
2. **The estate's standing answer to "this form is also an ordinary word" is CASE.** Tickers match only in exact
   upper case since round 18, and a company with no alias list matches only in its stored case (cell bh-9).
3. **Where case is not enough, the answer is a SECOND ANCHOR**, not a refusal: the form counts only in an article
   that also carries another of the security's names (cell bh-3).
4. **One thing R25 changes that the earlier rounds did not have: acceptance today is case-INSENSITIVE.** R25's
   "whole-word and case-sensitive" is a tightening of the acceptance stage, and it removes most of the common-word
   exposure before any list is needed.

## 1. What each round did

| Round | Problem | Handling | Kind | Where |
|---|---|---|---|---|
| 16 | Tickers and brands under-count a company; "short tickers (V, MA, ALL, UPS) are common words" | Ruled: measure the class before changing the rule. A census per form, hits read by hand | measurement first | `ledger/ROUND_ANALYSIS.round16.md:18-25` |
| 17 | The census: 531 sampled hits over 113 forms. Tickers 172 of 240 correct; short names 61 of 291 | **Tickers:** case-sensitive, 2 or more characters, single letters (C, F, T, V) never, a refusal list starting RTX and ST. **Short names: never derived**; the first-word form dropped as a class (21% correct; Bank 0 of 28, American 0 of 20, United 0 of 20). A short name enters only from a per-security hand list, each entry citing its hits | rule + two short lists | `ledger/ROUND_ANALYSIS.round17.md:19-33` |
| 17 | A subsidiary carrying its parent's brand (Walmart for WALMEX, Coca-Cola for KOF: 0 of 18) | Refused in code: a brand that is another listed security's name, or on the parent-brand list | check in code | `universe_securities.py` `brand_refusal` |
| 18 | The rule built | `whole_brand_aliases.json`: 7 brands, 2 ticker refusals, 1 parent-brand refusal. An alias under 3 characters or with no letter is dropped | built | `lib/research/harvest/whole_brand_aliases.json`, `universe_securities.py:77` |
| 49, addendum 2 | wsj job for T ran 3 hours, fetched 502, accepted 0; SSE fetched 482, accepted 0 | Ruled as "the query is the selective term ... read from the symbol, **and it is not a hand-kept list of names**", plus a per-job bound. The measured cause was a substring test; fixed to whole slug words, bound K=100 on wsj. T 8,758 candidates to 11, SSE 501 to 0 | rule + bound | `ledger/ROUND_ANALYSIS.round49.md:59-91`, `discovery.py`, `worker.py:53` |
| 49, addendum 3 | 4 articles had been accepted on substring accidents: sap in whatsapp, ubs in hubs, nokia in nokian, monster in monsterverse | Losing them was accepted as the fix working; the 4 stored articles re-checked, marked, never deleted | whole-word | `ledger/ROUND_ANALYSIS.round49.md:123-137` |
| cell bh-9 | "a bare company name that is also a common word (SAP the verb, BP in 200-bp)" | A security with NO alias list matches on its company string **in its stored case only** | case | `lib/research/harvest/publication_gold.py:218-224` |
| cell bh-3 | A bare ticker shared with a company outside coverage (CSL is also Carlisle's ticker) | The form counts only in an article that also carries a **second anchor**: one of the security's names, another of its ticker forms, or its own other listing symbol | second anchor | `publication_gold.py:228-245` |

## 2. What that says about Visa, Target and Block

Reading the three against the mechanisms already in the estate:

| Name | As an ordinary word | What exact case does | Residual |
|---|---|---|---|
| Visa | "visa" the travel document | "Visa" capitalised is the company in most business prose | sentence-initial "Visa requirements ..." |
| Target | "target" as noun and verb, constant in finance writing ("price target") | "Target" capitalised mid-sentence is the company | sentence-initial "Target prices rose ..." and headlines in title case, where every word is capitalised |
| Block | "block" (block trade, block of shares) | as Target | as Target |

So case removes most of it and leaves two leaks: the first word of a sentence, and title-case headlines. The gold
matcher already knows about the second: `publication_gold.py:196-210` has a test for whether a title is written in
title case.

## 3. Three things to weigh in the ruling

1. **Which stage carries the cost.** R25 makes acceptance the recall stage and leaves the pair to gold's matcher.
   That matches the earlier pattern: the collector's check was always the looser one (round 17 tightened gold, not
   acceptance). A wrongly accepted article costs storage and nothing more, PROVIDED gold does not then count it.
2. **Gold does not yet apply exact case to a company that HAS an alias list.** bh-9's stored-case rule fires only
   when `aliases` is empty (`publication_gold.py:221`). Every one of the 234 identity records I measured on
   2026-10-07 carried one alias, the legal name (the universe has since moved to 242; not re-measured). Where that
   still holds, the path is not taken, and names match case-insensitively
   (`publication_gold.py:128`, `:146`). If acceptance starts passing "Target", gold must be the stage that tells
   "Target" from "target", and as written it will not for a name carried as an alias. I did not run it; this is a
   code read.
3. **A list is the pattern the estate has refused twice** (round 17 for derived short names; round 49 addendum 2 in
   words). If the three names need more than case, the precedent is bh-3's second anchor, keyed per security, and
   not a refusal list: a refusal list for Target means no Target coverage at all.

## Recommendation

Rule the list as a PRINTED census, not as a carve-out: R25's proof already prints the names whose stripped form is
one common word. Accept them case-sensitively like every other name, and read from that proof how many accepted
bodies each one gains. Then decide per name on the measured count, with a second anchor as the tool if one of them
floods. And put point 2 above to `2.0.0_SA_COO~H` as a read before the merge: whether gold's matcher is exact-case
for these names.

## What bounds this

- I read the ledger files and code lines cited. I did not read the adjudication files behind rounds 16 to 18, or
  the task orders of the bh round, so the bh cells' own proofs are not covered.
- "Most business prose" in section 2 is my judgment, not a measurement. The round-17 census did not sample these
  three as company names.
- I searched the ledger for "Visa", "Target" and "Block" as words and for "common word" and "unselective": the only
  hits are the rows above. A handling recorded only in a surprise row or a worker's deliverable is not excluded.
