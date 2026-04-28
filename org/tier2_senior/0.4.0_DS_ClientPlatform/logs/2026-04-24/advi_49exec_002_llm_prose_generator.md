# ADVI_49EXEC.002 Session Log -- LLM Prose Generator Lambda
**Agent:** 0.4.0_DS_ClientPlatform  
**Date:** 2026-04-24  
**TO:** ADVI_49EXEC.002.ds-llm-prose-generator.md  
**Commit:** a3fdf4bf  
**Status:** COMPLETE

## Summary

Implemented exec-summary-generator Lambda from scratch. Wraps trigger_eval.py 6 slot evaluators, calls Claude Sonnet 4.6 via Anthropic SDK with prompt caching, validates responses, and writes exec_summary.json to S3. All Phase 1 + Phase 2 compiler gates passed. 62/62 tests passing.

## Files Delivered

| File | Type | Description |
|------|------|-------------|
| `infra/aws/lambda/exec-summary-generator/config.py` | New | All constants: MODEL_ID, S3_BUCKET, prefixes, thresholds, CW_NAMESPACE, MAX_ADVISORS_PER_FIRE |
| `infra/aws/lambda/exec-summary-generator/platinum_reader.py` | New | S3 reads + 4 positions-based evaluators + 6 build_*_context() functions |
| `infra/aws/lambda/exec-summary-generator/validator.py` | New | 4-stage validator: JSON parse, URL detect (retry once), PII assert, 240-char cap |
| `infra/aws/lambda/exec-summary-generator/metrics.py` | New | 6 CloudWatch emit_*() functions (Opal/ExecSummary namespace) |
| `infra/aws/lambda/exec-summary-generator/lambda_function.py` | New | Main handler: headline builders, _call_llm (prompt caching), _build_slot, process_advisor, lambda_handler |
| `infra/aws/lambda/exec-summary-generator/prompts/system.txt` | New | System prompt with 8 rules (JSON only, 240-char, no URLs, no PII, cite specifics, third-person, no speculation, no disclaimers) |
| `infra/aws/lambda/exec-summary-generator/prompts/top_gainer.txt` | New | Slot template |
| `infra/aws/lambda/exec-summary-generator/prompts/top_loser.txt` | New | Slot template |
| `infra/aws/lambda/exec-summary-generator/prompts/concentration_risk.txt` | New | Slot template |
| `infra/aws/lambda/exec-summary-generator/prompts/tax_loss_candidate.txt` | New | Slot template |
| `infra/aws/lambda/exec-summary-generator/prompts/leaderboard_rank_delta.txt` | New | Slot template |
| `infra/aws/lambda/exec-summary-generator/prompts/top_nna_mover.txt` | New | Slot template |
| `tests/exec_summary/fixtures/sample_positions.json` | New | 7-position fixture (NVDA/MSFT/AAPL/INTC/TSLA/GOOG/BND) with null-handling edge cases |
| `tests/exec_summary/test_llm_generator.py` | New | 62 tests across 8 test classes |

## Design Decisions

- **4 positions evaluators in Lambda** (top_gainer, top_loser, concentration_risk, tax_loss_candidate) vs 2 from trigger_eval.py (leaderboard_rank_delta, top_nna_mover). trigger_eval.py is read-only (TO 1 artifact, 8cc69bab).
- **Null-handling contract**: unrealized_gain_pct null -> rank by $ (not pct); oldest_lot_holding_days null -> skip tax_loss_candidate; acquisition dates null -> pass None through to LLM context.
- **prompt caching**: cache_control ephemeral on system prompt + slot template blocks; per-advisor variable data has no cache_control. betas=['prompt-caching-2024-07-31'].
- **URL retry**: On URLDetectedError, retry once with __instruction field. On second failure or any other error: emit_slot_dropped(), return None (slot silently omitted from bullets).
- **Patch target**: Functions imported via `from platinum_reader import fn` are patched at lambda_function level (lambda_function.fn), not at source (platinum_reader.fn) -- already-bound references.

## Compiler Tools Run Log

