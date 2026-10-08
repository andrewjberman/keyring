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

## Addendum ~16:4xZ -- restart the laptop fabric; no fabric-wide deploys on this box

Verbatim, laptop terminal to 1.0.0_SA_CTO:

> "Ok great, now I think we need to get the fabric on here rolling again. ALl i recall that you had going was COO~G. We
> should no longer need to be running deploys for the whole fabric on this box, so that should take off some of the load
> on that basis."

Placement: 0.0.0_AB_MSTR spawns `2.0.0_SA_COO~G` to resume LGIC_BLANKFIX round 6 (its handoff @d96bc61aed: round 5
closed, round 6 drafted, not issued). The laptop is the control plane: no deploy seat is re-seated here to carry other
boxes' deploys (0.7.0_AE_CloudOps~E and ~F stay down); a deploy for a project placed on another box runs on that box.

Same minute, verbatim: "With that in mind, we do have the codex 0.7.0_AE_CloudOps available and idle as needed for
deploys on this box". So the laptop's own deploys (e.g. the NFRA_CTLPLN identity-root apply) go to the Codex seat
`0.7.0_AE_CloudOps`, by task order.

## Addendum ~17:0xZ -- GitHub Actions budget

Verbatim, laptop terminal to 1.0.0_SA_CTO, answering (1) add a cancel-superseded-runs rule to portal `ci.yml`? and (2) read
the Actions minute usage through the GitHub API?: "1.) No need. 2.) Yes". Per-use word for one read of the Opal-Capital
org's billing usage and budgets (gh api). Read ~17:0xZ: plan `free`; October 1-8 Linux minutes 1,811 (portal 1,035,
ajb_workspace 769, opal_ai 7), all inside the included allowance; Actions budget $200 with prevent_further_usage=false
(alerts to the org owner), so Actions do not stop when the allowance runs out.

## Addendum ~17:1xZ -- status of the box managers on the new GC and GitOps abilities

Verbatim: "Yes I updated it, i also want to make sure that the various MSTRs across the boxes are now managing with the new
garbage collection and git ops abilities, get status on this". ("it" = the GitHub Actions budget.) Read at ~17:1xZ:
origin CLOUD 838362db08; since the fast-fix push a92d59d74f, dell1 has drained and pushed (838362db08), dell2 and site Z
have not. 0.0.0_AB_MSTR collects a per-box status over the bus.

## Addendum ~17:1xZ -- the CROs drive changes themselves; de-duplicate against 2.0.0_SA_COO~C

Verbatim: "I have also tasked the CROs (Base ~A and ~B) with driving changes themselves, because we need to move and a lot of
this isnt complicated. I want you to get timing expectations from that group and check in with COO~C and make sure taht
their work is not duplicated or in any way overlapping. Likely makes the most sense to start with COO~C first to establish
what is in their workstream"

Placement: 1.0.0_SA_CTO reads 2.0.0_SA_COO~C's workstream (cells, write paths, state) first, then asks 4.0.0_SA_CRO,
~A and ~B for timing and their write paths, and rules any overlap to one owner.

## Addendum ~17:4xZ -- Andrew answers six open calls

Cards put at ~17:3xZ (1 unattended cleanup: (a) /govern only or (b) also a scheduled task; 2 two-phase commit on for the
laptop ~2:10 PM ET; 3 start the long-term self-ending script packages; 4 graph engine: (a) stay on Kuzu 0.11.3, (b) a
fork, (c) another way; 5 branch model: (a) one trunk, (b) per-box, (c) per-project; 6 automatic worktree removal and its
limits). Verbatim answer:

> "1.) A is better for now. 2.) Yes, but faster, 2p ET today. 3.) rec approved. 4.) A for now, also i dont think its
> actually frozen youre just not accounting for the stitch functions. 5.) A for now but we need to get on to B very soon it
> is a priority. 6.) Yes sure, CRO~B is working on a formal version of this"

Routing: 1 -> 4.0.0_SA_CRO~B (no scheduled task installed; /govern Step 3a.6 is the one unattended reaper). 2 -> 0.0.0_AB_MSTR
and 4.0.0_SA_CRO~A (two-phase safe-commit ON by default on the laptop at 2:00 PM ET = 18:00Z today). 3 -> 4.0.0_SA_CRO~B
(start P1, the comms watchers). 4 -> 4.0.0_SA_CRO (stay on Kuzu; the engine's upstream is archived, but the served graph is
not frozen: the stitch functions keep it current). 5 -> 4.0.0_SA_CRO~A (keep one trunk now; per-box branches are a
priority, design starts now). 6 -> 4.0.0_SA_CRO~B (worktree removal allowed: merged, clean, idle 48 h, never `drain-*`,
logged; its formal version governs).

## Addendum ~17:4xZ (1:45 PM ET) -- site Z locking up; move the cluster now

Verbatim, laptop terminal to 1.0.0_SA_CTO, after being told site Z's merge waited on his word at its terminal:

> "Also i can see the locking up is already beginning to happen on the sitez box, which i interpret as a function of not
> having the efficient gitops on there. It is currently 1:45p, we should begin making moves across the cluster to get on
> that now."

Placement: this is the word for site Z to drain the fast-fix set now (origin CLOUD, which holds a92d59d74f), the
drain-worktree way, then the one-time kill-maint sweep and /govern 30m. Two-phase safe-commit follows when the laptop's
first read is clean; that read is pulled forward from ~18:45Z to ~18:15Z.

## Addendum ~18:3xZ -- two carried calls answered

Cards put at ~18:2xZ: (1) restart this seat's hourly /self-drive over the laptop directives now, at the :17 slot, with GitOps,
GC and graph coherence ranked first each tick; (2) delete the 159 old `origin/q/*` branches once per-box branches have run
clean -- only those already in the trunk, after all four boxes run a full day on their own branches, the other 10 listed for
their owners first. Verbatim answer:

> "1.) Yes. 2.) YEs."

Placement: (1) this seat re-arms `/self-drive` at `17 * * * *` off the arming record
`ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`, the three priorities first. (2) B8 of
`PER_BOX_BRANCH_BUILD_PLACEMENT_20261008.md` is authorized on those terms; 0.0.0_AB_MSTR deletes when the condition reads true.
