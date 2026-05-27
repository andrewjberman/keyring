# FIND_INSURE — CVO Validation Mandate (Andrew sovereign 2026-05-27T~2050Z)

**Audience:** 3.0.0_SA_CVO (primary), 2.0.0_SA_COO (CC for /drive prioritization)
**Author:** 1.0.0_SA_CTO (ws CTO; directive-routing, not novel scoping)
**Trigger:** Andrew direct sovereign 2026-05-27 ~2050Z to ws CTO. Verbatim:

> "the primary work focus for this session on ws is FIND_INSURE. I want CVO to be on top of validating the initial phase work. We need to know first of all that all 99 URLs were scraped from the imo list. We need to know what the results of that scrape were. We need to know what the fields are in the bronze/silver/gold web-scrape files are, we need to know if the information is being parsed effectively, we need to know what that gold structured layout looks like and how we're ranking entities that appear to have wealth-management programs or may be adjacent to it, we need to know what the criterion for wealth/asset management terminology is and how it's being classified, all of these details need to be established objectively and CVO needs to be on top of it and assess that we are indeed setting up these channels in a meaningful, business-useful way, not just mechanically doing a bunch of bullshit throwing noise around."

## Session focus declaration

**Primary ws session focus is FIND_INSURE.** All ws CTO /ws-charter cycles + ws COO /drive cycles + ws CVO /spot-check + /verify-channel cycles deprioritize non-FIND_INSURE work until Andrew rescopes. Other active ws projects (ADVI_*, ADHC_*, YALP_MACROS, SXPL_RESTIN, TRSB_LEDGER) continue under worker-lane autonomy but do not consume Tier-1 bandwidth this session.

## CVO mandate — 11 validation axes (objective evidence required per axis)

CVO is directed to execute `/verify-channel` across the following axes for Phase 1 (web-scrape end-to-end across 99-IMO universe). Each axis = answerable with concrete S3 paths, counts, sample records, schema diffs, or rubrics. No narrative-only verdicts.

### Crawl coverage
1. **C1 — 99/99 attestation.** Empirical evidence that ALL 99 IMO source URLs were crawled (CVO 1933Z spot-check noted current state "empirical 3/99 scraped"). Required: S3 bronze object inventory under `s3://opal-data-imo/corp/{slug}/web-scrape/bronze/{YYYY-MM-DD}/` showing per-IMO crawl-attempt presence. Expected output: table of 99 IMO slugs × {present | missing | error}.
2. **C2 — Crawl outcome distribution.** For the 99 attempts, classify outcome: SUCCESS (body_text non-null + content_length > N), EMPTY-BODY (body_text null or whitespace-only), BLOCKED (HTTP 4xx/5xx or anti-bot), TIMEOUT, ERROR. Required: counts per class + sample failure records. This is the AC-T2 escape-valve trigger input — if EMPTY-BODY class >5-10% per PRD threshold, AE 0.7~B scraping_browser1 v0.3.0 fires.

### Field inventories (bronze / silver / gold)
3. **B1 — Bronze field inventory.** Read 5+ representative bronze objects across success/empty/blocked classes. Enumerate every field present + dtype + null-rate + sample value. Identify any "intent-stated-but-not-actually-populated" fields (the column-gap class from comp-pipescript io history).
4. **S1 — Silver field inventory + Rule-17 preserve-all check.** Same as B1 for `data/find/imo/scripts/silver/parse_web_silver.py` output. Confirm silver does NOT slim bronze fields (CLAUDE.md Rule 17 — silver = dedup + dtype standardize only; no `output_cols` projection, no `fillna()` business defaults, no row-filtering on business semantic). Diff bronze field-set vs silver field-set; flag any drops.
5. **G1 — Gold structured layout.** Read score_web_gold.py output. Enumerate gold schema. Confirm structural shape suitable for downstream consumer (IR team target tables): is each row a (company, indicator-bundle, score, evidence)? Are fields decision-useful or just intermediate?

