# STEP LOG COMPILATION -- NFRA_COMPEFFICACY round 1 (compiler 1.0.0_SA_CTO, against the spine v2.1)

**Denominator:** 63 rows from 4 of 6 expected seats (0.0.0_AB_MSTR, 1.0.0_SA_CTO, 2.0.0_SA_COO, 3.0.0_SA_CVO filed; missing: 4.0.0_SA_CRO, 0.8.0_AE_CloudComp). Per limb: L10 3, L2 2, L3 1, L4 4, L5 3, L6 5, L7 3, L8 3, L9 4, X 35. Per quadrant: ON_PLAN_EFFICIENT 38, ON_PLAN_DEFICIENT 10, OFF_PLAN_DEFICIENT 10, OFF_PLAN_EFFICIENT 5.

## The four quadrants

| quadrant | rows | reading |
|---|---|---|
| ON_PLAN_EFFICIENT | 38 | the loop worked |
| ON_PLAN_DEFICIENT | 10 | plan-improvement opportunities |
| OFF_PLAN_EFFICIENT | 5 | worked, but ruled out or absorbed into the plan |
| OFF_PLAN_DEFICIENT | 10 | gate candidates |

## Gate-candidate classes

- **a Tier-1 seat holding an L7 task order** -- rows [('1.0.0_SA_CTO', 11), ('2.0.0_SA_COO', 3), ('2.0.0_SA_COO', 4), ('3.0.0_SA_CVO', 10)] -- CLOSED -- gate (i) @caa8b5c3a5 refuses it at commit
- **the issuer committing a worker's status text / anyone but the COO issuing** -- rows [('2.0.0_SA_COO', 8)] -- CLOSED -- lane grant @f9c97a52ce + limb (iv) @c765283365
- **a surprise carried by message instead of a row** -- rows [('3.0.0_SA_CVO', 12)] -- CLOSED -- surprises limb @7968221ef5 + law @6e8805eb90
- **the CVO messaging a worker during L7-L10 (and an issuer endorsing it)** -- rows [('2.0.0_SA_COO', 10)] -- OPEN -- spine v2.1 states it; the mechanical guard is Andrew's call (a broker send from 3.0.0_SA_CVO to a Tier-2 serial while the project is in L7-L9: refused or announced). His words lean to the gate.

## Plan-improvement classes

- **CVO engaged at L2-L7 before the ruling** -- CLOSED in the spine (not-engaged sets); guarded by reading only
- **the L4 owner accepting drafts/reads of an L4 artifact from a non-engaged seat** -- CLOSED in the spine
- **a CVO review sequence treated as the condition for opening L6** -- CLOSED in the spine (no certification before L6)
- **dep_stage flipped by hand, late** -- OPEN -- candidate: flip on the first tree TO mechanically
- **a bound amendment by message before the artifact carried it** -- OPEN -- candidate: artifact first, message names it
- **push windows: two frames per window on a refused re-read; six windows in two hours** -- OPEN -- Andrew gates cadence while at the terminal (LD-0522)

## Every row

