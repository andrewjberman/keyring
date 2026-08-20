# validation_context_declaration -- comp-adversary v1
family: L0a boundary_report SIBLING (declaration + conformance + pins + denominators)
read-vintage: HEAD @2790d31d2d at 2026-08-20T12:31:39Z  [pin kind: read-vintage]
artifact: org/tier2_senior/0.5.0_AE_OpalETL/deliverables/laneZ_D6_TOF_W6_GUARDRAILS_REVIEW_20260819.md
artifact-vintage: de57e559c2 (2026-08-19T17:11:56)

## AUTHOR PROFILE (what the author's evidence context WAS)
pins found: 0 commits, 1 repo paths, 0 file:line cites, 3 tool mentions
tools cited: comp-find, comp-iam, comp-routes

## COMPLEMENT (what the validator should know the author may NOT have seen)

### source 1: cited-commit verification (0 attempted / 0 verified / 0 UNVERIFIABLE)

### source 2: cited-path vintage (1 attempted / 0 stable / 1 flagged)
  - org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-08-19/andrew_direct_1900Z_relay_findings_to_mstrz.md : MOVED-SINCE-AUTHORING (last change 2026-08-19T22:41:20 postdates the artifact)

### source 3: uncited neighborhood (directory siblings of cited paths)
  total uncited siblings: 1 (showing 1 -- the CAP is declared, not silent)
  - org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-08-19/daily_guardrail_1300Z_wdac_pull_failure_verified.md

### source 4: comp-state drift (raw excerpt -- validator reads full output)
  {
   "scanned_commits": 400,
   "records": 2534,
   "drift": [
    {
     "kind": "TO",
     "id": "NFRA_COMPLEARN.P0.tool-activity-catalog-seed-backfill",
     "code": "NFRA_COMPLEARN",
     "status": "staged -- dispatch on ~E spawn (MSTR ALLOCATION-REQUEST 222838Z) + grant landed",
     "path": "org/projects/NFRA_COMPLEARN/task_orders/NFRA_COMPLEARN.P0.tool-activity-catalog-seed-backfill.md",
     "last": 1782858874,
     "verdict": "BEHIND",

## DECLARED EXCLUSIONS (sources the validator was NOT shown -- v1 contract)
  - toolgraph SHARES_SUBSTRATE independence : v1: toolgraph consumption not wired -- the independence oracle rides v2 (0.8.0 build)
  - comp-axes unexamined-axes (snapshot rows) : v1: snapshot-row consumption not wired (never live-render, per the 71.5s constraint)
  - comp-blast/comp-trace neighborhood expansion : v1: graph expansion not wired -- neighborhood = directory siblings only
  - comp-pulse warnings / comp-cochange diversity : v1: not wired
  - comp-read digests (the packet stage) : v1: the packet lists POINTERS, not digests
  - T11 admissibility method : named slot, ships when CRO's method ratifies

## DENOMINATORS
complement sources: 4 run / 0 deferred-with-reason / 6 declared-excluded
pin kinds: all pins in this declaration are READ-VINTAGE (declaration-vintage pins
appear only where the artifact itself recorded one -- trace-to-authority claims are
UNANSWERABLE from this declaration alone and are not implied).
