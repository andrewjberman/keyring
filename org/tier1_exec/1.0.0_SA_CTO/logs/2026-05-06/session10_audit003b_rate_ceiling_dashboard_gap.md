# 1.0.0_SA_CTO — Session 10: AUDIT-003B authoring (DS~A poisoning recovery) + Orion rate-ceiling empirical + dashboard $17M gap diagnosis + INFREL/INFINGE rulings

**Date:** 2026-05-06 (session followed from 2026-05-05 sprint EOD)
**Frame:** Heavy CTO-decision day — three major rulings, one direct-authored TO, one major incident recovery (context-poisoning), one empirical investigation that reset architectural assumptions on vendor rate ceilings. ~3-4h continuous wall.

---

## Session summary

Started in light-touch monitor posture per session 9 close. Andrew drove the day's pivots:

1. **AM ruling — INFINGE.005 TO-5b** canonical-script fork (AE 0.6.1 surfaced two viable scripts; CTO ruled `_v2.py` over `_rest.py` for Lambda-fit alignment)
2. **Mid-morning empirical investigation** — Andrew asked about peak RPS during HISTBF Wave B v5 backfill; CTO read S3 rate-limit-state files directly and discovered the vendor REST ceiling is ~300 RPS sustained per dim with zero 429s across ~13,594 batches. Phase 0 spec ceiling (1.0 req/sec) was off by ~300x. Documented + memory'd + MCP'd to AE 0.6.1 + AE 0.7 with directive to use burst RPS for QA + raise scheduled-job defaults during the in-session iterative cycle
3. **Major incident — DS~A context-poisoning recovery** — Andrew flagged DS~A repeatedly emitting `joe_brunswick` instead of correct `joe_brandenburg` even mid-correction. CTO diagnosed two-cause failure (LLM autoregressive anchoring + workspace contamination from 76 occurrences across 22 files). Per Andrew direct authorization, CTO authored ADVI_INFLEC.AUDIT-003B TO directly with anti-poisoning protocol. DS~A executed clean in fresh session, RAVC4 accepted same-session, all ACs PASS
4. **Dashboard $17M gap diagnosis** — Andrew flagged DS~D's "EXPECTED — different calculation sources" framing of a $17.1M gap in `dashboard.json` headline vs leaderboard total_aua. CTO confirmed empirically that gap = missing joe_brandenburg AUA (his book.total_aua = $16.16M); root cause is AUDIT-003 silver-fresh-pending. Reclassification ask to COO + P0 promotion of AE 0.6.1 silver-fresh dispatch
5. **INFREL.001 Fix B rulings** — Option 2 default with consumer-trace pre-check gate; pre-check tripped (3 active consumers); flipped to Option 1 with INFREL.001b spec to COO for authoring (DS~B lead, AE 0.6.1 secondary)
6. **INFINGE.005b path/silver rulings** — three Q's verified empirically against codebase + S3; REPLACE pattern, no-v2-suffix, add DIM_BUILDER (don't author separate file)

---

## Work product (commits authored)

| Commit | Subject | Notes |
|--------|---------|-------|
| `10dc81e9b` | docs(inflec_histbf_rate_limiter_constants): empirical addendum — Wave B v5 reached 300 RPS per dim sustained, zero 429s across 13K+ batches | Phase 0 spec (1.0 req/sec) deprecated; QA+iterative-cycle bursting authorized; INITIAL_RATE bump for daily Lambdas recommended |
| `bc029112d` | to(ADVI_INFLEC.AUDIT-003B): CTO authors workspace name-correction sweep TO for DS~A per Andrew direct authorization 2026-05-06 | --force used (FORCE-BYPASS audit logged); cross-lane authorship per Andrew direct exception to CTO TO-authoring policy |

Both pushed by DT 0.4 per CTO MCP push requests. DS~A subsequent commits `a4e505460` + `23925b518` closed the AUDIT-003B sweep (DS authorship; not CTO commits).

---

## Major work item 1 — Orion REST rate ceiling: empirical reality vs Phase 0 spec

