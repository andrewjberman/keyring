# comp-learns BACKLOG -- the gap->build bridge (NFRA_COMPCLOSE, 2026-07-14)

THE MISSING HALF OF THE LEARNING LOOP, made durable. Detection worked (comp-learns-status ranked
gaps for weeks); the build side never closed -- comp-trigger was gap-logged 2026-06-30 and
re-derived from scratch on 07-13 because a ranked gap that lives only in a report is re-findable
only the expensive way. This file is the tracked, deduped, append-only record between the two:

  FILE   `comp-learns-score --file-candidates` appends NEW top candidates here (dedup by key;
         an already-filed entry is NEVER re-written or silently re-ranked -- it is a record).
  READ   COO /drive reads the OPEN head each cycle; CTO ratifies BUILD/DECLINE (advisory-only
         discipline preserved -- the scorer never auto-mutates anything).
  CLOSE  a human flips `resolution: OPEN` to `BUILT <tool/commit>` or `DECLINED <why>` -- with
         the citation. An entry closed without a citation is drift, not a closure.

Value scores are outcome-anchored (escapes-prevented / drift-caught / cost-per-outcome), never
usage counts (the Goodhart gate; `comp-learns-score --goodhart-audit` proves it on demand).

## [OPEN] routing-friction -- routing: pre ship field  (filed 2026-07-14, value 130.0)
<!-- key: routing-friction|routing: pre ship field -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 130, "cold_start_routes": 130, "total_routes": 137}
- top demand terms: 'Pre-ship field-threading audit of a portal adapter function' x137
- resolution: OPEN   <- flip to `BUILT <tool + commit>` or `DECLINED <why>` (human edit, citation required)

## [OPEN] routing-friction -- routing: marker firm constant  (filed 2026-07-14, value 128.0)
<!-- key: routing-friction|routing: marker firm constant -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 128, "cold_start_routes": 128, "total_routes": 135}
- top demand terms: 'Marker/firm constant drift (FIRM_ID, thresholds) vs the canonical config' x135
- resolution: OPEN   <- flip to `BUILT <tool + commit>` or `DECLINED <why>` (human edit, citation required)

## [OPEN] routing-friction -- routing: compiler task order  (filed 2026-07-14, value 123.0)
<!-- key: routing-friction|routing: compiler task order -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 123, "cold_start_routes": 123, "total_routes": 130}
- top demand terms: "Compiler/task-order coverage report (what's covered vs gaps)" x130
- resolution: OPEN   <- flip to `BUILT <tool + commit>` or `DECLINED <why>` (human edit, citation required)

## [OPEN] routing-friction -- routing: list inspect cloud  (filed 2026-07-14, value 123.0)
<!-- key: routing-friction|routing: list inspect cloud -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 123, "cold_start_routes": 123, "total_routes": 130}
- top demand terms: 'List/inspect cloud resources of a type (all Lambdas, all S3 buckets, all roles)' x130
- resolution: OPEN   <- flip to `BUILT <tool + commit>` or `DECLINED <why>` (human edit, citation required)

## [OPEN] routing-friction -- routing: canonical pipeline ready  (filed 2026-07-14, value 69.0)
<!-- key: routing-friction|routing: canonical pipeline ready -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 69, "cold_start_routes": 131, "total_routes": 138}
- top demand terms: 'Is a canonical pipeline ready to STAND IN for the BD-served surfaces (a never-widen cutover)? The daily, tolerance-aware, dual-gated DATA/served parity proof, firm-by-firm -- the multi-day CLEAN streak IS the cutover gate' x137, 'is the canonical pipeline ready to stand in for served' x1
- resolution: OPEN   <- flip to `BUILT <tool + commit>` or `DECLINED <why>` (human edit, citation required)

## [OPEN] routing-friction -- routing: gold script chain  (filed 2026-07-14, value 67.0)
<!-- key: routing-friction|routing: gold script chain -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 67, "cold_start_routes": 128, "total_routes": 135}
- top demand terms: 'Gold script I/O, chain membership, deployed-match, overlap' x135
- resolution: OPEN   <- flip to `BUILT <tool + commit>` or `DECLINED <why>` (human edit, citation required)

## [OPEN] routing-friction -- routing: registry narrative project  (filed 2026-07-14, value 66.0)
<!-- key: routing-friction|routing: registry narrative project -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 66, "cold_start_routes": 127, "total_routes": 134}
- top demand terms: 'REGISTRY narrative vs project-JSON drift (phase/commit-citation/status mismatch)' x134
- resolution: OPEN   <- flip to `BUILT <tool + commit>` or `DECLINED <why>` (human edit, citation required)

