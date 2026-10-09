# ANDREW_DIRECT 2026-10-09 ~00:0xZ -- keep the work driving: an open-call queue that forces adjudication, cross-adjudication files, and /next-calls on an empty drive tick

**Channel:** laptop terminal, to 1.0.0_SA_CTO. **Recorded by:** 1.0.0_SA_CTO, same turn. **Owner of the build:** 4.0.0_SA_CRO~B,
spawned for it this turn; Andrew will talk it through in that seat's session.

## Andrew's words, verbatim

> "I need to figure out a mechanism where we keep the work driving. I thought that the canonical-drive loop would be enough, but
> what i notice happening is that agents are working up to a point and they either get caught on an open call, or get caught
> waiting for some external thing to happen (e.g. a 7a pull the next day). We have so much work to do it is astronomical, which
> means we really can't afford to let stuff like this sit when there is really so much to do. i think there are two clear
> solutions that could be optimized. 1.) open calls must filter up into a queue. We already have this in place but it doesnt
> sponsor any action. I think there should be a "notification" function that scans that json per box every 10 min and if it has
> open-calls on it, the CTO on that box has to adjudicate. If it is a case where the fix is open-ended, or otherwise seems like it
> is deeply architectural or may overlap with other boxes, then in that case that CTO should write a file including the context,
> their position on it, and a breakdown of the reason why it gave them pause (was it ambiguous? if so how? is it out of pattern?
> why are you not using the normal pattern? are there other solutions that could be better? what are they and why? etc). Then
> that document gets transferred to the laptop CTO, or SiteZ CTO as a backup if the laptop is down, to ajudicate, and the laptop
> CTO notes these adjudications in a document type somewhere (same concept as change-management files, but id call it
> cross-adjudication files). 2.) If a COO has canonical-drive or closer-drive running on a given project, and they have an empty
> tick, they are to run /next-calls and proceed with the chosen sequence. This should continue until there is truly nothing left
> for them to do. I think next-calls should also be reformatted slightly for this case whereby it includes the option of "if you
> are blocked or waiting on one thing, what else can you be doing to proceed this project outside of that?" just so we dont have a
> single sequence that gets blocked on one track and all the other work needed for a project is now gated/bottlenecked on a
> trigger or something stupid. I want you to take this whole text block and notate it as an andrew direct, sending it to CRO~B to
> figure out. CRO~B will be spawned by you on this turn, and their task will be to figure this out as well as get it
> implemneted. I will be in their session to talk it through with them as well."

## The two mechanisms, as stated (placement only; scope is his words)

1. **Open-call queue that forces action.** A notification scans each box's open-calls JSON every 10 minutes; any open call makes
   that box's CTO adjudicate. An open-ended, deeply architectural or cross-box call becomes a written file (context, the CTO's
   position, why it gave pause: ambiguity and how, out of pattern and why, better alternatives and why) sent to the laptop CTO
   (site Z CTO as backup when the laptop is down), who adjudicates and records it in a new record type: **cross-adjudication
   files**, on the model of the change-management files.
2. **No empty drive tick.** A COO running `/canonical-drive` or `/closer-drive` whose tick finds nothing to do runs `/next-calls`
   and proceeds with the chosen sequence, until there is truly nothing left. `/next-calls` gains a branch: "if you are blocked or
   waiting on one thing, what else can you be doing to proceed this project outside of that?", so one blocked track never gates
   the rest of a project.

## Known constraint to design around (the CTO's note, not his words)

CLAUDE.md section 5 carries a standing moratorium on building alerts, monitors and notification senders "unless Andrew explicitly
asks". His words above explicitly ask for a "notification" function that scans every 10 minutes; that is the explicit ask, scoped
to this one mechanism.
