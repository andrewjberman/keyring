# ANDREW-DIRECT 2026-09-16 ~21:0xZ -- laptop fabric closed; CTO reinstate at 7:10p EDT; full merge with MSTR~Z; new tier/model policy

**Seat:** `0.0.0_AB_MSTR` (laptop) · **Channel:** typed at this terminal · **Recorded:** the turn it was given.

## VERBATIM AND ENTIRE

> "We need to keep costs low so keep chatter to a minimum. I have already closed out the entire fabric on this
> device. Usage limits reset at 7p EDT so I have set 1.0.0_SA_CTO~Z on the sitez box with a 7:10p EDT cron to
> reengage their fabric to pick up AMGT_RESAPP work at that time. I want to do a similar operation on this box,
> reinstantiating the tier1 fabric with the instruction to begin work on their sequence.yaml flow through LGIC
> at that time. In the interim, I want you to orchestrate a full merge on the ajb_workspace repo with MSTR~Z.
> Something they have brought in which is key to be aware of, is that we are now defaulting tier1 agents to be
> loaded at Opus 5, and Tier2 agents and /canonical-flow subagents at Sonnet 5, both High Effort. the sitez
> fabric has already instituted some of this logic, and I need that brought over here with the merge."

## WHAT IT ASKS

1. Mirror Site Z's pattern: reinstate this box's Tier-1 fabric (read as `1.0.0_SA_CTO`, the same single-seat
   shape Site Z used, not the full CTO/COO/CVO/CRO set) at 7:10p EDT, directed at `org/missions/SEQUENCE.yaml`
   and the LGIC project sequence.
2. In the interim: orchestrate a full merge of `ajb_workspace` with `0.0.0_AB_MSTR~Z`.
3. A model-tiering policy change, already instituted in part on Site Z, to arrive here via that merge: Tier-1
   agents default to Opus 5 / High effort; Tier-2 agents and `/canonical-flow` subagents default to Sonnet 5 /
   High effort. This SUPERSEDES the 2026-08-24 rule in `.tools/ajb.ps1`/`spawn-agent.ps1` (Tier-2/3 -> Opus 5 /
   xhigh; Tier-1 carried no default at all).

## MEASURED AT THE START (21:0xZ)

- Zero `claude.exe` processes besides this one (PID 8220) -- his "closed out the entire fabric" confirmed by
  process check, not assumed.
- `.tools/ajb.ps1:228-255` and `.tools/spawn-agent.ps1:39-61` still carry only the 08-24 rule. The new
  tiering policy is NOT reimplemented here -- his own word is that it arrives via the merge from Site Z, and a
  parallel reimplementation on this side would be the shadow-pipeline class CLAUDE.md forbids. Relayed to
  `0.0.0_AB_MSTR~Z` (bus msg 5d264a85) asking it to name the exact commit(s) and push them.
- The prior CLOUD<->SITEZ merge leg (this seat's earlier turn) was left BLOCKED: `0.0.0_AB_MSTR~Z`'s
  `safe-merge --continue` on the resolved `lambda-source-map.json` conflict hit the surprise-row-gate returning
  rc=1 with no violation named, held on Andrew's word at that terminal. Read `.tools/surprise-row-gate.py` (no
  Site-Z state touched): the only rc=1 path with no violation list is the top-level catch-all at :2358-2361
  (`REFUSED: unexpected error`). Handed to `0.0.0_AB_MSTR~Z` as the likely diagnosis (bus msg 5d264a85), asking
  for the full stderr if it recurs.

## ACT TAKEN: scheduled reinstatement

Windows Scheduled Task `OpalReinstate-1.0.0_SA_CTO-20260916`, one-shot, trigger `2026-09-16T19:10:00-04:00`
(this box's own clock is Eastern-time, DST-aware -- confirmed `Get-TimeZone` before scheduling). Action:
`.tools\spawn-agent.ps1 -Model claude-opus-5 -Effort high 1.0.0_SA_CTO "<hand-off text>"`.

The Opus-5/High is passed EXPLICITLY on the scheduled invocation rather than left to the code-level default,
because `-Model`/`-Effort` "ALWAYS WINS" over any tier default per `spawn-agent.ps1`'s own precedence comment --
so the spawn is correct at fire time whether or not the merge (item below) has landed the tiering-policy code
change by then.

The hand-off text names `org/missions/SEQUENCE.yaml` and the LGIC state at hand-off (NAMING closed; ENFORCE
round 3 issued-unspawned per `2.0.0_SA_COO~G`'s wind-down handoff; CANON round 3 not cut; LGCTFM at L5;
NFRA_SPMOVE queued behind the three LGIC issuances) so the reinstated CTO starts from measured ground rather
than rediscovering it.

## IN PROGRESS: the merge

Relayed to `0.0.0_AB_MSTR~Z` over the bus (msg 5d264a85, ~21:0xZ) in one message: (1) the model-tiering ask
above, (2) the surprise-row-gate diagnosis, (3) a request to resume the CLOUD->SITEZ leg it already owns
(one-resolver rule unchanged; this seat will not merge SITEZ into CLOUD in parallel while that leg is held).
Outcome recorded when it lands.
