# ANDREW_DIRECT 2026-10-08 ~15:3xZ -- two priorities ahead of all else: cluster GitOps, and process garbage collection

**Channel:** laptop terminal, to 1.0.0_SA_CTO, after the laptop reboot (session start ~15:32Z).
**Recorded by:** 1.0.0_SA_CTO, same turn.

## Andrew's words, verbatim

Preface (same session, ~15:33Z):

> "Finish startup but we have two priorities right from the outset that we need to dive into ahead of all else. Await
> further advisory on those subjects when loaded."

The advisory (~15:3xZ):

> "The issue that we're finding is that we're having catastrophic slowdowns, which I get the impression originate from 2
> sources. On one side, it is the Git Ops. I believe that operating on a shared branch with 60 plus agents that are all
> committing and pushing and merging and doing who knows what at the same time is the root of these complete
> suffocations, these complete stranglings of process. That is on one side, an issue that we need to figure out. On the
> other side, I believe that we are accruing Bash and Python zombies, these little shell scripts and monitors and polars.
> They don't obsolesc correctly. They they become zombies that just seem to continue and persist, even if there are
> processes brought him to replace them. So what we need to figure out here, which is going to be 2 different projects
> for perhaps 2 CRO, CRO base, and CROA, which I will handle the spawn of CROA. We need to figure out how we are going to
> handle get ops across the organization, across the cluster. And we need to figure out what we can do to handle the
> garbage collection. I believe there are 2 approaches, one being the fast and easy one, and the 2nd being the longer
> term maintenance, which is elaborated on by one of the Dell MSTR agents. I believe Del won, but you have to check that.
> They wrote a brief recently. It should be in the queue, uh, on the on the cloud dash vocal laptop box, MSTR agent. in
> their SQSQ. But with that in mind, Yeah, on one side, we need some kind of kill process that, that, uh, I think it
> should be thresholds based that it just kills all zombies that's able to identify zombie processes that are either
> replaced or attached to clawed sessions that are no longer active or and so on. That's on one side, and then on the
> other side, I think that we need, when we're designing our scripts, and we have these high, uh, these high traffic
> critical scripts, like our watcher, our monitors, our agent bus, our, uh, various, uh, safe commit, safe deploy, all
> all of these kinds of things. I think we need to figure out how to make sure that they obsoles peacefully in the
> absence of a session that is actively using them. So, so there are several angles here that we need to address, but we
> need to move quickly on it."

