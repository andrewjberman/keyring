# 0.7.0_AE_CloudOps~B -- ADHC_COMMITGATE: fork-consolidation + rename off "ds-commit-gate.sh"

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

Window: ~1520Z -> ~1600Z, per COO DRIVE GO (MSTR-relayed CTO arch-gate APPROVED, Andrew-direct
origin), sequenced before NFRA_CMTQUE.TO-6R's load-test.

## Summary

`.tools/ds-commit-gate.sh` forked ~6 python subprocesses per file (py_compile, ds-precommit-
check.py, ruff, comp_constants_cli.py, manifest_check_cli.py, log_open_lint.py) -- a 10-file
commit forked ~60 processes, the likely dominant fork-volume source stressing the Huntress
EDR process per Andrew's diagnosis. Replaced with `.tools/commit-gate.sh` -> a new
`.tools/commit_gate_runner.py`: ONE long-lived python process that calls the SAME functions
each standalone script's own CLI wrapper calls (not a reimplementation) -- `scan_file()` /
`cmd_check()` / `cmd_scan()` / `main(argv=[...])` -- directly, in-process. Only `ruff` stays a
subprocess (one per `.py` file; no stable public Python API exists to eliminate it without
coupling to internal, unversioned bindings against the CLAUDE.md-pinned `ruff==0.15.11`
contract). Renamed off "ds-commit-gate.sh" (the gate is universal/ANY-lane, never DS-specific)
per CTO condition 3.

**Fork-count reduction (AC2):** 6 forks/file -> 1 fork/file (ruff only) + the single runner
process. A representative 10-`.py`-file commit: 60 subprocess forks -> 11 (1 runner + 10 ruff
calls) -- an 82% reduction. A 5-file mixed commit (4 `.py` + 1 in-scope `.sh`): 26 -> 5.

## Design rationale (why this is safe for parity -- CTO condition 1)

Read all 5 target scripts top-to-bottom BEFORE writing any consolidation code (`ds-precommit-
check.py`, `comp_constants_cli.py`, `manifest_check_cli.py`, `log_open_lint.py`, `shell_cli.py`).
Confirmed: every function this runner calls (`scan_file`, `cmd_check`, `cmd_scan`,
`log_open_lint.main(argv)`) is a **pure function that never calls `sys.exit()`** -- only each
script's own `if __name__ == "__main__":` guard does, which this runner never reaches (CTO
condition 2, the sys.exit/SystemExit hazard). No import-time side effects were found in any of
the 5 modules (module-level code is limited to constant/regex/dataclass definitions -- no I/O,
no network, no mutation). This was independently re-verified by importing the runner with
stdout/stderr temporarily replaced by `io.StringIO` and confirming zero output on import.

Rather than reimplement each check's output formatting (high parity risk), the runner calls
the EXACT SAME function the CLI does, with a lightweight `SimpleNamespace`/argv standing in for
argparse's `Namespace` -- so the printed output is byte-identical by construction, not by
careful reproduction.

## Parity verification (CTO condition 1, non-negotiable bar)

Built a before/after fixture set and ran BOTH gates against each fixture, comparing exit code
+ full byte-for-byte output (`cmp -s`), per the TO's required matrix (all-pass, each-check-
fails-alone, multi-fail):

| Fixture | Trigger | old_rc | new_rc | Output |
|---|---|---|---|---|
| all-pass (commit_gate_runner.py itself) | clean file | 0 | 0 | IDENTICAL |
| f_syntax | py_compile SyntaxError | 1 | 1 | IDENTICAL |
| f_undefined | ds-precommit-check undefined name | 1 | 1 | IDENTICAL |
| f_ruff | ruff F401 unused import | 1 | 1 | IDENTICAL |
| f_constants | comp-constants FIRM_ID drift (3 sites) | 1 | 1 | IDENTICAL |
| f_logopen | log-open-lint strict-utf8 no errors= | 1 | 1 | IDENTICAL |
| f_multi | undefined-name + ruff together (fail-fast on the FIRST reached check) | 1 | 1 | IDENTICAL |
| f_shell.sh | comp-shell unguarded `pgrep` (.tools/-scoped) | 1 | 1 | IDENTICAL |
| f_manifest_advisory | manifest_check ADVISORY finding (non-blocking, mode=advisory in live config) | 0 | 0 | IDENTICAL |

