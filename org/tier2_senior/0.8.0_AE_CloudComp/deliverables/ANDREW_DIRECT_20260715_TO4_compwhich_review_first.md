# ANDREW-DIRECT (recorded verbatim, same turn) -- TO-4 comp-which top-k: REVIEW-FIRST, do not touch what works

**Channel:** direct session message to 0.8.0_AE_CloudComp~Z (mid-turn, Claude Code session 34c46bed)
**Time:** 2026-07-15 ~21:0xZ (received while committing TO-3)
**Recorded by:** 0.8.0_AE_CloudComp~Z, same turn, per the RECORD+BROADCAST law (org/XXX.md)

## Verbatim

> "Also just noticing TO-4, you shouldnt need to touch any of comp-whichs description or top-k.
> My understanding is that it already is doing top-3 with great descriptions that are working
> great, so id review the current state of that before touching it at all. Don't let this get
> you off track, just make sure to heed these comments before addressing TO-4 in your greater
> task list."

## Scope (surfaced, NOT adjudicated -- the receiving agent does not adjudicate)

Plain reading: TO-4 (NFRA_GRAPHFEED.W1, "comp-which top-k per NFRA_COMPASSURANCE_COMPWHICH_TOPK.md,
Andrew verbatim 'top-5 with attached description'") begins with a CURRENT-STATE REVIEW, not an
implementation. Andrew's understanding: comp-which already serves top-3 with descriptions, working
great. Corroborating observation already banked this session (before this instruction): live
comp-which output prints "MATCHES (top 3 of 58 -- score is overlap, NOT a confidence)" with
per-candidate descriptions AND writes the full ranked+described list of all 58 tools to
.comp-graph/which/rank-<pid>.yaml per call.

Open question the review must answer (not assumed either way): whether the existing top-3 +
full-rank-file behavior satisfies the COMPASSURANCE PRD's "top-5 with attached description"
directive as-is, and what the zero-result rate measures now (the ~34% full-tally number the PRD
attacks). Any touch to comp-which's ranking/description surface is contingent on that review
finding a real gap -- latest + most-restrictive binds.

Note: this session's TO-3 registration added a comp-axes CURATED RULE to comp-which (routing
vocabulary only, pre-instruction, frozen baseline re-verified PASS) -- no ranking/description/
top-k surface was touched.
