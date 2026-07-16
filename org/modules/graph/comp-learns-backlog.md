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
- resolution: OPEN -- **BUILD RATIFIED, APPROVED-PENDING-BUILDER** (CTO, msg 20260714T032105Z, the bridge's
  first ratified read-through: sec-21 coverage-gap lane, sanctioned; route to 0.8.0-class capacity when it
  exists). Flips to `BUILT <tool + commit>` at build time.

## [OPEN] routing-friction -- routing: marker firm constant  (filed 2026-07-14, value 128.0)
<!-- key: routing-friction|routing: marker firm constant -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 128, "cold_start_routes": 128, "total_routes": 135}
- top demand terms: 'Marker/firm constant drift (FIRM_ID, thresholds) vs the canonical config' x135
- resolution: OPEN -- **BUILD RATIFIED, APPROVED-PENDING-BUILDER** (CTO, msg 20260714T032105Z; sec-21
  coverage-gap lane, sanctioned; route to 0.8.0-class capacity when it exists). Flips to
  `BUILT <tool + commit>` at build time.

## [DECLINED] routing-friction -- routing: compiler task order  (filed 2026-07-14, value 123.0)
<!-- key: routing-friction|routing: compiler task order -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 123, "cold_start_routes": 123, "total_routes": 130}
- top demand terms: "Compiler/task-order coverage report (what's covered vs gaps)" x130
- resolution: DECLINED pending-a-concrete-instance (CTO, msg 20260714T032105Z: "its description reads as
  process-shaped, and the no-new-process constraint gets the benefit of the doubt tonight." Re-openable by
  a new concrete instance with a named consumer -- refile as a fresh entry, do not un-decline this one.)

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

## [BUILT comp-state @ c7aca9200] routing-friction -- routing: registry narrative project  (filed 2026-07-14, value 66.0)
<!-- key: routing-friction|routing: registry narrative project -->
- disposition: routing-refinement -- the LIVE router repeatedly hedged this intent -- a curated comp-which rule / keyword refinement (or the learned affinity term) would sharpen it to a confident decision (LD-0226 routing-mutation surface)
- value evidence: {"low_confidence_routes": 66, "cold_start_routes": 127, "total_routes": 134}
- top demand terms: 'REGISTRY narrative vs project-JSON drift (phase/commit-citation/status mismatch)' x134
- resolution: BUILT `comp-state` @ c7aca9200 (+ crash-fix 686eee21c; skill .claude/skills/comp-state) -- closed 2026-07-14 by 1.0.0_SA_CTO.
  The demanded intent (REGISTRY-row / project-JSON / TO-status / PRD-status drift vs COMMIT EVIDENCE) is
  exactly comp-state's verdict surface; exercised same-night (self-test 3/3, 3 real drifts found + fixed
  a7ea07516). RESIDUAL, deliberately NOT a tool: cross-record NARRATIVE coherence (row prose vs JSON prose,
  same facts told two ways) stays a /spot-check-class judgment read -- comp-state flags both records when
  either lags the estate, which bounds how far the two texts can diverge; a prose-vs-prose comparator would
  be a second BM25 instrument measuring the first. Route the intent to comp-state in comp-which vocab.

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

## [OPEN] tooling-gap -- backlog citation-less-closure DETECTOR  (filed 2026-07-14, from CVO~Z /verify verdict 3d816c650)
<!-- key: tooling-gap|backlog-citationless-closure-detector -->
- disposition: BUILD-CHEAP -- a comp-learns-status (or comp-manifest-check) flag that scans THIS
  file for entries whose `resolution:` was flipped off OPEN without a citation (no commit hash /
  tool path / reason in the resolution line) and prints them LOUD.
- value evidence: the closure rule ("an entry closed without a citation is drift, not a closure")
  is PROSE-ONLY -- nothing detects a violation. The verifier who found this had just re-taken six
  claims precisely because prose rules without detectors are how records drift (CVO~Z, verdict
  cvoz_verify_nfra_compclose_verdict.md).
- resolution: OPEN   <- flip to `BUILT <tool + commit>` or `DECLINED <why>` (human edit, citation required)