**3 real bugs the fixtures caught and fixed (not hypothetical -- each one failed before the
fix, passed after):**
1. **py_compile print-order bug:** wrapper printed "BLOCKED: ..." BEFORE the exception's own
   traceback text, reversed vs bash's `subprocess-prints-then-wrapper-echoes` sequence. Fixed
   by swapping the print order.
2. **stdout/stderr interleaving:** Python defaults to FULLY buffered stdout when not attached
   to a TTY (every real caller of this gate). A long-lived process's buffered stdout writes
   could appear AFTER later stderr writes when both streams are merged (`2>&1`), even though
   emitted in the correct order -- an artifact that doesn't exist in the old per-subprocess-
   per-check design (each subprocess's stdio flushes fresh at process exit). Fixed with
   `line_buffering=True` on both streams.
3. **Windows CRLF-translation scope bug:** text re-emitted FROM an imported check (e.g.
   `py_compile`'s own traceback, `comp_constants_cli.cmd_check`'s captured stdout) must keep
   Python's default CRLF-on-Windows translation (matching what a REAL subprocess would have
   written) -- but THIS wrapper's own bash-`echo`-equivalent lines must stay bare-LF (bash's
   `echo` never CRLF-translates). Conflating the two (or forcing `newline='\n'` globally) broke
   parity in both directions until a `_echo()` helper (raw `.buffer.write`, bypassing
   translation) was split out for wrapper-only lines. Also found bash's `_cc_out=$(...)` in the
   original comp-constants check strips exactly one trailing newline before `echo "$_cc_out"`
   re-adds one bare-LF one -- replicated that exact two-step behavior (CRLF on every embedded
   line, bare-LF on the final one) once the pattern was understood from the byte-level diff.

None of these three were assumed away -- each was caught by an actual `cmp -s` failure against
a real subprocess run of the OLD script, then root-caused via `od -c`/`cat -A` byte inspection,
not guessed.

## Compiler Tools

