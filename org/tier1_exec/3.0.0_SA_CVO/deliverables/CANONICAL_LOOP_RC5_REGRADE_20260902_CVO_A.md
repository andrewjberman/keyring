# Canonical loop RC5 re-grade -- CVO~A (second-pass final)

> **CURRENT VERDICT: RC5 GREEN.** Second-pass implementation `03cf4d17ac`
> satisfies the inert-collection, execution-parity, and end-to-end production
> mutant bar. This final ruling supersedes both the premature first-pass GREEN
> and the subsequent PARTIAL below.

**Date:** 2026-09-02  
**Final order:** CloudComp message 92712; CVO Base corroboration 92722
**Final implementation pinned:** `03cf4d17ac689274909b4bb541ac21e57f775193`
**Final battery blob:** `338e9db5b846c2c4e48ad018150953b0dae16a7c`
**First-pass implementation:** `e66d5e698d6ea99af959a9c9d6ec7178d5877f47`
**Parent review:** `CANONICAL_LOOP_ADVERSARIAL_REVIEW_20260902_CVO_A.md` @ `af981709a1`  

## Second-pass final re-grade -- GREEN

- Static AST inspection finds zero module-scope executable calls. A direct
  import with `subprocess.run` patched to raise completes with `RESULTS=[]`,
  `_RAN=False`, and `_WS_CACHE=None`.
- `python -m pytest --collect-only -q` exits 0 with exactly one collected test
  in `0.05s`; independently measured wall time is `1.746s`, below the ruled
  five-second ceiling.
- `python -m pytest -q` exits 0 with `1 passed in 108.30s`. Work is therefore in
  execution, not collection.
- Direct mode exits 0 with `STAGE-4 PACKET BATTERY: 7/7 PASS (denominator 7)`;
  all original arm ids remain present in their original order.
- Independent production mutant: in a temporary copy only, the unique
  `return txt, None` at `.tools/comp-adversary:289` was changed to
  `return "", None`. With `COMP_ADVERSARY_TOOL` pointing at that copy, the
  standard pytest path exits 1 and reports `DIGEST-CONTENT` as the sole failed
  arm (`1 of 7`, zero comp-read banners and zero SHAPE panels).
- The unmutated production tool's SHA-256 is identical before and after the
  mutant run:
  `c4a60f042c01f605c6a2275955a6ee2832b58a4e8036f2275d3e58b8b755d553`.
  The temporary file is removed and the production/test paths are worktree
  clean.
- `ruff check` and `py_compile` pass on the final battery.

Release condition 5 is satisfied. `comp-adversary` may receive an effective
runnable disposition and its mandatory-core step-6 admission seam may lift.
This does not close the broader efficacy audit row and does not lift the whole
canonical-loop/ETFS hold: RC7 remains open, and the separate step-6 PRD
manifest/staged-register limb remains PARTIAL under `d019922d68`.

**Initial verdict (withdrawn):** **RC5 GREEN.** The standard runner now collects and executes the comp-adversary battery with a real denominator, while direct mode retains the original seven-arm contract and the pytest entry point fails on a red arm.

## Independent evidence

- `python -m pytest --collect-only -q .tools/tests/test_comp_adversary_stage4_packet.py` exits 0 and reports exactly `1 test collected` (`test_all_arms_pass`).
- `python -m pytest -q .tools/tests/test_comp_adversary_stage4_packet.py` exits 0 and reports `1 passed`.
- `python .tools/tests/test_comp_adversary_stage4_packet.py` exits 0 and reports `STAGE-4 PACKET BATTERY: 7/7 PASS (denominator 7)`.
- The direct run exercises and passes `DIGEST-CONTENT`, `DENOMINATOR`, `EXCLUSIONS-5`, `OPEN-MODE`, `MUTANT-NO-DIGEST`, `NEGATIVE-CONTROL`, and `MECE-PARTITION`.
- A forced-failure control compiled the exact committed `test_all_arms_pass` function with one synthetic `FAIL` row. It raised `AssertionError` and reported `stage-4 packet battery arms failed (1 of 1)`, proving the added pytest denominator is failure-sensitive rather than nominal.
- `python -m py_compile .tools/tests/test_comp_adversary_stage4_packet.py` exits 0.
- The pinned diff changes only module-final reporting and entry-point structure: the module-scope `sys.exit` becomes `_report()`, `test_all_arms_pass()` is added, and direct exit is guarded by `if __name__ == "__main__"`. None of the seven arm bodies changes.

## T-16 corrective re-grade

The collection count was correct but insufficient. The same independent run
reported `1 test collected in 111.95s`. CTO and CVO Base independently measured
131.9s and 135.14s. Source inspection at the pinned implementation explains the
clock: `WS = subprocess.run(...)` at module scope and, critically,
`OUT = run(["compose", ...])` at module scope execute the battery while pytest
imports the file. `test_all_arms_pass()` only grades the `RESULTS` that import
already populated.

That violates the P0.1 battlefield contract adopted for the efficacy project:

- collection and execution must be reported separately;
- module-scope unbounded subprocess work must be caught; and
- each important green needs a red-first mutant or negative control.

A 90-second collection ceiling was independently killed with no output and
exit 124. Thus the repair changed collector death into a long import that still
looks hung or dead to a runner with a lower ceiling. Collection is not inert and
cannot be distinguished from execution.

The forced-failure control in the initial re-grade proved only that the isolated
`test_all_arms_pass()` assertion rejects a synthetic `FAIL` row. It did **not**
plant a defect in the production tool and demonstrate that the standard pytest
invocation turns red. The FWD-6/T-16 end-to-end mutant limb therefore remains
unevidenced.

### Surgical acceptance bar

1. Import and `pytest --collect-only` perform no comp-adversary compose work and
   finish in under 5 seconds with one collected test.
2. The collected pytest test performs the seven-arm work and passes; direct mode
   remains 7/7 with the same arm semantics.
3. A planted production-tool mutant is selected by the standard pytest path and
   makes pytest fail. The unmutated tool then passes under the identical command.
4. The diff remains confined to the battery's execution/reporting boundary; no
   production behavior or test-arm meaning changes.

## First-pass corrected release effect (superseded by second pass)

Release condition 5 is **not yet satisfied**. Collector death is fixed and the
existing substantive arms are green, but inert collection and the end-to-end
mutant proof remain open. `comp-adversary` effective admission and the
corresponding step-6 seam remain held.

At that vintage RC2 and RC4 were also red/partial. They were subsequently graded
GREEN under `d019922d68`; RC7 and the separate step-6 limb remain open.

-- 3.0.0_SA_CVO~A
