# F10 hygiene: hold-era suite repaired to post-lift truth + F9-gate enrollment FIRED + the 91-file census (5 more F10-class reds NAMED) -- 0.8.0_AE_CloudComp~D

**archetype:** IMPLEMENT

Window: 2026-08-04 ~1710Z -> ~1745Z. TO `ADHOC.graph-tests-hygiene-f10` (COO GO 171151Z, pulled
forward on Andrew "Proceed" 1706Z). Landed @3e2da967b.

---

## Part 1: the repair (test_extract_column_gaps_bd_hold.py)

- **Pre-fix control:** 3 red reproduced exactly (rc=1 pipe-free) -- hold-era assertions (bd/schwab
  SKIPPED) against the correctly-lifted engine (SOVEREIGN_HELD_PATHS=() per the 07-14 retraction
  + CTO 07-22 predicate split). The ENGINE was right; the TESTS were stale.
- **Repair shape (CVO's verbatim intent):** post-lift truth asserted (bd READS like inf); the
  guard MECHANISM tested against INJECTED synthetic held values -- monkeypatch on
  `sovereign_held.SOVEREIGN_HELD_PATHS`, which `is_held_path` resolves at CALL time (grounded:
  `sovereign_held.py:114`; substring semantics `:80`); include_held_override io-threading
  exercised UNDER the injected hold. Marker is SYNTHETIC (`synthetic_held_zone_f10`) -- the test
  never re-asserts governance.
- **Discrimination proven:** throwaway neutered-guard engine mutant (`if False and ...` at
  extract_pipeline.py:1002, uncommitted) -> both mechanism tests FAIL; reverted byte-clean ->
  3/3 green. No landed engine edits.

## Part 2: F9-gate enrollment -- proven by FIRE, not glob-read

Exact-path entry added to WATCH_GLOBS in `.tools/git-hooks/pipescript-suite-check.sh` -- the ONE
derivation point (trigger predicate AND suite invocation both derive from it; commented with TO
+ dial F10). The landing commit @3e2da967b staged the test file and **the gate FIRED on it**:

```
[pipescript-suite-gate] watched path staged -- running the comp-pipescript suite (7 files) ...
[pipescript-suite-gate] OK: 54 passed in 30.32s
2026-08-04T17:27:22Z  PERMITTED  author=0.8.0_AE_CloudComp~D  files=7 result='54 passed in 30.32s'  trigger=org/modules/graph/tests/test_extract_column_gaps_bd_hold.py
```

Suite denominator 51 -> 54, files 6 -> 7.

## Part 3: the census (predicate-not-roster -- derived from the gate file itself)

Method: WATCH_EXACT/WATCH_GLOBS parsed from the gate script at census time (single source, no
hand copy); every `org/modules/graph/tests/*.py` matched against the same predicate + pytest
`--collect-only` per file.

**DENOMINATOR: 91 test files | 7 WATCHED / 84 unwatched | 90 collect-clean / 1 BROKEN.**
(Full 91-row table emitted in-session; reproduce with the parser above.)

- **BROKEN (1), NAMED to CTO~B's RCG lane, not fixed here:** `test_adapter_audit.py` -- imports
  `adapter_audit_cli.py` which no longer exists (mass-deletion residue); any whole-dir pytest of
  tests/ dies at collection.
- **comp-depth test files in the census: ZERO exist** -- nothing to note-and-defer for CVO's
  open comp-depth dial.
- **The 84 unwatched files are NOT per-file defects** -- F9's gate is deliberately scoped to the
  comp-pipescript suite. The family-level reading: any unwatched file that oracles a LIVE
  instrument has no commit-gate runner and can rot F10-style when its engine moves. Routed as a
  family observation, not fixed.

### >> NEW FINDING (named, not fixed): 6 MORE F10-class stale-reds in 4 sibling files <<

Collection health is not RUN health, so the census was extended with one targeted run of the
10-file held/bd_hold sibling family (the exact F10 class): **rc=1, 6 failed / 44 passed**,
grep ^FAILED verbatim:

```
FAILED test_comp_secrets_bd_hold.py::test_consumers_excludes_bd_and_schwab_by_default
FAILED test_freshness_manifest_gen_bd_hold.py::test_is_held_predicate
FAILED test_freshness_manifest_gen_bd_hold.py::test_bd_config_held_by_default_reads_under_flag_nonvacuous
FAILED test_incrparity_cli_bd_hold.py::test_bd_blocked_for_agent_by_default
FAILED test_platinum_held_path_guard.py::test_guard_prevents_read_on_a_held_bd_path
FAILED test_platinum_held_path_guard.py::test_held_path_hit_is_a_pure_string_check_never_opens
```

Same superseded-contract class as F10, silently red, unwatched by any gate. **NOT repaired
here** (lane discipline, and each needs per-file truth-grounding: `incrparity_cli`'s
sovereign_held guard was DELETED at f9ddda52f -- retired-not-lifted is a DIFFERENT target truth
than F10's lifted-but-mechanism-retained; comp_secrets/platinum/freshness_manifest need their
own mechanism reads). Routed to CVO for fold/re-dial routing with this capture.

## Compiler Tools

| Tool | Invocation | Result vs expect |
|---|---|---|
| pytest | pre-fix control (pipe-free rc) | 3 red reproduced = expect PASS |
| pytest | post-fix | 3 green = expect PASS |
| pytest | neutered-guard mutant run | 2 mechanism tests FAIL -> revert -> 3 green (discriminates) = expect PASS |
| commit-gate.sh | repaired .py | rc=0 clean |
| F9 gate (own build) | fired on landing commit | 7 files / 54 passed, audit line 17:27:22Z = enrollment PROVEN |
| census parser | 91 files vs gate predicate + collect-only | full denominator, 1 broken, 0 silent drops |
| pytest | 10-file held-family run | 6 failed / 44 passed -- the NEW F10-class finding |
| sovereign_held ground reads | is_held_path :114, _path_matches :80, split doctrine :30-60 | mechanism grounded before repair design |

## Blockers
None.

## Next Steps
- **[3.0.0_SA_CVO]** verify the repaired file per dial scope; fold/route the 3 new stale-red
  sibling files (per-file truth differs -- incrparity is retired-not-lifted).
- **[1.0.0_SA_CTO / CTO~B]** adapter_audit stays with the RCG lane (re-cited).
- **[0.8.0_AE_CloudComp~D]** IDLE after reports; event-driven.

-- 0.8.0_AE_CloudComp~D
