# ANDREW-DIRECT 2026-09-11 ~19:0xZ -- "yes to all recs": all four `/open-calls` cards RULED

**archetype:** COORDINATE

**Channel:** Andrew-direct at the `0.0.0_AB_MSTR~Z` terminal (this seat), answering this seat's
`/open-calls` output of ~19:0xZ.

## THE WORD, VERBATIM AND ENTIRE

> "yes to all recs"

Terse, so **what it answers is recorded here in full** -- a bare "yes" is only as legible as the cards
it lands on, and a successor reading this record must not have to reconstruct them.

## WHAT HE SAID YES TO -- the four cards as presented, unedited

| # | call | REC he approved |
|---|---|---|
| 1 | The `opal-data-research` rename ruling rested on a false premise ("no data in there") -- re-rule or let it stand? | **LET IT STAND**, run as a MEASURED MIGRATION: copy all 53 objects preserving key grammar, verify destination count = 53 and paths match, only then delete source; accept the ~7 lost overwrite-versions explicitly |
| 2 | Authorise the CLOUD->SITEZ merge leg? | **YES** -- overlap 0.84%, one mechanical-union conflict, deploy ceiling 0 both directions |
| 3 | Re-pin the `opalbloomberg` gateway token on site Z (D7 intake) | **DO IT BEFORE THE NEXT REAL TICKET**, not after one goes quiet |
| 4 | Widen the M365 gateway allowlist for attachments | **WIDEN IT** -- attachment-only is a main inbound path, and the cost is invisible to the sender |

**Cards 3 and 4 are HIS OWN ACTS** (a credential re-pin and an allowlist change at his terminal).
His yes is agreement to take them, not an instruction to this seat -- **no agent executes either**, and
this record does not treat them as delegated.

**Card 2 IS this seat's act** and is executed this turn. **Card 1 is `4.0.0_SA_CRO~Z`'s to sequence**
under his execute-and-oversee word; this seat routes, it does not sequence.

## ⛔ CARD 1'S REC WAS INCOMPLETE WHEN HE APPROVED IT -- AND HE IS BEING TOLD, NOT HELD

`1.0.0_SA_CTO~Z` msg 21542 landed **after** the cards were presented and **before** his answer was
recorded. It adds a THIRD dimension to the rename that card 1's REC did not carry:

**THE RENAME IS ALSO A CODE CHANGE.** `comp-find 'opal-data-research' --band DEF` -> 12 of 328 hits
across 56,355 files, confirmed independently by two seats on their own runs:

```
 1  ENV-OVERRIDABLE   pull_enqueue/lambda_function.py:32  (RESEARCH_BUCKET env -- config, not code)
 1  INHERITS          pull_consumer.py:45  (BUCKET = mbp.BUCKET -- re-point the parent, this follows)
10  REQUIRE AN EDIT   5 LIVE: derive_fye_fixed.py:33 · model_block_pull.py:43 ·
                              pull_baba_daily_px.py:29 · lib/research/freshness/build_view.py:54 ·
                              lib/research/ledger/ledger.py:37
                      5 worker check scripts under deliverables/ (proof reproduction path)
```

⛔ **MIGRATING THE DATA WITH THE CODE UNTOUCHED IS THE ONE VARIANT WHERE NOTHING ANNOUNCES THE BREAK.**
Five live modules would point at a bucket that no longer exists and fail at **RUN** time, not at apply
time -- so the migration looks clean and the breakage surfaces later, on whatever runs first.

⚠ **AND IT HAS A CLOCK.** `AMGT-rd-5`'s chatter producer runs daily at `cron(0 10 * * ? *)` UTC. **A
rename landing between two fires breaks the next one silently.** At this record's vintage (~19:0xZ
2026-09-11) the next fire is **2026-09-12 10:00Z**, so roughly a FIFTEEN-HOUR clear window exists --
ample, but it is a window and not an absence of one.

>> **HIS RULING IS NOT HELD HOSTAGE TO THIS.** The migration is still authorised and still the right
   act; what changed is that its SEQUENCING now has three parts (data, code, timing) rather than one.
   Surfacing it is not re-litigating it. <<

**ALSO CARRIED FORWARD:** the recommendation to collapse the ten literals onto one shared constant or
env var, so the NEXT rename is a config change rather than this conversation again. Adopted by the CTO
as its own recommendation; `4.0.0_SA_CRO~Z`'s to sequence, a gate from nobody.

## A COUNT CORRECTION THAT CUTS TOWARD THE SAFER READING

The first census said ELEVEN edits and SIX live modules; the confirming run reads **TEN and FIVE**,
because `pull_consumer.py:45` DERIVES its bucket from `model_block_pull` and needs no edit -- the
comment on that line says so in terms. ⭐ **Whoever wrote that line made this migration cheaper**, and
the correction was published precisely because a SMALLER number is the one more likely to be
under-checked.

## WHAT IS NOW CLOSED

Card 1's underlying ruling (rename, from ~18:5xZ), card 2 (merge leg), and his agreement on cards 3
and 4. **Also closed earlier the same hour and NOT re-asked in those cards:** POSN_ASTTAX round 2 may
route (his "call 1 yes"), which lifts the LD-0521 precondition **for that round only** -- the rule is
not amended and still binds every other round.

## WHAT REMAINS UNRULED

The **Bright Data Web Unlocker proxy vendor** for the three session harvesters -- a NEW per-use vendor
call, not triggered unless the EC2 IP proves unworkable against PerimeterX. Deliberately NOT put in
front of him tonight: it is event-gated and asking early would spend his attention on a fork that may
never open.

**PORTAL REMAINS FROZEN**, both fabrics, PROD and DEV, until he names it. Nothing in "yes to all recs"
touches it -- none of the four cards was a portal card, and reading a general yes as lifting a specific
standing hold is exactly the widening CLAUDE.md forbids.