## [OPEN] instrument-integrity -- comp-freshness ddb FALSE-EMPTY on populated tables (CF-1)  (filed 2026-07-14, CTO-routed)
<!-- key: instrument-integrity|comp-freshness-ddb-false-empty-cf1 -->
- disposition: DEFECT + config gap -- ddb mode's default PK-prefix probe fits neither opal-assets-daily-aua
  nor opal-news-articles key shapes; "WARN / No items found with PK prefix ''" is byte-indistinguishable
  from a genuinely empty table (verification law 5: not-knowing rendering as confidence; same family as
  the NEVER#1 flat-hours fallback made structural @ 50568a481).
- value evidence: 2/2 false-empty on populated tables (0.7.0 connector sweep,
  CONNECTOR_SWEEP_C_LANDED_BYTES_INTERIM_20260714.md FINDING CF-1; direct scans return items on both).
- DESIGN RULED (CTO 2026-07-14 ~18:5xZ): (1) a config-missing/key-shape-mismatch read MUST print a
  distinct CONFIG-MISS verdict class -- never a WARN that looks measured; the tool needs a channel for
  "I don't know". (2) per-table config entries carry the REAL PK pattern (+ freshness_basis where
  applicable) for both named tables, grounded on describe-table key schema, not guessed.
- resolution: OPEN -- **BUILD RATIFIED, APPROVED-PENDING-BUILDER** (CTO, routed from COO 185255Z; base-CTO
  is instruct-usage-never-build per the 07-14 scope directive -- route to ~Z-group/0.8.0-class capacity
  via MSTR when it exists). Flips to `BUILT <tool + commit>` at build time.

## [OPEN] coverage-gap -- the MONOLITH (opal-data-assets) has zero comp-tool coverage  (filed 2026-07-14, CTO)
<!-- key: coverage-gap|monolith-opal-data-assets-no-comp-tool -->
- disposition: coverage gap by the rail's own law -- every landing/backfill/freshness verify on the
  monolith tonight ran raw listings under audited rail-checked markers (org/mcp/comp-which-rail.log,
  2026-07-14 16:1xZ-18:4xZ, repeated single-intent overrides = build signal). comp-freshness has no
  opal-data-assets entries; pipescript/comp-aws do not model the {source}/{scope}/{layer} grammar,
  the sweep verdict manifests (meta/conversions/), or the trading-day frontier for the new channels.
- value evidence: >= 8 rail-checked raw listings in one session by one agent (CTO), across orion/eclipse/
  blackdiamond/schwab/smartx/etf channels; the monolith is now the estate's primary data plane.
- DESIGN NOTE (not binding): the cheapest first cut is comp-freshness family entries per channel with
  freshness_basis: trading-day-frontier + the manifest listing as the sweep-health oracle.
- resolution: OPEN -- registry-owner lane to scope; base-CTO files, does not build (07-14 scope directive).

## [OPEN] instrument-integrity -- comp-state REGROW touch-dating blind to in-row edits + record-keeping corpus noise  (filed 2026-07-14, CTO)
<!-- key: instrument-integrity|comp-state-regrow-s-dating-and-fold-noise -->
- disposition: TWO measured defects from the 07-14 convergence pass. (A) Row touch-dating uses
  `git log -S<code>` = occurrence-COUNT change detection: COO's fold 4f92bdf51 (20:49Z) directly
  edited REGISTRY:OPAL_ASSETS yet the record's last-touch still dated 08:53Z -- the scan then lists
  the fold itself as EVIDENCE for a BEHIND verdict on the very record the fold fixed. A row updated
  without changing its code's token count is INVISIBLE as a touch => rows read permanently BEHIND
  under active maintenance. Candidate fix: -G<regex> or row-line-range blame or row-content-hash
  dating. (B) Under high commit velocity, record-keeping commits (org(board)/log/record/deliverable
  prefixes) dominate the evidence corpus -- each fold re-flags every other record within minutes;
  convergence-to-CURRENT is unachievable while the fabric commits faster than folds land. Candidate
  fix: an --exclude-recordkeeping corpus filter (prefix-based) so evidence means ESTATE motion, not
  bookkeeping about it.
- value evidence: 07-14 21:0xZ convergence re-run: hot set verified CURRENT by direct read of the
  fold commits, yet instrument read BEHIND 14/1/2 across three projects; the false-BEHIND cost one
  full re-run + manual diff to diagnose.
- resolution: OPEN -- design ruled at filing; build routes to ~Z-group/0.8.0-class capacity via MSTR
  (base-CTO instruct-usage-never-build). Flips to `BUILT <tool + commit>` at build time.

## [OPEN] coverage-gap -- lambda deployed-artifact drift check (comp-pipescript-deployed for the lambda estate)  (filed 2026-07-14, CTO)
<!-- key: coverage-gap|lambda-artifact-drift-check -->
- disposition: MISSING CONTROL, measured live twice today. A stale S3 artifact is INVISIBLE to a TF
  diff (TF compares state to config, and the config points at the same key) -- so an env-leg apply
  can pre-clear while the code leg silently never shipped. C4 half-landed exactly this way (env
  applied 03:05Z; artifact LastModified 07-13T22:41 predates the flip commit; tonight's 22:00Z fire
  wrote legacy-only; 0.5.0 escalation 230221Z, forward-fix GO'd 230335Z). The vident deploy ran the
  countermeasure BY HAND x5 (live CodeSha256 == uploaded sha == source-map artifact_sha256).
- DESIGN RULED: a check that, per lambda-source-map entry, compares (a) live CodeSha256, (b) the S3
  artifact's content-sha256 metadata, (c) artifact_sha256 in the map, and optionally (d) a
  build-from-HEAD hash for the files[] set -- any pairwise mismatch = named drift verdict. Belongs
  beside comp-pipescript deployed (same question, lambda estate instead of EC2 gold). CI candidate:
  the source map already carries everything but the live read. AMENDMENT (0.5.0, 231613Z): the same
  build should ship ONE canonical formatter for lambda-source-map.json -- two different writers
  reformatted the whole file in one night (CTO json.dump indent=2; 0.5.0's edit churned it again),
  and whole-file churn destroys blame utility on the estate's deploy-truth record.
- value evidence: C4 half-landed 20+ hours undetected across two sessions + a ratified-then-falsified
  'APPLIED' claim (config-read-for-behavioral, 22a); found only when the scheduled fire exercised it.
- resolution: OPEN -- build routes to ~Z-group/0.8.0-class capacity via MSTR (base-CTO
  instruct-usage-never-build). Flips to `BUILT <tool + commit>` at build time.

## [OPEN] coverage-gap -- portal light-fg silver-canvas commit-time nudge (WARN-level, announce-then-enforce)  (filed 2026-07-15, CTO; routed from 0.5.0~A CC of Andrew-direct #6)
<!-- key: coverage-gap|portal-light-fg-silver-canvas-nudge -->
- disposition: MISSING CONTROL, Andrew-named recurring footgun (light text/buttons outside a dark
  panel on the SILVER canvas). Scope exactly as specced by 0.5.0~A: a commit-time WARN when a
  portal/src/pages/**.tsx adds light-fg classes (text-white*, text-*-100..300, bg-white/N) in a
  file with NO Panel-primitive import. WARN-level per announce-then-enforce -- the deterministic
  instrument stays the SCREENSHOT (portal/scripts/ui-smoke.mjs is the exercised-path primitive; a
  grep cannot see containment/contrast -- 0.5.0~A's own file part-evaded a naive lint via
  bg-black/30 inputs, the recorded evasion witness).
- LAW SOURCE (amended per Andrew-direct #7, 2026-07-15 ~16:1xZ): cite design/brand/COLOR_ARCHETYPES.md
  (the root design/ canonical repository, UIUX macro) as the color law, not portal/CLAUDE.md alone.
- extension point noted: comp-transform schema-check has no color/contrast dimension; ui-smoke.mjs
  is the primitive a COMP lane would build on.
- resolution: OPEN -- build routes to ~Z-group/0.8.0-class capacity via MSTR (base-CTO
  instruct-usage-never-build). Flips to `BUILT <tool + commit>` at build time.

## [OPEN] coverage-gap -- design/ tree missing from doc-globbing comp-tool scan roots  (filed 2026-07-15, CTO; routed from 0.5.0~A CC of Andrew-direct #7)
<!-- key: coverage-gap|design-tree-scan-roots -->
- disposition: NEW top-level tree design/ (Andrew-direct #7: THE canonical design repository,
  anti-sprawl law, ws 210f70a9a + portal 3df9231e). comp-grep/comp-glob are repo-scoped and cover it
  automatically; ANY comp tool with HARDCODED doc scan roots (surface maps, graph doc-derives,
  systems-context doc indexing) needs design/ added or it silently omits the canonical design law
  from every answer. Audit which registries hardcode roots, then add.
- resolution: OPEN -- rides the same ~Z/0.8.0 registry-touch wave; small.

## [OPEN] tool-defect -- comp-blast cp1252 crash on non-ASCII in corpus quotes  (filed 2026-07-15, CTO; found by 0.4.0_DS~A on the A1 sweep)
<!-- key: tool-defect|comp-blast-cp1252-print-crash -->
- disposition: comp-blast crashes under cp1252 console encoding when a corpus quote carries U+2192
  (and any non-ASCII); utf-8 retry works. Fix: cli.py _p() encode-safe (errors=replace or
  reconfigure stdout utf-8). Workaround in use: utf-8 env retry.
- resolution: OPEN -- small; rides the next comp-tool touch or the ~Z/0.8.0 wave.

## [OPEN] tool-defect -- comp-state REGROW convergence structurally unclosable (pickaxe blind to count-neutral row edits)  (filed 2026-07-15, COO; found on the OPAL macro sweep)
<!-- key: tool-defect|comp-state-regrow-pickaxe-count-neutral -->
- disposition: REGISTRY-row last-touch = git log -1 -S <code> -- REGISTRY.md, and -S fires only when
  the occurrence COUNT of <code> changes. A row rewrite that keeps the code's count unchanged (the
  NORMAL reconciliation edit) is invisible: the row stays BEHIND forever and protocol rule 7
  (re-run -> fixed records read CURRENT) cannot close for REGROW. Verified live: 6 rows fixed at
  beab2082e, all 6 re-read BEHIND; the 4 JSONs + 1 TO in the same commit read CURRENT.
  Fix candidates: -G"\| \x60?<code>\x60?" regex-diff instead of -S; or per-row content hash mapped to
  last commit touching REGISTRY.md that changed that row's line. Second cost item, same engine:
  load_records computes per-record git last-touch for ALL ~1,700 TOs BEFORE the --project filter
  (~5-8 min per invocation on this host); filter-first would make --project seconds.
- resolution: OPEN -- rides the next comp-state touch; sweep results remain valid (agent = precision
  layer; the gap is the convergence loop, not the recall).

## [OPEN] instrument-gap -- the .013 freshness gate is VACUOUS on the orion gold runner  (filed 2026-07-16, CTO)
<!-- key: instrument-gap|comp-freshness absent on orion-gold-runner PATH -->
- disposition: deploy-gap + dead-reference cleanup -- TWO cells, same family, found by run-2's readable log
  (AoR window forensics, GLDRNS_B1 ledger): (1) `comp-freshness` is NOT on the orion gold runner's PATH, so
  the dispatch's ADHC_COMPIL.013 gate prints "WARN: comp-freshness not found in PATH -- freshness gate
  skipped" and proceeds EVERY run -- a gate that cannot fire on the box it guards (verification law 4: a
  guard nothing invokes == no guard). (2) `check_freshness` in the same dispatch is dead code against the
  current estate: silver/aum_snapshot/ is an EMPTY prefix and gold/artifacts/header_metrics.json is a 404 --
  both inputs empty -> proceed-on-WARN every run (a gate whose reference artifacts no longer exist).
- value evidence: the gate's absence was DISCOVERED because its hypothesized firing fit a real +13s death;
  a vacuous gate is worse than no gate -- it reads as coverage in every census of the dispatch's protections.
- fix shape: stage comp-freshness (+ its trading-calendar lib dep) into the runner's code/ closure per
  Rule-12, OR delete the .013 call from the dispatch and route freshness to the container-side sweep --
  DECIDE, don't leave the WARN-skip. check_freshness: retire or re-point its reference artifacts.
- resolution: OPEN -- CTO-filed post-incident 2026-07-16 ~00:21Z; NOT touched mid-window (guard-state
  change rule). Route: DS~B refactor lane (the dispatch is theirs under B1) or the STNDRD deploy standard.

## [OPEN] instrument-gap -- comp-state REGROW row dating is blind to same-count edits  (filed 2026-07-16, CTO)
<!-- key: instrument-gap|comp-state regrow pickaxe same-count blind -->
- disposition: state_scan.py dates a REGISTRY row via `git log -S<code>` (pickaxe), which fires only when
  the OCCURRENCE COUNT of the code changes. A row-content rewrite that keeps the count identical (the
  2026-07-16 670452627 reconcile: window-OPEN text -> CLOSED-STAMPED text, code appears only in the row's
  first cell, untouched) is INVISIBLE -- the row then reads BEHIND forever against newer evidence even
  though it is current. Found by exercising protocol rule 7 (convergence) on the reconcile's own fix.
- value evidence: a reconcile that cannot converge trains agents to ignore convergence failures -- the
  check dies as a control.
- fix shape: date REGROW rows by the REGISTRY.md file's last commit intersected with a line-range blame
  for the row, or fall back to blame on the row's first cell; pickaxe stays as the fast path.
- resolution: OPEN -- CTO-filed 2026-07-16 ~12:15Z.

## [OPEN] tool-defect -- deploy_ledger _md_status regex misses colon-inside-bold Status variants (Layer-3 drift detector blind on its own hunting quadrant)  (filed 2026-07-16, COO; found by 0.6.2 on the v22b close)
<!-- key: tool-defect|deploy-ledger-md-status-colon-inside-bold -->
- disposition: _md_status() requires the exact token `**Status:**`; a ledger carrying `**Status: CLOSED, 2/2 legs**`
  (colon INSIDE the bold) returns None, so the Layer-3 DRIFT detector never fired on a ledger whose PROSE said
  CLOSED over two unproven legs -- precisely the drift-dangerous quadrant the detector exists for, missed on a
  cosmetic variant. Layer 1 caught that instance (nothing lost), but the detector's coverage is narrower than its
  docstring implies. Fix candidate: tolerant regex (\*\*Status:?\*\*:? / colon either side) + a self-test planting
  the colon-inside variant. Evidence: 0.6.2 131410Z + 291a28fc8.
- resolution: OPEN -- CTO ratification per the gap->build routing; rides the next deploy_ledger touch.
