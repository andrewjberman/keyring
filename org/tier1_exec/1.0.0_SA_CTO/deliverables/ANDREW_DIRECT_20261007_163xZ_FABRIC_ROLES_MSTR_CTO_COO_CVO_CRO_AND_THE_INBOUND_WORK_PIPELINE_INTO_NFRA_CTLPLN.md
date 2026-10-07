# ANDREW-DIRECT 2026-10-07 ~16:3xZ (1.0.0_SA_CTO terminal) -- how each seat operates in a fabric, and the inbound-work pipeline; all folded into NFRA_CTLPLN

## His words, VERBATIM AND ENTIRE

> "Also I want to take this opportunity with CTLPLN to refine how MSTR and CTO agents operate in the fabric. MSTR whole purpose is not business logic/project reasoning, they are infrastructure managers. They manage merges/pulls/pushes/integrates across the fabric. They also can manage /unstick /mstr-spawn /mstr-kill to keep their fabric running cleanly. They also need to have that functioning bid pipeline for pulling in work based on utilization, which is key for work that comes in via Teams/Outlook/etc. I think we need to have a defined pipeline, maybe an extension of the Kimi Teams agent, that is constantly checking for requests of that nature, because that needs to be organized and tightened. The agents that get those jobs should be spawned fresh, briefed, and run /remote-drive. I recommend this going to a dedicated COO. Moving past that, The CTO is the business-logic/project-focused lead on their fabric. They are responsible for accruing any and all /open-calls on their fabric. If the open call in question only pertains to their fabric, does not interfere with any other projects resources or materials, they can adjudicate them. If however there is an open call that touches multiple surfaces, they must have their MSTR reach out to the MSTR of the relevant fabric and coordinate as needed. COOs are the workers, they either run /canonical-drive /closer-drive to proceed projects, running /remote-drive if a one-off request comes in, which I will get the text at the Quo line from the Kimi agent with a recommendation if they identify that work is being requested. CVO is dedicated reviewer in those drive processes so mandatory spawn on any fabric. If there are multiple projects attached to one macro on a fabric, it is best practice to spawn a CVO specific to that macro, e.g. CVO~NFRA. CRO is the dedicated research agent. Their primary use case is analyzing projects with me and running /brief-create to kick off the /canonical-flow , however an almost equally important use case is researching risky or otherwise unclear operations of meaningful at the behest of the fabric's CTO. On the risk side, if the project does not meet a meaningful quantified risk layer (I know we are indexing this somewhere and already have this classified), there is no need to bring them out. I want all of this folded in to NFRA_CTLPLN. We need to lock in these processes more formally, whether it takes place in launcher updates, skill updates/creation, gates, etc., I want to make sure we cover both GitOps, AWS DevOps, and Agent Workflow Ops as is described above."

## What it states, by seat (his terms, not widened)

| Seat | What he says it is | What he says it does |
|---|---|---|
| MSTR | an infrastructure manager; "not business logic/project reasoning" | merges, pulls, pushes, integrates across the fabric; `/unstick`, `/mstr-spawn`, `/mstr-kill`; a working bid pipeline that pulls in work by utilization, for work arriving by Teams, Outlook and the like |
| CTO | "the business-logic/project-focused lead on their fabric" | accrues every `/open-calls` item on its fabric; adjudicates one that pertains only to its fabric and interferes with no other project's resources or materials; for one that touches several surfaces, has its MSTR reach the MSTR of the relevant fabric and coordinate |
| COO | "the workers" | `/canonical-drive` or `/closer-drive` to proceed projects; `/remote-drive` for a one-off request |
| CVO | the dedicated reviewer in those drives | a mandatory spawn on any fabric; where several projects share one macro on a fabric, best practice is a CVO for that macro, for example `CVO~NFRA` |
| CRO | the dedicated research agent | with Andrew: analyzing projects and `/brief-create` to start `/canonical-flow`; for the fabric's CTO: researching risky or unclear operations of meaningful risk. Below "a meaningful quantified risk layer" it is not brought out |

**The inbound-work pipeline, as he describes it:** something constantly checking Teams, Outlook and similar for requests, "maybe an
extension of the Kimi Teams agent"; when work is being requested he gets a text at the Quo line from the Kimi agent with a
recommendation; the agent that takes the job is spawned fresh, briefed, and runs `/remote-drive`; he recommends this goes to a
dedicated COO.

**Where it lives:** "I want all of this folded in to NFRA_CTLPLN." **How it is locked in:** launcher updates, skill updates or
creation, gates. **Coverage he names:** GitOps, AWS DevOps, Agent Workflow Ops.

## Not said, or left open by him (stated so nothing is read into it)

- "maybe an extension of the Kimi Teams agent": a suggestion of form, not a decision.
- Which index holds the quantified risk layer: he says it exists and is classified; he does not name it.
- "researching risky or otherwise unclear operations of meaningful" ends there in his text; read with the next sentence it
  means meaningful risk.
- Nothing here changes an existing hard stop, a never-widen rule or the canonical workflow's limb owners.

## Acts taken on it, same turn

- Broadcast to `0.0.0_AB_MSTR`, `3.0.0_SA_CVO`, `4.0.0_SA_CRO`, `2.0.0_SA_COO~C`.
- An L1 brief asked of `4.0.0_SA_CRO` for this addition to NFRA_CTLPLN; the PRD addendum follows the brief.
