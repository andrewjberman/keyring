# /drive — 2.0.0_SA_COO~Z, D-family scoped loop, 2026-08-20T20:37–20:45Z (day tick 25)

**archetype:** VALIDATE

The blocker I found last tick closed in 22 minutes, and a new Andrew-direct landed that binds how
every agent writes.

| Project | Class | Owner | Attestation | Action |
|---|---|---|---|---|
| D7 TAC-4 | **CLOSED — VALIDATED** | `0.5.0_AE_OpalETL~Z` authored @6e5670fed2 | **my own** validator run rc=0 VALID (4 rows, 0 violations) + **my own** control rc=1 | validated, not accepted on report |
| D7 TO-AC flip | **ONE WORD AWAY** | `1.0.0_SA_CTO~Z` (acceptance) | all four TAC rows satisfied at my hold | acceptance stamp requested; **I did not flip on my own validation** |
| Full-serial rule | **COMPLIED + defect found** | mine | @a6d824f79b, 60 replacements, 0 defects, verified both directions | W-C half (a) gained an assignee it never had |
| D7 W-lanes | queued, in order | `0.5.0_AE_OpalETL~Z` | re-read the amendments; "building NOTHING out of order" | none needed |
| Live intake loop | **HEALTHY** | `0.5.0_AE_OpalETL~Z` | 20:29:46Z + 20:34:46Z passes, exit 0, `fetched=0` | production surface watched, not assumed |

## TAC-4 — and why I ran the control myself

`0.5.0_AE_OpalETL~Z` had already run their own mutant (expected set naming TAC-9 → rc=1,
violations=2, recorded in the instance's `controls.mutant` as M4). I ran a **different** one
(TAC-42) from my own seat anyway. Not distrust — **a validator that cannot fail proves nothing about
the instance that passed**, and two independent controls reaching the same verdict is a stronger
object than either alone. rc captured unpiped both times.

## The full-serial rule found a real defect, not a style issue

Andrew-direct ~2036Z (record @9e1e94c4f4, via `0.4.0_DT_ClientPlatform~Z`): agents refer to other
agents by **FULL SERIAL**. Applied to my four TOs — scoped to my own artifacts, never another
seat's files, never history.

**W-C's half (a) read "DE-class hands AT THE NEXT SEAT WINDOW."** That is not an address at all: the
portal half of a JOINT task order named **nobody** — no seat to spawn, no serial to GO. Now
`0.4.0_DE_ClientPlatform~Z`.

⛔ **AND THE FABRIC-SPECIFIC HAZARD, which is sharper than the rule as stated:**
`0.4.0_DE_ClientPlatform~Z` and `0.4.0_DT_ClientPlatform~Z` **differ by one letter and both are real
registered seats.** His measured instance was two seats answering to one shorthand; this is the
adjacent, worse shape — **a single-character slip inside a FULL serial still lands on a live wrong
seat**, and `send_message` returns DELIVERED either way. **Consequence for the proposed send-time
lint:** checking "is this a registered serial" would **not** catch a DE/DT transposition, because
both match. Surfaced to `1.0.0_SA_CTO~Z` with the routing, not built.

*Method note: the replace used a negative lookbehind so an already-full serial could not be
double-prefixed, and I verified in both directions afterward — no double-prefix artifacts, no bare
shorthand remaining, denominator printed. The one surviving `DE-class` string is inside my own
correction note, quoting the old text; the scanner flagged it and I read the context instead of
blind-fixing a deliberate citation.*

## Two corrections banked from `0.5.0_AE_OpalETL~Z` (their own, unprompted)

1. **An ASCII control that does not exist.** A readback had credited "ensure_ascii doing its job"
   for the buzz body being pure ASCII. The composer performs **zero** ASCII coercion — today's body
   was ASCII because a human typed ASCII. Killed before it hardened into a standing property; the
   first client typing a curly apostrophe would have falsified it in the channel.
2. **A 200 that cannot fail.** `https://opalinvest.dev/<anything>` returns 200 — the SPA catch-all
   answers every path, so their nonexistent-route control returned 200 too. The render clause was
   recorded as a **DECLARED EXCLUSION**, not a PASS.

Both are the same discipline as the TAC-4 mutant. **I checked my own TAC-2' record against both:**
it never cited a 200 and never credited ASCII coercion — it claims the link *carries the param*,
which is what was actually measured. It holds.

Dispatches: 1 (three recipients, one act — 3 DELIVERED / 0 QUEUED / 0 REFUSED). Gate: **PASS** —
the tick's blocker was validated closed, the sovereign instruction was complied with the same tick
it arrived, and the one remaining gate (the TO-AC acceptance stamp) is genuinely another seat's word
with the request already fired.

## Compiler Tools
`proof-of-spec-check.py` positional ×2 (the PASS and my own discriminating control — rc unpiped
both). `fabric-check`/`deploy_ledger` cycle gates clean. A python pass with lookbehind + a
two-direction verifier for the serial rewrite, because a blind replace would have produced
`2.0.0_SA_2.0.0_SA_COO~Z` and a bare grep would not have shown it.
