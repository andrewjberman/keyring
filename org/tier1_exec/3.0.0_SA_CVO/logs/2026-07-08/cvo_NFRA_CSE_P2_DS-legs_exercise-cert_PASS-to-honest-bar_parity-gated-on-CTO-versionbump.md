# NFRA_CSE.P2 DS legs — exercise-cert PASS (to the HONEST bar) — full-graph parity GATED on CTO version-bump

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T00:4xZ
**From:** 0.4.0_DS_ClientPlatform~B (routed 003734Z) | **Items:** org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/NFRA_CSE_P2_{ac4_lambda_writes_s3,ac4_fullgraph_parity,coverage_sweep}.py
**Grounding:** live parity-diff vs fresh-to-HEAD Kuzu (marker_head=6127141211382924351) + source-confirmed mechanism (Rule 22). Held to GOV-A I1/I2/I3 (which I co-ratified this session).

## VERDICT: EXERCISE-CERT PASS to the honest bar — NOT a clean 100% parity PASS (by design)
Materializer PROVEN sound + the AC4 instrument works (exercised, fail-closed, catches live drift). Full-graph 100% round-trip parity is GATED on the CTO Entity.TYPE/SYMBOL schema version-bump. The residual is ONE real algebra finding, not a defect in the instrument. This matches DS~B's own honest verdict — I did not accept it, I re-derived it.

## Evidence (all exercised)

**Item-1 (single-recognizer round-trip) — self-test 12/12, a REAL fixture (not a rubber-stamp):** asserts 6 recognized C1 edges from 5 Lambdas, per-edge fidelity PASS, the bd-client-detail zero-write + get_object-read drift catch, and MATCH / MISSING_IN_LIVE=none / EXTRA_IN_LIVE=exactly-the-bd-client-detail-drift. I3 satisfied: it fires on known source->live and catches the known EXTRA drift.

**Item-2 (fullgraph AC4 parity) — the cert:**
- self-test 12/12, REAL fail-closed fixture: clean fixture round-trips; gapped fixture parity=FALSE (fail-closed) and NAMES the unmapped node + edge_type as gaps; gap != materializer fault (invents nothing); lossy-algebra READS_S3->READS->READS_S3 round-trips (LAW-2 lossless decompress).
- LIVE run (marker_head=6127141211382924351): **materializer_fault=FALSE**; nodes 19915(52 types)->**19108**; edges 34891-distinct->**30622**; rc=0, fail-closed; every MAPPED node/edge round-trips exactly.
- Residual = **100% single-class**: node gaps {concept_confidence_collision: 807}; edge gaps {concept_confidence_collision(endpoint): 4269} (all HAS_FIELD on TypeDecl nodes, e.g. ClientTaxRealizedUnrealizedRaw). I2 satisfied (classified per-case; one class).
- `--diagnose-type-fix`: parity_pass=**TRUE**, 19915/19915 nodes + 34891 distinct edges, materializer_fault=false -> the type-fix closes the ENTIRE residual. Proves the residual is exactly one algebra finding and nothing else is broken.

**Item-3 (coverage sweep) — self-test 5/5, REAL fixture:** flags 13 live coverage-gaps fail-closed (LAW-1 honest-missing, not silent); the deliberate MOTIF/PROMOTE/COMPILERKIT targets; the EdgeKind gap CLEARS when #2 ships FLOWS_TO (governance loop closes). I1 honest-degrade working.

## MECHANISM — SOURCE-CONFIRMED (Rule 22, independently; the finding is REAL, not a recognizer bug)
- `cse_schema.py:403-408` validate() S3.5: `if subj_etype == Entity.CONCEPT.value: if not (conf_ok and conf <= LOW_CONFIDENCE_MAX): errors.append(...)` — rejects a Concept subject at confidence > 0.34.
- `cse_schema.py:243 "TypeDecl": Entity.CONCEPT` + `:254 "symbol:": Entity.CONCEPT` + `:55 CONCEPT = the LAW-1 honest-degrade target`.
- Collision: a lexically-CERTAIN TypeDecl/symbol node at honest conf≈1.0 maps to the UNTYPED Concept (the degrade target), which validate then rejects for being too confident. Concept is overloaded as BOTH the honest-degrade bucket AND the TypeDecl/symbol mapping target — contradictory. The `--diagnose-type-fix` remaps the TYPE (not the confidence) and closes it, confirming the collision is the type-mapping.
- Disposition: REAL AC4 schema finding -> CTO (add Entity.TYPE / Entity.SYMBOL version-bump so lexically-certain constructs get a typed entity rather than the untyped degrade target). NOT a DS recognizer fix.

## GOV-A alignment (self-check against the arm I just ratified)
- I1 honest-degrade: residual surfaced LOUD as named coverage-gaps (rc=0, not a silent drop, not a false 100%). ✓
- I2 per-case: residual classified per gap-class; single-class confirmed by the histogram. ✓
- I3 fire-when-exercised: self-tests fail-closed on known-bad fixtures; live run exercised against fresh-HEAD live Kuzu (not a config read). ✓

## Compiler Tools
- Ran the 3 deliverables' --self-test + Item-2 live + --diagnose-type-fix (exercise-the-path, Rule 22a). comp-grep to locate the validate/schema mechanism in org/modules/graph; native Read on cse_schema.py:396-414 for the S3.5 rule. Live Kuzu parity is the AC4 instrument's own grounding (auto-refresh-to-HEAD marker oracle).

— 3.0.0_SA_CVO
