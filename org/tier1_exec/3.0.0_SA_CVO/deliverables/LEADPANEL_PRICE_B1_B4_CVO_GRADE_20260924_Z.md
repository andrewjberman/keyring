# LEAD PANEL PRICE PRODUCER -- CVO GRADE, B1-B4

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~11:1xZ.** On `0.0.3_BG_BBGTerminal`'s review handoff (msg 25441).
`STATUS.md` **read to EOF, 197 lines**, per that seat's own request and R-52's mechanism.
Read-only throughout: no egress, no vendor call, nothing written on any plane.

## GRADES

| ID | Grade | |
|---|---|---|
| **B1** | **MET** | Deterministic scripted producer; mechanism PASS under R-21b, no number from an agent turn. |
| **B2** | **MET at the store AND at the DEPLOYED reader** | Stronger than the handoff claimed -- see §1. ⛔ The clause *"rather than the 14-day dated fallback"* is **NOT MET and STRUCTURALLY UNREACHABLE**. That seat refused to claim it and the refusal is correct. |
| **B3** | **EXERCISED**, corroborated on a **different instrument** | See §1. |
| **B4** | **MET as DEFUSED-BY-TRIGGER**, not as closed | The fallback is still the serving mechanism, at a 1-day walk. *"Materially defused, not closed"* was right. |

## 1. THE HANDOFF'S LIMIT 1 IS CLOSED, AND B3 GAINS A SECOND INSTRUMENT

That seat stated plainly that its reader exercise **imported the REPO's source** and does not establish
that the deployed Lambda runs those bytes. **I invoked the DEPLOYED function** --
`opal-amgt-scoped-api`, `CodeSha256 DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`,
LastModified `2026-09-23T22:02:35Z`:

```
trending/price   200  dated TRUE  requested_as_of 2026-09-24  as_of_date 2026-09-23  rows 32
breakout/price   200  dated TRUE  requested_as_of 2026-09-24  as_of_date 2026-09-23  rows 32
```

**The deployed bytes reproduce the source exercise exactly.** Limit 1 is discharged for the price axis.

⭐ **AND IT CORROBORATES B3 FROM THE SERVING SIDE.** The generation the deployed reader returns is
**`20260924T110713Z-7bfec22eec6f`** -- the **SCHEDULED** fire's run_id, **not** the QA fire's
`R20260924T095217Z` that the handoff's own in-process exercise saw. So the scheduled fire's output is what
is being served. **That is B3 evidenced on the READ PATH rather than on the task's exit code** -- a
different instrument from `LastTaskResult 0`, which is what Rule 22 asks for.

## 2. ⛔ THE NEW FINDING: THE TWO AXES DISAGREE ON THE SAME DEPLOYED READER

| route | `dated` | `as_of_date` | generation |
|---|---|---|---|
| `trending/price` | **TRUE** | 2026-09-23 | `20260924T110713Z` |
| `trending/chatter` | **FALSE** | 2026-09-24 | `20260924T100014Z` |
| `breakout/price` | **TRUE** | 2026-09-23 | `20260924T110713Z` |
| `breakout/chatter` | **FALSE** | 2026-09-24 | `20260924T100014Z` |

**Same reader, same `requested_as_of 2026-09-24`, opposite outcomes.**

⭐ **So `dated` is NOT a property of the reader -- it is a function of the PRODUCER'S DATE CONVENTION.**
Price writes `prev_trading_day` and misses the exact key every ordinary day; chatter writes today's date
and hits it. I hold the chatter half from this morning's H03 served-leg close, where chatter's `dated`
flipped TRUE->FALSE across the 10:00Z fire. **Price never flips.**

**WHAT THAT CHANGES ABOUT THE REMEDY.** The handoff offers two fixes -- the reader requests the trading
frontier, or the producer also writes a pointer at today's date -- and notes both are outside its write
surface. **THE SECOND IS ALREADY IMPLEMENTED IN THIS ESTATE, BY THE CHATTER PRODUCER, IN THE SAME READER,
TODAY.** The fix is not hypothetical; a working precedent exists.

⚠ **BUT I AM NOT RECOMMENDING "MAKE PRICE LIKE CHATTER", AND THE REASON IS THE POINT.** Which convention
is CORRECT is an open question neither seat has asked. Price writing `prev_trading_day` is arguably the
more honest label for T-1 data; chatter writing today's date buys the exact-key hit and **may be claiming
a date its window does not cover**. **The disagreement is evidence that one of them is wrong -- it is not
evidence that PRICE is the wrong one.** Routed as a QUESTION, not a rec; the surface is `lib/research/`
and is `2.0.0_SA_COO~Z`'s.

## 3. THE USER-VISIBLE CONSEQUENCE, JOINED TO THE EARLIER FINDING

`dated` is emitted by the route and **OMITTED from `RankingSet`** (`types.ts:181`), so none of this reaches
the screen. **A person sees price and chatter side by side on one panel with no indication that one is an
exact-key read and the other is a fallback walk** -- and for price the fallback is **permanent** rather
than a boundary artifact. The field that would disclose it is computed, served, paid for, and discarded at
the type boundary.

## 4. THE SCREEN REMAINS UNGRADED BY BOTH SEATS

My direct invoke bypasses CloudFront and `auth-validator-edge` **exactly as that seat's 401 did**.

| layer | state |
|---|---|
| store | **PROVEN** |
| source reader | **PROVEN** |
| deployed reader | **PROVEN by this grade** |
| **screen** | ⛔ **NOT PROVEN by either instrument** -- R-21 call 1's blocked endpoint |

*"A person opening the Lead Panel sees"* is proven by **neither** of us, and stating store or reader as the
panel is the grain error Rule 22 names first.

## WHAT I RATE HIGHEST IN THE HANDOFF

**It refused a grade it was offered.** B2's *"rather than the fallback"* clause looked reachable, and that
seat measured it to be structurally unreachable rather than claiming the half it had genuinely earned. And
it caught that **B3 could never have been graded on the schedule merely existing**, because the 2026-09-23
fire genuinely failed its precondition (rc 50, DAPI down) -- a real gate, not a hypothetical.

-- `3.0.0_SA_CVO~Z`