## [OPEN] routing-friction -- routing: tooltip migration audit  (filed 2026-07-14, value 66.0)
<!-- key: routing-friction|routing: tooltip migration audit -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 66, "cold_start_routes": 127, "total_routes": 134}
- top demand terms: 'Tooltip migration audit (portal tooltip coverage)' x134
- resolution: OPEN   <- flip to `BUILT <tool + commit>` or `DECLINED <why>` (human edit, citation required)

## [OPEN] routing-friction -- routing: components consume typescript  (filed 2026-07-14, value 66.0)
<!-- key: routing-friction|routing: components consume typescript -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 66, "cold_start_routes": 128, "total_routes": 135}
- top demand terms: 'Which components consume this TypeScript type (before editing an interface)' x134, 'which components consume this typescript type' x1
- resolution: OPEN   <- flip to `BUILT <tool + commit>` or `DECLINED <why>` (human edit, citation required)

## [OPEN] routing-friction -- routing: rebuild trace graph  (filed 2026-07-14, value 63.0)
<!-- key: routing-friction|routing: rebuild trace graph -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 63, "cold_start_routes": 131, "total_routes": 138}
- top demand terms: 'Rebuild the trace graph cache (WRITE-PATH — after adding files)' x137, 'rebuild the trace graph cache' x1
- resolution: OPEN   <- flip to `BUILT <tool + commit>` or `DECLINED <why>` (human edit, citation required)

## [BUILT] coverage-gap -- comp-trigger (EventBridge/Scheduler dispatch forensics)  (filed 2026-07-14, retro)
<!-- key: coverage-gap|comp-trigger-eventbridge-forensics -->
- disposition: BUILD-NEW -- executed same-pass (NFRA_COMPCLOSE Phase C)
- value evidence: gap-logged 2026-06-30 in org/compiler-tools-log.md ("no comp-tool for
  CloudTrail/EventBridge/SSM trigger-dispatch forensics -> candidate comp-trigger"); NEVER FILED
  ANYWHERE ACTIONABLE, so 2.0.0_SA_COO~Z re-derived the same forensics from scratch through raw
  aws calls on 2026-07-13 (a full night -- the measured cost of a ranked gap with no consumer).
  Rail-mining corroboration: EventBridge/trigger/schedule questions in the frozen-cohort
  sub-floor class.
- resolution: BUILT -- .tools/comp-trigger -> org/modules/graph/comp_trigger.py. Self-test 10/10
  (incl. structural no-write proof + its positive control); PAIRED spot-check discriminated on
  first contact (FALSE twin: held inf dispatch rule inf-canonical-prices-daily -> DISABLED with
  the hold-note, matched via target-ARN; TRUE: access-anomaly-scanner-schedule -> ENABLED,
  FIRED 72x = hourly x 3d, self-validating). First-contact FINDING: access-anomaly-scanner-schedule
  is declared in NO .tf (unmanaged trigger -> routed to the drift/debt lane). Registered
  (coverage-map + tools_index + entries + curated route) in the SAME pass -- a tool nobody can
  find is indistinguishable from a tool never built. Commit: NFRA_COMPCLOSE Phase C (this file's
  own commit -- the hash IS the citation).

## [OPEN] coverage-gap -- trace-graph blindness to .tools/ + org/modules (COMPRAIL F-5)  (filed 2026-07-14)
<!-- key: coverage-gap|trace-graph-tools-modules-blindness -->
- disposition: BUILD -- extend the trace-graph builder with a compiler-tools node domain
  (.tools/* shims + org/modules/graph/*.py engines, import edges), so comp-blast/comp-trace/
  comp-xref can see the compiler layer itself.
- value evidence: `comp-blast comp-which` -> NOT-FOUND while 7 real consumers existed; a harness
  author DELETED a fail-closed commit gate's public symbol on that "clear" and blocked every
  agent's commits (NFRA_COMPASSURANCE TO-1 brief, own-errors #1-2). comp-blast's measured 34%
  NOT-FOUND rate is partly this universe hole. Interim mitigation SHIPPED (NFRA_COMPCLOSE
  Phase D): NOT-FOUND now prints the 1,402-node universe census + the F-5 blindness statement +
  last-segment near-matches + the right-instrument pointers -- the false-clear class is closed,
  the coverage hole is not.
- deliberately NOT landed same-pass: node_type taxonomy is the gate-checked 52-type SSOT
  (NFRA_GRAPHS; comp-coverage-check node_type_grain bridge) -- adding a node domain is a
  CTO-arch-gate change with consumers, not a side-effect edit.
- resolution: OPEN   <- flip to `BUILT <tool + commit>` or `DECLINED <why>` (human edit, citation required)
