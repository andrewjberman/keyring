# ANDREW-DIRECT 2026-09-30 ~17:45Z -- NFRA_MCPMSP: the outside-Teams test is struck; the first live Inflection conversation is not a gate at this stage

**Channel:** Andrew, in-session at the 2.0.0_SA_COO~MS terminal (site Z), 2026-09-30 ~17:45Z.
**Recorded by:** 2.0.0_SA_COO~MS. **Carrier:** this file; one line to 1.0.0_SA_CTO~O names it.

## Andrew's words, verbatim

> There is no way for us to test outside teams test. I dont think that needs to be tested anyway, its not a major
> priority nor should it block work accordingly. I would be fine with striking that from reqs even. Also the first live
> inflection conversation is not happening, we are so far from that. There are countless things we need to do before
> that; that cannot be a gate at this stage in development.

## What it refers to (the issuer's reading of the objects, not a ruling on scope)

- "outside teams test" = NFRA_MCPMSP round 1 **hop 0, the federated-chat probe** (PRD v0.3 Canonical handoff hop 0,
  acceptance **A0**, surface S1, gate G-OUTSIDE): one outside test account sending a one-to-one Teams chat to an Opal
  user, read through the gateway's Teams reader.
- "the first live inflection conversation" = round 1's **close run** (acceptance **A1**, FWD-1's DONE WHEN "EXERCISED --
  one live conversation, read end to end"), which the decomposition v1 section 8 and the round-1 drain-end read
  (msg to 1.0.0_SA_CTO~O, 2026-09-30T15:07Z) carried as waiting on G-USER, G-IT-INF, G-ADVISOR, G-FIRM and G-PUSH.

## State at the time of the words (measured)

- Round 1: 10 of 10 task orders terminal and drained @1fe1ef07b3 (LOCAL). Neither hop 0 nor the close run was run.

## Scope

Per org/XXX.md ("the receiving agent does NOT adjudicate scope"), this record relays the words; it does not itself
amend the PRD's ENDPOINT or acceptance matrix. Striking A0 from the requirements and re-placing FWD-1's live
conversation are PRD acts of 1.0.0_SA_CTO~O. What Andrew's words decide directly, verbatim: neither item "should ...
block work" / "cannot be a gate at this stage in development".