### Parsing effectiveness
6. **P1 — Parsing yield.** For bronze records with body_text populated, what fraction yield non-trivial silver content (meta_tags, headings, link_graph, structured_blocks)? Are the parsers extracting decision-useful signal or just text dumps? Sample 10 records across the IMO size distribution.
7. **P2 — Empirical false-positive / false-negative on indicator terms.** For 5 IMOs where wealth/asset-management presence is publicly known (Andrew can spot-check) and 5 where it's known absent, does the gold score correctly discriminate? This is the "true-positive on Avantax (100 mature-AM) + true-negative on 1st-Atlantic (0 insurance-only)" pattern already validated 2-IMO; expand to 10.

### Wealth/asset-management classification
8. **W1 — Term taxonomy criterion.** Read `data/find/imo/config/term-taxonomy-v1.json`. Document the explicit criterion for what counts as "wealth management" / "asset management" / "adjacent" vs. unrelated. Is the criterion (a) keyword-presence, (b) keyword-context, (c) co-occurrence-pattern, (d) something else? What threshold separates "has-WM-program" from "adjacent" from "absent"?
9. **W2 — Scoring weights traceability.** Read `data/find/imo/config/scoring-weights-v0.1.json`. For each weight, justify provenance (Andrew direction / empirical fit / heuristic). Are weights load-bearing or post-hoc justifying a ranking the team already wanted?
10. **W3 — Ranking output.** Read serving-layer scoring table. For the top-quintile IMOs the pipeline currently ranks "WM-present", read 5 evidence trails: which silver/gold fields drove the rank? Are the evidence trails compelling or trivially superficial (e.g., "site mentions retirement" → ranked AM-present)?

### Business-usefulness meta-assessment
11. **M1 — Noise vs. signal.** Standing outside the mechanical pipeline, render CVO judgment: is this pipeline producing IR-team-actionable output, or is it throwing noise around? Specifically — would an IR analyst, handed the current top-20 ranked IMOs + evidence trails, agree with the ranking after 30min of independent verification? If not, what's the fix?

## Output format

CVO writes one `/verify-channel` finding doc per axis, or one consolidated finding doc with 11 sections. Per Andrew's "established objectively" criterion: each axis answer = S3 path / file path / count / sample / verbatim config field. NO narrative-only assertions.

Per Andrew's lift-grading framework `[[feedback_lift_grading_framework_cvo_judgment]]`: CVO assigns delivered_lift_grade per axis (A/B/C/D/F). M1 is the aggregate grade — is this even working as a business artifact.

## Routing

- **ws CVO (3.0.0_SA_CVO):** primary execution. Engage immediately; this displaces /spot-check 20m default cadence for this session.
- **ws COO (2.0.0_SA_COO):** /drive cycles prioritize FIND_INSURE worker-lane dispatch (DS~A/B/C/D/E + AE 0.7~A/B) ahead of non-FIND_INSURE backlog this session. Surface any blocker to CVO axes immediately.
- **ws CTO (1.0.0_SA_CTO; self):** standing for REPAIR-AMENDMENT triggers from CVO findings. If CVO renders (a) mechanical-untruth or (b) inadequate-coverage on any axis, /ws-charter authors PRD/spec repair within the cycle.

## Expected cadence

Andrew implicit standard: "primary work focus for this session" = expect substantive CVO findings within ~1-2 /spot-check cycles (40-60min wall). Not "next session" or "queued for tomorrow."

## Anti-pattern guardrails

- **No mechanical PASS.** CVO does not rubber-stamp pipeline existence as "channel working." Each axis answers a *useful* question, not a *checkbox* question.
- **No self-validation.** CVO did not author the FIND_INSURE pipeline (DS pods + AE 0.7 did); CVO has clean independence on these axes.
- **No deferral to Phase 2.** Phase 1 must justify itself empirically before Phase 2 LinkedIn enrichment fires. If Phase 1 ranking is noise, Phase 2 is noise on noise.

## Logged

- Brief commit: this file
- Per-tick log: `org/tier1_exec/1.0.0_SA_CTO/logs/2026-05-27/ws-charter_2050Z.md` (NOVEL-class cycle 0091)
- ws CTO MCP to ws CVO + CC ws COO: same commit cycle

Andrew sovereign direction binds. CVO and COO acknowledge by action, not by reply.
