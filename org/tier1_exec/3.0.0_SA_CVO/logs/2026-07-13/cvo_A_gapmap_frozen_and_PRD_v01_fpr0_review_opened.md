# CVO~A -- OPAL_ASSETS gap map FROZEN for PRD synthesis; PRD v0.1 landed (79231da3e); FP-R0 schema review OPENED (2 findings grounded, verdict pending)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

**Window:** 2026-07-13T00:40Z (last log b5a944b17) -> 04:23Z. 0 commits this window (review in progress -- the verdict doc + commit are the next action). MCP: 2 significant exchanges.

## 1. Freeze-check answered (CTO~B 011443Z -> my FREEZE reply)

CTO~B asked whether G1-G6 is frozen for PRD synthesis. Answered **FREEZE**, with the three
discovery-driven refinements AS the frozen form (not amendments to fold later):
- **G2 as-refined:** proven pull + NEW CBUGL pipe-delimited converter + both-masters cohort wiring
  (the SmartX RPS converter does NOT generalize).
- **G4 explicitly G2-DEPENDENT via D1=SPLIT:** INTERIM = fold avgcap-only NOW with a disclosed
  `partial: 08242234-only` flag (never silently undercount); FULL = both-masters dedup when G2 lands.
- **G6 removed from the build map:** DONE -> frozen as the ACCEPTANCE HARNESS.
Plus two G5 design constraints carried into the PRD: ONE as_of semantics (per-cohort OWN-field,
never cross-partner min) and the Cottonwood leg strictly one-way cot->bucket (Rule 13). Clarified
that my FP-R0 verdict is a REVIEW step on the draft, not a moving input; the only genuinely-open
map item is G3(b) 2021 depth (Andrew's vendor-channel call).

## 2. PRD v0.1 LANDED -- FP-R0 schema review OPENED

- **79231da3e** (CTO~B, pushed CLOUD): `docs/architecture/OPAL_ASSETS_PRD.md` + registry
  `org/projects/OPAL_ASSETS.json`. Commit verified (git show: 2 files, 130 insertions, author
  1.0.0_SA_CTO~B). Synthesis honors the frozen form: all 3 refinements present (sec 4), both G5
  constraints present (sec 3d/3e), G6 = acceptance harness (sec 4 + AC spine sec 5).
- **Review scope (CTO~B's ask 024240Z):** FP-R0 claim-classing + evidence discipline; focus = row
  shape {cohort, source_master(s), value, as_of, state}, ONE-as_of semantics, both-masters-dedup
  grain, AC framework AC1-AC6.
- **Findings grounded so far (verdict doc pending):**
  1. **State-enum gap [OBSERVED]:** PRD row `state in {fresh, rolled_forward, missing}` cannot
     represent the checker's fourth live state `incomplete` (one expected master present, one
     absent -- cohort-8's CURRENT condition). Source: mdpf-freshness-checker
     `lambda_function.py:305` (`state = "incomplete"`) @ working-tree (post-46d8be80d). The bucket
     schema must mirror or supersede the checker vocabulary; recommendation drafting: carry
     `source_masters` (expected) + `masters_present` (actual) so incompleteness is derivable and
     the G4 `partial` flag unifies into the row schema.
  2. **G1 mechanism grounding EXISTS, citation absent from PRD [OBSERVED]:** the "silver alternates
     46K/1.2M rows = stub/partial landings" line traces to the 07-02 stub-reject deploy ledger
     (`org/critical_paths/change_management/20260702T2042Z_bd-silver-alloc-stub-reject_deploy_completion.md:19`
     -- 45KB vs 1.2MB grounded live) + my blueprint b2a17a7e3. Fix = attach the pointer so COO's G1
     TO inherits Rule-22 grounding; no re-investigation needed.
  3. Drafting (not yet grounded-complete): AC3's double-count falsifier has NO detector (the alarm
     spine measures FRESHNESS; a double-counted cohort reads green) -> needs a dedup reconciliation
     instrument at G2 acceptance; dedup-by-account grain under-specified (duplicate definition,
     master precedence, account- vs position-level) -> recommend the both-masters account-overlap
     census as an explicit G2 investigate-and-report item; AC5 needs the A4-style mutant carried to
     the bucket emitter (emit-time as_of stamping is the falsifier no live read catches -- same
     date-axis class as CVO~B's round-8 finding).
- **Andrew direct query answered in-session** ("what are you reviewing exactly") -- explained the
  review object + the two review dimensions; awaiting no redirect, proceeding.

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| git show/log (79231da3e) | commit verification | PASS -- author/paths/insertions match the claim |
| grep pinpoint x2 (rail-checked markers) | checker enum literals + 46K/1.2M provenance | PASS -- both findings grounded to file:line |

- What worked: grounding review findings BEFORE authoring the verdict -- both flags carry file:line
  citations instead of recollection.
- What failed: nothing this window.
- Gap found: none new (the state-enum gap is a finding IN the reviewed artifact, not a tool gap).

## Blockers

None. The verdict authoring is in-hand, not blocked.

## Current State (handoff)

- OPAL_ASSETS PRD v0.1 = `docs/architecture/OPAL_ASSETS_PRD.md` @ 79231da3e; registry
  `org/projects/OPAL_ASSETS.json`. COO decomposition waits on my FP-R0 verdict.
- My review: 2 findings grounded (state-enum gap @ lambda_function.py:305; G1 citation pointer @
  the 07-02 deploy ledger), 3 drafting (AC3 detector, dedup grain spec, AC5 emit-time mutant).
- Verdict doc destination: `org/tier1_exec/3.0.0_SA_CVO/deliverables/` (next commit), then
  send_message to 1.0.0_SA_CTO~B with the fold list.
- Inbox Monitor live (task b9jexby6b); nested lane inbox path = `org/mcp/inbox/3.0.0_SA_CVO/~A/`.

## Next Steps

- **[me]** author + commit the FP-R0 verdict doc; message [1.0.0_SA_CTO~B] with the fold list
  (state-enum, G1 citation, AC3 detector, dedup grain, AC5 mutant).
- **[1.0.0_SA_CTO~B]** fold accepted flags into PRD v0.2 before/as COO decomposes.
- **[2.0.0_SA_COO]** TO decomposition after the fold.
