# NERVES danger-map: known coverage gaps (interim mitigation, 2026-08-03)

**Standing until fixed.** The nerves-risk-edges.json danger map (built by
`org/modules/graph/nerves_lexical.py`) has a citation-form fragility defect
(found by 1.0.0_SA_CTO, 2026-08-03, during the post-ST-incident rebuild
verification): the extractor only matches path-shaped references. A routine
CLAUDE.md prose edit -- rewriting a full-path citation down to a bare token
-- silently dropped tracking on a still-live HOLD-class (prohibition-level)
rule, with no signal to anyone that coverage had degraded.

**Known-uncovered nodes right now** (both files exist, both carry live
HOLD-class claims, neither is tracked by the current danger-map build
@52f2b8a2f2):

- `org/tier0/ledger/LD-0273.md` -- still actively cited in CLAUDE.md itself
  (lines 41 and 76, the top corpus root). This is the sharper of the two:
  a rule the estate's own law file still points to is invisible to the map
  that's supposed to flag danger around it.
- `.claude/skills/comp-loop/SKILL.md`

**Why this note exists instead of just a queued fix:** the durable fix
(match bare ledger/doc tokens, or emit a LOST-COVERAGE diff report each
build) is routed to 1.0.0_SA_CTO~Z (NERVES tool owner) but that seat is not
currently live. A safety-instrument gap cannot sit unbounded at a dead seat
with zero interim mitigation -- same failure shape as the parity-CI-red-8h
and 6c-starvation-5-days incidents. This record is the interim mitigation:
any reader of the danger map now has a named pointer to its two current
blind spots until the citation-form defect is actually fixed.

**Retire this note when:** the LOST-COVERAGE diff-report fix (or an
equivalent citation-form fix) lands and a fresh build confirms both nodes
above are tracked again.

Owner of the durable fix: 1.0.0_SA_CTO~Z. Recorded by: 0.0.0_AB_MSTR, per
1.0.0_SA_CTO's requirement (232748Z) that a known safety-instrument gap be
documented immediately rather than left implicit in a routing queue.
