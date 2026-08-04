# KIMI_EMPTY — DIAGNOSIS (mechanism proven by exercise, 2026-08-04 ~05:1xZ)

**Authority:** Andrew startup approval (via MSTR relay 20260804T050242Z, verbatim "yeah its
approved by me i want that started up"); diagnosis = sanctioned step 1 of the close path
(@f022ca3e0). Egress: 2 minimal calls to the pipeline's own endpoint/model/secret
(api.moonshot.ai / kimi-k3 / astn/kimi/api-key) — the pipeline's Andrew-direct per-use
designation (instance.tf:39-40), re-affirmed by the startup approval. ~230 tokens total.

## MECHANISM (source-confirmed + exercised)

**kimi-k3 is a REASONING model. It emits `reasoning_content` before `content`, and
`max_tokens` bounds BOTH. When the budget is consumed by reasoning, the API returns 200 with
`finish_reason="length"` and `content=""` — which the runner's parser
(`estate_report_runner.py:748-752`, reads only `content`) records as KIMI_EMPTY.**

Probe evidence (both directions, isolated invocations):

| probe | result |
|---|---|
| trivial prompt, max_tokens=4000 (positive control) | `finish_reason=stop`, `content='OK'`, `reasoning_content` PRESENT (20 reasoning tokens) |
| same prompt, max_tokens=10 (failure reproduction) | `finish_reason=length`, **`content=''`**, reasoning consumed the budget — **byte-identical to the production symptom** |

Production fit: the run's prompt is ~60KB (`build_prompt` truncates resources at 60,000
chars, `:703`) with `max_tokens: 4000` (`:732`). A reasoning model spends heavily on a prompt
that size before answering; both attempts starve identically, which explains the x2
consistency. RESIDUAL, stated honestly: the production run's own `finish_reason` was never
persisted (the empty-success path discards the body — instrument gap, below), so the
production instance is INFERRED-from-proven-mechanism until the first re-run with logging
confirms it. No other candidate mechanism survives the probes (auth, model id, endpoint,
temperature all positively controlled by probe 1's success).

## INSTRUMENT GAP (second finding, same class the code already banked once)

`call_kimi`'s HTTPError branch captures the response body ("CAPTURE THE BODY, NOT JUST THE
CODE", `:756-767`); the EMPTY-SUCCESS branch does not — on empty `content` it logs only
"KIMI_EMPTY" and discards `finish_reason`, `usage`, and `reasoning_content` presence. The
lesson was applied to the error path and not the empty path; this diagnosis took a live probe
that one logged field would have made unnecessary.

## FIX SPEC (for the builder — ~B lane)

1. **Raise `max_tokens`** to give the content phase headroom past reasoning (recommend 16384,
   or the model max; 4000 is a chat-sized default applied to a reasoning workload — the same
   inherited-parameter class as the 120s timeout, `:62-77`).
2. **Log the body on empty content**: `finish_reason` + `usage` (incl.
   `completion_tokens_details.reasoning_tokens`) + reasoning_content presence/length. The
   empty-success path gets the same body-capture discipline as the error path.
3. Do NOT read `reasoning_content` as the answer (advisory diagnostics only — the contract
   stays: proposals come from `content`).
4. Re-run ad-hoc (QA instrument, permitted) → expect a populated AI section; the re-run's
   logged `finish_reason=stop` + non-empty content is the confirmation that closes the
   production residual above.

## Verification hooks (CVO holds)

- Acceptance on the fix: the re-run report carries a real AI section AND the new empty-path
  logging exists (exercise it with a deliberately tiny max_tokens in a test invocation — the
  control must FIRE on the defect event).
- Then: _EPOCH write + scheduler enable per close-path steps 5–6.
