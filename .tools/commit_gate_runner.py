#!/usr/bin/env python3
"""ADHC_COMMITGATE -- consolidated commit-gate runner (ONE python process, not ~6 forks/file).

Replaces .tools/ds-commit-gate.sh's per-file loop of 6 forked python subprocesses
(py_compile, ds-precommit-check.py, ruff, comp_constants_cli.py, manifest_check_cli.py,
log_open_lint.py) with direct in-process calls to the SAME functions each of those scripts'
own CLI wrapper calls -- not a reimplementation of their checks or their output formatting.

WHY THIS IS SAFE FOR PARITY (CTO condition 1): every check below calls the exact same
function the standalone CLI calls (scan_file / cmd_check / cmd_scan / main(argv=[...])) --
none of these inner functions call sys.exit() themselves (confirmed by reading all 5
source scripts; only each script's OWN `if __name__ == "__main__":` guard calls
sys.exit(), which this runner never reaches). So there is no SystemExit to catch and no
import-time side effect to worry about (CTO condition 2) -- this was verified by reading
every one of the 5 scripts top-to-bottom before writing this file, not assumed.

RUFF STAYS A SUBPROCESS (one per file, unchanged from today): the `ruff` PyPI package is a
compiled Rust binary with no stable public Python API for programmatic checks (only a CLI
entry point) -- importing its internal bindings would be fragile and version-coupled against
the CLAUDE.md-pinned ruff==0.15.11 contract. py_compile IS trivially importable (stdlib) and
is consolidated here rather than kept as a subprocess (better than ADHC_COMMITGATE's own
"py_compile may stay distinct if consolidating it isn't straightforward" allowance).

ORDER PRESERVED EXACTLY (per-file, per-check, fail-fast) to guarantee identical pass/fail +
output vs today's gate: py_compile -> ds-precommit-check -> ruff -> comp-constants ->
comp-manifest-check -> log-open-lint for .py; comp-shell (in-scope only) -> comp-manifest-check
for .sh. The first failing check on a file BLOCKS immediately (matching the bash `|| exit 1`
chain) -- files after a blocked file are never reached, exactly as today.

Usage: python .tools/commit_gate_runner.py <file1> [file2 ...]
Exit 0 on clean; exit 1 on the first blocking failure (message on stderr, same text as today).
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import py_compile
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

# Force line-buffering (Python defaults to FULLY buffered when not attached to a TTY, e.g.
# redirected to a file/pipe -- as every real caller of this gate does). Without this, stdout
# writes from the in-process checks (cmd_check/cmd_scan/log_open_lint's own prints) can
# appear AFTER later stderr writes when both streams are merged (2>&1), even though this
# script emits them in the correct order -- an interleaving artifact that does NOT occur
# with today's one-subprocess-per-check design (each subprocess's own stdio is freshly
# flushed at process exit). Verified via the before/after parity fixture set (ADHC_COMMITGATE
# requirement 3) -- this fix was REQUIRED, not precautionary. Newline translation is
# DELIBERATELY left at Python's default (CRLF on Windows) here: text re-emitted from an
# imported check (py_compile's own traceback text, cmd_check's captured stdout, ...) must
# look exactly like a real `python some_script.py` subprocess wrote it -- which is what the
# parity baseline actually does on this platform. `_echo()` below is the separate path for
# THIS wrapper's own bash-`echo`-equivalent lines, which must stay bare-LF (bash's echo does
# not CRLF-translate) -- conflating the two was an earlier bug caught by the parity fixtures.
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)


def _echo(msg: str, stream) -> None:
    """Write msg + bare LF, bypassing the stream's platform newline translation --
    matches bash's `echo ... [>&2]` exactly (never CRLF, unlike a python subprocess's
    default text-mode stdout on Windows). Use this ONLY for this wrapper's own
    ds-commit-gate-equivalent messages, never for text re-emitted from an imported check."""
    stream.flush()
    stream.buffer.write((msg + "\n").encode("utf-8"))
    stream.buffer.flush()


SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE = SCRIPT_DIR.parent
GRAPH_DIR = WORKSPACE / "org" / "modules" / "graph"
COMPPROOF_DIR = GRAPH_DIR / "compproof"

# ds-precommit-check.py has a hyphenated filename -- not a valid `import` identifier,
# so it's loaded via importlib.util (standard technique for a non-module-name .py path).
def _load_hyphenated(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

ds_precommit_check = _load_hyphenated("ds_precommit_check", SCRIPT_DIR / "ds-precommit-check.py")

for _p in (str(GRAPH_DIR), str(COMPPROOF_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import comp_constants_cli   # noqa: E402
import manifest_check_cli   # noqa: E402
import shell_cli            # noqa: E402
import log_open_lint        # noqa: E402

# Rule-16 in-scope path prefixes for the shell scan (mirrors ds-commit-gate.sh _SHELL_SCOPE).
_SHELL_SCOPE = (".tools/", "org/mcp/", "org/threads/", "infra/aws/lambda/ci/", "infra/aws/terraform/")


def _shell_in_scope(f: str) -> bool:
    try:
        rel = os.path.relpath(f, WORKSPACE).replace("\\", "/")
    except ValueError:
        rel = f
    return any(rel.startswith(prefix) for prefix in _SHELL_SCOPE)


def _run_ruff(f: str) -> int:
    """The one subprocess this runner still shells out to (no stable ruff Python API)."""
    proc = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--target-version", "py39", "--extend-select", "FA", f],
        cwd=str(WORKSPACE),
    )
    return proc.returncode


def _comp_constants_check(f: str, config: dict) -> int:
    """Mirrors `comp_constants_cli.py check --file <f>` exactly (same function, same args
    shape) -- captures stdout so a BLOCK can echo it after the wrapper message, matching
    bash's `_cc_out=$(...) || { echo BLOCKED; echo "$_cc_out"; }` (silent on success)."""
    ns = SimpleNamespace(file=f, lane=None)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = comp_constants_cli.cmd_check(ns, config)
    if rc != 0:
        _echo(f"BLOCKED: comp-constants drift detected on {f}", sys.stderr)
        # Re-emitted cmd_check output. bash's `_cc_out=$(...)` strips the subprocess's
        # trailing newline (POSIX command-substitution semantics), then `echo "$_cc_out"`
        # re-appends exactly one bare-LF -- so every EMBEDDED line keeps the subprocess's
        # own CRLF (print(), default translation) but the final line ends bare-LF (_echo's
        # raw write), matching that two-step bash behavior exactly (parity-fixture-caught).
        content = buf.getvalue()
        if content.endswith("\n"):
            content = content[:-1]
        print(content, file=sys.stderr, end="")
        _echo("", sys.stderr)
        return 1
    return 0