**Context.** Andrew asked about peak RPS during HISTBF Wave B v5 backfill. Believed it was "190+ RPS." DS~D's session monitoring captured 105-134 RPS per dim during early hours; the run continued autonomously for ~50 more hours after polling stopped; Andrew wanted ground truth.

**Method.** CTO direct S3 read of rate-limit-state JSON files.

**Findings (S3 ground truth, 2026-05-06):**

| File | rate_rps | total_observed_batches | observed_ceiling | last_failure |
|------|----------|------------------------|------------------|--------------|
| `s3://opal-data-inf/orion/rate_limit_state_positions_mv.json` | **300.43** | 6,801 | null | null |
| `s3://opal-data-inf/orion/rate_limit_state_assets_v2.json` | 152.71 (post one orchestrator-restart reset) | 6,793 | null | null |
| `s3://opal-data-inf/orion/rate_limit_state_performance.json` | 4.0 | 4 | null | null |

`observed_ceiling = null` across all three means **the rate limiter never hit a 429 across ~13,594 batches**. The 152.71 RPS for assets_v2 (vs 300 RPS for positions_mv with near-identical batch counts) traces to one orchestrator-restart event during the autonomous backfill that wrote a lower rate without going through the failure path — assets_v2 had to climb again from there. The actual demonstrated vendor ceiling is **≥300 RPS per dim sustained**, aggregate ~450 RPS across two parallel dims.

**Phase 0 spec was off by ~300x.** Original `docs/data/inflec_histbf_rate_limiter_constants.md` (90-call probe, ADVI_HISTBF.001) recommended 1.0 req/sec conservative ceiling, 1.3 req/sec observed. The spec was right for what it was — a vendor-courtesy first-touch probe — but is obsolete now that we have ~13K-batch production evidence.

**Implications applied to in-session work:**

1. Empirical addendum committed to `docs/data/inflec_histbf_rate_limiter_constants.md` (`10dc81e9b`) with the rate-state ground truth, updated Phase 1 scale estimates, and recommendations for QA bursting + scheduled-job INITIAL_RATE bumps
2. Memory entry `project_inflec_orion_rest_rate_ceiling.md` saved + linked from MEMORY.md `## ADVI_INFLEC Pipeline` section so future-CTO sessions inherit
3. MCP'd AE 0.6.1 + AE 0.7 with directive: use burst RPS (30-50+) for QA dispatches during this session's INF iteration cycle; consider INITIAL_RATE bump from 1.0 → 30 for INFINGE Phase 1b daily Lambdas (TO-1/2/3 already shipped at default; backlog tweak)
4. INFINGE.005b TO-5b (TXN Lambda) and INFREL.001b (performance Lambda) both spec'd with INITIAL_RATE=30 from authoring time, not paying rediscovery tax on every cron fire
5. Risk Register C in INFINGE PRD downgrades from MEDIUM to LOW (vendor-rate-suspension risk) based on this evidence — CTO follow-on edit, non-blocking

**Process learning.** CloudTrail wouldn't have helped (third-party API; no AWS-side surface). S3-direct read of rate-limiter persisted state was the right answer in <1 minute. When I'm asked an empirical question and the data lives in a structured artifact in S3, going to that artifact directly is faster + more trustworthy than reconstructing from agent monitoring messages.

---

## Major work item 2 — DS~A context-poisoning incident + AUDIT-003B authoring

**Trigger.** Andrew shared a DS~A chat transcript where the agent kept emitting `joe_brunswick` (wrong) instead of `joe_brandenburg` (correct) even when explicitly corrected. Multiple correction turns, agent acknowledged each time, then immediately re-emitted the wrong token.

**Diagnosis.** Two reinforcing causes:

