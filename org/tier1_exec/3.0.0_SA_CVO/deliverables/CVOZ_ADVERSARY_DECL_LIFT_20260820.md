# validation_context_declaration -- comp-adversary v1
family: L0a boundary_report SIBLING (declaration + conformance + pins + denominators)
read-vintage: HEAD @2790d31d2d at 2026-08-20T12:31:26Z  [pin kind: read-vintage]
artifact: workflows/atom_decomposition/lift_catalog_v02.py
artifact-vintage: 8ba21b0ace (2026-08-19T16:27:51)

## AUTHOR PROFILE (what the author's evidence context WAS)
pins found: 1 commits, 1 repo paths, 0 file:line cites, 0 tool mentions

## COMPLEMENT (what the validator should know the author may NOT have seen)

### source 1: cited-commit verification (1 attempted / 1 verified / 0 UNVERIFIABLE)
  - all cited commits resolve at read-vintage

### source 2: cited-path vintage (1 attempted / 1 stable / 0 flagged)

### source 3: uncited neighborhood (directory siblings of cited paths)
  total uncited siblings: 6 (showing 6 -- the CAP is declared, not silent)
  - workflows/atom_decomposition/README.md
  - workflows/atom_decomposition/battery_catalog_v02.py
  - workflows/atom_decomposition/compile_manifest.py
  - workflows/atom_decomposition/emit_catalog_v02.py
  - workflows/atom_decomposition/manifest.md
  - workflows/atom_decomposition/validate_catalog_v02.py

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
