# ANDREW-DIRECT — TO-4 vertical order + the artifact-census → tool-registry plan (briefing to CTO)

**Channel:** MSTR~Z terminal (site Z), direct prompt
**Time:** 2026-08-10 ~1740Z
**Received by:** 0.0.0_AB_MSTR~Z · **Recorded:** same turn (record+broadcast law)
**Consumer:** 1.0.0_SA_CTO~Z (briefing per his closing instruction), cc 2.0.0_SA_COO~Z (TO-4 dispatch owner)

## VERBATIM

> I would start with Model Portfolios, then Pod-2 Analytics, then Macro, then News DDB (as News
> is the most broad/abstract one which we will need to consider how to scope). The premise here
> is that for each Vertical, we need to identify each artifact served on the portal under said
> vertical, where that artifact appears visually (What page -> On header or tab? -> What panel
> in said location is this information featured in? What data fields are available in said
> artifact?). That needs to be a structured deliverable per vertical. I woould suggest having
> 0.5.0 do it for Model Portfolios first and /draw the complete results of their findings. Then
> if I like the structuring, they can proceed to the other surfaces. The premise here is that
> once we have these pages/artifacts completely structured out, then I can provide overhead
> judgment on what the fields mean/how to deliver that information/what information can be used
> in conjunction. To start we just want to focus on serving raw numbers that are citable with
> relevant timestamps. We then want to create a yaml structure or similar index, essentially a
> tool-call registry, so that when the agent is queried about certain topics, it can reference
> its registry to know what information to retrieve and the tool that will go get it. That is
> the baseline expectation. Once this is rigidly established and developed for all surfaces,
> then we can begin getting into more inferential/analysis-forward derivations of that
> information. Let's develop a briefing that covers this step by step plan and deliver that to
> CTO.

## THE STEP-BY-STEP PLAN (briefing body — CTO to shape into TO-4 structure with COO)

**Vertical order (ruled):** 1. Model Portfolios → 2. Pod-2 Analytics → 3. Macro → 4. News DDB.
News is deliberately LAST: it is the broadest/most abstract vertical and its scoping is an open
question to be considered when reached — do not pre-scope it now.

**Step 1 — Per-vertical artifact census (structured deliverable, one per vertical).**
For every artifact served on the portal under the vertical, capture the full visual + data
coordinates:
- WHAT: the served artifact (S3 key / DDB table, exact).
- WHERE, visually, as a strict hierarchy: What page → header or tab? → which panel in that
  location features the information?
- FIELDS: every data field available in the artifact.
The census is a STRUCTURED deliverable — one grammar for all verticals (Rule 24 discipline:
one grain per level, page → location → panel → artifact → field).

**Step 2 — Pilot: 0.5.0 does Model Portfolios FIRST, and /draw's the complete findings.**
The rendered /draw of the full MP census goes to Andrew. **HIS STRUCTURING REVIEW IS THE GATE
FOR PROCEEDING** (his design: "if I like the structuring, they can proceed to the other
surfaces") — this is an Andrew-asked review point, not a manufactured gate. No census work on
verticals 2–4 until his word on the MP structuring.

**Step 3 — Andrew's overhead judgment pass (his, not the fabric's).**
Once pages/artifacts are completely structured, Andrew provides the semantic layer: what the
fields MEAN, how to deliver that information, what information can be used in conjunction.
The fabric produces the structure; the meaning-assignment is sovereign input to be received,
not inferred.

**Step 4 — Baseline serving posture: RAW NUMBERS ONLY, citable, timestamped.**
The concierge serves raw figures with citation (exact artifact) + relevant timestamp/vintage.
No derivation, no inference, no synthesis across artifacts at this stage.

**Step 5 — The tool-call registry (yaml or similar index).**
Build the query-routing index: topic/query-class → what information to retrieve → which tool
retrieves it. When the agent is queried on a topic, it references the registry to know the
retrieval, rather than reasoning it out ad hoc. Natural home: the existing
`refs/DATA_CATALOG.yaml` grammar (fuzzy query → exact key + tool) extended per-vertical off
the census — CTO to judge extend-vs-new (Build Ladder rung 2: the estate already has a
catalog seed).

**Step 6 — THE BASELINE BAR, then (and only then) inferential growth.**
"Rigidly established and developed for all surfaces" is the bar: all four verticals censused,
Andrew's semantic pass done, registry live, raw-number serving exercised. Only after that does
inferential/analysis-forward derivation work begin — it is explicitly OUT of the baseline
scope and needs no design attention now.

## Sequencing note for CTO/COO

TO-4 as previously conceived ("vertical growth") now decomposes per this plan: TO-4a = MP
census + /draw (0.5.0, dispatchable NOW), Andrew structuring review, then TO-4b/c/d per
vertical in ruled order, registry work threading through. COO~Z holds dispatch; CTO~Z owns
the census grammar + registry design judgment.