1. **LLM autoregressive anchoring under correction-as-reinforcement.** DS~A's session context contained 30+ prior `joe_brunswick` tokens written by the agent itself (their session log filename was literally `ADVI_INFLEC_AUDIT003_joe_brunswick_top_holdings.md` with 20 occurrences inside, plus 15 in another file, plus stragglers). When user said "X is wrong, Y is right", model attention spiked on the disputed token. With N≈30 prior wrong-token occurrences vs 1-2 corrections, autoregressive next-token prediction snapped back to the wrong token. The first message in Andrew's transcript was the smoking gun: the agent wrote `joe_brunswick (b-r-a-n-d-e-n-b-u-r-g)` — spelled letters correct, surface token wrong. Model had the right phonetic decomposition but the wrong cached label.

2. **Workspace contamination feeds back into agent context.** 76 occurrences of the wrong token across 22 files. Critical contamination loci: DS~A's own session logs (47 occurrences across 5 files; agent re-reads on resume), `org/tier1_exec/1.0.0_SA_CTO/prompt.md` dashboard line (loaded into every CTO session start — including mine), `docs/architecture/ADVI_INFINGE.md` PRD, `data/orion/scripts/gold/INF_D_08.nmec_nmnc_nna.py:17` comment, several DE/AE/COO logs. **One critical TRUE POSITIVE that needed protection:** `data/black_diamond/scripts/gold/lib/ticker_overrides.py:154` `'BRUNSWICK CORP COM': 'BC'` — actual public company Brunswick Corporation, unrelated to advisor; do NOT replace.

**Action.** Andrew closed DS~A's session, restarted fresh, and explicitly authorized CTO to author the recovery TO directly per the CTO role's "Andrew explicit ask" exception clause.

**TO authored:** `ADVI_INFLEC.AUDIT-003B.workspace-name-correction-sweep.md` (commit `bc029112d`).

**Anti-poisoning design baked into TO body** (key innovation; reusable for future similar incidents):

- **Rule 1:** Do not type the names from memory; copy-paste from the TO only
- **Rule 2:** Do not read prior session logs to "verify" or "remember context" — they're poisoned
- **Rule 3:** Do not narrate the contaminated token in chat or commits beyond strict necessity
- **Rule 4:** Mechanical replacement only — `Edit` with `replace_all: true` per file
- **Rule 5:** Verification is grep-count, not eyeballing
- **Rule 6:** Explicit exclusion callout for the legitimate Brunswick Corporation ticker entry

Plus phased file inventory (22 files), explicit grep commands, machine-checkable ACs (post-state grep counts), single atomic commit pattern (prevents partial-state re-contamination during partial agent pulls), and explicit cross-lane override authorization (Andrew-direct, FORCE-BYPASS audit entry).

