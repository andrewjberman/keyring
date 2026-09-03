# TO-CE-T-17 comp-estate s.4 audit

**Seat:** `0.8.0_AE_CloudComp~H`  
**Order:** `NFRA_COMPEFFICACY.TO-CE-T-17.comp-estate-s4-audit`  
**Window:** 2026-09-03 14:39Z-15:5xZ  
**Code commit:** `be15852e764df27c631c9d410eea0a51cd442264` (LOCAL)  
**Surprise commit:** `718767b608be1d8b44b5168a2c4909dcc477f538` (LOCAL)

## Outcome

Audited the real 62-line `.tools/comp-estate` runpy shim and its engine. The engine now prints
the ratified answer-state tokens for absent, present-zero, partial/blind C(N), and empty-mode N/A
cases. Literal C(N) is carried to `NFRA_C3MATERIALIZE` as `NOT-DECIDABLE`; no ontology membership
is guessed. The `<name>` and default `--resource` chain scans consume shared `_compbudget.py`,
support flag/env/default precedence and deterministic cursors, and distinguish `BUDGET REACHED`
from `WITHIN BUDGET` while retaining execution-only rc 0 at expiry.

The live source denominator was 29 named verticals and 135 chains at snapshot `last_review
2026-07-30`; `cma` is a positive one-chain control and `ceo-digest` is a present-zero control.
The downstream typed Observation_Record rc/heading consumer still parses both controls.

## Verification

- Engine and battery commit gates: PASS, 1/1 each; combined safe-commit gate 2/2.
- Direct battery: 7/7 PASS; seven disposable mutants went red and were removed.
- File-grain pytest: 1 passed, rc 0.
- Directory-grain pytest: rc 3 before collection; pre-existing module-scope `sys.exit(0)` at
  `.tools/tests/test_fabric_check_classify.py:76`; no tests ran. The new file is import-inert.
- Result JSON: parses; identity 7 + disclosure 8 + answer-state 4 + bounds 4 + passcraft 3 +
  usage 5 = exactly 31 required fields; four answer-state keys match the ratified enum.
- Production identity: engine blob `1f646d7c26` -> `8feb1bb38c`; shim blob remains
  `e0bd92509e`.

## Findings carried, not hidden

- C(N) remains a RELIES-ON on active/incomplete `NFRA_C3MATERIALIZE`.
- Rule P remains incomplete: `--head` declares truncation and preserves the true denominator but
  is not `PAGE i of N`.
- Rule T is complete for the audited named/default-resource traversal. The optional refresh,
  verify-served, and aws census modes retain unbudgeted/constant subprocess behavior, disclosed in
  the result rather than widened under this order.
- `comp-passcraft recon comp-estate` mislabels the runpy shim self-contained; this repeats the
  already-recorded S25 detector class.
- The Codex launcher shares one `CLAUDE_CODE_SESSION_ID` across concurrent seats, causing `.to_id`
  last-writer-wins attribution. Filed as `NFRA_COMPEFFICACY-S28` at `718767b608`; usage therefore
  counts by exact tool+serial+rc, never by task id.

## Compiler Tools

| Tool | Invocation / evidence | Result |
|---|---|---|
| `comp-to` | `comp-to NFRA_COMPEFFICACY.TO-CE-T-17.comp-estate-s4-audit` | Set repeatedly; S28 records cross-seat overwrite of the Claude-keyed session carrier. |
| `comp-read` | engine and `org/projects/NFRA_C3MATERIALIZE.json`, exact task prompts | Both required sources read before writing; initial direct wrapper spelling failed, canonical PATH invocation succeeded. |
| `comp-passcraft` | `comp-passcraft recon comp-estate` | Evidence pack only, no verdict; hand-run moves 1-8 completed in the result. |
| `comp-estate` | `--list`, `cma`, four state cases, flag/env budget controls, cursor control | 29/135 source denominator; four distinct states; Rule T completion/expiry discriminated. |
| `commit-gate` | engine and new battery, separately and through safe-commit | PASS. |
| `proof-of-spec-check` | T17 instance against `T17-AC1..T17-AC6` | Required before complete flip; final result recorded in proof. |

## Usage snapshot

At 2026-09-03T15:48:19Z the exact run sink contained 316 30-day `comp-estate` rows. The
rail log contained 2,080 mentions but zero `tool=comp-estate` execution rows. Executable hook
census found advisory HUD text and zero hook invocations, so hook-driven traffic is 0/316. The
full mode/caller breakdown is in `comp-estate.result.md`.

## Placement

Per issuer message 93728, this seat never pushes. Push state is reported as LOCAL with the remote
head measured in the proof/report. FWD-9 was requested from the COO after the production commit;
the independent seat receipt is appended to the proof before completion.
