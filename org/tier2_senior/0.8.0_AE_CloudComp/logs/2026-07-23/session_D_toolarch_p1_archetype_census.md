# NFRA_TOOLARCH.P1 archetype census -- dogfood the C0-C3 ladder on the whole estate (~D lane)

**archetype:** TRACE
**secondary_archetypes:** DIAGNOSE, COORDINATE

Session 2026-07-23 ~18:30Z -> ~19:17Z. Serial `0.8.0_AE_CloudComp~D` (fresh ~D lane; distinct from the
base `0.8.0_AE_CloudComp` session running the comp_log_auto derivation queue). Event-driven; arms zero crons.

## What happened

Started online, ran /watcher (clean fresh arm, task b5wzpaknl -- no orphan), completed org/XXX.md startup
(session serial written, audit-archive rc=0 not-due, owned-paths hook present, comp-context set). Inbox
fired a GO within the first turn: CTO~Z dispatched `NFRA_TOOLARCH.P1.archetype-census` (Andrew-spawned,
@bfad48b9b). ACK'd immediately, flipped to pending, executed end-to-end, delivered, ACCEPTED same session.

## The deliverable -- @f38a386a6 (accepted; CVO~Z verifying)

`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_TOOLARCH_P1_ARCHETYPE_CENSUS.md` +
reproducible `archetype_census.py`. A C0-C3 census of Opal itself against the ratified rule bank, vintage
pinned (comp-kuzu built 2026-07-23T14:52:37Z, Nessie HEAD current, 20398 nodes / 40796 edges, snapshots
3752421917688589142 / 2676052258466818414). Method = the INTENT_DENOMINATOR_SYNCHRONIZATION process:
INTENT from the rule bank (above the graph), DENOMINATOR from the live graph (run-time), GAP printed per
rung x plane.

Findings (CTO~Z: "the program's most important finding so far"):
- **C1 reproduces CVO~Z tick-29 BYTE-FOR-BYTE** via an INDEPENDENT derivation (my script parses the YAML
  mapping surfaces programmatically vs their hand-count of 3 surfaces). Direction-1 unmapped = 11 types /
  3912 edges (9.6%); Direction-2 zero-live = 9. Two independent derivations agreeing = boundary DERIVED.
- **THE HEADLINE: the frontend is the estate's biggest plane (54.8% mass, ~83% with M365) and its
  least-described** -- RENDERS 2447 + PROP_PASSES 1382 = 97.9% of unmapped edge mass (no relation verb for
  frontend data-flow), AND 0/7 frontend + 0/1 M365 canonical C2 families materialized. Under-covered at
  BOTH C1 and C2. CTO~Z: the measured root of an MSBEFF coverage-failure class.
- **C2:** 13/21 canonical families materialized (all A+B, landed since the 07-18 catalog). **C3:** 11/19
  motifs systematized -- the two heaviest canonical motifs (AGrant 1553, BDataflow 956) sit in NO system.
- **C0:** 10/14 roles by the fixed adapter (18535 nodes, CHECK sum == 20398). The 4 "zero" roles
  (Source/Producer/Router/Custodian) are un-static-bindable, grounded not null (Router = 82 ROUTES_TO from
  API_ROUTE but Gateway-priority-dominated -> possibly unreachable; Custodian = 15 MS_USER; Source/Producer
  = 447 producing sources). A methodology boundary.
- **R-0 (whole-plane boundary the edge-census can't see):** the records/governance plane (TOs/ledgers/
  memory/commits) is entirely absent from the graph except 23 self-materialized ontology nodes. Banked by
  CTO~Z for TOOLBHVR closeout-trigger work.

Ranked archetype table (freq x plane-spread x systematized) -> ~13 archetypes, tool-demand in ~6. P2
pattern inventory named as the sequenced follow-on (blocked on ~C's ONTOLOGY2 rails; not attempted).

## Coordination

- ACK -> execute -> DELIVERED-with-evidence -> ACCEPTED, full RAVC loop closed with CTO~Z same session.
- Handed the reproducible artifact to CVO~Z for family-charter verify (called out the C0 Router-unreachable
  reading + R-0-as-boundary-not-defect as the two judgment calls I want checked).
- Sent ~C the ONE shared uncovered set (5 boundaries) for its ONTOLOGY2 rail authoring; CTO~Z has routed
  the frontend-gap to ~C as its P1 design fork (per edge type: binds_up existing relation = additive/~C, or
  new vocab = ratified/CTO~Z). I hold the single reference and reshape to ~C's grain on request.

## Gotchas caught

- **Nested-bash -> WSL-stub (CLAUDE.md git_bash_resolver hazard):** my census script's `subprocess.run(["bash",...])`
  from a python spawned under bash hit the System32 WSL stub ("no installed distributions"), silently
  returning empty -> zeroed the whole census on first run. Fixed by importing `.tools/git_bash_resolver.git_bash()`.
  Exactly the class the rule exists for; caught on the first run because the output was visibly all-zeros.
- **owned-paths ANY_CTO lock:** docs/architecture/ is CTO-lane-locked; my commit was blocked. Moved the doc
  to my deliverables/ (the TO's stated alternative) rather than override -- CTO~Z confirmed the right call.
- **commit-gate ruff:** the terse analysis script tripped 28 style errors; ruff format + --fix + one noqa
  (intentional post-sys.path import) -> clean, and I re-ran the script to confirm figures unchanged before commit.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-kuzu | node/edge distributions, C2Motif/C3System nodes+props+membership, 4 edge-derived role groundings, --schema | PASS | vintage pinned from provenance header (built 14:52:37Z, HEAD current); the census substrate |
| comp-to | set session TO_ID = NFRA_TOOLARCH.P1.archetype-census | PASS | race-free per-session |
| comp-glob | locate rule bank + motif catalog (2 hits each; disambiguated canonical vs deliverable copy) | PASS | on-rails, .gitignore-aware |
| safe-commit / commit-gate | 2 commits (deliverable @f38a386a6, TO-flip @82ebf89ef); -F bodies | PASS | surface-check clean, risk-reflex CLEAN (3 files vs 1484 danger nodes), owned-paths block honored + rerouted |
| ruff | format + --fix + check on the census script | PASS | 28 -> 0; noqa on intentional E402 |

**What worked:** the intent-denominator method as a census discipline -- parsing the rule bank
programmatically gave an independent second surface that reproduced tick-29 exactly, which is the phase-2
cross-check. **What failed then was caught:** the nested-bash WSL-stub zeroed the first run (caught by
all-zero output + the CLAUDE.md rule); the ruff gate blocked the terse script (fixed, re-verified). **Gap
found:** none in the tools -- the census itself IS the gap-finding instrument, and the frontend/records
coverage boundaries are its output.

## Blockers

None. TO complete + accepted. Event-driven standing by for the next TOOLARCH leg or a ~C coordination reply.
