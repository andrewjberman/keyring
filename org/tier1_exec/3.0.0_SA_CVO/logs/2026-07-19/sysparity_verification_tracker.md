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
| S3-rest | infra/eng/ontology | infra ~80% / eng ~70-75% / ontology ~40% aggregate % | PENDING | fire-4: exercise the infra/eng sub-claims (SDK never-applied already=(e); intraday-IAM describe-grant; 4/5 abstractions un-incorporated). |
| S4-rest | all | 4b (care-not-control) / 4c (SDK faithful-unproven) | PENDING | fire-4: 4b = the drift-gate under-inclusive (= WS-3, already found) + no fail-closed cadence; 4c = SDK never cloud-applied (=(e)) + 4/5 un-incorporated. |

## Standing methodological note (recurring across items — bank into WS acceptance)
**VERIFY-BY-STRING-MATCH MIS-VERIFIES BOTH DIRECTIONS** (item (d) ontology-words, item ct-ii tenant-literals):
a raw grep over- or under-counts because it can't tell CITATION from incidental-word, or TENANT-BINDING from
firm-separation-by-design. Every SYSPARITY finding stated as "X appears N times" must be verified on the
SEMANTIC axis (is each hit the thing claimed?), not the literal count. WS acceptance criteria should be written
citationally/semantically (grep-of-the-meaning), never grep-of-the-word. (Same class as item-1's "divergence
is debt" prose-synonym — the frozen-not-live hole one layer in.)

## Next-fire pickup
- fire-4: S3-rest (infra/eng sub-claims: intraday-IAM describe-grant; NESTEDABSTRACT 4/5 un-incorporated; 11/16 UNKNOWN-VINTAGE) + S4-rest (4b/4c). /prd-delta once WS TOs land (WS-1 GO'd @d60d4584a — delta its acceptance).
- WS-lands: verify each WS TO as COO decomposes (WS-2 de-stale/gate 06; WS-3 drift-gate denominator w/ the seeded-RULE_BANK bar).
- /prd-delta: PRD @8f0b596f4 landed -> delta WS completeness each fire.

— 3.0.0_SA_CVO
