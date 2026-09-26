# Andrew-direct 2026-09-26 ~02:3xZ at the 2.0.0_SA_COO~M terminal -- established equities stay equities; `other` is personal assets only

## Verbatim

1. "If we have established securities are equities we should keep them as such"
2. "the only context for "other" is personal assets, like somebodys house, their credit card line, and similar held away"

Given while ~M was measuring the class flips of the ONE COT OpenAI run (CALL 2, @37025a10e9;
`IRPT_MVP_M/CLASSIFY_COT_NEW_RESULTS_20260926.json`: 1,012 keys, 1,012 answered, 54 `other`).

## What it binds

- **Rule 1.** A write never moves a security that is already established as `equity` to another class. It narrows
  the COT-new write set and any recut of batch B.
- **Rule 2.** `other` is personal assets held away: the Investor Manual Asset rows (a home, a car, jewelry, a credit
  card line, a mortgage, and the like). A real security is never `other`: a listed stock, a fund, an escrow or
  bankrupt share, a coin.
- **It narrows the rule of 2026-09-25 ~14:4xZ** ("personal and held away is all Other", @705be61575) and batch B,
  which was built under that rule. The CTO's act-2 sign-off (@4fdc4284c9) was signed over a 37-key set that holds
  securities, and it is re-cut before any write.
- The B_01b prompt (CLOUD e20b0990d5) carries the wider wording, so it is amended to rule 2 before B_01b deploys.

Recorded by 2.0.0_SA_COO~M.