| seat | seq | limb | quadrant | disposition | discriminator |
|---|---|---|---|---|---|
| 0.0.0_AB_MSTR | 1 | X | ON_PLAN_EFFICIENT | NONE | integrator startup; a broker trap banked |
| 0.0.0_AB_MSTR | 2 | X | ON_PLAN_EFFICIENT | NONE | a push window with ls-remote before and after |
| 0.0.0_AB_MSTR | 3 | X | ON_PLAN_EFFICIENT | NONE | the carrier function to Andrew; its content became the governing record |
| 0.0.0_AB_MSTR | 4 | X | ON_PLAN_DEFICIENT | PLAN_IMPROVEMENT | the same-breath re-read refused once (a commit inside the hold); two frames per window |
| 0.0.0_AB_MSTR | 5 | X | ON_PLAN_EFFICIENT | NONE | cross-fabric exchange, assess-only on his launch row |
| 0.0.0_AB_MSTR | 6 | X | ON_PLAN_EFFICIENT | NONE | a law push with its record |
| 0.0.0_AB_MSTR | 7 | X | ON_PLAN_DEFICIENT | PLAN_IMPROVEMENT | re-read refused on a peer's staged paths; two frames again |
| 0.0.0_AB_MSTR | 8 | X | ON_PLAN_EFFICIENT | NONE | the brief on his word; the census deferred to the spec decomp |
| 0.0.0_AB_MSTR | 9 | X | ON_PLAN_EFFICIENT | NONE | a ruling recorded; the first draft corrected before committing |
| 0.0.0_AB_MSTR | 10 | X | ON_PLAN_EFFICIENT | NONE | a push window |
| 0.0.0_AB_MSTR | 11 | X | ON_PLAN_EFFICIENT | NONE | carried a proposed limb to Andrew; approved |
| 0.0.0_AB_MSTR | 12 | X | ON_PLAN_DEFICIENT | PLAN_IMPROVEMENT | six windows in two hours read by him as interrupting the fabric; push cadence is his to gate while at the terminal |
| 0.0.0_AB_MSTR | 13 | X | ON_PLAN_EFFICIENT | NONE | the READ clock honoured on every message |
| 1.0.0_SA_CTO | 1 | X | ON_PLAN_EFFICIENT | NONE | a sovereign word recorded verbatim; the record law, outside the limbs |
| 1.0.0_SA_CTO | 2 | L2 | ON_PLAN_EFFICIENT | NONE | L2 owner ran the L2 instrument on the L1 artifact; qualitative outcomes, each cited |
| 1.0.0_SA_CTO | 3 | X | ON_PLAN_EFFICIENT | NONE | gate infrastructure before L3 on his word; red-first; not a limb act |
| 1.0.0_SA_CTO | 4 | L3 | ON_PLAN_EFFICIENT | NONE | L3 owner registered under the tree; the validator's refusals fired then cleared |
| 1.0.0_SA_CTO | 5 | L4 | ON_PLAN_DEFICIENT | PLAN_IMPROVEMENT | L4 owner landed the PRD, but from a draft authored by a seat the spine keeps out of L4; v2.0 now says 'not engaged' |
| 1.0.0_SA_CTO | 6 | L4 | ON_PLAN_DEFICIENT | PLAN_IMPROVEMENT | same class: an L4 version driven by a CVO row-by-row read of an L4 artifact |
| 1.0.0_SA_CTO | 7 | L5 | ON_PLAN_EFFICIENT | NONE | row owner flipped dep_stage on the L5 handoff |
| 1.0.0_SA_CTO | 8 | X | ON_PLAN_DEFICIENT | PLAN_IMPROVEMENT | the readers' repair was right; treating a CVO review sequence as the condition for opening L6 was not -- v2.0: nobody certifies before L6 |
| 1.0.0_SA_CTO | 9 | X | ON_PLAN_EFFICIENT | NONE | a hold on his word; nothing half-landed |
| 1.0.0_SA_CTO | 10 | X | ON_PLAN_EFFICIENT | NONE | startup and the record+broadcast law |
| 1.0.0_SA_CTO | 11 | L7 | OFF_PLAN_DEFICIENT | GATE_CANDIDATE | a Tier-1 seat accepted an L7 task order; L7 is Tier-2 only |
| 1.0.0_SA_CTO | 12 | L4 | ON_PLAN_EFFICIENT | NONE | L4 owner closed two open spec decisions as data; limb 5 exercised on the bytes; the notifier reached READ |
| 1.0.0_SA_CTO | 13 | X | ON_PLAN_DEFICIENT | NONE | the report was owed and sent; one clause read the wrong plane and was retracted -- a seat error, not a plan gap |
| 1.0.0_SA_CTO | 14 | X | ON_PLAN_EFFICIENT | NONE | process law on his mandate, outside the round; the round's L7 completion ran through the gates it produced |
| 1.0.0_SA_CTO | 15 | L6 | ON_PLAN_DEFICIENT | PLAN_IMPROVEMENT | the flip is the row owner's and it happened 98 minutes late; nothing flips dep_stage mechanically on the first task order |
| 1.0.0_SA_CTO | 16 | X | ON_PLAN_EFFICIENT | NONE | process law on his word, outside the round |
| 2.0.0_SA_COO | 1 | X | ON_PLAN_EFFICIENT | NONE | startup per the protocol; no project act before his word |
| 2.0.0_SA_COO | 2 | X | ON_PLAN_DEFICIENT | PLAN_IMPROVEMENT | record+broadcast law followed; the record's reading seated a Tier-1 seat as an L7 worker and needed his correction |
| 2.0.0_SA_COO | 3 | L6 | OFF_PLAN_DEFICIENT | GATE_CANDIDATE | two of three task orders named Tier-1 seats in <issued_to> |
| 2.0.0_SA_COO | 4 | L6 | OFF_PLAN_DEFICIENT | GATE_CANDIDATE | two of three GOs dispatched to Tier-1 seats |
| 2.0.0_SA_COO | 5 | L6 | ON_PLAN_EFFICIENT | NONE | the correction executed within minutes: withdrawn as task orders, decisions routed to their L4 owner |
| 2.0.0_SA_COO | 6 | L5 | ON_PLAN_DEFICIENT | PLAN_IMPROVEMENT | L5 owner amended the decomposition; the bound amendment reached the worker by message before the artifact carried it |
| 2.0.0_SA_COO | 7 | X | ON_PLAN_EFFICIENT | NONE | registry grantor widened a lane the law needed; measured before and after |
| 2.0.0_SA_COO | 8 | L6 | OFF_PLAN_DEFICIENT | GATE_CANDIDATE | the issuer committed the worker's own status text because the lane refused the worker |
| 2.0.0_SA_COO | 9 | X | ON_PLAN_EFFICIENT | NONE | registry grantor on his word; proposed the limb the grant made necessary |
| 2.0.0_SA_COO | 10 | L10 | OFF_PLAN_DEFICIENT | GATE_CANDIDATE | endorsed the CVO's direct ask to a worker during L7-L10; named by him as off the intended flow |
| 2.0.0_SA_COO | 11 | X | ON_PLAN_EFFICIENT | NONE | record+broadcast law; the session log |
| 2.0.0_SA_COO | 12 | L10 | ON_PLAN_EFFICIENT | NONE | L10 route received by its owner; the next acts are L5 then L6 |
| 3.0.0_SA_CVO | 1 | X | ON_PLAN_EFFICIENT | NONE | infrastructure review of the gates; later ruled not a limb engagement |
| 3.0.0_SA_CVO | 2 | L2 | OFF_PLAN_EFFICIENT | PLAN_IMPROVEMENT | engaged with L2 (CTO only); it helped and he ruled it out -- the spine now names the not-engaged set |
| 3.0.0_SA_CVO | 3 | L4 | OFF_PLAN_EFFICIENT | PLAN_IMPROVEMENT | drafted an L4 artifact (CTO only); adopted and ruled out |
| 3.0.0_SA_CVO | 4 | L5 | OFF_PLAN_EFFICIENT | PLAN_IMPROVEMENT | certified the L5 decomposition; void under the state of record |
| 3.0.0_SA_CVO | 5 | X | OFF_PLAN_EFFICIENT | PLAN_IMPROVEMENT | decided a spec question outside L4; carried into the PRD by its owner |
| 3.0.0_SA_CVO | 6 | L7 | OFF_PLAN_EFFICIENT | PLAN_IMPROVEMENT | graded a worker deliverable as certifier of record; that role is void; the per-tool grade itself is the project's L8/L9 work under the PRD |
| 3.0.0_SA_CVO | 7 | X | ON_PLAN_EFFICIENT | NONE | a hold on his word |
| 3.0.0_SA_CVO | 8 | X | ON_PLAN_EFFICIENT | NONE | startup |
| 3.0.0_SA_CVO | 9 | X | ON_PLAN_EFFICIENT | NONE | record+broadcast law with two surfaces, not adjudicated |
| 3.0.0_SA_CVO | 10 | L7 | OFF_PLAN_DEFICIENT | GATE_CANDIDATE | a Tier-1 seat accepted an L7 task order |
| 3.0.0_SA_CVO | 11 | X | ON_PLAN_EFFICIENT | NONE | handed everything drafted to the L4 owner as input, up the loop |
| 3.0.0_SA_CVO | 12 | L8 | OFF_PLAN_DEFICIENT | GATE_CANDIDATE | assembled a row from a surprise that arrived by message only; the carrier was the deviation |
| 3.0.0_SA_CVO | 13 | X | ON_PLAN_EFFICIENT | NONE | relayed a sovereign word; recorded |
| 3.0.0_SA_CVO | 14 | L8 | ON_PLAN_EFFICIENT | NONE | L8 intake via the notifier and a re-derived evidence item; the message to the worker that followed is scored under rows 17 and 21 |
| 3.0.0_SA_CVO | 15 | L9 | ON_PLAN_EFFICIENT | NONE | L9 grounding with three exercised measurements |
| 3.0.0_SA_CVO | 16 | L9 | OFF_PLAN_DEFICIENT | NONE | an in-place disposition flip; the existing row gate refused it and the write was discarded -- the gate exists and fired |
| 3.0.0_SA_CVO | 17 | L9 | OFF_PLAN_DEFICIENT | GATE_CANDIDATE | the additive adjudication was right; the disarm ask went directly to the worker |
| 3.0.0_SA_CVO | 18 | X | ON_PLAN_EFFICIENT | NONE | the annex rewritten under the amendment protocol |
| 3.0.0_SA_CVO | 19 | L8 | ON_PLAN_EFFICIENT | NONE | L8 intake + L9 verification of the worker's measurement, line by line |
| 3.0.0_SA_CVO | 20 | L9 | ON_PLAN_EFFICIENT | NONE | L9 discriminating measurement; the cheapest hypothesis that fit, confirmed |
| 3.0.0_SA_CVO | 21 | L10 | OFF_PLAN_DEFICIENT | GATE_CANDIDATE | the stamp and the backward route were right; operating instructions went directly to the worker |
| 3.0.0_SA_CVO | 22 | X | ON_PLAN_EFFICIENT | NONE | the step log in the schema |

0.8.0_AE_CloudComp's step log is not filed at compile time; this compilation covers 4 of 6 expected seats and is re-run when it lands. 4.0.0_SA_CRO was not live in round 1 (the L1 artifact was an ANDREW_DIRECT record).
