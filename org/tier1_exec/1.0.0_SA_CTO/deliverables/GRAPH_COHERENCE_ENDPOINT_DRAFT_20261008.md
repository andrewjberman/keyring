# NFRA_GRPHCO PRD -- multi-device graph coherence

```json
{
 "project": "NFRA_GRPHCO",
 "directive": "D0",
 "fabric": "laptop",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/multi-device-graph-coherence-brief-20261008.md@8b4f996b64",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "status": "DRAFT"
}
```

**prd_version:** v0.1 (ENDPOINT and first SURFACE MANIFEST; contracts follow at L4)
**Owner:** 1.0.0_SA_CTO | **Directive:** D0 | **Macro:** NFRA
**Brief (L1):** `docs/briefs/multi-device-graph-coherence-brief-20261008.md` @8b4f996b64 (14,335 bytes), by 4.0.0_SA_CRO
**Placement (L2, 1.0.0_SA_CTO, 2026-10-08 ~16:0xZ):** its own project, not an addition to NFRA_CTLPLN. Andrew's later
word names it "the multi-device graph coherence project" (record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_160xZ_CRO_BASE_GRAPH_OPS_CRO_A_GITOPS_CRO_B_GC.md`
@b387b7e868). NFRA_CTLPLN is a dependency: it applies every IAM and secret-class change this project needs (brief Part II).

---

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  A seat on a Dell, about to change one part of the estate, asks the shared graph from its own box what that
         part is and what it connects to, and learns from the same answer which other box changed it today
         DONE WHEN  EXERCISED -- one live trace, a real seat on a Dell asking a real question about a real part of the
                    estate, ending in the answer it read
         ACCEPT     the seat gets its answer without going through the laptop; the answer says how old it is and it is
                    from today; it names the other box, the seat and the change that touched the same part today
         SOURCE     brief Part I, "THE CANDIDATE THREAD" (lines 47-56)

  FWD-2  A seat on any of the four boxes asks the same graph question with the same tool and gets the same answer
         DONE WHEN  EXERCISED -- the same question asked on the laptop, dell1, dell2 and site Z, and the answers read
         ACCEPT     four boxes, one question, four matching answers, and no box relayed the question for another
         SOURCE     brief O1 (lines 58-61)

  FWD-3  A seat can tell how current its answer is, and under normal running it is current
         DONE WHEN  EXERCISED -- an answer read on an ordinary day, and an answer read after a rebuild was made to fail
         ACCEPT     every answer says when the facts behind it were gathered; on an ordinary day that is recent enough
                    that nobody acts on a state the estate has already left; when the overnight rebuild fails, a seat
                    reading the graph can see that it failed instead of being handed the old picture as if it were new
         SOURCE     brief O2 (lines 63-67)

  FWD-4  A seat names a part of the estate and learns who else is working on it
         DONE WHEN  EXERCISED -- the question asked about a part that two boxes have both touched, and the answer read
         ACCEPT     the answer lists each box, seat, project and task order that has claimed, edited, merged a change to,
                    or holds a deploy on that part, each with when it happened, and a person checking it against what
                    actually happened finds nothing missing and nothing invented
         SOURCE     brief O3 (lines 69-73)

  FWD-5  Andrew asks where the boxes overlap and gets the answer on demand
         DONE WHEN  EXERCISED -- Andrew, or a box's integrator, has asked and read the answer
         ACCEPT     Andrew reads a list of the parts of the estate with two or more boxes on them, and which boxes, without
                    a seat assembling it by hand; nothing notifies anyone and nothing blocks anyone
         SOURCE     brief O4 (lines 75-79)

  FWD-6  A Dell records its own activity in the shared graph itself
         DONE WHEN  EXERCISED -- a Dell's own change shows up in the graph, written from the Dell
         ACCEPT     a change made on a Dell appears in the graph without the laptop carrying it, about as quickly as a
                    laptop change does, so that no box is a second-class source
         SOURCE     brief O5 (lines 81-84); Andrew's call 3, "They should be able to"

  FWD-7  Andrew decides what the shared graph runs on, knowing the engine's makers publish no new versions
         DONE WHEN  APPLIED -- the decision is written down with Andrew's word on it
         ACCEPT     the record says which choice Andrew made, says plainly that the engine's makers publish no new
                    versions while the graph's facts stay current every night, and says what each choice would cost
                    the other outcomes here
         NOTE       Andrew-direct ~17:4xZ: "A for now, also i dont think its actually frozen youre just not accounting
                    for the stitch functions." Stay on the current engine for now.
         SOURCE     brief O6 (lines 86-91)
```

NOT READ (Phase 0 reads the brief only): the task-order register, any project JSON, the NFRA_CTLPLN PRD, the two prior
research files the brief stands on (@f4cac7f3dc, @f0b12ccd02), any Dell or site Z box.

---

## SURFACE MANIFEST (step 4 -> step 5)

`claim`: `held` = the brief's measurement, not re-read at L4 yet; `unmeasured` = new.

| id | outcome_ref | surface | claim | evidence | verb | depends_on | bound |
|---|---|---|---|---|---|---|---|
| S01 | FWD-1, FWD-2 | secret `opal/mcp/graph-read-token` classed PLATFORM-KEY; Dell group secrets grant | held (brief Part IV.3: `derive_vendor_secrets.py:156`, `iam.tf:155-165`) | Dell read path | wire | -- | applied by NFRA_CTLPLN, never by this project |
| S02 | FWD-1, FWD-2 | served graph endpoint `mcp.opalinvest.dev/graph/cypher` and the comp-tools that read it | held (brief Part IV.1) | one read route for every box | read | S01 | read-only |
| S03 | FWD-3 | served vintage and the overnight rebuild's publish state | held (brief Part IV.2, `comp-graph status` 15:52Z) | freshness a seat can see | wire | -- | no monitor, no alert |
| S04 | FWD-1, FWD-4, FWD-5 | fabric layer: box, seat, project, task order, commit; declares, edits, holds, merged | unmeasured (research @f4cac7f3dc section 5) | who-else and overlap | build | S02 | read on demand; nothing refuses |
| S05 | FWD-6 | graph bucket `opal-313476888478-globgrph`; Dell `s3:PutObject` on `opal-*/*`; row NFRA_CTLPLN-S31 | held (brief Part IV.4, policy read only) | Dell writes its own activity | wire | S04 | a sanctioned write shape; grant applied by NFRA_CTLPLN |
| S06 | FWD-7 | Kuzu 0.11.3 pin in the projection worker | held (brief Part IV.5, `projection_worker.py:303`) | engine decision record | decide | -- | decision only, no migration |
