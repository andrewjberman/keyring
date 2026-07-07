# VERIFY #06 -- target: B_01b.classify_new_securities.py

- is_real: **True**
- confidence: **confirmed**
- corrected_severity: high

## Reasoning
REAL defect, not refuted. Traced a concrete end-to-end triggering path with every code link verified.

UNGUARDED LOOP (confirmed): In B_01b.classify_new_securities.py the only try/except (lines 300-305) wraps just call_openai and ends with `continue`; the `for result in results:` loop (307-343) is at the same indent level, OUTSIDE the guard. Any exception in the loop body propagates out of the bare main() call (line 367) -> non-zero exit.

LINE 312 float coercion (confirmed): `confidence = float(result.get('confidence', 0.0))`. `result` is a raw dict from json.loads inside call_openai, which returns `parsed.get('results', [])` with NO per-field validation/coercion. dict.get's default fires only for a MISSING key -> a present `"confidence": null` returns None -> float(None) -> TypeError; `"confidence": "high"/"n/a"` -> float(...) -> ValueError. This line runs for EVERY result, before any validity gate. The call uses response_format={'type':'json_object'} which is OpenAI JSON MODE (guarantees valid JSON only), NOT strict json_schema (which is not used) -- so the model (gpt-5.4-mini) can legally emit a null/non-numeric confidence. The reviewer's Python semantics are correct.

LINE 316 secondary crash (confirmed, weaker): `r_name = result.get('asset_name','')` is None when the model echoes `"asset_name": null`; the invalid-asset_class branch does `r_name[:40]` -> TypeError. That branch is commonly hit because the check is case-sensitive lowercase set membership ({'equity','fixed_income','alternatives'}), so `"Equity"`/`"equities"`/`"cash"`/null all enter it. Needs two field deviations, so secondary to line 312.

BLAST RADIUS (confirmed via gold_dispatch.sh): CATALOG line 86 runs B_01b with --upload; daily `--chain full` -> UPLOAD mode -> loop executes (dry-run returns at line 278 first). B_01b runs at PHASE_B3 (lines 410-412); wait_phase (352-359) detects any non-zero child and does `exit 1` ("FATAL ... aborting chain"). So a single malformed LLM field aborts before B_02/B_03/C_*/D_* -> entire cot served platinum stales for the night. It is a hard-fail compute step, not a tolerated API-pull step (run_script has no timeout/tolerate).

REFUTATION ATTEMPTS ALL FAILED: (a) no upstream sanitization -- call_openai returns raw model results; (b) json_object mode does not enforce field types; (c) .get('confidence',0.0) does not protect against present-but-null; (d) UPLOAD is the scheduled production path; (e) the crash genuinely hard-fails the whole chain. The only non-deterministic link is whether the model emits a null/non-numeric field, but that is documented real behavior of non-strict JSON mode and the code has zero defense, so it is when-not-if over nightly runs across many securities.

Severity high (borders critical): trivially-missing guard + whole-firm nightly served-staleness blast radius, offset by a probabilistic (not every-run) trigger. Minimal fix: wrap the per-result body in try/except (increment total_errors + continue), and coerce defensively (e.g. `float(result.get('confidence') or 0.0)` inside the guard, `(result.get('asset_name') or '')`). Same loop also crashes if a `results` element is a bare string instead of an object (AttributeError on .get) -- same defect class, reinforcing the fix.
