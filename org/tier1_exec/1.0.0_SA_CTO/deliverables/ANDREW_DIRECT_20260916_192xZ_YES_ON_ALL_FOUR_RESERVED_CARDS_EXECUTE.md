# ANDREW-DIRECT 2026-09-16 ~19:2xZ (3:2x PM Eastern) -- "Yes on all four, execute them." -- the four reserved AMGT_RESAPP cards

- **Channel:** Andrew, direct, at the `1.0.0_SA_CTO~Z` terminal. **Recorded by:** `1.0.0_SA_CTO~Z`, same turn.
- **Scope:** surfaced VERBATIM and routed to each act's owner; not adjudicated wider or narrower. The four cards are quoted
  below exactly as this seat presented them, because his "yes" binds to that text.

## 1. HIS WORDS, VERBATIM AND ENTIRE

First message:

> Give me the reserved calls

Second message, after this seat presented the four cards in section 2:

> Yes on all four, execute them.

Nothing is elided.

## 2. THE FOUR CARDS AS PRESENTED (the text his "yes" answers)

**CARD 1 -- Run the two Bloomberg producers.** Decision: authorize the budgeted Bloomberg sign-in to pull model blocks for the
keyed coverage names, and run the price-axis pull once so the Price list has a today-dated generation. Recommendation: YES on
the pull for the 33 keyed coverage names, run once now, no cadence armed. The price pull rides the same sign-in. Cadence stays a
separate word.

**CARD 2 -- The filings and drafting batch.** Decision: approve the filings analyzer and drafting run over the keyed names, at
roughly one dollar per filing. Rider: regenerating BA's filings document under the new producer is also a vendor call as the
producer stands, so a one-name pilot re-run sits under this card too. Recommendation: YES for the 33 keyed names (about USD
36), not the full 89.

**CARD 3 -- Push the portal DEV branch.** Decision: fast-forward portal DEV to the branch carrying the Security Analysis page,
and push it. A DEV push runs CI and deploys nothing; "no portal promote necessary" is untouched. Recommendation: YES, now.
`0.0.0_AB_MSTR~Z` executes it on his word.

**The SITEZ push and the CLOUD-to-SITEZ merge leg.** Decision: push local SITEZ and run the cross-fabric merge leg (LD-0522, held
by `0.0.0_AB_MSTR~Z`). Recommendation: YES on the push; the merge leg after it.

## 3. WHAT HIS WORD AUTHORIZES, AND WHAT IT DOES NOT

| authorized by this word | still reserved (not in the cards, so not answered) |
|---|---|
| ONE run of the model-block pull over the 33 keyed coverage names, through the budgeted two-phase sign-in (`integrations/bloomberg/READ_HERE.md`) | any recurring cadence for either Bloomberg pull |
| ONE run of the price-axis pull, same sign-in | any pull over the 89 (the card said 33, not 89) |
| the filings analyzer + drafting batch over the 33 keyed names (~USD 36) and the one-name BA pilot re-run | the harvest COLLECTION mechanism and cadence (@`9db2a36cdc`), unchanged |
| the portal DEV fast-forward to `wk-amgt_resapp-12-23-portal` and its push, by `0.0.0_AB_MSTR~Z` | any PROD promote; the portal freeze stands |
| the SITEZ push and the `CLOUD -> SITEZ` merge leg, by `0.0.0_AB_MSTR~Z` | nothing wider on LD-0522 than these two acts |

## 4. ROUTING -- who executes what, and how it enters the canonical flow

- **CARD 3 and the SITEZ push + merge leg -> `0.0.0_AB_MSTR~Z`**, the LD-0367/0368 and LD-0522 holder, who already has both
  carded at its terminal with the measurements attached. It executes, measures before and after, and reports push state from
  `ls-remote`. Order: SITEZ push, then the merge leg, and the portal DEV fast-forward + push; the superproject's `portal`
  gitlink update follows the portal push under that seat's own mechanics.
- **CARDS 1 and 2 -> `2.0.0_SA_COO~Z`**, the round-12 issuer. Both are PRODUCER RUNS the decomposition never carried because
  their gate was reserved; his word lifts the gate, and they enter as ONE issuer amendment cutting the orders (or as round 13's
  first cells if the issuer judges round 12 too close to its drain-end -- the issuer's call, stated in the amendment). Bounds the
  orders carry: the two-phase budgeted sign-in and the READ_HERE surface for Bloomberg; the 33 keyed names as the population,
  printed; ONE run each, no schedule armed, no cadence; the price pull once; the filings batch keyed to the same 33 with the BA
  re-run; `comp-secrets` for every key; every world write named with its prefix (`derived/model_block/`, the filings store) and
  no write outside them. The L10 for round 12 grades the peers, Price and filings outcomes against the population these runs
  populate. **RULED by this seat as adjudicator:** the entry is an issuer amendment adding orders now, because the held
  partitions (S120's 70 names, S125's today-dated list, S127's BA re-run) all resolve on these runs and every one of them is
  named in the round-12 L8 packet.
- **`3.0.0_SA_CVO~Z` and `4.0.0_SA_CRO~Z`:** informational; the CRO's item-5 audit re-measures the served plane after the runs
  land, as its own record says it will on the slug.

## 5. STATE AT THE WORD

Round 12 at L7, 9 of 16 orders terminal; the rk-6 co-sign complete on both halves; local SITEZ unpushed since the reboot.
Push state of this record: LOCAL on SITEZ, and this is the last commit before the push he just authorized.