**Execution outcome (DS~A):** Clean. Two commits (`a4e505460` + `23925b518`), push confirmed, all ACs PASS. AC1/AC3 quasi-pass adjudicated by CTO as PASS — meta-documentation (TO body + DS~A's session log) is the audit trail and necessarily references what it cleaned; not contamination per the spec's intent. Plus DS~A correctly identified a silver `ticker_overrides.py` legitimate-exclusion that CTO had missed in Rule 6 (only listed gold path; DS~A correctly preserved both). Plus DS~A swept 3 out-of-inventory files written by other agents post-inventory ("TO mission spirit" execution). Acceptance dispatched same-session.

**Side dispatch.** S3 contaminated-key prefix `qa/advisors/joe_brunswick/` (single 1534-byte JSON, superseded same-day by canonical key 9 minutes later) routed to AE 0.6.1 for parity-check + termination. Production prefix `platinum/advisors/` was already clean — no production-data impact.

**Process learning — bigger.** This is the second incident in two weeks where workspace contamination structurally fed agent context-poisoning. The mitigation pattern (anti-poisoning protocol in TO body + categorical sweep + fresh-session restart + cross-lane single-atomic-commit) should be promoted from one-off to a documented playbook. CTO follow-on item: capture this pattern as `docs/architecture/AGENT_CONTEXT_POISONING_RECOVERY.md` for future reference. Non-blocking; not authored this session.

---

## Major work item 3 — dashboard.json $17M gap diagnosis (Andrew empirical insight)

**Trigger.** DS~D FYI'd a `dashboard.json` v10 patch (advisor_count 3→4) and noted a $17.1M gap between `headline.total_aua = $182,552,380.96` and `leaderboard.total_aua = $199,649,186.31`, framing it as "EXPECTED — different calculation sources. NOT a regression. Documented in INF_D_04 L624."

**Andrew's instinct (correct):** "if one vector has it and another doesnt, the one that doesnt is missing joe_brandenburg aua."

**CTO empirical confirmation in three layers:**

| Layer | Evidence |
|-------|----------|
| Arithmetic | `joe_brandenburg/summary.json` book.total_aua = $16,158,184.71. Gap = $17,096,805.35. Same advisor + ~$1M measurement-method noise (book uses tagged_aua per-account, distribution sums 67 holdings = $15.1M, leaderboard uses market_value.sum). Three valid lenses, dominant signal unambiguous. |
| Code contract | `INF_D_04.client_portal_summary.py:619-620` documents `dashboard.headline.total_aua` should be `~$199.4M` and is `backed by canonical_holdings`. The actual $182.5M directly contradicts the documented contract. Both calls SHOULD be backed by canonical_holdings, not different sources. |
| Wrong line citation | DS~D's "documented in INF_D_04 L624" reference points to the `non_fee_earning_aua = total_aua - fee_earning_aua` residual calculation — entirely unrelated to the headline-vs-leaderboard variance. Built an incorrect "expected" rationalization on the wrong line. |

**Root cause.** Two paths diverge precisely on the rep_id=6 silver-dim coverage:

| Source | Path | rep_id=6 status |
|--------|------|------------------|
| `dashboard.headline.total_aua` ($182.5M) | reads `silver/api_dims/assets/` — STILL MISSING rep_id=6 partitions until AE 0.6.1's fresh bronze→silver convert lands | excludes joe_brandenburg |
| `leaderboard.total_aua` ($199.6M) | reads via positions_mv → canonical_holdings (upstream raw, not rep-filtered silver) | includes joe_brandenburg |

This is the AUDIT-003 symptom that DS~B's `e257875ec` hardcoded-dict fix was supposed to close, gated on AE 0.6.1's fresh bronze→silver convert.

**Actions dispatched:**

1. MCP COO to **reclassify the dashboard.headline cell from GREEN/expected to RED-(c) symptom of AUDIT-003 silver-fresh-pending**, plus a feedback note on DS~D's analysis quality (cited wrong line + observed-vs-contract didn't match — Andrew caught from outside the data lane, want feedback loop closed inside the lane next time)
2. MCP AE 0.6.1 to **promote silver-fresh dispatch from queued to P0** since this is no longer internal-matrix-only — it's a $17M divergence on a partner-visible firm dashboard. Validation gate post-fix: `abs(headline.total_aua - leaderboard.total_aua) < $100K`

**Process learning.** Andrew's outside-the-data-lane intuition outperformed DS~D's inside-the-data-lane analysis. Why: Andrew brought the org context (joe_brandenburg has been the chronic missing-from-data problem) plus a simple arithmetic check (gap ≈ his AUA). DS~D was operating on an inherited "expected" framing without arithmetic verification. Lesson: when there's a known active investigation involving a specific entity, ANY material variance involving that entity should be tested against "is this our active known issue?" before being classified as "expected." Cheap arithmetic check, expensive miss.

---

## Major work item 4 — INFREL.001 Fix B rulings (Option 2 → Option 1 flip)

