# ANDREW-DIRECT 2026-09-03 ~02:2xZ -- L7 WORKERS are TIER-2 ONLY; NFRA_COMPEFFICACY's worker count is ONE (`0.8.0_AE_CloudComp`)

**Channel:** Andrew, in person, at the `2.0.0_SA_COO` (base, laptop) terminal, replying to this seat's report that
"all three L7 workers" (`1.0.0_SA_CTO`, `3.0.0_SA_CVO`, `0.8.0_AE_CloudComp`) were executing. **Recorded by:**
`2.0.0_SA_COO`. **Corrects:** this seat's broadcast 92900 s.6 and its GOs 92905 (TO-CE-DISC-2 -> `1.0.0_SA_CTO`) and
92906 (TO-CE-TP-1 -> `3.0.0_SA_CVO`), and reading 4 of the record @`2bec6afa0a`, which called `3.0.0_SA_CVO`'s seat on
TP-1 "an L7 WORKER".

## VERBATIM

> WHat do you mean all three L7 agents? Only tier2 agents are workers, MSTR does not "WORK" on projects, they are an
> integrator. COMPEFFICIENCY workers at this point number at 1, which is 0.8.0_AE_CloudComp

## What it binds (readings, marked)

1. **The transcript's L7 "workers" are TIER-2 seats only.** A Tier-1 exec (`1.0.0_SA_CTO`, `3.0.0_SA_CVO`, `4.0.0_SA_CRO`,
   `2.0.0_SA_COO`) does not hold an L7 task order; `0.0.0_AB_MSTR` integrates (push windows, cross-fabric) and never
   works a project.
2. **Round 1 of `NFRA_COMPEFFICACY` has ONE worker and ONE live task order:** `TO-CE-T-1` at `0.8.0_AE_CloudComp`
   (@`4d9cd02e40`, GO 92913, acked 92920).
3. **The two mis-seated task orders are WITHDRAWN by their issuer** (this seat, msg 92927-92930, same turn): TO-CE-DISC-2
   and TO-CE-TP-1. The files stay on disk with a WITHDRAWN status line as record.
4. **READING, marked -- this seat's L6 routing of the two withdrawn cells, reversible on his word:** both were STAGE 0
   "decide-first" cells, i.e. SPEC DECISIONS the PRD had left open (the 4.3 answer-state spellings; Rule T's budget
   form for s.4.4). A spec decision is L4 content and stays with the L4 owner, `1.0.0_SA_CTO`, as a PRD version on that
   owner's own authority -- no task order, no proof-of-spec instance, no report cycle. A re-address to a Tier-2 worker
   was NOT chosen: a worker writing normative spec that CTO must then land in the PRD is a second wrapper around the
   same act, the opposite of the tight circle the transcript asks for.
5. `3.0.0_SA_CVO` stands down from TP-1 and holds for L8. His "you are not going to be driving this" at the CVO
   terminal (@`96af269f47`) and this correction read the same way; the open call CVO surfaced (92909 s.3(b), whether
   its worker seat survives) is CLOSED in the restrictive direction by this word.

## Where this seat went wrong (so the class is named, not the incident)

The 00:5xZ proposal that Andrew approved ("cut the first three task orders", @`774c108bb5`) already named `1.0.0_SA_CTO`
and `3.0.0_SA_CVO` as assignees, and this seat read his approval of the CUT as approval of the SEATING. The transcript
(02:07Z) then fixed L7 as "the workers"; this seat kept the Tier-1 assignees and relabelled them "L7 workers" instead
of asking who a worker is. **Latest + most-restrictive binds: a role-exclusivity word re-classifies every earlier
seating it touches, including ones he approved before it existed.**

## NOT read into it

- No change to TO-CE-T-1 (scope, acceptance, the interim expiry grammar, the CVO grade clause) -- unchanged, live.
- No change to the decomp's cell ids or order; CE-disc-2 and CE-tp-1 remain cells, now satisfied by an L4 landing
  rather than a task order.
- No lift of the D2 `/drive` hold; zero crons; nothing about CLDGRPH or ETFS_GUARDRAIL.
