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
| b | ontology | 06 reports cse_schema @0.4 while live=0.5 | **CONFIRMED** (2000Z) | 06_current_state.json:81 "@0.4"; cse_schema.py:42 SCHEMA_VERSION="0.5". Real declarative drift (= the OWNS 0.4->0.5 bump re-signed @b6e7055ef; 06 never regenerated). -> WS-2 de-stale. |
| c | ontology | surface_map.json omits RULE_BANK.yaml/variance_dimensions.yaml | **CONFIRMED** (2000Z) | surface_map.json:78-79 watches canon-patterns + AB_MATERIALIZE_SPEC only. = WS-3. SAME abstraction_loop as the drift-gate I verified @183xZ -> a 2nd facet of my C1 (under-inclusive denominator). WS-3 BAR: seeded RULE_BANK.yaml change must FIRE the gate (+ variance_dimensions + cse_emit_graphhead — all 3, one fix). |
| e | infra | infra SDK never cloud-applied (acme/verify-report.json tier=local) | **CONFIRMED** (fire-2 2012Z) | LOCATED at infra/system/sdk/tenants/acme/verify-report.json:2 = `"tier":"local"` (brief's path citation was imprecise; finding HOLDS). fire-1 could-not-verify was a path-resolution issue. |
| a | eng+loops | comp-system --check = SYSTEM STALE (ledger 80->82, tools 59->61) | **CONFIRMED** (fire-2 2012Z) | live `comp-system --check` = "SYSTEM STALE: 5 managed-region spans drifted -- 00_synthesis/03_comp_tools/README ledger_union 80->82; 03 tools_index 59->61". Exact match. -> WS-2 de-stale. |
| d | ontology | 0 of 8 core docs mention the ontology (14 Roles/10 Rel/6 Var) | **CONFIRMED-SHARPENED** (fire-2 2012Z) | CITATIONAL anchor (NFRA_ONTOLOGY/LD-0311/14-Roles/Custodian/Fork-Shadow/derives-from) = 0/8. The raw-word overlaps (Source 7/8, Producer 6/8, Twin 5/8, Canonical 3/8) are INCIDENTAL: "Canonical tier"=comp_ladder tiers (diff concept), "superseded-twin detector"=comp-similar TOOL, common-noun usage -- NONE a citation of the ratified taxonomy. NAME-vs-CONCEPT (item-1 prose-synonym class): a word-grep mis-verifies BOTH directions; only the semantic reading confirms the ontology is absent AS a governing framework. |
| ct-i | comp-tools | 03 names the rail without describing its enforcement | **CONFIRMED** (fire-3 2021Z) | 03:9 names "COMPRAIL" in a spine list + generic "enforcement" (03:3); but the DISTINCTIVE mechanisms (# rail-checked marker / DENY-gate / HUD / /freeform / Rule-21) are ABSENT from the text. Names the rail, not its enforcement. |
| ct-ii | comp-tools | "tenant-neutral comp-tools" overstated: 11+ hardcode, only comp-genesis+comp-which parameterize | **CONFIRMED-directionally, SHARPENED** (fire-3 2021Z) | 86 comp-* files; 12 carry opal-313476888478/opal-data-* literals (brief "11+" consistent). comp-genesis clean; comp-which's opal-data-assets is a ROUTING KEYWORD (:359), not a binding — brief holds. SHARPEN: the 12 MIX 3 categories — tenant-BOUND (comp-assets = opal-data-assets tool), firm-AWARE-by-design (comp-secrets/comp-freshness Rule-13 firm regexes = CORRECT, not a tenant-neutral gap), routing-keyword (comp-which). Thesis (tenant-porting UNBUILT) holds; the raw count over-states the *gap* by folding in legit firm-separation. |
| 4a | all | scope declared but incomplete (README boundary + 2 un-declared omissions) | **CONFIRMED** (fire-3 2021Z) | README "## Boundary" EXPLICITLY excludes the pipeline estate (INF/49F/COT/TAXSMA/OPAL_ASSETS) + taxonomy plane (sound boundary). But the ontology's absence has NO boundary sentence (neither in nor out) -> §4a(i) omission CONFIRMED (ties §5's rule-ontology-IN recommendation). |
| eng-1 | eng+loops | NESTEDABSTRACT incorporated only 1/5, 4/5 pending | **CONFIRMED** (fire-4 2113Z) | ABSTRACTION_LEDGER.jsonl = exactly 5 records; NA-0003 incorporation_status="incorporated" (notes cite the AC4 v2 raw-axis co-land + MY CVO re-sign @005100Z this session), NA-0001/0002/0004/0005 ="pending". 1/5 incorporated, 4/5 pending -- exact. |
| eng-2 | eng+loops | 06: 11 of 16 knowledge-classes UNKNOWN-VINTAGE | **CONFIRMED-directionally** (fire-4 2113Z) | ~12-13 UNKNOWN-VINTAGE string-fields (vs 19 "current", 8 "fresh") -> heavy staleness CONFIRMED (thesis holds). BUT exact "11 of 16" NOT cleanly reproducible: 06 embeds cert/vintage in FORMATTED STRINGS, not machine-clean JSON fields, so the 16-denominator isn't recoverable at the string grain. NOT a clean changed-number (grain-fuzzy, ~11-13). WS-2 input: regenerate 06 with clean machine-queryable vintage fields so the metric is countable. |
| S3-inf | infra | infra ~80%: SDK never cloud-applied (=(e) CONFIRMED); intraday-IAM describe-grant; producer plane 3/6 | PARTIAL | (e) done. fire-5: intraday-IAM describe-grant (would-AccessDeny) + producer-plane 3/6 + declared-but-unwired toggles. |
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

## Burndown status (fire-4)
Verified: b, c, a, d, e, ct-i, ct-ii, 4a, eng-1, eng-2 (10 items) + 4b/4c structural theses grounded on sub-findings. Remaining: S3-infra sub-claims (intraday-IAM / producer-plane / toggles), §6 WS premises, /prd-delta (deferred). Domains: comp-tools DONE (ct-i/ct-ii + count), ontology DONE (b/c/d), eng DONE (a/eng-1/eng-2), infra PARTIAL (e done; IAM/producer/toggles remain).
- WS-lands: verify each WS TO as COO decomposes (WS-2 de-stale/gate 06; WS-3 drift-gate denominator w/ the seeded-RULE_BANK bar).
- /prd-delta: PRD @8f0b596f4 landed -> delta WS completeness each fire.

— 3.0.0_SA_CVO
