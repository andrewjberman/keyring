# work_2335Z_b_lane_spawn_phase2a_011_ac3_gold_scoring_ship
**archetype:** IMPLEMENT
**secondary_archetypes:** SCRIBE

## Spawn moment

MSTR-DIRECT SPAWN-WITH-DIRECTION 2026-05-27T~23:35Z per Andrew direct 23:25Z "parallelize: bring on 3 or 4 more DS." Scoped task per spawn-msg:

> FIND_INSURE Phase 2A gold scoring + LushaAI structure. STEP 3: scope = score_linkedin_gold.py employee scoring (.011 AC3) + LushaAI response shape ratify for gold-tier discrimination.

This is a parallelization split of `FIND_INSURE.011` (originally a 5-deliverable bundle for DS~C): ~B (this session) takes AC3 gold-side; ~C retains AC1 (crawl) + AC2 (parse, already shipped) + AC4 (lusha_client utility) + AC5 (opt-out webhook).

## Cycle 1 timeline (~28 min wall, 23:35Z → 00:03Z)

| Time | Step |
|---|---|
| 23:35Z | spawn, /watcher self-heal (PID 28552 LIVE; task `b6h4de1tm` tracked watcher) |
| 23:36Z | CronCreate /work 20m armed (job `1ac8fdb6` 7,27,47 cadence) |
| 23:36-23:45Z | Read CLAUDE.md + org/XXX.md + README + prompt.md + FIND_INSURE PRD v0.7 + .011 TO + .006 sister TO + project JSON + scoring-weights-v0.1.json + ws CTO Phase 2A design brief + parse_linkedin_silver.py (input contract) + lusha-api-v3.md |
| 23:45-23:55Z | Author score_linkedin_gold.py (720 LOC) + test suite (9 test functions, 50+ cases) |
| 23:55Z | First test run — 2 fails (Vice President / Executive Vice President wrongly hitting c-suite via bare `president`); patched _SENIORITY_PATTERNS precedence (evp_svp + vp_director checked before bare-president c-suite fallback) |
| 23:57Z | All 50+ test cases PASS |
| 23:58Z | Author Lusha-shape gold-discrimination ratify brief |
| 23:59Z | ds-commit-gate.sh CLEAN on both .py files |
| 00:00Z | safe-commit.sh --force (multi-agent index contention; CVO+AE+DS lanes concurrently staging) → commit `6457f6861` lands |
| 00:01Z | watcher-exit fired (inbound from DS~C); relaunched tracked watcher; ACK'd DS~C sister-coord with ownership-boundary clarification (taxonomy=~B, weights=~E) |
| 00:03Z | [RAVC2-Request] FIND_INSURE.011 AC3 dispatched to ws COO + [CC RAVC2] to ws CTO |

## Files Modified

| File | Change |
|---|---|
| `data/find/imo/scripts/gold/score_linkedin_gold.py` | NEW — Phase 2A gold scoring Lambda skeleton (~720 LOC) |
| `data/find/imo/scripts/gold/test_score_linkedin_gold.py` | NEW — 9 self-test functions / 50+ cases all PASS |
| `docs/briefs/find-insure-phase2a-lusha-shape-gold-discrimination-ratify-20260527.md` | NEW — Lusha v3 response shape ratify for gold-tier discrimination (named-individuals HIGH + Series-license counts MEDIUM-HIGH + AUM extraction MEDIUM) |

## Module design (score_linkedin_gold.py)

Three gold-tier discriminators per .011 AC3 + scoring per E1 `scoring-weights-v0.1.json`:

1. **Named-individuals pass-through** — `contact_id` + `fullName` + `linkedinUrl` preserved verbatim from silver per Rule 17.
2. **Series-license detection** — regex `\b(?:series[\s-]?|s)(\d{1,3})\b` across `certifications[]` + `currentPosition.{title,description}` + `previousPositions[*]`; 40-char downstream negation-window suppresses retired/lapsed/inactive/expired/formerly; valid-code allowlist `{6,7,22,24,26,51,52,53,63,65,66,79,82}` matches E1 series_license_weights.
3. **AUM number extraction** — regex on bio/description with AUM-context proximity gate (80 chars); $M/$B/$K + comma-thousands; returns max + evidence list.

Employee scoring per E1:
```
employee_score = (tenure_normalized * 0.25)
               + (seniority_class_weight * 0.25)
               + (series_license_count_weighted * 0.30)
               + (title_keyword_match * 0.20)
```

Seniority taxonomy (8 classes) with precedence ordering — founder/owner first (single-decision-maker class per E1 O-6 ratification), then c-suite SPECIFIC (Managing Director + Chief X Officer + CEO/CFO/etc.), then evp_svp (consumes Executive/Senior Vice President + EVP + SVP), then vp_director (Vice President + VP + Director + Head of + Partner + Principal), then bare-president as c-suite-catchall, then manager, then ic, then other.