| Tool | Use | Result vs `<expect>` |
|---|---|---|
| `comp-blast ds-commit-gate.sh` (Phase 1) | enumerate every caller before rename | NOT-FOUND ("no graph node matches 'ds-commit-gate.sh'") -- comp-blast does not resolve shell-script callers (matches the TO's own documented fallback path). Fell back to comp-grep per the TO's `<if_mismatch>`. |
| `comp-grep "ds-commit-gate" .` (Phase 1) | full reference discovery | 210-line hit list across ~70 files -- superset of the TO's preliminary list (which named CLAUDE.md, 4 SKILL.md, commit-worker.sh, gold_validate_config.yaml x2, "several docs files"). Categorized into LIVE (must-update) vs HISTORICAL (deliberately excluded: 35 dated docs/briefs/*.md, 5 CHANGELOG.json deploy-history logs, org/compiler-tools-log.md, 2 point-in-time deploy-note references) -- see the two rename commits' messages for the full reasoning. |
| Before/after parity test matrix (Phase 2) | identical pass/fail + attribution across all-pass / each-check-alone / multi-fail | PASS -- all 9 fixtures `cmp -s` byte-identical + matching exit codes, after fixing the 3 real bugs the fixtures caught (see above). Full test commands + outputs are in this log body, not summarized-away. |
| `py_compile` + standalone import of `commit_gate_runner` (Phase 2) | confirm no import-time side effects | Initially crashed under an `io.StringIO`-redirected import (`sys.stdout.reconfigure` AttributeError) -- a real fragility (not a functional bug in the actual subprocess-invoked path, but a legitimate defensive gap). Fixed with `contextlib.suppress(AttributeError)` around both reconfigure calls; re-verified clean import (`IMPORT_STDOUT: ''`, `IMPORT_STDERR: ''`) AND re-ran the parity matrix post-fix to confirm no regression (PASS). |
| `comp-grep "ds-commit-gate" .` (Phase 3, re-run) | zero stale references | 0 hits outside: (a) the deliberately-excluded historical categories (unchanged from Phase 1's categorization), (b) 2 files routed to CTO (CLAUDE.md, 17 docs/architecture/*.md + 2 _drafts -- ANY_CTO/BASE_EXEC lane, owned-paths-blocked for AE, edited in working tree + MCP'd to CTO), (c) 2 files routed to DS (gold_validate_config.yaml x2, POD4 lane, same pattern), (d) this runner's own + CLAUDE.md's deliberate explanatory self-references naming the OLD string as history (not stale pointers -- e.g. "renamed off ds-commit-gate.sh 2026-07-07"). |
| `comp-iam gaps` | n/a this TO -- no new IAM/AWS resource, pure local file consolidation + rename | N/A, correctly not run |

## Files Modified

- `.tools/commit_gate_runner.py` (new) -- the consolidated single-process runner.
- `.tools/commit-gate.sh` (new) -- thin wrapper (path resolution + `exec python
  commit_gate_runner.py "$@"`), replaces `.tools/ds-commit-gate.sh` (deleted).
- `.claude/settings.json`, `.claude/skills/{cloud-ops,freeform,gold-runner-code-review,work}/
  SKILL.md`, `.tools/commit-worker.sh`, `.tools/freeform.sh`, `data/canonical/schwab/docs/
  08_GOLD_SCOPE.md`, `data/cot/scripts/gold/README_FIRM_NATIVE_DIVERGENCE.md`, `data/find/imo/
  README.md` + 2 test `.py` files -- rename references updated (commits `3ebdcf9bf`, `b7f1dce45`).

## Blockers (routed, not stranded)

- **CTO lane:** CLAUDE.md Rule 14 + 17 `docs/architecture/*.md` + 2 `_drafts` briefs --
  owned-paths-blocked for AE (`ANY_CTO`/`BASE_EXEC`), discovered only at safe-commit time (I'd
  checked the general `docs/**` catch-all but missed the more specific `docs/architecture/**`
  override -- longest-match, not first-match). Edited correctly in my working tree; MCP'd to
  1.0.0_SA_CTO with the exact file list + substitution pattern.
- **DS lane (POD4):** `data/{black_diamond,inf}/scripts/gold/gold_validate_config.yaml` -- same
  pattern, edited + MCP'd to 0.4.0_DS_ClientPlatform.

## Current State (zero-context handoff)

`.tools/commit-gate.sh` is the live universal pre-commit gate as of commit `b7f1dce45`
(pushed). `ds-commit-gate.sh` no longer exists. `.claude/settings.json`'s Bash permission
allowlist already covers `commit-gate.sh*` / `.tools/commit-gate.sh*` (the old entries were
replaced, not left stale). Parity is proven via a 9-case fixture matrix (not asserted) and 3
real bugs were caught + fixed by that matrix, not assumed away.

## Next Steps

- [1.0.0_SA_CTO] land the 19 routed docs/CLAUDE.md rename references (exact list + pattern in
  the MCP message 155844Z).
- [0.4.0_DS_ClientPlatform] land the 2 routed gold_validate_config.yaml comment fixes
  (low-pri, MCP 155857Z).
- [2.0.0_SA_COO] TO-ready-for-close (all 4 acceptance criteria met) -- RAVC sent; the TO lives
  in your task_orders/ (ANY_EXEC lane), status flip drafted in my working tree, not committed
  by me.
- Per COO's sequencing: NFRA_CMTQUE.TO-6R's load-test can now proceed against the corrected
  (consolidated) commit-gate design.
