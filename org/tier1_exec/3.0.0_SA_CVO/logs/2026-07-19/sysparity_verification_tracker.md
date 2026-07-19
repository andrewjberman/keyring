# NFRA_SYSPARITY verification tracker (LD-0318 standing regime — 3.0.0_SA_CVO)

**archetype:** VALIDATE

**Living tracker** the 30-min loop (cron 02d90dce) reads + updates each fire. Rule: EXERCISE every brief
assumption against LIVE state (never the brief's report — CHECK-LIVE-NOT-FROZEN / Rule 22a). Brief:
`docs/briefs/NFRA_SYSPARITY_BRIEF_20260719.md`. PRD: `@8f0b596f4` (S7 folds this regime into WS acceptance).
Basis per item: /molecule + /verify (+ /prd-delta as WS land). Status: CONFIRMED (brief right at HEAD) /
DRIFTED (brief itself stale) / COULD-NOT-VERIFY / PENDING.

**REPORTING CADENCE (MSTR 201825Z — durable, applies every fire incl. after re-arm):** surface to MSTR+COO
ONLY on EXCEPTIONS — (a) a CHANGED assumption/parity-number, (b) a REFUTED brief finding, (c) a NEW
cross-connection / scope question, (d) a could-not-verify needing a lane call. Routine CONFIRMED-drift
verdicts roll into THIS tracker + the WS only — NO MSTR/COO turn (don't generate a 30-min nudge). Heartbeat
+ skip on a no-delta fire.

## Status by item

| # | Domain | Assumption (brief) | Status | Exercise evidence @HEAD |
|---|---|---|---|---|
| b | ontology | 06 reports cse_schema @0.4 while live=0.5 | **CONFIRMED-then-FIXED** (2000Z->2155Z) | fire-1 CONFIRMED drift; NOW FIXED by WS-2 part-a @4e5a78abc -- system_parity.py ont-cse-version-current PASS ("stale 0.4 absent"). Baseline MOVED (assumption closed). CHANGED-verdict, surfaced to ~A/MSTR. |
| c | ontology | surface_map.json omits RULE_BANK.yaml/variance_dimensions.yaml | **CONFIRMED** (2000Z) | surface_map.json:78-79 watches canon-patterns + AB_MATERIALIZE_SPEC only. = WS-3. SAME abstraction_loop as the drift-gate I verified @183xZ -> a 2nd facet of my C1 (under-inclusive denominator). WS-3 BAR: seeded RULE_BANK.yaml change must FIRE the gate (+ variance_dimensions + cse_emit_graphhead — all 3, one fix). |
| e | infra | infra SDK never cloud-applied (acme/verify-report.json tier=local) | **CONFIRMED** (fire-2 2012Z) | LOCATED at infra/system/sdk/tenants/acme/verify-report.json:2 = `"tier":"local"` (brief's path citation was imprecise; finding HOLDS). fire-1 could-not-verify was a path-resolution issue. |
| a | eng+loops | comp-system --check = SYSTEM STALE (ledger 80->82, tools 59->61) | **CONFIRMED** (fire-2 2012Z) | live `comp-system --check` = "SYSTEM STALE: 5 managed-region spans drifted -- 00_synthesis/03_comp_tools/README ledger_union 80->82; 03 tools_index 59->61". Exact match. -> WS-2 de-stale. |
| d | ontology | 0 of 8 core docs mention the ontology (14 Roles/10 Rel/6 Var) | **CONFIRMED-SHARPENED** (fire-2 2012Z) | CITATIONAL anchor (NFRA_ONTOLOGY/LD-0311/14-Roles/Custodian/Fork-Shadow/derives-from) = 0/8. The raw-word overlaps (Source 7/8, Producer 6/8, Twin 5/8, Canonical 3/8) are INCIDENTAL: "Canonical tier"=comp_ladder tiers (diff concept), "superseded-twin detector"=comp-similar TOOL, common-noun usage -- NONE a citation of the ratified taxonomy. NAME-vs-CONCEPT (item-1 prose-synonym class): a word-grep mis-verifies BOTH directions; only the semantic reading confirms the ontology is absent AS a governing framework. |
| ct-i | comp-tools | 03 names the rail without describing its enforcement | **CONFIRMED** (fire-3 2021Z) | 03:9 names "COMPRAIL" in a spine list + generic "enforcement" (03:3); but the DISTINCTIVE mechanisms (# rail-checked marker / DENY-gate / HUD / /freeform / Rule-21) are ABSENT from the text. Names the rail, not its enforcement. |
| ct-ii | comp-tools | "tenant-neutral comp-tools" overstated: 11+ hardcode, only comp-genesis+comp-which parameterize | **CONFIRMED-directionally, SHARPENED** (fire-3 2021Z) | 86 comp-* files; 12 carry opal-313476888478/opal-data-* literals (brief "11+" consistent). comp-genesis clean; comp-which's opal-data-assets is a ROUTING KEYWORD (:359), not a binding — brief holds. SHARPEN: the 12 MIX 3 categories — tenant-BOUND (comp-assets = opal-data-assets tool), firm-AWARE-by-design (comp-secrets/comp-freshness Rule-13 firm regexes = CORRECT, not a tenant-neutral gap), routing-keyword (comp-which). Thesis (tenant-porting UNBUILT) holds; the raw count over-states the *gap* by folding in legit firm-separation. |
| 4a | all | scope declared but incomplete (README boundary + 2 un-declared omissions) | **CONFIRMED** (fire-3 2021Z) | README "## Boundary" EXPLICITLY excludes the pipeline estate (INF/49F/COT/TAXSMA/OPAL_ASSETS) + taxonomy plane (sound boundary). But the ontology's absence has NO boundary sentence (neither in nor out) -> §4a(i) omission CONFIRMED (ties §5's rule-ontology-IN recommendation). |
| eng-1 | eng+loops | NESTEDABSTRACT incorporated only 1/5, 4/5 pending | **CONFIRMED** (fire-4 2113Z) | ABSTRACTION_LEDGER.jsonl = exactly 5 records; NA-0003 incorporation_status="incorporated" (notes cite the AC4 v2 raw-axis co-land + MY CVO re-sign @005100Z this session), NA-0001/0002/0004/0005 ="pending". 1/5 incorporated, 4/5 pending -- exact. |
| eng-2 | eng+loops | 06: 11 of 16 knowledge-classes UNKNOWN-VINTAGE | **CONFIRMED-directionally** (fire-4 2113Z) | ~12-13 UNKNOWN-VINTAGE string-fields (vs 19 "current", 8 "fresh") -> heavy staleness CONFIRMED (thesis holds). BUT exact "11 of 16" NOT cleanly reproducible: 06 embeds cert/vintage in FORMATTED STRINGS, not machine-clean JSON fields, so the 16-denominator isn't recoverable at the string grain. NOT a clean changed-number (grain-fuzzy, ~11-13). WS-2 input: regenerate 06 with clean machine-queryable vintage fields so the metric is countable. |
| S3-inf | infra | infra: SDK never cloud-applied (=(e)); intraday-IAM describe-grant; producer plane 3/6 | **CONFIRMED** (fire-5 2206Z) | (e) done+WS-5-labeled. intraday-IAM: CONFIRMED -- real incremental_updater calls dynamodb.describe_table (lambda_function.py:300) but SDK intraday.tf IAM grants only S3+SQS (no DescribeTable) -> would-AccessDeny if applied (DESIRED-SDK fidelity gap, no live impact; flagged to SDK-IAM owner). producer-3/6 + toggles remain (deep DESIRED-SDK TF review, low-impact). |
| WS-8h | infra | WS-8 hardened @b721ce89d (my declared-subset rec) | **CLEAR** (2211Z) | fail-closed both-directions (undeclared-fires + declared-excluded-OK); sdk_crosswalk_scope.json = scope_contract pattern; 7 flags -> 2 fedobs undeclared gaps + 5 declared-excluded. My rec implemented+verified. |
| WS-1v | all | WS-1 vintage fold @2399689ee (my working-tree-vintage finding) | **CLEAR** (2211Z) | metric now prints "VINTAGE: committed HEAD <sha> (reproducible across agents)", defaults committed-HEAD (ignores uncommitted worktree), --worktree for local. My 3rd finding closed end-to-end. = LD-0319 cold-trigger PREREQ MET -> rides my next load. |
| S4-rest | all | 4b (care-not-control) / 4c (SDK faithful-unproven) | PARTIAL | 4b spine CONFIRMED via WS-3 (drift-gate under-inclusive, found fire-1) + no-fail-closed-cadence; 4c CONFIRMED via (e) SDK-never-applied + eng-1 4/5-un-incorporated. Both structural theses now grounded on the sub-findings. |

## Standing methodological note (recurring across items — bank into WS acceptance)
**VERIFY-BY-STRING-MATCH MIS-VERIFIES BOTH DIRECTIONS** (item (d) ontology-words, item ct-ii tenant-literals):
a raw grep over- or under-counts because it can't tell CITATION from incidental-word, or TENANT-BINDING from
firm-separation-by-design. Every SYSPARITY finding stated as "X appears N times" must be verified on the
SEMANTIC axis (is each hit the thing claimed?), not the literal count. WS acceptance criteria should be written
citationally/semantically (grep-of-the-meaning), never grep-of-the-word. (Same class as item-1's "divergence
is debt" prose-synonym — the frozen-not-live hole one layer in.)

## Next-fire pickup
- fire-5: infra sub-claims (intraday-IAM describe-grant would-AccessDeny; producer-plane 3/6 scheduler-divergence; declared-but-unwired toggle vars) — the last un-exercised S3 domain. Then §6 workstream premises. /prd-delta DEFERRED until WS work progresses (WS-1 just GO'd @d60d4584a; running it now = uninformative ~0%; run when >=2 WS have TO-activity).

## WS-gate verdicts (LD-0318 PRD-S7 per-WS CVO gate) + standing-role updates (2155Z-2205Z)
- **WS-2** (06 de-stale + fail-closed gate) CLEAR @748bd523a -- CLOSES my fire-2 (a) comp-system-STALE + fire-1 (b) cse_schema: 06 now SYSTEM CURRENT (sources unchanged, 0 managed-regions drifted); engine --self-test 15/15 both-directions; gate is SOURCE-DRIFT-conditioned NOT wall-clock (the NEVER#1 false-Monday distinction in a fail-closed gate = the S4b care->control thesis) + fail-safe (tool-error -> WARN). Throwaway commit-gate leg taken as ~D-verified (logic self-test-proven).
>> BURST COMPLETE: all SYSPARITY workstreams CVO-verified (WS-1 SOUND, WS-2/3/4/5/7/8 CLEAR, WS-8h hardened, LD-0319 validated). Every charter domain closed: comp-tools (WS-7), ontology (WS-3+WS-4, my c/d), eng+loops (WS-2, my a/b + eng-1/2), infra (WS-1/5/8 + intraday-IAM). FIVE of my findings closed end-to-end on my own bars (a/b via WS-2, c/C1 via WS-3, d via WS-4, e via WS-5, vintage via WS-1-fold). REMAINING: LD-0319 cold-load trigger (rides next load) + ONTOCLARITY Part-2 (semantic axis, ~C's WS-A..D). <<
- **WS-3** (drift-gate denominator) CLEAR @a8917afdf -- CLOSES my fire-1 (c) + NFRA-wave drift-gate C1: RULE_BANK.yaml + variance_dimensions.yaml now IN the ontology surface. Seeded-FIRE bar MET: check 0f5ba0d92 (rule-bank) rc1 DRIFT (CLEAN pre-WS-3) + my INDEPENDENT check 68d728b90 (variance_dimensions) rc1 DRIFT; --self-test PASS. Both vocab facets fire; denominator under-coverage class closed (with the GLOBGRPH cse_emit_graphhead facet).
- **WS-7** (rail-description + count-reconcile) CLEAR: (a) OVERSTATED-self-caught by ~Z, corrected @f6ff89fa0 -> re-exercised, matches the live hook (aws/.tf=DENY, broad-grep=STAGED-NUDGE); (b) @82d447392 incorporated my ~61-vs-~12 flag; (c) 4 front-ends PASS; (d) scoping PASS. The fix for "names-rail-without-enforcement" itself overstated enforcement -> the SYSPARITY meta-defect, caught by exercising the gate.
- **WS-1** (parity metric) SOUND: denominator=declared scope, exclusions NAMED not scored (VL#6); axis=mechanical COVERAGE (not accuracy -- honestly defers accuracy to the CVO gate); ct-rail metric-GREEN while CVO-RED (WS-7 a) = the metric+CVO division proven live. FINDING: metric reads WORKING TREE not committed HEAD -> in the shared worktree it read ~C's uncommitted 03 edit; vintage must be declared/pinned. Routed ~A.
- **WS-4** (ontology representation) AC-4 CLEAR [Part A @e1f5f23 + Part B]: 00_synthesis @HEAD CITES the ratified ontology AS governing framework (NFRA_ONTOLOGY/LD-0311/0315 + canonical artifacts) -- CITATION not incidental words; citational anchor 0/8 -> 5/8 core docs; SDK ontology_ref cites the rule-bank artifact. Metric ontology domain FLIPPED 50% -> 100% (both FAIL units PASS). Verified on COMMITTED HEAD (my vintage finding). = my fire-2 (d) finding closed END-TO-END (name-vs-concept catch -> citational acceptance bar -> fix -> verified on that axis). ONTOLOGY DOMAIN (brief's weakest ~40%) now CLOSED.
- **WS-5** (SDK cloud-acceptance-bar label) PASS: "## Cloud-tier acceptance bar" threads the boundary precisely -- tier=local GROUNDED (both tenants verify-report.json), TF module Rule-22a-LABELED DESIRED-not-applied, "loop+storage cloud-exercised / full PROVISION not" avoids over- AND under-claim. Closes WS-1 inf-sdk-exercised-label FAIL. (storage-real-S3 sub-claim rides ~Z's grounding, noted.)
- **WS-8** (doc<->TF<->SDK crosswalk) SOUND: self-test PASS both-directions (seeds 3 defects each flagged + negative control no-false-fire); denominator globgrph-in/pipeline-out VL#6-printed; 7 uncovered files FLAGGED-not-masked. REC: declare the SDK component-subset (exclusions list) so "uncovered-declared-excluded" vs "silent-gap" distinguishes -> fail-closed control. fedobs/fedobs_glue = strongest should-cover candidates.
- ~A folded my WS-1 q3 axis-clarification INTO the metric's own description ("PASS=documented not accurate; metric-GREEN can coexist with CVO-RED by design"). Feedback -> tool self-description.
- **LD-0319** (PERMANENT load-time parity control, Andrew-direct): mechanism VALIDATED both controls (positive=reads true 100/75/80/50 not 100%-clean; negative=isolated in-memory seed FLIPS PASS->FAIL, LIVE). 3 homes landed: prompt.md @b8fa22d0c + XXX.md 1b-F + ajb.ps1 @150df9d23. Load-TRIGGER = could-not-verify-until-cold-load (rides next session load). Working-tree-vintage finding routed ~A.
- **ONTOCLARITY (SYSPARITY Part 2)** now in-regime (PRD @b9b132933, SEMANTIC axis): a fog class resolves only when the ambiguity is GONE (not reworded / not "a word appears") -- my word-grep-mis-verifies finding DROVE this explicit binding. 10 fog-spots = the Part-2 assumption list; verify as ~C's WS-A..D land.

## fire-7 (2246Z): /prd-delta completeness lens
7/8 SYSPARITY workstreams CVO-verified (WS-1/2/3/4/5/7/8). **WS-6 (incorporation-debt SLA) = the ONE remaining,
TO=STAGED (not started).** Its target debt GREW this session: NESTEDABSTRACT NA ledger 5->7 records, pending
4->6. The 2 new rows are the SESSION'S OWN fixes -- NA-0006=WS-2 staleness gate, NA-0007=WS-4 firm-alias map --
correctly DETECTED by the NESTEDABSTRACT loop + logged pending (detection sound; incorporation = the self-feeding
debt WS-6 SLAs). Surfaced COO (scheduling) + MSTR (exception). WS-6-land verify bar: each of the 6 pending
INCORPORATED-or-explicitly-DEFERRED, EXERCISED, not just an SLA date logged.

## ONTOCLARITY (Part-2, semantic axis) verdicts
- **WS-A** (root ontology-fog fix) @f7eef81f1 semantic-axis PASS: all 5 fogs RESOLVED (ambiguity GONE, not reworded, verified by reading the resolution not word-grep). (a) two-layer -- meta.layers states both senses + each disclaims the other, once authoritatively; (b) canonical-source -- self-declares + mirror DO-NOT-CONSUME banner (COMPLETENESS NOTE flagged: verify ALL 4 mirrors carry it, I checked 1+canonical); (c) Observer -- settled to full Role #13 "no longer open", no two-truths; (d) fork-shadow=debt -- ZERO live blanket assertion (my item-1 sweep re-confirmed on this HEAD); (e) variance_dimensions -- header disambiguates axes-vs-verdicts at point of confusion. Consistent-by-construction with WS-4 (00_synthesis two-layer = meta.layers). WS-B/C/D verify per-fog on the same bar as they land.

## fire-6 (2216Z): producer-plane 3/6 CONFIRMED-directionally
SDK globgrph module parameterizes ~3 producer concepts (derive/intraday/producers.tf) vs real ~6-7 globgrph
producers (comp_learns/cse/fedobs/item2a/item2b/resource_summaries/stitch) = documented tenant-template
SUBSET (3/6), consistent with WS-8's declared-subset (fedobs = the real scoping question). Scheduler-divergence
nuance = deeper DESIRED-SDK TF detail, low-value, not deep-exercised. Routine -> tracker, no nudge.
**ASSUMPTION BURNDOWN ESSENTIALLY COMPLETE** -- all brief §3/§4 meaningful items exercised across fires 1-6;
residuals (declared-unwired toggles, scheduler-divergence) are low-value DESIRED-SDK fidelity. NEXT: /prd-delta
(project completeness vs PRD) once WSs are TO-closed; ONTOCLARITY Part-2 semantic-axis verifies as ~C's WS-A..D land.

## Burndown status (fire-4)
Verified: b, c, a, d, e, ct-i, ct-ii, 4a, eng-1, eng-2 (10 items) + 4b/4c structural theses grounded on sub-findings. Remaining: S3-infra sub-claims (intraday-IAM / producer-plane / toggles), §6 WS premises, /prd-delta (deferred). Domains: comp-tools DONE (ct-i/ct-ii + count), ontology DONE (b/c/d), eng DONE (a/eng-1/eng-2), infra PARTIAL (e done; IAM/producer/toggles remain).
- WS-lands: verify each WS TO as COO decomposes (WS-2 de-stale/gate 06; WS-3 drift-gate denominator w/ the seeded-RULE_BANK bar).
- /prd-delta: PRD @8f0b596f4 landed -> delta WS completeness each fire.

— 3.0.0_SA_CVO
