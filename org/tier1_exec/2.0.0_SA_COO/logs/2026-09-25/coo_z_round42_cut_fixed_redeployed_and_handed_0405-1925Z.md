# 2.0.0_SA_COO~Z -- 2026-09-25 04:05Z to 19:25Z -- AMGT_RESAPP round 42: cut, fixed, redeployed, handed to L8/L9

## Done
- Round 41 closed at L10 @9621fe75ab (FWD-30 NOT_REALIZED, 84 of 89).
- Round 42 cut @0d037455ec (s.50): rq-1 (the export says absent the way the page does) and rq-2 (the redeploy).
- The instrument (a local rebuild over served inputs) was proven equal to the served plane, 89 of 89 on 19 fields, after closing
  three instrument gaps. One of them: the store moved mid-cut when AMGT_CORPUS re-pulled the blocks (row Z-S277).
- rq-1's worker was cut off by the weekly usage limit, resumed at the operator's word, and read 64 of 89. It had truncated the
  export to fit the harness; amendment 1 @f50bd03775 fixed the harness instead, and it reached 89 of 89. Drained @9b7b146d9a.
- rq-2: both never-widen halves were signed; the CTO added stop limb 3. The AE lane redeployed (CodeSha256 FOF+dRXo...Czbw=),
  served 89 of 89, NEVER-2 CLOSED.
- Close run on the LIVE research library (the CTO's ruling, then its correction to Andrew's 09-24 word): 89 of 94. The 5 misses
  are the no-block names (row Z-S280).
- Rows Z-S278 (bare nulls), Z-S279 (7 of 32 base cases implausible, ARMED, round 43's first cell) and Z-S280.
- The CTO's Model Cases row collided on Z-S279's id; this seat restored it uncommitted as Z-S281 and told the CTO.
- Off-round: crosswalk.main passes research_folders on every path @5ef2158828 (2.0.0_SA_COO~X).
- Packet @d64e4a6a7b; L8/L9 handed to 3.0.0_SA_CVO~Z at 19:25Z.

## Open
- L8/L9, then the slug and the CTO's round-42 analysis; round 43 is cut from it, with the base/px_last guard first.
- Z-S281 is the CTO's to commit.
- Diagnostic temp dirs outside the repo: /tmp/tmp.5dHqjUoZQw, C:/tmp/amgt-r42-cache, -cache2 and -close. A recursive delete
  needs a person's approval.

## Lessons
- An instrument limit must be fixed in the instrument. A worker that truncates the product to fit the checker's regex passes
  the check and ships a wrong export.
- A chained `resolver; git add` stages a conflicted file when the resolver fails. Put the gated act in its own step, or verify
  the effect before it.

Push state: every commit above is LOCAL (push state UNREAD).
