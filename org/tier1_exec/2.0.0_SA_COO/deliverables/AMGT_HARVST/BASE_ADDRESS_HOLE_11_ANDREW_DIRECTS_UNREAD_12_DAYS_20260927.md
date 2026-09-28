# 191 base-addressed messages unread at `2.0.0_SA_COO`, including 11 Andrew-direct relays about THIS pipeline

**Found 2026-09-27 ~23:5xZ by `2.0.0_SA_COO~Y`**, prompted by `0.0.0_AB_MSTR~Z`'s 234904Z ask ("address me as
`~Z`, not the bare base serial"). **Its finding reproduces at my seat, larger.** I checked my own base slice
because its message named the mechanism: *"a watcher watches exactly one slice."*

## THE HOLE, MEASURED

| slice | `.md` files in top-level | watched by |
|---|---|---|
| `org/mcp/inbox/2.0.0_SA_COO/~Y/` (my lane) | **0** | my stream watcher, re-armed 156 times tonight |
| `org/mcp/inbox/2.0.0_SA_COO/` (the BASE) | **191** | **NOTHING** |

Oldest in the base slice: 2026-09-15. **Eleven are `4.0.0_SA_CRO~W` relays of Andrew-direct instructions about
the opal-data-harvest pipeline -- the exact project this lane has worked all night -- and they are 12 days
unread.**

## 11 FILES ARE NOT 11 DIRECTIVES -- measure before reporting the number

**11 files, 11 DISTINCT bodies, but only 12 DISTINCT verbatim Andrew quotes.** Each file re-quotes its
predecessors and adds one or two, so this is **ONE Andrew-direct session (2026-09-14 US Eastern) relayed as
eleven accreting files.** Reporting "11 unread directives" would have inflated one conversation into eleven, the
same shape as calling N failures N causes. The count that matters is **12 distinct instructions**.

## WHAT THE 12 QUOTES SAY, and which bear on LIVE work

Load-bearing for what this lane did tonight or plans for round 8:

1. **THE BLOOMBERG PRESS-AND-HOLD TECHNIQUE, described by Andrew himself:** *"This case youre on right now with
   bloomberg is the case where the press and hold starts draining and you have to wait and un-press for a
   moment, and then press again after its gone down somewhat."*
2. **A LOOP STRATEGY OVER STRATEGIES:** *"we need to create a loop strategy where you just keep looping
   strategies until you can reliably get 5 articles worth of results from a given ticker"*.
3. **TOKEN THEN REST, NOT SCRAPING:** *"the whole purpose of the harvester scripts is to actually get the token,
   and then you just use the rest api to pull the data no scraping"*.
4. **CRAWL ONLY FOR SHAPE:** *"crawling is a suboptimal wayto do this, you should only be crawling if you want to
   get the api endpoint shape"*.
5. **JSON FIRST:** *"Try to get proper JSON. If there really is no clean JSON field available, then we can allow
   HTTP extraction, but it is a last resort."*
6. **WSJ AND BARRON'S CREDENTIALS EXIST:** *"I just set up a credential for WSJ and Barron's. Let's get scraper
   method set up for them in same fashion as we have done for the other harvesters."*
7. **A CANONICAL TOKEN LIB:** *"make sure there is a lib or something in canonicl form inside opal-data-harvest
   that has the various tokens for each of these platforms"*.
8. **AN ACCEPTANCE BAR this lane has NOT been tracking**, carried in the relay's own prose: five distinct
   complete articles per publisher, for three consecutive different tickers, publisher order SA, FT, WSJ,
   Bloomberg each round.

## WHY I AM RECORDING THIS RATHER THAN ACTING ON IT

⛔ **THREE REASONS NOT TO TREAT THESE AS LIVE LAW, and each one is a reason to ASK rather than infer:**

- **PROVENANCE IS WEAK ON ITS FACE.** Every one of the eleven carries *"Sender-unverified: the sending session
  was not registered; this from-line is asserted, not proven."* That is the relay's own warning about itself.
- **THEY ARE 12 DAYS OLD AND LATER RULINGS EXIST.** Quote 2's "keep looping strategies" reads as broad standing
  authorization for repeated vendor attempts. **Tonight I told Andrew the opposite about bbg -- no further
  requests from this seat without a fresh word -- and I am not going to reverse my own bound on a 12-day-old
  unverified relay.** Quote 6 (WSJ/Barron's credentials) also sits against a LATER line in the same relay set
  saying WSJ needs no subscriber login because it uses Bright Data Web Unlocker: **the set contradicts itself
  internally**, which is what a relay accreting over an evening looks like.
- **A RELAY OF ANDREW'S WORD MUST NOT BE WIDENED BY THE READER.** These were addressed to `2.0.0_SA_COO` as a
  base, not to this lane or this round, and reading them as authorization for acts in round 8 would be
  adjudicating scope I was not given.

**WHAT IS UNAMBIGUOUSLY USEFUL AND CARRIES NO AUTHORIZATION QUESTION:** quote 1 is a TECHNIQUE, not a
permission, and it matters because **the producer already implements it** -- the solver logs *"adaptive
press-and-hold at (680,244) -- drain -> release -> partial fall -> re-press"*, which is Andrew's description
almost word for word. It then fails with *"no checkmark or peak detected within 12s ... recoveries=0"*.
**`recoveries=0` means the drain never partially fell, so the technique's own precondition was never met** --
which is a sharper statement of the bbg blocker than "the solver cannot pass it", and it is the thing a fix
would target. Filed against row `AMGT_HARVST-Z-S32`.

## THE KEEPABLE FORM

**A LANE-SCOPED WATCHER MAKES BASE-ADDRESSED MAIL INVISIBLE, AND INVISIBLE IS NOT EMPTY.** I re-armed my watcher
156 times tonight and reported reachability as healthy every time. That was true of ONE slice. **The instrument
I trusted could not see the slice where 191 messages were waiting, and nothing in its output said so** -- a
reader that cannot see reports absence. **COST: one `ls` of the base slice per session.** NON-APPLICATION: a
seat with no lane suffix, where the base slice IS the watched slice.

Corollary, and it is why this was found by accident: **`0.0.0_AB_MSTR~Z` found its own hole because a PUSH GATE
counted pending mail.** My seat has no such gate, so nothing would ever have told me. A hole found only by a
neighbouring seat's unrelated instrument is a hole with no local detector.
