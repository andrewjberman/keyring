# ANDREW-DIRECT 2026-09-24 ~14:3xZ (~10:3x AM ET) -- Report 2: the canonical flow and the closer flow, a fast closer mode, /closer-drive, and the switch between them

**Channel:** the `4.0.0_SA_CRO~A` terminal, typed by Andrew mid-turn during this seat's `/watcher` + `org/XXX.md`
startup, received ~14:37-14:39Z.
**Received and recorded by:** `4.0.0_SA_CRO~A`, same turn.
**Recon ID:** RCN-0017 (RCN-0016 is reserved by `4.0.0_SA_CRO~B` for the process-debt brief, which Andrew calls report 3).

## Verbatim

> I want to go through some conceptual architecture with you and have that be analyzed and rendered into a brief. We had built this /closer skill with the purpose of making
>   a faster flow than /canonical-flow. I want to assess the dynamics of how we switch back and forth between these two and how, based on your analysis of the two, we make
>   revisions to improve the quality. The issue that we're having is that there is so much process debt that we really need to clear out (this will be report 3), but in the
>   interim I want to tighten up these two functions (and also add a /closer-drive that mirrors /canonical-drive which is basically a faster version with no subagents and
>   looser permissions/verification load). My issue with the canonical drive flow is that somehow it just takes far too long to go through projects, so we had made edits to
>   it yesterday where the entire purpose for new projects run via canonical-flow requires an end to end build completed in round 1. I want to identify where else it is slow,
>   where we are taking up too much time with process bureaucracy. Part of report 2 is identifying process bureaucracy within the canonical flow and process. We want to find
>   mechanisms that can be employed to optimize iterative cycling and outcome generation. For example, before the edits yesterday, we would have an entire process flow and
>   subagent spawn to change one font's weight. I think we have since fixed for that, but by the same token, if even in the current state the task orders are very light
>   coding tasks (analyze canonical flow runs in the last  12 hours to support/refute how light the TOs are), maybe we need to use simpler models like sonnet on medium effort
>   or opus low effort? not sure how to optimize there but optimization needs to happen. Outside canonical flow, on closer flow i want there to be a mode where it just
>   drives hard and fast, I want to identify where we have opportunities to relax restrictions for it. The major concerns are on shared surfaces where agents could crash, or
>   scenarios where they could accidentally be duplicating existing work. Take a look at these and write a report to optimize both flows, as well as synthesize how they can
>   be better interchanged. For example, i like canonical-flow if i am away from the computer because more verification is good when im sleeping and not present. If I am at
>   the computer however i prefer a closer version that can just move fast. This is why there needs to be a clean and clear mechanism to switch back and forth between the
>   two.

(Typos, spacing and line breaks are his, preserved as pasted.)

## Scope as given (not widened, not narrowed)

- **Report 2.** Analyze the canonical flow and the closer flow; find where canonical is still slow and where process
  bureaucracy inside the canonical flow costs time; measure the canonical runs of the last 12 hours to support or
  refute that the task orders are light coding tasks; recommend model and effort choices; define a fast "drive hard"
  closer mode and the restrictions it can relax, with shared surfaces and duplicated work as the two named concerns;
  specify `/closer-drive` as the fast mirror of `/canonical-drive` (no subagents, looser permissions and verification);
  and design a clean mechanism to switch between the two, canonical when he is away and closer when he is present.
- **Not in scope:** report 3 (the process-debt clean-out). `4.0.0_SA_CRO~B` holds that brief under its own
  Andrew-direct of ~14:4xZ (`ANDREW_DIRECT_20260924_144xZ_PROCESS_ARCHITECTURE_BRIEF.md` in this folder). Report 2
  cites it rather than re-measuring the estate-wide debt.
- This seat researches and PROPOSES. Skill, spine and law edits, hooks and dispatch belong to the owning seats.

## Deliverable

`org/tier1_exec/4.0.0_SA_CRO/deliverables/REPORT2_CANONICAL_AND_CLOSER_FLOWS_SPEED_MODE_AND_SWITCH_20260924.md`.
