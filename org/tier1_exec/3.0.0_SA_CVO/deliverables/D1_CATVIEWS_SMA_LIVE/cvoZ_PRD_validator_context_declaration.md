# validation_context_declaration -- comp-adversary v1
family: L0a boundary_report SIBLING (declaration + conformance + pins + denominators)
read-vintage: HEAD @f0ac3a5db9 at 2026-08-28T21:30:55Z  [pin kind: read-vintage]
artifact: docs/architecture/D1_CATVIEWS_SMA_LIVE_PRD.md
artifact-vintage: f0ac3a5db9 (2026-08-28T17:29:33)

## AUTHOR PROFILE (what the author's evidence context WAS)
pins found: 0 commits, 0 repo paths, 1 file:line cites, 0 tool mentions
!! ZERO MACHINE-EXTRACTABLE PINS: this artifact's evidence is prose-cited or
!! externally homed -- the validator must derive the evidence set BY READING.
!! Every complement source below ran against an EMPTY profile and says so in
!! its own denominator. A zero here is a signal, never a clean pass.

## COMPLEMENT (what the validator should know the author may NOT have seen)

### source 1: cited-commit verification (0 attempted / 0 verified / 0 UNVERIFIABLE)

### source 2: cited-path vintage (0 attempted / 0 stable / 0 flagged)

### source 3: uncited neighborhood (directory siblings of cited paths)
  total uncited siblings: 0 (showing 0 -- the CAP is declared, not silent)

### source 4: comp-state drift (raw excerpt -- validator reads full output)
  {
   "scanned_commits": 400,
   "records": 2722,
   "drift": [
    {
     "kind": "TO",
     "id": "NFRA_COMPUNIFY.V1.cvo-completeness-nonredundancy-verify",
     "code": "NFRA_COMPUNIFY",
     "status": "complete -- SPRING-CLEAN 2026-08-25: project NFRA_COMPUNIFY is complete; this TO was last touched 2026-06-30, predating ",
     "path": "org/projects/NFRA_COMPUNIFY/task_orders/NFRA_COMPUNIFY.V1.cvo-completeness-nonredundancy-verify.md",
     "last": 1787682712,
     "verdict": "POST-CLOSE",

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
