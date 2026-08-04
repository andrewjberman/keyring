# MISSIONS -> KIMI-OFFTAKE TRANSFORMATION SPEC (Andrew-ratified 2026-08-04 ~2155Z)

**Author:** 3.0.0_SA_CVO (design, with Andrew in-session; rounds 7-8 of the
ANDREW_DIRECT_20260804_1945Z record carry the verbatims). **Executor:** 0.0.0_AB_MSTR (the
tree's LD-0341 owner). **Ratified:** Andrew, "I like it, proceed."

## Verdict that motivates it (measured, 2026-08-04)

The missions apparatus was built in one day (07-28) and its maintenance mechanism is DEAD
SILENTLY: the post-commit hook exists, is executable, references missions -- and the generated
org/missions/MISSIONS.md was last regenerated 07-29 04:26, ~1,900 commits ago; zero commits have
touched the tree since. A generated artifact that LOOKS machine-maintained carries false
authority. Andrew's architectural ruling: the missions concept is better realized as movements
between C4 / C3.ii / C3.i than as a second, hand-drawn semantic schema.

## The transformation, layer by layer

1. **IDENTITY**: the 3 groups / 10 sub-groups re-anchor to C4 segments / C3.ii verticals via a
   ~10-row mapping table (MSTR authors it; CVO verifies each row against the canon; ambiguous
   rows are adjudication events per the ladder's own reconciliation rule). EXTERNAL's empty
   forward containers map to DECLARED-BUT-CHAINLESS verticals -- the canonical form of the same
   idea. Old sub-group ids tombstone in the mapping table (never vanish).
2. **ACTIVITY**: comp-missions glob attribution RETIRES; activity blocks succeed to
   comp-cochange `grain` rollups at C4/C3.ii (Kimi attribution + the ported DECLARED-trailer
   precedence). SEQUENCING GATE: this spec executes only after 0.2.0_DS lands grain mode --
   the successor exists before the predecessor dies.
3. **STANCE** (the human-judgment content -- DECIDED/BUILT/SERVING, FRONTIER, BLOCKED-ON):
   succeeds to the State half of the OPAL_KIMIPIPELINE State/Friction design (lifecycle_value
   7-enum; Kimi PROPOSES, Andrew RATIFIES, CVO LANDS via the daily loop). Existing state.yaml
   stance content migrates as the seed values, marked pre-mechanism vintage. Judgment fields
   the enum cannot carry (FRONTIER prose, BLOCKED-ON specifics) remain human-written,
   anchored to vertical ids.
4. **GOALS**: root_goal + the sovereign-approved goals survive VERBATIM, re-homed per
   segment/vertical (intent_from_above discipline -- they are its textbook case).
5. **SERVING**: org/missions/MISSIONS.md regenerates as a C4 -> C3.ii rollup view compiled from
   the ladder + adjudicated daily reports + grain activity, REFRESHED BY THE DAILY ESTATE-REPORT
   LOOP (report-as-persistence). The post-commit hook RETIRES -- the daily loop has an absence
   oracle (_EPOCH); a hook has none, and six silent days just proved what that costs.
6. **DOCUMENTED AS OFFTAKE, EXCLUSIVELY** (Andrew's word): the tree's README/header states it
   is a VIEW over the Kimi pipeline's C4/C3 layering; no independent taxonomy exists here.
7. **RETIREMENTS** (delete-together, MSTR executes): org/tier0/missions.yaml glob layer; the
   comp-missions attribution modes (the commits() parser ALREADY extracts to
   org/modules/graph/commit_stream.py per round 6 -- comp_missions.py gains a back-compat
   import in the cochange build); the post-commit compile hook; registry/HUD/doc citations in
   the same motion (retired_aliases declaration if the comp-missions NAME retires).

## Acceptance (CVO verifies on landing)

Mapping table rows exercised against canon; first regenerated MISSIONS.md diffed against the
ladder's own censuses (counts must reconcile with denominators printed); the daily-loop refresh
observed on a real report day (not the authoring run); stance seed migration spot-checked
against pre-transformation state.yaml content; retirements delete-together verified (zero
dangling citations, comp-manifest-check green).

-- 3.0.0_SA_CVO