Company aggregate (Phase-2A-only sub-score):
```
company_score_linkedin = 0.5 * max_employee_score
                       + 0.3 * series_licensed_normalized
                       + 0.2 * mean_employee_score_top5
```
Cross-channel join (Phase 1 web + Phase 2A LinkedIn + Phase 2B jobs) lives in Phase 3 `build_companies_serving` per E1 company_score formula — this module does NOT double-count.

## Test coverage

| Function | Cases | Notes |
|---|---|---|
| test_classify_seniority | 18 | founder/owner/c-suite/evp_svp/vp_director/manager/ic/other variants + None/empty |
| test_detect_series_licenses | 3 | multi-code positive + retired-negation + invalid-code filter |
| test_series_license_count_weighted | 2 | weighted sum + empty set |
| test_extract_aum_usd | 7 | $M/$B/multi-amount-max/no-context-rejected/None/empty |
| test_parse_tenure_and_normalize | 7 | YYYY-MM-DD + ISO-8601 + missing + cap/floor |
| test_title_keyword_match_indicator | 4 | substring match + no-match + None |
| test_score_employee_full | 12 | high-signal CIO (~0.74) + low-signal Insurance Agent (~0.16) end-to-end |
| test_aggregate_company | 5 | 3-employee mixed rollup |
| test_handler_stub_end_to_end | 9 | full Lambda handler stub-mode against in-memory silver fixtures |

`python test_score_linkedin_gold.py` exits 0. Fixture-driven; no live S3 calls.

## Discipline

- **Rule 14** (ds-commit-gate.sh): CLEAN on both .py files (py_compile + ds-precommit-check.py + ruff py39).
- **Rule 15** (from-future-annotations): first import on both .py files.
- **Rule 14a** (safe-commit.sh): `--force` invoked due to multi-agent shared-index contention. FORCE-BYPASS audit logged. `git commit --only` structurally scopes commit to declared pathspec regardless of other staged files.
- **Rule 17** (silver passthrough preservation): module READS silver per the parse_linkedin_silver schema, applies business-logic at GOLD tier — exactly where it belongs per [[feedback_silver_no_field_slimming]].

## Compiler Tools

| Tool | Run | Notes |
|---|---|---|
| `comp-pipescript io` | `comp-pipescript io data/find/imo/scripts/gold/score_linkedin_gold.py` | Reports "Unknown script" — new file not yet in comp-graph; AE 0.7 owns FIND_INSURE.003 comp-graph registration of data/find/imo/ subtree. Expected pre-AC10-gate state per .006 sister precedent. |

## Inbound this cycle

- DS~C [SISTER-COORD] FIND_INSURE.027 AC3 draft — ACK'd at 00:01Z with ownership-boundary clarification (term-taxonomy=~B; scoring-weights=~E) + heads-up on AC3 ship.

## Outbound this cycle

- [RAVC2-Request] FIND_INSURE.011 AC3 → ws COO (broker + filesystem delivery)
- [CC RAVC2] → ws CTO (design-authority + brief-author CC per LD-0084-style eager-pre-positioning)
- [SISTER-COORD ACK] → DS~C

## LD-0116 routing posture

Spawn-msg said "RAVC2 ws COO + CC MSTR on ship." Per LD-0116 (sovereign Andrew 2026-05-27T~17:36Z) chain-of-command: T2/3 ↔ MSTR direct comms = NEVER. I routed to ws COO only; COO surfaces to MSTR per fabric protocol if warranted. Noted explicitly in RAVC2-Request body for transparency.

## Next Steps

1. **[ws COO]** RAVC2-ACCEPT or RAVC2-ACCEPT-with-additives verdict on FIND_INSURE.011 AC3.
2. **[ws CTO]** CORROBORATE/COUNTER/CORROBORATE-with-CONCERN on Lusha shape ratify brief per §5 (soft-fix candidate: `aum_self_reported_extracted_usd` column-naming downstream).
3. **[CVO 3.0.0_SA_CVO]** `/verify-channel` Mode A rationale-narrative-class candidate per LD-0095 verification-class taxonomy (mechanical field-mapping bookkeeping; not empirical-smoke-class until real Lusha calls land Phase 2A).
4. **[DS~E]** Heads-up — AUM column-naming recommendation `aum_self_reported_extracted_usd` (not `aum_usd`) may inform Phase 3 `serving/employees.{json,parquet}` column-naming.
5. **[DS~C]** Coordinate bundle shape — .011 remaining scope = AC1 + AC2 (already shipped) + AC4 + AC5; AC3 closed by this cycle.
6. **[AE 0.7 / FIND_INSURE.003]** Comp-graph registration of `data/find/imo/scripts/gold/score_linkedin_gold.py` for `comp-pipescript io` + `comp-pipescript deployed` AC10-equivalent post-Phase-1-RAVC2-Accept.
7. **[~B self-loop /work 20m]** Cron `1ac8fdb6` armed at 7,27,47 cadence; next tick consumes COO verdict + acts on any follow-on TOs.

— 0.1.0_DS_MarketIntelligence~B 2026-05-28T00:04Z
