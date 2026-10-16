# L4-R review -- NFRA_WFSPINE PRD v0.1, ratified-text half (ENDPOINT + CONTRACTS)

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-16 ~04:1xZ. Delivered by 1.0.0_SA_CTO~DELL1 msg 6472 and its note.
**Graded:** `org/missions/D9/NFRA/NFRA_WFSPINE/prd/NFRA_WFSPINE_PRD.md` @aaa7e63625 (v0.1, half hash d7f784c8ff9a), a new project with no prior signed version.

## Verdict: REFUSE -- C-POPULATION keeps the people Andrew excludes in bronze; FWD-8 says they are absent everywhere

## The four checks

| Check | Result |
|---|---|
| ENDPOINT against its pins | VERBATIM. The FWD-1..FWD-9 block (55 lines) is byte-equal to `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_M365_WORKFLOW_SPINE_20261016.md` @f96be0de11 (diff empty). Andrew's approval of that text reads "Yes I like this layout you have for the project. I approve." (`ANDREW_DIRECT_20261016_035xZ_WFSPINE_DONE_WHEN_APPROVED.md` line 8). The bucket words read "I think all of this should be stored in a bucket called opal-data-trino also, using LGIC_NAMING conventions otherwise." and "its a product folder so follows product rules" (`ANDREW_DIRECT_20261016_040xZ_WFSPINE_BUCKET_OPAL_DATA_TRINO.md` lines 8 and 24). |
| Every operative constraint present | **NO, on one row.** FWD-8's head reads "Andrew decides who is in the spine, and everyone else is absent everywhere". C-POPULATION reads "Only the accounts Andrew lists are collected into silver and beyond. Bronze holds what the source ships, and the population filter applies at the bronze-to-silver step". The Management Activity feed is tenant-wide, so bronze in `opal-data-trino` would hold the raw events of every account Andrew leaves out: their file names, email subjects and client names (C-CLIENTDATA), kept with no stated retention. FWD-8's ACCEPT names "any timeline, chain or suggestion", but the head Andrew approved says "everywhere", and the contract permits more than the head. The rest is present: one app, app-only, one consent, the gateway unchanged (C-APP); hourly scheduled collection with the 7-day loss written (C-COLLECT, C-COVERAGE); no alerting (C-NOALERT); mail and Teams content out (C-CONTENT); builder output for every address and name, with the refusals recorded rather than worked around (C-HOMES). |
| No annotation, history or seat name inside the section | ENDPOINT carries none. |
| CONTRACTS agrees with the counterpart PRD | No counterpart PRD. The query surface keeps NFRA_GLOBGRPH unchanged (C-QUERY), and the registry rows are owed in round 1 and named, not typed (C-HOMES). |

## What would make this signable

One of these, and the choice is Andrew's (it narrows or widens his own words):
1. **Filter at landing:** the collector drops events of accounts outside the population before bronze is written. That departs from R9's "bronze is raw", so it needs an R20 entry for his acknowledgement. Or:
2. **Andrew narrows FWD-8's head** to the derived views ("absent from every timeline, chain and suggestion"), and C-POPULATION states what bronze then holds for an excluded account: who can read it, how long it is kept, and that no Trino namespace exposes it.

Either way, C-POPULATION and FWD-8 then say the same thing. This seat re-signs on a re-read of those two texts alone.

## Noted, not a ground to refuse

- The PRD names the New York employee-monitoring notice (Civil Rights Law s.52-c) as a fact for Andrew and counsel, not a gate. That is the right placement. Any departure in (1) or (2) above touches the same question.
- The secret id has no builder kind (C-HOMES). The PRD leaves it to round 1, cell 1, as the one name it does not fix. It is stated, not hidden.

## What you should have asked

Whether the excluded accounts' bronze is itself the sensitive asset. A timeline view can be withheld, but a tenant-wide raw audit log of who
opened which file and which email subject they sent, for people who were told they are not in the spine, is what an employee notice would be
about.

-- 3.0.0_SA_CVO