def _manifest_check_one(f: str) -> int:
    """Mirrors `manifest_check_cli.py check --file <f>` exactly (blocking only on an
    ERROR-class finding in blocking mode, per that script's own config-driven mode)."""
    ns = SimpleNamespace(file=[f], mode=None)
    rc = manifest_check_cli.cmd_check(ns)
    if rc == 1:
        _echo(f"BLOCKED: comp-manifest-check flagged non-canonical graph access in {f} (blocking mode)", sys.stderr)
        return 1
    return 0


def _log_open_lint_one(f: str) -> int:
    """Mirrors `log_open_lint.py <f>` (no --advisory flag, matching today's non-blocking-off
    invocation) including its own crash-fail-open guard (CTO safeguard 2, replicated here
    since we call main() directly rather than through its `if __name__` top-level guard)."""
    try:
        rc = log_open_lint.main([f])
    except Exception as e:  # noqa: BLE001 -- crash-fail-open, mirrors log_open_lint's own __main__ guard
        _echo(f"WARN (log-open-lint): unexpected error -- failing open, not blocking: {e!r}", sys.stderr)
        rc = 0
    if rc == 1:
        _echo(
            f"BLOCKED: strict-utf8 log read without errors= in {f} -- add errors=\"replace\", or an "
            f"audited '# log-open-ok: <reason>' override. This is the class that bricked COMPLEARN "
            f"corpus load fabric-wide (2026-07).",
            sys.stderr,
        )
        return 1
    return 0


def _shell_scan_one(f: str) -> int:
    """Mirrors `shell_cli.py scan <f>` exactly (same cmd_scan function -> identical printed
    findings/summary), then the wrapper's own BLOCKED line on an ERROR-class finding."""
    ns = SimpleNamespace(paths=[f], all=False, guard_lookback=shell_cli.GUARD_LOOKBACK_DEFAULT)
    rc = shell_cli.cmd_scan(ns)
    if rc != 0:
        _echo(f"BLOCKED: comp-shell found ERROR-level forbidden utility in {f}", sys.stderr)
        return 1
    return 0


def process_files(files: list[str]) -> int:
    checked = 0
    # comp-constants config loaded ONCE (read-only; re-reading it per file, like the
    # original per-file subprocess did, would be safe too, but this cheap in-process
    # optimization changes nothing observable -- cmd_check never mutates it).
    cc_config = comp_constants_cli._load_config(comp_constants_cli.DEFAULT_CONFIG_PATH)

    for f in files:
        if f.endswith(".py"):
            try:
                py_compile.compile(f, doraise=True)
            except py_compile.PyCompileError as e:
                # order matters for parity: py_compile's OWN traceback prints first (as it
                # would mid-subprocess in the original), the wrapper's BLOCKED line after.
                # print() (not _echo) for e's own text -- matches a real subprocess's
                # default-CRLF-on-Windows traceback text; _echo for the wrapper's own line.
                print(str(e), file=sys.stderr, end="")  # str(e) already ends in '\n'
                _echo(f"BLOCKED: py_compile failed on {f}", sys.stderr)
                return 1

            rc = ds_precommit_check.scan_file(f, verbose=False, strict=False)
            if rc != 0:
                _echo(f"BLOCKED: undefined-name scan failed on {f}", sys.stderr)
                return 1

            rc = _run_ruff(f)
            if rc != 0:
                _echo(f"BLOCKED: ruff check failed on {f}", sys.stderr)
                return 1

            if _comp_constants_check(f, cc_config) != 0:
                return 1

            if _manifest_check_one(f) != 0:
                return 1

            if _log_open_lint_one(f) != 0:
                return 1

            checked += 1

        elif f.endswith(".sh"):
            if _shell_in_scope(f):
                if _shell_scan_one(f) != 0:
                    return 1
                checked += 1

            # manifest-check runs on ALL .sh regardless of Rule-16 scope (mirrors bash:
            # this call sits OUTSIDE the _shell_in_scope block) -- does NOT bump `checked`.
            if _manifest_check_one(f) != 0:
                return 1
        else:
            continue

    _echo(f"OK: pre-commit gate clean for {checked} file(s)", sys.stdout)
    return 0


def main() -> int:
    files = sys.argv[1:]
    return process_files(files)


if __name__ == "__main__":
    sys.exit(main())
