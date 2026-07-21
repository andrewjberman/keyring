# 1.0.0_SA_CTO — MDPF_REVAMP cutover drive (census + disposition + routing mechanism) + WS-E PRD

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, IMPLEMENT
**Window:** 2026-07-21 crash-recovery (~135429Z) -> ~2114Z (first log of session) | **Serial:** 1.0.0_SA_CTO (main-fabric CTO)

## Summary
Drove MDPF_REVAMP (P0) from crash-recovery to a fully-specified, de-risked, HELD cutover. Andrew's mid-session directives reshaped it twice: (1) an UNDER-SCOPE catch (the page reads aum-metrics + aum-timeseries the revamp didn't produce -> 7->9 keys); (2) "confer with CVO, be comprehensive" -> a cross-verified FE-consumption census. Ruled every disposition, gated the routing mechanism through a real signing constraint, and authored the WS-E Cottonwood fold-in PRD. 10 commits, all to durable records (streak-tracker + PRDs). Nothing serves; everything HELD on producers + census + co-sign.

## Key rulings / gates issued (the substance)
- **Mechanism (S5 routing):** Option A (L@E origin-swap) -> RULED over Option-2-in-place (AE durability: legacy clobbers portal-v2 nightly) -> then FLIPPED to **Option C direct exact-8 behaviors** when AE grounded that OAC does NOT re-sign after an L@E domainName-swap (403). C clones the catch-all (reuse L@E, change only TargetOriginId) -> no swap, no re-sign; b1 PROVEN (own-origin OAC 200 + discriminating 403, zero-residual teardown). Quota was a MISCOUNT (25=count, real limit 75/50 headroom) -> no quota action. b2 skipped as moot; a C-pre-flight real-distro exercise (both path shapes) replaces it. Design pass GATED (apply held for census/A1/co-sign).
- **A1/A2 disposition (SPLIT, census-driven):** A1 aum-metrics = DS BUILDS a producer (4-surface blast radius: ModelPortfolios:425 + FactorTilts:83 + SelectionTab:89 + HoldingsTab:564 -- FE-derive too invasive). A2 aum-timeseries = DE FE-DERIVES (stale @05-29, FE already routes around it; DONE @2f603319, fixed a latent vintage bug). A4 = DS decouples from the legacy emitter (snapshot frozen pre-cutover + byte-verify). aum-timeseries DROPPED from routing (8 routed keys, not 9).
- **Coherence (a):** frontier per-model account_count = account_dist's own count via a stable model_key meta-map (coherent-by-construction; DT COHERENCE_PASS 3/3 @b75b459b3).
- **Content A+B:** honest-None in data + connectNulls in render (NOT LOCF, NOT drop-to-zero); grounded as additive feed-gaps (CVO: served=real history, not forward-fill; revamp richer overall), NOT regressions. Pre-onset boundary must NOT bridge.
- **cohort_provenance (Andrew-direct):** derive from the opal-data-assets SOURCE-PATH ({source}->display name), replacing served hand-labels AND revamp all-None. Lineage-derived, self-maintaining.
- **WS-E:** authored the production PRD (@5d62583e9); MDPF_COTMDL superseded; WS-1 ratifications (opal_closure transitive + roster-raw-complete; pagination = ground-estate-then-mirror else strict-pages + mandatory totalResultCount integrity gate).

## Compiler Tools
| Tool | Where | Result | Note |
|---|---|---|---|
| safe-commit surface-check | all 10 commits | PASS | "touch no critical surface" each (doc/tracker files) |
| comp-pulse risk-reflex (embedded) | all 10 commits | CLEAN | measured, 1 file vs 1239 danger nodes each |
| native Grep | portal/src FE-consumption | PASS | aum-metrics/aum-timeseries consumer trace (nudge-and-proceed; portal submodule, off estate-grep gate) |
| general-purpose agent | portal FE census | PARTIAL->PASS | stalled once (API), re-launched; delivered 15-row census |

**What worked:** delegating the deep grounding to the implementing agents (AE comp-routes/comp-blast on public-data-router L@E; CVO comp-grep whole-estate census; DS source-grounding) while I gated — the gate-not-implement split. The cross-verified census (mine + CVO's) found MORE than either alone (the 4-surface aum-metrics blast radius). **What failed:** the census agent stalled mid-stream once (API), un-resumable (no transcript) -> re-launched fresh. **Gap found:** none new; the "25 behavior limit" was a shared miscount (AE's originally, carried into my steer) — a load-bearing assumption grounded-away before an unnecessary quota request.

## MCP traffic
~40 dispatches sent this window (high; live cutover coordination hub). Significant: the mechanism rulings (A->2-rejected->C exact-8 gated), the A1/A2/A4 disposition + corrections (3 DS re-directs as the disposition converged through the census — owned the churn), content A/B ruling, cohort_provenance directive, the census confer+reconcile with CVO, the WS-E PRD handoff to COO+0.6.2, WS-1 ratifications, the AE OAC signing venue/test gate (b1 proven), COO reallocation approval. No RAVC left open by me.

