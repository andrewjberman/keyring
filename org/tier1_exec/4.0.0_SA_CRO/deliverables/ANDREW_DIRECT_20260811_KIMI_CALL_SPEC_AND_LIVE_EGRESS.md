# ANDREW-DIRECT 2026-08-11 (~08:1xZ, CRO~B terminal) -- SPEC THE KIMI API CALLS + PROMPTS, ONE AT A TIME, WITH LIVE CALLS

**Recorded by:** `4.0.0_SA_CRO~B` · **Status:** SOVEREIGN. Verbatim. Broadcast to CTO + COO + MSTR + CVO same turn.

## 1. VERBATIM

> Now I need you to spec out the api calls and associated prompts for Kimi. We should have expansive
> prior art for this in terms of the api call structure, i want to go through with you one prompt/api
> call at a time starting with the inputs for prompt/call #1 which should be the F1 F2 F3 F4 inputs and
> friction axes. Let's make sure we have a canonical form for this, establish it with a live call and
> response, assess quality of response and move to the next.

## 2. WHAT THIS ESTABLISHES

- **CRO~B specs the Kimi SVP API calls + prompts, sequentially, call #1 first** (the F1-F4 friction-axis
  call). Method: establish a canonical form -> LIVE call+response -> quality assessment -> next call.
- **VENDOR-EGRESS AUTHORIZATION (per-use, this instruction):** live calls to Kimi (Moonshot,
  `https://api.moonshot.ai/v1/chat/completions`, model `kimi-k3`) for this spec work are AUTHORIZED by
  this instruction. This is a per-use grant scoped to the Kimi-SVP spec work; it is NOT a standing lift
  and does NOT extend to any other vendor. Payloads are estate-STRUCTURAL (vertical names, path counts,
  heat scores, co-movement pairs) -- the same data class production already sends to Kimi; no client
  data. (The pipeline already carries a standing Andrew-direct per-use Kimi designation for its own
  fires; this authorizes the spec-time exercise of it.)

## 3. PRIOR ART GROUNDED (the "expansive prior art" he referenced)

- **API-call template:** `infra/aws/ec2/estate-report-runner/estate_report_runner.py:1572` `call_kimi_sub`
  -- single user message, `temperature=1` (MANDATORY for kimi-k3, else HTTP 400), per-kind `max_tokens`
  (`KIMI_BUDGETS`) + timeout (`KIMI_TIMEOUTS`), Bearer auth from Secrets Manager `astn/kimi/api-key`,
  JSON output (fence-stripped), full pre-call telemetry (survives timeout), per-kind retry semantics.
- **Prompt house style:** `build_narrate_prompt` / `build_detect_prompt` / `build_author_prompt`
  (`:1434-1529`) -- role framing + scope, `=== SECTION ===` evidence blocks each carrying its
  denominator + vintage + "SAMPLE not the set" honesty, an explicit `Return ONLY JSON: {schema}`,
  HARD CONSTRAINTS "enforced by the runner not by trust", honest-empty affordance, an evidence-status
  enum (MEASURED / INFERRED / UNMEASURED / NOT_MEASURABLE), ASCII-only.
- **Call graph (deployed subdivision, @959236f60d):** Call 0 deterministic compile -> Wave 1
  (NARRATE + DETECT x group) -> Wave 2 (AUTHOR per candidate). **That subdivision is the semantic-DRIFT
  pipeline; the F1-F4 FRICTION axis is a DISTINCT call that does not exist in the runner yet** -- which
  is what this spec adds: a new `friction` kind on the same proven `call_kimi_sub` structure.
- **Friction battery spec:** `docs/architecture/OPAL_KIMIPIPELINE_STATE_FRICTION_DESIGN.md` s.3 (F1 blast
  overlap / F2 heat trajectory / F3 operator signal / F4 co-movement), s.8.1 partition (instruments
  MEASURE, Kimi TRANSLATES+PROPOSES, Andrew ASSERTS), s.13 (F1 unbuildable until the deterministic
  composition exists; C3.ii/STATE deferred -- so call #1 is the FRICTION characterization, not STATE).

## 4. DESIGN PREMISE FOR CALL #1 (flagged, not asserted -- his to confirm)

Per s.3 the F1-F4 battery is DETERMINISTIC (runner + comp instruments), and Kimi's role (s.8.1) is to
TRANSLATE. So **call #1 = Kimi reads the deterministic F1-F4 battery and produces the per-vertical
FRICTION CHARACTERIZATION** (is this vertical heating / spreading / consolidating / being abandoned, and
in which direction), grounded strictly on the cited F-figures. STATE (lifecycle_value) is the NEXT axis
and is deferred per s.13. If call #1 was meant to be something else, that redirects before we go deep.

## 5. LIVE-EXERCISE STATE (honest, current build)

F2 (comp-heat) + F4 (comp-cochange) are READY and computed real. F1 (blast over composed C3.i
structures) is UNMEASURED -- the deterministic composition it needs is unbuilt (s.13). F3 (operator
signal) is UNMEASURED -- the capture uploader (B6) is unbuilt (s.9.1). So the first live battery is
2-of-4 measured + 2 declared-degraded (the residue-degraded mode s.8.3 already specifies) -- which is
the true state AND a faithful test that Kimi handles a partial battery honestly.
