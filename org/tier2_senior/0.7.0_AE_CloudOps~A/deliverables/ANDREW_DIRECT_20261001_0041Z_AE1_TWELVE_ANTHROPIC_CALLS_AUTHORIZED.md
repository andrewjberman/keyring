# ANDREW-DIRECT -- 2026-10-01 00:41Z -- `AMGT-ae-1`: the 12 Anthropic calls are authorized

**Channel:** Claude Code terminal, direct to `0.7.0_AE_CloudOps~A`, session `a248016e`.
**Time:** 2026-10-01T00:41:29Z (clock read at the turn).
**Recorded by:** `0.7.0_AE_CloudOps~A`, same turn as the instruction, per `org/XXX.md`.

## The instruction, VERBATIM

```
go
```

That is the whole of it. One word, no qualifier.

## What it answers, and therefore its SCOPE

It is the direct reply to the question this seat put to Andrew in the immediately preceding turn, which
named one decision and nothing else:

> "**What I need from you:** whether you authorize the 12 Anthropic calls for this batch. If yes, the
> issuer sends the GO naming your word and the pin, and I run it."

So the scope of the word is exactly: **the 12 Anthropic model calls of `AMGT_RESAPP.TO-AMGT-ae-1`, one per
target, the posture judge's own call.** That is the per-use word CLAUDE.md's vendor-egress rule requires
("NEVER call an external vendor API without Andrew's explicit per-use word -- availability is not
authorization") and that `AMGT-ae-1`'s own preflight requires ("EGRESS CLASS, declared: VENDOR -- Anthropic,
12 messages ... ON ANDREW'S PER-USE WORD ONLY: the GO names it").

⛔ **IT IS NOT WIDER.** This seat does not adjudicate scope (`org/XXX.md`: "the receiving agent does NOT
adjudicate scope. Surface, do not adjudicate"), and CLAUDE.md section 2 forbids relaying wider OR narrower.
Specifically, this word does NOT authorize:
- any vendor call beyond the 12 named targets (a 13th target is a REFUSAL under BOUNDS 1);
- `management_posture_batch.py posture --force`, which the order bans outright because it has no key filter
  and would call Anthropic for all 35 subjects;
- any Lusha or Bright Data call (the management stage, excluded by BOUNDS 1);
- any vendor egress on any other order, round or project.

## What it does NOT by itself satisfy

`AMGT-ae-1` section 1 gates the act on the ISSUER'S GO, not on the word alone:

> "**Begin only when all hold:** the issuer's GO names Andrew's per-use word for the 12 calls and the commit
> to run from, and both halves are committed (their paths are in the GO)."

The word has arrived by a more direct channel than the one the order anticipated, so this seat RELAYS it to
`2.0.0_SA_COO~Z` (the issuer, which had asked Andrew at ~23:2xZ and is holding the GO on the answer) rather
than treating the word as the GO. Relay, never adjudicate. The act begins when the GO lands.

## State of the other preconditions at this write

- Both halves committed: `deliverables/2.0.0_SA_COO~Z/round55/NEVER_WIDEN_HALF_COO_AE1.md` and
  `ledger/NEVER_WIDEN_ROUND55_AE1_CTO_HALF.md`.
- `deliverables/2.0.0_SA_COO~Z/round55/checks/ae_1_posture.py` present.
- The pin the issuer named for the GO, `51df60aa1a`, RESOLVES in this repo
  (`51df60aa1a4c0c7bd37dc49998246919db99ef83`).
- Issuer confirmation that holding was correct: msg 27456, READ-acked by this seat.

Relayed to `2.0.0_SA_COO~Z` the same turn.
