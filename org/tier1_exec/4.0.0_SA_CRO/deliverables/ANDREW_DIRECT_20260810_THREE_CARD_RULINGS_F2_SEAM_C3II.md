# ANDREW-DIRECT 2026-08-10 (~17:1xZ) -- THREE CARD RULINGS: F-2 conditional, seam edge AUTHORIZED with a territory caveat, C3.ii folded into Item 0

**Recorded by:** `4.0.0_SA_CRO` (Chief Research Officer)
**Channel:** CRO terminal, answering the /open-calls cards.
**Status:** SOVEREIGN. Verbatim. Broadcast to CTO + COO + MSTR + CVO same turn.

---

## CARD 1 -- F-2 (ATOM_DECOMP rule-list fork): RULING IS CONDITIONAL ON A STRUCTURAL FACT

VERBATIM: *"Does either rule-set structurally dictate the remainder of the functionality? If so,
that should be the canonical one. If it is just prose rules that are not structurally-linked, then
I'd say synthesize the best rules from both versions. If however there is structural connection then
we should focus on tightening synthesis on that basis and striking the rest."*

**The decision procedure he set:**
1. **IF one list is structurally load-bearing** (the rest of the corpus keys on it -- gates,
   templates, workflow steps citing its numbers) -> **that list is canonical**; tighten synthesis ON
   THAT BASIS and STRIKE the rest.
2. **IF both are free-floating prose** -> **synthesize the best rules from both** into one list.

**The structural fact was NOT known at ruling time.** CRO measures it (same day) and executes the
matching branch. The measurement and its result are recorded in the companion investigation note.

## CARD 2 -- THE SERVE-SEAM EDGE: BUILD AUTHORIZED, WITH ONE DEFINITIONAL CAVEAT

VERBATIM: *"I do authorize the build, the only caveat I'd provide is really delving into the logic
between aws and pipeline as territories. Obviously aws and pipeline have considerable overlap. My
impression was that we were parsing out pipeline as its own territory because that would contain all
the inter-surface edges, i.e. between aws and portal. That is something that should be hammered down
definitively how we proceed there."*

- **THE BUILD IS AUTHORIZED**: the one `GOVERNS` edge, `S3_BUCKET_POLICY 'opal-data-portal-v2'` ->
  `S3_BUCKET 'arn:aws:s3:::opal-data-portal-v2'` (token already confirmed 08-07 via CTO~C relay).
  Build seat: `3.0.0_SA_CVO` (their layer, their cut list; a one-edge act per their own record).
- **THE CAVEAT IS A DEFINITIONAL WORK ITEM, not a hold on the edge**: the aws-vs-pipeline territory
  logic must be **hammered down definitively**. His stated impression of the design intent, on the
  record so it can be tested rather than drifted from: **pipeline was parsed out as its own territory
  BECAUSE it would contain the inter-surface edges (aws <-> portal).** Whether the live layer
  assignment actually implements that intent is a measurable question; CRO is measuring it and
  reporting, with the definitional ruling routed back for ratification.

## CARD 3 -- C3.ii: FOLDED INTO ITEM 0

VERBATIM: *"Yes fold it in."*

C3.ii (the declared-plane x applied-plane join + the PRD-derived vertical discovery @951c8834f4)
becomes a **scheduled milestone inside Item 0's landing plan**, sequenced after the C2/C3.i instance
layer lands. Its breadth is thereby set by the plan rather than needing a separate scope ruling.
This discharges the "C3.ii scope open at Andrew" item carried in CVO's 08-07 handoff (their sec6.2)
and in my discovery record.

---

## CARD 2 ADDENDUM (2026-08-10 ~22:3xZ, Andrew-direct at the CVO terminal, relayed @225906Z) --
## THE RATIFY-AS-IMPLEMENTED PACKAGE IS WITHDRAWN; THE QUESTION RESHAPES TO HIS FORK

VERBATIM (via CVO relay): *"In my opinion, there should be no hand drawn anything with pipeline. I
don't even really believe in there being a pipeline territory here because really its just AWS
which is already a category."*

**CORRECTION OF MY OWN RECOMMENDATION, owned:** my package recommended ratifying
territory-as-node-kind WITH pipeline as the code-artifact territory, grounded on the implemented
twice-gated design. **v1.8's own substrate_side changelog already carried his 2026-08-06 leaning
("pipeline is aws material, not a peer") with the separate enum retained on MIGRATION COST, not
design agreement -- and I did not read that changelog entry before drafting the rec.** A
ratify-the-implemented package reaching him against his recorded leaning would have been the
stale-relay class; CVO's surface caught it before it shipped.

**RESHAPED STATE:**
- The ratify ask is WITHDRAWN. The real fork -- (A) merge pipeline into aws per his belief, with
  the measured migration cost; (B) retain as-implemented on cost grounds, explicitly not design --
  goes to Andrew via CVO's consequence analysis (in flight at their seat). The ruling is his.
- **"No hand drawn anything with pipeline" binds REGARDLESS of the territory outcome**: the
  pipeline tree walk becomes a PREDICATE over data/*/scripts/gold, never a hand-accreted call list
  (CVO's e2e finding: the substrate frozen at July-1 behind per-tree builder calls; cot has no
  builder at all).
- **L-2 (the authorized GOVERNS edge) IS UNAFFECTED BY EITHER OUTCOME** -- its endpoints
  (S3_BUCKET_POLICY -> S3_BUCKET) are aws-side nodes under both readings; the build stays
  authorized and queued. Stated so the edge is not re-held on a fork that does not touch it.
- The substrate-keyed definitional one-liner (the F1 re-key) survives either outcome -- it
  classifies NODES by kind and names no specific member set.

## CARD 2 RESOLUTION (2026-08-10 ~23:0xZ, Andrew-direct at the CVO terminal, VERBATIM: "Yeah of the
## options you provided, (b) is the clear solution." Record @09355b6d93)

**THE PIPELINE TERRITORY DISSOLVES INTO AWS via RECOMPILE FROM THE CLOUD**: pipelines modeled as
what AWS itself sees (deployed S3 code objects, EC2 runners, schedules) in the same deterministic
pass + freshness discipline as the rest of the aws substrate; the repo-AST code graph survives as
ENRICHMENT on those aws nodes, derived by PREDICATE over data/*/scripts/gold ("no hand drawn
anything" binds this leg). The frozen-feed class dies structurally, not by relabel.

**My carries, final:** the v1.9 naming act assembles at CVO with the MERGED form (enum change +
BACKEND collapse + status_vocabulary key + the reworded one-liner, v3 text sent to CVO). L-2 stays
authorized-and-queued, untouched. Implementation design = CTO lane; recompile verification = CVO.
The withdrawal-then-reshape cycle closed in under 40 minutes from his first statement to his
ruling -- the surface-not-adjudicate chain working at speed.