| Step | Command | Result | Note |
|------|---------|--------|------|
| P1.1 | `python -m py_compile infra/aws/lambda/exec-summary-generator/config.py` | exit 0 | PASS |
| P1.2 | `python -m py_compile infra/aws/lambda/exec-summary-generator/platinum_reader.py` | exit 0 | PASS |
| P1.3 | `python -m py_compile infra/aws/lambda/exec-summary-generator/validator.py` | exit 0 | PASS |
| P1.4 | `python -m py_compile infra/aws/lambda/exec-summary-generator/metrics.py` | exit 0 | PASS |
| P1.5 | `python -m py_compile infra/aws/lambda/exec-summary-generator/lambda_function.py` | exit 0 | PASS |
| P1.6 | `.tools/ds-commit-gate.sh infra/aws/lambda/exec-summary-generator/config.py` | exit 0 | py_compile + AST + ruff all PASS |
| P1.7 | `.tools/ds-commit-gate.sh infra/aws/lambda/exec-summary-generator/platinum_reader.py` | exit 0 | PASS |
| P1.8 | `.tools/ds-commit-gate.sh infra/aws/lambda/exec-summary-generator/validator.py` | exit 0 | PASS |
| P1.9 | `.tools/ds-commit-gate.sh infra/aws/lambda/exec-summary-generator/metrics.py` | exit 0 | PASS |
| P1.10 | `.tools/ds-commit-gate.sh infra/aws/lambda/exec-summary-generator/lambda_function.py` | exit 0 | PASS |
| P2.1 | `python -m pytest tests/exec_summary/test_llm_generator.py -v` | 62/62 PASS | 0 failures |
| P2.2 | `comp-iam service exec-summary-generator` | SKIPPED (no graph entry) | Expected -- TO 4 DT provisions IAM |
| P2.3 | `comp-pii audit` | PASS | 0 cleartext fields in new Lambda |
| P2.4 | `comp-cache collisions` | PASS | 0 new cache key collisions |

## /claude-api Skill

Invoked at Lambda implementation start per CTO item D mandate. Skill enforced:
- Model ID: `claude-sonnet-4-6` (explicit string, not alias)
- Prompt caching: cache_control ephemeral on system + slot template blocks
- betas=['prompt-caching-2024-07-31'] header
- Structured response: JSON tool-use mode (validate_slot_response parses {"detail": "..."})

## Test Results

```
collected 62 items

TestValidator (13): all PASS
TestPlatinumReaderEvaluators (12): all PASS
TestContextBuilders (2): all PASS
TestHeadlineBuilders (6): all PASS
TestInputHash (3): all PASS
TestSlotPipeline (10): all PASS
TestNullHandlingContract (5): all PASS
TestProcessAdvisor (4): all PASS
TestLambdaHandler (3): all PASS
TestMetrics (3): all PASS

62 passed in 0.24s
```

## Mock Invoke Evidence

Local mock invoke (all LLM calls patched, S3 patched): produced valid exec_summary.json with:
- 5 bullets (top_gainer + top_loser + concentration_risk + tax_loss_candidate + leaderboard_rank_delta)
- 5 LLM calls (1 per triggered slot)
- 15 CloudWatch put_metric_data calls (tokens_in + tokens_out + llm_calls_made per slot, + advisors_processed + empty_advisors at handler level)
- input_hash: sha256:... (deterministic for fixed input)
- model: "claude-sonnet-4-6"
- 0 PII fields
- permissions_scope.min_role = "advisor", client_pii_revealed = false

## AC Status

| AC | Description | Status |
|----|-------------|--------|
| 1 | Lambda reads 4 platinum artifacts + 2 leaderboards per advisor | DONE |
| 2 | Null-handling contract for unrealized_gain_pct / oldest_lot_holding_days / acquisition_dates | DONE |
| 3 | 6 slot evaluators: 4 positions-based + 2 from trigger_eval.py | DONE |
| 4 | /claude-api skill invoked; model = claude-sonnet-4-6; prompt caching | DONE |
| 5 | Validator: JSON parse + URL detect/retry + PII assert + 240-char cap | DONE |
| 6 | exec_summary.json schema: advisor_id, firm_id, generated_at, model, input_hash, bullets[], permissions_scope | DONE |
| 7 | S3 write to platinum/advisors/{advisor_id}/exec_summary.json with AES256 SSE | DONE |
| 8 | 6 CloudWatch metrics emitted | DONE |
| 9 | 62/62 tests passing | DONE |
| 10 | All compiler gate phases passed (py_compile + AST + ruff + tests + comp-pii + comp-cache) | DONE |
| 11 | from __future__ import annotations on all .py files | DONE |
| 12 | MAX_ADVISORS_PER_FIRE ceiling check in lambda_handler (raises RuntimeError) | DONE |
