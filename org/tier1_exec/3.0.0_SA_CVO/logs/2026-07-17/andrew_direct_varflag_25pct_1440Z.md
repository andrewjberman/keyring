# ANDREW-DIRECT record — MDPF_VARFLAG threshold reframe + guard exploration (verbatim)

**archetype:** SCRIBE
**recorded by:** `3.0.0_SA_CVO` · **channel:** Claude Code session, direct to this agent
**time:** 2026-07-17 ~14:40Z (immediately after my MDPF_VARFLAG review delivery @ `4ade1cc08`)

## The word, VERBATIM

> "Ok let's identify how we can do this, look through the historical data, we upload new data every
> single week for most market data so there should be an easy way to do this. Maybe instead of
> 2std, its if any numbers are more than 25% higher or lower than their prior figure, on a
> proportional basis. Try scanning with that perspective. I'd like to make some kind of guard here
> if possible, explore how that could be done."

## Context carried with the quote (surfaced, NOT adjudicated — XXX.md rule)

Arrived at the CVO session directly after the CVO review of `MDPF_VARFLAG_PROPOSAL.md` was
delivered (review @ `4ade1cc08`; the review had surfaced that pure 2σ over ~595 cells yields ~23
spurious flags per clean upload). Plain read: Andrew is entertaining replacing the 2σ statistic
with a **±25% proportional-change-vs-prior-figure rule**, asks for a scan of the historical
vintage data under that rule, and wants guard options explored. This modifies/extends the verbatim
core in the proposal ("outside 2 standard deviations") — latest + most-restrictive binds on
whatever he ratifies after the scan. Scope (whether 25% replaces 2σ, or is a candidate pending the
scan results) is NOT mine to adjudicate — the phrasing is "Maybe" + "Try scanning": an
investigation directive, not yet a ratified threshold change.

## Action taken same turn

- This record committed; broadcast MCP'd to COO + CTO + MSTR.
- Scan executed by CVO against the live S3 version history of the served artifacts (results in
  the companion analysis file / MCP).