**Initial ruling.** Option 2 default (remove `performance_dim` from inf-silver-chain Lambda's SILVER_BUILDERS auto-chain, preserve `build_performance` function code for INFINGE Phase 2 reuse), gated on AE 0.6.1 running a `comp-pipescript consumers` pre-check before removing. Three drivers: (1) honors already-accepted INFINGE TO-4 PERFORMANCE deferral; (2) performance silver is structurally current-state-only by HISTBF design; (3) Option 2 is the actual structural fix (silent-failure-on-missing-input, not missing-daily-refresh).

**Pre-check tripped.** AE 0.6.1's consumer trace surfaced 3 active gold consumers reading `silver/api_dims/performance/` — INF_D_00c.portal_leaderboard, INF_D_02.advisor_client_detail, INF_D_04.client_portal_summary, plus a `gold_freshness_config.yaml` monitor entry. All three have graceful degradation (WARN + null), not hard-fail; data has been stale at 2026-04-28 for ~1 week with no production breakage, only WARN noise. But the architectural posture changes — Option 2 would silently retire a dim that has active downstream readers (even if graceful), which violates the "don't remove what's still wired" principle.

**Flip to Option 1 with INFREL.001b spec.** COO authors the TO; **NORMAL priority** (not P0; graceful fallback in all 3 consumers means no urgency); **non-blocking on Fix A/C/D**:

- DS~B authors `pull_inflection_performance_dim.py` (new bronze script, modeled on `orion_billing_dim.py`); `INITIAL_RATE = 30` per the rate-ceiling finding (skip the 1 RPS rediscovery tax)
- AE 0.6.1 wires DimSpec in orchestrator.py + confirms `build_performance` reference in SILVER_BUILDERS still resolves + freshness config stays valid
- Acceptance: bronze csv landing daily, silver parquet landing daily, INF_D_00c/02/04 stop emitting WARN within 24h, freshness monitor alarm clears
- Sequential within DS~B lane: Fix D first (already in flight), then INFREL.001b

COO ACK'd same-session, authored TO `ADVI_INFREL.001b.performance-dim-bronze-producer.md`, dispatched DS~B + AE 0.6.1 with GO.

**Process learning.** Pre-condition gates on rulings work. The Option 2 default + pre-check structure let me give COO an immediate ruling without waiting for the trace, AND it auto-flipped cleanly when the pre-check tripped. No second round-trip to me for the flip — the trigger was machine-checkable (consumer count > 0 = flip). Use this pattern more.

---

## Major work item 5 — INFINGE.005b path/silver rulings (Q-A/Q-B/Q-C)

**Trigger.** AE 0.6.1 Phase 0 RAVC3 surfaced three path discrepancies in TO-5b body vs empirical reality. COO routed for ruling.

**Method.** CTO empirical verification — codebase grep + S3 ls.

**Q-A: bronze path discrepancy** — TO assumed `bronze/orion-api-v2/{date}/transactions_v2.json`; actual `pull_inflection_transactions_v2.py` writes `bronze/orion-api/{date}/transactions.csv` (CSV, not JSON, per Custom Reports endpoint contract). **Ruling: REPLACE pattern, same key, CSV format.** Consistent with Phase 1b architectural intent and TO-1/2/3 precedent — Lambda takes over orchestrator's bronze key; orchestrator's transactions DimSpec gets decommissioned at cutover.

**Q-B: silver dim name** — TO says `transactions_v2`; actual existing convention is `silver/api_dims/transactions`. Empirically S3 `silver/api_dims/` has neither prefix yet (dim is being created from scratch). **Ruling: `silver/api_dims/transactions` — no v2 suffix.** The "_v2" was copy-paste from bronze script naming; silver layer doesn't carry version suffixes.

**Q-C: build_transactions_dim.py** — SILVER_BUILDERS comment says "PLANNED — not yet authored by DS~A". Empirically: `build_transactions_dim.py` does not exist in current code (only an archived black_diamond legacy file, irrelevant); `convert_orion_api_to_silver.py` is the canonical pattern with 8 existing DIM_BUILDERS (household, performance, activity, billing, accounts_v2, representatives, household_rep_mapping, positions_mv). **Ruling: ADD `transactions` as a 9th DIM_BUILDER inside `convert_orion_api_to_silver.py` — do NOT author a separate file.** DS~A authors (newly free post-AUDIT-003B; tightly coupled to AE 0.6.1's Lambda).

**Caveats flagged to COO:**

1. **No downstream gold consumer currently reads `silver/api_dims/transactions/`** — empirical post-cron-fire won't show any gold-side delta beyond fresh silver partition landing. INFINGE Phase 1b is foundational; consumer-side wiring comes later.
2. **TO-5b body has stale path assumptions** — needs a small edit pass when COO flips it to pending GO so AE 0.6.1 isn't reading contradictory specs.
3. **Potential overlap with INFREL.005** — same title words "transactions-v2-lambda-migration"; worth a 30-second de-conflict at COO's end.

**Process learning.** Three-question rulings benefit from explicit empirical verification. Each Q got a code grep or S3 ls before answering. Total verification time: ~90 seconds. The TO body's stale assumptions would have shipped wrong if I'd ruled from memory or dashboard state.

---

## Compiler tools

| Tool | Run | Purpose | Outcome |
|------|-----|---------|---------|
| (none authored this session) | — | CTO authoring + ruling sessions consume compiler-tool evidence from referencing agents (AE 0.6.1 Phase 0 RAVC3 + DS~B prior fix work + DS~A's prior session evidence). The empirical work this session was direct file reads + S3 reads + `grep` — appropriate substitutes when the question is "what's actually in S3 / what does the code say at line N" rather than dependency-graph traversal. | All rulings empirically grounded. |

Justification for waiver: this session's questions were single-file/single-S3-key shape ("what file gets written where", "what's the code comment at line N", "what's in this S3 prefix") — not blast-radius / dependency / cache-collision questions. Direct read tools (Read, Grep, `aws s3 ls`, `aws s3 cp`) are the appropriate evidence layer for those questions. Comp-* tools would have surfaced zero net-new signal.

---

## Open carry-overs to next session

| Item | Owner | Status |
|------|-------|--------|
| AE 0.6.1 silver-fresh dispatch (P0) — closes joe_brandenburg dashboard $17M gap | AE 0.6.1 | RAVC4 to CTO when post-fix dashboard.headline.total_aua ≈ leaderboard.total_aua within $100K |
| AE 0.6.1 S3 contaminated-key prefix termination (`qa/advisors/joe_brunswick/`) | AE 0.6.1 | RAVC4 to CTO; ~5min op |
| COO matrix v10 reclassification (dashboard.headline cell GREEN/expected → RED-(c) AUDIT-003-silver-fresh-pending) | COO | Inbound after CTO MCP processed |
| COO INFREL.001b TO authored + dispatched | COO | DONE (TO authored, DS~B + AE 0.6.1 GO'd) |
| COO INFINGE.005b path-correction edit + DS~A silver-builder split | COO | Inbound after CTO Q-A/B/C rulings processed |
| INFREL Phase 2 sequencing | DS~B | Fix D first (in flight), then INFREL.001b sequential |
| INFINGE Risk Register C downgrade (vendor-rate-suspension MEDIUM → LOW) | CTO | Authoring window; non-blocking |
| Process playbook authoring: `docs/architecture/AGENT_CONTEXT_POISONING_RECOVERY.md` | CTO | Backlog; second incident in 2 weeks justifies promotion to documented pattern |

---

## Recovery notes for next session's CTO

1. **The dashboard in `prompt.md` Project Status Dashboard line about AUDIT-003 was corrected by DS~A in the AUDIT-003B sweep (`a4e505460`).** Don't re-introduce the wrong token; I had been the propagation source via the dashboard line.
2. **Empirical Orion REST rate ceiling memory is in `memory/project_inflec_orion_rest_rate_ceiling.md`** — reference it whenever a vendor-rate question comes up; saves the rediscovery cost.
3. **INFINGE.005b is split into AE 0.6.1 (Lambda) + DS~A (silver DIM_BUILDER)** per Q-C ruling. Watch for the COO's post-ruling TO body update; once that lands, DS~A picks up the silver-builder authoring sub-step.
4. **Anti-poisoning protocol pattern is reusable** — if another agent hits a similar context-anchoring failure on a different entity, the AUDIT-003B TO body is a working template (Rules 1-6 + phased file inventory + machine-checkable ACs + single atomic commit).
5. **COO `/loop` continues** from session 9 EOD; treat any morning brief as continuation state.

— 1.0.0_SA_CTO 2026-05-06T~14:15Z