## Blockers
None. The cutover is HELD (a deliberate multi-gate, not a blocker): producers (A1 build, A4 decouple, cohort_provenance) + census-close + full render-check + C-pre-flight + co-sign + verify-before-serve. WS-E scheduled-pull HELD on a STANDING egress word (surfaced to Andrew, pending — the per-use grants were discovery-scoped).

## Current State (handoff — zero prior context)
**MDPF_REVAMP cutover — HELD, fully specified. Durable source-of-truth: `org/critical_paths/MDPF_REVAMP_streak_tracker.json` (single-writer CTO).**
- **Mode:** PUSH-NOW (Andrew-authorized on verified cycle-1 data, "roll it back immediately if it doesnt work"); N=3 scheduled streak OVERRIDDEN by sovereign call, current_streak stays 0/3.
- **Routing mechanism = Option C exact-8 direct behaviors** on distro EVTSA9VEHNZVH (portal-auth workspace) + a dedicated assets OAC + a bucket-policy on opal-data-assets (opal-assets workspace) scoped to the 8 EXACT keys + SourceArn. Clone the catch-all (reuse L@E + auth, change only TargetOriginId). Rollback = remove behaviors -> catch-all resumes portal-v2 (untouched). AE building the concrete TF/behavior-JSON/publisher diffs to COMMIT near census/A1-clearing; APPLY after co-sign.
- **8 routed keys:** json/mdpf/{global,49financial,inflection}/aggregate-aua-timeseries.json + json/mdpf/{49financial,inflection}/account-distribution.json + json/portfolios/{account-distribution,non_model_assets,aum-metrics}.json. (aum-timeseries FE-derived, NOT routed.)
- **Producer state:** aggregate x3 + account_dist x3 coherent-staged @165b84ac4 (final ETags in tracker); A4 clean (DT NAMED_DELTA_PASS @de07f087c); coherence PASS 3/3 @b75b459b3; A2 FE-derive DONE @2f603319 (portal DEV). IN FLIGHT (DS): A1 aum-metrics producer (match legacy MoM/QoQ/YoY calc, field-identity to AUMMetricsResponse+AUMSummaryResponse), A4 decouple snapshot, cohort_provenance source-path population, content-B silver-infeasible->honest-None. IN FLIGHT (DE): connectNulls render (~6 null-plumbing sites, SEV1 chart) + content-A per-date diff.
- **Census:** reconciled CTO+CVO; CVO deliverable @760a457e8 (merging authoritative doc, CTO co-signs). Gaps = aum-metrics(A1) + aum-timeseries(A2); PartnerAnalytics AUA = separate advisor-intelligence pipeline (opal-data-bd/inf), out of scope; benchmarks/peers separate.
- **Pre-push gate (tracker pre_push_conditions):** census closed + 9-key(->8 routed) produced + content A/B resolved + coherent 3-pass + render-check (VALUE+COUNT, 3 firms, no picket-fence/mixed-basis) + C-pre-flight (both path shapes, 200+neg+fail-safe) + AE rollback tested + COO re-co-sign (pin to final ETags, cover all served keys) + verify-before-first-serve cycle-1.

**WS-E Cottonwood fold-in — PRD committed @5d62583e9 (`docs/architecture/WSE_COTTONWOOD_MDPF_FOLDIN_PRD.md`).** Project WSE_COTMDL, 5 TOs @761b2b86a (COO). WS-1 bronze (0.6.2) dry-built @e55bcbb00, GO'd build-phase (deploy-held on egress); ratifications sent (opal_closure transitive + roster-complete; pagination ground-estate). WS-2/3 silver/gold (DS, staged). WS-4 DDB fold-in (0.7.0) STAGED behind WS-3 + **MY sec-8 DDB-contract gate** (ratify the exact MDPF DDB model-row schema + write path, Rule 22a exact-ARN simulate on PutItem, before any MDPF write). WS-5 IAM (0.7.0) building gate-ready in the held MDPF window (COO reallocation). MDPF_COTMDL superseded (banner @9a779f9cd).

## Next Steps
- [1.0.0_SA_CTO] GATE the AE concrete MDPF diffs (behavior-JSON + origin/OAC/policy TF + publisher retarget) when committed near census/A1-clearing; run/verify the C-pre-flight (both path shapes) before the flip.
- [1.0.0_SA_CTO] Independent S3 re-verify of the coherent 8-key set + the coherence assertion at the final gate; co-sign package to [2.0.0_SA_COO] (pin final ETags).
- [1.0.0_SA_CTO] WS-E sec-8 DDB-contract gate when [0.4.0_DS_ClientPlatform] WS-3 gold lands.
- [0.4.0_DS_ClientPlatform] finish A1 producer + A4 decouple + cohort_provenance + report field-identity + source->provenance mapping.
- [0.4.0_DE_ClientPlatform] connectNulls render + content-A diff + heavy render-check (gaps bridged / pre-onset not fabricated / headline intact); report screenshots.
- [3.0.0_SA_CVO] merge the authoritative census doc (incl cohort_provenance RESOLVED); CTO co-signs.
- [0.7.0_AE_CloudOps] commit the MDPF diffs near census/A1-clearing; pivot from WS-5 on census/A1 clear.
- [ANDREW] standing egress word for the WS-E daily Cottonwood pull; cohort_provenance approach confirmed (source-path derive).
