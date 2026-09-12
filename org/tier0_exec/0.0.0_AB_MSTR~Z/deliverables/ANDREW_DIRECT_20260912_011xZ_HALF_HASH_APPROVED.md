# ANDREW-DIRECT 2026-09-12 ~01:1xZ -- "Half hash approved"

**archetype:** RATIFY

**Channel:** Andrew-direct at the `0.0.0_AB_MSTR~Z` terminal, sent mid-turn while this seat was
composing an `/exec-sum`. Recorded and broadcast the same turn per `org/XXX.md`.

## THE WORD, VERBATIM AND ENTIRE

> "Half hash approved, Give me /exec-sum of what's going on on this device right now"

Two clauses. The first is a ratification; the second is a request for a report and carries no
direction to any other seat.

## WHAT IT RATIFIES

`.tools/prd-signoff.py --expect-half-hash`, landed by `1.0.0_SA_CTO~Z` as the L4-R gate's owner at
`7204d31156`, on `origin/SITEZ` in `b9aec29d31`.

A signer may now assert WHICH BYTES IT REVIEWED. If the PRD half has moved since those bytes, the
stamp is REFUSED `rc=3` with both hashes printed. It accepts the 12-char prefix `status` already
prints as well as the full hash. Every pre-existing caller is unchanged.

**Exercised in-path on a REAL sign by `4.0.0_SA_CRO~Z` at 00:59:46Z, both arms:**

```
NEGATIVE  --expect-half-hash 219a6113f   (the half actually reviewed in section 9)
          while current is 590ba0cbf3ae  -> REFUSED rc=3, both hashes printed
POSITIVE  --expect-half-hash 590ba0cbf3ae (the 12-char prefix status prints)
          -> STAMPED rc=0, POSN_ASTTAX ADMITTED
```

The refusal was measured a TRUE NO-OP: after it the record still read `signed_at 00:47:19Z` with
`review_ref d5b216a3bd`, and `git status --porcelain` on the sign-off directory was EMPTY.

⭐ **The negative arm was the REAL INCIDENT, not a fixture.** `219a6113f` is the half that seat
actually read; `590ba0cbf3ae` is what the bad stamp actually bound 2m35s after the CTO landed it.
The guard was pointed at the event that motivated it and refused it.

## ⛔ WHAT THIS WORD DOES **NOT** REACH -- stated so nobody widens it

He approved the half-hash guard. **He did not name any of the following, and none of them is
authorized by this sentence:**

1. **The `prd_signoff_lib.py:198` VERSION-STRING FALLBACK.** A record with no `half_hash` is still
   graded on `prd_version`. Making that fail-closed would flip **IRPT_BCKEND and IRPT_FNTEND from
   ADMITTED to WITHHELD immediately**, on the LAPTOP fabric, mid-winddown. That is a separate act
   with a named blast radius and it is NOT covered here. Row `AMGT_RESAPP-Z-S6` stays ARMED and is
   `1.0.0_SA_CTO~Z`'s.
2. **The `--review` artifact guard** (limb (b) of the CRO's two-limb REC): `--review` accepts any
   string and never checks the path resolves. `4.0.0_SA_CRO~Z`'s own stamp `9a2e542c0b` carries
   PROSE in that field and `git show` of it returns ZERO BYTES. Different defect, not named.
3. **The re-stamp of the four IRPT records.** Parked with this seat as owner --
   `PARKED_20260912_IRPT_L4R_RESTAMP_CROSS_FABRIC.md`. Un-parks on those laptop seats being live, or
   on Andrew widening site-Z scope past AMGT_RESAPP + POSN_ASTTAX.
4. **The portal freeze and the CLOUD->SITEZ leg-2.** Untouched by this word.

⭐ The general class all three instances belong to, and it is a bigger statement than any of them:
**every field in an L4-R sign-off record is written by the party it certifies and validated by
nobody** -- `half_hash` excepted only because the tool computes it. What Andrew just approved is the
act that moved `review`-to-bytes OUT of that set. The `review_ref` path is what remains in it.

## PUSH STATE

The ratified gate is already on `origin/SITEZ` (`b9aec29d31`, ls-remote read). Nothing about this
ratification requires a new deploy, a gate flip, or an act by any other fabric.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015xKcpLRvtCWL5P3uTb6L3g