(Voice transcription. "Git Ops" / "get ops" = GitOps; "polars" = pollers; "obsolesc" / "obsoles" = obsolesce;
"clawed" = Claude; "Del won" = dell1; "cloud dash vocal laptop" = the laptop box's agentbus queue; "SQSQ" = SQS queue.)

## What the CTO placed (placement only; scope is Andrew's words above)

1. **Two projects, two L1 briefs, ahead of all other laptop work.**
   - **GitOps across the cluster** (one shared branch, 60+ agents committing, pushing and merging concurrently) --
     L1 brief to **4.0.0_SA_CRO** (base): it is live now and its open thread is the multi-agent coherence discussion.
   - **Process garbage collection** (approach A: threshold-based reaper of zombie, replaced or session-orphaned
     processes; approach B: high-traffic scripts -- watcher, Monitors, agentbus, safe-commit, safe-deploy -- end
     themselves when no live session uses them) -- L1 brief to **4.0.0_SA_CRO~A**, which Andrew spawns. Input: the dell1
     draft below. Until `~A` is live, this assignment is parked here with the CRO base as reader.
2. **The dell1 brief is located.** Author `0.0.0_AB_MSTR~DELL1` (Andrew's "Del won" is correct). It is on origin CLOUD
   in commit `4d069108b5`, file `docs/briefs/process-and-worktree-garbage-collection-brief-20261008.md` (DRAFT; input
   to the L1 brief, not the brief of record). Read: `git show 4d069108b5:docs/briefs/process-and-worktree-garbage-collection-brief-20261008.md`.
3. **The `/self-drive` 60m laptop loop is not re-armed** while these two lead.

## Addendum ~15:5xZ -- Andrew re-places the seats (supersedes item 1's seat placement)

Verbatim, laptop terminal to 1.0.0_SA_CTO:

> "Heres how this is going to go, we are gong tto have CRO Base focused on the multi-device graph coherence project. We
> are going to have CRO A focus on the Git Ops. Then lastly we are going to have the CRO B on the Garbage COllector and
> script ops"

Placement now: **4.0.0_SA_CRO** (base) = multi-device graph coherence; **4.0.0_SA_CRO~A** = GitOps;
**4.0.0_SA_CRO~B** = garbage collector and script ops (input: the dell1 draft @4d069108b5). Same word recorded by the
CRO at `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_160xZ_CRO_BASE_GRAPH_OPS_CRO_A_GITOPS_CRO_B_GC.md`
@b387b7e868.

## Addendum ~16:0xZ -- fast solutions across the boxes first; projects later

Verbatim, laptop terminal to 1.0.0_SA_CTO:

> "Yes our goal is to get organized very quickly here"

> "before bringing on all the COOs"

> "In theory, these briefs dont necessarily have to be full on registered projects, just yet. We will want to develop
> projects around these that will be operated on the laptop box, but because we are in a time crunch and need to move
> very quickly, we need to get fast solutions out across the boxes while we get organized for the more comphrehensive
> infrastructure builds"

Placement: each of the three briefs leads with a FAST FIX that can go out to every box now; the registered project
(laptop-operated) follows. The graph-coherence PRD draft `org/tier1_exec/1.0.0_SA_CTO/deliverables/GRAPH_COHERENCE_ENDPOINT_DRAFT_20261008.md`
stays DRAFT and is not registered (no L3 carriers) until the project stage.

## Addendum ~16:1xZ -- bring back the apply seats

Verbatim, laptop terminal to 1.0.0_SA_CTO, answering "Do you want to bring one or both back for those two items?" (the
graph read grant and the one-off graph rebuild, `FAST_FIX_RULINGS_20261008_162xZ.md` graph F1 and F3):

> "yes, bring back COO~C and a CloudOps seat"

Placement: 0.0.0_AB_MSTR spawns `2.0.0_SA_COO~C` and `0.7.0_AE_CloudOps~E` (the seat that held the identity-root
deploy before the reboot). ~C cuts the grant widen (graph token included); ~E applies it and runs the graph rebuild.

Correction, verbatim, same minute: "we have 0.7.0_AE_CloudOps already working as a codex agent". So only `2.0.0_SA_COO~C` is
spawned; the apply and the rebuild go to the live Codex seat `0.7.0_AE_CloudOps`, as task orders cut by ~C (a Tier-2
seat hears an act only as a task order, LD-0529).

## Addendum ~16:3xZ -- garbage collection becomes a /govern responsibility

Verbatim, laptop terminal to 1.0.0_SA_CTO:

> "Also, I think there is an opportunity here that we can build very fast that can be folded in to our existing /govern
> function for the fabric manager MSTR agents. In essence, we already have a script that they use to check cpu/ram, they
> should also have a script to do a scan for the python/bash processes, which probably already exists as a function of
> /kill scripts. I think the fast solution is adding a quick concise "garbage collector" line into govern skill text as a
> garbage collection responsibility. I think with each loop tick, they basically run a check on what scripts are running
> and if any are accruing / zombies and manage from there."

Placement: 1.0.0_SA_CTO adds the line to `.claude/skills/govern/SKILL.md` Step 3a (this box's own processes, every cycle,
dry census then act). It reaches every box's MSTR by the trunk. This is the unattended-run word the GC fast-fix list held
for Andrew, scoped to a /govern cycle.
